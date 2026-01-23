# Effective Cost

Effective Cost represents the cost of a [*charge*](#glossary:charge) based on the [*resources*](#glossary:resource) used, [*services*](#glossary:service) used, or [*contract commitments*](#glossary:contract-commitment) consumed in a given [*charge period*](#glossary:charge-period). Effective Cost differs from [Billed Cost](#datasets.costandusage.billedcost) when *charges* (both pre-paid and post-paid) are invoiced separately from usage.

For all *charges*, Effective Cost reflects all applicable pricing adjustments (e.g., reduced pricing from [*negotiated discounts*](#glossary:negotiated-discount) or [*commitment discounts*](#glossary:commitment-discount)). For usage *charges*, Effective Cost includes the recognized portion of *Billed Cost* from related purchase *charges* (e.g., amortized portions of prepayments, drawdowns). For purchase *charges*, Effective Cost excludes any amounts recognized in related usage *charges* (e.g., usage covered by *commitments*, pre-payments, or marketplace purchases which draw down based on usage), regardless of when those related *charges* are invoiced.

Effective Cost is denominated in the [Billing Currency](#datasets.costandusage.billingcurrency). Effective Cost is commonly used to support FinOps activities, including [*accrual-based*](#glossary:accrual-based-accounting) reporting, forecasting, and cost allocation.

## Requirements

EffectiveCost adheres to the following requirements:

* EffectiveCost MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).
* EffectiveCost MUST be of type Decimal.
* EffectiveCost MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* EffectiveCost MUST NOT be null.
* EffectiveCost MUST be a valid decimal value.
* EffectiveCost MUST be 0 when [ChargeCategory](#datasets.costandusage.chargecategory) is "Purchase" and the purchase is intended to cover future eligible *charges*.
* EffectiveCost MUST be denominated in the BillingCurrency.
* The sum of EffectiveCost in a given *billing period* MAY differ from the sum of the invoices received for the same *billing period* for a [*billing account*](#glossary:billing-account).
* When ChargeCategory is not "Usage" or "Purchase", EffectiveCost adheres to the following additional requirements:
  * EffectiveCost of a *charge* calculated based on other *charges* (e.g., when the ChargeCategory is "Tax") MUST be calculated based on the EffectiveCost of those related *charges*.
  * EffectiveCost of a *charge* unrelated to other *charges* (e.g., when the ChargeCategory is "Credit") MUST match the [BilledCost](#datasets.costandusage.billedcost).
* *Charges* for a given [CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid) adhere to the following additional requirements:
  * The sum of EffectiveCost where ChargeCategory is "Usage" MUST equal the sum of BilledCost where ChargeCategory is "Purchase".
  * The sum of EffectiveCost where ChargeCategory is "Usage" MUST equal the sum of EffectiveCost where ChargeCategory is "Usage" and [CommitmentDiscountStatus](#datasets.costandusage.commitmentdiscountstatus) is "Used", plus the sum of EffectiveCost where ChargeCategory is "Usage" and CommitmentDiscountStatus is "Unused".

## Column ID

EffectiveCost

## Display Name

Effective Cost

## Description

Cost of a *charge* based on the *resources* or *services* used or *contract commitments* consumed in a given *charge period*.

## Content constraints

|    Constraint   |      Value              |
|:----------------|:------------------------|
| Column type     | Metric                  |
| Feature level   | Mandatory               |
| Allows nulls    | False                   |
| Data type       | Decimal                 |
| Value format    | [Numeric Format](#attributes.numericformat) |
| Number range    | Any valid decimal value |

## Introduced (version)

0.5
