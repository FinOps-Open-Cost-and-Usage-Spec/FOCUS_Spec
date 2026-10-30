---
dataset: CostAndUsage
---

# Service Categorization

## Description

FOCUS provides a structure for categorizing services based on their core functions. By classifying services into high-level categories and more granular subcategories, practitioners can organize costs according to functional areas. This standardized categorization provides data that practitioners can use in their cost management processes and decision making.

## Directly Dependent Columns

* [ServiceCategory](#col)
* [ServiceName](#col)
* [ServiceSubcategory](#col)

## Supporting Columns

* [BilledCost](#col)
* [BillingCurrency](#col)
* [BillingPeriodEnd](#col)
* [BillingPeriodStart](#col)
* [ServiceProviderName](#col)

## Example SQL Query

```sql
SELECT
  BillingPeriodStart,
  BillingPeriodEnd,
  ServiceProviderName,
  ServiceCategory,
  ServiceSubcategory,
  ServiceName,
  BillingCurrency,
  SUM(BilledCost) AS TotalBilledCost
FROM CostAndUsage
WHERE BillingPeriodStart >= ? and BillingPeriodEnd < ?
GROUP BY
  BillingPeriodStart,
  BillingPeriodEnd,
  ServiceProviderName,
  ServiceCategory,
  ServiceSubcategory,
  ServiceName,
  BillingCurrency
```

## Version Introduced

1.1
