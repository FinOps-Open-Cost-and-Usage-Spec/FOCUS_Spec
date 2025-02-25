# Commitment Discount Category

Commitment Discount Category indicates whether the [*commitment discount*](#glossary:commitment-discount) identified in the CommitmentDiscountId column is based on usage quantity or cost (aka "spend"). The CommitmentDiscountCategory column is only applicable to *commitment discounts* and not [*negotiated discounts*](#glossary:negotiated-discount).

The CommitmentDiscountCategory column adheres to the following requirements:

* CommitmentDiscountCategory MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountCategory MUST be of type String.
* CommitmentDiscountCategory MUST conform to [String Handling](#stringhandling) requirements.
* CommitmentDiscountId nullability is defined as follows:
  * CommitmentDiscountCategory MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null.
  * CommitmentDiscountCategory MUST NOT be null when CommitmentDiscountId is not null.
* CommitmentDiscountCategory MUST be one of the allowed values when not null.

## Column ID

CommitmentDiscountCategory

## Display Name

Commitment Discount Category

## Description

Indicates whether the *commitment discount* identified in the CommitmentDiscountId column is based on usage quantity or cost (aka "spend").

## Content constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | Allowed Values   |

Allowed values:

| Value   | Description                                                              |
|:--------|:-------------------------------------------------------------------------|
| Spend   | Commitment discounts that require a predetermined amount of spend. |
| Usage   | Commitment discounts that require a predetermined amount of usage. |

## Introduced (version)

1.0-preview
