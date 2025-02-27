# Resource Usage

## Introduced Version
1.0

## Description
FOCUS standardizes tracking of cloud resource consumption through billing data. By recording what resources were used, in what quantities, and with what units of measure, practitioners can detect anomalies in usage patterns and optimize workloads.

## Directly Dependent Columns
* ChargeCategory
* ChargePeriodEnd
* ChargePeriodStart
* ConsumedQuantity
* ConsumedUnit
* ProviderName
* ResourceId
* ServiceName
* SkuId

## Indirectly Dependent Columns


## Example SQL Query
```
SELECT
  ProviderName,
  ServiceName,
  ResourceId,
  SkuId,
  ConsumedUnit,
  SUM(ConsumedQuantity) AS TotalQuantity
FROM focus_data_table
WHERE ChargeCategory='Usage'
  AND ChargePeriodStart >= ? AND ChargePeriodEnd <= ?
GROUP BY
  ProviderName,
  ServiceName,
  ResourceId,
  SkuId,
  ConsumedUnit
``` 