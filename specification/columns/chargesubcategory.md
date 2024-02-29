# Charge Subcategory

Charge Subcategory indicates what kind of usage or [*adjustment*](#glossary:adjustment) the [*row*](#glossary:row) represents. Charge Subcategory is a supplemental detail to the [Charge Category](#chargecategory). It provides additional context to describe the primary category of charge.

This linkage to the parent Charge Category means that for every entry under Charge Category, there can be a corresponding Charge Subcategory that further refines the nature of the charge. It's a nested level of detail that allows users to see not just what type of charge was incurred. Current sub-categorization currently applies to Charge Category values "Usage" and "Adjustment". Support for others will be added as needed.

When Charge Category is "Usage" and the charge is related to a [*commitment*](#glossary:commitment), the Charge Subcategory indicates whether the row represents committed usage or is an [*amortized*](#glossary:amortization) charge for the unused portion of the *commitment*. Charge Subcategory is commonly used for scenarios like calculating *commitment* utilization when Charge Category is "Usage".

When Charge Category is "Adjustment", the Charge Subcategory indicates what kind of after-the-fact *adjustment* the record represents and is commonly used to identify changes like credits and refunds.

ChargeSubcategory MUST follow the requirements listed below:

* The ChargeSubcategory MUST be present in the billing data.
* ChargeSubcategory is of type String and MUST be one of the allowed values.
* ChargeSubcategory MUST NOT be null when ChargeCategory is "Usage" and the charge is covered by a *commitment*.
  * When a usage charge is covered by a *commitment*, ChargeSubcategory MUST be *_commitment_*.
* ChargeSubcategory MUST be *_On-Demand_* when ChargeCategory is "Usage" and is not covered by a *commitment*.
* ChargeSubcategory MUST NOT be null when ChargeCategory is "Adjustment".
  * When an *adjustment* applies to a specific item, the corresponding FOCUS columns that identify that item MUST NOT be null and MUST match the applicable item details the *adjustment* pertains to.
* ChargeSubcategory MUST NOT be null when ChargeCategory is "Purchase".
  * When ChargeCategory is *purchase*, the corresponding FOCUS columns that identify that item MUST NOT be null and MUST match the applicable item details the *purchase* pertains to.


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
| Column required | True           |
| Allows nulls    | True           |
| Data type       | String         |
| Value format    | Allowed values |

Allowed values when ChargeCategory is "Usage":

| Value             | Description                                                                            |
| :---------------- | :------------------------------------------------------------------------------------- |
| On-Demand         | Usage charges that are not associated with a commitment                                |
| Commitment   | Usage charges that are associated with consumption of a commitment's underlying basis. |


Allowed values when ChargeCategory is "Adjustment":

| Value              | Description                                           |
| :----------------- | :-----------------------------------------------------|
| Refund             | Negative charges that were previously billed and are being returned by the provider. Providers can have multiple types of refunds such as resolving a tax error or for returned or exchanged commitment-based discounts. |
| Credit             | Negative charges granted by the provider for various scenarios, like negotiated benefits, usage discounts, or promotional credits.                                                                                       |
| Rounding Error     | Positive or negative charges that are needed to ensure raw billing data aggregations match the total cost on the invoice, which may be rounded.                                                                   |
| Other              | Positive or negative charges the provider applies that do not fall into other adjustment category values.                                                                                                                |

Allowed valuew when ChargeCategory is "Purchase"

| Value              | Description     |
| :------------------| :----------------------------------------------------------------------------------------|
| Commitment         | Purchase relates to a commitment based purchase such as reservation, savings plan or partial upfront reservation or savings plan |
| MarketPlace        | Purchase relates to a service purchased from the CSP marketplace |
| Other              | Purchase type not covered by commmitments or marketplace purchases |

## Introduced (version)

1.0
