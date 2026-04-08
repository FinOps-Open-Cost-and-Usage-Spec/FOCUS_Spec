# AWS Savings Plan - All Upfront - 0% Utilization

| Parameter                    | Value                |
| ---------------------------- | -------------------- |
| Scenario Type                | commitment           |
| Payment Model                | All Upfront          |
| Commitment Discount Category | Spend                |
| Utilization                  | 0%                   |
| Hours Generated              | 24                   |
| Annual Commitment            | &dollar;353,028.00   |
| List Unit Price              | &dollar;60.45/hour   |

[CSV Example](/specification/data/commitment_discount_scenarios/aws_savings_plan_all_upfront_0pct.csv)

## Scenario Description

This example shows an **Amazon Web Services EC2 Instance Savings Plan**, which is a commitment (with a Commitment Discount Category of `Spend`) where you commit to a specific dollar amount of usage per hour.

The **All Upfront** payment option means the entire commitment cost is paid at purchase time. This results in a single Purchase row with the full BilledCost and zero EffectiveCost (since the cost is amortized to usage rows).

This scenario demonstrates **zero utilization** where the commitment is purchased but no resources are consumed. All usage rows have CommitmentDiscountStatus='Unused', representing wasted commitment capacity. The EffectiveCost on these rows reflects the cost of unused commitment that cannot be recovered.

## Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type           | Count   | BilledCost               | EffectiveCost         |
| ------------------ | ------- | ------------------------ | --------------------- |
| Purchase           | 1       | &dollar;353,028.00       | &dollar;0.00          |
| Usage (Unused)     | 24      | &dollar;0.00             | &dollar;967.20        |
| **Total**          | 25      | **&dollar;353,028.00**   | **&dollar;967.20**    |

## Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

### Quantity Columns: PricingQuantity vs ConsumedQuantity vs CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column                           | Purpose                                 | When Populated                  | Typical Value              |
| -------------------------------- | --------------------------------------- | ------------------------------- | -------------------------- |
| **PricingQuantity**              | Quantity used for pricing calculation   | All priced rows                 | 40.30 (USD, hourly rate)   |
| **ConsumedQuantity**             | Actual resource consumption             | Usage rows with resources       | 1 (hours consumed)         |
| **CommitmentDiscountQuantity**   | Commitment capacity applied             | Rows with commitment discount   | 40.30 (USD)                |

**For spend-based commitments:** CommitmentDiscountQuantity represents the dollar amount applied, not a count of resources. For this commitment, the value equals the hourly dollar commitment.

### Pricing Columns: ListUnitPrice vs ContractedUnitPrice

| Column                    | Purpose                    | Commitment-Covered        |
| ------------------------- | -------------------------- | ------------------------- |
| **ListUnitPrice**         | List (public) unit price   | &dollar;1.00              |
| **ContractedUnitPrice**   | Negotiated unit price      | &dollar;1.00              |

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., EDP rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices. For spend-based purchase and unused rows, PricingUnit is USD and ListUnitPrice is &dollar;1.00, because you are fundamentally purchasing a block of dollars.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario           | BilledCost         | EffectiveCost   | ListCost           |
| ------------------ | ------------------ | --------------- | ------------------ |
| **Purchase Row**   | &dollar;353,028.00 | &dollar;0.00    | &dollar;353,028.00 |
| **Unused Row**     | &dollar;0.00       | &dollar;40.30   | &dollar;40.30      |

This scenario has no Used or Standard rows because utilization is 0% and no resources were consumed.

The following critical rules apply to commitment discount data:

* **Purchase rows:** `EffectiveCost` must be 0. The cost is distributed to usage rows.
* **Unused rows:** `BilledCost` = 0 but `EffectiveCost` > 0 to represent wasted commitment value.

## Purchase Row Details

| Column                     | Value                                | Explanation                                                 |
| -------------------------- | ------------------------------------ | ----------------------------------------------------------- |
| ChargeCategory             | Purchase                             | Commitment purchase transaction                             |
| ChargeFrequency            | One-Time                             | One-time upfront payment                                    |
| BilledCost                 | &dollar;353,028.00                   | Full annual commitment payment                              |
| EffectiveCost              | &dollar;0.00                         | **must be 0** - cost is amortized to usage rows             |
| PricingQuantity            | 353,028.00                           | Total commitment in USD (PricingUnit = USD)                 |
| CommitmentDiscountStatus   | null                                 | Status only applies to usage rows                           |
| CommitmentDiscountQuantity | 353,028.00                           | Full annual commitment (&dollar;40.30/hr &times; 8,760 hrs) |
| CommitmentDiscountUnit     | USD                                  | Unit of commitment capacity (spend-based)                   |
| SkuId                      | AWS-USEAST1-COMPUTE-PURCHASE         | Commitment purchase SKU                                     |
| SkuPriceId                 | AWS-USEAST1-COMPUTE-PURCHASE-UPFRONT | Price point for upfront purchase                            |

## Unused Commitment Row Details

| Column                       | Value                                                          | Explanation                                        |
| ---------------------------- | -------------------------------------------------------------- | -------------------------------------------------- |
| ChargeCategory               | Usage                                                          | Represents commitment capacity                     |
| BilledCost                   | &dollar;0.00                                                   | No additional billing (already paid at purchase)   |
| EffectiveCost                | &dollar;40.30                                                  | **Wasted value** - lost commitment                 |
| PricingQuantity              | 40.30                                                          | Hourly commitment in USD (PricingUnit = USD)       |
| ListCost                     | &dollar;40.30                                                  | &dollar;1.00 &times; 40.30 USD                     |
| ConsumedQuantity             | null                                                           | **No resource consumed**                           |
| CommitmentDiscountQuantity   | 40.30                                                          | Commitment wasted                                  |
| CommitmentDiscountStatus     | Unused                                                         | Commitment not utilized                            |
| ResourceId                   | arn:aws:savingsplans::123456789012:savingsplan/sp-abc123def456 | must match CommitmentDiscountId (no resource used) |
| ResourceName                 | EC2 Instance Savings Plan                                      | Carried from Purchase row (no resource consumed)   |
| ResourceType                 | Commitment                                                     | Carried from Purchase row (no resource consumed)   |
| SkuId                        | AWS-USEAST1-COMPUTE-PURCHASE                                   | must match Purchase row (no resource consumed)     |
| SkuPriceId                   | AWS-USEAST1-COMPUTE-PURCHASE-UPFRONT                           | must match Purchase row (no resource consumed)     |

For spend-based unused rows, PricingUnit is USD and PricingQuantity is the hourly commitment amount. ListCost = ListUnitPrice (&dollar;1.00) &times; PricingQuantity, which equals the wasted commitment dollars per hour.
