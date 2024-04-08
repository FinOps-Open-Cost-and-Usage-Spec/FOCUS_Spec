# Charge Class

A Charge Class indicates whether the row represents a regular charge or a correction to one or more previous charges. Charge Class is commonly used to differentiate refunds from regularly incurred charges.


The ChargeClass column MUST be present and MUST NOT be null. This column is of type String and MUST be one of the allowed values.

## Column ID

ChargeClass

## Display Name

Charge Class

## Description

Indicates whether the row represents a regular charge or a correction to one or more previous charges, its primary use iis for differentiating refunds from normal usage.

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
| Regular     | Normal charge                        |
| Correction    | Correction to one or more previous charges       |

## Introduced (version)

0.5
