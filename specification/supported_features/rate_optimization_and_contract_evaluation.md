# Rate Optimization and Contract Evaluation

## Description

FOCUS supports the evaluation of the rate an organization pays against the rates a [*service provider*](#glossary:service-provider) offers. The [SKU Price](#datamodel.skuprice) dataset carries each price as its own record, and Unit Price Type states what kind of price a record carries: "List" for the public list price, on a record with a null Contract ID, and "Contracted" for a rate negotiated under the [*contract*](#glossary:contract) its Contract ID names. A *contract* can also carry a "Base" record, a list price fixed for that *contract*, under the same SKU Price ID as a "Contracted" record. Comparing a negotiated rate with the public rate therefore pairs the two records for the same price, rather than inferring the difference from what was billed. Joining SKU Price to [Cost and Usage](#datamodel.costandusage) on SKU Price ID then places recorded consumption against the [*price list*](#glossary:price-list) it was drawn from, which is what turns a rate difference into a quantified amount.

Three optimization questions follow. The first is what negotiation reduced the rate by: subtracting Unit Price on the contracted record from Unit Price on the list record for the same price yields the reduction per unit, and Contract ID names the *contract* the negotiated rate belongs to. The two records carry their own effective dates, so the pairing tests each against the same point in time, and a negotiated rate whose effective dates differ from the public rate's pairs with the public rate in force at that moment. That difference is the negotiated portion of an agreement rather than its full effect, because the reduction from applying a [*commitment discount*](#glossary:commitment-discount) to a [*charge*](#glossary:charge) is recognized in Effective Cost on the Cost and Usage side. The [Cost Comparison](#supportedfeatures.costcomparison) supported feature covers reading the two together.

The second is whether consumption sits in the right quantity tier. Quantity Tier Minimum and Quantity Tier Maximum bound the quantity envelope a rate applies to, measured in the Pricing Unit. Quantity Tier Minimum is the exclusive lower bound and Quantity Tier Maximum is the inclusive upper bound, so a quantity falls in a tier when it is strictly greater than the minimum and no greater than the maximum. The highest tier carries a null Quantity Tier Maximum. Because adjacent tiers meet at a shared boundary with no gap, the tier above a given tier is the one whose Quantity Tier Minimum equals that tier's Quantity Tier Maximum, which is what allows the distance to the next rate to be measured. A tier is identified by its boundaries rather than by a published label, so reconciliation against a public pricing page matches on the quantity range the rate applies to.

Each tier is published as its own record with its own SKU Price ID, since the SKU Price dataset requires each SKU Price ID to carry one Quantity Tier Minimum and one Quantity Tier Maximum when the [*operating model*](#glossary:operating-model) includes quantity tier pricing. The tier queries below find the tiers of one offering through the service provider, SKU ID, Pricing Region ID, Pricing Unit, and Pricing Currency they share rather than through SKU Price ID. No column separates one set of tiers from other prices published under the same SKU ID. Commitment Discount Category marks the rates for consumption a *commitment discount* covers, but only where the *operating model* includes commitment discounts, and it does not mark which records form a set of tiers. The tier queries below therefore read public prices only from records that carry a tier boundary (a Quantity Tier Minimum above zero or a populated Quantity Tier Maximum), and assume one set of public tiers for each such combination.

The third is which purchase term to commit to. Purchase Duration Type gives the categorical term of a purchase, and Purchase Payment Model gives how the obligation is settled across "No Upfront", "Partial Upfront", and "All Upfront". Purchase Payment Model is populated where Charge Category is "Purchase", and Purchase Duration Type may be null there when the *service provider* publishes no standard term. Both are null where Charge Category is "Usage" or "Credit". The fees for each available term and settlement structure can therefore be listed side by side and weighed against the consumption that would run under them. Whether those fees differ across payment models is set by the *service provider*: some charge less in total the more of the obligation is settled upfront, and others charge the same total under every payment model, in which case the records differ only in when the obligation is paid.

> **Note:** Each payment model offered is published as a separate SKU Price record. A "Partial Upfront" purchase can be one record, or separate records for the upfront fee and the recurring fee, so comparing it with another payment model takes all of its records together rather than one of them.

The [Verification, Comparison, and Fluctuation Tracking of Unit Prices](#supportedfeatures.verificationcomparisonandfluctuationtrackingofunitprices) supported feature reads List Unit Price and Contracted Unit Price as recorded on a charge in Cost and Usage. This feature reads the public and negotiated rates from the published catalog, so the two answer different questions: what an organization was charged, against what a *service provider* offers. The query that compares recorded unit prices with published rates reads both, placing the unit prices recorded on each charge beside the rates the SKU Price dataset publishes.

### When Public and Negotiated Records are Paired

Pairing a public record with a negotiated record is needed only when the two rates are compared with each other in the catalog, with no charge to anchor them. Where the *operating model* includes them, Cost and Usage carries List Unit Price and Contracted Unit Price on every charge with a SKU Price ID, so savings on recorded consumption are measured from List Cost and Contracted Cost through the Cost Comparison supported feature, and the recorded unit prices are read through the Verification, Comparison, and Fluctuation Tracking of Unit Prices supported feature, without reading the SKU Price dataset. Checking a charge's recorded unit price against the catalog joins the charge to one SKU Price record: the "List" record for the list price, or the "Contracted" record under the *contract* that applies to the charge for the negotiated rate. Pairing applies to questions asked of the catalog itself, such as what negotiation reduces a rate by or how the two rates compare at a given quantity, which the first two queries below answer, and those queries narrow the SKU Price dataset to the service or SKU in scope before pairing.

A "Base" record under a *contract* carries a list price the *contract* fixes rather than a negotiated rate, so the queries below that read a negotiated rate select "Contracted" records, and replacing "Contracted" with "Base" in a query reads that fixed price instead.

A *commitment discount* is not carried as a negotiated rate. Its purchase fee is a record with a Charge Category of "Purchase", and consumption it covers can carry the SKU Price ID of a usage record of its own, priced at the list price, so the reduction it brings is read from Effective Cost in Cost and Usage rather than from a Unit Price. Where the rate on a usage record of this kind differs by commitment term (e.g., one year and three years), each term carries its own SKU Price ID. Where the *operating model* includes commitment discounts, both records carry a Commitment Discount Category stating whether the commitment is to an amount of usage ("Usage") or of spend ("Spend").

### Reading SKU Price ID and the Effective Date Columns

SKU Price ID identifies the stable properties of a price rather than a single row, and repeats across contracts, unit price types, pricing currencies, and time windows by design, which is what keeps prices comparable across them. Joining Cost and Usage to SKU Price on SKU Price ID alone therefore multiplies each charge by every record sharing that identifier. A SKU Price ID is also specified by the *service provider*, so two service providers can publish the same value. Every join below constrains the match further, at minimum by Service Provider Name, Pricing Currency, and the effective date window.

SKU Price Effective Start is inclusive and SKU Price Effective End is exclusive, and either may be null, in which case the window is unbounded in that direction. A charge falls under a price when its Charge Period Start is on or after SKU Price Effective Start and before SKU Price Effective End, which is the `(bound IS NULL OR comparison)` pattern the joins below use. With the service provider, Contract ID, Pricing Currency, and Unit Price Type fixed, a SKU Price ID identifies one record at any point in time. A [*dataset instance*](#glossary:dataset-instance) may carry only the prices in force when it was captured, so a charge from before the latest price change finds its record only in an earlier dataset instance retained for that purpose, and the joins below drop a charge that finds no record.

The SKU Price dataset relates a charge to a price through the charge's Pricing Currency, or through its Billing Currency when the *operating model* does not include pricing and billing currency differences. The queries that read Cost and Usage match on Billing Currency, because Effective Cost is denominated in the Billing Currency. A charge priced in a different currency from the one it is billed in therefore matches only a price the *service provider* also quotes in the Billing Currency. These queries take a time range through Charge Period Start and Charge Period End. Charge Period End is exclusive, so a charge that ends where the range ends falls inside it, and the range is tested with `ChargePeriodEnd <= ?`.

### Scope When Conditional Columns are Absent

This feature applies wherever a *service provider* publishes a SKU Price dataset, and the data model states when that dataset is present. Unit Price, Unit Price Type, and Contract ID are present in every SKU Price *dataset instance*. Reading public rates applies wherever the dataset carries "List" records, and comparing negotiated rates against public rates applies wherever it also carries "Contracted" records. "List" and "Contracted" are recommended values rather than required ones, so for a *service provider* that labels its prices with values of its own, those values take their place in the queries below. Cost and Usage carries SKU Price ID under the same condition as the SKU Price dataset, so the queries that join the two datasets apply wherever this feature does.

Conditional columns narrow this feature independently:

* Quantity tier analysis uses Quantity Tier Minimum and Quantity Tier Maximum, present when the *operating model* [includes quantity tier pricing](#operatingmodelconditions.includesquantitytierpricing). Where they are absent, a price applies at any quantity, so consumption cannot sit in the wrong tier, and resolving a tier, measuring the next tier, and comparing public and negotiated prices at a quantity do not apply. Quantity Tier Minimum and Quantity Tier Maximum also drop out of the columns the negotiation and repricing queries return.
* The tier queries also match on Pricing Region ID, present when the *operating model* [includes regions](#operatingmodelconditions.includesregions). Where it is absent, prices do not vary by location, and Pricing Region ID and the predicates on it drop out of those queries.
* Purchase term evaluation uses Purchase Duration Type and Purchase Payment Model, present when the *operating model* [includes purchases](#operatingmodelconditions.includespurchases). Where they are absent, the catalog publishes no acquisition fees, no row carries a Charge Category of "Purchase", and this capability does not apply.
* Repricing recorded consumption excludes the consumption a *commitment discount* covered, using Commitment Discount ID, present when the *operating model* [includes commitment discounts](#operatingmodelconditions.includescommitmentdiscounts). Where it is absent, no consumption is covered by a *commitment discount*, so the exclusion is unnecessary and the result is unchanged. Commitment Discount Category, which the purchase terms query returns, is present under the same condition, and where it is absent it drops out of that query.
* Matching on Billing Currency assumes a charge is priced in the currency it is billed in. Where the *operating model* [includes pricing and billing currency differences](#operatingmodelconditions.includespricing-billingcurrencydifferences), Cost and Usage also carries Pricing Currency, and matching on it instead resolves the charges the Billing Currency match leaves out, with Pricing Currency Effective Cost in place of Effective Cost when repricing.
* Comparing recorded unit prices reads List Unit Price and Contracted Unit Price from Cost and Usage. Where either column is absent, it and the differences computed from it drop out of that query.

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

The following queries use ANSI SQL, with `?` marking each input value, and may need small adjustments for a particular database engine.

> **Note:** The following queries assume FOCUS-conformant dataset artifacts. Practitioners should verify provider conformance before relying on these queries. Non-conformant dataset artifacts may produce inaccurate results.

### Measure What Negotiation Reduces the Rate By

This query takes inputs of a service provider, a Pricing Service Name, a Contract ID, and a point in time, and reports, for each consumption rate negotiated under that *contract* for the service, how far it sits below the public rate for the same price. It assumes the comparison is scoped to specific services or SKUs first, as a procurement review of an agreement usually is, rather than run across the full price list. Adding a SKU ID predicate to both sets narrows it from a service to specific SKUs. The public prices ("List" records) and the negotiated prices ("Contracted" records under that Contract ID) in force at that point in time are built as separate sets, and each negotiated record is paired with the public record that shares its service provider, SKU Price ID, and Pricing Currency. Each record's effective date window is tested against the point in time separately, so a negotiated rate whose effective dates differ from the public rate's pairs with the public rate in force at that moment, and a negotiated rate that has not yet taken effect does not appear. A negotiated rate with no public record in force for the same SKU Price ID and Pricing Currency, such as a private offer or a tier an agreement defines under its own SKU Price ID, returns with the public columns null. What it returns is the reduction attributable to negotiation, not the total reduction an organization realizes on that [*SKU*](#glossary:sku), since any further reduction from applying a *commitment discount* is recognized in Effective Cost. The reduction is measured from the public rate in force at that point in time. Where the *contract* also carries a "Base" record for the same SKU Price ID, measuring from that record instead gives the reduction from the list price the *contract* fixed.

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

This query answers the same question for one offering at a given quantity, where the negotiated tiers need not match the public ones. It takes inputs of a service provider, a SKU ID, a Pricing Region ID, a Pricing Unit, a Pricing Currency, a quantity, a point in time, and a Contract ID, then returns the public price whose tier contains that quantity alongside the negotiated price under that Contract ID whose tier contains the same quantity. Each side resolves its own tier and its own effective date window, so an agreement whose tier boundaries or effective dates differ from those of the public prices is still compared at the quantity and moment supplied. Where the *contract* prices no tier containing the quantity, or is not in force at that point in time, the negotiated columns are null.

The public side reads only records that carry a tier boundary, as described above, so an offering without quantity tiers returns no rows; for such an offering, the query above compares the negotiated rate with the public rate. A *contract* with more than one rate containing the quantity, such as a tier and a flat rate for the same offering, returns one row for each. Several sets of inputs can be compared in one run, and a set entered more than once returns its rows once.

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

This query takes inputs of a time range via Charge Period Start and Charge Period End, aggregates the consumption recorded over that range, and returns the tier the aggregated quantity falls within. Each charge is first placed in a set of tiers through the public record for the SKU Price ID it was billed under. The quantity is then aggregated across the set before the tier is resolved, because a tier boundary is evaluated against the quantity accumulated over the pricing period rather than against the quantity billed under any one SKU Price ID.

The joins carry the effective date window so that consumption matches the price that applied during the range, not every price ever published under that SKU Price ID. The window is evaluated against the earliest charge period start in the range, so the range supplied is one that falls within a single effective window. A range that crosses a price change resolves the tier against the record in force at the start of the range rather than against each record in turn. The range supplied is also a single tier accounting period, as the published pricing terms for the offering define it (e.g., one calendar month). Tier quantities accumulate within that period and start again in the next, so a longer range adds together quantities the *service provider* evaluates separately and can return a tier that no single period reached. The public tier returns with a null Contract ID, and each negotiated ("Contracted") rate that contains the aggregated quantity, whether a tier or a flat rate, returns its own row. A charge billed under a SKU Price ID that has no "List" record, such as a rate an agreement defines with its own tier boundaries, is not counted. Corrections to a closed billing period keep the charge period of the consumption they correct, so they count toward that range: a reversal reduces the quantity and cost, and a correction for usage missing from an earlier invoice adds to them. The aggregation spans every [*billing account*](#glossary:billing-account) in the range; where a *service provider* evaluates tiers for each *billing account*, adding Billing Account ID to `ChargeTierSet` and to the grouping keeps each account's quantity apart.

> **Note:** Whether the resolved rate applies only to the units inside that tier or retroactively to all units consumed is a property of the published pricing terms for the offering rather than of the tier boundaries, so the tier returned here identifies the applicable rate rather than recalculating the charge.

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

### Quantify the Effect of Reaching the Next Quantity Tier

This query takes an input of a point in time and reports, for each tier that has a tier above it, how much additional quantity separates the two and what the rate becomes on the other side. Adjacent tiers meet at a shared boundary value, so the next tier is the record in the same set of tiers whose Quantity Tier Minimum equals the current record's Quantity Tier Maximum. A tier with a null Quantity Tier Maximum is the highest tier and has no successor, so it does not appear.

The two records are matched on Contract ID as well as on the set of tiers and the boundary, so a public tier pairs with the public tier above it and a negotiated tier with the negotiated tier above it. The same point in time is supplied to the bounds of both records, so a superseded or forward-dated tier is not returned as the successor of a tier in force. A negotiated tier whose *contract* prices no tier above it does not appear; the rate beyond its maximum is set by the terms of the agreement, and the query that compares public and negotiated prices at a given quantity shows both sides at a chosen quantity.

```sql
SELECT
  CURRENT_TIER.ServiceProviderName,
  CURRENT_TIER.SkuId,
  CURRENT_TIER.PricingRegionId,
  CURRENT_TIER.ContractId,
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
FROM SkuPrice CURRENT_TIER
INNER JOIN SkuPrice NEXT_TIER
  ON NEXT_TIER.ServiceProviderName = CURRENT_TIER.ServiceProviderName
  AND NEXT_TIER.SkuId = CURRENT_TIER.SkuId
  AND (NEXT_TIER.PricingRegionId = CURRENT_TIER.PricingRegionId OR (NEXT_TIER.PricingRegionId IS NULL AND CURRENT_TIER.PricingRegionId IS NULL))
  AND NEXT_TIER.PricingUnit = CURRENT_TIER.PricingUnit
  AND NEXT_TIER.PricingCurrency = CURRENT_TIER.PricingCurrency
  AND NEXT_TIER.ChargeCategory = CURRENT_TIER.ChargeCategory
  AND (
    NEXT_TIER.ContractId = CURRENT_TIER.ContractId
    OR (NEXT_TIER.ContractId IS NULL AND CURRENT_TIER.ContractId IS NULL)
  )
  AND NEXT_TIER.QuantityTierMinimum = CURRENT_TIER.QuantityTierMaximum
  AND (NEXT_TIER.SkuPriceEffectiveStart IS NULL OR NEXT_TIER.SkuPriceEffectiveStart <= ?)
  AND (NEXT_TIER.SkuPriceEffectiveEnd IS NULL OR NEXT_TIER.SkuPriceEffectiveEnd > ?)
WHERE CURRENT_TIER.QuantityTierMaximum IS NOT NULL
  AND (CURRENT_TIER.SkuPriceEffectiveStart IS NULL OR CURRENT_TIER.SkuPriceEffectiveStart <= ?)
  AND (CURRENT_TIER.SkuPriceEffectiveEnd IS NULL OR CURRENT_TIER.SkuPriceEffectiveEnd > ?)
ORDER BY CURRENT_TIER.SkuId, CURRENT_TIER.ContractId, CURRENT_TIER.QuantityTierMinimum
```

### Evaluate the Purchase Terms Offered for a SKU

This query takes inputs of a service provider, a SKU ID, and a point in time, then lists every purchase fee published for that *SKU*, so the available terms and settlement structures can be compared before a commitment is made. Every fee is returned, told apart by Contract ID and Unit Price Type, since an agreement can discount a purchase ("Contracted") or fix its list price ("Base"). A "Partial Upfront" purchase published as separate upfront-fee and recurring-fee records returns a row for each, and the two together are the price of that payment model. Commitment Discount Category is returned so a fee for a *commitment discount* shows whether it commits to an amount of usage or of spend, which decides whether the consumption it would cover is weighed in usage or in cost.

Comparing the fee for a *commitment discount* with the public rate for the usage it would cover also takes the amount of usage one unit covers and the rate the *commitment discount* produces on that usage. The SKU Price dataset carries neither, so that comparison depends on commitment terms from outside the dataset.

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

This query takes inputs of a time range via Charge Period Start and Charge Period End, a service provider, and a Contract ID, aggregates the consumption recorded over that range that no *commitment discount* covered, and reprices it at the rate negotiated under that agreement. The difference between what that consumption cost and what it would cost at the negotiated rate is the amount at stake in the agreement.

Consumption already covered by a *commitment discount* is excluded. Its Effective Cost already reflects that commitment while the negotiated Unit Price does not, so including it would subtract the two against different baselines and report the agreement as raising cost rather than lowering it.

Consumption is repriced at the negotiated rate carried under the SKU Price ID it was billed under, since a SKU Price ID stays the same across contracts. Each tier carries its own SKU Price ID, so that rate is the negotiated rate for the tier the charge was billed in. A SKU Price ID fixes both the Quantity Tier Minimum and the Quantity Tier Maximum of its tier, so a negotiated tier whose boundaries differ from those of every public tier carries a SKU Price ID of its own, and consumption billed under the public tiers finds no negotiated rate for it. The query that compares public and negotiated prices at a given quantity finds such tiers through the SKU ID. The effective date window is evaluated against the earliest charge period start, so the range supplied is one that falls within a single effective window. Corrections to a closed billing period keep the charge period of the consumption they correct, so they count toward that range: a reversal reduces the quantity and cost, and a correction for usage missing from an earlier invoice adds to them. A *contract* does not make its negotiated rate available to all of an organization's consumption. SKU Price Eligibility decides which consumption receives the rate, and it can limit the rate to certain *billing accounts*, [*sub accounts*](#glossary:sub-account), regions, or other Cost and Usage values. This query reprices all consumption billed under the SKU Price ID that no *commitment discount* covered. Consumption the agreement does not cover stays out only when each charge is checked against SKU Price Eligibility before `ObservedUsage` adds the charges up.

Effective Cost is denominated in the Billing Currency while Unit Price is denominated in the Pricing Currency, so the join matches the two currencies before the difference is taken. Consumption billed in a currency the negotiated rate is not quoted in does not return, because the SKU Price dataset does not carry a conversion rate.

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

This query takes inputs of a service provider, a Contract ID, and a time range via Charge Period Start and Charge Period End, and returns each usage charge in that range with its recorded List Unit Price and Contracted Unit Price beside the public and negotiated rates the SKU Price dataset publishes for the same SKU Price ID. Once `Charges` is scoped to the consumption the agreement covers, as described below, a difference shows that the unit price recorded on a charge does not match the rate the *service provider* publishes for it, such as a rate not updated after a price change. The contracted difference multiplied by Pricing Quantity is a gap at the contracted rate rather than an amount billed. Contracted Unit Price is the rate before any *commitment discount* applies, so the result does not test Billed Cost or show whether a *commitment discount* was applied.

The query joins each charge to the public record and to the negotiated record separately, so each comparison needs one SKU Price record, and the two appear on one row only because both joins return to the same charge. `Prices` narrows the SKU Price dataset to the SKU Price IDs that appear in the charges, and to the "List" records and the "Contracted" records of the supplied *contract*, so each join matches against only the prices the charges need. Each charge joins to the record in force at its own Charge Period Start, so a range that crosses a price change compares each charge with the rate that applied to it. With the service provider, Contract ID, Pricing Currency, and Unit Price Type fixed, each join resolves at most one record, so each charge returns once.

A rate the SKU Price dataset does not carry returns null, and so does its difference, rather than reading as a match: a charge from before the earliest price the *dataset instance* retains, a charge billed in a currency the rate is not quoted in, and a charge under a SKU Price ID with no "Contracted" record under the *contract*. A null negotiated rate therefore means the comparison could not be made, not that no [*negotiated discount*](#glossary:negotiated-discount) applies, and a correction without a Pricing Quantity returns a null cost difference. Supplying a null Contract ID compares the list price alone. Where a *service provider* publishes a separate usage record for consumption a *commitment discount* covers, a covered charge is compared with the rates published for that record. Matching on Billing Currency compares a charge priced in another currency with a rate quoted in the Billing Currency, so a converted unit price shows a difference that is not a billing error. Where the *operating model* includes pricing and billing currency differences, matching on Pricing Currency and comparing Pricing Currency List Unit Price and Pricing Currency Contracted Unit Price instead compares each charge in the currency it was priced in.

Nothing in the query establishes that the supplied *contract* applies to a charge. A charge billed under a different agreement, or one SKU Price Eligibility excludes from the negotiated rate, shows a difference that is not a billing error, so the comparison assumes `Charges` is first scoped to the consumption the agreement covers (e.g., with a Billing Account ID predicate for the *billing accounts* it covers). For a charge applied to a contract commitment, the Contract ID can instead be read from [Contract Applied](#datamodel.costandusage.contractapplied), as the relationship between the SKU Price and Cost and Usage datasets describes.

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
