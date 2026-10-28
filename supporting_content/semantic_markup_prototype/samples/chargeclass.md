# Charge Class

Charge Class indicates whether a [charge](#term) represents a [correction](#term) to a previously [closed billing period](#term). Charge Class is commonly used to differentiate such [corrections](#term) from all other [charges](#term), including both regularly incurred [charges](#term) and [corrections](#term) to [open billing periods](#term).

## Requirements

ChargeClass MUST adhere to the following requirements:

* ChargeClass MUST be of type String.
* ChargeClass MUST adhere to the following nullability requirements:
  * ChargeClass MUST be null when the [charge](#term) does not represent a [correction](#term) to a previously [closed billing period](#term).
  * ChargeClass MUST NOT be null when the [charge](#term) represents a [correction](#term) to a previously [closed billing period](#term).
* ChargeClass MUST be ["Correction"](#val:ChargeClass) when ChargeClass is not null.

## Allowed Values

| Value      | Description                                                                                    |
| :--------- | :----------------------------------------------------------------------------------------------|
| Correction | [Correction](#term) to a previously [closed billing period](#term) (e.g., refunds and credit modifications). |

## Column ID

ChargeClass

## Display Name

Charge Class

## Description

Indicates whether a [charge](#term) represents a [correction](#term) to a previously [closed billing period](#term).

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating Model Conditions | Not applicable                            |
| Column type                | Dimension                                 |
| Feature level              | Mandatory                                 |
| Allows nulls               | True                                      |
| Data type                  | String                                    |
| Value format               | Allowed values                            |

## Version Introduced

1.0
