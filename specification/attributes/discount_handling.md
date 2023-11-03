# Discount Handling

A discount is a type of pricing model in which cloud providers offer their customers a reduced price that is applied to the usage of the cloud provider’s services. There are many types of discounts that a cloud provider can support, including but not limited to commercially negotiated discounts, commitment-based discounts that offer lower prices when you agree to a certain amount of their services or spend, and bundled discounts where you receive free or discounted usage of one product or service based on the usage of another product or service. Discount handling is commonly used in scenarios for verifying discounts were applied and calculating cost savings.

Some of the discount offers can be purchased from a provider in order to get reduced prices. The most common example of this is commitment-based discounts, where you "purchase" a commitment to use or spend a specific amount within a period. There are instances where a portion of the purchased discount may go unused. This can result in effectively lost savings and needs to be clearly identifiable at a granular level to enable FinOps scenarios. In order to facilitate this, the amount of a purchased discount is amortized over the term that the discount is applied to (e.g., 1 year). Amortization is a process used to break down and spread the purchase costs over a period of time or term of use. When a purchase is applicable to resources, like commitment-based discounts, the amortized cost of a resource takes the initial payment and term into account and distributes it out based on the resource's usage, attributing the prorated cost for each hour of billing. Amortization provides a method for FinOps practitioners to reallocate purchase charges to the appropriate audience in support of their cost allocation efforts. Discount Handling for purchased commitments is commonly used for scenarios like calculating utilization and implementing chargeback of the purchase amount.

While providers may use different terms to describe discounts, FOCUS identifies a discount as being a reduced price applied directly to a row or charge. Any price or cost reductions that are awarded after the fact are identified as a "Credit" Adjustment Type. One example might be when a provider offers a reduced rate after passing a certain threshold of usage or spend.

## Attribute ID

DiscountHandling

## Attribute name

Discount Handling

## Description

Indicates how to include and apply discounts to usage charges or rows. 

## Requirements

* All applicable discounts MUST be applied to each row they pertain to and MUST NOT be negated in a separate row.
* All discounts applied to a row MUST apply to the entire charge. 
  * If a discount only applies to a subset of the charge, then that portion of the charge MUST be split into a separate row. One with the discount and one without.
  * If multiple discounts apply, there MUST be separate rows for each unique combination of applied discounts or undiscounted amount.
  * Each discount MUST be identifiable using existing FOCUS columns. 
    * Discounts applied to charges/rows from a commitment-based discount MUST include a CommitmentDiscountId.
    * If a provider applies a discount that cannot be represented by a FOCUS column, they SHOULD include additional columns to identify the source of the discount.
* Purchased discounts (e.g., commitment-based discounts) MUST specify CommitmentUtilization on the usage rows that received the reduced rates from the discount. 
* Purchased discounts (e.g., commitment-based discounts) MUST be amortized.
  * The BilledCost MUST be 0 for the discounted portion of the charge and the EffectiveCost MUST be the portion of the purchase cost that applies to this row.
  * CommitmentUtilization MUST be "Used" for rows that received a reduced price from that commitment.
  * If a commitment is not fully utilized, the provider MUST include a row that represents the unused portion of the commitment for that charge period. CommitmentUtilization MUST be "Not Used".
  * The sum of the EffectiveCost for all "Used" and "Not Used" rows for each CommitmentDiscountId MUST be the same as the BilledCost of the commitment-based discount purchase.
* Credits that are applied after the fact MUST use a ChargeType of "Adjustment" and AdjustmentCategory of "Credit".

## Exceptions

None

## Introduced (version)

1.0
