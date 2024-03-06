# Adjustment Category

A Adjustment Category indicates whether the row represents reguar costs incurred, a refund for taxable usage or a non-taxable credit.

The AdjustmentCategory column MUST be present and MAY be null. This column is of type String and MUST be one of the allowed values.

## Column ID

AdjustmentCategory

## Display Name

Adjustment Category

## Description

Indicates whether the row represents regular usage charges, service refunds or incentive credits.

## Content Constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column type     | Dimension      |
| Column required | True           |
| Allows nulls    | False          |
| Data type       | String         |
| Value format    | Allowed values |

Allowed values:

| Value      | Description                          |
| :--------- | :------------------------------------|
| NULL       | Default value for all incomming charges.             |
| Refund     | Refunded related to usage or prucahse specific activities (expects a matching 'tax' transaction) |
| Credit     | Promotional / negotiated / incentive credits provided at providers discression (does NOT expect a matching 'tax' transaction)       |


## Introduced (version)

0.5
