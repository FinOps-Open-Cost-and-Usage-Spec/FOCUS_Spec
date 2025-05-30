# Charge Description

A Charge Description provides a high-level context of a [*row*](#glossary:row) without requiring additional discovery. This column is a self-contained summary of the [*charge's*](#glossary:charge) purpose and price. It typically covers a select group of corresponding details across a billing dataset or provides information not otherwise available.

The ChargeDescription column adheres to the following requirements:

* ChargeDescription MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ChargeDescription MUST be of type String.
* ChargeDescription MUST conform to [StringHandling](#stringhandling) requirements.
* ChargeDescription SHOULD NOT be null.
* ChargeDescription maximum length SHOULD be provided in the corresponding FOCUS Metadata Schema.

## Column ID

ChargeDescription

## Display Name

Charge Description

## Description

Self-contained summary of the *charge's* purpose and price.

## Content Constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Mandatory        |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.0-preview
