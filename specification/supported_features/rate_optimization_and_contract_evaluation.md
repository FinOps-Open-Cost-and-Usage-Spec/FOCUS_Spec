# Rate Optimization and Contract Evaluation

## Description

FOCUS helps compare the rate an organization pays with the rates a [*service provider*](#glossary:service-provider) offers. The [SKU Price](#datamodel.skuprice) dataset holds each price as its own record. Unit Price Type says what kind of price a record holds:

* "List" is the public list price. A "List" record has a null Contract ID.
* "Base" is a list price that a [*contract*](#glossary:contract) fixes. Its Contract ID names that *contract*.
* "Contracted" is any other price under a *contract*. Its Contract ID also names the *contract*. This page calls it the negotiated rate.

One *contract* can have both a "Base" and a "Contracted" record under the same SKU Price ID.

Comparing a negotiated rate with the public rate pairs the two records for the same price. It does not work out the difference from what was billed. Joining SKU Price to [Cost and Usage](#datamodel.costandusage) on SKU Price ID then lines up recorded consumption with the [*price list*](#glossary:price-list) it came from. That is what turns a rate difference into an amount.

This feature answers three questions.

The first is how much negotiation lowered the rate. The reduction per unit is the Unit Price on the "List" record minus the Unit Price on the "Contracted" record for the same price. Contract ID names the *contract* the negotiated rate belongs to. Each record has its own effective dates, so the pairing tests both records against the same point in time. A negotiated rate whose dates differ from the public rate's dates pairs with the public rate in force at that moment. This difference is only the negotiated part of an agreement, not its full effect. Any further reduction from applying a [*commitment discount*](#glossary:commitment-discount) to a [*charge*](#glossary:charge) shows in Effective Cost on the Cost and Usage side. The [Cost Comparison](#supportedfeatures.costcomparison) supported feature covers reading the two together.

The second is whether consumption is in the right quantity tier. Quantity Tier Minimum and Quantity Tier Maximum set the range of quantities a rate applies to, counted in the Pricing Unit. The minimum is exclusive and the maximum is inclusive. So a quantity is in a tier when it is greater than the minimum and no greater than the maximum. The highest tier has a null Quantity Tier Maximum. Neighboring tiers meet at a shared boundary with no gap. So the tier above a given tier is the one whose Quantity Tier Minimum equals that tier's Quantity Tier Maximum. That is how the next tier and its rate are found. A tier is known by its boundaries, not by a published name. So checking a tier against a public pricing page means matching on the range of quantities its rate applies to.

Each tier is its own record with its own SKU Price ID. That is because the SKU Price dataset requires each SKU Price ID to have one Quantity Tier Minimum and one Quantity Tier Maximum when the [*operating model*](#glossary:operating-model) includes quantity tier pricing. The tier queries below find the tiers of one offering through what those tiers share: the service provider, SKU ID, Pricing Region ID, Pricing Unit, and Pricing Currency. They do not use SKU Price ID for this.

No column separates one set of tiers from other prices under the same SKU ID. Commitment Discount Category marks the rates for consumption a *commitment discount* covers. But it is present only when the *operating model* includes commitment discounts, and it does not mark which records form a set of tiers. So the tier queries read public prices only from records with a tier boundary (a Quantity Tier Minimum above zero or a populated Quantity Tier Maximum). They assume one set of public tiers for each combination of service provider, SKU ID, Pricing Region ID, Pricing Unit, and Pricing Currency.

The third is which purchase term to commit to. Purchase Duration Type gives the length of a purchase's term as a category (e.g., "1 Year"). Purchase Payment Model gives how the purchase is paid: "No Upfront", "Partial Upfront", or "All Upfront". Purchase Payment Model is populated when Charge Category is "Purchase". Purchase Duration Type may be null on a "Purchase" record when the *service provider* publishes no standard term. Both are null when Charge Category is "Usage" or "Credit".

So the fees for each term and payment model can be listed side by side. They can then be weighed against the consumption that would run under them. The *service provider* decides whether those fees differ by payment model. Some *service providers* charge less in total when more is paid upfront. Others charge the same total under every payment model, so the records differ only in when the amount is paid.

> **Note:** Each payment model is published as its own SKU Price record. A "Partial Upfront" purchase can be one record. It can also be two records: one for the upfront fee and one for the recurring fee. So comparing it with another payment model takes all of its records together, not just one.

The [Verification, Comparison, and Fluctuation Tracking of Unit Prices](#supportedfeatures.verificationcomparisonandfluctuationtrackingofunitprices) supported feature reads List Unit Price and Contracted Unit Price as recorded on a charge in Cost and Usage. This feature reads the public and negotiated rates from the published catalog. So the two answer different questions: what an organization was charged, and what a *service provider* offers. The query that compares recorded unit prices with published rates reads both. It puts the unit prices recorded on each charge next to the rates the SKU Price dataset publishes.

### When Public and Negotiated Records are Paired

Pairing a public record with a negotiated record is needed in only one case. That is when the two rates are compared with each other in the catalog, with no charge to tie them to.

When the *operating model* includes List Unit Price and Contracted Unit Price, Cost and Usage has both on every charge with a SKU Price ID. Savings on recorded consumption are then measured from List Cost and Contracted Cost, through the Cost Comparison supported feature. The recorded unit prices are read through the Verification, Comparison, and Fluctuation Tracking of Unit Prices supported feature. Neither one needs the SKU Price dataset. Checking a charge's recorded unit price against the catalog joins the charge to one SKU Price record. For the list price, that is the "List" record. For the negotiated rate, it is the "Contracted" record under the *contract* that applies to the charge. Measuring how far a billed negotiated rate is below the public rate is a different comparison. That one reads the "List" record, as the Relationships section of the SKU Price dataset describes.

Pairing applies to questions asked of the catalog itself, such as how much negotiation lowers a rate, or how the two rates compare at a given quantity. The first two queries below answer these questions. They narrow the SKU Price dataset to the service or SKU in scope before pairing.

A "Base" record under a *contract* holds a list price the *contract* fixes, not a negotiated rate. So the queries below that read a negotiated rate select "Contracted" records. Replacing "Contracted" with "Base" in a query reads that fixed price instead.

A *commitment discount* is not stored as a negotiated rate. Its purchase fee is a record with a Charge Category of "Purchase". Consumption it covers can be billed under the SKU Price ID of a separate usage record, priced at the list price. So the reduction it brings is read from Effective Cost in Cost and Usage, not from a Unit Price. When the rate on such a usage record differs by commitment term (e.g., one year and three years), each term has its own SKU Price ID. When the *operating model* includes commitment discounts, the purchase fee record and the usage record both have a Commitment Discount Category. It says whether the commitment is to an amount of usage ("Usage") or of spend ("Spend").

### Reading SKU Price ID and the Effective Date Columns

SKU Price ID names the stable properties of a price, not a single row. By design, it repeats across contracts, unit price types, pricing currencies, and time windows. That is what keeps prices comparable across them. So joining Cost and Usage to SKU Price on SKU Price ID alone repeats each charge once for every record with that ID. The *service provider* also sets the SKU Price ID, so two service providers can publish the same value. Every join below narrows the match further, at least by Service Provider Name, Pricing Currency, and the effective date window.

SKU Price Effective Start is inclusive, and SKU Price Effective End is exclusive. Either one may be null, which means no limit on that side. A charge falls under a price when its Charge Period Start is on or after SKU Price Effective Start and before SKU Price Effective End. The joins below test this with the pattern `(bound IS NULL OR comparison)`. With the service provider, Contract ID, Pricing Currency, and Unit Price Type fixed, a SKU Price ID points to one record at any point in time.

A [*dataset instance*](#glossary:dataset-instance) may hold only the prices in force when it was captured. So a charge from before the latest price change finds its record only in an earlier dataset instance kept for that purpose. The queries below that resolve a tier or reprice consumption drop a charge that finds no record. The query that compares recorded unit prices keeps it, with null rates.

The SKU Price dataset links a charge to a price through the charge's Pricing Currency. When the *operating model* does not include pricing and billing currency differences, the link uses the charge's Billing Currency instead. The queries that read Cost and Usage match on Billing Currency, because Effective Cost is in the Billing Currency. So a charge priced in one currency and billed in another matches only a price the *service provider* also quotes in the Billing Currency.

These queries take a time range through Charge Period Start and Charge Period End. Charge Period End is exclusive, so a charge that ends where the range ends falls inside the range. The range is tested with `ChargePeriodEnd <= ?`.

### Scope When Conditional Columns are Absent

This feature applies wherever a *service provider* publishes a SKU Price dataset. The data model says when that dataset is present. Unit Price, Unit Price Type, and Contract ID are in every SKU Price *dataset instance*. Reading public rates applies wherever the dataset has "List" records. Comparing negotiated rates with public rates applies wherever it also has "Contracted" records.

"List" and "Contracted" are recommended values, not required ones. When a *service provider* labels its prices with values of its own, those values replace "List" and "Contracted" in the queries below. Unlike "List" and "Contracted", a value of its own says nothing about Contract ID. So a query that reads public prices then also needs a filter for a null Contract ID. A query that reads contract prices needs a filter for a populated one. Cost and Usage has SKU Price ID under the same condition as the SKU Price dataset. So the queries that join the two datasets apply wherever this feature does.

Each conditional column narrows this feature on its own:

* Quantity tier analysis uses Quantity Tier Minimum and Quantity Tier Maximum. They are present when the *operating model* [includes quantity tier pricing](#operatingmodelconditions.includesquantitytierpricing). When they are absent, a price applies at any quantity, so consumption cannot be in the wrong tier. Resolving a tier, finding the next tier, and comparing public and negotiated prices at a quantity then do not apply. Quantity Tier Minimum and Quantity Tier Maximum also drop out of the columns the negotiation and repricing queries return.
* The tier queries also match on Pricing Region ID. It is present when the *operating model* [includes regions](#operatingmodelconditions.includesregions). When it is absent, prices do not vary by location. Pricing Region ID and the filters on it then drop out of those queries.
* Purchase term evaluation uses Purchase Duration Type and Purchase Payment Model. They are present when the *operating model* [includes purchases](#operatingmodelconditions.includespurchases). When they are absent, the catalog has no purchase fees and no row has a Charge Category of "Purchase", so this part of the feature does not apply.
* Repricing recorded consumption leaves out the consumption a *commitment discount* covered, using Commitment Discount ID. That column is present when the *operating model* [includes commitment discounts](#operatingmodelconditions.includescommitmentdiscounts). When it is absent, no consumption is covered by a *commitment discount*, so the filter is not needed and the result is the same. Commitment Discount Category, which the purchase terms query returns, is present under the same condition. When it is absent, it drops out of that query.
* Matching on Billing Currency assumes a charge is priced in the currency it is billed in. When the *operating model* [includes pricing and billing currency differences](#operatingmodelconditions.includespricing-billingcurrencydifferences), Cost and Usage also has Pricing Currency. Matching on Pricing Currency instead finds the charges the Billing Currency match leaves out. Repricing then uses Pricing Currency Effective Cost in place of Effective Cost.
* Comparing recorded unit prices reads List Unit Price and Contracted Unit Price from Cost and Usage. When either column is absent, that column and the differences computed from it drop out of that query.

## Directly Dependent Columns

* [SkuPrice](#datamodel.skuprice)
  * ContractId
  * PurchaseDurationType
  * PurchasePaymentModel
  * QuantityTierMaximum
  * QuantityTierMinimum
  * UnitPrice
  * UnitPriceType

## Supporting Columns

* [SkuPrice](#datamodel.skuprice)
  * ChargeCategory
  * CommitmentDiscountCategory
  * PricingCurrency
  * PricingRegionId
  * PricingServiceName
  * PricingUnit
  * ServiceProviderName
  * SkuId
  * SkuPriceDescription
  * SkuPriceEffectiveEnd
  * SkuPriceEffectiveStart
  * SkuPriceId
* [CostAndUsage](#datamodel.costandusage)
  * BillingAccountId
  * BillingCurrency
  * ChargeCategory
  * ChargePeriodEnd
  * ChargePeriodStart
  * CommitmentDiscountId
  * ContractedUnitPrice
  * EffectiveCost
  * ListUnitPrice
  * PricingQuantity
  * PricingUnit
  * ServiceProviderName
  * SkuPriceId

## Example SQL Queries

The following queries use ANSI SQL, with `?` marking each input value. They may need small changes for a particular database engine.

> **Note:** The following queries assume FOCUS-conformant dataset artifacts. Practitioners should verify provider conformance before relying on these queries. Non-conformant dataset artifacts may produce inaccurate results.

### Measure What Negotiation Reduces the Rate By

This query answers what the negotiated usage rates for one service in a *contract* save per unit. An agreement can then be judged rate by rate (e.g., before a renewal). It takes a service provider, a Pricing Service Name, a Contract ID, and a point in time. It looks at each usage rate negotiated under that *contract* for the service. For each one, it shows how far the rate is below the public rate for the same price. It assumes the comparison is limited to certain services or SKUs first, as a review of an agreement usually is. It is not meant to run across the full price list. Adding a SKU ID filter to both sets narrows it from a service to specific SKUs.

The query builds two sets of prices in force at the point in time: public prices ("List" records) and negotiated prices ("Contracted" records under that Contract ID). It pairs each negotiated record with the public record that has the same service provider, SKU Price ID, and Pricing Currency. Each record's effective dates are tested against the point in time on their own. So a negotiated rate whose dates differ from the public rate's dates pairs with the public rate in force at that moment. A negotiated rate that has not started yet does not appear. Some negotiated rates have no public record in force for the same SKU Price ID and Pricing Currency, such as a private offer or a tier an agreement defines under its own SKU Price ID. These rates return with the public columns null.

The result is the reduction from negotiation, not the total reduction an organization gets on that [*SKU*](#glossary:sku). Any further reduction from applying a *commitment discount* shows in Effective Cost. The reduction is measured from the public rate in force at the point in time. When the *contract* also has a "Base" record for the same SKU Price ID, measuring from that record instead gives the reduction from the list price the *contract* fixed.

```sql
WITH Review AS (
  SELECT
    ? AS ServiceProviderName,
    ? AS PricingServiceName,
    ? AS ContractId,
    ? AS PointInTime
),
PublicPrices AS (
  SELECT
    SP.ServiceProviderName,
    SP.SkuPriceId,
    SP.PricingCurrency,
    SP.UnitPrice
  FROM SkuPrice SP
  INNER JOIN Review R
    ON SP.ServiceProviderName = R.ServiceProviderName
    AND SP.PricingServiceName = R.PricingServiceName
    AND (SP.SkuPriceEffectiveStart IS NULL OR SP.SkuPriceEffectiveStart <= R.PointInTime)
    AND (SP.SkuPriceEffectiveEnd IS NULL OR SP.SkuPriceEffectiveEnd > R.PointInTime)
  WHERE SP.UnitPriceType = 'List'
),
ContractedPrices AS (
  SELECT
    SP.ServiceProviderName,
    SP.ContractId,
    SP.SkuPriceId,
    SP.PricingUnit,
    SP.PricingCurrency,
    SP.QuantityTierMinimum,
    SP.QuantityTierMaximum,
    SP.UnitPrice
  FROM SkuPrice SP
  INNER JOIN Review R
    ON SP.ServiceProviderName = R.ServiceProviderName
    AND SP.PricingServiceName = R.PricingServiceName
    AND SP.ContractId = R.ContractId
    AND (SP.SkuPriceEffectiveStart IS NULL OR SP.SkuPriceEffectiveStart <= R.PointInTime)
    AND (SP.SkuPriceEffectiveEnd IS NULL OR SP.SkuPriceEffectiveEnd > R.PointInTime)
  WHERE SP.ChargeCategory = 'Usage'
    AND SP.UnitPriceType = 'Contracted'
)
SELECT
  CP.ServiceProviderName,
  CP.ContractId,
  CP.SkuPriceId,
  CP.PricingUnit,
  CP.PricingCurrency,
  CP.QuantityTierMinimum,
  CP.QuantityTierMaximum,
  PP.UnitPrice AS PublicUnitPrice,
  CP.UnitPrice AS ContractedUnitPrice,
  PP.UnitPrice - CP.UnitPrice AS UnitPriceReduction,
  (PP.UnitPrice - CP.UnitPrice) / NULLIF(PP.UnitPrice, 0) AS DiscountRate
FROM ContractedPrices CP
LEFT JOIN PublicPrices PP
  ON PP.ServiceProviderName = CP.ServiceProviderName
  AND PP.SkuPriceId = CP.SkuPriceId
  AND PP.PricingCurrency = CP.PricingCurrency
ORDER BY DiscountRate DESC
```

### Compare Public and Negotiated Prices at a Given Quantity

This query answers how the public price and the negotiated price compare at a specific quantity. An agreement with its own tiers can then be judged at the volumes the organization expects. It makes the comparison the query above makes, for one offering whose negotiated tiers may not match the public ones. It takes a service provider, a SKU ID, a Pricing Region ID, a Pricing Unit, a Pricing Currency, a quantity, a point in time, and a Contract ID. It returns the public price whose tier contains that quantity. Next to it is the negotiated price under that Contract ID whose tier contains the same quantity. Each side finds its own tier and its own effective dates. So an agreement whose tier boundaries or dates differ from the public prices is still compared at the quantity and moment given. When the *contract* prices no tier that contains the quantity, or is not in force at that point in time, the negotiated columns are null.

The public side reads only records with a tier boundary, as described above. So an offering without quantity tiers returns no rows. For such an offering, the query above compares the negotiated rate with the public rate. A *contract* with more than one rate that contains the quantity, such as a tier and a flat rate for the same offering, returns one row for each. Several sets of inputs can be compared in one run, and a set entered more than once returns its rows only once.

```sql
WITH Comparison (ServiceProviderName, SkuId, PricingRegionId, PricingUnit, PricingCurrency, Quantity, PointInTime, ContractId) AS (
  VALUES (?, ?, ?, ?, ?, ?, ?, ?)
),
PublicTier AS (
  SELECT
    C.ServiceProviderName,
    C.SkuId,
    C.PricingRegionId,
    C.PricingUnit,
    C.PricingCurrency,
    C.Quantity,
    C.PointInTime,
    C.ContractId,
    SP.SkuPriceId,
    SP.QuantityTierMinimum,
    SP.QuantityTierMaximum,
    SP.UnitPrice
  FROM SkuPrice SP
  INNER JOIN Comparison C
    ON SP.ServiceProviderName = C.ServiceProviderName
    AND SP.SkuId = C.SkuId
    AND (SP.PricingRegionId = C.PricingRegionId OR (SP.PricingRegionId IS NULL AND C.PricingRegionId IS NULL))
    AND SP.PricingUnit = C.PricingUnit
    AND SP.PricingCurrency = C.PricingCurrency
    AND C.Quantity > SP.QuantityTierMinimum
    AND (SP.QuantityTierMaximum IS NULL OR C.Quantity <= SP.QuantityTierMaximum)
    AND (SP.SkuPriceEffectiveStart IS NULL OR SP.SkuPriceEffectiveStart <= C.PointInTime)
    AND (SP.SkuPriceEffectiveEnd IS NULL OR SP.SkuPriceEffectiveEnd > C.PointInTime)
  WHERE SP.ChargeCategory = 'Usage'
    AND SP.UnitPriceType = 'List'
    AND (SP.QuantityTierMinimum > 0 OR SP.QuantityTierMaximum IS NOT NULL)
),
ContractedTier AS (
  SELECT
    C.ServiceProviderName,
    C.SkuId,
    C.PricingRegionId,
    C.PricingUnit,
    C.PricingCurrency,
    C.Quantity,
    C.PointInTime,
    C.ContractId,
    SP.SkuPriceId,
    SP.QuantityTierMinimum,
    SP.QuantityTierMaximum,
    SP.UnitPrice
  FROM SkuPrice SP
  INNER JOIN Comparison C
    ON SP.ServiceProviderName = C.ServiceProviderName
    AND SP.SkuId = C.SkuId
    AND (SP.PricingRegionId = C.PricingRegionId OR (SP.PricingRegionId IS NULL AND C.PricingRegionId IS NULL))
    AND SP.PricingUnit = C.PricingUnit
    AND SP.PricingCurrency = C.PricingCurrency
    AND SP.ContractId = C.ContractId
    AND C.Quantity > SP.QuantityTierMinimum
    AND (SP.QuantityTierMaximum IS NULL OR C.Quantity <= SP.QuantityTierMaximum)
    AND (SP.SkuPriceEffectiveStart IS NULL OR SP.SkuPriceEffectiveStart <= C.PointInTime)
    AND (SP.SkuPriceEffectiveEnd IS NULL OR SP.SkuPriceEffectiveEnd > C.PointInTime)
  WHERE SP.ChargeCategory = 'Usage'
    AND SP.UnitPriceType = 'Contracted'
)
SELECT DISTINCT
  PT.ServiceProviderName,
  PT.SkuId,
  PT.PricingRegionId,
  PT.PricingUnit,
  PT.PricingCurrency,
  PT.Quantity,
  PT.PointInTime,
  PT.ContractId,
  PT.SkuPriceId AS PublicSkuPriceId,
  PT.QuantityTierMinimum AS PublicTierMinimum,
  PT.QuantityTierMaximum AS PublicTierMaximum,
  PT.UnitPrice AS PublicUnitPrice,
  CT.SkuPriceId AS ContractedSkuPriceId,
  CT.QuantityTierMinimum AS ContractedTierMinimum,
  CT.QuantityTierMaximum AS ContractedTierMaximum,
  CT.UnitPrice AS ContractedUnitPrice,
  PT.UnitPrice - CT.UnitPrice AS UnitPriceReduction
FROM PublicTier PT
LEFT JOIN ContractedTier CT
  ON CT.ServiceProviderName = PT.ServiceProviderName
  AND CT.SkuId = PT.SkuId
  AND (CT.PricingRegionId = PT.PricingRegionId OR (CT.PricingRegionId IS NULL AND PT.PricingRegionId IS NULL))
  AND CT.PricingUnit = PT.PricingUnit
  AND CT.PricingCurrency = PT.PricingCurrency
  AND CT.Quantity = PT.Quantity
  AND CT.PointInTime = PT.PointInTime
  AND CT.ContractId = PT.ContractId
```

### Resolve the Quantity Tier That Applies to Observed Consumption

This query answers which quantity tier the consumption in one pricing period reached. The result can be checked against the tier the organization planned for. It takes a time range through Charge Period Start and Charge Period End. It adds up the consumption recorded over that range and returns the tier the total falls in. First, each charge is placed in a set of tiers through the public record for the SKU Price ID it was billed under. Then the quantity is added up across the set before the tier is found. That is because a tier boundary is checked against the quantity built up over the pricing period. It is not checked against the quantity billed under any one SKU Price ID.

The joins include the effective date window, so consumption matches the price that applied during the range, not every price ever published under that SKU Price ID. The window is checked against the earliest Charge Period Start in the range. So the query assumes the range falls within a single effective window. A range that crosses a price change finds the tier using the record in force at the start of the range, not each record in turn.

The query also assumes the range is a single tier accounting period (e.g., one calendar month). The published pricing terms for the offering define that period. Tier quantities build up within the period and start again in the next one. So a longer range adds together quantities the *service provider* counts separately, and it can return a tier that no single period reached.

The public tier returns with a null Contract ID. Each negotiated ("Contracted") rate that contains the total quantity, whether a tier or a flat rate, returns its own row. A charge billed under a SKU Price ID with no "List" record, such as a rate an agreement defines with its own tier boundaries, is not counted.

Corrections to a closed billing period keep the charge period of the consumption they correct, so they count toward that range. A reversal lowers the quantity and cost. A correction for usage missing from an earlier invoice adds to them. The total covers every [*billing account*](#glossary:billing-account) in the range. When a *service provider* checks tiers for each *billing account* separately, adding Billing Account ID to `ChargeTierSet` and to the grouping keeps each account's quantity apart.

> **Note:** The published pricing terms for the offering, not the tier boundaries, decide whether the rate of the tier returned here applies only to the units inside that tier or to every unit consumed. So this query returns the tier the total quantity reached and that tier's rate. It does not recalculate the charge.

```sql
WITH ChargeTierSet AS (
  SELECT
    CU.ServiceProviderName,
    SP.SkuId,
    SP.PricingRegionId,
    CU.PricingUnit,
    CU.BillingCurrency,
    CU.ChargePeriodStart,
    CU.PricingQuantity,
    CU.EffectiveCost
  FROM CostAndUsage CU
  INNER JOIN SkuPrice SP
    ON SP.ServiceProviderName = CU.ServiceProviderName
    AND SP.SkuPriceId = CU.SkuPriceId
    AND SP.PricingUnit = CU.PricingUnit
    AND SP.PricingCurrency = CU.BillingCurrency
    AND SP.UnitPriceType = 'List'
    AND SP.ChargeCategory = 'Usage'
    AND (SP.QuantityTierMinimum > 0 OR SP.QuantityTierMaximum IS NOT NULL)
    AND (SP.SkuPriceEffectiveStart IS NULL OR CU.ChargePeriodStart >= SP.SkuPriceEffectiveStart)
    AND (SP.SkuPriceEffectiveEnd IS NULL OR CU.ChargePeriodStart < SP.SkuPriceEffectiveEnd)
  WHERE CU.ChargePeriodStart >= ? AND CU.ChargePeriodEnd <= ?
    AND CU.ChargeCategory = 'Usage'
),
PeriodQuantity AS (
  SELECT
    ServiceProviderName,
    SkuId,
    PricingRegionId,
    PricingUnit,
    BillingCurrency,
    MIN(ChargePeriodStart) AS EarliestChargePeriodStart,
    SUM(PricingQuantity) AS TotalPricingQuantity,
    SUM(EffectiveCost) AS TotalEffectiveCost
  FROM ChargeTierSet
  GROUP BY ServiceProviderName, SkuId, PricingRegionId, PricingUnit, BillingCurrency
)
SELECT
  PQ.ServiceProviderName,
  PQ.SkuId,
  PQ.PricingRegionId,
  PQ.PricingUnit,
  PQ.BillingCurrency,
  PQ.TotalPricingQuantity,
  PQ.TotalEffectiveCost,
  SP.SkuPriceId,
  SP.ContractId,
  SP.QuantityTierMinimum,
  SP.QuantityTierMaximum,
  SP.UnitPrice
FROM PeriodQuantity PQ
INNER JOIN SkuPrice SP
  ON SP.ServiceProviderName = PQ.ServiceProviderName
  AND SP.SkuId = PQ.SkuId
  AND (SP.PricingRegionId = PQ.PricingRegionId OR (SP.PricingRegionId IS NULL AND PQ.PricingRegionId IS NULL))
  AND SP.PricingUnit = PQ.PricingUnit
  AND SP.PricingCurrency = PQ.BillingCurrency
  AND SP.ChargeCategory = 'Usage'
  AND (
    SP.UnitPriceType = 'Contracted'
    OR (SP.UnitPriceType = 'List' AND (SP.QuantityTierMinimum > 0 OR SP.QuantityTierMaximum IS NOT NULL))
  )
  AND PQ.TotalPricingQuantity > SP.QuantityTierMinimum
  AND (SP.QuantityTierMaximum IS NULL OR PQ.TotalPricingQuantity <= SP.QuantityTierMaximum)
  AND (SP.SkuPriceEffectiveStart IS NULL OR PQ.EarliestChargePeriodStart >= SP.SkuPriceEffectiveStart)
  AND (SP.SkuPriceEffectiveEnd IS NULL OR PQ.EarliestChargePeriodStart < SP.SkuPriceEffectiveEnd)
ORDER BY PQ.TotalEffectiveCost DESC
```

### Identify the Next Quantity Tier

This query answers where the next quantity tier starts and what its rate is. Together with the tier and total quantity the query above returns, that shows how far current consumption is from the next tier's rate. It takes one or more *SKUs*, each named by a Service Provider Name and SKU ID, and a point in time. For each tier of those *SKUs* that has a next tier, it returns the tier's boundaries, rate, and width. It also returns the next tier, the next tier's rate, and the difference between the two rates.

The next tier is the tier in the same set whose Quantity Tier Minimum equals the current tier's Quantity Tier Maximum. The two tiers are matched on Service Provider Name, SKU ID, Pricing Region ID, Contract ID, Unit Price Type, Pricing Unit, Pricing Currency, and Charge Category, as well as on that boundary. This keeps public and negotiated tiers apart. It also keeps a "Base" tier from pairing with a "Contracted" tier under the same *contract*.

The query assumes one set of tiers for each such combination. It looks only at tiers in effect at the given point in time.

Tier Width is the current tier's Quantity Tier Maximum minus its Quantity Tier Minimum. It does not show how far recorded consumption is from the next tier, because the query reads only the SKU Price dataset.

A tier with a null Quantity Tier Maximum is the highest tier. It has no next tier, so it does not appear. A tier is also left out when no other tier starts at its Quantity Tier Maximum. So a gap or overlap between tier boundaries is not reported as a next tier. A negotiated tier whose *contract* defines no next tier does not appear either. For such a tier, the terms of the agreement set the rate beyond its maximum. The query that compares public and negotiated prices at a given quantity shows both sides at a chosen quantity. A requested *SKU* without quantity tiers returns no rows.

> **Note:** The published pricing terms for the offering decide how the next tier's rate applies, not the tier boundaries. The rate may apply only to the units inside that tier, or to every unit consumed. So the difference between the two rates is the change in rate at the boundary. It is not the change in cost from reaching the next tier.

```sql
WITH RequestedSkus (ServiceProviderName, SkuId) AS (
    VALUES
        -- (ServiceProviderName, SkuId)
        (?, ?),
        (?, ?),
        (?, ?)
),
ActiveTiers AS (
    SELECT
        SP.ServiceProviderName,
        SP.SkuId,
        SP.PricingRegionId,
        SP.ContractId,
        SP.UnitPriceType,
        SP.PricingUnit,
        SP.PricingCurrency,
        SP.ChargeCategory,
        SP.SkuPriceId,
        SP.QuantityTierMinimum,
        SP.QuantityTierMaximum,
        SP.UnitPrice
    FROM SkuPrice SP
    WHERE EXISTS (
        SELECT 1
        FROM RequestedSkus RS
        WHERE RS.ServiceProviderName = SP.ServiceProviderName
          AND RS.SkuId = SP.SkuId
    )
      AND (SP.QuantityTierMinimum > 0 OR SP.QuantityTierMaximum IS NOT NULL)
      AND (SP.SkuPriceEffectiveStart IS NULL OR SP.SkuPriceEffectiveStart <= ?)  -- point in time
      AND (SP.SkuPriceEffectiveEnd IS NULL OR SP.SkuPriceEffectiveEnd > ?)       -- point in time
)
SELECT
    CURRENT_TIER.ServiceProviderName,
    CURRENT_TIER.SkuId,
    CURRENT_TIER.PricingRegionId,
    CURRENT_TIER.ContractId,
    CURRENT_TIER.UnitPriceType,
    CURRENT_TIER.PricingUnit,
    CURRENT_TIER.PricingCurrency,
    CURRENT_TIER.SkuPriceId AS CurrentSkuPriceId,
    CURRENT_TIER.QuantityTierMinimum AS CurrentTierMinimum,
    CURRENT_TIER.QuantityTierMaximum AS CurrentTierMaximum,
    CURRENT_TIER.UnitPrice AS CurrentUnitPrice,
    NEXT_TIER.SkuPriceId AS NextSkuPriceId,
    NEXT_TIER.QuantityTierMaximum AS NextTierMaximum,
    NEXT_TIER.UnitPrice AS NextUnitPrice,
    CURRENT_TIER.UnitPrice - NEXT_TIER.UnitPrice AS UnitPriceReduction,
    CURRENT_TIER.QuantityTierMaximum - CURRENT_TIER.QuantityTierMinimum AS TierWidth
FROM ActiveTiers CURRENT_TIER
INNER JOIN ActiveTiers NEXT_TIER
    ON NEXT_TIER.ServiceProviderName = CURRENT_TIER.ServiceProviderName
    AND NEXT_TIER.SkuId = CURRENT_TIER.SkuId
    AND (
        NEXT_TIER.PricingRegionId = CURRENT_TIER.PricingRegionId
        OR (
            NEXT_TIER.PricingRegionId IS NULL
            AND CURRENT_TIER.PricingRegionId IS NULL
        )
    )
    AND NEXT_TIER.PricingUnit = CURRENT_TIER.PricingUnit
    AND NEXT_TIER.PricingCurrency = CURRENT_TIER.PricingCurrency
    AND NEXT_TIER.ChargeCategory = CURRENT_TIER.ChargeCategory
    AND (
        NEXT_TIER.ContractId = CURRENT_TIER.ContractId
        OR (
            NEXT_TIER.ContractId IS NULL
            AND CURRENT_TIER.ContractId IS NULL
        )
    )
    AND NEXT_TIER.UnitPriceType = CURRENT_TIER.UnitPriceType
    AND NEXT_TIER.QuantityTierMinimum = CURRENT_TIER.QuantityTierMaximum
WHERE CURRENT_TIER.QuantityTierMaximum IS NOT NULL
ORDER BY
    CURRENT_TIER.SkuId,
    CURRENT_TIER.ContractId,
    CURRENT_TIER.UnitPriceType,
    CURRENT_TIER.QuantityTierMinimum
```

### Evaluate the Purchase Terms Offered for a SKU

This query answers which ways of buying a *SKU* are on offer and what fees each one has. The options can then be lined up before a commitment is made. It takes a service provider, a SKU ID, and a point in time, and it lists every purchase fee published for that *SKU*. Every fee is returned. Contract ID and Unit Price Type tell the fees apart, since an agreement can discount a purchase ("Contracted") or fix its list price ("Base"). A "Partial Upfront" purchase published as separate upfront-fee and recurring-fee records returns a row for each. The two together are the price of that payment model. Commitment Discount Category is returned so a fee for a *commitment discount* shows whether it commits to an amount of usage or of spend. That decides whether the consumption it would cover is weighed in usage or in cost.

Ranking these options means finding the effective unit price of each one: what one unit of covered usage costs under that option. The SKU Price dataset does not carry what that takes. For a commitment to an amount of usage, the fees are spread over the term. That takes two facts: which usage the purchase covers, and how much usage one unit of it covers. A commitment to an amount of spend needs the rate it gives on each covered *SKU*. FOCUS has no standard way to carry that rate. So the comparison depends on commitment terms from outside the dataset.

```sql
SELECT
  SkuId,
  SkuPriceId,
  ContractId,
  UnitPriceType,
  SkuPriceDescription,
  CommitmentDiscountCategory,
  PurchaseDurationType,
  PurchasePaymentModel,
  PricingUnit,
  PricingCurrency,
  UnitPrice
FROM SkuPrice
WHERE ServiceProviderName = ?
  AND SkuId = ?
  AND ChargeCategory = 'Purchase'
  AND (SkuPriceEffectiveStart IS NULL OR SkuPriceEffectiveStart <= ?)
  AND (SkuPriceEffectiveEnd IS NULL OR SkuPriceEffectiveEnd > ?)
ORDER BY PurchaseDurationType, PurchasePaymentModel, SkuPriceId, ContractId, UnitPriceType
```

### Project the Effect of Moving Consumption to a Contracted Rate

This query answers what consumption would cost at the negotiated rate in a *contract*, compared with what it cost. The difference sizes the value of moving that consumption onto the agreement (e.g., before extending the agreement to more *billing accounts*). It takes a time range through Charge Period Start and Charge Period End, a service provider, and a Contract ID. It adds up the consumption recorded over that range that no *commitment discount* covered. Then it reprices that consumption at the rate negotiated under that agreement. The difference between what the consumption cost and what it would cost at the negotiated rate is the amount at stake in the agreement.

Consumption already covered by a *commitment discount* is left out. Its Effective Cost already reflects that commitment, but the negotiated Unit Price does not. Including it would subtract two amounts measured from different starting points. The agreement could then look like it raises cost instead of lowering it.

Consumption is repriced at the negotiated rate under the SKU Price ID it was billed under, since a SKU Price ID stays the same across contracts. Each tier has its own SKU Price ID, so that rate is the negotiated rate for the tier the charge was billed in. A SKU Price ID fixes both the Quantity Tier Minimum and the Quantity Tier Maximum of its tier. So a negotiated tier whose boundaries differ from those of every public tier has a SKU Price ID of its own. Consumption billed under the public tiers is not repriced at that tier's rate. The query that compares public and negotiated prices at a given quantity finds such tiers through the SKU ID.

The effective date window is checked against the earliest Charge Period Start, so the query assumes the range falls within a single effective window. Corrections to a closed billing period keep the charge period of the consumption they correct, so they count toward that range. A reversal lowers the quantity and cost. A correction for usage missing from an earlier invoice adds to them.

A *contract* does not make its negotiated rate available to all of an organization's consumption. SKU Price Eligibility decides which consumption gets the rate. It can limit the rate to certain *billing accounts*, [*sub accounts*](#glossary:sub-account), regions, or other Cost and Usage values. This query reprices all consumption billed under the SKU Price ID that no *commitment discount* covered. Consumption the agreement does not cover stays out only when each charge is checked against SKU Price Eligibility before `ObservedUsage` adds the charges up.

Effective Cost is in the Billing Currency, while Unit Price is in the Pricing Currency. So the join matches the two currencies before taking the difference. Consumption billed in a currency the negotiated rate is not quoted in does not return, because the SKU Price dataset has no conversion rate.

```sql
WITH ObservedUsage AS (
  SELECT
    ServiceProviderName,
    SkuPriceId,
    PricingUnit,
    BillingCurrency,
    MIN(ChargePeriodStart) AS EarliestChargePeriodStart,
    SUM(PricingQuantity) AS TotalPricingQuantity,
    SUM(EffectiveCost) AS TotalEffectiveCost
  FROM CostAndUsage
  WHERE ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
    AND ChargeCategory = 'Usage'
    AND SkuPriceId IS NOT NULL
    AND CommitmentDiscountId IS NULL
  GROUP BY ServiceProviderName, SkuPriceId, PricingUnit, BillingCurrency
)
SELECT
  SP.ContractId,
  OU.ServiceProviderName,
  OU.SkuPriceId,
  OU.PricingUnit,
  OU.TotalPricingQuantity,
  OU.TotalEffectiveCost,
  SP.QuantityTierMinimum,
  SP.QuantityTierMaximum,
  SP.UnitPrice,
  SP.PricingCurrency,
  OU.TotalPricingQuantity * SP.UnitPrice AS ProjectedContractedAmount,
  OU.TotalEffectiveCost - (OU.TotalPricingQuantity * SP.UnitPrice) AS ProjectedReduction
FROM ObservedUsage OU
INNER JOIN SkuPrice SP
  ON SP.ServiceProviderName = OU.ServiceProviderName
  AND SP.SkuPriceId = OU.SkuPriceId
  AND SP.PricingUnit = OU.PricingUnit
  AND SP.PricingCurrency = OU.BillingCurrency
  AND (SP.SkuPriceEffectiveStart IS NULL OR OU.EarliestChargePeriodStart >= SP.SkuPriceEffectiveStart)
  AND (SP.SkuPriceEffectiveEnd IS NULL OR OU.EarliestChargePeriodStart < SP.SkuPriceEffectiveEnd)
WHERE SP.ServiceProviderName = ?
  AND SP.ContractId = ?
  AND SP.UnitPriceType = 'Contracted'
  AND SP.ChargeCategory = 'Usage'
ORDER BY ProjectedReduction DESC
```

### Compare Recorded Unit Prices with Published Rates

This query answers whether the unit prices recorded on each charge match the rates the catalog publishes. A mismatch that remains after the checks below can then be raised with the *service provider*. It takes a service provider, a Contract ID, and a time range through Charge Period Start and Charge Period End. It returns each usage charge in that range with its recorded List Unit Price and Contracted Unit Price. Next to them are the public and negotiated rates the SKU Price dataset publishes for the same SKU Price ID. After `Charges` is limited to the consumption the agreement covers (see below), a difference has one meaning. The unit price recorded on the charge does not match the rate the *service provider* publishes for it. One cause is a rate not updated after a price change. The contracted difference times Pricing Quantity is a gap at the contracted rate, not an amount billed. Contracted Unit Price is the rate before any *commitment discount* applies. So the result does not test Billed Cost or show whether a *commitment discount* was applied.

The query joins each charge to the public record and to the negotiated record separately. So each comparison needs one SKU Price record, and the two appear on one row only because both joins return to the same charge. `Prices` narrows the SKU Price dataset to the SKU Price IDs that appear in the charges. It also keeps only the "List" records and the "Contracted" records of the given *contract*. So each join looks only at the prices the charges need. Each charge joins to the record in force at its own Charge Period Start. So a range that crosses a price change compares each charge with the rate that applied to it. With the service provider, Contract ID, Pricing Currency, and Unit Price Type fixed, each join finds at most one record, so each charge returns once.

A rate the SKU Price dataset does not have returns null, and so does its difference, instead of reading as a match. This happens for a charge from before the earliest price the *dataset instance* keeps. It also happens for a charge billed in a currency the rate is not quoted in, and for a charge under a SKU Price ID with no "Contracted" record under the *contract*. So a null negotiated rate means the comparison could not be made. It does not mean no [*negotiated discount*](#glossary:negotiated-discount) applies. A correction without a Pricing Quantity returns a null cost difference. Giving a null Contract ID compares the list price alone.

A *service provider* can publish a separate usage record for consumption a *commitment discount* covers. A covered charge is then compared with the rates published for that record. Matching on Billing Currency compares a charge priced in another currency with a rate quoted in the Billing Currency. So a converted unit price shows a difference that is not a billing error. When the *operating model* includes pricing and billing currency differences, matching on Pricing Currency instead compares each charge in the currency it was priced in. That comparison reads Pricing Currency List Unit Price and Pricing Currency Contracted Unit Price in place of List Unit Price and Contracted Unit Price.

Nothing in the query proves that the given *contract* applies to a charge. A charge billed under a different agreement shows a difference that is not a billing error. A charge that SKU Price Eligibility excludes from the negotiated rate does too. For this reason, the comparison assumes `Charges` is first limited to the consumption the agreement covers (e.g., with a Billing Account ID filter for the *billing accounts* it covers). For a charge applied to a contract commitment, the Contract ID can instead be read from [Contract Applied](#datamodel.costandusage.contractapplied), as the relationship between the SKU Price and Cost and Usage datasets describes.

```sql
WITH Comparison AS (
  SELECT
    ? AS ServiceProviderName,
    ? AS ContractId,
    ? AS RangeStart,
    ? AS RangeEnd
),
Charges AS (
  SELECT
    CU.ServiceProviderName,
    CU.BillingAccountId,
    CU.ChargePeriodStart,
    CU.SkuPriceId,
    CU.PricingUnit,
    CU.PricingQuantity,
    CU.BillingCurrency,
    CU.ListUnitPrice,
    CU.ContractedUnitPrice
  FROM CostAndUsage CU
  INNER JOIN Comparison V
    ON CU.ServiceProviderName = V.ServiceProviderName
  WHERE CU.ChargePeriodStart >= V.RangeStart
    AND CU.ChargePeriodEnd <= V.RangeEnd
    AND CU.ChargeCategory = 'Usage'
    AND CU.SkuPriceId IS NOT NULL
),
Prices AS (
  SELECT
    SP.ServiceProviderName,
    SP.UnitPriceType,
    SP.SkuPriceId,
    SP.PricingCurrency,
    SP.SkuPriceEffectiveStart,
    SP.SkuPriceEffectiveEnd,
    SP.UnitPrice
  FROM SkuPrice SP
  INNER JOIN Comparison V
    ON SP.ServiceProviderName = V.ServiceProviderName
    AND (SP.UnitPriceType = 'List' OR (SP.ContractId = V.ContractId AND SP.UnitPriceType = 'Contracted'))
  WHERE SP.ChargeCategory = 'Usage'
    AND SP.SkuPriceId IN (SELECT SkuPriceId FROM Charges)
)
SELECT
  C.ServiceProviderName,
  C.BillingAccountId,
  C.ChargePeriodStart,
  C.SkuPriceId,
  C.PricingUnit,
  C.PricingQuantity,
  C.BillingCurrency,
  C.ListUnitPrice,
  PP.UnitPrice AS PublishedListUnitPrice,
  C.ListUnitPrice - PP.UnitPrice AS ListUnitPriceDifference,
  C.ContractedUnitPrice,
  CP.UnitPrice AS PublishedContractedUnitPrice,
  C.ContractedUnitPrice - CP.UnitPrice AS ContractedUnitPriceDifference,
  C.PricingQuantity * (C.ContractedUnitPrice - CP.UnitPrice) AS ContractedCostDifference
FROM Charges C
LEFT JOIN Prices PP
  ON PP.ServiceProviderName = C.ServiceProviderName
  AND PP.SkuPriceId = C.SkuPriceId
  AND PP.PricingCurrency = C.BillingCurrency
  AND PP.UnitPriceType = 'List'
  AND (PP.SkuPriceEffectiveStart IS NULL OR C.ChargePeriodStart >= PP.SkuPriceEffectiveStart)
  AND (PP.SkuPriceEffectiveEnd IS NULL OR C.ChargePeriodStart < PP.SkuPriceEffectiveEnd)
LEFT JOIN Prices CP
  ON CP.ServiceProviderName = C.ServiceProviderName
  AND CP.SkuPriceId = C.SkuPriceId
  AND CP.PricingCurrency = C.BillingCurrency
  AND CP.UnitPriceType = 'Contracted'
  AND (CP.SkuPriceEffectiveStart IS NULL OR C.ChargePeriodStart >= CP.SkuPriceEffectiveStart)
  AND (CP.SkuPriceEffectiveEnd IS NULL OR C.ChargePeriodStart < CP.SkuPriceEffectiveEnd)
ORDER BY ContractedCostDifference DESC NULLS LAST
```

## Version Introduced

1.5
