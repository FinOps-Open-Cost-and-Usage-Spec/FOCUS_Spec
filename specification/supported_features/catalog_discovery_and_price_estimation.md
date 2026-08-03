# Catalog Discovery and Price Estimation

## Description

FOCUS supports the discovery of the prices a [*service provider*](#glossary:service-provider) offers, and the estimation of cost for consumption that has not happened yet. Prices are carried in the [SKU Price](#datasets.skuprice) dataset, which describes the full [*price list*](#glossary:price-list) a *service provider* publishes rather than only the [*SKUs*](#glossary:sku) that already appear in [Cost and Usage](#datasets.costandusage) data. A [*practitioner*](#glossary:practitioner) sizing a net-new architecture can therefore price it from the same schema across every *service provider*, without reading one catalog format per provider.

List Unit Price is the public rate for a single Pricing Unit, denominated in the Pricing Currency, so an estimate is the planned quantity in that Pricing Unit multiplied by List Unit Price. Pricing Currency Category states whether that product is a financial amount or a balance in a [*consumption currency*](#glossary:consumption-currency) the *service provider* issues. A "Consumable" rate yields a virtual balance and needs a further conversion before it can be read as money, so an estimate that mixes the two categories without converting is not a monetary total.

Charge Category separates the rate to consume something ("Usage") from the fee to acquire it ("Purchase"), so a forecast keeps recurring consumption apart from acquisition fees rather than summing the two.

SKU Price Eligibility carries the inclusion and exclusion logic that determines which entities may receive a given price. A published catalog commonly contains prices an organization cannot obtain, so evaluating eligibility before pricing an architecture is what separates an achievable estimate from a theoretical one.

### Reading the Effective Date Columns

SKU Price Effective Start and SKU Price Effective End carry meaning only as a pair, and a query that tests one without the other returns the wrong prices. SKU Price Effective Start is inclusive and SKU Price Effective End is exclusive, and either may be null:

* Neither populated: the price applies across all time in both directions.
* Start only: the price applies from that date forward.
* End only: the price applies from the earliest available time through that date.
* Both populated: the price applies within that finite window.

A point-in-time lookup therefore treats a null bound as unbounded in that direction, which is the `(bound IS NULL OR comparison)` pattern every query below uses. Rating a charge follows the same rule against Charge Period Start: a charge falls under a price when its charge period start is on or after SKU Price Effective Start and before SKU Price Effective End.

> **Note:** A dataset instance may hold only the prices in force today, or it may also carry forward-dated changes and superseded prices. The specification does not require a *service provider* to publish pricing history, and carries no signal distinguishing the two, so the same query can return one row per SKU Price ID from one *service provider* and several from another. Filtering to a point in time rather than assuming one row per SKU Price ID is what makes a query portable.

### Scope When Conditional Columns are Absent

This feature applies wherever a *service provider* publishes a SKU Price dataset, and the data model states when that dataset is present. Every column this feature directly depends on is present in every SKU Price dataset instance.

One capability narrows. Pricing Region ID is present when the [*operating model*](#glossary:operating-model) [includes regions](#conditions.includesregions). Where it is absent, prices do not vary by location and a single price stands for every region, so comparing rates across regions does not apply rather than returning an incomplete result.

## Directly Dependent Columns

* [SkuPrice](#datasets.skuprice)
  * ChargeCategory
  * ListUnitPrice
  * PricingCurrency
  * PricingCurrencyCategory
  * PricingServiceName
  * PricingUnit
  * ServiceProviderName
  * SkuId
  * SkuPriceDescription
  * SkuPriceEffectiveEnd
  * SkuPriceEffectiveStart
  * SkuPriceEligibility
  * SkuPriceId

## Supporting Columns

* [SkuPrice](#datasets.skuprice)
  * PricingRegionId
  * SkuPriceCreated
  * SkuPriceLastUpdated

## Example SQL Queries

> Note: The following examples are informative and non-normative. They do not define requirements.

SKU Price Eligibility is defined in [*JSON object format*](#attributes.jsonobjectformat), and ANSI SQL does not define a standard for parsing JSON. The eligibility query below uses BigQuery Standard SQL JSON functions (e.g., `JSON_VALUE`, `JSON_EXTRACT_ARRAY`, `JSON_VALUE_ARRAY`, `UNNEST`); similar functions exist in all major SQL engines. Every other query below is ANSI SQL and runs without modification.

> Important Consideration: The following queries assume FOCUS-conformant dataset artifacts. Practitioners should verify provider conformance before relying on these queries. Non-conformant dataset artifacts may produce inaccurate results.

### Find the List Prices in Force at a Point in Time

This query takes inputs of a service provider, a pricing service name, and a point in time, then returns the public rates that apply for that service at that moment. The same point in time is supplied to both bounds, and each bound is tested for null so that an open-ended price is returned rather than filtered out.

```sql
SELECT
  SkuId,
  SkuPriceId,
  SkuPriceDescription,
  PricingUnit,
  PricingCurrency,
  PricingCurrencyCategory,
  ListUnitPrice
FROM SkuPrice
WHERE ServiceProviderName = ?
  AND PricingServiceName = ?
  AND ChargeCategory = 'Usage'
  AND ListUnitPrice IS NOT NULL
  AND (SkuPriceEffectiveStart IS NULL OR SkuPriceEffectiveStart <= ?)
  AND (SkuPriceEffectiveEnd IS NULL OR SkuPriceEffectiveEnd > ?)
ORDER BY SkuId, ListUnitPrice
```

### Estimate the Cost of a Planned Workload

This query takes a set of planned quantities, each paired with the SKU Price ID it is priced under and a point in time, and returns the projected cost of each line and the components behind it. The planned quantity is expressed in the Pricing Unit of the matching price, so a rate quoted per `1K Requests` takes a quantity counted in thousands of requests rather than in requests.

Pricing Currency Category is returned alongside the total because a "Consumable" rate produces a balance in a consumption currency rather than a financial amount. Rows carrying different Pricing Currency values, or a mix of "Payable" and "Consumable", are not additive without a conversion step the SKU Price dataset does not carry.

```sql
WITH PlannedUsage AS (
  SELECT ? AS SkuPriceId, ? AS PlannedQuantity
)
SELECT
  SP.SkuPriceId,
  SP.SkuPriceDescription,
  SP.PricingUnit,
  PU.PlannedQuantity,
  SP.ListUnitPrice,
  SP.PricingCurrency,
  SP.PricingCurrencyCategory,
  PU.PlannedQuantity * SP.ListUnitPrice AS EstimatedAmount
FROM PlannedUsage PU
INNER JOIN SkuPrice SP
  ON PU.SkuPriceId = SP.SkuPriceId
WHERE SP.ListUnitPrice IS NOT NULL
  AND (SP.SkuPriceEffectiveStart IS NULL OR SP.SkuPriceEffectiveStart <= ?)
  AND (SP.SkuPriceEffectiveEnd IS NULL OR SP.SkuPriceEffectiveEnd > ?)
ORDER BY EstimatedAmount DESC
```

### Identify the Prices a Billing Account is Eligible For

This query takes inputs of a service provider and a billing account identifier, then returns the prices that account may receive. A price with `IsGlobalScope` set to `true` applies to all entities without restriction. A price with neither global nor complex scope carries an `Inclusions` array whose rules name the dimension, operator, and values that define the boundary.

> **Note:** This query evaluates the `In` operator against the `BillingAccountId` dimension only, and returns rows flagged `IsComplexScope` for review rather than resolving them. A complete evaluation applies `InclusionOperator` across all inclusion rules and then removes any entity caught by `Exclusions`, in the order described in the SKU Price Eligibility column definition.

```sql
SELECT
  SkuPriceId,
  SkuPriceDescription,
  ListUnitPrice,
  PricingCurrency,
  SkuPriceEligibility
FROM SkuPrice
WHERE ServiceProviderName = ?
  AND (SkuPriceEffectiveStart IS NULL OR SkuPriceEffectiveStart <= ?)
  AND (SkuPriceEffectiveEnd IS NULL OR SkuPriceEffectiveEnd > ?)
  AND (
    JSON_VALUE(SkuPriceEligibility, '$.IsGlobalScope') = 'true'
    OR JSON_VALUE(SkuPriceEligibility, '$.IsComplexScope') = 'true'
    OR EXISTS (
      SELECT 1
      FROM UNNEST(JSON_EXTRACT_ARRAY(SkuPriceEligibility, '$.Inclusions')) AS INC
      WHERE JSON_VALUE(INC, '$.Dimension') = 'BillingAccountId'
        AND JSON_VALUE(INC, '$.Operator') = 'In'
        AND ? IN UNNEST(JSON_VALUE_ARRAY(INC, '$.Values'))
    )
  )
ORDER BY SkuPriceId
```

### Separate Recurring Usage Rates from Purchase Fees

This query takes inputs of a service provider and a point in time, then reports the catalog split between rates that price consumption and fees that price acquisition. A forecast built only on "Usage" rates omits the acquisition fees an architecture also incurs, so the two are counted separately rather than summed.

```sql
SELECT
  ChargeCategory,
  PricingUnit,
  PricingCurrency,
  COUNT(*) AS SkuPriceCount,
  MIN(ListUnitPrice) AS LowestListUnitPrice,
  MAX(ListUnitPrice) AS HighestListUnitPrice
FROM SkuPrice
WHERE ServiceProviderName = ?
  AND ListUnitPrice IS NOT NULL
  AND (SkuPriceEffectiveStart IS NULL OR SkuPriceEffectiveStart <= ?)
  AND (SkuPriceEffectiveEnd IS NULL OR SkuPriceEffectiveEnd > ?)
GROUP BY ChargeCategory, PricingUnit, PricingCurrency
ORDER BY ChargeCategory, PricingUnit
```

### Find Announced Price Changes and Scheduled Retirements

This query takes inputs of a service provider and a point in time, then returns the prices whose applicability changes after that moment: those that take effect later, and those that stop applying. A forward-dated SKU Price Effective Start is an announced price change, and a SKU Price Effective End in the future is a scheduled retirement of that price.

SKU Price Created and SKU Price Last Updated are returned so a change can be traced to when the record entered the catalog and when it last moved. Because the dataset represents prices as of the date it is captured, retaining successive dataset instances and comparing them on these two columns is how a practitioner reconstructs a price history the *service provider* does not publish.

```sql
SELECT
  SkuId,
  SkuPriceId,
  SkuPriceDescription,
  ListUnitPrice,
  PricingCurrency,
  SkuPriceEffectiveStart,
  SkuPriceEffectiveEnd,
  SkuPriceCreated,
  SkuPriceLastUpdated
FROM SkuPrice
WHERE ServiceProviderName = ?
  AND (SkuPriceEffectiveStart > ? OR SkuPriceEffectiveEnd > ?)
ORDER BY SkuPriceEffectiveStart, SkuPriceEffectiveEnd
```

### Compare List Prices Across Regions

This query takes inputs of a pricing service name and a point in time, then reports how the public rate for each SKU Price ID varies by location, so that a deployment decision can account for the price difference between regions. It applies where the operating model includes regions.

```sql
SELECT
  SkuId,
  SkuPriceId,
  PricingRegionId,
  PricingUnit,
  PricingCurrency,
  ListUnitPrice
FROM SkuPrice
WHERE PricingServiceName = ?
  AND ChargeCategory = 'Usage'
  AND ListUnitPrice IS NOT NULL
  AND (SkuPriceEffectiveStart IS NULL OR SkuPriceEffectiveStart <= ?)
  AND (SkuPriceEffectiveEnd IS NULL OR SkuPriceEffectiveEnd > ?)
ORDER BY SkuPriceId, ListUnitPrice
```

## Version Introduced

1.5
