# Billed Cost and Invoice Alignment

## Description

FOCUS data should be consistent with the costs indicated on payable invoices. This is relevant to the total cost of the invoice, as well as the period of time the invoice covers.

## Directly Dependent Columns

* BilledCost
* BillingCurrency
* BillingPeriodEnd
* BillingPeriodStart
* InvoiceId

## Supporting Columns

* ProviderName
* ServiceName

## Example SQL Query

```sql
SELECT
  BillingPeriodStart,
  BillingPeriodEnd,
  InvoiceId,
  SUM(BilledCost)
FROM focus_data_table
Group by
  BillingPeriodStart,
  BillingPeriodEnd,
  InvoiceId
```

## Introduced (Version)

0.5
