# Charge Description

A Charge Description provides a high-level context of a row without requiring additional discovery. This column is a self-contained summary of the charge's purpose and price. It typically covers a select group of corresponding details across a billing dataset or provides information not otherwise available.

The Charge Description column MUST be present within the dataset, MUST be of type String, and SHOULD NOT be null. Providers SHOULD specify the length of this column in their publicly available FOCUS documentation.

## Column ID

ChargeDescription

## Display Name

Charge Description

## Description

Brief, human-readable summary of a row.

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
