# Adjustment Type

An adjustment is a positive or negative change in cost applied after the original usage or purchase record(s). Adjustments may be related to one or more charges and are identified by the ChargeType column.

Adjustment Type indicates what kind of after-the-fact adjustment the record represents. Adjustment Type is commonly used to identify changes like credits and refunds.

The AdjustmentType column MUST be present and MUST NOT be null or empty when ChargeType is "Adjustment". AdjustmentType MUST be null when ChargeType is not "Adjustment". This column is of type String and SHOULD be one of the example Allowed values or a value of choosing from the vendor.

## Column ID

AdjustmentType

## Display Name

Adjustment Type

## Description

Indicates the record represents an after-the-fact change to an invoice or cost of usage that already occurred (e.g., refunds, credits).

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
| Adjustment | Any adjustments that are applied after the original usage or purchase record. Adjustments may be related to multiple charges.  Adjustment types can be any of the example values or a value the vendor chooses, but MUST be added if ChargeType is of type Adjustment.


Allowed Value Type Definition:
| Value | Description |
|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Refund | Applied by the vendor where a refund is given to the vendor, refund can be multiple types, the refund type should be noted in the column ChargeType, this could be for example a refund for unused reservations, or unused pre-commit amounts.
| Usage Correction | Applied when vendor has incorrectly billed usage - example, a virtual machine ran for 700 hours but was billed for 730 hours, the adjustment would show usage correction, with comments or notes stating a correction was made in billing for usage of virtual machines due to billing calculation errors.
| Price Correction | Applied as an adjustment where a vendor has incorrectly applied the price to a service, this could be a negative or positive value.
| SLA Violation | Applied after customers request refunds for SLA violations. SLA Violations are where a consumed service did not meet the vendor specified SLO.
| Promo Credit | Similar to General adjustment
| GoodWill | Similar to General adjustment
| Tax error | Applied where a vendor has applied the wrong tax calculations
| Balance Transfer | Applied to an account where a customer migrates an account from one account to another where the migrated account had a positive balance | Applied where an account had a positive balance that was not consumed in the previous month
| Rounding Error | Applied where the usage calculations have exceeded the maximum amount of hours in a month, this would be rounded down to the correct level of usage where a vendor uses rounding methods.
| Account Closure | Applied as a refund of unused balances in a vendor account when a customer closes an account and exits the service.
| General Adjustment | Any adjustment the vendor applies to a customer account that does not have a specific type
## Introduced (version)

1.0
