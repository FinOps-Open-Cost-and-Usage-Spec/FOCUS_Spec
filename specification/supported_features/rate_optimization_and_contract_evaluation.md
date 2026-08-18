# Rate Optimization and Contract Evaluation

## Description

FOCUS supports the evaluation of the rate an organization pays against the rates a [*service provider*](#glossary:service-provider) offers. The [SKU Price](#datamodel.skuprice) dataset carries the public rate and the negotiated rate as two columns on the same record, List Unit Price and Contracted Unit Price, so the difference between them is read directly rather than inferred from what was billed or reassembled from two rows. Joining SKU Price to [Cost and Usage](#datamodel.costandusage) on SKU Price ID then places recorded consumption against the price list it was drawn from, which is what turns a rate difference into a quantified amount.

Three optimization questions follow from that pairing. The first is what negotiation reduced the rate by: subtracting Contracted Unit Price from List Unit Price on a record yields the reduction per unit, and Contract ID names the [*contract*](#glossary:contract) the negotiated rate belongs to. That difference is the negotiated portion of an agreement rather than its full effect, because the reduction from applying a [*commitment discount*](#glossary:commitment-discount) to a charge is recognized in Effective Cost on the Cost and Usage side. The [Cost Comparison](#supportedfeatures.costcomparison) supported feature covers reading the two together.

The second is whether consumption sits in the right quantity tier. Quantity Tier Minimum and Quantity Tier Maximum bound the quantity envelope a rate applies to, measured in the Pricing Unit. Quantity Tier Minimum is the exclusive lower bound and Quantity Tier Maximum is the inclusive upper bound, so a quantity falls in a tier when it is strictly greater than the minimum and no greater than the maximum. The highest tier carries a null Quantity Tier Maximum. Because adjacent tiers meet at a shared boundary with no gap, the tier above a given tier is the one whose Quantity Tier Minimum equals that tier's Quantity Tier Maximum, which is what allows the distance to the next rate to be measured. A tier is identified by its boundaries rather than by a published label, so reconciliation against a public pricing page matches on the quantity range the rate applies to.

The third is which purchase term to commit to. Purchase Duration Type gives the categorical term of a purchase, and Purchase Payment Model gives how the obligation is settled across "No Upfront", "Partial Upfront", and "All Upfront". Purchase Payment Model is populated where Charge Category is "Purchase", and Purchase Duration Type may be null there when the *service provider* publishes no standard term. Both are null where Charge Category is "Usage" or "Credit". The fees for each available term and settlement structure can therefore be listed side by side and weighed against the consumption that would run under them.

> **Note:** A "Partial Upfront" purchase is typically represented across more than one SKU Price record, one for the upfront fee and a separate record for the recurring fee. Summing the price across the records for a single purchase, rather than reading a single record, is what produces the total obligation for that term.

The [Verification, Comparison, and Fluctuation Tracking of Unit Prices](#supportedfeatures.verificationcomparisonandfluctuationtrackingofunitprices) supported feature reads List Unit Price and Contracted Unit Price as recorded on a charge in Cost and Usage. This feature reads them from the published catalog, so the two answer different questions: what an organization was charged, against what a *service provider* offers.

### Reading SKU Price ID and the Effective Date Columns

SKU Price ID identifies the stable properties of a price rather than a single row, and repeats across contracts, quantity tiers, pricing currencies, and time windows by design, which is what keeps prices comparable across them. Joining Cost and Usage to SKU Price on SKU Price ID alone therefore multiplies each charge by every record sharing that identifier. Every join below constrains the match further, at minimum by the effective date window.

SKU Price Effective Start is inclusive and SKU Price Effective End is exclusive, and either may be null, in which case the window is unbounded in that direction. A charge falls under a price when its Charge Period Start is on or after SKU Price Effective Start and before SKU Price Effective End, which is the `(bound IS NULL OR comparison)` pattern the joins below use. Where a *service provider* publishes prices in more than one currency or across more than one quantity tier, the join needs a predicate on those columns as well.

### Scope When Conditional Columns are Absent

This feature applies wherever a *service provider* publishes a SKU Price dataset, and the data model states when that dataset is present. Measuring consumption against a rate additionally uses SKU Price ID in Cost and Usage; where that column is absent, the SKU Price dataset still supports rate and tier comparison on its own, and only the queries that join the two datasets do not apply. Repricing recorded consumption further uses Commitment Discount ID, present when the *operating model* [includes commitment discounts](#conditions.includescommitmentdiscounts); where it is absent, no consumption is covered by a *commitment discount*, so the exclusion that query applies is unnecessary and its result is unchanged.

Each of the three capabilities above rests on a conditional column, and each narrows independently:

* Comparing negotiated rates against public rates uses Contracted Unit Price and Contract ID, present when the [*operating model*](#glossary:operating-model) [includes contract commitments](#conditions.includescontractcommitments). Where they are absent, every published price is a public rate carried in List Unit Price, so there is no negotiated rate to evaluate and this capability does not apply.
* Quantity tier analysis uses Quantity Tier Minimum and Quantity Tier Maximum, present when the *operating model* [includes quantity tier pricing](#conditions.includesquantitytierpricing). Where they are absent, a SKU Price ID carries one rate that applies at any quantity, so consumption cannot sit in the wrong tier and this capability does not apply. Repricing consumption at a contracted rate resolves the tier through the same two columns; where they are absent, an agreement carries one rate per SKU Price ID and the tier predicates drop out.
* Purchase term evaluation uses Purchase Duration Type and Purchase Payment Model, present when the *operating model* [includes purchases](#conditions.includespurchases). Where they are absent, the catalog publishes no acquisition fees, no row carries a Charge Category of "Purchase", and this capability does not apply.

List Unit Price is present in every SKU Price dataset instance, so reading and comparing public rates over time holds regardless of which of the three conditions a *service provider* meets.

## Directly Dependent Columns

* [SkuPrice](#datamodel.skuprice)
  * ContractedUnitPrice
  * ContractId
  * ListUnitPrice
  * PurchaseDurationType
  * PurchasePaymentModel
  * QuantityTierMaximum
  * QuantityTierMinimum

## Supporting Columns

* [SkuPrice](#datamodel.skuprice)
  * ChargeCategory
  * PricingCurrency
  * PricingUnit
  * ServiceProviderName
  * SkuId
  * SkuPriceDescription
  * SkuPriceEffectiveEnd
  * SkuPriceEffectiveStart
  * SkuPriceId
* [CostAndUsage](#datamodel.costandusage)
  * ChargeCategory
  * ChargePeriodEnd
  * ChargePeriodStart
  * CommitmentDiscountId
  * EffectiveCost
  * PricingQuantity
  * PricingUnit
  * SkuPriceId

## Example SQL Queries

> Note: The following examples are informative and non-normative. They do not define requirements.

The following queries use ANSI SQL and run against any major database engine without modification.

> Important Consideration: The following queries assume FOCUS-conformant dataset artifacts. Practitioners should verify provider conformance before relying on these queries. Non-conformant dataset artifacts may produce inaccurate results.

### Measure What Negotiation Reduces the Rate By

This query takes an input of a point in time and reports, for each agreement, how far the negotiated rate sits below the public rate. Both prices are properties of the same record, so no self-join is needed and no reassembly step can pair the wrong rows. What it returns is the reduction attributable to negotiation, not the total reduction an organization realizes on that SKU, since any further reduction from applying a *commitment discount* is recognized in Effective Cost.

```sql
SELECT
  ServiceProviderName,
  ContractId,
  SkuPriceId,
  PricingUnit,
  PricingCurrency,
  ListUnitPrice,
  ContractedUnitPrice,
  ListUnitPrice - ContractedUnitPrice AS UnitPriceReduction,
  (ListUnitPrice - ContractedUnitPrice) / NULLIF(ListUnitPrice, 0) AS DiscountRate
FROM SkuPrice
WHERE ContractedUnitPrice IS NOT NULL
  AND ChargeCategory = 'Usage'
  AND (SkuPriceEffectiveStart IS NULL OR SkuPriceEffectiveStart <= ?)
  AND (SkuPriceEffectiveEnd IS NULL OR SkuPriceEffectiveEnd > ?)
ORDER BY DiscountRate DESC
```

### Resolve the Quantity Tier That Applies to Observed Consumption

This query takes inputs of a time range via Charge Period Start and Charge Period End, aggregates consumption per SKU Price ID over that range, and returns the tier each aggregated quantity falls within. The quantity is aggregated before the tier is resolved, because a tier boundary is evaluated against the quantity accumulated over the pricing period rather than against the quantity on a single charge.

The join carries the effective date window so that consumption matches the price that applied during the range, not every price ever published under that SKU Price ID. A SKU Price ID that also carries a negotiated rate on the resolved tier returns one row per agreement, and Contract ID is null on the public record.

> **Note:** Whether the resolved rate applies only to the units inside that tier or retroactively to all units consumed is a property of the published pricing terms for the offering rather than of the tier boundaries, so the tier returned here identifies the applicable rate rather than recalculating the charge.

```sql
WITH PeriodQuantity AS (
  SELECT
    SkuPriceId,
    PricingUnit,
    MIN(ChargePeriodStart) AS EarliestChargePeriodStart,
    SUM(PricingQuantity) AS TotalPricingQuantity,
    SUM(EffectiveCost) AS TotalEffectiveCost
  FROM CostAndUsage
  WHERE ChargePeriodStart >= ? AND ChargePeriodEnd < ?
    AND ChargeCategory = 'Usage'
    AND SkuPriceId IS NOT NULL
  GROUP BY SkuPriceId, PricingUnit
)
SELECT
  PQ.SkuPriceId,
  PQ.PricingUnit,
  PQ.TotalPricingQuantity,
  PQ.TotalEffectiveCost,
  SP.ContractId,
  SP.QuantityTierMinimum,
  SP.QuantityTierMaximum,
  SP.ListUnitPrice,
  SP.ContractedUnitPrice
FROM PeriodQuantity PQ
INNER JOIN SkuPrice SP
  ON PQ.SkuPriceId = SP.SkuPriceId
  AND PQ.PricingUnit = SP.PricingUnit
  AND PQ.TotalPricingQuantity > SP.QuantityTierMinimum
  AND (SP.QuantityTierMaximum IS NULL OR PQ.TotalPricingQuantity <= SP.QuantityTierMaximum)
  AND (SP.SkuPriceEffectiveStart IS NULL OR PQ.EarliestChargePeriodStart >= SP.SkuPriceEffectiveStart)
  AND (SP.SkuPriceEffectiveEnd IS NULL OR PQ.EarliestChargePeriodStart < SP.SkuPriceEffectiveEnd)
ORDER BY PQ.TotalEffectiveCost DESC
```

### Quantify the Effect of Reaching the Next Quantity Tier

This query takes an input of a point in time and reports, for each tier that has a tier above it, how much additional quantity separates the two and what the rate becomes on the other side. Adjacent tiers meet at a shared boundary value, so the next tier is the record whose Quantity Tier Minimum equals the current record's Quantity Tier Maximum. A tier with a null Quantity Tier Maximum is the highest tier and has no successor, so it does not appear.

The two records are matched on Contract ID as well as on the boundary, so a public tier pairs with the public tier above it and a negotiated tier with the negotiated tier above it. The same point in time is supplied to the bounds of both records, so a superseded or forward-dated tier is not returned as the successor of a tier in force.

```sql
SELECT
  CURRENT_TIER.SkuPriceId,
  CURRENT_TIER.ContractId,
  CURRENT_TIER.PricingUnit,
  CURRENT_TIER.PricingCurrency,
  CURRENT_TIER.QuantityTierMinimum AS CurrentTierMinimum,
  CURRENT_TIER.QuantityTierMaximum AS CurrentTierMaximum,
  CURRENT_TIER.ListUnitPrice AS CurrentListUnitPrice,
  NEXT_TIER.QuantityTierMaximum AS NextTierMaximum,
  NEXT_TIER.ListUnitPrice AS NextListUnitPrice,
  CURRENT_TIER.ListUnitPrice - NEXT_TIER.ListUnitPrice AS ListUnitPriceReduction,
  CURRENT_TIER.QuantityTierMaximum - CURRENT_TIER.QuantityTierMinimum AS TierWidth
FROM SkuPrice CURRENT_TIER
INNER JOIN SkuPrice NEXT_TIER
  ON CURRENT_TIER.ServiceProviderName = NEXT_TIER.ServiceProviderName
  AND CURRENT_TIER.SkuPriceId = NEXT_TIER.SkuPriceId
  AND CURRENT_TIER.PricingCurrency = NEXT_TIER.PricingCurrency
  AND CURRENT_TIER.QuantityTierMaximum = NEXT_TIER.QuantityTierMinimum
  AND (
    CURRENT_TIER.ContractId = NEXT_TIER.ContractId
    OR (CURRENT_TIER.ContractId IS NULL AND NEXT_TIER.ContractId IS NULL)
  )
  AND (NEXT_TIER.SkuPriceEffectiveStart IS NULL OR NEXT_TIER.SkuPriceEffectiveStart <= ?)
  AND (NEXT_TIER.SkuPriceEffectiveEnd IS NULL OR NEXT_TIER.SkuPriceEffectiveEnd > ?)
WHERE CURRENT_TIER.QuantityTierMaximum IS NOT NULL
  AND (CURRENT_TIER.SkuPriceEffectiveStart IS NULL OR CURRENT_TIER.SkuPriceEffectiveStart <= ?)
  AND (CURRENT_TIER.SkuPriceEffectiveEnd IS NULL OR CURRENT_TIER.SkuPriceEffectiveEnd > ?)
ORDER BY CURRENT_TIER.SkuPriceId, CURRENT_TIER.QuantityTierMinimum
```

### Evaluate the Purchase Terms Offered for a SKU

This query takes inputs of a SKU ID and a point in time, then lists every purchase fee published for that SKU, so the available terms and settlement structures can be compared before a commitment is made. Both the public fee and any negotiated fee are returned, since a purchase can itself be discounted under an agreement.

```sql
SELECT
  SkuId,
  SkuPriceId,
  SkuPriceDescription,
  PurchaseDurationType,
  PurchasePaymentModel,
  PricingUnit,
  PricingCurrency,
  ListUnitPrice,
  ContractedUnitPrice
FROM SkuPrice
WHERE SkuId = ?
  AND ChargeCategory = 'Purchase'
  AND (SkuPriceEffectiveStart IS NULL OR SkuPriceEffectiveStart <= ?)
  AND (SkuPriceEffectiveEnd IS NULL OR SkuPriceEffectiveEnd > ?)
ORDER BY PurchaseDurationType, PurchasePaymentModel, SkuPriceId
```

### Project the Effect of Moving Consumption to a Contracted Rate

This query takes inputs of a time range via Charge Period Start and Charge Period End and a Contract ID, aggregates the consumption recorded over that range that no *commitment discount* covered, and reprices it at the negotiated rate carried under that agreement. The difference between what that consumption cost and what it would cost at the contracted rate is the amount at stake in the agreement, which is what a purchase fee returned by the preceding query is weighed against.

Consumption already covered by a *commitment discount* is excluded. Its Effective Cost already reflects that commitment while Contracted Unit Price does not, so including it would subtract the two against different baselines and report the agreement as raising cost rather than lowering it.

The join resolves the quantity tier the aggregated consumption falls into, so an agreement that negotiated several tiers reprices at the one rate that applies rather than once per tier.

```sql
WITH ObservedUsage AS (
  SELECT
    SkuPriceId,
    PricingUnit,
    MIN(ChargePeriodStart) AS EarliestChargePeriodStart,
    SUM(PricingQuantity) AS TotalPricingQuantity,
    SUM(EffectiveCost) AS TotalEffectiveCost
  FROM CostAndUsage
  WHERE ChargePeriodStart >= ? AND ChargePeriodEnd < ?
    AND ChargeCategory = 'Usage'
    AND SkuPriceId IS NOT NULL
    AND CommitmentDiscountId IS NULL
  GROUP BY SkuPriceId, PricingUnit
)
SELECT
  SP.ContractId,
  OU.SkuPriceId,
  OU.PricingUnit,
  OU.TotalPricingQuantity,
  OU.TotalEffectiveCost,
  SP.QuantityTierMinimum,
  SP.QuantityTierMaximum,
  SP.ContractedUnitPrice,
  SP.PricingCurrency,
  OU.TotalPricingQuantity * SP.ContractedUnitPrice AS ProjectedContractedAmount,
  OU.TotalEffectiveCost - (OU.TotalPricingQuantity * SP.ContractedUnitPrice) AS ProjectedReduction
FROM ObservedUsage OU
INNER JOIN SkuPrice SP
  ON OU.SkuPriceId = SP.SkuPriceId
  AND OU.PricingUnit = SP.PricingUnit
  AND OU.TotalPricingQuantity > SP.QuantityTierMinimum
  AND (SP.QuantityTierMaximum IS NULL OR OU.TotalPricingQuantity <= SP.QuantityTierMaximum)
  AND (SP.SkuPriceEffectiveStart IS NULL OR OU.EarliestChargePeriodStart >= SP.SkuPriceEffectiveStart)
  AND (SP.SkuPriceEffectiveEnd IS NULL OR OU.EarliestChargePeriodStart < SP.SkuPriceEffectiveEnd)
WHERE SP.ContractId = ?
  AND SP.ContractedUnitPrice IS NOT NULL
  AND SP.ChargeCategory = 'Usage'
ORDER BY ProjectedReduction DESC
```

## Version Introduced

1.5
