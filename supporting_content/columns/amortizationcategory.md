# Column: Amortization Category

Objective: we need a simple method to calculate savings that doesn't accidentally double-count commitment discount purchase costs.

## Example provider mappings

Current column mappings found in available data sets:

| Provider | Data set                 | Column                    |
|----------|--------------------------|---------------------------|
| AWS      | CUR                      | lineItem/lineItemType     |
| Google Cloud | BigQuery Billing Export | ??N/A because no upfront payments??  |
| Microsoft | Cost details             | ?? Specific SKUs that designate upfront payments |
| OCI | Cost reports             | ??? |

## Example usage scenarios

This example demonstrates a commitment discount that gets 50% off list price when the organization has an 20% discount on all usage.

ChargeDescription | ChargePeriodStart | ListCost | ContractedCost | BilledCost | EffectiveCost
---|---|---:|---:|---:|---:
Reservation | Jan 1 | $365.00 | $365.00 | $365.00 | $0.00
VM usage | Jan 1 | $2.00 | $1.80 | $0.00 | $1.00
VM usage | Jan 2 | $2.00 | $1.80 | $0.00 | $1.00
VM usage | ... | ... | ... | ... | ...
VM usage | Dec 31 | $2.00 | $1.80 | $0.00 | $1.00
Sum of 365 days | Jan 1-Dec 31 | $1,095.00 | $1,022.00 | $365 | $365

The issue is that if you SUM the ListCost or ContractedCost columns, you'll be double counting the original "Reservation" charge and overcounting the savings present in the e.g. EffectiveCost column. We need an attribute that allows us to selectively exclude upfront payments from such calculations, so that we are only SUMming the usage charges that benefit from the original upfront payment (or "unused commitment" line items).

`SUMIF(ListCost, AmortizationCategory != "Principal")` would give you the correct total of $730.00, which is the sum of the usage charges that benefit from the original upfront payment.

## Discussion / Scratch space: