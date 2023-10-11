# Billed Unit Price

The Billed Unit Price represents the unit price for a single pricing measurement unit, which incorporates various discounts like volume/tier-based rates, negotiated discounts, and commitment-based discounts. Billed Unit Price does not amortize upfront charges (one-time or recurring). This unit price can match the List Unit Price, if there are no discounts in place. This pricing is denominated in the [Billing Currency](#billingcurrency). It is used to calculate Billed Cost and savings based on financial optimization activities.

The BilledUnitPrice column MUST be present in the billing data. This column MUST be a numeric value of type Decimal within the range of non-negative decimal values. It MUST NOT contain null values in cases where the [ChargeType](#chargetype) is 'usage' or 'purchase'. When BilledUnitPrice is not null, multiplying BilledUnitPrice by [QuantityInPricingUnit](#quantityinpricingunit) MUST equal [BilledCost](#billedcost).

## Column ID

BilledUnitPrice

## Display name

Billed Unit Price

## Description

Represents the unit price for a single pricing measurement unit, which incorporates various discounts like volume/tier-based rates, negotiated discounts and commitment-based discounts.

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
