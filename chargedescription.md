# Charge Description

A Charge Description provides a high-level context of a [*row*](#glossary:row) without requiring additional discovery. This column is a self-contained, summary explanation of what the [*charge*](#glossary:charge) is for and how it was priced. It typically covers a select group of corresponding details across a cost and usage dataset or provides information not otherwise available.

The Charge Description column MUST be present within the dataset, MUST be of type String, and SHOULD NOT be null. [Providers](#glossary:provider) SHOULD specify the length of this column in their publicly available [FOCUS](#glossary:finops-cost-and-usage-specification) documentation.

## Column ID

ChargeDescription

## Display Name

Charge Description

## Description

Brief, human-readable summary of a *row*.

## Content Constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column required | True             |
| Data type       | String           |
| Allows nulls    | True             |
| Value format    | \<not specified> |

## Introduced (version)

1.0
