# Effective Cost

Effective Cost represents the cost of a [*charge*](#glossary:charge) based on the actual [*resource*](#glossary:resource) or [*service*](#glossary:service) usage or applicable [*contract commitments*](#glossary:contract-commitment) during a given [*charge period*](#glossary:charge-period), regardless of when those costs are invoiced. It is inclusive of all applicable pricing adjustments, such as reduced pricing from [*negotiated*](#glossary:negotiated-discount) or [*commitment discounts*](#glossary:commitment-discount). This cost is denominated in the [Billing Currency](#datasets.costandusage.billingcurrency). Effective Cost is commonly used for FinOps activities such as reporting, cost forecasting, cost allocation, and chargeback based on actual usage and consumption.

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

Cost of a *charge* based on the actual *resource* or *service* usage or applicable *contract commitments* during a given *charge period*, regardless of when those costs are invoiced.

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
