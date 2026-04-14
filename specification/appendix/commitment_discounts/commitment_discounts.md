# Examples: Commitment Discounts

This appendix section defines the concept of a [*commitment discount*](#glossary:commitment-discount). It then lays out a series of FOCUS dataset examples.

## Overview

A [*commitment discount*](#glossary:commitment-discount) is a billing discount model that offers reduced rates on preselected [*SKUs*](#glossary:sku) in exchange for an obligated usage or spend amount over a specified [*period*](#glossary:period). *Commitment discounts* typically consist of purchase and usage records within cost and usage datasets.

Usage-based *commitment discounts* obligate a customer to a predetermined amount of usage over a specified [*period*](#glossary:period). In some cases, usage-based *commitment discounts* also feature [*commitment discount flexibility*](#glossary:commitment-discount-flexibility) which may expand the types of [*resources*](#glossary:resource) that a *commitment discount* can cover. It is important to note when mixing *commitment discounts* with and without *commitment discount flexibility*, the [CommitmentDiscountUnit](#datasets.costandusage.commitmentdiscountunit) should reflect this difference.

Spend-based *commitment discounts* obligate a customer to a predetermined amount of spend over a specified [*period*](#glossary:period). In the usage examples below, each [*row*](#glossary:row) measures the monetary amount of the hourly commit consumed by the *commitment discount*, so the CommitmentDiscountUnit chosen is "USD", or the [*billing currency*](#glossary:billing-currency).

### Purchasing

While customers are bound to the [*period*](#glossary:period) of a *commitment discount*, service providers offer some or all of the following payment options before and/or during the *period*:

* *All Upfront* - The *commitment discount* is paid in full before the *period* begins.
* *No Upfront* - The *commitment discount* is paid on a repeated basis, typically over each [*billing period*](#glossary:billing-period) of the *period*.
* *Partial Upfront* - Some of the *commitment discount* is paid before the *period* begins, and the rest is paid repeatedly over the *period*.

For example, if a customer buys a 1-year, spend-based *commitment discount* with a $1.00 hourly commit and pays with the partial option, the *commitment discount's* payment consists of a one-time purchase in the beginning of the *period* *and* monthly recurring purchases. The one-time payment covers half of the annual commitment (AWS Savings Plans are half, Reserved Instances are a portion of the cost), while the recurring payment covers the remaining half and is calculated based on the exact number of hours in each [*billing period*](#glossary:billing-period):

1. *One-Time* - $4,380 (24 hours &times; 365 days &times; $1.00 &times; 0.5)
2. *Recurring* - $336.00 for February (672 hours in the month &times; $1.00 &times; 0.5)

### Usage

Commitment discounts follow a "use-it-or-lose-it" model where the [*amortization*](#glossary:amortization) of a *commitment discount's* purchase applies evenly to eligible *resources* over each [*charge period*](#glossary:charge-period) of the *period*.

For example, if a customer buys a spend-based *commitment discount* with a $1.00 hourly commit in January (31 days), only $1.00 is eligible for consumption for each hourly *charge period*. If a customer has eligible *resources* running during this *charge period*, an amount of up to $1.00 will be allocated to these *resources*. Conversely, if a customer does not have eligible *resources* running that fully take advantage of this $1.00 during this *charge period*, then some or all of this amount will go to waste.

## Data Generator Scenarios

Below are tables listing some common commitment discount scenarios for a few prominent FOCUS data generators.

### Data Generator Scenarios: Amazon Web Services (AWS)

| Scenario                                                                                                                                  | What You'll Learn                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Reserved Instance - All Upfront](#appendix.commitmentdiscountexamples.awsreservedinstance-allupfront-100%utilization)                    | How a single large upfront purchase amortizes across usage rows. BilledCost=0 on usage rows; EffectiveCost carries the amortized value. Usage-based commitment (`CommitmentDiscountCategory=Usage`).  |
| [Reserved Instance - Partial Upfront](#appendix.commitmentdiscountexamples.awsreservedinstance-partialupfront-100%utilization)            | How partial upfront splits into two purchase rows: one `One-Time` and one `Recurring`. Demonstrates the hybrid payment model for RIs.                                                                 |
| [Savings Plan - All Upfront](#appendix.commitmentdiscountexamples.awssavingsplan-allupfront-100%utilization)                              | How Savings Plans differ from RIs: `CommitmentDiscountCategory=Spend` (dollar-based) instead of `Usage` (instance-based). Quantities measured in USD, not instance hours.                             |
| [Savings Plan - Partial Upfront](#appendix.commitmentdiscountexamples.awssavingsplan-partialupfront-100%utilization)                      | The partial upfront pattern applied to Savings Plans. Two purchase rows (one-time + recurring) mirror the RI partial model but with spend-based commitment fields.                                    |
| [Savings Plan - No Upfront](#appendix.commitmentdiscountexamples.awssavingsplan-noupfront-100%utilization)                                | The no-upfront model: only a `Recurring` purchase row, no initial capital outlay. Compare the higher effective rate against all-upfront and partial-upfront variants.                                 |
| [Savings Plan - 100% Utilization with Overage](#appendix.commitmentdiscountexamples.awssavingsplan-allupfront-100%utilizationwithoverage) | What happens when demand exceeds commitment capacity. Committed hours apply the effective unit price; overage hours spill to standard pricing at full list price (`PricingCategory=Standard`).        |
| [Savings Plan - 75% Utilization](#appendix.commitmentdiscountexamples.awssavingsplan-allupfront-75%utilization)                           | Moderate underutilization: 18 hours `Used`, 6 hours `Unused`. Unused rows carry EffectiveCost with null resource fields, representing wasted spend.                                                   |
| [Savings Plan - 50% Utilization](#appendix.commitmentdiscountexamples.awssavingsplan-allupfront-50%utilization)                           | Significant underutilization: 12 hours `Used`, 12 hours `Unused`. Half the commitment value is wasted - key pattern for identifying commitment right-sizing opportunities.                            |
| [Savings Plan - 0% Utilization](#appendix.commitmentdiscountexamples.awssavingsplan-allupfront-0%utilization)                             | Worst case: commitment purchased but never applied. All 24 hours show `Unused` status. EffectiveCost accrues entirely as waste.                                                                       |

### Data Generator Scenarios: Microsoft Azure

| Scenario                                                                                                       | What You'll Learn                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Reservation - All Upfront](#appendix.commitmentdiscountexamples.azurereservation-allupfront-100%utilization)  | Azure's usage-based reservation model in FOCUS format. ARM-style resource IDs, `CommitmentDiscountType=Azure Reservation`. Compare structure and rates against AWS RIs.                        |
| [Reservation - No Upfront](#appendix.commitmentdiscountexamples.azurereservation-noupfront-100%utilization)    | Azure no-upfront reservations with monthly recurring payments only. Note the higher effective rate vs all-upfront, reflecting the deferred-payment premium.                                    |
| [Savings Plan - All Upfront](#appendix.commitmentdiscountexamples.azuresavingsplan-allupfront-100%utilization) | Azure's spend-based Savings Plan (`CommitmentDiscountCategory=Spend`). Uses `Microsoft.BillingBenefits/savingsPlans` resource paths. Compare against Azure Reservations and AWS Savings Plans. |

### Data Generator Scenarios: Google Cloud Platform (GCP)

| Scenario                                                                                                     | What You'll Learn                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Resource CUD - No Upfront](#appendix.commitmentdiscountexamples.gcpresourcecud-noupfront-100%utilization)   | GCP's usage-based commitment: `CommitmentDiscountCategory=Usage`, quantities in `Hours`. Monthly billing only (GCP CUDs have no upfront option). Deepest discount.   |
| [Flex CUD - No Upfront](#appendix.commitmentdiscountexamples.gcpflexcud-noupfront-100%utilization)           | GCP's spend-based commitment: `CommitmentDiscountCategory=Spend`, quantities in `USD`. Monthly recurring billing, no upfront payment. Compare against AWS and Azure. |
