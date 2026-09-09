# Resource Usage

## Description

FOCUS enables tracking of resource consumption by providing information about which resources were used, in what quantities, and with what units of measure.

## Directly Dependent Columns

* ConsumedQuantity
* ConsumedUnit
* ResourceId
* SkuId

## Supporting Columns

* ChargeCategory
* ChargeClass
* ChargePeriodEnd
* ChargePeriodStart
* ServiceProviderName
* ServiceName
* SkuPriceDetails
* SubAccountId
* Tags

## Example SQL Queries

The cache hit rate and input-to-output ratio queries read FOCUS-defined [SkuPriceDetails](#datamodel.costandusage.skupricedetails) properties. Because ANSI SQL does not define a standard for parsing JSON, they use the BigQuery Standard SQL `JSON_VALUE` function; similar functions are available in all major SQL engines, and the examples can be adapted to any particular database instance.

### Resource Consumption by Resource and SKU

```sql
SELECT
  ServiceProviderName,
  ServiceName,
  ResourceId,
  SkuId,
  ConsumedUnit,
  SUM(ConsumedQuantity) AS TotalQuantity
FROM focus_data_table
WHERE ChargeCategory='Usage'
  AND ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
GROUP BY
  ServiceProviderName,
  ServiceName,
  ResourceId,
  SkuId,
  ConsumedUnit
```

### Cache Hit Rate for Token-Metered SKUs

Computes the share of input tokens served from a prompt cache, per workload, using the TokenDirection and CacheAction properties. The denominator is every input token row, so it holds whether or not a service provider meters cache writes as their own charge. Where a service provider emits cache read rows but no uncached input row, the denominator loses that bucket and the ratio overstates the hit rate.

```sql
SELECT
  ServiceProviderName,
  SubAccountId,
  Tags,
  COALESCE(SUM(CASE WHEN JSON_VALUE(SkuPriceDetails, '$.CacheAction') = 'Read'
                    THEN ConsumedQuantity END), 0)
    / NULLIF(SUM(ConsumedQuantity), 0) AS CacheHitRate
FROM focus_data_table
WHERE ChargeCategory = 'Usage'
  AND ChargeClass IS NULL
  AND ConsumedUnit = 'Tokens'
  AND JSON_VALUE(SkuPriceDetails, '$.TokenDirection') = 'Input'
  AND ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
GROUP BY
  ServiceProviderName,
  SubAccountId,
  Tags
```

### Input-to-Output Token Ratio by Model

Compares the tokens consumed from requests with the tokens generated in responses for each model, using the TokenDirection and ModelId properties.

```sql
SELECT
  ServiceProviderName,
  JSON_VALUE(SkuPriceDetails, '$.ModelId') AS ModelId,
  SUM(CASE WHEN JSON_VALUE(SkuPriceDetails, '$.TokenDirection') = 'Input'
           THEN ConsumedQuantity END) AS InputTokens,
  SUM(CASE WHEN JSON_VALUE(SkuPriceDetails, '$.TokenDirection') = 'Output'
           THEN ConsumedQuantity END) AS OutputTokens,
  SUM(CASE WHEN JSON_VALUE(SkuPriceDetails, '$.TokenDirection') = 'Input'
           THEN ConsumedQuantity END)
    / NULLIF(SUM(CASE WHEN JSON_VALUE(SkuPriceDetails, '$.TokenDirection') = 'Output'
                      THEN ConsumedQuantity END), 0) AS InputToOutputRatio
FROM focus_data_table
WHERE ChargeCategory = 'Usage'
  AND ChargeClass IS NULL
  AND ConsumedUnit = 'Tokens'
  AND ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
GROUP BY
  ServiceProviderName,
  ModelId
```

## Version Introduced

1.0

## Version Updated

1.5
