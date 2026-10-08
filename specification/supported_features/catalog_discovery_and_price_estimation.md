# Catalog Discovery and Price Estimation

> **Note:** Placeholder for the content in #2595. The sections below are added to it.

## Directly Dependent Columns

* [SkuPrice](#datamodel.skuprice)
  * CommitmentApplicability

## Example SQL Queries

### Identify the Usage a Commitment Covers

This query answers which usage the [*commitment discounts*](#glossary:commitment-discount) offered under a service cover, and what that usage costs with and without them. It takes a service provider, the Pricing Service Name under which the commitments are purchased, and a point in time. For each commitment purchase record and each usage SKU Price it covers, it returns the list and contracted unit prices of the usage, and the effective unit prices that follow from the coverage:

* **List Unit Price:** the Unit Price of the "List" record of the usage.
* **Contracted Unit Price:** the Unit Price of a "Contracted" record of the usage, one row per *contract*. Without a "Contracted" record, it defaults to the List Unit Price.
* **Effective List Unit Price and Effective Contracted Unit Price:**
  * `Factor`: the Unit Price of the purchase record spread over the hours of its term, multiplied by `Factor`, for both.
  * `Discount`: the List Unit Price and the Contracted Unit Price, each reduced by `Discount`.
  * `UnitPrice`: the published unit price, for both.

This query uses BigQuery Standard SQL JSON functions (e.g., `JSON_VALUE`, `JSON_QUERY`, `JSON_EXTRACT_ARRAY`, `JSON_VALUE_ARRAY`, `UNNEST`). All major SQL engines have similar functions.

> **Note:** This query evaluates only inclusion rules whose `Dimension` is `SkuId`, `SkuPriceId`, `PricingServiceName`, `PricingRegionId`, or `RegionId` (compared with Pricing Region ID) and whose `Operator` is `In` or `StartsWith`. It does not check `Exclusions`, and it skips purchase records flagged `IsComplexScope`. It considers "List" purchase records only, and usage records in the Pricing Currency of the purchase. A `Factor` is converted to an hourly price only for usage priced in "Hours" and a Purchase Duration Type of "1 Year" or "3 Years", and only when the purchase record's Unit Price carries the whole obligation of the purchase. Effective unit prices assume the *commitment discount* is fully used.

```sql
WITH Commitment AS (
  SELECT
    SkuPriceId AS CommitmentSkuPriceId,
    ChargeCategory AS CommitmentChargeCategory,
    CommitmentDiscountCategory,
    PurchaseDurationType,
    PurchasePaymentModel,
    PricingCurrency AS CommitmentCurrency,
    UnitPrice AS CommitmentUnitPrice,
    CommitmentApplicability
  FROM SkuPrice
  WHERE ServiceProviderName = ?
    AND PricingServiceName = ?
    AND ChargeCategory = 'Purchase'
    AND UnitPriceType = 'List'
    AND CommitmentApplicability IS NOT NULL
    AND COALESCE(JSON_VALUE(CommitmentApplicability, '$.IsComplexScope'), 'false') <> 'true'
    AND (SkuPriceEffectiveStart IS NULL OR SkuPriceEffectiveStart <= ?)
    AND (SkuPriceEffectiveEnd IS NULL OR SkuPriceEffectiveEnd > ?)
),
UsagePrice AS (
  SELECT
    ServiceProviderName,
    ChargeCategory,
    SkuId,
    SkuPriceId,
    PricingServiceName,
    PricingRegionId,
    PricingUnit,
    PricingCurrency,
    ContractId,
    UnitPriceType,
    UnitPrice
  FROM SkuPrice
  WHERE ServiceProviderName = ?
    AND ChargeCategory = 'Usage'
    AND (SkuPriceEffectiveStart IS NULL OR SkuPriceEffectiveStart <= ?)
    AND (SkuPriceEffectiveEnd IS NULL OR SkuPriceEffectiveEnd > ?)
),
Usage AS (
  SELECT
    L.ChargeCategory,
    L.SkuId,
    L.SkuPriceId,
    L.PricingServiceName,
    L.PricingRegionId,
    L.PricingUnit,
    L.PricingCurrency,
    K.ContractId,
    L.UnitPrice AS ListUnitPrice,
    COALESCE(K.UnitPrice, L.UnitPrice) AS ContractedUnitPrice
  FROM UsagePrice AS L
  LEFT JOIN UsagePrice AS K
    ON K.SkuPriceId = L.SkuPriceId
    AND K.PricingCurrency = L.PricingCurrency
    AND K.UnitPriceType = 'Contracted'
  WHERE L.UnitPriceType = 'List'
),
RuleTarget AS (
  SELECT
    C.*,
    U.*,
    RuleOrder,
    InclusionRule,
    JSON_VALUE(InclusionRule, '$.Operator') AS Operator,
    JSON_VALUE_ARRAY(InclusionRule, '$.Values') AS RuleValues,
    CASE JSON_VALUE(InclusionRule, '$.Dimension')
      WHEN 'SkuId' THEN U.SkuId
      WHEN 'SkuPriceId' THEN U.SkuPriceId
      WHEN 'PricingServiceName' THEN U.PricingServiceName
      WHEN 'PricingRegionId' THEN U.PricingRegionId
      WHEN 'RegionId' THEN U.PricingRegionId
    END AS Target
  FROM Commitment AS C
  JOIN Usage AS U
    ON U.PricingCurrency = C.CommitmentCurrency
  LEFT JOIN UNNEST(JSON_EXTRACT_ARRAY(C.CommitmentApplicability, '$.Inclusions')) AS InclusionRule
    WITH OFFSET AS RuleOrder
),
RuleMatch AS (
  SELECT
    *,
    CASE Operator
      WHEN 'In' THEN Target IN UNNEST(RuleValues) OR '*' IN UNNEST(RuleValues)
      WHEN 'StartsWith' THEN EXISTS (
        SELECT 1 FROM UNNEST(RuleValues) AS RuleValue WHERE STARTS_WITH(Target, RuleValue)
      )
      ELSE FALSE
    END AS IsMatch
  FROM RuleTarget
),
Covered AS (
  SELECT
    CommitmentSkuPriceId,
    CommitmentChargeCategory,
    CommitmentDiscountCategory,
    PurchaseDurationType,
    PurchasePaymentModel,
    CommitmentUnitPrice,
    ChargeCategory,
    SkuId,
    SkuPriceId,
    PricingUnit,
    PricingCurrency,
    ContractId,
    ListUnitPrice,
    ContractedUnitPrice,
    CASE
      WHEN JSON_VALUE(ANY_VALUE(CommitmentApplicability), '$.IsGlobalScope') = 'true'
        THEN JSON_QUERY(ANY_VALUE(CommitmentApplicability), '$.Coverage')
      WHEN JSON_VALUE(ANY_VALUE(CommitmentApplicability), '$.InclusionOperator') = 'And'
        AND LOGICAL_AND(COALESCE(IsMatch, FALSE))
        THEN JSON_QUERY(ANY_VALUE(CommitmentApplicability), '$.Coverage')
      WHEN JSON_VALUE(ANY_VALUE(CommitmentApplicability), '$.InclusionOperator') = 'Or'
        THEN ARRAY_AGG(
          IF(IsMatch, COALESCE(JSON_QUERY(InclusionRule, '$.Coverage'), JSON_QUERY(CommitmentApplicability, '$.Coverage')), NULL)
          IGNORE NULLS ORDER BY RuleOrder LIMIT 1
        )[SAFE_OFFSET(0)]
    END AS Coverage
  FROM RuleMatch
  GROUP BY
    CommitmentSkuPriceId,
    CommitmentChargeCategory,
    CommitmentDiscountCategory,
    PurchaseDurationType,
    PurchasePaymentModel,
    CommitmentUnitPrice,
    ChargeCategory,
    SkuId,
    SkuPriceId,
    PricingUnit,
    PricingCurrency,
    ContractId,
    ListUnitPrice,
    ContractedUnitPrice
),
Effective AS (
  SELECT
    *,
    CASE
      WHEN JSON_VALUE(Coverage, '$.UnitPrice') IS NOT NULL
        THEN CAST(JSON_VALUE(Coverage, '$.UnitPrice') AS NUMERIC)
      WHEN JSON_VALUE(Coverage, '$.Discount') IS NOT NULL
        THEN ROUND(ListUnitPrice * (1 - CAST(JSON_VALUE(Coverage, '$.Discount') AS NUMERIC)), 6)
      WHEN JSON_VALUE(Coverage, '$.Factor') IS NOT NULL AND PricingUnit = 'Hours'
        THEN ROUND(
          CommitmentUnitPrice * CAST(JSON_VALUE(Coverage, '$.Factor') AS NUMERIC)
          / CASE PurchaseDurationType WHEN '1 Year' THEN 8760 WHEN '3 Years' THEN 26280 END,
          6)
    END AS EffectiveListUnitPrice
  FROM Covered
  WHERE Coverage IS NOT NULL
)
SELECT
  CommitmentSkuPriceId,
  CommitmentChargeCategory,
  CommitmentDiscountCategory,
  PurchaseDurationType,
  PurchasePaymentModel,
  Coverage,
  ChargeCategory,
  SkuId,
  SkuPriceId,
  PricingCurrency,
  ContractId,
  ListUnitPrice,
  ContractedUnitPrice,
  EffectiveListUnitPrice,
  CASE
    WHEN JSON_VALUE(Coverage, '$.Discount') IS NOT NULL
      THEN ROUND(ContractedUnitPrice * (1 - CAST(JSON_VALUE(Coverage, '$.Discount') AS NUMERIC)), 6)
    ELSE EffectiveListUnitPrice
  END AS EffectiveContractedUnitPrice
FROM Effective
ORDER BY CommitmentSkuPriceId, SkuId, SkuPriceId, ContractId
```

In the [SKU Price examples](#appendix.examples:skuprice), the commitments offered under "Aura Web Compute" are the one-year reservation and the flexible spend plan. The reservation covers the standard virtual machine, whose List Unit Price of 0.384000 and Contracted Unit Price of 0.326400 per hour both become 0.216164, 0.228174, or 0.240183 per hour for "All Upfront", "Partial Upfront", and "No Upfront", respectively. The spend plan covers the standard, burstable, and shared-core virtual machines at 28 percent off their unit prices, for example 0.276480 per hour from the List Unit Price and 0.235008 per hour from the Contracted Unit Price of the standard virtual machine.

### Derive the Effective Unit Price of a SKU Under Each Commitment

This query answers what one unit of a *SKU* costs under each *commitment discount* that covers it, so that the purchase options for that *SKU* can be ranked by the price they lead to. It takes a service provider, the SKU Price ID of a usage record, and a point in time. For each commitment purchase record whose Commitment Applicability covers the usage record, it returns the coverage and the effective unit price that follows from it:

* **`UnitPrice`:** the published unit price of covered usage.
* **`Discount`:** the Unit Price of the "List" usage record, in the same Pricing Currency as the purchase, reduced by `Discount`.
* **`Factor`:** the Unit Price of the purchase record spread over the hours of its term, multiplied by `Factor`.

This query uses BigQuery Standard SQL JSON functions (e.g., `JSON_VALUE`, `JSON_QUERY`, `JSON_EXTRACT_ARRAY`, `JSON_VALUE_ARRAY`, `UNNEST`). All major SQL engines have similar functions.

> **Note:** This query evaluates only inclusion rules whose `Dimension` is `SkuId`, `SkuPriceId`, `PricingServiceName`, `PricingRegionId`, or `RegionId` (compared with Pricing Region ID) and whose `Operator` is `In` or `StartsWith`. It does not check `Exclusions`, and it skips purchase records flagged `IsComplexScope`. A `Factor` is converted to an hourly price only for a usage record priced in "Hours" and a Purchase Duration Type of "1 Year" or "3 Years", and only when the purchase record's Unit Price carries the whole obligation of the purchase. The effective unit price assumes the *commitment discount* is fully used.

```sql
WITH UsagePrice AS (
  SELECT
    ChargeCategory,
    SkuId,
    SkuPriceId,
    PricingServiceName,
    PricingRegionId,
    PricingUnit,
    PricingCurrency,
    ContractId,
    UnitPriceType,
    UnitPrice
  FROM SkuPrice
  WHERE ServiceProviderName = ?
    AND SkuPriceId = ?
    AND ChargeCategory = 'Usage'
    AND (SkuPriceEffectiveStart IS NULL OR SkuPriceEffectiveStart <= ?)
    AND (SkuPriceEffectiveEnd IS NULL OR SkuPriceEffectiveEnd > ?)
),
UsageSku AS (
  SELECT DISTINCT ChargeCategory AS UsageChargeCategory, SkuId, SkuPriceId, PricingServiceName, PricingRegionId, PricingUnit
  FROM UsagePrice
),
Commitment AS (
  SELECT
    SkuPriceId AS CommitmentSkuPriceId,
    ChargeCategory AS CommitmentChargeCategory,
    ContractId AS CommitmentContractId,
    CommitmentDiscountCategory,
    PurchaseDurationType,
    PurchasePaymentModel,
    PricingCurrency AS CommitmentCurrency,
    UnitPrice AS CommitmentUnitPrice,
    CommitmentApplicability
  FROM SkuPrice
  WHERE ServiceProviderName = ?
    AND ChargeCategory = 'Purchase'
    AND CommitmentApplicability IS NOT NULL
    AND COALESCE(JSON_VALUE(CommitmentApplicability, '$.IsComplexScope'), 'false') <> 'true'
    AND (SkuPriceEffectiveStart IS NULL OR SkuPriceEffectiveStart <= ?)
    AND (SkuPriceEffectiveEnd IS NULL OR SkuPriceEffectiveEnd > ?)
),
RuleTarget AS (
  SELECT
    C.*,
    U.UsageChargeCategory,
    U.SkuId,
    U.SkuPriceId,
    U.PricingUnit,
    RuleOrder,
    InclusionRule,
    JSON_VALUE(InclusionRule, '$.Operator') AS Operator,
    JSON_VALUE_ARRAY(InclusionRule, '$.Values') AS RuleValues,
    CASE JSON_VALUE(InclusionRule, '$.Dimension')
      WHEN 'SkuId' THEN U.SkuId
      WHEN 'SkuPriceId' THEN U.SkuPriceId
      WHEN 'PricingServiceName' THEN U.PricingServiceName
      WHEN 'PricingRegionId' THEN U.PricingRegionId
      WHEN 'RegionId' THEN U.PricingRegionId
    END AS Target
  FROM Commitment AS C
  CROSS JOIN UsageSku AS U
  LEFT JOIN UNNEST(JSON_EXTRACT_ARRAY(C.CommitmentApplicability, '$.Inclusions')) AS InclusionRule
    WITH OFFSET AS RuleOrder
),
RuleMatch AS (
  SELECT
    *,
    CASE Operator
      WHEN 'In' THEN Target IN UNNEST(RuleValues) OR '*' IN UNNEST(RuleValues)
      WHEN 'StartsWith' THEN EXISTS (
        SELECT 1 FROM UNNEST(RuleValues) AS RuleValue WHERE STARTS_WITH(Target, RuleValue)
      )
      ELSE FALSE
    END AS IsMatch
  FROM RuleTarget
),
Covered AS (
  SELECT
    CommitmentSkuPriceId,
    CommitmentChargeCategory,
    UsageChargeCategory,
    SkuPriceId,
    CommitmentContractId,
    CommitmentDiscountCategory,
    PurchaseDurationType,
    PurchasePaymentModel,
    CommitmentCurrency,
    CommitmentUnitPrice,
    PricingUnit,
    CASE
      WHEN JSON_VALUE(ANY_VALUE(CommitmentApplicability), '$.IsGlobalScope') = 'true'
        THEN JSON_QUERY(ANY_VALUE(CommitmentApplicability), '$.Coverage')
      WHEN JSON_VALUE(ANY_VALUE(CommitmentApplicability), '$.InclusionOperator') = 'And'
        AND LOGICAL_AND(COALESCE(IsMatch, FALSE))
        THEN JSON_QUERY(ANY_VALUE(CommitmentApplicability), '$.Coverage')
      WHEN JSON_VALUE(ANY_VALUE(CommitmentApplicability), '$.InclusionOperator') = 'Or'
        THEN ARRAY_AGG(
          IF(IsMatch, COALESCE(JSON_QUERY(InclusionRule, '$.Coverage'), JSON_QUERY(CommitmentApplicability, '$.Coverage')), NULL)
          IGNORE NULLS ORDER BY RuleOrder LIMIT 1
        )[SAFE_OFFSET(0)]
    END AS Coverage
  FROM RuleMatch
  GROUP BY
    CommitmentSkuPriceId,
    CommitmentChargeCategory,
    UsageChargeCategory,
    SkuPriceId,
    CommitmentContractId,
    CommitmentDiscountCategory,
    PurchaseDurationType,
    PurchasePaymentModel,
    CommitmentCurrency,
    CommitmentUnitPrice,
    PricingUnit
)
SELECT
  CV.SkuPriceId,
  CV.UsageChargeCategory,
  CV.CommitmentSkuPriceId,
  CV.CommitmentChargeCategory,
  CV.CommitmentContractId,
  CV.CommitmentDiscountCategory,
  CV.PurchaseDurationType,
  CV.PurchasePaymentModel,
  CV.Coverage,
  CASE
    WHEN JSON_VALUE(CV.Coverage, '$.UnitPrice') IS NOT NULL
      THEN CAST(JSON_VALUE(CV.Coverage, '$.UnitPrice') AS NUMERIC)
    WHEN JSON_VALUE(CV.Coverage, '$.Discount') IS NOT NULL
      THEN ROUND(B.UnitPrice * (1 - CAST(JSON_VALUE(CV.Coverage, '$.Discount') AS NUMERIC)), 6)
    WHEN JSON_VALUE(CV.Coverage, '$.Factor') IS NOT NULL AND CV.PricingUnit = 'Hours'
      THEN ROUND(
        CV.CommitmentUnitPrice * CAST(JSON_VALUE(CV.Coverage, '$.Factor') AS NUMERIC)
        / CASE CV.PurchaseDurationType WHEN '1 Year' THEN 8760 WHEN '3 Years' THEN 26280 END,
        6)
  END AS EffectiveUnitPrice,
  CV.CommitmentCurrency AS PricingCurrency
FROM Covered AS CV
LEFT JOIN UsagePrice AS B
  ON B.UnitPriceType = 'List'
  AND B.PricingCurrency = CV.CommitmentCurrency
WHERE CV.Coverage IS NOT NULL
ORDER BY EffectiveUnitPrice, CV.CommitmentSkuPriceId
```

In the [SKU Price examples](#appendix.examples:skuprice), the on-demand rate of the standard virtual machine is 0.384000 per hour. Under the one-year reservation, its effective unit price is 0.216164, 0.228174, or 0.240183 per hour for "All Upfront", "Partial Upfront", and "No Upfront", respectively. Under the flexible spend plan, it is 0.276480 per hour for every payment model.

## Version Introduced

1.5
