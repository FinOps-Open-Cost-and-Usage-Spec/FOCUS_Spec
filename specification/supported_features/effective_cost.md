# Effective Cost Analysis

## Description

FOCUS enables practitioners to analyze costs on an [*accrual basis*](#glossary:accrual-based-accounting), where expenses are recognized when [*resources*](#glossary:resource) are consumed, [*services*](#glossary:service) are used, or [*contract commitments*](#glossary:contract-commitment) are recognized, regardless of when those costs are invoiced. The [EffectiveCost](#datasets.costandusage.effectivecost) column reflects all applicable pricing adjustments and distributes the cost of related purchases (one-time or recurring) to the [*charges*](#glossary:charge) they cover.

For *charges* not covered by related purchases, EffectiveCost reflects the same amount as [BilledCost](#datasets.costandusage.billedcost). When purchases cover related eligible *charges* (e.g., [*commitment discounts*](#glossary:commitment-discount), prepaid marketplace subscriptions), the purchase row has an EffectiveCost of 0, and the covered usage rows carry the recognized cost. For *commitment discount* scenarios, usage rows with [CommitmentDiscountStatus](#datasets.costandusage.commitmentdiscountstatus) "Used" represent the amortized portion allocated to consumed *resources* or *services*. Usage rows with CommitmentDiscountStatus "Unused" represent the amortized portion not allocated to any *resources* or *services*.

EffectiveCost is commonly used for *accrual-based* reporting, cost allocation, chargeback, and spending trend analysis. For scenarios involving *commitment discounts* across different payment models, see [Examples: Commitment Discount Flexibility](#appendix.examples:commitmentdiscountflexibility). For marketplace and SaaS scenarios, see [Examples: SaaS](#appendix.examples:saas).

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

## Example SQL Queries

### Effective Cost by Service and Region

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
FROM focus_data_table
WHERE BillingPeriodStart >= ? AND BillingPeriodEnd <= ?
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

```sql
SELECT
  ServiceProviderName,
  CommitmentDiscountId,
  CommitmentDiscountStatus,
  ChargePeriodStart,
  ChargePeriodEnd,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
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

## Introduced (Version)

0.5

## Updated (Version)

1.4
