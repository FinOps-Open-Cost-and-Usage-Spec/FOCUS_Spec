# Effective Cost

The Effective Cost represents a charge inclusive of the impacts of all reduced rates and discounts, augmented with the amortization of relevant purchases (one-time or recurring) paid to cover future eligible charges. The amortized portion included should be proportional to the [Quantity In Pricing Unit](#quantityinpricingunit) and the time granularity of the data. This cost is denominated in the [Billing Currency](#billingcurrency). The Effective Cost is commonly utilized to track and analyze spending trends.

This metric resolves two challenges that are faced by practitioners:

1. Practitioners need to amortize relevant purchases over the duration of the commitment and distribute them to the appropriate reporting groups (e.g. tags, resources).
2. Many commitment-based discount constructs include a recurring expense for the commitment for every billing period and must distribute this cost to the resources using the commitment. This forces reconciliation between the initial commitment line item per period and the actual usage line items.

The EffectiveCost column MUST be present in the billing data. This column MUST be a valid numeric value of type Decimal and MUST NOT contain null values. The aggregated EffectiveCost for a billing period MAY NOT match the charge received on the invoice for the same billing period.

## Column ID

EffectiveCost

## Display name

Effective Cost

## Description

A charge inclusive of the impacts of all reduced rates and discounts, augmented with the amortization of relevant purchases (one-time or recurring) paid to cover future eligible charges.

### Concerning Granularity and Distribution of Recurring Fee

Providers should distribute the commitment purchase amount instead of including a line item at the beginning of a period so practitioners do not need to manually distribute the fee themselves.

### Concerning Amortization Approaches

The amortization of the upfront charge should be amortized using a methodology determined by the provider that reflects the needs of their customer base and is proportional with usage quantity and the time granularity of the line item. Should a practitioner desire to amortize upfront fees using a different approach, the practitioner can do so using the Billed Cost for the line item representing the initial purchase.

## Content constraints

|    Constraint   |      Value              |
|:----------------|:------------------------|
| Column required | True                    |
| Data type       | Decimal                 |
| Allows nulls    | False                   |
| Value format    | Numeric value           |
| Number range    | Any valid decimal value |

## Introduced (version)

0.5
