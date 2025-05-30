# Verification, Comparison, and Fluctuation Tracking of Unit Prices

## Description

When a provider supports unit pricing concepts, FOCUS allows practitioners to:

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
  SkuId,
  SkuPriceId,
  SkuPriceDetails,
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

## Introduced (Version)

1.0
