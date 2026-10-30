# Contract ID

[Contract ID](#col) is a service-provider-assigned identifier for a [contract](#term) describing the agreed terms between a service provider and a customer. Contracts can include commitment to a certain amount of spend or usage over an agreed period of time. A null [Contract ID](#col) indicates a public list price that is not tied to a specific contract; a non-null [Contract ID](#col) associates the price with a specific contract. The terms of a contract, including its duration, are described in the [Contract Commitment](#ds) dataset, while the SKU Price dataset carries the unit price specific to that contract.

> **Note:** [SkuPriceEligibility](#col) is the exclusive determinant of which entities are eligible for the SkuPrice record. [ContractId](#col) serves only to identify the source agreement; it does not implicitly grant pricing eligibility to all accounts governed by that contract.

## Requirements

[ContractId](#col) MUST adhere to the following requirements:

* [ContractId](#col) MUST be of type String.
* [ContractId](#col) MUST conform to [StringHandling](#attr) requirements.
* [ContractId](#col) MUST adhere to the following nullability requirements:
  * [ContractId](#col) MUST be null when the SkuPrice record does not represent a price specific to a contract.
  * [ContractId](#col) MUST be null when [UnitPriceType](#col) is "List".
  * [ContractId](#col) MUST NOT be null when the SkuPrice record represents a price specific to a contract.
  * [ContractId](#col) MUST NOT be null when [UnitPriceType](#col) is "Base" or "Contracted".
* When [ContractId](#col) is not null, [ContractId](#col) MUST adhere to the following requirements:
  * [ContractId](#col) MUST be a unique identifier within the service provider.
  * [ContractId](#col) SHOULD be a fully-qualified identifier.

## Column ID

ContractId

## Display Name

Contract ID

## Description

A service-provider-assigned identifier for a contract describing the agreed terms between a service provider and a customer.

## Content Constraints

| Constraint                 | Value                                                                                      |
| :------------------------- | :----------------------------------------------------------------------------------------- |
| Dataset                    | [SKU Price](#ds)                                                                           |
| Operating Model Conditions | Not applicable                                                                             |
| Column type                | Dimension                                                                                  |
| Feature level              | Mandatory                                                                                  |
| Allows nulls               | True                                                                                       |
| Data type                  | String                                                                                     |
| Value format               | \<not specified>                                                                           |

## Version Introduced

Preview: 1.5
