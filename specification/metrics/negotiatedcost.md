# Negotiated Cost

The Negotiated Cost represents a charge inclusive of the impacts of volume/tier-based rates and negotiated discounts while excluding any commitment-based discounts or the amortization of upfront charges (one-time or recurring). This cost is denominated in the [Billing Currency](#billingcurrency). The Negotiated Cost equals the [List Cost](#listcost) when no negotiated discounts are present. It is used to calculate savings based on negotiation activities, by comparing it with List Cost.

The NegotiatedCost column MUST be present in the billing data. This column MUST be a valid numeric value of type Decimal and MUST NOT contain null values. When a [NegotiatedUnitPrice](#negotiatedunitprice) is not null, multiplying the NegotiatedUnitPrice by [QuantityInPricingUnit](#quantityinpricingunit ) MUST produce the NegotiatedCost. In cases where the NegotiatedUnitPrice is null, the following applies:

* If the line item is based on other charges (e.g. [ChargeType](#chargetype) is 'Tax'), the NegotiatedCost MUST be calculated based on NegotiatedCost of the related charges
* If the line item is unrelated to other charges (e.g. [AdjustmentType](#adjustmenttype) is 'Credit'), the NegotiatedCost MUST match the BilledCost.

## Column ID

NegotiatedCost

## Display name

Negotiated Cost

## Description

A charge inclusive of the impacts of volume/tier-based rates and negotiated discounts while excluding any commitment-based discounts or the amortization of upfront charges (one-time or recurring).

## Content constraints

|    Constraint   |      Value              |
|:----------------|:------------------------|
| Column required | True                    |
| Data type       | Decimal                 |
| Allows nulls    | False                   |
| Value format    | Numeric value           |
| Number range    | Any valid decimal value |

## Introduced (version)

1.0
