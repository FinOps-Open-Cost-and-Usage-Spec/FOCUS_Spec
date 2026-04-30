# Effective Cost Analysis

## Description

FOCUS enables practitioners to analyze costs on an [*accrual basis*](#glossary:accrual-based-accounting), where expenses are recognized when [*resources*](#glossary:resource) are consumed, [*services*](#glossary:service) are used, or [*contract commitments*](#glossary:contract-commitment) are recognized, regardless of when those costs are invoiced. The [EffectiveCost](#datasets.costandusage.effectivecost) column reflects all applicable pricing adjustments and distributes the cost of [*covering charges*](#glossary:covering-charge) (one-time or recurring purchases) to the [*covered charges*](#glossary:covered-charge) they offset.

For [*charges*](#glossary:charge) that are not *covered charges*, EffectiveCost reflects the same amount as [BilledCost](#datasets.costandusage.billedcost). For *covering charges* (e.g., [*commitment discount*](#glossary:commitment-discount) purchases, prepayments, or marketplace purchases), EffectiveCost is 0 because their cost is recognized on the *covered charges* instead. In *commitment discount* scenarios, [CommitmentDiscountStatus](#datasets.costandusage.commitmentdiscountstatus) distinguishes whether amortized cost was allocated to consumed *resources* or *services* ("Used") or remained unallocated ("Unused").

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

EffectiveCost can be analyzed using [*billing period*](#glossary:billing-period) or [*charge period*](#glossary:chargeperiod) time filters. Billing period aligns with invoice cycles and is useful for financial reporting. Charge period captures when resources were consumed or commitments were recognized, which is more precise for consumption-based analysis.

### Effective Cost by Service and Region

Aggregates EffectiveCost by billing period to align accrual-based cost reporting with invoice cycles.

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

Analyzes commitment discount amortization by charge period, capturing costs based on when resources were consumed.

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

## Version Introduced

0.5

## Version Updated

1.4
