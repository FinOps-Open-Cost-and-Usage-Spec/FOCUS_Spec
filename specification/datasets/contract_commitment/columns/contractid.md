# Contract ID

[Contract ID](#col) is a service-provider-assigned identifier for a contract describing the agreed terms between a service provider and a customer. Contracts can include commitment to a certain amount of spend or usage over an agreed period of time.

## Requirements

[ContractId](#col) MUST adhere to the following requirements:

* [ContractId](#col) MUST be of type String.
* [ContractId](#col) MUST conform to [StringHandling](#attr) requirements.
* [ContractId](#col) MUST NOT be null.
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

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [Contract Commitment](#ds)                           |
| Operating model conditions | Not applicable                                       |
| Column type                | Dimension                                            |
| Feature level              | Mandatory                                            |
| Allows nulls               | False                                                |
| Data type                  | String                                               |
| Value format               | \<not specified>                                     |

## Version Introduced

1.3
