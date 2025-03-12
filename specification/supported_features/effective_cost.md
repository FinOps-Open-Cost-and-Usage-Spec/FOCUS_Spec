# Effective Cost

## Introduced Version
0.5

## Description
The FOCUS spec supports representing costs taking into account discounts and the amortization of upfront fees paid for services. This feature represents cost after negotiated discounts, commitment discounts, and the applicable portion of relevant, prepaid purchases (one-time or recurring) that covered this charge. The amortized portion included is proportional to the Pricing Quantity and the time granularity of the data. Effective Cost is commonly utilized to track and analyze spending trends and is complex and crucial such that it needs its own supported feature. 

## Directly Dependent Columns
* PricingQuantity
* BilledCost

## Supporting Columns
* ChargeCategory
* ChargePeriodEnd
* ChargePeriodStart
* RegionName
* BillingPeriodStart
* BillingPeriodEnd
* ProviderName
* ServiceName

## Example SQL Query
```
SELECT
  ProviderName,
  BillingPeriodStart,
  BillingPeriodEnd,
  ServiceCategory,
  ServiceName,
  RegionId,
  RegionName,
  PricingUnit,
  SUM(EffectiveCost) AS TotalEffectiveCost,
  SUM(PricingQuantity) AS TotalPricingQuantity
FROM focus_data_table
WHERE BillingPeriodStart >= ? AND BillingPeriodEnd <= ?
GROUP BY
  ProviderName,
  BillingPeriodStart,
  BillingPeriodEnd,
  ServiceCategory,
  ServiceName,
  RegionId,
  RegionName,
  PricingUnit
``` 