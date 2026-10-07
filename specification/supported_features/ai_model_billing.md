# AI Model Billing

## Description

FOCUS enables normalization of usage-based billing data from artificial intelligence and machine learning services, including token consumption for AI model APIs. Token quantities are represented through consumption and pricing columns, allowing consumption and cost to be tracked by [*SKU*](#glossary:sku), token direction, and cache interaction. The TokenDirection and TokenCacheAction properties of [SkuPriceDetails](#datamodel.costandusage.skupricedetails) label the direction of the metered tokens and their interaction with a cache, so those attributes can be compared across service providers independently of provider-specific meter names, with model identity carried in the same SkuPriceDetails object.

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

The following queries use BigQuery Standard SQL JSON functions (e.g., `JSON_VALUE`) to read the ModelDeveloper, ModelId, TokenDirection, and TokenCacheAction properties from SkuPriceDetails. Similar JSON functions are widely available across major SQL engines with variances in syntax, so the examples may need to be adapted for other database engines. Standard SQL functions used here (e.g., `NULLIF`) should work without modification.

### Effective Cost Per Million Tokens

Effective cost per one million tokens, by model, SKU, token direction, and cache action:

```sql
SELECT
  ServiceProviderName,
  JSON_VALUE(SkuPriceDetails, '$.ModelDeveloper') AS ModelDeveloper,
  JSON_VALUE(SkuPriceDetails, '$.ModelId') AS ModelId,
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
  JSON_VALUE(SkuPriceDetails, '$.ModelDeveloper'),
  JSON_VALUE(SkuPriceDetails, '$.ModelId'),
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
  JSON_VALUE(SkuPriceDetails, '$.ModelDeveloper') AS ModelDeveloper,
  JSON_VALUE(SkuPriceDetails, '$.ModelId') AS ModelId,
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
  JSON_VALUE(SkuPriceDetails, '$.ModelDeveloper'),
  JSON_VALUE(SkuPriceDetails, '$.ModelId'),
  JSON_VALUE(SkuPriceDetails, '$.TokenDirection'),
  JSON_VALUE(SkuPriceDetails, '$.TokenCacheAction')
```

## Version Introduced

1.5
