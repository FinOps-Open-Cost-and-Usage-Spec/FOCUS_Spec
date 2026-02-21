# Commitment Discount Examples

Each scenario provides a complete FOCUS-conformant dataset illustrating how commitment discount purchases, usage, and amortization appear as line items. Scenarios cover different commitment types (Reserved Instances, Savings Plans, CUDs), payment models (all-upfront, partial-upfront, no-upfront), and utilization levels (0% through 150%).

The following sections detail each scenario:

### AWS

| Scenario                            | What You'll Learn                                                                                                                                                                                     |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Reserved Instance - All Upfront](#appendix.commitmentdiscountexamples.awsreservedinstance-allupfront-100%utilization)     | How a single large upfront purchase amortizes across usage rows. BilledCost=$0 on usage rows; EffectiveCost carries the amortized value. Usage-based commitment (`CommitmentDiscountCategory=Usage`). |
| [Reserved Instance - Partial Upfront](#appendix.commitmentdiscountexamples.awsreservedinstance-partialupfront-100%utilization) | How partial upfront splits into two purchase rows: one `One-Time` and one `Recurring`. Demonstrates the hybrid payment model for RIs.                                                                 |
| [Savings Plan - All Upfront](#appendix.commitmentdiscountexamples.awssavingsplan-allupfront-100%utilization)          | How Savings Plans differ from RIs: `CommitmentDiscountCategory=Spend` (dollar-based) instead of `Usage` (instance-based). Quantities measured in USD, not instance hours.                             |
| [Savings Plan - Partial Upfront](#appendix.commitmentdiscountexamples.awssavingsplan-partialupfront-100%utilization)      | The partial upfront pattern applied to Savings Plans. Two purchase rows (one-time + recurring) mirror the RI partial model but with spend-based commitment fields.                                    |
| [Savings Plan - No Upfront](#appendix.commitmentdiscountexamples.awssavingsplan-noupfront-100%utilization)           | The no-upfront model: only a `Recurring` purchase row, no initial capital outlay. Compare the higher effective rate against all-upfront and partial-upfront variants.                                 |
| [Savings Plan - 150% Utilization](#appendix.commitmentdiscountexamples.awssavingsplan-allupfront-150%utilization)     | What happens when demand exceeds commitment capacity. The first 24 hours apply the effective unit price; 12 additional hours spill over to standard pricing at full list price (`PricingCategory=Standard`). |
| [Savings Plan - 75% Utilization](#appendix.commitmentdiscountexamples.awssavingsplan-allupfront-75%utilization)      | Moderate underutilization: 18 hours `Used`, 6 hours `Unused`. Unused rows carry EffectiveCost with null resource fields, representing wasted spend.                                                   |
| [Savings Plan - 50% Utilization](#appendix.commitmentdiscountexamples.awssavingsplan-allupfront-50%utilization)      | Significant underutilization: 12 hours `Used`, 12 hours `Unused`. Half the commitment value is wasted - key pattern for identifying commitment right-sizing opportunities.                            |
| [Savings Plan - 0% Utilization](#appendix.commitmentdiscountexamples.awssavingsplan-allupfront-0%utilization)       | Worst case: commitment purchased but never applied. All 24 hours show `Unused` status. EffectiveCost accrues entirely as waste.                                                                       |

### Azure

| Scenario                   | What You'll Learn                                                                                                                                                                              |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Reservation - All Upfront](#appendix.commitmentdiscountexamples.azurereservation-allupfront-100%utilization)  | Azure's usage-based reservation model in FOCUS format. ARM-style resource IDs, `CommitmentDiscountType=Azure Reservation`. Compare structure and rates against AWS RIs.                        |
| [Reservation - No Upfront](#appendix.commitmentdiscountexamples.azurereservation-noupfront-100%utilization)   | Azure no-upfront reservations with monthly recurring payments only. Note the higher effective rate vs all-upfront, reflecting the deferred-payment premium.                                    |
| [Savings Plan - All Upfront](#appendix.commitmentdiscountexamples.azuresavingsplan-allupfront-100%utilization) | Azure's spend-based Savings Plan (`CommitmentDiscountCategory=Spend`). Uses `Microsoft.BillingBenefits/savingsPlans` resource paths. Compare against Azure Reservations and AWS Savings Plans. |

### GCP

| Scenario                   | What You'll Learn                                                                                                                                               |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Resource CUD - All Upfront](#appendix.commitmentdiscountexamples.gcpresourcecud-allupfront-100%utilization) | GCP's usage-based commitment: `CommitmentDiscountCategory=Usage`, quantities in `vCPU Hours`. GCP's equivalent of AWS RIs. Deepest discount of all GCP options. |
| [Flex CUD - All Upfront](#appendix.commitmentdiscountexamples.gcpflexcud-allupfront-100%utilization)     | GCP's spend-based commitment: `CommitmentDiscountCategory=Spend`, quantities in `USD`. Uses `//compute.googleapis.com/` resource ID format.                     |
| [Flex CUD - Partial Upfront](#appendix.commitmentdiscountexamples.gcpflexcud-partialupfront-100%utilization) | Partial upfront payment model applied to GCP CUDs. One-time + recurring purchase rows, same pattern as AWS and Azure partial upfront models.                    |
