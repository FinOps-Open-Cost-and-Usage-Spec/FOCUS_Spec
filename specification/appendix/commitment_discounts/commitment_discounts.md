# Commitment Discount Examples - Overview

This page summarizes the FOCUS commitment discount example scenarios. Each scenario demonstrates a specific combination of cloud provider, commitment type, payment model, or utilization pattern.

## Provider-Specific Scenarios

These are full 41-column FOCUS datasets showing realistic billing data with a 24-hour EC2/VM/Compute Engine workload plus ancillary services (storage, database, serverless).

### AWS

| Scenario                            | File                                                                                            | What You'll Learn                                                                                                                                                                                     |
| ----------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Reserved Instance - All Upfront     | [aws_reserved_instance_all_upfront_100pct](aws_reserved_instance_all_upfront_100pct.md)         | How a single large upfront purchase amortizes across usage rows. BilledCost=$0 on usage rows; EffectiveCost carries the amortized value. Usage-based commitment (`CommitmentDiscountCategory=Usage`). |
| Reserved Instance - Partial Upfront | [aws_reserved_instance_partial_upfront_100pct](aws_reserved_instance_partial_upfront_100pct.md) | How partial upfront splits into two purchase rows: one `One-Time` and one `Recurring`. Demonstrates the hybrid payment model for RIs.                                                                 |
| Savings Plan - All Upfront          | [aws_savings_plan_all_upfront_100pct](aws_savings_plan_all_upfront_100pct.md)                   | How Savings Plans differ from RIs: `CommitmentDiscountCategory=Spend` (dollar-based) instead of `Usage` (instance-based). Quantities measured in USD, not instance hours.                             |
| Savings Plan - Partial Upfront      | [aws_savings_plan_partial_upfront_100pct](aws_savings_plan_partial_upfront_100pct.md)           | The partial upfront pattern applied to Savings Plans. Two purchase rows (one-time + recurring) mirror the RI partial model but with spend-based commitment fields.                                    |
| Savings Plan - No Upfront           | [aws_savings_plan_no_upfront_100pct](aws_savings_plan_no_upfront_100pct.md)                     | The no-upfront model: only a `Recurring` purchase row, no initial capital outlay. Compare the higher effective rate against all-upfront and partial-upfront variants.                                 |
| Savings Plan - 150% Utilization     | [aws_savings_plan_all_upfront_150pct](aws_savings_plan_all_upfront_150pct.md)                   | What happens when demand exceeds commitment capacity. The first 24 hours apply the effective unit price; 12 additional hours spill over to on-demand at full list price (`PricingCategory=Standard`).       |
| Savings Plan - 75% Utilization      | [aws_savings_plan_all_upfront_75pct](aws_savings_plan_all_upfront_75pct.md)                     | Moderate underutilization: 18 hours `Used`, 6 hours `Unused`. Unused rows carry EffectiveCost with null resource fields, representing wasted spend.                                                   |
| Savings Plan - 50% Utilization      | [aws_savings_plan_all_upfront_50pct](aws_savings_plan_all_upfront_50pct.md)                     | Significant underutilization: 12 hours `Used`, 12 hours `Unused`. Half the commitment value is wasted - key pattern for identifying commitment right-sizing opportunities.                            |
| Savings Plan - 0% Utilization       | [aws_savings_plan_all_upfront_0pct](aws_savings_plan_all_upfront_0pct.md)                       | Worst case: commitment purchased but never applied. All 24 hours show `Unused` status. EffectiveCost accrues entirely as waste.                                                                       |

### Azure

| Scenario                   | File                                                                              | What You'll Learn                                                                                                                                                                              |
| -------------------------- | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Reservation - All Upfront  | [azure_reservation_all_upfront_100pct](azure_reservation_all_upfront_100pct.md)   | Azure's usage-based reservation model in FOCUS format. ARM-style resource IDs, `CommitmentDiscountType=Azure Reservation`. Compare structure and rates against AWS RIs.                        |
| Reservation - No Upfront   | [azure_reservation_no_upfront_100pct](azure_reservation_no_upfront_100pct.md)     | Azure no-upfront reservations with monthly recurring payments only. Note the higher effective rate vs all-upfront, reflecting the deferred-payment premium.                                    |
| Savings Plan - All Upfront | [azure_savings_plan_all_upfront_100pct](azure_savings_plan_all_upfront_100pct.md) | Azure's spend-based Savings Plan (`CommitmentDiscountCategory=Spend`). Uses `Microsoft.BillingBenefits/savingsPlans` resource paths. Compare against Azure Reservations and AWS Savings Plans. |

### GCP

| Scenario                   | File                                                                          | What You'll Learn                                                                                                                                               |
| -------------------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Resource CUD - All Upfront | [gcp_resource_cud_all_upfront_100pct](gcp_resource_cud_all_upfront_100pct.md) | GCP's usage-based commitment: `CommitmentDiscountCategory=Usage`, quantities in `vCPU Hours`. GCP's equivalent of AWS RIs. Deepest discount of all GCP options. |
| Flex CUD - All Upfront     | [gcp_flex_cud_all_upfront_100pct](gcp_flex_cud_all_upfront_100pct.md)         | GCP's spend-based commitment: `CommitmentDiscountCategory=Spend`, quantities in `USD`. Uses `//compute.googleapis.com/` resource ID format.                     |
| Flex CUD - Partial Upfront | [gcp_flex_cud_partial_upfront_100pct](gcp_flex_cud_partial_upfront_100pct.md) | Partial upfront payment model applied to GCP CUDs. One-time + recurring purchase rows, same pattern as AWS and Azure partial upfront models.                    |

## Generic Reference Scenarios

Minimal examples using placeholder IDs that isolate the core FOCUS patterns without provider-specific details. Ideal for learning the fundamental row structures.

### Purchase Patterns

| Scenario                 | File                                                                                  | What You'll Learn                                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| All Upfront Purchase     | [commitment_discount_purchase_scenario_1](commitment_discount_purchase_scenario_1.md) | Single `Purchase/One-Time` row. Full cost in BilledCost, EffectiveCost=$0 (amortized to usage rows). ChargePeriod spans the full commitment term. |
| No Upfront Purchase      | [commitment_discount_purchase_scenario_2](commitment_discount_purchase_scenario_2.md) | Multiple `Purchase/Recurring` rows within a billing period. No one-time payment - all cost flows through periodic charges.                        |
| Partial Upfront Purchase | [commitment_discount_purchase_scenario_3](commitment_discount_purchase_scenario_3.md) | Hybrid model: one `One-Time` row plus multiple `Recurring` rows. Shows how cost splits between immediate capital and ongoing operational expense. |

### Usage Patterns

| Scenario           | File                                                                            | What You'll Learn                                                                                                                                                           |
| ------------------ | ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fully Utilized     | [commitment_discount_usage_scenario_1](commitment_discount_usage_scenario_1.md) | Single `Used` row: BilledCost=$0, EffectiveCost reflects amortized commitment value. The simplest happy-path usage pattern.                                                 |
| Fully Unused       | [commitment_discount_usage_scenario_2](commitment_discount_usage_scenario_2.md) | Single `Unused` row: ResourceId points to the commitment itself (not a resource), ConsumedQuantity is null. EffectiveCost still accrues - pure waste.                       |
| Partially Utilized | [commitment_discount_usage_scenario_3](commitment_discount_usage_scenario_3.md) | Two rows for one hour: a `Used` portion and an `Unused` portion. CommitmentDiscountQuantity values sum to the full hourly commitment. The most nuanced utilization pattern. |
