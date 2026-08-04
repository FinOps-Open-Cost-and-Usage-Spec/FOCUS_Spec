# Contract ID

Contract ID is a service-provider-assigned identifier for a [*contract*](#glossary:contract) describing the agreed terms between a service provider and a customer. Contracts can include commitment to a certain amount of spend or usage over an agreed period of time. A null Contract ID indicates a public list price that is not tied to a specific contract; a non-null Contract ID associates the price with a specific contract. The terms of a contract, including its duration, are described in the [Contract Commitment](#datamodel.contractcommitment) dataset, while the SKU Price dataset carries the contracted unit price itself.

## Requirements

ContractId MUST adhere to the following requirements:

* ContractId MUST be of type String.
* ContractId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* When ContractId is not null, ContractId MUST adhere to the following requirements:
  * ContractId MUST be a unique identifier within the service provider.
  * ContractId SHOULD be a fully-qualified identifier.

## Column ID

ContractId

## Display Name

Contract ID

## Description

A service-provider-assigned identifier for a contract describing the agreed terms between a service provider and a customer.

## Content Constraints

| Constraint      | Value                                                                                      |
|:----------------|:-------------------------------------------------------------------------------------------|
| Dataset         | [SKU Price](#datamodel.skuprice)                                                            |
| Column type     | Dimension                                                                                  |
| Feature level   | Conditional                                                                                |
| Condition       | [Includes contract commitments](#conditions.includescontractcommitments)                   |
| Allows nulls    | True                                                                                       |
| Data type       | String                                                                                     |
| Value format    | \<not specified>                                                                           |

## Version Introduced

1.5
