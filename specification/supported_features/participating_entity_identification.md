---
dataset: CostAndUsage
---

# Participating Entity Identification

## Description

FOCUS allows practitioners to identify the several participating entities involved in resource or service hosting, invoicing, and data generation. The FOCUS Specification includes multiple columns to identify key participating entities, including [Service Provider Name](#col), [Invoice Issuer Name](#col), [Host Provider Name](#col), and Data Generator.

## Directly Dependent Columns

* [ServiceProviderName](#col)
* [InvoiceIssuerName](#col)
* [HostProviderName](#col)

## Applicable Metadata

* [DataGenerator](#meta)

## Example SQL Query

```sql
SELECT
  BillingPeriodStart,
  BillingPeriodEnd,
  ServiceProviderName,
  InvoiceIssuerName,
  HostProviderName,
  ServiceName,
  BillingCurrency,
  SUM(BilledCost) AS TotalBilledCost
FROM CostAndUsage
WHERE BillingPeriodStart >= ? and BillingPeriodEnd < ?
GROUP BY
  BillingPeriodStart,
  BillingPeriodEnd,
  ServiceProviderName,
  InvoiceIssuerName,
  HostProviderName,
  ServiceName,
  BillingCurrency
```

## Version Introduced

1.1

## Version Updated

1.3
