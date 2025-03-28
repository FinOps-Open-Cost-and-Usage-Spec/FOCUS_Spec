# Resource Usage

## Introduced Version

1.0

## Description

FOCUS enables tracking of resource consumption by providing information about which resources were used, in what quantities, and with what units of measure.

## Directly Dependent Columns

* ConsumedQuantity
* ConsumedUnit
* ResourceId
* SkuId

## Supporting Columns

* ChargeCategory
* ChargePeriodEnd
* ChargePeriodStart
* ProviderName
* ServiceName

## Example SQL Query

```sql
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
