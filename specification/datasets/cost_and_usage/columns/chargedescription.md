# Charge Description

A [Charge Description](#col) provides a high-level context of a [row](#term) without requiring additional discovery. This column is a self-contained summary of the [charge's](#term:charge) purpose and price. It typically covers a select group of corresponding details across a billing dataset or provides information not otherwise available.

## Requirements

[ChargeDescription](#col) MUST adhere to the following requirements:

* [ChargeDescription](#col) MUST be of type String.
* [ChargeDescription](#col) MUST conform to [StringHandling](#attr) requirements.
* [ChargeDescription](#col) SHOULD NOT be null.
* [ChargeDescription](#col) maximum length SHOULD be provided in the corresponding FOCUS Metadata Schema.

## Column ID

ChargeDescription

## Display Name

Charge Description

## Description

Self-contained summary of the *charge's* purpose and price.

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | Not applicable                            |
| Column type                | Dimension                                 |
| Feature level              | Mandatory                                 |
| Allows nulls               | True                                      |
| Data type                  | String                                    |
| Value format               | \<not specified>                          |

## Version Introduced

1.0-preview
