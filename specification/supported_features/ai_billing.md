# AI Billing

## Description

FOCUS enables normalization of usage-based billing data from artificial intelligence and machine learning services, including token consumption for frontier model APIs. Token quantities are represented through consumption and pricing columns, allowing consumption and cost to be tracked by [*SKU*](#glossary:sku), token direction, and cache interaction. The TokenDirection and TokenCacheAction properties of [SkuPriceDetails](#datamodel.costandusage.skupricedetails) label the direction of the metered tokens and their interaction with a cache, so those attributes can be compared across service providers independently of provider-specific meter names, with model identity carried in the same SkuPriceDetails object.

## Directly Dependent Columns

* ConsumedQuantity
* ConsumedUnit
* PricingQuantity
* PricingUnit
* SkuId
* SkuMeter
* SkuPriceDetails

## Supporting Columns

* BillingCurrency
* ChargeCategory
* ChargePeriodEnd
* ChargePeriodStart
* EffectiveCost
* InvoiceIssuerName
* ServiceCategory
* ServiceName
* ServiceProviderName
* ServiceSubcategory
* SkuPriceId

## Example SQL Queries

Because ANSI SQL does not define a standard for parsing JSON, the following queries use BigQuery Standard SQL JSON functions (e.g., `JSON_VALUE`) to read the TokenDirection and TokenCacheAction properties from SkuPriceDetails. Similar functions are available in all major SQL engines; the examples can be adapted to accommodate any particular database instance. Non-JSON constructs (`NULLIF`) are ANSI SQL and should work without modification.

### Effective Cost Per Million Tokens

Effective cost per one million tokens, by SKU, token direction, and cache action:

```sql
SELECT
  ServiceProviderName,
  SkuId,
  SkuPriceId,
  SkuMeter,
  JSON_VALUE(SkuPriceDetails, '$.TokenDirection') AS TokenDirection,
  JSON_VALUE(SkuPriceDetails, '$.TokenCacheAction') AS TokenCacheAction,
  BillingCurrency,
  SUM(ConsumedQuantity) AS TotalTokens,
  SUM(EffectiveCost) AS TotalEffectiveCost,
  SUM(EffectiveCost) * 1000000 / NULLIF(SUM(ConsumedQuantity), 0) AS EffectiveCostPerMillionTokens
FROM focus_data_table
WHERE ChargeCategory='Usage'
  AND ServiceCategory='AI and Machine Learning'
  AND ConsumedUnit='Tokens'
  AND ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
GROUP BY
  ServiceProviderName,
  SkuId,
  SkuPriceId,
  SkuMeter,
  JSON_VALUE(SkuPriceDetails, '$.TokenDirection'),
  JSON_VALUE(SkuPriceDetails, '$.TokenCacheAction'),
  BillingCurrency
```

### Token Consumption Volume Over Time

Token consumption volume over time, by service, token direction, and cache action:

```sql
SELECT
  ChargePeriodStart,
  InvoiceIssuerName,
  ServiceProviderName,
  ServiceName,
  SkuMeter,
  JSON_VALUE(SkuPriceDetails, '$.TokenDirection') AS TokenDirection,
  JSON_VALUE(SkuPriceDetails, '$.TokenCacheAction') AS TokenCacheAction,
  SUM(ConsumedQuantity) AS TotalTokens
FROM focus_data_table
WHERE ChargeCategory='Usage'
  AND ServiceCategory='AI and Machine Learning'
  AND ConsumedUnit='Tokens'
  AND ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
GROUP BY
  ChargePeriodStart,
  InvoiceIssuerName,
  ServiceProviderName,
  ServiceName,
  SkuMeter,
  JSON_VALUE(SkuPriceDetails, '$.TokenDirection'),
  JSON_VALUE(SkuPriceDetails, '$.TokenCacheAction')
```

## Version Introduced

1.5
