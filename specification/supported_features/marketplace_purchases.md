# Marketplace Purchases

## Description

FOCUS supports the analysis of cost and usage data for marketplace purchases and their associated costs. It also supports the reporting of EffectiveCost for usage from the provider.  

## Directly Dependent Columns

* InvoiceIssuerName
* ProviderName

## Supporting Columns

* BilledCost
* EffectiveCost

## Example SQL Query on a CSP Marketplace using the Cost and Usage FOCUS Dataset

```sql
SELECT
  ProviderName,
  InvoiceIssuerName,
  BillingPeriodStart,
  BillingPeriodEnd,
  SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE ProviderName = '<Example SaaS Provider>'
  AND InvoiceIssuerName = '<Example CSP Marketplace>'
GROUP BY
  ProviderName,
  InvoiceIssuerName,
  BillingPeriodStart,
  BillingPeriodEnd
```

## Example SQL Query on a Provider using the Cost and Usage FOCUS Dataset

```sql
SELECT
  ChargePeriodStart,
  ChargePeriodEnd,
  ResourceId,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM focus_data_table
WHERE InvoiceIssuerName = '<Example CSP Marketplace>'
GROUP BY
  ChargePeriodStart,
  ChargePeriodEnd,
  ResourceId
```

## Introduced (Version)

1.0
