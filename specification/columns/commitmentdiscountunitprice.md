# Commitment Discount Unit Price

Commitment Discount Unit Price represents the [*effective unit price*](#glossary:effectiveunitprice) for a single [Pricing Unit](#pricingunit) of the associated [*commitment discount's*](#glossary:commitmentdiscount) purchase or utilizing resource's SKU, exclusive of any [*negotiated discounts*](#negotiated-discount]). This price is denominated in the [Billing Currency](#billingcurrency) and is commonly used to calculate the discounted cost of a purchase or resource utilizing the *commitment discount*.

The CommitmentDiscountUnitPrice column adheres to the following requirements:

* CommitmentDiscountUnitPrice MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountUnitPrice MUST be a Decimal within the range of non-negative decimal values.
* CommitmentDiscountUnitPrice MUST conform to [Numeric Format](#numericformat) requirements.
* CommitmentDiscountUnitPrice MUST be denominated in the [*BillingCurrency*](#billingcurrency).
* CommitmentDiscountUnitPrice MUST be present when [*CommitmentDiscountId*](#commitmentdiscountid) is present.
* CommitmentDiscountUnitPrice MUST NOT include [*negotiated discounts*](#glossary:negotiated-discount)
* CommitmentDiscountUnitPrice MAY be null or any valid decimal value if [*ChargeClass*](#chargeclass) is "Correction".

When [*CommitmentDiscountCategory*](#commitmentdiscountcategory) is "Spend" and *ChargeClass* is not "Correction", the following applies:

* When [*ChargeCategory*](#chargecategory) is "Purchase", CommitmentDiscountUnitPrice MUST be the predefined amount of spend committed for each [*charge period*](glossary:chargeperiod) of the *commitment discount's* [*term*](glossary:term).
* When *ChargeCategory* is "Usage", CommitmentDiscountUnitPrice MUST be the *effective unit price* of the covering resource's SKU.

When *CommitmentDiscountCategory* is "Usage" and *ChargeClass* is not "Correction", the following applies:

* CommitmentDiscountUnitPrice MUST be the *effective unit price* for the preselected SKU.
* When *commitment discount flexibility* applies, the CommitmentDiscountUnitPrice of the covering resource's SKU MAY be different than the purchasing SKU.
* When [*commitment discount flexibility*](glossary:commitment-discount-flexibility) does not apply, the CommitmentDiscountUnitPrice of the covering resource's SKU MUST match the purchasing SKU.

## Column ID

CommitmentDiscountUnitPrice

## Display Name

Commitment Discount Unit Price

## Description

The *effective unit price* for a single Pricing Unit of the associated *commitment discount's* purchase or covering resource's SKU, exclusive of any *negotiated discounts*.

## Usability Constraints

**Aggregation:** Column values should only be viewed in the context of their row and not aggregated to produce a total.

## Content Constraints

| Constraint      | Value                                |
|:----------------|:-------------------------------------|
| Column type     | Metric                               |
| Feature level   | Conditional                          |
| Allows nulls    | True                                 |
| Data type       | Decimal                              |
| Value format    | [Numeric Format](#numericformat)     |
| Number range    | Any valid non-negative decimal value |

## Introduced (version)

1.2
