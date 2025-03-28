# Compare Billed and Effective Costs

## Introduced Version

1.0

## Description

FinOps Practitioners must be able to verify that proper discounting is applied for negotiated discounts, live discounts, commitment based discounts, or other discount mechanisms. A FinOps Practitioner can calculate the costs of services over a billing period and compare it to the invoice. Corrections to charges incurred in a previous billing period are excluded to avoid these items impacting the calculation. This query assists the practitioner in the process of verifying by providing the List, Billed, and Effective costs of each providers services and calculates the percentage discount for each.

## Directly Dependent Columns

* BilledCost
* BillingAccountID
* BillingAccountName
* BillingPeriodEnd
* BillingPeriodStart
* BillingCurrency
* EffectiveCost
* ListCost
* ProviderName

## Supporting Columns

* ChargeClass
* ServiceName

## Example SQL Query

```sql
SELECT
  ProviderName,
  BillingAccountId,
  BillingAccountName,
  BillingCurrency,
  ServiceName,
  SUM(EffectiveCost) AS TotalEffectiveCost,
  SUM(ListCost) AS TotalListCost,
  SUM(BilledCost) AS TotalBilledCost,
  (SUM(EffectiveCost)/SUM(BilledCost))*100 AS EffectiveDiscount
FROM focus_data_table
WHERE BillingPeriodStart >= ? AND BillingPeriodEnd < ?
  AND ChargeClass != 'Correction'
GROUP BY
  ProviderName,
  BillingAccountId,
  BillingAccountName,
  BillingCurrency,
  ServiceName
```
