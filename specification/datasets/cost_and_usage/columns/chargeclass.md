# Charge Class

Charge Class indicates whether a [*charge*](#glossary:charge) represents a [*correction*](#glossary:correction) to a previously [*closed billing period*](#glossary:closed-billing-period). Charge Class is commonly used to differentiate such corrections from all other charges, including both regularly incurred *charges* and *corrections* to [*open billing periods*](#glossary:open-billing-period).

## Requirements

ChargeClass MUST adhere to the following requirements:

* ChargeClass MUST be of type String.
* ChargeClass MUST adhere to the following nullability requirements:
  * ChargeClass MUST be null when the *charge* does not represent a correction to a previously *closed billing period*.
  * ChargeClass MUST NOT be null when the *charge* represents a correction to a previously *closed billing period*.
* ChargeClass MUST be "Correction" when ChargeClass is not null.

## Column ID

ChargeClass

## Display Name

Charge Class

## Description

Indicates whether a *charge* represents a correction to a previously *closed billing period*.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | Allowed values                                       |

Allowed values:

| Value      | Description                                                                                    |
| :--------- | :----------------------------------------------------------------------------------------------|
| Correction | Correction to a previously *closed billing period* (e.g., refunds and credit modifications). |

## Version Introduced

1.0
