# Adjustment Category

An adjustment is a positive or negative change in cost applied after the original usage or purchase record(s). Adjustments may be related to one or more charges and are identified by the ChargeType column.

Adjustment Category indicates what kind of after-the-fact adjustment the record represents. Adjustment Category is commonly used to identify changes like credits and refunds.

The AdjustmentCategory column MUST be present and MUST NOT be null or empty when ChargeType is "Adjustment". AdjustmentCategory MUST be null when ChargeType is not "Adjustment". This column is of type String and SHOULD be one of the allowed values or a value of choosing from the vendor.

## Column ID

AdjustmentCategory

## Display Name

Adjustment Category

## Description

A positive or negative change in cost applied after the original usage or purchase record(s).

## Content Constraints

| Constraint      | Value                                    |
| :-------------- | :--------------------------------------- |
| Column required | True                                     |
| Data type       | String                                   |
| Allows nulls    | True                                     |
| Value format    | list-of-values                           |

Allowed values:

| Value      | Description                                                                                                                                                                   |
|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Refund | Applied by the vendor where a refund is given to the vendor, refund can be multiple types, the refund type should be noted in the column ChargeType, this could be for example a refund for unused reservations, or unused pre-commit amounts.
|Credits  | Applied when vendor has incorrectly billed usage or applied a credit for usage such as a promo credit, tax error, SLA violation, usage correction or pricing correction.
| Rounding Error | Applied where the usage calculations have exceeded the maximum amount of hours in a month, this would be rounded down to the correct level of usage where a vendor uses rounding methods.
| Balance Transfer | Applied to an account where a customer migrates an account from one account to another where the migrated account had a positive balance | Applied where an account had a positive balance that was not consumed in the previous month.
| General Adjustment | Any adjustment the vendor applies to a customer account that does not have a specific type.
## Introduced (version)

1.0
