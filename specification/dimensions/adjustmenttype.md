# Adjustment Type

An adjustment is a positive or negative change in cost applied after the original usage or purchase record(s). Adjustments may be related to one or more charges and are identified by the ChargeType column.

Adjustment Type indicates what kind of after-the-fact adjustment the record represents. Adjustment Type is commonly used to identify changes like credits and refunds.

The AdjustmentType column MUST be present and MUST NOT be null or empty. This column is of type String and MUST be one of the allowed values.

- Usage Correction
- Price Correction
- GoodWill
- SLA Violation
- Balance Transfer
- General Adjustment
- Promo Credit
- Refund - Reservations
- Refund - Savings Plan
- Refund - General usage
- Tax error
- Rounding Error
- Account Closure

See [Appendix: adjustment type) for details about allowed values and governance criteria for this dimension.

## Column ID

AdjustmentType

## Display Name

Adjustment Type

## Description

Indicates whether the record represents an after-the-fact change to an invoice or cost of usage that already occurred (e.g., refunds, credits).

## Content Constraints

| Constraint      | Value                                    |
| :-------------- | :--------------------------------------- |
| Column required | True                                     |
| Data type       | String                                   |
| Allows nulls    | True                                     |
| Value format    | list-of-values                           |

Allowed values:

| Value      | Description                                                                                                                                                                   |
|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Adjustment | Any adjustments that are applied after the original usage or purchase record. Adjustments may be related to multiple charges.                                                 |


## Introduced (version)

1.0
