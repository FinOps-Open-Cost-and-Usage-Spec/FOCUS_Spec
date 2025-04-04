# Service Categorization

## Introduced Version

1.1

## Description

FOCUS provides a structure for categorizing services based on their core functions. By classifying services into high-level categories and more granular subcategories, practitioners can organize costs according to functional areas. This standardized categorization provides data that practitioners can use in their cost management processes and decision making.

## Directly Dependent Columns

* ServiceCategory
* ServiceName
* ServiceSubcategory

## Supporting Columns

* BilledCost
* BillingCurrency
* BillingPeriodEnd
* BillingPeriodStart
* ProviderName

## Example SQL Query

```sql
SELECT
  BillingPeriodStart,
  BillingPeriodEnd,
  ProviderName,
  ServiceCategory,
  ServiceSubcategory,
  ServiceName,
  BillingCurrency,
  SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE BillingPeriodStart >= ? and BillingPeriodEnd < ?
GROUP BY
  BillingPeriodStart,
  BillingPeriodEnd,
  ProviderName,
  ServiceCategory,
  ServiceSubcategory,
  ServiceName,
  BillingCurrency
```
