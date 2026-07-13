# Contract Commitment Duration Type

Contract Commitment Duration Type represents the categorical length of the [*contract commitment*](#glossary:contract-commitment) a recommendation proposes to purchase (e.g., "1 Year", "3 Years", "100 DPUs").

## Requirements

ContractCommitmentDurationType MUST adhere to the following requirements:

* ContractCommitmentDurationType MUST be of type String.
* ContractCommitmentDurationType MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* ContractCommitmentDurationType MUST adhere to the following nullability requirements:
  * ContractCommitmentDurationType MUST NOT be null when a recommendation proposes the purchase of a *contract commitment*.
  * ContractCommitmentDurationType MUST be null when a recommendation does not propose the purchase of a *contract commitment*.
* When not null, ContractCommitmentDurationType SHOULD be expressed with a quantity and usage unit, where quantity is a positive integer and usage unit is a standardized unit of usage, either singular or plural (e.g., "1 DPU", "300 DPUs").

## Expected Format

A given Contract Commitment Duration Type value follows a structured format of "[Numeric Value] [Unit]".

* [Numeric Value]: A positive integer.
* [Unit]: A unit of time or measurement of usage, singular or plural (e.g., Hour, Year, Years, MB, GB).

## Column ID

ContractCommitmentDurationType

## Display Name

Contract Commitment Duration Type

## Description

The categorical duration of the *contract commitment* a recommendation proposes to purchase.

## Content Constraints

| Constraint      | Value                                          |
| :-------------- | :--------------------------------------------- |
| Dataset         | [Recommendation](#datasets.recommendation)     |
| Column type     | Dimension                                      |
| Feature level   | Conditional                                    |
| Allows nulls    | True                                           |
| Data type       | String                                         |
| Value format    | Expected format                                |

## Version Introduced

1.5
