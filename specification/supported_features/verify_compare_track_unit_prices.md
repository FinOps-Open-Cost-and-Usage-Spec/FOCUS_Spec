# Verification, Comparison, and Fluctuation Tracking of Unit Prices

## Introduced Version

1.0

## Description

When provider supports unit pricing concepts, The FOCUS Specification allows practioners to:

* Verify that the correct List Unit Prices and Contracted Unit Prices are applied.
* Compare applied Contracted Unit Prices across different billing accounts and with applied List Unit Prices at specific points in time.
* Track fluctuations in unit prices over time.

## Directly Dependent Columns

* ContractedUnitPrice
* ListUnitPrice
* SkuId
* SkuPriceDetails
* SkuPriceId

## Supporting Columns

* BillingCurrency
* BillingPeriodId
* ChargePeriodEnd
* ChargePeriodStart

## Example SQL Query

```sql
SELECT DISTINCT
  SkuPriceId,
  BillingPeriodId,
  ChargePeriodStart,
  ChargePeriodEnd,
  BillingCurrency,
  ListUnitPrice,
  ContractedUnitPrice
FROM focus_data_table
WHERE
  SkuPriceId = ?
  AND ChargePeriodStart >= ?
  AND ChargePeriodEnd < ?
```
