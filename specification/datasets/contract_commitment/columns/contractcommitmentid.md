# Contract Commitment ID

Contract Commitment ID is a provider-assigned identifier describing a single contract term agreed between a provider and a customer.  Contracts can include commitments to a certain amount of spend or usage over an agreed period of time.

## Requirements

ContractCommitmentId adheres to the following requirements:

* ContractCommitmentId MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ContractCommitmentId MUST be of type String.
* ContractCommitmentId MUST conform to [StringHandling](#stringhandling) requirements.
* ContractCommitmentId MUST NOT be null.
* When ContractCommitmentId is not null, ContractCommitmentId adheres to the following additional requirements:
  * ContractCommitmentId MUST be a unique identifier within the provider.
  * ContractCommitmentId SHOULD be a fully-qualified identifier.
* ContractCommitmentId MUST have one and only one parent [ContractId](#contractid).
* ContractCommitmentId MAY be equal to ContractId.
* ContractCommitmentId MUST be unique across the Contract Commitment dataset.

## Column ID

ContractCommitmentId

## Display Name

Contract Commitment ID

## Description

A provider-assigned identifier describing a single contract term agreed between a provider and a customer.

## Content Constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Mandatory        |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.3
