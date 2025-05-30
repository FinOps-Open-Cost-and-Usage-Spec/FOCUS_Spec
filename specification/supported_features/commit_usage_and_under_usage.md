# Commit Usage and Under Usage

## Description

FOCUS supports the tracking of commitment discounts usage and under usage, which can come in the form of commitment discounts or capacity reservations.

## Directly Dependent Columns

* CommitmentDiscountID
* CommitmentDiscountStatus
* CommitmentDiscountType
* CapacityReservationID
* CapacityReservationStatus
* CapacityReservationType

## Supporting Columns

* BilledCost
* ChargePeriodStart
* ChargePeriodEnd
* EffectiveCost
* ServiceCategory

## Example SQL Query for Commitment Discounts

```sql
SELECT
  ProviderName,
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
  ProviderName,
  BillingAccountId,
  CommitmentDiscountId,
  CommitmentDiscountType
```

## Example SQL Query for Capacity Reservations

```sql
SELECT
  ProviderName,
  BillingAccountId,
  CapacityReservationId,
  CapacityReservationStatus,
  SUM(BilledCost) AS TotalBilledCost,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE ChargePeriodStart >= ? AND ChargePeriodEnd < ?
  AND CapacityReservationStatus = 'Unused'
GROUP BY
  ProviderName,
  BillingAccountId,
  CapacityReservationId,
  CapacityReservationStatus
```

## Introduced (Version)

1.0
