# Charge Class

Charge Class indicates whether the row represents a correction to a previously invoiced [*billing period*](#glossary:billing-period). Charge Class is commonly used to differentiate corrections from regularly incurred charges.

The ChargeClass column adheres to the following requirements:

* The ChargeClass column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* This column MUST be of type String and MUST be "Correction" when the row represents a correction to a previously invoiced *billing period*.
* ChargeClass MUST be null when it is not a correction or when it is a correction within the current *billing period*.

## Column ID

ChargeClass

## Display Name

Charge Class

## Description

Indicates whether the row represents a correction to a previously invoiced *billing period*.
OCI INDICATED: this restriction may need to be removed as corrections can happen in month... need to be aware of this to avoid historic reprocessing

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

OPTIONS:

| Value      | Description                          |
| :--------- | :------------------------------------|
| General Correction | Correction to a previously invoiced *billing period* (e.g., refunds and credit modifications). |
| Price Correction | Correction to a previously invoiced *billing period* (e.g., refunds and credit modifications). |
| Usage Correction | Correction to a previously invoiced *billing period* (e.g., refunds and credit modifications). |

## Introduced (version)

1.0
