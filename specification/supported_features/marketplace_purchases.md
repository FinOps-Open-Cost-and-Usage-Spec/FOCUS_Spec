---
dataset: CostAndUsage
---

# Marketplace Purchases

## Description

FOCUS supports the analysis of cost and usage data for marketplace purchases and their associated costs. It also supports the reporting of [Effective Cost](#col) for usage from the [service provider](#term).

## Directly Dependent Columns

* [InvoiceIssuerName](#col)
* [ServiceProviderName](#col)

## Supporting Columns

* [BilledCost](#col)
* [EffectiveCost](#col)

## Example SQL Queries

### Report Billed Cost for a Provider on a CSP Marketplace

```sql
SELECT
  ServiceProviderName,
  InvoiceIssuerName,
  BillingPeriodStart,
  BillingPeriodEnd,
  SUM(BilledCost) AS TotalBilledCost
FROM CostAndUsage
WHERE ServiceProviderName = '<Example SaaS Provider>'
  AND InvoiceIssuerName = '<Example CSP Marketplace>'
GROUP BY
  ServiceProviderName,
  InvoiceIssuerName,
  BillingPeriodStart,
  BillingPeriodEnd
```

### Report Effective Cost by Resource for a CSP Marketplace

```sql
SELECT
  ChargePeriodStart,
  ChargePeriodEnd,
  ResourceId,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM CostAndUsage
WHERE InvoiceIssuerName = '<Example CSP Marketplace>'
GROUP BY
  ChargePeriodStart,
  ChargePeriodEnd,
  ResourceId
```

## Version Introduced

1.0
