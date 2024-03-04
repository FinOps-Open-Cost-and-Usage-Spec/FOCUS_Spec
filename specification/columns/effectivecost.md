# Effective Cost

Effective Cost represents a cost inclusive of the impacts of all reduced rates and discounts, augmented with the [*amortization*](#glossary:amortization) of relevant purchases (one-time or recurring) paid to cover future eligible charges. The *amortized* portion included should be proportional to the [Pricing Quantity](#pricingquantity) and the time granularity of the data. This cost is denominated in the [Billing Currency](#billingcurrency). The Effective Cost is commonly utilized to track and analyze spending trends.

This column resolves two challenges that are faced by practitioners:

1. Practitioners need to *amortize* relevant purchases, such as upfront fees, over the duration of the *commitment* and distribute them to the appropriate reporting groups (e.g. [*tags*](#glossary:tag), [*resources*](#glossary:resource)).
2. Many [*commitment-based discount*](#glossary:commitment-based-discount) constructs include a recurring expense for the *commitment* for every [*billing period*](#glossary:billing-period) and must distribute this cost to the *resources* using the *commitment*. This forces reconciliation between the initial *commitment* [*row*](#glossary:row) per period and the actual usage *rows*.

The EffectiveCost column MUST be present in the billing data and MUST NOT be null. This column MUST be of type Decimal, MUST conform to [Numeric Format](#numericformat), and be denominated in the BillingCurrency. The aggregated EffectiveCost for a billing period MAY NOT match the charge received on the invoice for the same *billing period*.

In cases where the [SkuPriceId](#skupriceid) is null, the following applies:

* The EffectiveCost MUST be calculated based on the EffectiveCost of the related charges if the charge is calculated based on other charges (e.g. [ChargeCategory](#chargecategory) is "Tax").
* The EffectiveCost MUST match the [BilledCost](#billedcost) if the charge is unrelated to other charges (e.g. [ChargeSubcategory](#chargesubcategory) is "Credit").

## Column ID

EffectiveCost

## Display name

Effective Cost

## Description

Cost inclusive of the impacts of all reduced rates and discounts, augmented with the *amortization* of relevant purchases (one-time or recurring) paid to cover future eligible *charges*.

### Concerning Granularity and Distribution of Recurring Fee

Providers should distribute the *commitment* purchase amount instead of including a *row* at the beginning of a period so practitioners do not need to manually distribute the fee themselves.

### Concerning Amortization Approaches

Eligible purchases should be *amortized* using a methodology determined by the provider that reflects the needs of their customer base and is proportional with the Pricing Quantity and the time granularity of the *row*. Should a practitioner desire to *amortize* relevant purchases using a different approach, the practitioner can do so using the [Billed Cost](#billedcost) for the line item representing the initial purchase.

## Content constraints

|    Constraint   |      Value              |
|:----------------|:------------------------|
| Column type     | Metric                  |
| FOCUS Essential | True                    |
| Allows nulls    | False                   |
| Data type       | Decimal                 |
| Value format    | [Numeric Format](#numericformat) |
| Number range    | Any valid decimal value |

## Introduced (version)

0.5
