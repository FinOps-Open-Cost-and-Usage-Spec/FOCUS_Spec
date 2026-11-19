---
dataset: CostAndUsage
---

# Account Structures

## Description

Different [service providers](#term) have different account constructs that FinOps [practitioners](#term) use for allocation, reporting, and more. Organizations may have one or many accounts within one or more [service providers](#term) and FinOps [practitioners](#term) may need to review the cost broken down by each account. FOCUS has two types of accounts: a [billing account](#term) and a [sub account](#term).

A [billing account](#term) is the account where [invoices](#term) are generated. Each [billing account](#term) can have one or more [sub accounts](#term), which can be used for deploying and managing [resources](#term) and [services](#term). Billing and sub accounts are often used to facilitate allocation strategies and FinOps [practitioners](#term) must be able to break costs down by billing and sub account to facilitate FinOps scenarios like chargeback and budgeting.

## Directly Dependent Columns

* [BillingAccountId](#col)
* [BillingAccountName](#col)
* [BillingAccountType](#col)
* [SubAccountId](#col)
* [SubAccountName](#col)
* [SubAccountType](#col)

## Supporting Columns

* [BilledCost](#col)
* [BillingCurrency](#col)

## Example SQL Query

```sql
SELECT
  BillingAccountId,
  BillingAccountName,
  BillingAccountType,
  SubAccountId,
  SubAccountName,
  SubAccountType,
  BillingCurrency,
  SUM(BilledCost)
FROM CostAndUsage
WHERE BillingPeriodStart >= ? AND BillingPeriodEnd < ?
GROUP BY
  BillingAccountId,
  BillingAccountName,
  BillingAccountType,
  SubAccountId,
  SubAccountName,
  SubAccountType,
  BillingCurrency
```

## Version Introduced

0.5
