# Charge Subcategory

Charge Subcategory is a detailed descriptor within the billing and usage reports that acts as a supplementary detail to the main ChargeType column. It essentially dissects the primary category of charge to indicate more specific information about how each cost item relates to predefined pricing commitments.

This linkage to the parent ChargeType means that for every entry under ChargeType, there is a corresponding Charge Subcategory that further refines the nature of the charge. It's a nested level of detail that allows users to see not just what type of charge was incurred, but also how that charge interacts with their purchasing agreements and discounts.

When ChargeType is "Usage", the Charge Subcategory is list of values such as Commitment Used and Commitment Unused to show that the usage is covered by pre-purchased commitment agreements such as Savings Plans and Reserved Instances or did not apply those discounts.

When Charge Type is "Adjustment", the Charge Subcategory is "Adjustment Category" indicates what kind of after-the-fact adjustment the record represents. Adjustment Category is commonly used to identify changes like credits and refunds.

- The ChargeSubCategory column MUST be present and MUST NOT be null or empty when ChargeType is "Adjustment".
- ChargeSubCategory is of type String and MUST be one of the allowed values.
- AdjustmentCategory MUST be null when ChargeType is not "Adjustment". 
- This column is of type String and MUST be one of the allowed values.
- When AdjustmentCategory is "Refund" or "Credit", the charge MUST be negative.
- When an adjustment applies to a specific item, the corresponding FOCUS columns that identify that item MUST NOT be null and MUST match the applicable item details the adjustment pertains to.

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
