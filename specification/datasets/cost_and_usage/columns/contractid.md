# Contract ID

Contract ID is a provider-assigned identifier for a contract describing the agreed terms between a provider and a customer.  Contracts can include commitment to a certain amount of spend or usage over an agreed period of time.

The ContractId column adheres to the following requirements:

* ContractId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *negotiated discounts*.
* ContractId MUST be of type String.
* ContractId MUST conform to [StringHandling](#stringhandling) requirements.
* ContractId nullability is defined as follows:
  * ContractId MUST be null when a [*charge*](#glossary:charge) is not related to a *negotiated discount*.
  * ContractId MUST NOT be null when a *charge* is related to a *negotiated discount*.
* When ContractId is not null, ContractId adheres to the following additional requirements:
  * ContractId MUST be a unique identifier within the provider.
  * ContractId SHOULD be a fully-qualified identifier.

## Column ID

ContractId

## Display Name

Contract ID

## Description

A provider-assigned identifier for a contract describing the agreed terms between a provider and a customer.

## Content constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.3
