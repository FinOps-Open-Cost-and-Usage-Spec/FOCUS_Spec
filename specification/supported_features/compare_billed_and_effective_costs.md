# Supported Feature

Compare billed cost to the effective cost, to understand the actual savings rate. Used to compare with negotiated discounts

## Supported Specification Version
1.0

## Description
FinOps Practitioners must be able to verify that proper discounting is applied for negotiated discounts, live discounts, commitment based discounts, or other discount mechanisms. A FinOps Practitioner can calculate the costs of services over a billing period and compare it to the invoice. Refunds for charges incurred in a previous billing period are excluded to avoid these items impacting the calculation. This query assists the practitioner in the process of verifying by providing the List, Billed, and Effective costs of each providers services and calculates the percentage discount for each.
"

## Directly Dependent Columns
* Provider 
* Billing Account ID
* Billing Account Name
* Billing Currency
* Service Name
* Effective Cost
* List Cost
* Billed Cost
* Billing Period Start
* Billing Period End
* Charge Class

## Indirectly Dependent Columns



## Example SQL Query
```
SELECT
  ProviderName,
  BillingAccountId,
  BillingAccountName,
  BillingCurrency,
  ServiceName,
  SUM(EffectiveCost) AS TotalEffectiveCost,
  SUM(ListCost) AS TotalListCost,
  SUM(BilledCost) AS TotalBilledCost,
  (SUM(EffectiveCost)/SUM(BilledCost))*100 AS EffectiveDiscount
FROM focus_data_table
WHERE BillingPeriodStart >= ? AND BillingPeriodEnd < ?
  AND ChargeClass != 'Correction'
GROUP BY
  ProviderName,
  BillingAccountId,
  BillingAccountName,
  BillingCurrency,
  ServiceName
```

## Parameters
* BillingPeriodStart
* BillingPeriodEnd