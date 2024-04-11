# Commitment Discount Category

Commitment Discount Category indicates whether the [*commitment-based discount*](#glossary:commitment-based-discount) identified in the CommitmentDiscountId column is based on usage quantity or cost (aka "spend").

The CommitmentDiscountCategory column MUST be present in the billing data when the provider supports *commitment-based discounts*. This column MUST be of type String data and MUST contain one of the allowed enumerated values:
* "Spend": Commitment-based discounts that require a predetermined amount of spend.
* "Usage": Commitment-based discounts that require a predetermined amount of usage.

Additionally:
 IF [CommitmentDiscountId](#commitmentdiscountid) is null, THEN CommitmentDiscountCategory MUST also be null.
 IF [CommitmentDiscountId](#commitmentdiscountid) is not null, THEN CommitmentDiscountCategory MUST NOT be null and adhere to the allowed enumerated values.

## Column ID

CommitmentDiscountCategory

## Display Name

Commitment Discount Category

## Description

Indicates whether the *commitment-based discount* identified in the CommitmentDiscountId column is based on usage quantity or cost (aka "spend").

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
| Spend   | Commitment-based discounts that require a predetermined amount of spend. |
| Usage   | Commitment-based discounts that require a predetermined amount of usage. |

## Introduced (version)

1.0
