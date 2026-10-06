# Contract ID

Contract ID is a service-provider-assigned identifier for a [*contract*](#glossary:contract) describing the agreed terms between a service provider and a customer. Contracts can include commitment to a certain amount of spend or usage over an agreed period of time. A null Contract ID indicates a public list price that is not tied to a specific contract; a non-null Contract ID associates the price with a specific contract. The terms of a contract, including its duration, are described in the [Contract Commitment](#datamodel.contractcommitment) dataset, while the SKU Price dataset carries the contracted unit price itself.

> **Note:** [SkuPriceEligibility](#datamodel.skuprice.skupriceeligibility) is the exclusive determinant of which entities are eligible for the SkuPrice record. ContractId serves only to identify the source agreement; it does not implicitly grant pricing eligibility to all accounts governed by that contract.

## Requirements

ContractId MUST adhere to the following requirements:

* ContractId MUST be of type String.
* ContractId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* ContractId MUST adhere to the following nullability requirements:
  * ContractId MUST be null when the SkuPrice record does not represent a price established by a contract.
  * ContractId MUST be null when [*UnitPriceType*](#datamodel.skuprice.unitpricetype) is "List".
  * ContractId MUST NOT be null when the SkuPrice record represents a price established by a contract.
  * ContractId MUST NOT be null when *UnitPriceType* is "Base" or "Contracted".
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

| Constraint                 | Value                                                                                      |
| :------------------------- | :----------------------------------------------------------------------------------------- |
| Dataset                    | [SKU Price](#datamodel.skuprice)                                                           |
| Operating Model Conditions | Not applicable                                                                             |
| Column type                | Dimension                                                                                  |
| Feature level              | Mandatory                                                                                  |
| Allows nulls               | True                                                                                       |
| Data type                  | String                                                                                     |
| Value format               | \<not specified>                                                                           |

## Version Introduced

1.5
