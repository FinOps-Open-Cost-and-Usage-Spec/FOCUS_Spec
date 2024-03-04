# Commitment Discount Category

Commitment Discount Category indicates whether the [*commitment-based discount*](#glossary:commitment-based-discount) identified in the CommitmentDiscountId column is based on usage quantity or cost (aka "spend").

The CommitmentDiscountCategory column MUST be present in the billing data when the provider supports *commitment-based discounts*. This column MUST be of type String, MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null, and MUST NOT be null when CommitmentDiscountId is not null. The CommitmentDiscountCategory MUST be one of the allowed values.

## Column ID

CommitmentDiscountCategory

## Display name

Commitment Discount Category

## Description

Indicates whether the *commitment-based discount* identified in the CommitmentDiscountId column is based on usage quantity or cost (aka "spend").

## Content constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column type     | Dimension        |
| FOCUS Essential | False            |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | Allowed Values   |

Allowed values:

| Value   | Description                                                              |
|:--------|:-------------------------------------------------------------------------|
| Spend   | Commitment-based discounts that require a predetermined amount of spend. |
| Usage   | Commitment-based discounts that require a predetermined amount of usage. |

## Introduced (version)

1.0
