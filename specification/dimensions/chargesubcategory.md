# Charge SubCategory

ChargeSubCategory is a categorization method within cloud billing to reflect the utilization status of any committed discount programs such as savings plans or reserved instances. This categorization is particularly relevant for resources that can be covered under commitment-based pricing models, which are commonly offered by cloud service providers.

ChargeSubCategory indicates the relationship between the usage of resources such as AWS EC2 instances, Azure VMs, or GCP's Compute Engine and the pre-purchased commitment plans.

An adjustment is a positive or negative change in cost applied after the original usage or purchase record(s). Adjustments may be related to one or more charges and are identified by the ChargeType column.

Adjustment Category indicates what kind of after-the-fact adjustment the record represents. Adjustment Category is commonly used to identify changes like credits and refunds.

ChargeSubCategory is essential for distinguishing whether resource consumption aligns with the pre-bought commitment agreements or falls outside their scope. When utilization is within the ambit of these commitments, the corresponding resources benefit from the agreed-upon reduced rates. Conversely, if there is a lack of utilization, it could mean either that the resources, while eligible, are not capitalizing on the available commitments, or that they simply do not qualify for the commitments that have been procured.

- The ChargeSubCategory column MUST be present and MUST NOT be null or empty when ChargeType is "Adjustment".
- ChargeSubCategory is of type String and MUST be one of the allowed values.
- AdjustmentCategory MUST be null when ChargeType is not "Adjustment". 
- This column is of type String and MUST be one of the allowed values.
- When AdjustmentCategory is "Refund" or "Credit", the charge MUST be negative.
- When an adjustment applies to a specific item, the corresponding FOCUS columns that identify that item MUST NOT be null and MUST match the applicable item details the adjustment pertains to.

## Column ID

ChargeSubCategory

## Display Name

ChargeSubCategory

## Description

A variation in the billed amount that reflects whether the resource usage corresponds to pre-arranged discount agreements subsequent to the initial usage or purchase records.

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
| CommitmentCoveredUsage | This value indicates that the usage of resources, such as EC2 instances, Azure VMs, or GCP's Compute Engine, has been covered under a commitment-based discount plan. Essentially, the resources being used are within the scope of what the organization has agreed to utilize, and therefore, they benefit from the discounted rate.
| CommitmentUsed  | The resources are being used as per the commitment terms. However, this could also imply that the commitment has been fully utilized, and any additional usage might not be covered by the commitment, thus subject to standard pricing.
| CommitmentUnused | This value would represent the portion of a commitment that has not been used. For example, if an organization has reserved instances but is not utilizing all of them, the unused portion falls under this category. It highlights an area where the organization is not fully leveraging its commitments, which could be a lost cost-saving opportunity.


Allowed values for adjustments:

| Value      | Description                                                                                                                                                                   |
|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Refund | Negative charges that were previously billed and are being returned by the provider. Providers can have multiple types of refunds such as resolving a tax error or for returned or exchanged commitment-based discounts.
| Credit  | Negative charges granted by the provider for various scenarios, like negotiated benefits, usage discounts, or promotional credits.
| Rounding Error | Positive or negative charges that are needed to ensure raw cost and usage data aggregations match the total cost on the invoice, which may be rounded. |
| General Adjustment | Positive or negative charges the provider applies that do not fall into other adjustment category values. |

## Introduced (version)

1.0
