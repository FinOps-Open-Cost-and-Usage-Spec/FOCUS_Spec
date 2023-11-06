# Discount Handling

A discount is a pricing construct where providers offer a reduced price for services. Providers may have many types of discounts, including but not limited to commercially negotiated discounts, commitment-based discounts when you agree to a certain amount of usage or spend, and bundled discounts where you receive free or discounted usage of one product or service based on the usage of another. Discount Handling is commonly used in scenarios like verifying discounts were applied and calculating cost savings.

Some discount offers can be purchased from a provider to get reduced prices. The most common example is commitment-based discounts, where you "purchase" a commitment to use or spend a specific amount within a period. There are instances where a portion of the purchased discount may go unused, which results in lost savings and needs to be clearly identifiable at a granular level. To facilitate this, the purchase amount is amortized over the term the discount is applied to (e.g., 1 year). Amortization is a process used to break down and spread purchase costs over a period of time or term of use. When a purchase is applicable to resources, like commitment-based discounts, the amortized cost of a resource takes the initial payment and term into account and distributes it out based on the resource's usage, attributing the prorated cost for each unit of billing. Amortization enables FinOps practitioners to distribute purchase charges to the appropriate audience in support of cost allocation efforts. Discount Handling for purchased commitments is commonly used for scenarios like calculating utilization and implementing chargeback for the purchase amount.

While providers may use different terms to describe discounts, FOCUS identifies a discount as being a reduced price applied directly to a row or charge. Any price or cost reductions that are awarded after the fact are identified as a "Credit" Charge Subcategory. One example might be when a provider offers a reduced rate after passing a certain threshold of usage or spend.

All rows defined in FOCUS MUST follow the discount handling requirements listed below.

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
  * The BilledCost MUST be 0 for any row where the commitment covers the entire cost for the charge period.
  * The EffectiveCost MUST be the portion of the amortized purchase cost that applies to this row.
  * CommitmentUtilization MUST be "Used" for rows that received a reduced price from that commitment.
  * If a commitment is not fully utilized, the provider MUST include a row that represents the unused portion of the commitment for that charge period. Charge Subcategory MUST be "Commitment Unused".
  * The sum of the EffectiveCost for all "Commitment Used" and "Commitment Unused" rows for each ChargeSubcategory MUST be the same as the BilledCost of the commitment-based discount purchase.
* Credits that are applied after the fact MUST use a ChargeType of "Adjustment" and ChargeSubcategory of "Credit".

## Exceptions

None

## Introduced (version)

1.0
