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
* EffectiveCost MUST equal BilledCost when the *charge* is unrelated to other *charges*.
* EffectiveCost MUST be 0 when [ChargeCategory](#datasets.costandusage.chargecategory) is "Purchase" and the purchase is intended to cover related eligible *charges*.
* EffectiveCost MUST be derived from the EffectiveCost of underlying *charges* when ChargeCategory is "Tax" or "Adjustment".
* The sum of EffectiveCost MUST equal the sum of BilledCost within [*dataset artifacts*](#glossary:dataset-artifact) from a single data generator when those *dataset artifacts* include both purchase *charges* (ChargeCategory is "Purchase") and the related eligible *charges* they are intended to cover from the same source, or when the artifact contains neither purchase nor covered charges.
* The sum of EffectiveCost MAY differ from the sum of BilledCost within [*dataset artifacts*](#glossary:dataset-artifact) from a single data generator when the artifact contains only purchase *charges* (ChargeCategory is "Purchase") or only the related eligible *charges* they are intended to cover, and those *charges* originate from different data sources (e.g., marketplace scenarios).
* The sum of EffectiveCost in a given *billing period* MAY differ from the sum of the payable amounts provided in the invoices received for the same *billing period* for a [*billing account*](#glossary:billing-account).
* *Charges* for a given [CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid) adhere to the following additional requirements:
  * The sum of EffectiveCost where ChargeCategory is "Usage" MUST equal the sum of BilledCost where ChargeCategory is "Purchase".
  * The sum of EffectiveCost where ChargeCategory is "Usage" MUST equal the sum of EffectiveCost where ChargeCategory is "Usage" and [CommitmentDiscountStatus](#datasets.costandusage.commitmentdiscountstatus) is "Used", plus the sum of EffectiveCost where ChargeCategory is "Usage" and CommitmentDiscountStatus is "Unused".
  * When CommitmentDiscountStatus is "Used", EffectiveCost MUST represent the portion of the amortized *commitment discount* allocated to eligible *resources* or *services* consumed during the *charge period*.
  * When CommitmentDiscountStatus is "Unused", EffectiveCost MUST represent the portion of the amortized *commitment discount* that was not allocated to any *resources* or *services* during the *charge period*.

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
