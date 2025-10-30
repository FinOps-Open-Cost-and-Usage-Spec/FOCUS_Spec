# Participating Entity Identification

## Description

FOCUS allows practitioners to identify the several participating entities involved in resource or service hosting, invoicing, and data generation. The FOCUS Specification includes multiple columns to identify key participating entities, including Service Provider Name, Invoice Issuer Name, Host Provider Name, and Data Generator.

## Directly Dependent Columns

* ServiceProviderName
* InvoiceIssuerName
* HostProviderName

## Applicable Metadata

* DataGenerator

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
FROM focus_data_table
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

## Introduced (Version)

1.1

## Updated (Version)

1.3
