# Data Granularity

## Description

FOCUS supports multiple levels of cost and usage data granularity. This includes the ability to report on a daily, hourly, or other time period basis. FOCUS also supports the ability for cost and usage data to be provided for high granularity scenarios, such as down to the individual [*resources*](#glossary:resource) and [*SKUs*](#glossary:sku). It also supports high level granularity cost and usage data, such as account level, or service level [*charges*](#glossary:charge). For the account and service hierarchies themselves, see [Account Structures](#supportedfeatures.accountstructures) and [Service Provider Services](#supportedfeatures.serviceproviderservices).

## Directly Dependent Columns

* BillingAccountId
* ChargePeriodEnd
* ChargePeriodStart
* ResourceId
* ResourceName
* ServiceName
* SubAccountId

## Supporting Columns

* BilledCost
* BillingCurrency
* ConsumedQuantity
* ConsumedUnit
* EffectiveCost
* ListCost
* SkuId

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
