# Charge Subcategory

Charge Subcategory indicates what kind of usage or [*adjustment*](#glossary:adjustment) the row represents. Charge Subcategory is a supplemental detail to the [Charge Type](#chargetype). It provides additional context to describe the primary category of charge.

This linkage to the parent Charge Type means that for every entry under Charge Type, there can be a corresponding Charge Subcategory that further refines the nature of the charge. It's a nested level of detail that allows users to see not just what type of charge was incurred. Current sub-categorization currently applies to Charge Type values 'Usage' and 'Adjustment'. Support for others will be added as needed.

When Charge Type is "Usage" and the charge is related to a commitment, the Charge Subcategory indicates whether the row represents committed usage or is an [*amortized*](#glossary:amortization) charge for the unused portion of the commitment. Charge Subcategory is commonly used for scenarios like calculating commitment utilization when Charge Type is "Usage".

When Charge Type is "Adjustment", the Charge Subcategory indicates what kind of after-the-fact *adjustment* the record represents and is commonly used to identify changes like credits and refunds.

ChargeSubcategory MUST follow the requirements listed below:

* The ChargeSubcategory MUST be present in the billing data.
* ChargeSubcategory is of type String and MUST be one of the allowed values.
* ChargeSubcategory MUST NOT be null or empty when ChargeType is "Usage" and the charge is covered by a commitment.
  * When a usage charge is covered by a commitment, ChargeSubcategory MUST be "Used Commitment".
  * When a commitment is not used fully used or partially used within the committed period, ChargeSubcategory MUST be "Unused Commitment" for the unused usage charge.
* ChargeSubcategory MUST be null when ChargeType is "Usage" and is not covered by a commitment.
* ChargeSubcategory MUST NOT be null or empty when ChargeType is "Adjustment".
  * When an *adjustment* applies to a specific item, the corresponding FOCUS columns that identify that item MUST NOT be null and MUST match the applicable item details the *adjustment* pertains to.
* ChargeSubcategory MUST be null when ChargeType is "Purchase" or "Tax".

## Column ID

ChargeSubcategory

## Display Name

Charge Subcategory

## Description

Indicates what kind of usage or *adjustment* the row represents.

## Content Constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column required | True           |
| Data type       | String         |
| Allows nulls    | True           |
| Value format    | list-of-values |

Allowed values when ChargeType is `Usage`:

| Value             | Description                                                                                                                                                                                                                                                                                                                                                |
| :---------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| On-Demand         | Usage charges that are not associated with a commitment |
| Used Commitment   | Usage charges that are associated with consumption of a commitment's underlying basis.                                                                                                                                              |
| Unused Commitment | Amortized usage charges for the portion of a commitment that has not been used. For example, if an organization has a commitment-based discount that is not fully utilized, the unused portion falls under this category. It highlights an area where the organization is not fully leveraging its commitments, which could be a lost cost-saving opportunity. |

Allowed values when ChargeType is `Adjustment`:

| Value              | Description                                                                                                                                                                                                              |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Refund             | Negative charges that were previously billed and are being returned by the provider. Providers can have multiple types of refunds such as resolving a tax error or for returned or exchanged commitment-based discounts. |
| Credit             | Negative charges granted by the provider for various scenarios, like negotiated benefits, usage discounts, or promotional credits.                                                                                       |
| Rounding Error     | Positive or negative charges that are needed to ensure raw cost and usage data aggregations match the total cost on the invoice, which may be rounded.                                                                   |
| General Adjustment | Positive or negative charges the provider applies that do not fall into other adjustment category values.                                                                                                                |

## Introduced (version)

1.0
