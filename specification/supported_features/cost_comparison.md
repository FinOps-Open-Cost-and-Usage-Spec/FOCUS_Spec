# Cost Comparison

## Introduced Version

0.5

## Description

FOCUS supports the comparison of cost columns in order to identify savings, amortization, or other constructs.

## Directly Dependent Columns

* BilledCost
* ContractedCost
* EffectiveCost
* ListCost

## Supporting Columns

* BillingAccountId
* BillingAccountName
* BillingCurrency
* BillingPeriodEnd
* BillingPeriodStart
* ChargePeriodEnd
* ChargePeriodStart
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
GROUP BY
  ProviderName,
  BillingAccountId,
  BillingAccountName,
  BillingCurrency,
  ServiceName
```
