# Commitment Discount Status

Commitment Discount Status indicates whether the charge corresponds with the consumption of the [*commitment-based discount*](#glossary:commitment-based-discount) identified in the CommitmentDiscountId column or the unused portion of the committed amount.

The CommitmentDiscountStatus column MUST be present in the billing data when the provider supports *commitment-based discounts*. This column MUST be of type String, MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null, and MUST NOT be null when CommitmentDiscountId is not null and [Charge Category](#chargecategory) is "Usage". The CommitmentDiscountCategory MUST be one of the allowed values.

## Column ID

CommitmentDiscountStatus

## Display name

Commitment Discount Status

## Description

Indicates whether the charge corresponds with the consumption of a *commitment-based discount* or the unused portion of the committed amount.

## Content constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column type     | Dimension      |
| Feature level   | Conditional    |
| Allows nulls    | True           |
| Data type       | String         |
| Value format    | Allowed Values |

Allowed values:

| Value  | Description                                                                 |
| :----- | :-------------------------------------------------------------------------- |
| Used   | Charges that utilized a specific amount of a commitment-based discount.     |
| Unused | Charges that represent the unused portion of the commitment-based discount. |

## Introduced (version)

1.0
