# Effective Cost Analysis

## Description

FOCUS enables [*practitioners*](#glossary:practitioner) to analyze costs on an [*accrual basis*](#glossary:accrual-based-accounting), where expenses are recognized when [*resources*](#glossary:resource) are consumed, [*services*](#glossary:service) are used, or [*contract commitments*](#glossary:contract-commitment) are recognized, regardless of when those costs are invoiced. The [Effective Cost](#datamodel.costandusage.effectivecost) column reflects all applicable pricing adjustments and distributes the cost of [*covering charges*](#glossary:covering-charge) (one-time or recurring purchases) to the [*covered charges*](#glossary:covered-charge) they offset.

For [*charges*](#glossary:charge) that are not *covered charges*, Effective Cost reflects the same amount as [Billed Cost](#datamodel.costandusage.billedcost). For *covering charges* (e.g., [*commitment discount*](#glossary:commitment-discount) purchases, prepayments, or marketplace purchases), Effective Cost is 0 because their cost is recognized on the *covered charges* instead. In *commitment discount* scenarios, [Commitment Discount Status](#datamodel.costandusage.commitmentdiscountstatus) distinguishes whether amortized cost was allocated to consumed *resources* or *services* ("Used") or remained unallocated ("Unused").

Effective Cost is commonly used for *accrual-based* reporting, cost allocation, chargeback, and spending trend analysis. For scenarios involving *commitment discounts* across different payment models, see [Examples: Commitment Discount Flexibility](#appendix.examples:commitmentdiscountflexibility). For marketplace and SaaS scenarios, see [Examples: SaaS](#appendix.examples:saas).

## Directly Dependent Columns

* EffectiveCost

## Supporting Columns

* BillingPeriodEnd
* BillingPeriodStart
* ChargeCategory
* ChargePeriodEnd
* ChargePeriodStart
* CommitmentDiscountId
* CommitmentDiscountStatus
* ConsumedQuantity
* ConsumedUnit
* PricingQuantity
* RegionName
* ServiceName
* ServiceProviderName
* SkuId

## Example SQL Queries

Effective Cost can be analyzed using [*billing period*](#glossary:billing-period) or [*charge period*](#glossary:chargeperiod) time filters. *Billing period* aligns with invoice cycles and is useful for financial reporting. *Charge period* captures when *resources* were consumed or commitments were recognized, which is more precise for consumption-based analysis.

### Effective Cost by Service and Region

Aggregates Effective Cost by *billing period* to align *accrual-based* cost reporting with invoice cycles.

```sql
SELECT
  ServiceProviderName,
  BillingPeriodStart,
  BillingPeriodEnd,
  ServiceCategory,
  ServiceName,
  RegionId,
  RegionName,
  PricingUnit,
  SUM(EffectiveCost) AS TotalEffectiveCost,
  SUM(PricingQuantity) AS TotalPricingQuantity
FROM CostAndUsage
WHERE BillingPeriodStart >= ? AND BillingPeriodEnd < ?
GROUP BY
  ServiceProviderName,
  BillingPeriodStart,
  BillingPeriodEnd,
  ServiceCategory,
  ServiceName,
  RegionId,
  RegionName,
  PricingUnit
```

### Commitment Discount Effective Cost Breakdown

Analyzes *commitment discount* [*amortization*](#glossary:amortization) by *charge period*, capturing costs based on when *resources* were consumed.

```sql
SELECT
  ServiceProviderName,
  CommitmentDiscountId,
  CommitmentDiscountStatus,
  ChargePeriodStart,
  ChargePeriodEnd,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM CostAndUsage
WHERE ChargePeriodStart >= ? AND ChargePeriodEnd < ?
  AND CommitmentDiscountId IS NOT NULL
  AND ChargeCategory = 'Usage'
GROUP BY
  ServiceProviderName,
  CommitmentDiscountId,
  CommitmentDiscountStatus,
  ChargePeriodStart,
  ChargePeriodEnd
```

### Effective Cost by Consumed Quantity and Pricing Quantity

Compares the quantity consumed with the quantity priced for the same usage *charges*, per SKU. [Consumed Quantity](#datamodel.costandusage.consumedquantity) and [Consumed Unit](#datamodel.costandusage.consumedunit) measure what was used (e.g., hours, GB), while [Pricing Quantity](#datamodel.costandusage.pricingquantity) and [Pricing Unit](#datamodel.costandusage.pricingunit) measure what the unit price was applied to, which can use a different unit or block size (e.g., GB-months, blocks of 1,000 requests). Dividing Effective Cost by each quantity gives the cost per unit consumed and the effective price per unit priced. Rows where Consumed Quantity is null (e.g., when [Charge Category](#datamodel.costandusage.chargecategory) is not "Usage", or when Commitment Discount Status is "Unused") are excluded.

```sql
SELECT
  ServiceProviderName,
  BillingCurrency,
  ServiceName,
  SkuId,
  ConsumedUnit,
  PricingUnit,
  SUM(ConsumedQuantity) AS TotalConsumedQuantity,
  SUM(PricingQuantity) AS TotalPricingQuantity,
  SUM(EffectiveCost) AS TotalEffectiveCost,
  SUM(EffectiveCost) / NULLIF(SUM(ConsumedQuantity), 0) AS EffectiveCostPerConsumedUnit,
  SUM(EffectiveCost) / NULLIF(SUM(PricingQuantity), 0) AS EffectiveCostPerPricingUnit
FROM focus_data_table
WHERE ChargePeriodStart >= ? AND ChargePeriodEnd < ?
  AND ChargeCategory = 'Usage'
  AND ConsumedQuantity IS NOT NULL
GROUP BY
  ServiceProviderName,
  BillingCurrency,
  ServiceName,
  SkuId,
  ConsumedUnit,
  PricingUnit
```

## Version Introduced

0.5

## Version Updated

1.4
