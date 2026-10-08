# Rate Optimization and Contract Evaluation

## Description

> **Note:** Placeholder for the content of this section in #2595.

### When Public and Negotiated Records are Paired

> **Note:** Placeholder for the content of this section in #2595.

### Reading SKU Price ID and the Effective Date Columns

> **Note:** Placeholder for the content of this section in #2595.

### Scope When Conditional Columns are Absent

> **Note:** Placeholder for the content of this section in #2595.

## Directly Dependent Columns

> **Note:** Placeholder for the list in #2595. This PR adds the following column.

* [SkuPrice](#datamodel.skuprice)
  * CommitmentApplicability

## Supporting Columns

> **Note:** Placeholder for the list in #2595.

## Example SQL Queries

> **Note:** Placeholder for the content of this section in #2595.

### Measure What Negotiation Reduces the Rate By

> **Note:** Placeholder for the content of this section in #2595.

### Compare Public and Negotiated Prices at a Given Quantity

> **Note:** Placeholder for the content of this section in #2595.

### Resolve the Quantity Tier That Applies to Observed Consumption

> **Note:** Placeholder for the content of this section in #2595.

### Identify the Next Quantity Tier

> **Note:** Placeholder for the content of this section in #2595.

### Evaluate the Purchase Terms Offered for a SKU

> **Note:** Placeholder for the content of this section in #2595.

### Identify the Usage a Commitment Covers

This query answers which usage a [*commitment discount*](#glossary:commitment-discount) covers and how, before it is bought. It takes a service provider, the SKU Price ID of a commitment purchase, and a point in time. It returns one row per inclusion rule in Commitment Applicability, with the coverage that applies to the usage the rule matches: the rule's own coverage, or the default coverage of the purchase record when the rule has none. A purchase record with `IsGlobalScope` set to `true` returns a single row with the default coverage. Exclusions are returned as they are published.

This query uses BigQuery Standard SQL JSON functions (e.g., `JSON_VALUE`, `JSON_QUERY`, `JSON_EXTRACT_ARRAY`, `JSON_VALUE_ARRAY`, `UNNEST`). All major SQL engines have similar functions.

```sql
SELECT
  SP.SkuPriceId,
  SP.ContractId,
  SP.UnitPriceType,
  SP.CommitmentDiscountCategory,
  SP.PurchaseDurationType,
  SP.PurchasePaymentModel,
  JSON_VALUE(SP.CommitmentApplicability, '$.IsGlobalScope') AS IsGlobalScope,
  JSON_VALUE(SP.CommitmentApplicability, '$.IsComplexScope') AS IsComplexScope,
  JSON_VALUE(SP.CommitmentApplicability, '$.InclusionOperator') AS InclusionOperator,
  RuleOrder,
  JSON_VALUE(InclusionRule, '$.Dimension') AS Dimension,
  JSON_VALUE(InclusionRule, '$.Operator') AS Operator,
  JSON_VALUE_ARRAY(InclusionRule, '$.Values') AS IncludedValues,
  COALESCE(
    JSON_QUERY(InclusionRule, '$.Coverage'),
    JSON_QUERY(SP.CommitmentApplicability, '$.Coverage')
  ) AS Coverage,
  JSON_QUERY(SP.CommitmentApplicability, '$.Exclusions') AS Exclusions
FROM SkuPrice AS SP
LEFT JOIN UNNEST(JSON_EXTRACT_ARRAY(SP.CommitmentApplicability, '$.Inclusions')) AS InclusionRule
  WITH OFFSET AS RuleOrder
WHERE SP.ServiceProviderName = ?
  AND SP.SkuPriceId = ?
  AND SP.ChargeCategory = 'Purchase'
  AND SP.CommitmentApplicability IS NOT NULL
  AND (SP.SkuPriceEffectiveStart IS NULL OR SP.SkuPriceEffectiveStart <= ?)
  AND (SP.SkuPriceEffectiveEnd IS NULL OR SP.SkuPriceEffectiveEnd > ?)
ORDER BY SP.ContractId, SP.UnitPriceType, RuleOrder
```

### Derive the Effective Unit Price of a SKU Under Each Commitment

This query answers what one unit of a *SKU* costs under each *commitment discount* that covers it, so that the purchase options for that *SKU* can be ranked by the price they lead to. It takes a service provider, the SKU Price ID of a usage record, and a point in time. For each commitment purchase record whose Commitment Applicability covers the usage record, it returns the coverage and the effective unit price that follows from it:

* **`UnitPrice`:** the published unit price of covered usage.
* **`Discount`:** the Unit Price of the usage record whose Unit Price Type matches `Basis`, in the same Pricing Currency as the purchase, reduced by `Discount`. A "Contracted" basis uses the usage record under the same Contract ID as the purchase.
* **`Factor`:** the Unit Price of the purchase record spread over the hours of its term, multiplied by `Factor`.

This query uses BigQuery Standard SQL JSON functions (e.g., `JSON_VALUE`, `JSON_QUERY`, `JSON_EXTRACT_ARRAY`, `JSON_VALUE_ARRAY`, `UNNEST`). All major SQL engines have similar functions.

> **Note:** This query evaluates only inclusion rules whose `Dimension` is `SkuId`, `SkuPriceId`, `PricingServiceName`, `PricingRegionId`, or `RegionId` (compared with Pricing Region ID) and whose `Operator` is `In` or `StartsWith`. It does not check `Exclusions`, and it skips purchase records flagged `IsComplexScope`. A `Factor` is converted to an hourly price only for a usage record priced in "Hours" and a Purchase Duration Type of "1 Year" or "3 Years", and only when the purchase record's Unit Price carries the whole obligation of the purchase. The effective unit price assumes the *commitment discount* is fully used.

```sql
WITH UsagePrice AS (
  SELECT
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
  SELECT DISTINCT SkuId, SkuPriceId, PricingServiceName, PricingRegionId, PricingUnit
  FROM UsagePrice
),
Commitment AS (
  SELECT
    SkuPriceId AS CommitmentSkuPriceId,
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
    CommitmentContractId,
    CommitmentDiscountCategory,
    PurchaseDurationType,
    PurchasePaymentModel,
    CommitmentCurrency,
    CommitmentUnitPrice,
    PricingUnit
)
SELECT
  CV.CommitmentSkuPriceId,
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
  ON B.UnitPriceType = JSON_VALUE(CV.Coverage, '$.Basis')
  AND B.PricingCurrency = CV.CommitmentCurrency
  AND (
    (JSON_VALUE(CV.Coverage, '$.Basis') = 'List' AND B.ContractId IS NULL)
    OR (JSON_VALUE(CV.Coverage, '$.Basis') = 'Contracted' AND B.ContractId = CV.CommitmentContractId)
  )
WHERE CV.Coverage IS NOT NULL
ORDER BY EffectiveUnitPrice, CV.CommitmentSkuPriceId
```

In the [SKU Price examples](#appendix.examples:skuprice), the on-demand rate of the standard virtual machine is 0.384000 per hour. Under the one-year reservation, its effective unit price is 0.216164, 0.228174, or 0.240183 per hour for "All Upfront", "Partial Upfront", and "No Upfront", respectively. Under the flexible spend plan, it is 0.276480 per hour for every payment model.

### Project the Effect of Moving Consumption to a Contracted Rate

> **Note:** Placeholder for the content of this section in #2595.

### Compare Recorded Unit Prices with Published Rates

> **Note:** Placeholder for the content of this section in #2595.

## Version Introduced

1.5
