# Contracted Unit Price

[*Contracted Unit Price*](#glossary:contracted-unit-price) represents the negotiated unit price per [Pricing Unit](#datamodel.costandusage.pricingunit) for the [*SKU Price*](#glossary:sku-price) identified by the given [SKU Price ID](#datamodel.costandusage.skupriceid). It is the unit price before the application of any discount-bearing [*commitment programs*](#glossary:commitment-program) (e.g., [*commitment discount*](#glossary:commitment-discount)).

When no [*negotiated pricing terms*](#glossary:negotiated-pricing-terms) apply to the [*charge*](#glossary:charge), Contracted Unit Price defaults to [List Unit Price](#datamodel.costandusage.listunitprice).

Contracted Unit Price is denominated in the [Billing Currency](#datamodel.costandusage.billingcurrency). Contracted Unit Price is commonly used for negotiation and rate optimization activities.

## Requirements

ContractedUnitPrice MUST adhere to the following requirements:

* ContractedUnitPrice MUST be of type Decimal.
* ContractedUnitPrice MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* ContractedUnitPrice MUST adhere to the following nullability requirements:
  * ContractedUnitPrice MUST be null when SkuPriceId is null.
  * ContractedUnitPrice MUST be null when [ChargeCategory](#datamodel.costandusage.chargecategory) is "Tax".
  * ContractedUnitPrice MUST NOT be null when SkuPriceId is not null.
  * ContractedUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#datamodel.costandusage.chargeclass) is not "Correction".
  * ContractedUnitPrice MAY be null in all other cases.
* When ContractedUnitPrice is not null, ContractedUnitPrice MUST adhere to the following requirements:
  * ContractedUnitPrice MUST be a non-negative decimal value.
  * ContractedUnitPrice MUST be denominated in the BillingCurrency.
  * ContractedUnitPrice MUST reflect *negotiated pricing terms* for the *SKU Price* identified by the given SkuPriceId that are independent of any discount-bearing *commitment programs* being applied to the *charge*.
  * ContractedUnitPrice MUST NOT reflect any unit price impact dependent on a discount-bearing *commitment program* being applied to the *charge*.
  * ContractedUnitPrice MUST equal ListUnitPrice when no *negotiated pricing terms* apply to the *charge*.

## Implementation Guidance

Every *charge* with a SKU Price ID has a Contracted Unit Price, whether or not *negotiated pricing terms* apply. Agreeing to a contract does not by itself introduce *negotiated pricing terms*; only privately agreed terms that modify the service-provider-suggested pricing do.

Unlike List Unit Price, Contracted Unit Price reflects *negotiated pricing terms* when they apply to the *SKU Price* identified by the given SKU Price ID. These may include a negotiated unit price, a negotiated tier configuration, and [*negotiated FX pricing terms*](#glossary:negotiated-fx-pricing-terms), such as a negotiated currency exchange rate. When no *negotiated pricing terms* apply, Contracted Unit Price equals List Unit Price.

[Pricing Currency Contracted Unit Price](#datamodel.costandusage.pricingcurrencycontractedunitprice) does not reflect *negotiated FX pricing terms*, because it is before any currency exchange rate conversion.

The terms of a discount-bearing *commitment program* (e.g., a *commitment discount*) can also be negotiated, such as the unit price for its purchase, its discount, or its eligibility. Of these terms, Contracted Unit Price reflects only a negotiated unit price for the commitment purchase itself (i.e., the [*covering charge*](#glossary:covering-charge)). The impact of applying the *commitment program* to [*covered charges*](#glossary:covered-charge) is reflected in their [Effective Cost](#datamodel.costandusage.effectivecost), whether or not the program's discount or eligibility is negotiated.

## Usability Constraints

**Aggregation:** Column values should only be viewed in the context of their row and not aggregated to produce a total.

## Column ID

ContractedUnitPrice

## Display Name

Contracted Unit Price

## Description

The negotiated unit price per Pricing Unit for the *SKU Price* identified by the given SKU Price ID.

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

1.0
