# GCP Flex CUD - All Upfront - 100% Utilization

| Parameter         | Value              |
| ----------------- | ------------------ |
| Scenario Type     | commitment         |
| Payment Model     | All-Upfront        |
| CommitmentDiscountCategory | Spend        |
| Utilization       | 100%               |
| Hours Generated   | 24                 |
| Annual Commitment | &dollar;553,000.00 |
| Effective Unit Price | &dollar;63.13/hour |
| List Unit Price   | &dollar;94.70/hour |
| Savings           | 33%                |

[CSV Example](/specification/data/commitment_discount_scenarios/gcp_flex_cud_all_upfront_100pct.csv)

## Scenario Description

This example shows a **Google Cloud Platform Spend-based CUD** (Committed Use Discount (Spend)), which is a commitment (CommitmentDiscountCategory: Spend) where you commit to a specific dollar amount of usage per hour.

The **All-Upfront** payment option means the entire commitment cost is paid at purchase time. This results in a single Purchase row with the full BilledCost and EffectiveCost=0 (since the cost is amortized to usage rows).

This scenario demonstrates **full utilization** where exactly 100% of the commitment capacity is consumed. All usage rows have CommitmentDiscountStatus='Used', indicating the commitment was fully applied. BilledCost=0 on usage rows because they're covered by the commitment.

## Row Summary

| Row Type          | Count | Total BilledCost       | Total EffectiveCost  |
| ----------------- | ----- | ---------------------- | -------------------- |
| Purchase          | 1     | &dollar;553,000.00     | &dollar;0.00         |
| Usage (Used)      | 24    | &dollar;0.00           | &dollar;1,515.12     |
| Usage (Standard) | 12    | &dollar;25.52          | &dollar;25.52        |
| **Total**         | 37    | **&dollar;553,025.52** | **&dollar;1,540.64** |

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

| Column                  | Purpose                    | Commitment-Covered | Standard     |
| ----------------------- | -------------------------- | ------------------ | ------------- |
| **ListUnitPrice**       | List (public) unit price   | &dollar;94.70      | &dollar;94.70 |
| **ContractedUnitPrice** | Negotiated unit price | &dollar;63.13      | null          |

| **ContractedUnitPrice** | Negotiated unit price | &dollar;94.70      | &dollar;94.70 |

**Why this matters:** ContractedUnitPrice reflects enterprise-negotiated pricing (e.g., EDP rates), not commitment discount savings. In non-negotiated scenarios, ContractedUnitPrice equals ListUnitPrice. Commitment discount savings are reflected in EffectiveCost, not in unit prices.

### Cost Columns: BilledCost vs EffectiveCost vs ListCost

| Scenario          | BilledCost         | EffectiveCost | ListCost           |
| ----------------- | ------------------ | ------------- | ------------------ |
| **Purchase Row**  | &dollar;553,000.00 | &dollar;0.00  | &dollar;553,000.00 |
| **Used Row**      | &dollar;0.00       | &dollar;63.13 | &dollar;94.70      |
| **Standard Row** | &dollar;9.76       | &dollar;9.76  | &dollar;9.76       |

The following critical rules apply to commitment discount data:

* **Purchase rows:** `EffectiveCost` MUST be 0. The cost is distributed to usage rows.
* **Used rows:** `BilledCost` MUST be 0. Usage is covered by the commitment.
* **Unused rows:** `BilledCost` = 0 but `EffectiveCost` > 0 to represent wasted commitment value.
* **Standard pricing rows:** `BilledCost` = `EffectiveCost` = `ListCost`. No commitment discount applies.

## Purchase Row Details

| Column                   | Value              | Explanation                                     |
| ------------------------ | ------------------ | ----------------------------------------------- |
| ChargeCategory           | Purchase           | Commitment purchase transaction                 |
| ChargeFrequency          | One-Time           | One-time upfront payment                        |
| BilledCost               | &dollar;553,000.00 | Full annual commitment payment                  |
| EffectiveCost            | &dollar;0.00       | **MUST be 0** - cost is amortized to usage rows |
| PricingQuantity          | 1                  | One commitment unit purchased                   |
| CommitmentDiscountStatus | null               | Status only applies to usage rows               |

## Usage Row Details (Commitment-Covered)

| Column                     | Value                                                 | Explanation                           |
| -------------------------- | ----------------------------------------------------- | ------------------------------------- |
| ChargeCategory             | Usage                                                 | Compute resource consumption          |
| PricingCategory            | Committed                                             | Priced under commitment discount              |
| BilledCost                 | &dollar;0.00                                          | **MUST be 0** - covered by commitment |
| EffectiveCost              | &dollar;63.13                                         | Amortized cost (annual / hours)       |
| ListCost                   | &dollar;94.70                                         | What you would have paid at list price    |
| PricingQuantity            | 1                                                     | Units priced                          |
| ConsumedQuantity           | 1                                                     | Hours used                            |
| CommitmentDiscountQuantity | 63.13                                                 | Commitment dollars applied            |
| CommitmentDiscountStatus   | Used                                                  | Commitment applied                    |
| CommitmentDiscountId       | projects/my-project-123456/locations/us-central1/c... | Links usage to purchase               |

## Standard Pricing Usage Row Details

| Column                     | Value        | Explanation                   |
| -------------------------- | ------------ | ----------------------------- |
| ChargeCategory             | Usage        | Compute consumption (standard pricing) |
| PricingCategory            | Standard     | No discount applied           |
| BilledCost                 | &dollar;9.76 | List unit price               |
| EffectiveCost              | &dollar;9.76 | = BilledCost                  |
| ListCost                   | &dollar;9.76 | Same as BilledCost            |
| PricingQuantity            | 488          | Units priced                  |
| ConsumedQuantity           | 488          | Hours used                    |
| CommitmentDiscountQuantity | null         | **No commitment applied**     |
| CommitmentDiscountStatus   | null         | No commitment                 |
| CommitmentDiscountId       | (empty)      | No associated commitment      |
| ContractedUnitPrice        | null         | No contracted unit price            |

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

### Rule 3: Standard Pricing Cost Equality

```text
FOR ALL rows WHERE PricingCategory = 'Standard' AND ChargeCategory = 'Usage':
    ASSERT BilledCost = EffectiveCost
    ASSERT BilledCost = ListCost
```

**Rationale:** Standard pricing usage has no discount or amortization. All cost columns should be equal.

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

* Annual commitment: &dollar;553,000.00
* Hours in term: 24
* Hourly amortization: &dollar;553,000.00 / 24 = &dollar;23,041.67/hour
* Daily amortization (365 days): &dollar;553,000.00 / 365 = &dollar;1,515.07/day
* Sum(Usage EffectiveCost): &dollar;1,515.12

### All Validation Rules Passed

This example data is valid according to FOCUS commitment discount rules.
