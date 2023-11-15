# Charge Description

A Charge Description provides a high-level context of a [*row*](#glossary:row) without requiring additional discovery. This column is a self-contained, summary explanation of what the charge is for and how it was priced. It typically covers a select group of corresponding details across a billing dataset or provides information not otherwise available.

The Charge Description column MUST be present within the dataset, MUST be of type String, and SHOULD NOT be null. Providers SHOULD specify the length of this column in their publicly available documentation.

## Column ID

ChargeDescription

## Display Name

Charge Description

## Description

a self-contained, summary explanation of what the charge is for and how it was priced.

## Content Constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Column required | True             |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.0
