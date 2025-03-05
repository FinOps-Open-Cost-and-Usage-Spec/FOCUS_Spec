# Data Granularity

## Introduced Version
0.5

## Description
FOCUS support multiple levels of cost and usage data granularity. This includes the ability to report on a daily, hourly, or other time period basis. Focus also supports the ability for cost and usage data to be provided for both resource level cost and usage as well as line items that are not attributed to a specific resource. 

## Directly Dependent Columns
* ResourceId
* ChargePeriodStart
* ChargePeriodEnd

## Indirectly Dependent Columns



## Example SQL Query
```
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
