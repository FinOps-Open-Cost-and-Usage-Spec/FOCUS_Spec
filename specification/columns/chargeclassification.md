# Charge Classification

A Charge Classification indicates whether the row represents a regular charge or a correction to one or more previous charges.


The ChargeClassification column MUST be present and MUST NOT be null. This column is of type String and MUST be one of the allowed values.

## Column ID

ChargeClassification

## Display Name

Charge Classification

## Description

Indicates whether the row represents regular charges, or is a correction to previoulsly billed line items.

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
| :--------- | :------------------------------------|           |
| Regular     | Regular billing line item  |
| Correction    | Correction to a previously billed line item       |

## Introduced (version)

0.5
