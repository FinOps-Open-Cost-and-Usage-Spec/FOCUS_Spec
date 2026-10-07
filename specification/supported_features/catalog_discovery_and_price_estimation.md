# Catalog Discovery and Price Estimation

## Description

FOCUS helps a [*practitioner*](#glossary:practitioner) find the prices a [*service provider*](#glossary:service-provider) offers. It also helps estimate what future consumption will cost. The [SKU Price](#datamodel.skuprice) dataset holds these prices. It covers the full [*price list*](#glossary:price-list) a *service provider* publishes, not just the [*SKUs*](#glossary:sku) already in [Cost and Usage](#datamodel.costandusage) data. So a new architecture can be priced the same way for every *service provider*, without learning a different catalog format for each one.

Unit Price is the price of one Pricing Unit, in the Pricing Currency. Unit Price Type says what kind of price it is:

* "List" is the public list price. A "List" record has a null Contract ID.
* "Base" is a list price that a [*contract*](#glossary:contract) fixes. Its Contract ID names that *contract*.
* "Contracted" is any other price under a *contract*, such as a negotiated rate. Its Contract ID also names the *contract*.

An estimate from public prices multiplies the planned quantity by the Unit Price on the "List" record. The planned quantity is counted in the Pricing Unit.

Pricing Currency Category says whether that result is money or a balance in a [*consumption currency*](#glossary:consumption-currency) the *service provider* issues. A "Consumable" rate gives a balance, not money. That balance needs another conversion before it can be read as money. So an estimate that mixes the two categories without converting is not a money total.

Charge Category sorts prices into three kinds. "Usage" is the rate to use something. "Purchase" is the fee to buy it. "Credit" is the value of one unit of a granted credit. So a forecast can keep usage rates and purchase fees apart instead of adding them together.

SKU Price Eligibility holds the rules that decide which entities can get a price. A published catalog often includes prices an organization cannot get. Checking eligibility before pricing an architecture is what separates an estimate the organization can achieve from one that is only theoretical.

An estimate built this way leaves out the effect of any [*commitment discount*](#glossary:commitment-discount). Unit Price on a "List" record is the public rate. No rate in the SKU Price dataset shows the effect of a *commitment discount* applied to consumption. An organization with commitments that would cover the planned architecture pays less than this estimate shows. That difference is measured from recorded consumption in Cost and Usage, through the [Cost Comparison](#supportedfeatures.costcomparison) supported feature, not from the price list.

### Reading the Effective Date Columns

SKU Price Effective Start and SKU Price Effective End only make sense as a pair. A query that tests one without the other returns the wrong prices. The start is inclusive, so the price applies from that moment. The end is exclusive, so the price stops applying at that moment. Either one may be null:

* Neither populated: the price applies across all time in both directions.
* Start only: the price applies from that date forward.
* End only: the price applies from the earliest available time up to, but not including, that date.
* Both populated: the price applies within that finite window.

So a lookup at a point in time treats a null bound as having no limit on that side. The point-in-time queries below do this with the pattern `(bound IS NULL OR comparison)`. The query that finds announced changes is the exception. It tests the bounds directly, because it looks for prices that start or stop applying later, not for prices in force at that moment.

A [*charge*](#glossary:charge) follows the same rule, using its Charge Period Start. A charge falls under a price when its Charge Period Start is on or after SKU Price Effective Start and before SKU Price Effective End.

> **Note:** A [*dataset instance*](#glossary:dataset-instance) may hold only the prices in force today. Or it may also hold future price changes and old prices that were replaced. The specification does not require a *service provider* to publish price history, and FOCUS defines no way to tell these two kinds of dataset instance apart. So the same query can return one row per SKU Price ID from one *service provider* and several from another. A query that filters to a point in time, instead of expecting one row per SKU Price ID, works the same way for both.

### Scope When Conditional Columns are Absent

This feature applies wherever a *service provider* publishes a SKU Price dataset. The data model says when that dataset is present. Every column this feature directly depends on is in every SKU Price dataset instance.

The queries that read public prices keep only records with a Unit Price Type of "List". So they return nothing from a dataset instance that has only contract prices. "List" is a recommended value, not a required one. When a *service provider* labels its public prices with a value of its own, that value replaces "List" in these queries. Unlike "List", a value of its own does not mean the Contract ID is null, so these queries then also need a filter for a null Contract ID.

Four conditions change what applies:

* Pricing Region ID is present when the [*operating model*](#glossary:operating-model) [includes regions](#operatingmodelconditions.includesregions). When it is absent, prices do not vary by location, and one price stands for every region. Comparing rates across regions then does not apply, rather than giving an incomplete result.
* Quantity Tier Minimum and Quantity Tier Maximum are present when the *operating model* [includes quantity tier pricing](#operatingmodelconditions.includesquantitytierpricing). When they are absent, every price applies at any quantity, so a planned line needs no tier. The queries that return these two columns still work with them left out.
* Separating usage rates from purchase fees applies when the *operating model* [includes purchases](#operatingmodelconditions.includespurchases). When it does not, the catalog has no purchase fees, and no record has a Charge Category of "Purchase". An estimate from usage rates then has no purchase fees to add.
* Commitment Discount Category is present when the *operating model* [includes commitment discounts](#operatingmodelconditions.includescommitmentdiscounts). When it is absent, no price is for a *commitment discount*, and the list price query still works with that column left out.

## Directly Dependent Columns

* [SkuPrice](#datamodel.skuprice)
  * ChargeCategory
  * ContractId
  * PricingCurrencyCategory
  * SkuPriceEligibility
  * UnitPrice
  * UnitPriceType

## Supporting Columns

* [SkuPrice](#datamodel.skuprice)
  * CommitmentDiscountCategory
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

SKU Price Eligibility uses [*JSON object format*](#attributes.jsonobjectformat). The eligibility query below uses BigQuery Standard SQL JSON functions (e.g., `JSON_VALUE`, `JSON_EXTRACT_ARRAY`, `JSON_VALUE_ARRAY`, `UNNEST`). All major SQL engines have similar functions. Every other query below uses ANSI SQL, with `?` marking each input value. A query may need small changes for a particular database engine, such as in how it accepts the list of planned quantities.

> **Note:** The following queries assume FOCUS-conformant dataset artifacts. Practitioners should verify provider conformance before relying on these queries. Non-conformant dataset artifacts may produce inaccurate results.

### Find the List Prices in Force at a Point in Time

This query answers which public usage rates apply to a service at a given moment. An estimate starts from these rates. It takes a service provider, a pricing service name, and a point in time. It keeps only records with a Charge Category of "Usage", so purchase fees and granted credits are left out. Dropping that filter returns every public rate for the service. The same point in time goes to both date bounds. Each bound is tested for null, so a price with no start date or no end date is returned rather than dropped.

It also keeps only records with a Unit Price Type of "List", which hold the public list price. A record under a *contract* holds a "Base" or "Contracted" price instead. A record with no *contract* can instead hold a Unit Price Type the *service provider* defines for itself. This query leaves both out.

One *SKU* can still return the same public rate more than once. A *service provider* can publish a separate usage record, with its own SKU Price ID, for consumption a *commitment discount* covers. That record also holds the list price. SKU Price Description and Commitment Discount Category are returned so these rows can be told apart.

```sql
SELECT
  SkuId,
  SkuPriceId,
  SkuPriceDescription,
  CommitmentDiscountCategory,
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
  AND UnitPriceType = 'List'
  AND (SkuPriceEffectiveStart IS NULL OR SkuPriceEffectiveStart <= ?)
  AND (SkuPriceEffectiveEnd IS NULL OR SkuPriceEffectiveEnd > ?)
ORDER BY SkuId, UnitPrice
```

### Estimate the Cost of a Planned Workload

This query answers what a planned workload would cost at public rates. The total can then be checked against a budget or compared with another design. It takes a set of planned lines. Each line has a service provider, the SKU Price ID it is priced under, a planned quantity, and a point in time. The query returns the projected cost of each line and the values behind it. The planned quantity is counted in the Pricing Unit of the matching price. So a rate quoted per `1K Requests` takes a quantity counted in thousands of requests, not in requests.

Pricing Currency Category is returned with the total, because a "Consumable" rate gives a balance in a *consumption currency*, not money. Rows with different Pricing Currency values cannot be added together without a conversion, and neither can a mix of "Payable" and "Consumable" rows. The SKU Price dataset does not carry that conversion. A SKU Price ID published in more than one pricing currency returns one row per currency for the same planned line. Those rows are alternative prices for that line, not parts of it.

Quantity Tier Minimum and Quantity Tier Maximum are returned so each row can be matched to its tier. Each tier has its own SKU Price ID, so a planned line names its tier. A quantity that spans tiers is entered as one line per tier, split the way the pricing terms of the *service provider* say. Those terms, not the tier boundaries, decide whether a tier's rate applies only to the units inside that tier or to every unit consumed.

The query prices each line at the public rate from the "List" record. Replacing `SP.UnitPriceType = 'List'` with `SP.ContractId = ? AND SP.UnitPriceType = 'Contracted'` prices it at the rate negotiated under a *contract* instead. A line whose SKU Price ID has no "Contracted" record under that *contract* then returns with its price columns null. The Unit Price Type filter is still needed, because one *contract* can have both a "Base" and a "Contracted" record for the same SKU Price ID.

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
  AND SP.UnitPriceType = 'List'
  AND (SP.SkuPriceEffectiveStart IS NULL OR SP.SkuPriceEffectiveStart <= PU.PlannedDate)
  AND (SP.SkuPriceEffectiveEnd IS NULL OR SP.SkuPriceEffectiveEnd > PU.PlannedDate)
ORDER BY SP.PricingCurrencyCategory, SP.PricingCurrency, EstimatedPricingCurrencyListCost DESC
```

### Identify the Prices a Billing Account is Eligible For

This query answers which prices a [*billing account*](#glossary:billing-account) may be eligible for. An estimate can then set aside prices the account cannot receive. It takes a service provider, a point in time, and a *billing account* ID. A price with `IsGlobalScope` set to `true` applies to every entity its `Exclusions` do not remove. A price with neither global nor complex scope has an `Inclusions` array. Each rule in that array names a dimension, an operator, and the values that decide which entities are included.

Contract ID and Unit Price Type are returned to tell apart the prices under one SKU Price ID. Contract ID separates a *contract* price from the list price. Unit Price Type separates a "Base" price from a "Contracted" one under the same *contract*.

> **Note:** This query checks only the `In` operator on the `BillingAccountId` dimension. That includes the `["*"]` wildcard, which matches every account. Rows flagged `IsComplexScope` are returned for review, not resolved. The query does not check `Exclusions`, so it can return a price for an account that `Exclusions` removes. Some prices have neither global nor complex scope and have `Inclusions` that do not name `BillingAccountId`. Under the implicit wildcard rule in the SKU Price Eligibility column definition, such a price places no limit on billing account, but this query does not return it. The query compares values exactly as written, while the SKU Price Eligibility column definition compares them without regard to case. A full check applies `InclusionOperator` across all inclusion rules, then removes any entity caught by `Exclusions`, in the order the SKU Price Eligibility column definition gives.

```sql
SELECT
  SkuPriceId,
  ContractId,
  UnitPriceType,
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
ORDER BY SkuPriceId, ContractId, UnitPriceType
```

### Separate Usage Rates from Purchase Fees and Credit Values

This query answers what kinds of prices a catalog holds. Knowing that keeps a forecast from leaving out purchase fees or reading a credit value as a usage rate. It takes a service provider and a point in time, and it shows how the catalog splits across Charge Category. A forecast built only on "Usage" rates leaves out any purchase fees the architecture also has to pay. So each category is counted on its own, not added together. Only "List" records are counted, so the counts and price ranges describe the public catalog, not the prices of any one *contract*. Pricing Currency Category is returned so a rate priced in a *consumption currency* is not read as money.

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
  AND UnitPriceType = 'List'
  AND (SkuPriceEffectiveStart IS NULL OR SkuPriceEffectiveStart <= ?)
  AND (SkuPriceEffectiveEnd IS NULL OR SkuPriceEffectiveEnd > ?)
GROUP BY ChargeCategory, PricingUnit, PricingCurrency, PricingCurrencyCategory
ORDER BY ChargeCategory, PricingUnit
```

### Find Announced Price Changes and Scheduled Retirements

This query answers which public prices change after a given moment. A forecast or a migration plan can then account for a change before it takes effect. It takes a service provider and a point in time. It returns the public prices that change after that moment: prices that start later, and prices that stop applying later. A SKU Price Effective Start after that moment is an announced price change. A SKU Price Effective End after that moment is a scheduled retirement of that price. Only "List" records are returned. Dropping that filter also returns changes to *contract* prices and to any other Unit Price Type the *service provider* publishes.

SKU Price Created and SKU Price Last Updated are returned to show when the record entered the catalog and when it last changed. The dataset shows prices as of the date it is captured. To rebuild a price history the *service provider* does not publish, a *practitioner* keeps dataset instances over time. The *practitioner* then compares them on SKU Price Effective Start and SKU Price Effective End. The two timestamps cannot replace that comparison, because a correction can update a record after its effective window has closed.

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
  AND UnitPriceType = 'List'
  AND (SkuPriceEffectiveStart > ? OR SkuPriceEffectiveEnd > ?)
ORDER BY SkuPriceEffectiveStart, SkuPriceEffectiveEnd
```

### Compare List Prices Across Regions

This query answers how the public rate for each *SKU* varies by location. A deployment decision can then weigh the price difference between regions. It takes a service provider, a pricing service name, and a point in time. Rows are sorted by SKU ID, because SKU ID stays the same across the price details a *SKU* varies by, including location. SKU Price ID may not, since a *service provider* may publish a separate SKU Price ID for each region. This query applies where the *operating model* includes regions.

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
  AND UnitPriceType = 'List'
  AND (SkuPriceEffectiveStart IS NULL OR SkuPriceEffectiveStart <= ?)
  AND (SkuPriceEffectiveEnd IS NULL OR SkuPriceEffectiveEnd > ?)
ORDER BY SkuId, PricingCurrency, UnitPrice
```

## Version Introduced

1.5
