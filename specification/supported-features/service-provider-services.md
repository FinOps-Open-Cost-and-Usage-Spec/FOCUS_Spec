# Service Provider Services

## Description

FOCUS supports [*service providers*](#glossary:service-provider) specifying the [*services*](#glossary:service) and product offerings that they provide their customers that align with the names [*practitioners*](#glossary:practitioner) are familiar with. This empowers *practitioners* to analyze cost by *service*, report *service* costs by [*sub account*](#glossary:sub-account), forecast based on historical trends by *service*, and verify accuracy of *services* charged across *service providers*.

## Directly Dependent Columns

* ServiceCategory
* ServiceName
* ServiceSubcategory

## Supporting Columns

* ServiceProviderName

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
