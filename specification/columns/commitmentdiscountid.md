# Commitment Discount ID

A Commitment Discount ID is the identifier assigned to a [*commitment discount*](#glossary:commitment-discount) by the service provider. Commitment Discount ID is commonly used for scenarios like chargeback for *commitments* and savings per *commitment discount*. The CommitmentDiscountId column is only applicable to *commitment discounts* and not [*negotiated discounts*](#glossary:negotiated-discount).

The CommitmentDiscountId column adheres to the following requirements:

* The CommitmentDiscountId column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.
* This column MUST be of type String and MUST NOT contain null values when a charge is related to a *commitment discount*.
* When a charge is not associated with a *commitment discount*, the column MUST be null.
* CommitmentDiscountId MUST ensure global uniqueness within the service provider and SHOULD be a fully-qualified identifier.

## Column ID

CommitmentDiscountId

## Display Name

Commitment Discount ID

## Description

The identifier assigned to a *commitment discount* by the service provider.

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
