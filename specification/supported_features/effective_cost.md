---
dataset: CostAndUsage
---

# Effective Cost Analysis

## Description

FOCUS enables [practitioners](#term) to analyze costs on an [accrual basis](#term:accrual-based-accounting), where expenses are recognized when [resources](#term) are consumed, [services](#term) are used, or [contract commitments](#term) are recognized, regardless of when those costs are invoiced. The [Effective Cost](#col) column reflects all applicable pricing adjustments and distributes the cost of [covering charges](#term) (one-time or recurring purchases) to the [covered charges](#term) they offset.

For [charges](#term) that are not [covered charges](#term), [Effective Cost](#col) reflects the same amount as [Billed Cost](#col). For [covering charges](#term) (e.g., [commitment discount](#term) purchases, prepayments, or marketplace purchases), [Effective Cost](#col) is 0 because their cost is recognized on the [covered charges](#term) instead. In [commitment discount](#term) scenarios, [Commitment Discount Status](#col) distinguishes whether amortized cost was allocated to consumed [resources](#term) or [services](#term) ("Used") or remained unallocated ("Unused").

[Effective Cost](#col) is commonly used for *accrual-based* reporting, cost allocation, chargeback, and spending trend analysis. For scenarios involving [commitment discounts](#term) across different payment models, see [Examples: Commitment Discount Flexibility](#appendix.examples:commitmentdiscountflexibility). For marketplace and SaaS scenarios, see [Examples: SaaS](#appendix.examples:saas).

## Directly Dependent Columns

* [EffectiveCost](#col)

## Supporting Columns

* [BillingPeriodEnd](#col)
* [BillingPeriodStart](#col)
* [ChargeCategory](#col)
* [ChargePeriodEnd](#col)
* [ChargePeriodStart](#col)
* [CommitmentDiscountId](#col)
* [CommitmentDiscountStatus](#col)
* [ConsumedQuantity](#col)
* [ConsumedUnit](#col)
* [PricingQuantity](#col)
* [RegionName](#col)
* [ServiceName](#col)
* [ServiceProviderName](#col)
* [SkuId](#col)

## Example SQL Queries

[Effective Cost](#col) can be analyzed using [billing period](#term) or [charge period](#term) time filters. [Billing period](#term) aligns with invoice cycles and is useful for financial reporting. [Charge period](#term) captures when [resources](#term) were consumed or commitments were recognized, which is more precise for consumption-based analysis.

### Effective Cost by Service and Region

Aggregates [Effective Cost](#col) by [billing period](#term) to align *accrual-based* cost reporting with invoice cycles.

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

Analyzes [commitment discount](#term) [amortization](#term) by [charge period](#term), capturing costs based on when [resources](#term) were consumed.

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

Compares the quantity consumed with the quantity priced for the same usage [charges](#term), per SKU. [Consumed Quantity](#col) and [Consumed Unit](#col) measure what was used (e.g., hours, GB), while [Pricing Quantity](#col) and [Pricing Unit](#col) measure what the unit price was applied to, which can use a different unit or block size (e.g., GB-months, blocks of 1,000 requests). Dividing [Effective Cost](#col) by each quantity gives the cost per unit consumed and the effective price per unit priced. Rows where [Consumed Quantity](#col) is null (e.g., when [Charge Category](#col) is not ["Usage"](#val:CostAndUsage.ChargeCategory), or when [Commitment Discount Status](#col) is ["Unused"](#val:CostAndUsage.CommitmentDiscountStatus)) are excluded.

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
FROM CostAndUsage
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
