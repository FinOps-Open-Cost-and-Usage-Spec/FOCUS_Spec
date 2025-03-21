# Commitment Discount Unit Price

The Commitment Discount Unit Price represents the [*effective unit price*](#glossary:effectiveunitprice) for a single [Pricing Unit](#pricingunit) of the associated [*commitment discount's*](#glossary:commitmentdiscount) purchase or covering resource's SKU, exclusive of any [*negotiated discounts*](#negotiated-discount]). This price is denominated in the [Billing Currency](#billingcurrency). The Commitment Discount Unit Price is commonly used to calculate the discounted cost of a purchase or resource utilizing the *commitment discount*.

The CommitmentDiscountUnitPrice column adheres to the following requirements:

* CommitmentDiscountUnitPrice MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* TCommitmentDiscountUnitPrice MUST be a Decimal within the range of non-negative decimal values, MUST conform to [Numeric Format](#numericformat) requirements, and be denominated in the BillingCurrency.
* CommitmentDiscountUnitPrice MUST be present when [*CommitmentDiscountId*](#commitmentdiscountid) is present.
* When CommitmentDiscountUnitPrice is present and is not null, multiplying CommitmentDiscountUnitPrice by [PricingQuantity](#pricingquantity) MUST equal [CommitmentDiscountCost](#commitmentdiscountcost), except in cases of ChargeClass "Correction", which may address PricingQuantity or any cost discrepancies independently.

When [CommitmentDiscountCategory](#commitmentdiscountcategory) is "Usage", the following applies:
* CommitmentDiscountUnitPrice MUST be the [*effective unit price*](glossary:effectiveunitprice) for the preselected SKU when [*ChargeCategory*] is "Purchase".
* CommitmentDiscountUnitPrice MUST be the [*effective unit price*](glossary:effectiveunitprice) of the covering resource's SKU when [*ChargeCategory*] is "Usage". In cases where [*commitment flexibility*] applies, the covering resource's [*SkuId*](#skuid) MAY be different than the purchasing *SkuId*.

When [CommitmentDiscountCategory](#commitmentdiscountcategory) is "Spend", the following applies:
* CommitmentDiscountUnitPrice MUST be the predefined amount of spend committed to each [*charge period*](glossary:chargeperiod) of the *commitment discount's* [*term*](glossary:term) when [*ChargeCategory*] is "Purchase".
* CommitmentDiscountUnitPrice MUST be the [*effective unit price*](glossary:effectiveunitprice) of the covering resource's SKU when [*ChargeCategory*] is "Usage".


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
