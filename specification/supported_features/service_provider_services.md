---
dataset: CostAndUsage
---

# Service Provider Services

## Description

FOCUS supports [service providers](#term) specifying the [services](#term) and product offerings that they provide their customers that align with the names [practitioners](#term) are familiar with. This empowers [practitioners](#term) to analyze cost by [service](#term), report [service](#term) costs by [sub account](#term), forecast based on historical trends by [service](#term), and verify accuracy of [services](#term) charged across [service providers](#term).

## Directly Dependent Columns

* [ServiceCategory](#col)
* [ServiceName](#col)
* [ServiceSubcategory](#col)

## Supporting Columns

* [ServiceProviderName](#col)

## Example SQL Query

```sql
SELECT
  BillingPeriodStart,
  ServiceProviderName,
  SubAccountId,
  SubAccountName,
  ServiceCategory,
  ServiceSubcategory,
  ServiceName,
  SUM(BilledCost) AS TotalBilledCost,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM CostAndUsage
WHERE ServiceName = ?
  AND BillingPeriodStart >= ? AND BillingPeriodStart < ?
GROUP BY
  BillingPeriodStart,
  ServiceProviderName,
  SubAccountId,
  SubAccountName,
  ServiceCategory,
  ServiceSubcategory,
  ServiceName
ORDER BY TotalBilledCost DESC
```

## Version Introduced

0.5
