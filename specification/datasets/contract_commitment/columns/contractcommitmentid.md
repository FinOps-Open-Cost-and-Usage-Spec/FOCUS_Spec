# Contract Commitment ID

[Contract Commitment ID](#col) is a service-provider-assigned identifier describing a single contract term agreed between a provider and a customer. Contracts can include commitments to a certain amount of spend or usage over an agreed period of time.

## Requirements

[ContractCommitmentId](#col) MUST adhere to the following requirements:

* [ContractCommitmentId](#col) MUST be of type String.
* [ContractCommitmentId](#col) MUST conform to [StringHandling](#attr) requirements.
* [ContractCommitmentId](#col) MUST NOT be null.
* [ContractCommitmentId](#col) MUST be a unique identifier within the service provider.
* [ContractCommitmentId](#col) SHOULD be a fully-qualified identifier.
* [ContractCommitmentId](#col) MUST have one and only one parent [ContractId](#col).
* [ContractCommitmentId](#col) MAY match [ContractId](#col).

## Column ID

ContractCommitmentId

## Display Name

Contract Commitment ID

## Description

A service-provider-assigned identifier describing a single contract term agreed between a service provider and a customer.

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
