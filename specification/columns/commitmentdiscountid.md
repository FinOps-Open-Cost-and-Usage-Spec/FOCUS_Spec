# Commitment Discount ID

A Commitment Discount ID is the identifier assigned to a [*commitment discount*](#glossary:commitment-discount) by the provider. Commitment Discount ID is commonly used for scenarios like chargeback for *commitments* and savings per *commitment discount*. The CommitmentDiscountId column is only applicable to *commitment discounts* and not [*negotiated discounts*](#glossary:negotiated-discount).

---
The CommitmentDiscountId column adheres to the following requirements:

* CommitmentDiscountId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* If present, CommitmentDiscountId adheres to the following additional requirements:
  * CommitmentDiscountId MUST be of type String.
  * CommitmentDiscountId MUST conform to [String Handling](#stringhandling) requirements.
  * CommitmentDiscountId MUST be null when a charge is not related to a *commitment discount*.
  * CommitmentDiscountId MUST NOT be null when a charge is related to a *commitment discount*.
  * CommitmentDiscountId MUST ensure global uniqueness within the provider.
  * CommitmentDiscountId SHOULD be a fully-qualified identifier.

---
The CommitmentDiscountId column adheres to the following requirements:

* The CommitmentDiscountId column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* This column MUST be of type String and MUST NOT contain null values when a charge is related to a *commitment discount*.
* When a charge is not associated with a *commitment discount*, the column MUST be null.
* CommitmentDiscountId MUST ensure global uniqueness within the provider and SHOULD be a fully-qualified identifier.

## Column ID

CommitmentDiscountId

## Display Name

Commitment Discount ID

## Description

The identifier assigned to a *commitment discount* by the provider.

## Content constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.0-preview
