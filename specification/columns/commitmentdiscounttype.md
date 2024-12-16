# Commitment Discount Type

Commitment Discount Type is a provider-assigned name to identify the type of [*commitment discount*](#glossary:commitment-discount) applied to the [*row*](#glossary:row). The CommitmentDiscountType column is only applicable to *commitment discounts* and not [*negotiated discounts*](#glossary:negotiated-discount).

---
The CommitmentDiscountType column adheres to the following requirements:

* CommitmentDiscountType MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* If present, CommitmentDiscountType adheres to the following additional requirements:
  * CommitmentDiscountType MUST be of type String.
  * CommitmentDiscountType MUST conform to [String Handling](#stringhandling) requirements.
  * CommitmentDiscountType MUST be null if [CommitmentDiscountId](#commitmentdiscountid) is null.
  * CommitmentDiscountType MUST NOT be null if CommitmentDiscountId is not null.

---
The CommitmentDiscountType column adheres to the following requirements:

* The CommitmentDiscountType column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* This column MUST be of type String, MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null, and MUST NOT be null when CommitmentDiscountId is not null.

## Column ID

CommitmentDiscountType

## Display Name

Commitment Discount Type

## Description

A provider-assigned identifier for the type of *commitment discount* applied to the *row*.

## Content constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.0-preview
