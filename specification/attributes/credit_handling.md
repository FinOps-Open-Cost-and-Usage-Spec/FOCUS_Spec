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

* TODO

## Exceptions

None

## Introduced (version)

1.3
