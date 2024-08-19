# List Cost

List Cost represents the cost calculated by multiplying the [*list unit price*](#glossary:list-unit-price) and the corresponding [Pricing Quantity](#pricingquantity). List Cost is denominated in the [Billing Currency](#billingcurrency) and is commonly used for calculating savings based on various rate optimization activities, by comparing it with [Contracted Cost](#contractedcost), [Billed Cost](#billedcost) and [Effective Cost](#effectivecost).

**Important:** When aggregating List Cost for savings calculations, it's important to exclude either one-time or recurring charges ([Charge Category](#chargecategory) "Purchase") that are paid to cover future eligible charges (e.g., [*commitment-Based discount](#glossary:commitment-based-discount)) or the covered charges themselves. This exclusion helps prevent double counting of these charges in the aggregation. Which set of charges to exclude depends on whether cost are aggregated on a billed basis (exclude covered charges) or accrual basis (exclude Purchases for future charges). For instance, charges categorized as *Charge Category* "Purchase" and their related *Charge Category* "Tax" charges for a *commitment-based discount* might be excluded from an accrual basis cost aggregation of List Cost. This is because the "Usage" and "Tax" charge records provided during the [*term*](#glossary:term) of the commitment discount already specify the List Cost. Purchase charges that cover future eligible charges can be identified by filtering for *Charge Category* "Purchase" records with a [Billed Cost](#billedcost) greater than 0 and an [Effective Cost](#effectivecost) equal to 0.

The ListCost column adheres to the following requirements:

* ListCost MUST be present in a FOCUS dataset and MUST NOT be null.
* ListCost MUST be of type Decimal, MUST conform to [Numeric Format](#numericformat) requirements, and be denominated in the *BillingCurrency*.
* When [ListUnitPrice](#listunitprice) is present and not null, multiplying the *ListUnitPrice* by *PricingQuantity* MUST produce the ListCost, except in cases of [ChargeClass](#chargeclass) "Correction", which may address PricingQuantity or any cost discrepancies independently.
* ListCost MUST reflect the corresponding *commitment-based discount's* purchase's ListCost value, or be zero if no purchase record exists when *ChargeCategory* is "Usage" and [CommitmentDiscountStatus](#commitmentdiscountstatus) is "Unused".
* ListCost MUST be 0 when *ChargeCategory* is "Usage" and [CommitmentDiscountStatus](#commitmentdiscountstatus) is "Unused".

In cases where the *ListUnitPrice* is present and is null, the following applies:

* The ListCost of a charge calculated based on other charges (e.g., when the [ChargeCategory](#chargecategory) is "Tax") MUST be calculated based on the ListCost of those related charges.
* The ListCost of a charge unrelated to other charges (e.g., when the [ChargeCategory](#chargecategory) is "Credit") MUST match the [BilledCost](#billedcost).

## Column ID

ListCost

## Display Name

List Cost

## Description

Cost calculated by multiplying List Unit Price and the corresponding Pricing Quantity.

## Content Constraints

| Constraint      | Value                   |
|:----------------|:------------------------|
| Column type     | Metric                  |
| Feature level   | Mandatory               |
| Allows nulls    | False                   |
| Data type       | Decimal                 |
| Value format    | [Numeric Format](#numericformat) |
| Number range    | Any valid decimal value |

## Introduced (version)

1.0-preview
