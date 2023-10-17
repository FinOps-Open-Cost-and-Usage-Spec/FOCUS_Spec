# Adjustment Type

Adjustment Type indicates the record represents a change to your monthly invoice through after-the-fact adustements (e.g. refunds, pricing changes). An adjustment can be positive or negative.
Adjustment Type can be used by practitioners to assess any impacts to spend from positive or negative adjustments.

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

Adjustments

## Description

Indicates whether the record represents an after-the-fact change to an invoice or cost of usage that already occurred (e.g., refunds, credits).

## Content Constraints

| Constraint      | Value                                    |
| :-------------- | :--------------------------------------- |
| Column required | True                                     |
| Data type       | String                                   |
| Allows nulls    | False                                    |
| Value format    | list-of-values                           |

Allowed values:

| Value      | Description                                                                                                                                                                   |
|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Adjustment | Any adjustments that are applied after the original usage or purchase record. Adjustments may be related to multiple charges.                                                 |


## Introduced (version)

1.0
