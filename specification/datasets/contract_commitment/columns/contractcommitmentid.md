# Contract Commitment ID

Contract Commitment ID is a provider-assigned identifier describing a single contract term agreed between a provider and a customer.  Contracts can include commitments to a certain amount of spend or usage over an agreed period of time.

The ContractCommitmentID column adheres to the following requirements:

* ContractCommitmentID MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ContractCommitmentID MUST be of type String.
* ContractCommitmentID MUST conform to [StringHandling](#stringhandling) requirements.
* ContractCommitmentID nullability is defined as follows:
  * ContractCommitmentID MUST be null when a [*charge*](#glossary:charge) is not related to a *contract commitment*.
  * ContractCommitmentID MUST NOT be null when a *charge* is related to a *contract commitment*.
* When ContractCommitmentID is not null, ContractCommitmentID adheres to the following additional requirements:
  * ContractCommitmentID MUST be a unique identifier within the provider.
  * ContractCommitmentID SHOULD be a fully-qualified identifier.
* ContractCommitmentID MUST have one and only one parent [ContractID](#contractid).
* ContractCommitmentID MAY be equal to ContractID.
* ContractCommitmentID MUST be unique across the Contract Commitment dataset.

## Column ID

ContractCommitmentID

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
