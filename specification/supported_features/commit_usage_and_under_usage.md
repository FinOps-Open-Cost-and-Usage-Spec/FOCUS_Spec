# Commit Usage and Under Usage

## Description

FOCUS supports the tracking of commitment discounts usage and under usage, which can come in the form of commitment discounts or capacity reservations.

## Directly Dependent Columns

* CommitmentDiscountId
* CommitmentDiscountStatus
* CommitmentDiscountType
* CapacityReservationId
* CapacityReservationStatus

## Supporting Columns

* BilledCost
* ChargePeriodStart
* ChargePeriodEnd
* EffectiveCost

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
FROM focus_data_table
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
FROM focus_data_table
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
