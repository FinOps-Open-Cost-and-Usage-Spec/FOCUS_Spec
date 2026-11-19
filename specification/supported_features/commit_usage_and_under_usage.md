---
dataset: CostAndUsage
---

# Commit Usage and Under Usage

## Description

FOCUS supports the tracking of [commitment discounts](#term) usage and under usage, which can come in the form of [commitment discounts](#term) or [capacity reservations](#term).

## Directly Dependent Columns

* [CommitmentDiscountId](#col)
* [CommitmentDiscountStatus](#col)
* [CommitmentDiscountType](#col)
* [CapacityReservationId](#col)
* [CapacityReservationStatus](#col)

## Supporting Columns

* [BilledCost](#col)
* [ChargePeriodStart](#col)
* [ChargePeriodEnd](#col)
* [EffectiveCost](#col)

## Example SQL Queries

### Report on Unused Commitment Discounts

```sql
SELECT
  ServiceProviderName,
  BillingAccountId,
  CommitmentDiscountId,
  CommitmentDiscountType,
  CommitmentDiscountStatus,
  SUM(BilledCost) AS TotalBilledCost,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM CostAndUsage
WHERE ChargePeriodStart >= ? AND ChargePeriodEnd < ?
  AND CommitmentDiscountStatus = 'Unused'
GROUP BY
  ServiceProviderName,
  BillingAccountId,
  CommitmentDiscountId,
  CommitmentDiscountType,
  CommitmentDiscountStatus
```

### Report on Unused Capacity Reservations

```sql
SELECT
  ServiceProviderName,
  BillingAccountId,
  CapacityReservationId,
  CapacityReservationStatus,
  SUM(BilledCost) AS TotalBilledCost,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM CostAndUsage
WHERE ChargePeriodStart >= ? AND ChargePeriodEnd < ?
  AND CapacityReservationStatus = 'Unused'
GROUP BY
  ServiceProviderName,
  BillingAccountId,
  CapacityReservationId,
  CapacityReservationStatus
```

## Version Introduced

1.0
