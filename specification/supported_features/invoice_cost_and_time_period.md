# Billed Cost and Invoice Alignment

## Introduced Version
0.5

## Description
FOCUS data should be consistent with the costs indicated on payable invoices. This is relevant to the total cost of the invoice, as well as the period of time the invoice covers.

## Directly Dependent Columns
* BilledCost
* ChargePeriodEnd
* ChargePeriodStart

## Supporting Columns
* ProviderName
* ServiceName

## Example SQL Query
```
SELECT
  ChargePeriodStart,
  ChargePeriodEnd,
  SUM(BilledCost)
FROM focus_data_table
Group by
  ChargePeriodStart,
  ChargePeriodEnd
```
