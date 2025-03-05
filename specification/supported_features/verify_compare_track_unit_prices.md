# Verification, Comparison, and Fluctuation Tracking of Unit Prices

## Introduced Version

1.0

## Description

When provider supports unit pricing concepts, FOCUS dataset contains SKU Price ID, which represents provider-specified reference for specific SKU price in both public and contracted price lists, allowing practitioners to access detailed information about SKU Price, including associated ListUnitPrices and ContractedUnitPrices used to calculate charges. For a given SkuPriceId, FinOps practitioners must be able to:

* Verify that the correct ListUnitPrices and ContractedUnitPrices are applied.
* Compare applied ContractedUnitPrices across different billing accounts and with applied ListUnitPrices at specific points in time.
* Track fluctuations in unit prices over time.

## Directly Dependent Columns

* SkuPriceId
* BillingPeriodId
* ChargePeriodStart
* ChargePeriodEnd
* BillingCurrency
* ListUnitPrice
* ContractedUnitPrice

## Indirectly Dependent Columns

* SkuId
* SkuPriceDetails

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
