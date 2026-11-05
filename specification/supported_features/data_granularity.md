---
dataset: CostAndUsage
---

# Data Granularity

## Description

FOCUS supports multiple levels of cost and usage data granularity. This includes the ability to report on a daily, hourly, or other time period basis. FOCUS also supports the ability for cost and usage data to be provided for high granularity scenarios, such as down to the individual [resources](#term) and [SKUs](#term). It also supports high level granularity cost and usage data, such as account level, or service level [charges](#term). For the account and service hierarchies themselves, see [Account Structures](#supportedfeatures.accountstructures) and [Service Provider Services](#supportedfeatures.serviceproviderservices).

## Directly Dependent Columns

* [BillingAccountId](#col)
* [ChargePeriodEnd](#col)
* [ChargePeriodStart](#col)
* [ResourceId](#col)
* [ResourceName](#col)
* [ServiceName](#col)
* [SubAccountId](#col)

## Supporting Columns

* [BilledCost](#col)
* [BillingCurrency](#col)
* [ConsumedQuantity](#col)
* [ConsumedUnit](#col)
* [EffectiveCost](#col)
* [ListCost](#col)
* [SkuId](#col)

## Example SQL Query

```sql
SELECT
  ChargePeriodStart,
  ChargePeriodEnd,
  BillingAccountId,
  SubAccountId,
  ServiceName,
  ResourceId,
  ResourceName,
  SkuId,
  ConsumedUnit,
  BillingCurrency,
  SUM(ConsumedQuantity),
  SUM(ListCost),
  SUM(BilledCost),
  SUM(EffectiveCost)
FROM CostAndUsage
GROUP BY
  ChargePeriodStart,
  ChargePeriodEnd,
  BillingAccountId,
  SubAccountId,
  ServiceName,
  ResourceId,
  ResourceName,
  SkuId,
  ConsumedUnit,
  BillingCurrency
```

## Version Introduced

0.5
