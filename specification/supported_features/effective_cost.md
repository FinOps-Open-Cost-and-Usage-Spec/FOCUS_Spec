# Effective Cost

## Description

FOCUS enables practitioners to analyze costs without having to distribute upfront fees and discounts, taking discounts and the amortization of upfront fees paid for services into account. The EffectiveCost column represents cost after negotiated discounts, commitment discounts, and the applicable portion of relevant, prepaid purchases (one-time or recurring) that covered this charge. EffectiveCost is commonly utilized to track and analyze spending trends.

## Directly Dependent Columns

* EffectiveCost

## Supporting Columns

* BillingPeriodEnd
* BillingPeriodStart
* ChargeCategory
* ChargePeriodEnd
* ChargePeriodStart
* ConsumedQuantity
* ConsumedUnit
* PricingQuantity
* ProviderName
* RegionName
* ServiceName

## Example SQL Query

```sql
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

## Introduced (Version)

0.5
