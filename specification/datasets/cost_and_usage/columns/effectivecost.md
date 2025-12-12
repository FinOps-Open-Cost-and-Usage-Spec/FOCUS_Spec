# Effective Cost

Effective Cost represents the cost of a [*charge*](#glossary:charge) recognized in the specified [*charge period*](#glossary:charge-period), based on accrual-based accounting principles. Unlike [Billed Cost](#billedcost), which reflects invoiced amounts in a [*billing period*](#glossary:billing-period), Effective Cost reflects the value of usage or entitlements consumed during a *charge period*, regardless of when (or whether) those costs were invoiced. Effective Cost is inclusive of all applicable pricing adjustments, such as reduced unit prices resulting from [*negotiated*](#glossary:negotiated-discount) or [*commitment discounts*](#glossary:commitment-discount). This cost is denominated in the [Billing Currency](#billingcurrency). Effective Cost is commonly used to support FinOps capabilities, such as accrual-based reporting, cost forecasting, chargebacks, and usage-driven cost allocation.

This column resolves two challenges that are faced by practitioners:

1. Practitioners need to *amortize* relevant purchases, such as upfront fees, throughout the *commitment* and distribute them to the appropriate reporting groups (e.g., [*tags*](#glossary:tag), [*resources*](#glossary:resource)).
2. Many [*commitment discount*](#glossary:commitment-discount) constructs include a recurring expense for the *commitment* for every [*billing period*](#glossary:billing-period) and must distribute this cost to the *resources* using the *commitment*. This forces reconciliation between the initial *commitment* [*row*](#glossary:row) per period and the actual usage *rows*.

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

### Concerning Granularity and Distribution of Recurring Fee

Service providers should distribute the *commitment* purchase amount instead of including a *row* at the beginning of a period so practitioners do not need to manually distribute the fee themselves.

### Concerning Amortization Approaches

Eligible purchases should be *amortized* using a methodology determined by the service provider that reflects the needs of their customer base and is proportional to the Pricing Quantity and the time granularity of the *row*. Should a practitioner desire to *amortize* relevant purchases using a different approach, the practitioner can do so using the [Billed Cost](#billedcost) for the line item representing the initial purchase.

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
