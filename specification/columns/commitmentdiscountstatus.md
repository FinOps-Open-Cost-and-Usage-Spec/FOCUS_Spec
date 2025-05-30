# Commitment Discount Status

Commitment Discount Status indicates whether the [*charge*](#glossary:charge) corresponds with the consumption of a [*commitment discount*](#glossary:commitment-discount) identified in the CommitmentDiscountId column or the unused portion of the committed amount. The CommitmentDiscountStatus column is only applicable to *commitment discounts* and not [*negotiated discounts*](#glossary:negotiated-discount).

The CommitmentDiscountStatus column adheres to the following requirements:

* CommitmentDiscountStatus MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountStatus MUST be of type String.
* CommitmentDiscountStatus nullability is defined as follows:
  * CommitmentDiscountStatus MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null.
  * CommitmentDiscountStatus MUST NOT be null when CommitmentDiscountId is not null and [Charge Category](#chargecategory) is "Usage".
* CommitmentDiscountStatus MUST be one of the allowed values.

## Column ID

CommitmentDiscountStatus

## Display name

Commitment Discount Status

## Description

Indicates whether the *charge* corresponds with the consumption of a *commitment discount* or the unused portion of the committed amount.

## Content constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column type     | Dimension      |
| Feature level   | Conditional    |
| Allows nulls    | True           |
| Data type       | String         |
| Value format    | Allowed Values |

Allowed values:

| Value  | Description                                                             |
| :----- | :---------------------------------------------------------------------- |
| Used   | *Charges* that utilized a specific amount of a commitment discount.     |
| Unused | *Charges* that represent the unused portion of the commitment discount. |

## Introduced (version)

1.0
