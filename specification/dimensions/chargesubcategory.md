# ChargeSubcategory

Charge Subcategory is a detailed descriptor within the billing and usage reports that acts as a supplementary detail to the main ChargeType column. It essentially dissects the primary category of charge to indicate more specific information about how each cost item relates to predefined pricing commitments.

This linkage to the parent ChargeType means that for every entry under ChargeType, there is a corresponding Charge Subcategory that further refines the nature of the charge. It's a nested level of detail that allows users to see not just what type of charge was incurred, but also how that charge interacts with their purchasing agreements and discounts.

When "ChargeType" is classified as "Usage", the corresponding "Charge Subcategory" includes values such as "Commitment Used" and "Commitment Unused". These values specify if the usage is accounted for by pre-purchased commitments like Savings Plans and Reserved Instances, or if the usage has not benefited from these discounts.

When Charge Type is "Adjustment", the Charge Subcategory is "Adjustment Category" indicates what kind of after-the-fact adjustment the record represents. Adjustment Category is commonly used to identify changes like credits and refunds.

ChargeSubcategory column MUST be present and MUST be null or empty. This column is of type String and SHOULD be one of the allowed values or a value of choosing from the cloud provider.

## Column ID

ChargeSubcategory

## Display Name

ChargeSubcategory

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

## Introduced (version)

1.0
