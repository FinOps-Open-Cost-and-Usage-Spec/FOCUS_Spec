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

* TODO

## Exceptions

None

## Introduced (version)

1.3
