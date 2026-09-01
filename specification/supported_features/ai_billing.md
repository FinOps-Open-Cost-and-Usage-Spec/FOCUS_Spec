# AI Billing

## Description

FOCUS enables normalization of usage-based billing data from artificial intelligence and machine learning services, including token consumption for foundation model APIs. Token quantities are represented through consumption and pricing columns, allowing consumption and cost to be tracked by [*SKU*](#glossary:sku) and token type without provider-specific schemas, with model identity available in [SkuPriceDetails](#datamodel.costandusage.skupricedetails).

## Directly Dependent Columns

* ConsumedQuantity
* ConsumedUnit
* PricingQuantity
* PricingUnit
* SkuId
* SkuMeter

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
* SkuPriceDetails
* SkuPriceId

## Example SQL Queries

### Effective Cost Per Million Tokens

Effective cost per one million tokens, by SKU and token type:

```sql
SELECT
  ServiceProviderName,
  SkuId,
  SkuPriceId,
  SkuMeter,
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
  BillingCurrency
```

### Token Consumption Volume Over Time

Token consumption volume over time, by service and token type:

```sql
SELECT
  ChargePeriodStart,
  InvoiceIssuerName,
  ServiceProviderName,
  ServiceName,
  SkuMeter,
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
  SkuMeter
```

## Version Introduced

1.5
