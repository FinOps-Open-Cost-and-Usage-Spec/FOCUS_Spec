# Commit Usage and Under Usage

## Introduced Version
1.0

## Description
The FOCUS spec supports the tracking of committed use discounts usage and underusage, which can come in the form of commitment discounts, or capacity reservations. 

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
```SELECT
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
```
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
