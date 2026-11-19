# Charge Categorization

## Description

FOCUS supports the categorization of [*charges*](#glossary:charge) via [Charge Category](#datamodel.costandusage.chargecategory), including "Purchase", "Usage", "Tax", "Credit", and "Adjustment". It includes classification on frequency via [Charge Frequency](#datamodel.costandusage.chargefrequency). It includes classification on "Correction" vs normal entries via [Charge Class](#datamodel.costandusage.chargeclass).

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
* ServiceProviderName
* ServiceCategory

## Example SQL Queries

### Report on Commitment Discount Purchases

```sql
SELECT
  MIN(ChargePeriodStart) AS ChargePeriodStart,
  MAX(ChargePeriodEnd) AS ChargePeriodEnd,
  ServiceProviderName,
  BillingAccountId,
  CommitmentDiscountId,
  CommitmentDiscountType,
  CommitmentDiscountUnit,
  CommitmentDiscountQuantity,
  ChargeFrequency,
  SUM(BilledCost) AS TotalBilledCost
FROM CostAndUsage
WHERE ChargePeriodStart >= ? AND ChargePeriodEnd < ?
  AND ChargeCategory = 'Purchase'
  AND CommitmentDiscountId IS NOT NULL
GROUP BY
  ServiceProviderName,
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
  ServiceProviderName,
  BillingAccountId,
  ChargeCategory,
  ServiceCategory,
  ServiceName,
  SUM(BilledCost) AS TotalBilledCost
FROM CostAndUsage
WHERE BillingPeriodStart >= ? AND BillingPeriodEnd < ?
  AND ChargeClass = 'Correction'
GROUP BY
  ServiceProviderName,
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
FROM CostAndUsage
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

## Version Introduced

1.0
