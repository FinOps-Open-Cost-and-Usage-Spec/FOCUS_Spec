# Charge Class

A Charge Class indicates whether the row represents a regular charge unit based usage charge, a derivative percentage charged based on usage of one or more otehr services or a correction to one or more previous charges. Charge Class is commonly used to differentiate refunds from regularly incurred charges.

The ChargeClass column MUST be present and MUST NOT be null. This column is of type String and MUST be one of the allowed values.

## Column ID

ChargeClass

## Display Name

Charge Class

## Description

A Charge Class indicates whether the row represents a regular charge unit based usage charge, a derivative percentage charged based on usage of one or more otehr services or a correction to one or more previous charges. Charge Class is commonly used to differentiate refunds from regularly incurred charges.

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
| Standard    | Standard charges for services used or purchased. |
| Correction  | Modification to one or more previous charges, like refunds and credit modifications. |
| Percentage  | Denotes a charge that is billed NOT based on direct unit consumption but is based on a % cost of another service e.g. Support Costs |

## Introduced (version)

0.5
