# Charge Subcategory

Charge Subcategory is a detailed descriptor within the billing and usage reports that acts as a supplementary detail to the main ChargeType column. It essentially dissects the primary category of charge to indicate more specific information about how each cost item relates to predefined pricing commitments.

This linkage to the parent ChargeType means that for every entry under ChargeType, there is a corresponding Charge Subcategory that further refines the nature of the charge. It's a nested level of detail that allows users to see not just what type of charge was incurred, but also how that charge interacts with their purchasing agreements and discounts.

When Charge Type is "Usage", the Charge Subcategory specifies if the usage is accounted for by pre-purchased commitments or if the usage has not benefited from these discounts.

When Charge Type is "Adjustment", the Charge Subcategory indicates what kind of after-the-fact adjustment the record represents. Adjustment Category is commonly used to identify changes like credits and refunds.

ChargeSubcategory MUST abide by the following requirements:

- The ChargeSubcategory MUST be present in the billing data.
- ChargeSubcategory is of type String and MUST be one of the allowed values.
- ChargeSubcategory MUST NOT be null or empty when ChargeType is "Usage" and the charge is covered by a commitment.
  - When a usage charge is covered by a commitment, ChargeSubcategory MUST be "Commitment Used".
  - When a commitment is not used within the committed period, ChargeSubcategory MUST be "Commitment Unused" for the unused usage charge.
- ChargeSubcategory MUST NOT be null or empty when ChargeType is "Adjustment".
  - When ChargeSubcategory is "Refund" or "Credit", the charge MUST be negative.
  - When an adjustment applies to a specific item, the corresponding FOCUS columns that identify that item MUST NOT be null and MUST match the applicable item details the adjustment pertains to.
- ChargeSubcategory MUST be null when ChargeType is "Tax" or "Usage" and not covered by a commitment.

## Column ID

ChargeSubcategory

## Display Name

Charge Subcategory

## Description

Charge Subcategory is a detailed descriptor within the billing and usage reports that acts as a supplementary detail to the main ChargeType column.

## Content Constraints

| Constraint      | Value                                    |
| :-------------- | :--------------------------------------- |
| Column required | True                                     |
| Data type       | String                                   |
| Allows nulls    | True                                     |
| Value format    | list-of-values                           |

Allowed values for usage:

| Value      | Description                                                                                                                                                                   |
|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Commitment Used  | This Charge Subcategory value shows that the usage is covered by and benefiting from discounted rates due to pre-existing commitment agreements, such as Reserved Instances or Savings Plans.
| Commitment Unused | This value would represent the portion of a commitment that has not been used. For example, if an organization has reserved instances but is not utilizing all of them, the unused portion falls under this category. It highlights an area where the organization is not fully leveraging its commitments, which could be a lost cost-saving opportunity.

Allowed values for adjustments:

| Value      | Description                                                                                                                                                                   |
|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Refund | Negative charges that were previously billed and are being returned by the provider. Providers can have multiple types of refunds such as resolving a tax error or for returned or exchanged commitment-based discounts.
| Credit  | Negative charges granted by the provider for various scenarios, like negotiated benefits, usage discounts, or promotional credits.
| Rounding Error | Positive or negative charges that are needed to ensure raw cost and usage data aggregations match the total cost on the invoice, which may be rounded. |
| General Adjustment | Positive or negative charges the provider applies that do not fall into other adjustment category values. |

## Introduced (version)

1.0
