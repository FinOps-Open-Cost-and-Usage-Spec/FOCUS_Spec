# Data Granularity

## Description

FOCUS supports multiple levels of cost and usage data granularity. This includes the ability to report on a daily, hourly, or other time period basis. FOCUS also supports the ability for cost and usage data to be provided for high granularity scenarios, such as down to the individual resources. It also supports high level granularity cost and usage data, such as account level, or service level charges.

## Directly Dependent Columns

* ResourceId
* ResourceName
* ChargePeriodEnd
* ChargePeriodStart

## Supporting Columns

* BilledCost
* ConsumedQuantity
* ConsumedUnit
* EffectiveCost
* ListCost

## Example SQL Query

```sql
SELECT
  ChargePeriodStart,
  ChargePeriodEnd,
  ResourceId,
  ResourceName,
  ConsumedUnit,
  SUM(ConsumedQuantity),
  SUM(ListCost),
  SUM(BilledCost),
  SUM(EffectiveCost)
FROM focus_data_table
GROUP BY
  ChargePeriodStart,
  ChargePeriodEnd,
  ResourceId,
  ResourceName,
  ConsumedUnit
```

## Version Introduced

0.5
