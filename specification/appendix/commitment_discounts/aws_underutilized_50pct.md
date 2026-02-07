# Amazon Web Services EC2 Instance Savings Plan (All-Upfront)

| Parameter         | Value               |
| ----------------- | ------------------- |
| Scenario Type     | commitment          |
| Payment Type      | All-Upfront         |
| Category          | Spend-based         |
| Utilization       | 50%                 |
| Hours Generated   | 24                  |
| Annual Commitment | &dollar;693,000.00  |
| Committed Rate    | &dollar;79.11/hour  |
| On-Demand Rate    | &dollar;118.67/hour |
| Savings           | 33%                 |

[CSV Example](/specification/data/commitment_discount_scenarios/aws_underutilized_50pct.csv)

## Scenario Description

This example shows a **Amazon Web Services EC2 Instance Savings Plan** (Savings Plan), which is a spend-based commitment where you commit to a specific dollar amount of usage per hour.

The **All-Upfront** payment option means the entire commitment cost is paid at purchase time. This results in a single Purchase row with the full BilledCost and EffectiveCost=0 (since the cost is amortized to usage rows).

This scenario demonstrates **underutilization** at 50% where only 12 of 24 commitment hours are consumed. The remaining 12 hours appear as 'Unused' rows with CommitmentDiscountStatus='Unused'. These unused rows still have EffectiveCost to reflect the wasted commitment value.

## Row Summary

| Row Type          | Count | Total BilledCost       | Total EffectiveCost  |
| ----------------- | ----- | ---------------------- | -------------------- |
| Purchase          | 1     | &dollar;693,000.00     | &dollar;0.00         |
| Usage (Used)      | 12    | &dollar;0.00           | &dollar;949.32       |
| Usage (Unused)    | 12    | &dollar;0.00           | &dollar;949.32       |
| Usage (On-Demand) | 12    | &dollar;24.06          | &dollar;24.06        |
| **Total**         | 37    | **&dollar;693,024.06** | **&dollar;1,922.70** |

## Column Interactions

Understanding how columns relate to each other is critical for validating FOCUS data. This section explains the key relationships.

### Quantity Columns: PricingQuantity vs ConsumedQuantity vs CommitmentDiscountQuantity

These three quantity columns serve different purposes and must be understood in context:

| Column                         | Purpose                               | When Populated                | Typical Value        |
| ------------------------------ | ------------------------------------- | ----------------------------- | -------------------- |
| **PricingQuantity**            | Quantity used for pricing calculation | All priced rows               | 1 (per hour/unit)    |
| **ConsumedQuantity**           | Actual resource consumption           | Usage rows with resources     | 1 (hours consumed)   |
| **CommitmentDiscountQuantity** | Commitment capacity applied           | Rows with commitment discount | 1 (commitment units) |

### Pricing Columns: ListUnitPrice vs ContractedUnitPrice

| Column                  | Purpose                    | Commitment-Covered | On-Demand      |
| ----------------------- | -------------------------- | ------------------ | -------------- |
| **ListUnitPrice**       | On-demand (public) price   | &dollar;118.67     | &dollar;118.67 |
| **ContractedUnitPrice** | Negotiated/committed price | &dollar;79.11      | null           |

**Why this matters:** The difference between ListUnitPrice and ContractedUnitPrice represents your savings from the commitment. On-demand rows have no ContractedUnitPrice because they aren't covered by a commitment.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario          | BilledCost         | EffectiveCost | ListCost           |
| ----------------- | ------------------ | ------------- | ------------------ |
| **Purchase Row**  | &dollar;693,000.00 | &dollar;0.00  | &dollar;693,000.00 |
| **Used Row**      | &dollar;0.00       | &dollar;79.11 | &dollar;118.67     |
| **Unused Row**    | &dollar;0.00       | &dollar;79.11 | null               |
| **On-Demand Row** | &dollar;10.14      | &dollar;10.14 | &dollar;10.14      |

The following critical rules apply to commitment discount data:

* **Purchase rows:** `EffectiveCost` MUST be 0. The cost is distributed to usage rows.
* **Used rows:** `BilledCost` MUST be 0. Usage is covered by the commitment.
* **Unused rows:** `BilledCost` = 0 but `EffectiveCost` > 0 to represent wasted commitment value.
* **On-demand rows:** `BilledCost` = `EffectiveCost` = `ListCost`. No commitment discount applies.

## Purchase Row Details

| Column                   | Value              | Explanation                                     |
| ------------------------ | ------------------ | ----------------------------------------------- |
| ChargeCategory           | Purchase           | Commitment purchase transaction                 |
| ChargeFrequency          | One-Time           | One-time upfront payment                        |
| BilledCost               | &dollar;693,000.00 | Full annual commitment payment                  |
| EffectiveCost            | &dollar;0.00       | **MUST be 0** - cost is amortized to usage rows |
| PricingQuantity          | 1                  | One commitment unit purchased                   |
| CommitmentDiscountStatus | null               | Status only applies to usage rows               |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                           |
| -------------------------- | ----------------------------------------------------- | ------------------------------------- |
| ChargeCategory             | Usage                                                 | Compute resource consumption          |
| PricingCategory            | Committed                                             | Priced at committed rate              |
| BilledCost                 | &dollar;0.00                                          | **MUST be 0** - covered by commitment |
| EffectiveCost              | &dollar;79.11                                         | Amortized cost (annual / hours)       |
| ListCost                   | &dollar;118.67                                        | What you would have paid on-demand    |
| PricingQuantity            | 1                                                     | Units priced                          |
| ConsumedQuantity           | 1                                                     | Hours used                            |
| CommitmentDiscountQuantity | 79.11                                                 | Units applied                         |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                    |
| CommitmentDiscountId       | arn:aws:savingsplans::123456789012:savingsplan/sp-... | Links usage to purchase               |

## Unused Commitment Row Details

| Column                     | Value         | Explanation                                      |
| -------------------------- | ------------- | ------------------------------------------------ |
| ChargeCategory             | Usage         | Represents commitment capacity                   |
| BilledCost                 | &dollar;0.00  | No additional billing (already paid at purchase) |
| EffectiveCost              | &dollar;79.11 | **Wasted value** - lost commitment               |
| PricingQuantity            | 1             | Commitment units unused                          |
| ConsumedQuantity           | null          | **No resource consumed**                         |
| CommitmentDiscountQuantity | 79.11         | Commitment wasted                                |
| CommitmentDiscountStatus   | Unused        | Commitment not utilized                          |
| ResourceId                 | (empty)       | No resource associated                           |

## On-Demand Usage Row Details

| Column                     | Value         | Explanation                   |
| -------------------------- | ------------- | ----------------------------- |
| ChargeCategory             | Usage         | On-demand compute consumption |
| PricingCategory            | Standard      | No discount applied           |
| BilledCost                 | &dollar;10.14 | On-demand price               |
| EffectiveCost              | &dollar;10.14 | = BilledCost                  |
| ListCost                   | &dollar;10.14 | Same as BilledCost            |
| PricingQuantity            | 441           | Units priced                  |
| ConsumedQuantity           | 441           | Hours used                    |
| CommitmentDiscountQuantity | null          | **No commitment applied**     |
| CommitmentDiscountStatus   | null          | No commitment                 |
| CommitmentDiscountId       | (empty)       | No associated commitment      |
| ContractedUnitPrice        | null          | No contracted rate            |

## Validation Rules

Use these rules to validate FOCUS commitment data.

### Rule 1: Purchase Row Effective Cost

```text
FOR ALL rows WHERE ChargeCategory = 'Purchase':
    ASSERT EffectiveCost = 0
```

**Rationale:** Purchase costs are distributed to usage rows through amortization. The purchase itself has no effective cost.

### Rule 2: Commitment-Covered Usage Has Zero Billed Cost

```text
FOR ALL rows WHERE CommitmentDiscountStatus IN ('Used', 'Unused'):
    ASSERT BilledCost = 0
```

**Rationale:** Usage covered by a commitment has already been paid for through the purchase transaction.

### Rule 3: On-Demand Cost Equality

```text
FOR ALL rows WHERE PricingCategory = 'Standard' AND ChargeCategory = 'Usage':
    ASSERT BilledCost = EffectiveCost
    ASSERT BilledCost = ListCost
```

**Rationale:** On-demand usage has no discount or amortization. All cost columns should be equal.

### Rule 4: Commitment Link Integrity

```text
FOR ALL rows WHERE CommitmentDiscountStatus IS NOT NULL:
    ASSERT CommitmentDiscountId IS NOT EMPTY
    ASSERT CommitmentDiscountId matches a Purchase row ResourceId
```

**Rationale:** Every Used/Unused row must link back to its originating purchase.

### Rule 5: Amortization Balance

```text
FOR commitment period:
    ASSERT Sum(Purchase.BilledCost) = Sum(Usage.EffectiveCost WHERE CommitmentDiscountStatus IS NOT NULL)
```

**Rationale:** The total effective cost of commitment-covered usage should equal the purchase cost when summed over the commitment term.

### Validation for This Scenario

Validation for All-Upfront payment option:

* Annual commitment: &dollar;693,000.00
* Hours in term: 24
* Hourly amortization: &dollar;693,000.00 / 24 = &dollar;28,875.00/hour
* Daily amortization (365 days): &dollar;693,000.00 / 365 = &dollar;1,898.63/day
* Sum(Usage EffectiveCost): &dollar;949.32

**Check:** &dollar;949.32 should approach &dollar;693,000.00 over the full term.

### All Validation Rules Passed

This example data is valid according to FOCUS commitment discount rules.
