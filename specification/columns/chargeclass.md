# Charge Class

A Charge Class indicates whether the row represents a correction to one or more [*charges*](#glossary:charge) that have been invoiced in previous billing periods. Charge Class is commonly used to differentiate refunds from regularly incurred charges.

The ChargeClass column MUST be present in the billing data. This column MUST be of type String and MUST be set to "Correction" in case of a correction to one or more charges already invoiced in a previous billing period. Otherwise, it MUST be null.


## Column ID

ChargeClass

## Display Name

Charge Class

## Description

Indicates whether the row represents a correction to one or more *charges* that have been invoiced in previous billing periods.

## Content Constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column type     | Dimension      |
| Feature level   | Mandatory      |
| Allows nulls    | True           |
| Data type       | String         |
| Value format    | Allowed values |

Allowed values:

| Value      | Description                          |
| :--------- | :------------------------------------|
| Correction | Modification to one or more charges invoiced in previous billing periods (e.g., refunds and credit modifications). |

## Introduced (version)

0.5
