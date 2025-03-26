# Refund Handling

[*Refunds*](#glossary:refund) are line items that appear in the FOCUS data set to support any scenarios where providers need to rectify charges for usage that has already been incurred this is typically used to correct a billing / pricing technical errors such as charging a service at the incorrect rate or volume for a given SKU.

[*Refunds*](#glossary:refund) specifically apply to retrospective charge records where the usage has already been incurred, as such they are distinct from [*Credits*](#glossary:credit) which are applied in a forward looking perspective and are consumed ('burned-down') by future usage.

[*Refunds*](#glossary:refund) are intentionally not a separate 'Charge Category' in FOCUS as the objective is to have these adjustments handled as itemized 'Usage' or 'Purchase' 'Correction' records that can be recorded alongside the itemised charge record that is being refunded. This eliminates the chargeback reverse-enginnering practicioners face when handling bulk refunds that are submitted as a single line item (as the practicioner then needs to split that line item up and work out who should be refunded for what).

As such FOCUS supports two distinct models for the representation of [*Refunds*](#glossary:refund) in the specification with the understanding that providers typically support the 'Bulk' record style, but SHOULD support the 'Itemized' record style where possible to improve visibility and attribution of this data.

-Bulk Refunds are typically represented as a single line item that SHOULD be attributable to a given SKU
-Itemised Refunds are typically represented by multiple line items that include additional attribution data such as SKU, SubAccountID, Resource Name to allow for automatic attribution to the services and accounts being refunded.

In the event that a refund needs to be applied to a previously invoiced billing period, appropriate 'Correction' records should be added to the current billing data set with a current dated 'Billing Period' and a 'Charge Period' that matches the date of the record that is being refunded. FOCUS billing generators MUST NOT regenerate historic billing data from PREVIOUSLY CLOSED BILLING PERIODS as it decouples the invoicing cycle from the billing activity data.

All rows defined in FOCUS MUST follow the refund handling requirements listed below.

Example billing scenarios are outlined in (replace for refunds.md)

## Attribute ID

RefundHandling

## Attribute Name

Refund Handling

## Description

Indicates how to include and apply refunds to usage charges or rows in a FOCUS dataset.

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
