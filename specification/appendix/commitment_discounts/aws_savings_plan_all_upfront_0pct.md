# AWS Savings Plan - All Upfront - 0% Utilization

| Parameter                    | Value                |
| ---------------------------- | -------------------- |
| Scenario Type                | commitment           |
| Payment Model                | All Upfront          |
| Commitment Discount Category | Spend                |
| Utilization                  | 0%                   |
| Hours Generated              | 24                   |
| Annual Commitment            | &dollar;353,000.00   |
| List Unit Price              | &dollar;60.45/hour   |
| Savings                      | 0%                   |

[CSV Example](/specification/data/commitment_discount_scenarios/aws_savings_plan_all_upfront_0pct.csv)

## Scenario Description

This example shows an **Amazon Web Services EC2 Instance Savings Plan**, which is a commitment (CommitmentDiscountCategory: Spend) where you commit to a specific dollar amount of usage per hour.

The **All Upfront** payment option means the entire commitment cost is paid at purchase time. This results in a single Purchase row with the full BilledCost and zero EffectiveCost (since the cost is amortized to usage rows).

This scenario demonstrates **zero utilization** where the commitment is purchased but no resources are consumed. All usage rows have CommitmentDiscountStatus='Unused', representing wasted commitment capacity. The EffectiveCost on these rows reflects the cost of unused commitment that cannot be recovered.

## Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type           | Count   | BilledCost               | EffectiveCost         |
| ------------------ | ------- | ------------------------ | --------------------- |
| Purchase           | 1       | &dollar;353,000.00       | &dollar;0.00          |
| Usage (Unused)     | 24      | &dollar;0.00             | &dollar;967.20        |
| **Total**          | 25      | **&dollar;353,000.00**   | **&dollar;967.20**    |

## Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

### Quantity Columns: PricingQuantity vs ConsumedQuantity vs CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column                           | Purpose                                 | When Populated                  | Typical Value          |
| -------------------------------- | --------------------------------------- | ------------------------------- | ---------------------- |
| **PricingQuantity**              | Quantity used for pricing calculation   | All priced rows                 | 1 (per hour/unit)      |
| **ConsumedQuantity**             | Actual resource consumption             | Usage rows with resources       | 1 (hours consumed)     |
| **CommitmentDiscountQuantity**   | Commitment capacity applied             | Rows with commitment discount   | 1 (commitment units)   |

**For spend-based commitments:** CommitmentDiscountQuantity represents the dollar amount applied, not a count of resources. For this commitment, the value equals the hourly dollar commitment.

### Pricing Columns: ListUnitPrice vs ContractedUnitPrice

| Column                    | Purpose                    | Commitment-Covered        |
| ------------------------- | -------------------------- | ------------------------- |
| **ListUnitPrice**         | List (public) unit price   | &dollar;60.45             |
| **ContractedUnitPrice**   | Negotiated unit price      | &dollar;60.45             |

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., EDP rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario           | BilledCost         | EffectiveCost   | ListCost           |
| ------------------ | ------------------ | --------------- | ------------------ |
| **Purchase Row**   | &dollar;353,000.00 | &dollar;0.00    | &dollar;353,000.00 |
| **Unused Row**     | &dollar;0.00       | &dollar;40.30   | &dollar;60.45           |

This scenario has no Used or Standard rows because utilization is 0% — no resources were consumed.

The following critical rules apply to commitment discount data:

* **Purchase rows:** `EffectiveCost` MUST be 0. The cost is distributed to usage rows.
* **Unused rows:** `BilledCost` = 0 but `EffectiveCost` > 0 to represent wasted commitment value.

## Purchase Row Details

| Column                     | Value                | Explanation                                       |
| -------------------------- | -------------------- | ------------------------------------------------- |
| ChargeCategory             | Purchase             | Commitment purchase transaction                   |
| ChargeFrequency            | One-Time             | One-time upfront payment                          |
| BilledCost                 | &dollar;353,000.00   | Full annual commitment payment                    |
| EffectiveCost              | &dollar;0.00         | **MUST be 0** - cost is amortized to usage rows   |
| PricingQuantity            | 1                    | One commitment unit purchased                     |
| CommitmentDiscountStatus   | null                 | Status only applies to usage rows                 |

## Unused Commitment Row Details

| Column                       | Value           | Explanation                                        |
| ---------------------------- | --------------- | -------------------------------------------------- |
| ChargeCategory               | Usage           | Represents commitment capacity                     |
| BilledCost                   | &dollar;0.00    | No additional billing (already paid at purchase)   |
| EffectiveCost                | &dollar;40.30   | **Wasted value** - lost commitment                 |
| PricingQuantity              | 1               | Commitment units unused                            |
| ConsumedQuantity             | null            | **No resource consumed**                           |
| CommitmentDiscountQuantity   | 40.30           | Commitment wasted                                  |
| CommitmentDiscountStatus     | Unused          | Commitment not utilized                            |
| ResourceId                   | null            | No resource associated                             |

ListCost on unused rows represents the list-price value of the unused commitment capacity (ListUnitPrice × PricingQuantity).
