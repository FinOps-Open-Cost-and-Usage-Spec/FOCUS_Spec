# Marketplace Purchases

## Description

The FOCUS specification supports cost and usage data for marketplace purchases and their associated costs. It also supports the reporting of EffectiveCost for usage from the provider.  

## Directly Dependent Columns

* InvoiceIssuer
* Provider

## Supporting Columns

* BilledCost
* EffectiveCost

## Example SQL Query on a CSP Marketplace FOCUS Dataset

```sql
SELECT
  Provider,
  InvoiceIssuer,
  BillingPeriodStart,
  BillingPeriodEnd,
  SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE Provider = '<Example SaaS Provider>'
  AND InvoiceIssuer = '<Example CSP Marketplace>'
GROUP BY
  Provider,
  InvoiceIssuer,
  BillingPeriodStart,
  BillingPeriodEnd
``` 

## Example SQL Query on a Provider FOCUS Dataset

```sql
SELECT
  ChargePeriodStart,
  ChargePeriodEnd,
  ResourceId,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE InvoiceIssuer = '<Example CSP Marketplace>'
GROUP BY
  ChargePeriodStart,
  ChargePeriodEnd,
  ResourceId
``` 

## Introduced (Version)

1.0
