# Cost Comparison

## Introduced Version

0.5

## Description

FOCUS supports the comparison of cost columns in order to identify savings, amortization, or other constructs.

## Directly Dependent Columns

* BilledCost
* ContractedCost
* EffectiveCost
* ListCost

## Supporting Columns

* BillingAccountId
* BillingAccountName
* BillingCurrency
* BillingPeriodEnd
* BillingPeriodStart
* ChargePeriodEnd
* ChargePeriodStart
* ServiceName

## Example SQL Query

```sql
WITH AggregatedData AS (
  SELECT
    ProviderName,
    BillingAccountId,
    BillingAccountName,
    BillingCurrency,
    ServiceName,
    SUM(EffectiveCost) AS TotalEffectiveCost,
    SUM(BilledCost) AS TotalBilledCost,
    SUM(CASE 
          WHEN ChargeCategory = 'Usage' AND BilledCost = 0 AND EffectiveCost != 0
          THEN 0 
          ELSE ContractedCost
        END) AS TotalContractedCost,
    SUM(CASE 
          WHEN ChargeCategory = 'Usage' AND BilledCost = 0 AND EffectiveCost != 0
          THEN 0 
          ELSE ListCost
        END) AS TotalListCost
  FROM focus_data_table
  WHERE BillingPeriodStart >= ? 
    AND BillingPeriodEnd < ?
    AND ChargeClass IS NULL
  GROUP BY
    ProviderName,
    BillingAccountId,
    BillingAccountName,
    BillingCurrency,
    ServiceName
)
SELECT ProviderName,
    BillingAccountId,
    BillingAccountName,
    BillingCurrency,
    ServiceName,
    TotalEffectiveCost,
    TotalBilledCost,
    TotalListCost,
    1 - (TotalContractedCost / NULLIF(TotalListCost, 0)) * 100 AS ContractedDiscount
    1 - (TotalEffectiveCost / NULLIF(TotalListCost, 0)) * 100 AS EffectiveDiscount
FROM AggregatedData
```
