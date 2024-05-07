# Column: Consumed Quantity

## Example provider mappings

Current column mappings found in available data sets:

| Provider | Data set                | Column               |
|----------|-------------------------|----------------------|
| AWS      | CUR                     | lineItem/UsageAmount |
| Azure    | Cost Details            | quantity             |
| GCP      | BigQuery Billing Export | usage.amount               |

## Discussion Topics

* May 6th, 2024: After much discussion, it was agreed upon by the maintainers to rename this column to 'ConsumedQuantity' and the related unit to 'ConsumedUnit' to reduce confusion between what AWS calls lineitem/UsageAmmount. The modification done to the previous UsageUnit content: Specify that this column applies only to 'Usage' rows - as it was previously written as 'usage or purchase'. That now becomes consistent with the subsequent sentence of the introductory paragraph which describes the column as measuring consumption.
* The need for either a 'factor' to remove block pricing OR a column to represent the quantity you were charged for (for usage or purchase) in 'distinct' units was discussed and determined to be something that needs to be thought through and evaluated in detail post v1.0.