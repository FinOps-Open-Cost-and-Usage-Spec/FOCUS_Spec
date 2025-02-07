# Supported Feature

Cost data in the FOCUS specification is represented such that cost information is consistent with the costs indicated on invoices.


## Introduced Version
0.5

## Description
FOCUS data should be consistent with the costs indicated on invoices. This is relevant to the total cost of the invoice, as well as the period of time the invoice covers.

## Directly Dependent Columns
* BilledCost
* ChargePeriodStart
* ChargePeriodEnd

## Indirectly Dependent Columns



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

## Parameters
* ChargePeriodStart
* ChargePeriodEnd

