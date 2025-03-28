# Provider Services

## Introduced Version

0.5

## Description

The FOCUS spec supports providers specifying the services and product offerings that they provide their customers that align with the names practitioners are familiar with. This empowers practitioners to analyze cost by service, report service costs by subaccount, forecast based on historical trends by service, and verify accuracy of services charged across providers.

## Directly Dependent Columns

* ServiceCategory
* ServiceName
* ServiceSubcategory

## Supporting Columns

* Provider
* SkuId

## Example SQL Query

```sql
SELECT
  BillingPeriodStart,
  ProviderName,
  SubAccountId,
  SubAccountName,
  ServiceName,
  SUM(BilledCost) AS TotalBilledCost,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE ServiceName = ?
  AND BillingPeriodStart >= ? AND BillingPeriodStart < ?
GROUP BY
  BillingPeriodStart,
  ProviderName,
  SubAccountId,
  SubAccountName,
  ServiceName
ORDER BY MonthlyCost DESC
```
