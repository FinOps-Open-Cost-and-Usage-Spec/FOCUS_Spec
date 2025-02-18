# Correction Handling

Corrections are line items that appear in the FOCUS data set to support any scenarios where providers need to adjust a charge to a consumer. These scenarios include: 

- [*Refund*](#glossary:refund) - experiencing a billing technical error (i.e. charging the incorrect rate/volume for a service line item)
- [*Credit*](#glossary:credit) - providing a promotional benefit (i.e. migration incentives or new service incentives)
- Metadata Corrections
- Late Arriving Charges

Refunds are applied to retrospective charge records where the usage has already been incurred whereas credits are applied in a forward looking perspective and are consumed ('burned-down') by future usage.

include original summary linking out to correction or refund attributes as appropriate

DO NOT INCLUDE REQUIREMENTS IN THIS SECTION

correction to non cost and non usage columns i.e. metadata MAY be applied retrospectively

do example for late arriving costs

matrix of different scenarios

Correction curent period
Correction previous period
Refund current period
Refund previous period
Credit current period
credit previous period
late arriving costs
































A discount is a pricing construct where providers offer a reduced price for [*services*](#glossary:service). Providers may have many types of discounts, including but not limited to commercially [*negotiated discounts*](#glossary:negotiated-discount), [*commitment discounts*](#glossary:commitment-discount) when you agree to a certain amount of usage or spend, and bundled discounts where you receive free or discounted usage of one product or *service* based on the usage of another. Discount Handling is commonly used in scenarios like verifying discounts were applied and calculating cost savings.

Some discount offers can be purchased from a provider to get reduced prices. The most common example is a *commitment discount*, where you "purchase" a commitment to use or spend a specific amount within a period. When a commitment isn't fully utilized, the unused amount reduces the potential savings from the discount and can even result in paying higher costs than without the discount. Due to this risk, unused commitment amounts need to be clearly identifiable at a granular level. To facilitate this, unused commitments are recorded with a separate row for each charge period where the commitment was not fully utilized. To show the impact of purchased discounts on each discounted row, discount purchases need the purchase amount to be amortized over the [*term*](#glossary:term) the discount is applied to (e.g., 1 year) with each [*charge period*](#glossary:chargeperiod) split and applied to each row that received the discount.

Amortization is a process used to break down and spread purchase costs over a period of time or *term* of use. When a purchase is applicable to resources, like *commitment discounts*, the amortized cost of a resource takes the initial payment and *term* into account and distributes it out based on the resource's usage, attributing the prorated cost for each unit of billing. Amortization enables users of billing data to distribute purchase charges to the appropriate audience in support of cost allocation efforts. Discount Handling for purchased commitments is commonly used for scenarios like calculating utilization and implementing chargeback for the purchase amount.

While providers may use different terms to describe discounts, FOCUS identifies a discount as being a reduced price applied directly to a row. Any price or cost reductions that are awarded after the fact are identified as a "Credit" Charge Category. One example might be when a provider offers a reduced rate after passing a certain threshold of usage or spend.

All rows defined in FOCUS MUST follow the discount handling requirements listed below.

## Attribute ID

CorrectionHandling

## Attribute Name

Correction Handling

## Description

Indicates how to include and apply discounts to usage charges or rows in a FOCUS dataset.

## Requirements

* All applicable discounts SHOULD be applied to each row they pertain to and SHOULD NOT be negated in a separate row.
* All discounts applied to a row MUST apply to the entire charge.
  * Multiple discounts MAY apply to a row, but they MUST apply to the entire charge covered by that row.
  * If a discount only applies to a portion of a charge, then the discounted portion of the charge MUST be split into a separate row.
  * Each discount MUST be identifiable using existing FOCUS columns.
    * Rows with a *commitment discount* applied to them MUST include a CommitmentDiscountId.
    * If a provider applies a discount that cannot be represented by a FOCUS column, they SHOULD include additional columns to identify the source of the discount.
* Purchased discounts (e.g., *commitment discounts*) MUST be amortized.
  * The BilledCost MUST be 0 for any row where the commitment covers the entire cost for the charge period.
  * The EffectiveCost MUST include the portion of the amortized purchase cost that applies to this row.
  * The sum of the EffectiveCost for all rows where CommitmentDiscountStatus is "Used" or "Unused" for each CommitmentDiscountId over the entire duration of the commitment MUST be the same as the total BilledCost of the *commitment discount*.
  * The CommitmentDiscountId and ResourceId MUST be set to the ID assigned to the *commitment discount*. ChargeCategory MUST be set to "Purchase" on rows that represent a purchase of a *commitment discount*.
  * CommitmentDiscountStatus MUST be "Used" for ChargeCategory "Usage" rows that received a reduced price from a commitment. CommitmentDiscountId MUST be set to the ID assigned to the discount. ResourceId MUST be set to the ID of the resource that received the discount.
  * If a commitment is not fully utilized, the provider MUST include a row that represents the unused portion of the commitment for that *charge period*. These rows MUST be represented with CommitmentDiscountStatus set to "Unused" and ChargeCategory set to "Usage". Such rows MUST have their CommitmentDiscountId and ResourceId set to the ID assigned to the *commitment discount*.
* Credits that are applied after the fact MUST use a ChargeCategory of "Credit".

## Exceptions

None

## Introduced (version)

1.2