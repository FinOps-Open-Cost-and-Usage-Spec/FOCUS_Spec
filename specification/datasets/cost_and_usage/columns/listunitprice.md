# List Unit Price

[*List Unit Price*](#glossary:list-unit-price) represents the service-provider-suggested unit price per [Pricing Unit](#datamodel.costandusage.pricingunit) for the [*SKU Price*](#glossary:sku-price) identified by the given [SKU Price ID](#datamodel.costandusage.skupriceid). It is the unit price before the application of any [*negotiated pricing terms*](#glossary:negotiated-pricing-terms) or discount-bearing [*commitment programs*](#glossary:commitment-program) (e.g., [*commitment discount*](#glossary:commitment-discount)).

List Unit Price is denominated in the [Billing Currency](#datamodel.costandusage.billingcurrency). List Unit Price is commonly used for negotiation and rate optimization activities.

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
  * ListUnitPrice MUST represent the service-provider-suggested unit price per PricingUnit for the *SKU Price* identified by the given SkuPriceId.
  * ListUnitPrice MUST NOT reflect *negotiated pricing terms* for the associated *SKU Price*.
  * ListUnitPrice MUST NOT reflect any unit price impact dependent on a discount-bearing *commitment program* being applied to the [*charge*](#glossary:charge).

## Implementation Guidance

List Unit Price is the service-provider-suggested unit price that commonly serves as the starting point for negotiation. It is not necessarily publicly available. For example, it can be provided only in a [*price list*](#glossary:price-list) specific to a customer.

List Unit Price does not reflect any *negotiated pricing terms*. This includes the following cases, which may be less obvious:

* Tier configuration: a negotiated tier configuration results in SKU Price IDs that differ from those of the service-provider-suggested one. For these SKU Price IDs, List Unit Price is the service-provider-suggested unit price for the same quantity under the service-provider-suggested tier configuration.
* Currency exchange rates: when the [Pricing Currency](#datamodel.costandusage.pricingcurrency) differs from the Billing Currency, List Unit Price does not reflect [*negotiated FX pricing terms*](#glossary:negotiated-fx-pricing-terms), such as a negotiated currency exchange rate, even though it is denominated in the Billing Currency.

## Usability Constraints

**Aggregation:** Column values should only be viewed in the context of their row and not aggregated to produce a total.

## Column ID

ListUnitPrice

## Display Name

List Unit Price

## Description

The service-provider-suggested unit price per Pricing Unit for the *SKU Price* identified by the given SKU Price ID.

## Content Constraints

| Constraint                 | Value                                       |
| :------------------------- | :------------------------------------------ |
| Dataset                    | [Cost and Usage](#datamodel.costandusage)   |
| Operating Model Conditions | [Includes Unit Pricing](#operatingmodelconditions.includesunitpricing) |
| Column type                | Metric                                      |
| Feature level              | Conditional                                 |
| Allows nulls               | True                                        |
| Data type                  | Decimal                                     |
| Value format               | [Numeric Format](#attributes.numericformat) |
| Number range               | Any valid non-negative decimal value        |

## Version Introduced

1.0-preview
