# Charge Class

Charge Class indicates whether the row represents the original [*charge*](#glossary:charge), a correction to one or more previous *charges* that occurred in the same [*billing period*](#glossary:billing-period), or a correction to one or more *charges* that have been invoiced in a previous *billing period*. Charge Class is commonly used to differentiate refunds from regularly incurred charges.

The ChargeClass column MUST be present in the billing data. This column MUST be of type String, MUST NOT be null, and MUST be one of the allowed values.

## Column ID

ChargeClass

## Display Name

Charge Class

## Description

Indicates whether the row represents the original *charge*, a correction to one or more *charges* that occurred in the same *billing period*, or a correction to one or more *charges* that have been invoiced in a previous *billing period*.

## Content Constraints

| Constraint      | Value          |
|:----------------| :--------------|
| Column type     | Dimension      |
| Feature level   | Mandatory      |
| Allows nulls    | False          |
| Data type       | String         |
| Value format    | Allowed values |

Allowed values:

| Value                    | Description |
|:-------------------------|:------------|
| Original                 | Original charges for services used or purchased.                                        |
| Current-cycle Correction | Correction to one or more previous charges that occurred in the same billing period.    |
| Past-cycle Correction    | Correction to one or more charges that have been invoiced in a previous billing period. |

## Introduced (version)

1.0
