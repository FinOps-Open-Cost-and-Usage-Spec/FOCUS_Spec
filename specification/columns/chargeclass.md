# Charge Class

Charge Class indicates whether the row represents a correction to a previously invoiced [*billing period*](#glossary:billing-period). Charge Class is commonly used to differentiate corrections from regularly incurred charges.

The ChargeClass column adheres to the following requirements:

* ChargeClass MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ChargeClass MUST be of type String.
* ChargeClass nullability is defined as follows:
  * ChargeClass MUST be null when the row does not represent a correction or when it represents a correction within the current *billing period*.
  * ChargeClass MUST NOT be null when the row represents a correction to a previously invoiced *billing period*.
* When ChargeClass is not null, ChargeClass adheres to the following additional requirements:
  * ChargeClass MUST be one of the allowed values.
  * ChargeClass MUST be "Correction".

## Column ID

ChargeClass

## Display Name

Charge Class

## Description

Indicates whether the row represents a correction to a previously invoiced *billing period*.

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
| Correction | Correction to a previously invoiced *billing period* (e.g., refunds and credit modifications). |

## Introduced (version)

1.0
