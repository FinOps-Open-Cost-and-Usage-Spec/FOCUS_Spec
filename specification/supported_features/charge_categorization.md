# Charge Categorization

## Description

FOCUS supports the categorization of charges including purchases, usage, tax, credits and adjustments. It includes classification on frequency. It includes classification on correction vs normal entries

## Directly Dependent Columns

* ChargeCategory
* ChargeClass
* ChargeFrequency

## Supporting Columns

* BilledCost
* BillingAccountId
* BillingPeriodEnd
* BillingPeriodStart
* CommitmentDiscountId
* CommitmentDiscountType
* ProviderName
* ServiceCategory

## Example SQL Query

### Report on Commitment Discount Purchases

```sql
SELECT
  MIN(ChargePeriodStart) AS ChargePeriodStart,
  MAX(ChargePeriodEnd) AS ChargePeriodEnd,
  ProviderName,
  BillingAccountId,
  CommitmentDiscountId,
  CommitmentDiscountType,
  CommitmentDiscountUnit,
  CommitmentDiscountQuantity,
  ChargeFrequency,
  SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE ChargePeriodStart >= ? AND ChargePeriodEnd < ?
  AND ChargeCategory = 'Purchase'
  AND CommitmentDiscountId IS NOT NULL
GROUP BY
  ProviderName,
  BillingAccountId,
  CommitmentDiscountId,
  CommitmentDiscountType,
  CommitmentDiscountUnit,
  CommitmentDiscountQuantity,
  ChargeFrequency
```

### Report on Corrections

```sql
SELECT
  ProviderName,
  BillingAccountId,
  ChargeCategory,
  ServiceCategory,
  ServiceName,
  SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE BillingPeriodStart >= ? AND BillingPeriodEnd < ?
  AND ChargeClass = 'Correction'
GROUP BY
  ProviderName,
  BillingAccountId,
  ChargeCategory,
  ServiceCategory,
  ServiceName
```

### Report Recurring Charges

```sql
SELECT
  BillingPeriodStart,
  CommitmentDiscountId,
  CommitmentDiscountName,
  CommitmentDiscountType,
  ChargeFrequency,
  SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE BillingPeriodStart  >= ? AND BillingPeriodStart < ?
  AND ChargeFrequency = 'Recurring'
  AND CommitmentDiscountId IS NOT NULL
GROUP BY
  BillingPeriodStart,
  CommitmentDiscountId,
  CommitmentDiscountName,
  CommitmentDiscountType,
  ChargeFrequency
```

## Introduced (Version)

1.0
