# Service Categorization

## Introduced Version
1.1

## Description
FOCUS provides a structure for categorizing services based on their core functions. By classifying services into high-level categories and more granular subcategories, practitioners can analyze costs according to functional areas, identify spending patterns, discover optimization opportunities, and support more effective procurement decisions. Service categorization also enables organizations to track migration progress by monitoring how spending shifts across service categories over time as workloads move between environments.

## Directly Dependent Columns
* BilledCost
* BillingCurrency
* BillingPeriodEnd
* BillingPeriodStart
* ProviderName
* ServiceCategory
* ServiceName
* ServiceSubcategory

## Indirectly Dependent Columns


## Example SQL Query
```
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