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
* ChargePeriodEnd
* ChargePeriodStart
* ServiceProviderName
* ServiceName

## Example SQL Query

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

## Introduced (Version)

1.0
