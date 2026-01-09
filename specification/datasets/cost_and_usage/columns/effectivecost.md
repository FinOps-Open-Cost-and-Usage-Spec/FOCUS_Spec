# Effective Cost

Effective Cost represents the cost of a [*charge*](#glossary:charge) recognized in the specified [*charge period*](#glossary:charge-period), based on [*accrual-based accounting*](#glossary:accrual-based-accounting) principles. Unlike [Billed Cost](#billedcost), which reflects invoiced amounts in a [*billing period*](#glossary:billing-period), Effective Cost reflects the value of usage or [*entitlements*](#glossary:entitlement) consumed during a *charge period*, regardless of when (or whether) those costs were invoiced. Effective Cost is inclusive of all applicable pricing adjustments, such as reduced unit prices resulting from [*negotiated*](#glossary:negotiated-discount) or [*commitment discounts*](#glossary:commitment-discount). This cost is denominated in the [Billing Currency](#billingcurrency). Effective Cost is commonly used to support FinOps capabilities, such as accrual-based reporting, cost forecasting, chargebacks, and usage-driven cost allocation.

## Requirements

EffectiveCost adheres to the following requirements:

* EffectiveCost MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).
* EffectiveCost MUST be of type Decimal.
* EffectiveCost MUST conform to [NumericFormat](#numericformat) requirements.
* EffectiveCost MUST NOT be null.
* EffectiveCost MUST be a valid decimal value.
* EffectiveCost MUST be 0 when [ChargeCategory](#chargecategory) is "Purchase" and the purchase is intended to cover future eligible *charges*.
* EffectiveCost MUST be denominated in the BillingCurrency.
* The sum of EffectiveCost in a given *billing period* MAY differ from the sum of the invoices received for the same *billing period* for a [*billing account*](#glossary:billing-account).
* When ChargeCategory is not "Usage" or "Purchase", EffectiveCost adheres to the following additional requirements:
  * EffectiveCost of a *charge* calculated based on other *charges* (e.g., when the ChargeCategory is "Tax") MUST be calculated based on the EffectiveCost of those related *charges*.
  * EffectiveCost of a *charge* unrelated to other *charges* (e.g., when the ChargeCategory is "Credit") MUST match the [BilledCost](#billedcost).
* *Charges* for a given [CommitmentDiscountId](#commitmentdiscountid) adhere to the following additional requirements:
  * The sum of EffectiveCost where ChargeCategory is "Usage" MUST equal the sum of BilledCost where ChargeCategory is "Purchase".
  * The sum of EffectiveCost where ChargeCategory is "Usage" MUST equal the sum of EffectiveCost where ChargeCategory is "Usage" and [CommitmentDiscountStatus](#commitmentdiscountstatus) is "Used", plus the sum of EffectiveCost where ChargeCategory is "Usage" and CommitmentDiscountStatus is "Unused".

## Column ID

EffectiveCost

## Display Name

Effective Cost

## Description

Cost of a *charge* recognized in the specified *charge period*, based on accrual-based accounting principles.

## Content constraints

|    Constraint   |      Value              |
|:----------------|:------------------------|
| Column type     | Metric                  |
| Feature level   | Mandatory               |
| Allows nulls    | False                   |
| Data type       | Decimal                 |
| Value format    | [Numeric Format](#numericformat) |
| Number range    | Any valid decimal value |

## Introduced (version)

0.5
