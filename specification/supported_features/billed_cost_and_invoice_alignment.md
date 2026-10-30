# Billed Cost and Invoice Alignment

## Description

FOCUS data should be consistent with the costs indicated on payable [invoices](#term). This is relevant to the total cost of the [invoice](#term), as well as the period of time the [invoice](#term) covers.

## Directly Dependent Columns

* BilledCost
* BillingCurrency
* BillingPeriodEnd
* BillingPeriodStart
* InvoiceId

## Example SQL Query

```sql
SELECT
  BillingPeriodStart,
  BillingPeriodEnd,
  InvoiceId,
  BillingCurrency,
  SUM(BilledCost)
FROM CostAndUsage
GROUP BY
  BillingPeriodStart,
  BillingPeriodEnd,
  InvoiceId,
  BillingCurrency
```

## Version Introduced

0.5
