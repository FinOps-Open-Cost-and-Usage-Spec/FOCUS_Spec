# Commitment Discount Status

Commitment Discount Status indicates whether the [*charge*](#glossary:charge) corresponds with the consumption of a [*commitment discount*](#glossary:commitment-discount) identified in the CommitmentDiscountId column or the unused portion of the committed amount. The CommitmentDiscountStatus column is only applicable to *commitment discounts*, i.e., [*public commitment discounts (no carry-over)*](#glossary:public-commitment-discount-no-carry-over).

## Requirements

CommitmentDiscountStatus adheres to the following requirements:

* CommitmentDiscountStatus MUST be of type String.
* CommitmentDiscountStatus nullability is defined as follows:
  * CommitmentDiscountStatus MUST be null when [CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid) is null.
  * CommitmentDiscountStatus MUST NOT be null when CommitmentDiscountId is not null and [Charge Category](#datasets.costandusage.chargecategory) is "Usage".
* CommitmentDiscountStatus MUST be one of the allowed values.

## Column ID

CommitmentDiscountStatus

## Display name

Commitment Discount Status

## Description

Indicates whether the *charge* corresponds with the consumption of a *commitment discount* or the unused portion of the committed amount.

## Content constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | Allowed Values                                       |

Allowed values:

| Value  | Description                                                             |
| :----- | :---------------------------------------------------------------------- |
| Used   | *Charges* that utilized a specific amount of a commitment discount.     |
| Unused | *Charges* that represent the unused portion of the commitment discount. |

## Introduced (version)

1.0
