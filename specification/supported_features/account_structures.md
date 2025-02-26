# Account Structures

## Introduced Version
0.5

## Description

Providers have various account structures and sub structure that FinOps practitioners need to be able to use and report on. An organization may have one or many accounts with a Provider. A FinOps Practitioner may want to extrapolate data associated a specific account or accounts. A billing account is typically the account that handles organizational constructs and invoice reconciliation. Organizations can then break individual organizational units into sub-accounts, facilitating access management needs and cost allocation strategies. A FinOps practitioner must be able to distinguish which account is responsible for a charge as well as which account is responsible for the invoice for said charge.

## Directly Dependent Columns
* BillingAccountId
* BillingAccountName
* SubAccountId
* SubAccountName

## Indirectly Dependent Columns


## Example SQL Query
```
SELECT
  SubAccountID,
  SubAccountName,
  ChargePeriodStart,
  ServiceName,
  SUM(BilledCost)
FROM focus_data_table
WHERE BillingPeriodStart >= ? AND BillingPeriodEnd < ?
    AND SubAccountId = ?
Group by
  ServiceName,
  SubAccountId,
  SubAccountName,
  ChargePeriodStart
```

## Parameters
* BillingPeriodStart
* BillingPeriodEnd
* SubAccountId

