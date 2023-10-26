# Negotiated Unit Price

The Negotiated Unit Price represents a unit price for a single pricing measurement unit, which incorporates volume/tier-based rates and negotiated discounts while excluding any commitment-based discounts and the amortization of upfront charges (one-time or recurring). This price is denominated in the  [Billing Currency](#billingcurrency). The Negotiated Unit Price can match the [List Unit Price](#listunitprice), if there are no negotiated discounts in place. It is used to calculate [Negotiated Cost](#negotiatedcost) and savings based on negotiation activities.

The NegotiatedUnitPrice column MUST be present in the billing data. This column MUST be a numeric value of type Decimal within the range of non-negative decimal values. It MUST NOT contain null if [SkuId](#skuid) is not null and it MUST be null if SkuId is null. When NegotiatedUnitPrice is not null, multiplying NegotiatedUnitPrice by [QuantityInPricingUnit](#quantityinpricingunit) MUST equal [NegotiatedCost](#negotiatedcost).

## Column ID

NegotiatedUnitPrice

## Display name

Negotiated Unit Price

## Description

A unit price for a single pricing measurement unit, which incorporates volume/tier-based rates and negotiated discounts while excluding any commitment-based discounts and the amortization of upfront charges (one-time or recurring).

## Content Constraints

| Constraint      | Value                                |
|:----------------|:-------------------------------------|
| Column required | True                                 |
| Data type       | Decimal                              |
| Allows nulls    | True                                 |
| Value format    | Numeric value                        |
| Number range    | Any valid non-negative decimal value |

## Introduced (version)

1.0
