# Examples: Commitment Discounts

This appendix section defines the concept of a [_commitment discount_](#glossary:commitment-discount). It then lays out a series of real-world examples based on actual FOCUS data generators.

## Overview

A [_commitment discount_](#glossary:commitment-discount) is a billing discount model that offers reduced rates on preselected [_SKUs_](#glossary:sku) in exchange for an obligated usage or spend amount over a specified [_period_](#glossary:period). _Commitment discounts_ typically consist of purchase and usage records within cost and usage datasets.

Usage-based _commitment discounts_ obligate a customer to a predetermined amount of usage over a specified [_period_](#glossary:period). In some cases, usage-based _commitment discounts_ also feature [_commitment discount flexibility_](#glossary:commitment-discount-flexibility) which may expand the types of [_resources_](#glossary:resource) that a _commitment discount_ can cover. It is important to note when mixing _commitment discounts_ with and without _commitment discount flexibility_, the [CommitmentDiscountUnit](#datasets.costandusage.commitmentdiscountunit) should reflect this difference.

Spend-based _commitment discounts_ obligate a customer to a predetermined amount of spend over a specified [_period_](#glossary:period). In the usage examples below, each [_row_](#glossary:row) measures the monetary amount of the hourly commit consumed by the _commitment discount_, so the CommitmentDiscountUnit chosen is "USD", or the [_billing currency_](#glossary:billing-currency).

### Purchasing

While customers are bound to the [_period_](#glossary:period) of a _commitment discount_, service providers offer some or all of the following payment options before and/or during the _period_:

* _All Upfront_ - The _commitment discount_ is paid in full before the _period_ begins.
* _No Upfront_ - The _commitment discount_ is paid on a repeated basis, typically over each [_billing period_](#glossary:billing-period) of the _period_.
* _Partial Upfront_ - Some of the _commitment discount_ is paid before the _period_ begins, and the rest is paid repeatedly over the _period_.

For example, if a customer buys a 1-year, spend-based _commitment discount_ with a &dollar;1.00 hourly commit and pays with the partial option, the _commitment discount's_ payment consists of a one-time purchase in the beginning of the _period_ _and_ monthly recurring purchases with the following totals:

1. _One-Time_ - &dollar;4,380 (24 hours &times; 365 days &times; &dollar;1.00 &times; 0.5)
2. _Recurring_ - &dollar;365 per month (24 hours &times; 365 days &times; &dollar;1.00 &times; 0.5 &divide; 12 months)

### Usage

Commitment discounts follow a "use-it-or-lose-it" model where the [_amortization_](#glossary:amortization) of a _commitment discount's_ purchase applies evenly to eligible _resources_ over each [_charge period_](#glossary:charge-period) of the _period_.

For example, if a customer buys a spend-based _commitment discount_ with a &dollar;1.00 hourly commit in January (31 days), only &dollar;1.00 is eligible for consumption for each hourly _charge period_. If a customer has eligible _resources_ running during this _charge period_, an amount of up to &dollar;1.00 will be allocated to these _resources_. Conversely, if a customer does not have eligible _resources_ running that fully take advantage of this &dollar;1.00 during this _charge period_, then some or all of this amount will go to waste.

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

| Scenario                                                                                                     | What You'll Learn                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Resource CUD - All Upfront](#appendix.commitmentdiscountexamples.gcpresourcecud-allupfront-100%utilization) | GCP's usage-based commitment: `CommitmentDiscountCategory=Usage`, quantities in `vCPU Hours`. GCP's equivalent of AWS RIs. Deepest discount of all GCP options. |
| [Flex CUD - All Upfront](#appendix.commitmentdiscountexamples.gcpflexcud-allupfront-100%utilization)         | GCP's spend-based commitment: `CommitmentDiscountCategory=Spend`, quantities in `USD`. Uses `//compute.googleapis.com/` resource ID format.                     |
| [Flex CUD - Partial Upfront](#appendix.commitmentdiscountexamples.gcpflexcud-partialupfront-100%utilization) | Partial upfront payment model applied to GCP CUDs. One-time + recurring purchase rows, same pattern as AWS and Azure partial upfront models.                    |
