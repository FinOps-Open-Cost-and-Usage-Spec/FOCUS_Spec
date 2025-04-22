# Data Granularity

## Description

The FOCUS schema supports multiple levels of cost and usage data granularity. This includes the ability to report on a daily, hourly, or other time period basis. Focus also supports the ability for cost and usage data to be provided for high granularity scenarios, such as down to the individual resources. It also supports high level granularity cost and usage data, such as account level, or service level charges.

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
* PricingCurrency
* PricingUnit

## Example SQL Query

```sql
SELECT
  ChargePeriodStart,
  ChargePeriodEnd,
  ResourceId,
  SUM(EffectiveCost)
FROM focus_data_table
Group by
  ChargePeriodStart,
  ChargePeriodEnd,
  ResourceId
```

## Introduced (Version)

0.5
