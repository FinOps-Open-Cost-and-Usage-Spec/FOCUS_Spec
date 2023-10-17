# Charge Description

A Charge Description provides a high-level context of a line item without requiring additional discovery.  This column is typically a brief, human-readable summary of a select group of corresponding details or provides information not otherwise available.  

The Charge Description column MUST be present within billing data, MUST be of type String, and SHOULD not be null.

## Column ID

ChargeDescription

## Display Name

Charge Description

## Description

A brief, human-readable summary of a line item.

## Content Constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column required | True             |
| Data type       | String           |
| Allows nulls    | True             |
| Value format    | \<not specified> |

## Introduced (version)

1.0
