# Catalog Discovery and Price Estimation

## Description

FOCUS supports the discovery of the prices a [*service provider*](#glossary:service-provider) offers, and the estimation of cost for consumption that has not happened yet. Prices are carried in the [SKU Price](#datamodel.skuprice) dataset, which describes the full [*price list*](#glossary:price-list) a *service provider* publishes rather than only the [*SKUs*](#glossary:sku) that already appear in [Cost and Usage](#datamodel.costandusage) data. A [*practitioner*](#glossary:practitioner) sizing a net-new architecture can therefore price it from the same schema across every *service provider*, without reading one catalog format per provider.

Unit Price is the rate for a single Pricing Unit, denominated in the Pricing Currency. On a record with a null Contract ID it is the public list price, and on a record with a populated Contract ID it is a rate negotiated under that [*contract*](#glossary:contract), so an estimate from public prices is the planned quantity in that Pricing Unit multiplied by Unit Price on the record with a null Contract ID. Pricing Currency Category states whether that product is a financial amount or a balance in a [*consumption currency*](#glossary:consumption-currency) the *service provider* issues. A "Consumable" rate yields a virtual balance and needs a further conversion before it can be read as money, so an estimate that mixes the two categories without converting is not a monetary total.

Charge Category separates the rate to consume something ("Usage") from the fee to acquire it ("Purchase") and from the unit value of a granted credit ("Credit"), so a forecast keeps recurring consumption apart from acquisition fees rather than summing them.

SKU Price Eligibility carries the inclusion and exclusion logic that determines which entities may receive a given price. A published catalog commonly contains prices an organization cannot obtain, so evaluating eligibility before pricing an architecture is what separates an achievable estimate from a theoretical one.

An estimate built this way is a pre-commitment estimate. Unit Price on a record with a null Contract ID is the public rate, and no rate in the SKU Price dataset reflects a [*commitment discount*](#glossary:commitment-discount) having been applied to consumption. An organization holding commitments that would cover the planned architecture pays less than this estimate shows. Sizing that difference is done against recorded consumption in Cost and Usage, through the [Cost Comparison](#supportedfeatures.costcomparison) supported feature, rather than against the price list.

### Reading the Effective Date Columns

SKU Price Effective Start and SKU Price Effective End carry meaning only as a pair, and a query that tests one without the other returns the wrong prices. SKU Price Effective Start is inclusive and SKU Price Effective End is exclusive, and either may be null:

* Neither populated: the price applies across all time in both directions.
* Start only: the price applies from that date forward.
* End only: the price applies from the earliest available time up to, but not including, that date.
* Both populated: the price applies within that finite window.

A point-in-time lookup therefore treats a null bound as unbounded in that direction, which is the `(bound IS NULL OR comparison)` pattern the point-in-time queries below use. Finding announced changes is the exception: it tests the bounds directly, because it looks for prices whose applicability changes rather than for prices in force. Rating a [*charge*](#glossary:charge) follows the same rule against Charge Period Start: a charge falls under a price when its charge period start is on or after SKU Price Effective Start and before SKU Price Effective End.

> **Note:** A [*dataset instance*](#glossary:dataset-instance) may hold only the prices in force today, or it may also carry forward-dated changes and superseded prices. The specification does not require a *service provider* to publish pricing history, and carries no signal distinguishing the two, so the same query can return one row per SKU Price ID from one *service provider* and several from another. Filtering to a point in time rather than assuming one row per SKU Price ID is what makes a query portable.

### Scope When Conditional Columns are Absent

This feature applies wherever a *service provider* publishes a SKU Price dataset, and the data model states when that dataset is present. Every column this feature directly depends on is present in every SKU Price dataset instance. The queries that read public prices keep only records with a null Contract ID, so they return nothing from a dataset instance that carries only negotiated rates.

Three conditions change what applies. Pricing Region ID is present when the [*operating model*](#glossary:operating-model) [includes regions](#operatingmodelconditions.includesregions). Where it is absent, prices do not vary by location and a single price stands for every region, so comparing rates across regions does not apply rather than returning an incomplete result. Quantity Tier Minimum and Quantity Tier Maximum are present when the *operating model* [includes quantity tier pricing](#operatingmodelconditions.includesquantitytierpricing). Where they are absent, every price applies at any quantity, so a planned line needs no tier, and the queries that return those two columns hold with them left out. Separating usage rates from purchase fees applies when the *operating model* [includes purchases](#operatingmodelconditions.includespurchases). Where it does not, the catalog publishes no acquisition fees and no record carries a Charge Category of "Purchase", so an estimate from consumption rates has no purchase-fee component to add.

## Directly Dependent Columns

* [SkuPrice](#datamodel.skuprice)
  * ChargeCategory
  * ContractId
  * PricingCurrencyCategory
  * SkuPriceEligibility
  * UnitPrice

## Supporting Columns

* [SkuPrice](#datamodel.skuprice)
  * PricingCurrency
  * PricingRegionId
  * PricingServiceName
  * PricingUnit
  * QuantityTierMaximum
  * QuantityTierMinimum
  * ServiceProviderName
  * SkuId
  * SkuPriceCreated
  * SkuPriceDescription
  * SkuPriceEffectiveEnd
  * SkuPriceEffectiveStart
  * SkuPriceId
  * SkuPriceLastUpdated

## Example SQL Queries

SKU Price Eligibility is defined in [*JSON object format*](#attributes.jsonobjectformat). The eligibility query below uses BigQuery Standard SQL JSON functions (e.g., `JSON_VALUE`, `JSON_EXTRACT_ARRAY`, `JSON_VALUE_ARRAY`, `UNNEST`); similar functions exist in all major SQL engines. Every other query below uses ANSI SQL, with `?` marking each input value, and may need small adjustments for a particular database engine, such as in how it accepts the list of planned quantities.

> **Note:** The following queries assume FOCUS-conformant dataset artifacts. Practitioners should verify provider conformance before relying on these queries. Non-conformant dataset artifacts may produce inaccurate results.

### Find the List Prices in Force at a Point in Time

This query takes inputs of a service provider, a pricing service name, and a point in time, then returns the public consumption rates that apply for that service at that moment. It filters to a Charge Category of "Usage", so acquisition fees and granted credits are excluded; dropping that predicate returns every public rate for the service. The same point in time is supplied to both bounds, and each bound is tested for null so that an open-ended price is returned rather than filtered out.

It also keeps only records with a null Contract ID, which carry the public list price; a record with a populated Contract ID carries a rate negotiated under a specific *contract*. One *SKU* can still return the same public rate more than once. A *service provider* can publish a separate usage record, under its own SKU Price ID, for consumption a *commitment discount* covers, and that record carries the list price. SKU Price Description is returned so those rows can be told apart.

```sql
SELECT
  SkuId,
  SkuPriceId,
  SkuPriceDescription,
  PricingUnit,
  QuantityTierMinimum,
  QuantityTierMaximum,
  PricingCurrency,
  PricingCurrencyCategory,
  UnitPrice
FROM SkuPrice
WHERE ServiceProviderName = ?
  AND PricingServiceName = ?
  AND ChargeCategory = 'Usage'
  AND ContractId IS NULL
  AND (SkuPriceEffectiveStart IS NULL OR SkuPriceEffectiveStart <= ?)
  AND (SkuPriceEffectiveEnd IS NULL OR SkuPriceEffectiveEnd > ?)
ORDER BY SkuId, UnitPrice
```

### Estimate the Cost of a Planned Workload

This query takes a set of planned quantities, each paired with the service provider and the SKU Price ID it is priced under and a point in time, and returns the projected cost of each line and the components behind it. The planned quantity is expressed in the Pricing Unit of the matching price, so a rate quoted per `1K Requests` takes a quantity counted in thousands of requests rather than in requests.

Pricing Currency Category is returned alongside the total because a "Consumable" rate produces a balance in a consumption currency rather than a financial amount. Rows carrying different Pricing Currency values, or a mix of "Payable" and "Consumable", are not additive without a conversion step the SKU Price dataset does not carry. Additionally, a SKU Price ID published in more than one pricing currency returns one row per currency for the same planned line, and those rows are alternative prices for that line rather than parts of it.

Quantity Tier Minimum and Quantity Tier Maximum are returned so each row can be matched to the tier it prices. Each tier carries its own SKU Price ID, so a planned line names its tier. A quantity that spans tiers is entered as one line per tier, split as the pricing terms of the *service provider* dictate, since whether a tier's rate applies only to the units inside that tier or to every unit consumed is a property of those terms rather than of the tier boundaries.

The query prices each line at the public rate. Replacing `SP.ContractId IS NULL` with `SP.ContractId = ?` prices it at the rate negotiated under that *contract* instead, and a line whose SKU Price ID the *contract* does not price returns with its price columns null.

```sql
WITH PlannedUsage (ServiceProviderName, SkuPriceId, PlannedQuantity, PlannedDate) AS (
  VALUES (?, ?, ?, ?)
)
SELECT
  PU.ServiceProviderName,
  PU.SkuPriceId,
  SP.SkuPriceDescription,
  SP.PricingUnit,
  SP.QuantityTierMinimum,
  SP.QuantityTierMaximum,
  PU.PlannedQuantity,
  SP.UnitPrice,
  SP.PricingCurrency,
  SP.PricingCurrencyCategory,
  PU.PlannedQuantity * SP.UnitPrice AS EstimatedPricingCurrencyListCost
FROM PlannedUsage PU
LEFT JOIN SkuPrice SP
  ON SP.ServiceProviderName = PU.ServiceProviderName
  AND SP.SkuPriceId = PU.SkuPriceId
  AND SP.ContractId IS NULL
  AND (SP.SkuPriceEffectiveStart IS NULL OR SP.SkuPriceEffectiveStart <= PU.PlannedDate)
  AND (SP.SkuPriceEffectiveEnd IS NULL OR SP.SkuPriceEffectiveEnd > PU.PlannedDate)
ORDER BY SP.PricingCurrencyCategory, SP.PricingCurrency, EstimatedPricingCurrencyListCost DESC
```

### Identify the Prices a Billing Account is Eligible For

This query takes inputs of a service provider, a point in time, and a [*billing account*](#glossary:billing-account) identifier, then returns the prices that account may be eligible for. A price with `IsGlobalScope` set to `true` applies to every entity its `Exclusions` do not remove. A price with neither global nor complex scope carries an `Inclusions` array whose rules name the dimension, operator, and values that define the boundary. Contract ID is returned so a contracted price the account may receive can be told apart from the list price under the same SKU Price ID.

> **Note:** This query evaluates the `In` operator against the `BillingAccountId` dimension only, including the `["*"]` wildcard that matches every account, and returns rows flagged `IsComplexScope` for review rather than resolving them. It does not evaluate `Exclusions`, so a price can return for an account its `Exclusions` remove. Where a price has neither global nor complex scope and its `Inclusions` do not name `BillingAccountId`, the price is unrestricted on billing account under the implicit wildcard rule in the SKU Price Eligibility column definition, but this query does not return it. Values are compared as written, while the SKU Price Eligibility column definition normalizes case before comparing. A complete evaluation applies `InclusionOperator` across all inclusion rules and then removes any entity caught by `Exclusions`, in the order described in the SKU Price Eligibility column definition.

```sql
SELECT
  SkuPriceId,
  ContractId,
  SkuPriceDescription,
  UnitPrice,
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
        AND (
          ? IN UNNEST(JSON_VALUE_ARRAY(INC, '$.Values'))
          OR '*' IN UNNEST(JSON_VALUE_ARRAY(INC, '$.Values'))
        )
    )
  )
ORDER BY SkuPriceId, ContractId
```

### Separate Usage Rates from Purchase Fees and Credit Values

This query takes inputs of a service provider and a point in time, then reports how the catalog divides across Charge Category. A forecast built only on "Usage" rates omits the acquisition fees an architecture also incurs, so each category is counted separately rather than summed. Only records with a null Contract ID are counted, so the counts and price ranges describe the public catalog rather than the rates of any one *contract*. Pricing Currency Category is returned so a rate priced in a *consumption currency* is not read as a monetary amount.

```sql
SELECT
  ChargeCategory,
  PricingUnit,
  PricingCurrency,
  PricingCurrencyCategory,
  COUNT(*) AS SkuPriceCount,
  MIN(UnitPrice) AS LowestPublicUnitPrice,
  MAX(UnitPrice) AS HighestPublicUnitPrice
FROM SkuPrice
WHERE ServiceProviderName = ?
  AND ContractId IS NULL
  AND (SkuPriceEffectiveStart IS NULL OR SkuPriceEffectiveStart <= ?)
  AND (SkuPriceEffectiveEnd IS NULL OR SkuPriceEffectiveEnd > ?)
GROUP BY ChargeCategory, PricingUnit, PricingCurrency, PricingCurrencyCategory
ORDER BY ChargeCategory, PricingUnit
```

### Find Announced Price Changes and Scheduled Retirements

This query takes inputs of a service provider and a point in time, then returns the public prices whose applicability changes after that moment: those that take effect later, and those that stop applying. A forward-dated SKU Price Effective Start is an announced price change, and a SKU Price Effective End in the future is a scheduled retirement of that price. Only records with a null Contract ID are returned; dropping that predicate also returns changes to negotiated rates.

SKU Price Created and SKU Price Last Updated are returned so a change can be traced to when the record entered the catalog and when it last moved. Because the dataset represents prices as of the date it is captured, a practitioner reconstructs a price history the *service provider* does not publish by retaining successive dataset instances and comparing them on SKU Price Effective Start and SKU Price Effective End. The two audit timestamps are not a substitute, since a correction can update a record after its effective window has closed.

```sql
SELECT
  SkuId,
  SkuPriceId,
  SkuPriceDescription,
  UnitPrice,
  PricingCurrency,
  SkuPriceEffectiveStart,
  SkuPriceEffectiveEnd,
  SkuPriceCreated,
  SkuPriceLastUpdated
FROM SkuPrice
WHERE ServiceProviderName = ?
  AND ContractId IS NULL
  AND (SkuPriceEffectiveStart > ? OR SkuPriceEffectiveEnd > ?)
ORDER BY SkuPriceEffectiveStart, SkuPriceEffectiveEnd
```

### Compare List Prices Across Regions

This query takes inputs of a service provider, a pricing service name, and a point in time, then reports how the public rate for each *SKU* varies by location, so that a deployment decision can account for the price difference between regions. Rows are ordered by SKU ID, because SKU ID stays the same across the price details a *SKU* varies by, including location, while a *service provider* may publish a separate SKU Price ID for each region. It applies where the *operating model* includes regions.

```sql
SELECT
  SkuId,
  SkuPriceId,
  PricingRegionId,
  PricingUnit,
  QuantityTierMinimum,
  QuantityTierMaximum,
  PricingCurrency,
  UnitPrice
FROM SkuPrice
WHERE ServiceProviderName = ?
  AND PricingServiceName = ?
  AND ChargeCategory = 'Usage'
  AND ContractId IS NULL
  AND (SkuPriceEffectiveStart IS NULL OR SkuPriceEffectiveStart <= ?)
  AND (SkuPriceEffectiveEnd IS NULL OR SkuPriceEffectiveEnd > ?)
ORDER BY SkuId, PricingCurrency, UnitPrice
```

## Version Introduced

1.5
