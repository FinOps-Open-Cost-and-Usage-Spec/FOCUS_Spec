# Charge Subcategory

Charge Subcategory indicates what kind of usage or [*adjustment*](#glossary:adjustment) the [*row*](#glossary:row) represents. Charge Subcategory is a supplemental detail to the [Charge Category](#chargecategory). It provides additional context to describe the primary category of charge.

This linkage to the parent Charge Category means that for every entry under Charge Category, there can be a corresponding Charge Subcategory that further refines the nature of the charge. It's a nested level of detail that allows users to see not just what type of charge was incurred. Current sub-categorization currently applies to Charge Category values "Usage" and "Adjustment". Support for others will be added as needed.

When Charge Category is "Usage" and the charge is related to a [*commitment*](#glossary:commitment), the Charge Subcategory indicates whether the row represents committed usage or is an [*amortized*](#glossary:amortization) charge for the unused portion of the *commitment*. Charge Subcategory is commonly used for scenarios like calculating *commitment* utilization when Charge Category is "Usage".

When Charge Category is "Adjustment", the Charge Subcategory indicates what kind of after-the-fact *adjustment* the record represents and is commonly used to identify changes like credits and refunds.

ChargeSubcategory MUST follow the requirements listed below:

* The ChargeSubcategory column MUST be present in the billing data when the provider supports sub-categorization of the [Charge Category](#chargecategory) values.
* ChargeSubcategory is of type String and MUST be one of the allowed values.
* ChargeSubcategory MUST NOT be null when ChargeCategory is "Usage" and the charge is covered by a *commitment*.
  * When a usage charge is covered by a *commitment*, ChargeSubcategory MUST be "Used Commitment".
  * When a *commitment* is not used, fully used, or partially used within the committed period ChargeSubcategory MUST be "Unused Commitment" for the unused usage charge.
* ChargeSubcategory MUST be null when ChargeCategory is "Usage" and is not covered by a *commitment*.
* ChargeSubcategory MUST NOT be null when ChargeCategory is "Adjustment".
  * When an *adjustment* applies to a specific item, the corresponding FOCUS columns that identify that item MUST NOT be null and MUST match the applicable item details the *adjustment* pertains to.
* ChargeSubcategory MUST be null when ChargeCategory is "Purchase" or "Tax".

## Column ID

ChargeSubcategory

## Display Name

Charge Subcategory

## Description

Indicates what kind of usage or *adjustment* the *row* represents.

## Content Constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column type     | Dimension      |
| FOCUS Essential | False          |
| Allows nulls    | True           |
| Data type       | String         |
| Value format    | Allowed values |

Allowed values when ChargeCategory is "Usage":

| Value             | Description                                                                            |
| :---------------- | :------------------------------------------------------------------------------------- |
| On-Demand         | Usage charges that are not associated with a commitment                                |
| Used Commitment   | Usage charges that are associated with consumption of a commitment's underlying basis. |
| Unused Commitment | Amortized usage charges for the portion of a commitment that has not been used. For example, if an organization has a commitment-based discount that is not fully utilized, the unused portion falls under this category. It highlights an area where the organization is not fully leveraging its commitments, which could be a lost cost-saving opportunity. |

Allowed values when ChargeCategory is "Adjustment":

| Value              | Description                                           |
| :----------------- | :-----------------------------------------------------|
| Refund             | Negative charges that were previously billed and are being returned by the provider. Providers can have multiple types of refunds such as resolving a tax error or for returned or exchanged commitment-based discounts. |
| Credit             | Negative charges granted by the provider for various scenarios, like negotiated benefits, usage discounts, or promotional credits.                                                                                       |
| Rounding Error     | Positive or negative charges that are needed to ensure raw billing data aggregations match the total cost on the invoice, which may be rounded.                                                                   |
| General Adjustment | Positive or negative charges the provider applies that do not fall into other adjustment category values.                                                                                                                |

## Introduced (version)

1.0
