# Credit Handling

 [*Credits*](#glossary:credit) are line items that appear in the FOCUS data set to support any scenarios where providers are providing a promotional benefit such as migration incentives, new service incentives or bundled discounts where you receive free or discounted usage of one product or *service* based on the usage of another. 

While providers may use different terms to describe credits / discounts, FOCUS identifies a discount as being a reduced price applied directly to a row. Whereas any price or cost reductions that are awarded after the fact are identified as a "Credit" Charge Category. One example might be when a provider offers a reduced rate after passing a certain threshold of usage or spend.[Discount Handling](#discounthandling)

Credits are applied in a forward looking perspective and are consumed ('burned-down') by future usage, as such they are distinct from [*Refunds*](#glossary:refund) which apply to retrospective charge records where the usage has already been incurred.

FOCUS supports two distinct models for the representation of [*Credits*](#glossary:credit) in the specification with the understanding that providers typically support the 'Bulk' record style, but SHOULD support the 'Itemized' record style where possible to improve visibility and attribution of this data.

-Bulk credits are typically represented as a single line item that may or may not be attributable to a given SKU
-Itemised credits are typically represented by multiple line items that include additional attribution data such as SKU, SubAccountID, Resource Name to allow for automatic attribution to the services and accounts being credited.

Credits may also have subsequent correction records (negative values) that should follow the format of the original record. In the event that a credit 'correction' needs to be applied to a previously invoiced billing period, appropriate 'Correction' records should be added to the current billing data set with a current dated 'Billing Period' and a 'Charge Period' that matches the date of the credit record that is being corrected (see [*Example*](#refunds:myexample)). FOCUS billing generators MUST NOT regenerate historic billing data from previously invoiced billing periods as it decouples the invoicing cycle from the billing activity data.

All rows defined in FOCUS MUST follow the credit handling requirements listed below.

Example billing scenarios are outlined in (replace for refunds.md)

## Attribute ID

CreditHandling

## Attribute Name

Credit Handling

## Description

Indicates how to include and apply credit rows in a FOCUS dataset.

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