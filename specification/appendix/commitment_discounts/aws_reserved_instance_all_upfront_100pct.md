# AWS Reserved Instance - All Upfront - 100% Utilization

| Parameter                    | Value              |
| ---------------------------- | ------------------ |
| Scenario Type                | commitment         |
| Payment Model                | All Upfront        |
| Commitment Discount Category | Usage              |
| Utilization                  | 100%               |
| Hours Generated              | 24                 |
| Annual Commitment            | &dollar;402,960.00 |
| List Unit Price              | &dollar;69.00/hour |

[CSV Example](/specification/data/commitment_discount_scenarios/aws_reserved_instance_all_upfront_100pct.csv)

## Scenario Description

This example shows an **Amazon Web Services EC2 Reserved Instance**, which is a commitment (with a Commitment Discount Category of `Usage`) where you commit to a specific quantity of resource capacity (e.g., instance hours).

The **All Upfront** payment option means the entire commitment cost is paid at purchase time. This results in a single Purchase row with the full BilledCost and zero EffectiveCost (since the cost is amortized to usage rows).

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

## Row Summary

*The following row summary reflects only the rows included in the 24-hour sample CSV.*

| Row Type         | Count | BilledCost             | EffectiveCost        |
| ---------------- | ----- | ---------------------- | -------------------- |
| Purchase         | 1     | &dollar;402,960.00     | &dollar;0.00         |
| Usage (Used)     | 24    | &dollar;0.00           | &dollar;1,104.00     |
| **Total**        | 25    | **&dollar;402,960.00** | **&dollar;1,104.00** |

## Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

### Quantity Columns: PricingQuantity vs ConsumedQuantity vs CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column                         | Purpose                               | When Populated                | Typical Value        |
| ------------------------------ | ------------------------------------- | ----------------------------- | -------------------- |
| **PricingQuantity**            | Quantity used for pricing calculation | All priced rows               | 1 (per hour/unit)    |
| **ConsumedQuantity**           | Actual resource consumption           | Usage rows with resources     | 1 (hours consumed)   |
| **CommitmentDiscountQuantity** | Commitment capacity applied           | Rows with commitment discount | 1 (commitment units) |

**For usage-based commitments:** CommitmentDiscountQuantity represents the quantity of resources (e.g., instance hours), not a dollar amount. For a 1-hour reservation, CommitmentDiscountQuantity = 1.

### Pricing Columns: ListUnitPrice vs ContractedUnitPrice

| Column                  | Purpose                  | Commitment-Covered |
| ----------------------- | ------------------------ | ------------------ |
| **ListUnitPrice**       | List (public) unit price | &dollar;69.00      |
| **ContractedUnitPrice** | Negotiated unit price    | &dollar;69.00      |

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., EDP rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario         | BilledCost         | EffectiveCost | ListCost           |
| ---------------- | ------------------ | ------------- | ------------------ |
| **Purchase Row** | &dollar;402,960.00 | &dollar;0.00  | &dollar;402,960.00 |
| **Used Row**     | &dollar;0.00       | &dollar;46.00 | &dollar;69.00      |

The following critical rules apply to commitment discount data:

* **Purchase rows:** `EffectiveCost` MUST be 0. The cost is distributed to usage rows.
* **Used rows:** `BilledCost` MUST be 0. Usage is covered by the commitment.

## Purchase Row Details

| Column                     | Value                                | Explanation                                                                           |
| -------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------- |
| ChargeCategory             | Purchase                             | Commitment purchase transaction                                                       |
| ChargeFrequency            | One-Time                             | One-time upfront payment                                                              |
| BilledCost                 | &dollar;402,960.00                   | Full annual commitment payment                                                        |
| EffectiveCost              | &dollar;0.00                         | **MUST be 0** - cost is amortized to usage rows                                       |
| PricingQuantity            | 1                                    | One commitment unit purchased                                                         |
| CommitmentDiscountStatus   | null                                 | Status only applies to usage rows                                                     |
| CommitmentDiscountQuantity | 8760.00                              | Total commitment capacity for the 1-year term (1 instance-hr/hr &times; 8,760 hrs/yr) |
| CommitmentDiscountUnit     | Hours                                | Unit of commitment capacity (usage-based)                                             |
| SkuId                      | AWS-USEAST1-COMPUTE-PURCHASE         | Commitment purchase SKU                                                               |
| SkuPriceId                 | AWS-USEAST1-COMPUTE-PURCHASE-UPFRONT | Price point for upfront purchase                                                      |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                                |
| -------------------------- | ----------------------------------------------------- | ------------------------------------------ |
| ChargeCategory             | Usage                                                 | Compute resource consumption               |
| PricingCategory            | Committed                                             | Priced under commitment discount           |
| BilledCost                 | &dollar;0.00                                          | **MUST be 0** - covered by commitment      |
| EffectiveCost              | &dollar;46.00                                         | Amortized cost (annual / hours)            |
| ListCost                   | &dollar;69.00                                         | What you would have paid at list price     |
| PricingQuantity            | 1                                                     | Units priced                               |
| ConsumedQuantity           | 1                                                     | Hours used                                 |
| CommitmentDiscountQuantity | 1                                                     | Commitment units applied                   |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                         |
| CommitmentDiscountId       | arn:aws:ec2:us-east-1:123456789012:reserved-instan... | Links usage to purchase                    |
| SkuId                      | AWS-USEAST1-COMPUTE-USAGE                             | Resource usage SKU (differs from Purchase) |
| SkuPriceId                 | AWS-USEAST1-COMPUTE-USAGE-COMMITTED                   | Price point for committed usage            |
