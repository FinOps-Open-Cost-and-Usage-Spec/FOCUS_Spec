# Effective Cost

Effective Cost represents the cost of a [*charge*](#glossary:charge) based on the [*resources*](#glossary:resource) used, [*services*](#glossary:service) used, or [*contract commitments*](#glossary:contract-commitment) recognized in a given [*charge period*](#glossary:charge-period). Effective Cost differs from [Billed Cost](#datasets.costandusage.billedcost) when *charges* (both pre-paid and post-paid) are invoiced separately from usage.

For all *charges*, Effective Cost reflects all applicable pricing adjustments (e.g., reduced pricing from [*negotiated discounts*](#glossary:negotiated-discount) or [*commitment discounts*](#glossary:commitment-discount)). For usage *charges*, Effective Cost includes the recognized portion of *Billed Cost* from related purchase *charges* (e.g., amortized portions of prepayments, drawdowns). For purchase *charges*, Effective Cost excludes any amounts recognized in related usage *charges* (e.g., usage covered by *commitments*, pre-payments, or marketplace purchases which draw down based on usage), regardless of when those related *charges* are invoiced.

Effective Cost is denominated in the [Billing Currency](#datasets.costandusage.billingcurrency). Effective Cost is commonly used to support FinOps activities, including [*accrual-based*](#glossary:accrual-based-accounting) reporting, forecasting, and cost allocation.

## Requirements

EffectiveCost adheres to the following requirements:

* EffectiveCost MUST be of type Decimal.
* EffectiveCost MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* EffectiveCost MUST NOT be null.
* EffectiveCost MUST be a valid decimal value.
* EffectiveCost MUST be denominated in the BillingCurrency.
* EffectiveCost MUST reflect all applicable pricing adjustments, including but not limited to *negotiated discounts*, *commitment discounts*, and other applicable discount programs.
* EffectiveCost MUST equal BilledCost when ChargeCategory is "Usage" and the *charge* is not covered by other eligible *charges*.
* EffectiveCost MUST equal BilledCost when ChargeCategory is "Purchase" and the *charge* is neither intended to cover other eligible *charges* nor covered by other eligible *charges*.
* EffectiveCost MUST equal BilledCost when ChargeCategory is "Tax" or "Credit".
* EffectiveCost MAY differ from BilledCost when ChargeCategory is "Adjustment".
* EffectiveCost MUST be 0 when [ChargeCategory](#datasets.costandusage.chargecategory) is "Purchase" and the purchase is intended to cover related eligible *charges*.
* The sum of the EffectiveCost of eligible *charges* covered by a purchase *charge* (ChargeCategory is "Purchase") MUST equal the sum of the BilledCost of the purchase and covered usage *charges* (ChargeCategory is "Usage"), over the *charge period* the purchase applies to, even in cases where the purchase and eligible usage *charges* have different cost origins (e.g., commitment discount, prepayment, marketplace purchase scenarios).
* The sum of EffectiveCost in a given *billing period* MAY differ from the sum of the BilledCost for the same *billing period* for granularities like [*billing account*](#glossary:billing-account) and ServiceProviderName when the covered *charges* span more than one *billing period*, *billing account*, and in cases where the purchase records and usage records have different cost origins (e.g., commitment discount, prepayment, marketplace purchase scenarios).

## Column ID

EffectiveCost

## Display Name

Effective Cost

## Description

Cost of a *charge* based on the *resources* used, *services* used, or *contract commitments* recognized in a given *charge period*.

## Content constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Metric                                               |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | Decimal                                              |
| Value format    | [Numeric Format](#attributes.numericformat)          |
| Number range    | Any valid decimal value                              |

## Introduced (version)

0.5
