# Use Case

Compare billed cost per subaccount to budget

## Use Case ID
14383

## Supported Specification Version
1.0

## Description
Product wants to confirm charges are in line with expectations (budgets) for a business which has all its cost within a single subaccount. The ChargePeriod is used for filtering to capture items that apply to the period only (excludes adjustments from previous periods that were applied in the current BillingPeriod).

## Directly Dependent Columns
* Provider
* Sub Account ID
* Sub Account Name
* Billed Cost
* Charge Category
* Charge Period Start
* Charge Period End

## Indirectly Dependent Columns



## Example SQL Query
```
SELECT
  ProviderName,
  SubAccountId,
  SubAccountName,
  SUM(BilledCost) AS TotalBilledCost
FROM focus_data_table
WHERE ChargeCategory = 'Usage'
  AND ChargePeriodStart >= ? and ChargePeriodEnd <= ?
  AND ProviderName = ?  
  AND SubAccountId = ?  
GROUP BY
  ProviderName,
  SubAccountId,
  SubAccountName
```

## Parameters
* ChargePeriodStart
* ChargePeriodEnd
* ProviderName
* SubAccountId

## Use Case Change Log
| Version | Change | Purpose |
| :-------| :------| :-----------|