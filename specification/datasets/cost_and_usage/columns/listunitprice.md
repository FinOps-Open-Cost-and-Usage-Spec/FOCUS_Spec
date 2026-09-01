# List Unit Price

List Unit Price represents the service-provider-suggested unit price per [Pricing Unit](#datamodel.costandusage.pricingunit) for the [*SKU Price*](#glossary:sku-price) identified by the given [SKU Price ID](#datamodel.costandusage.skupriceid).

List Unit Price does not reflect negotiated unit price adjustments for the associated *SKU Price* or any unit price impact conditional on a discount-bearing [*commitment program*](#glossary:commitment-program) (e.g., [*commitment discount*](#glossary:commitment-discount)) being applied to the [*charge*](#glossary:charge).

List Unit Price is denominated in the [Billing Currency](#datamodel.costandusage.billingcurrency). List Unit Price is commonly used for rate optimization activities.

## Requirements

ListUnitPrice MUST adhere to the following requirements:

* ListUnitPrice MUST be of type Decimal.
* ListUnitPrice MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* ListUnitPrice MUST adhere to the following nullability requirements:
  * ListUnitPrice MUST be null when SkuPriceId is null.
  * ListUnitPrice MUST be null when [ChargeCategory](#datamodel.costandusage.chargecategory) is "Tax".
  * ListUnitPrice MUST NOT be null when SkuPriceId is not null.
  * ListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#datamodel.costandusage.chargeclass) is not "Correction".
  * ListUnitPrice MAY be null in all other cases.
* When ListUnitPrice is not null, ListUnitPrice MUST adhere to the following requirements:
  * ListUnitPrice MUST be a non-negative decimal value.
  * ListUnitPrice MUST be denominated in the BillingCurrency.
  * ListUnitPrice MUST represent the service-provider-suggested unit price per PricingUnit for the SKU Price identified by the given SkuPriceId.
  * ListUnitPrice MUST NOT reflect negotiated unit price adjustments for the associated *SKU Price*.
  * ListUnitPrice MUST NOT reflect any unit price impact conditional on a discount-bearing *commitment program* being applied to the *charge*.

## Usability Constraints

**Aggregation:** Column values should only be viewed in the context of their row and not aggregated to produce a total.

## Column ID

ListUnitPrice

## Display Name

List Unit Price

## Description

The service-provider-suggested unit price per Pricing Unit for the *SKU Price* identified by the given SKU Price ID.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datamodel.costandusage)            |
| Column type     | Metric                                               |
| Feature level   | Mandatory                                            |
| Allows nulls    | True                                                 |
| Data type       | Decimal                                              |
| Value format    | [Numeric Format](#attributes.numericformat)          |
| Number range    | Any valid non-negative decimal value                 |

## Version Introduced

1.0-preview
