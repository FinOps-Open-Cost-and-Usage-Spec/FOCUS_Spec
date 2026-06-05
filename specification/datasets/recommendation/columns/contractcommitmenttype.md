# Contract Commitment Type

Contract Commitment Type is a service-provider-assigned name to identify the type of [*contract commitment*](#glossary:contract-commitment) a recommendation proposes to purchase. In the Recommendation dataset, Contract Commitment Type is commonly used to describe the kind of commitment recommended for a rate-optimization opportunity, stated in service-provider-specific terms.

## Requirements

ContractCommitmentType MUST adhere to the following requirements:

* ContractCommitmentType MUST be of type String.
* ContractCommitmentType MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* ContractCommitmentType MUST adhere to the following nullability requirements:
  * ContractCommitmentType MUST NOT be null when a recommendation proposes the purchase of a *contract commitment*.
  * ContractCommitmentType MUST be null when a recommendation does not propose the purchase of a *contract commitment*.

## Column ID

ContractCommitmentType

## Display Name

Contract Commitment Type

## Description

A service-provider-assigned name to identify the type of *contract commitment* a recommendation proposes to purchase.

## Content Constraints

| Constraint      | Value                                          |
| :-------------- | :--------------------------------------------- |
| Dataset         | [Recommendation](#datasets.recommendation)     |
| Column type     | Dimension                                      |
| Feature level   | Conditional                                    |
| Allows nulls    | True                                           |
| Data type       | String                                         |
| Value format    | \<not specified>                               |

## Version Introduced

1.5
