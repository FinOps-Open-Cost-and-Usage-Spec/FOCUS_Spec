## DiscountHandling

### Normative Text v1.2

All rows defined in FOCUS MUST follow the discount handling requirements listed below.

## Attribute ID

DiscountHandling

## Attribute Name

Discount Handling

## Description

Indicates how to include and apply discounts to usage charges or rows in a FOCUS dataset.

## Requirements

* All applicable discounts SHOULD be applied to each row they pertain to and SHOULD NOT be negated in a separate row.
* All discounts applied to a row MUST apply to the entire charge.
  * Multiple discounts MAY apply to a row, but they MUST apply to the entire charge covered by that row.
  * If a discount only applies to a portion of a charge, then the discounted portion of the charge MUST be split into a separate row.
  * Each discount MUST be identifiable using existing FOCUS columns.
    * Rows with a *commitment discount* applied to them MUST include a CommitmentDiscountId.
    * If a provider applies a discount that cannot be represented by a FOCUS column, they SHOULD include additional columns to identify the source of the discount.
* Purchased discounts (e.g., *commitment discounts*) MUST be amortized.
  * The BilledCost MUST be 0 for any row where the commitment covers the entire cost for the charge period.
  * The EffectiveCost MUST include the portion of the amortized purchase cost that applies to this row.
  * The sum of the EffectiveCost for all rows where CommitmentDiscountStatus is "Used" or "Unused" for each CommitmentDiscountId over the entire duration of the commitment MUST be the same as the total BilledCost of the *commitment discount*.
  * The CommitmentDiscountId and ResourceId MUST be set to the ID assigned to the *commitment discount*. ChargeCategory MUST be set to "Purchase" on rows that represent a purchase of a *commitment discount*.
  * CommitmentDiscountStatus MUST be "Used" for ChargeCategory "Usage" rows that received a reduced price from a commitment. CommitmentDiscountId MUST be set to the ID assigned to the discount. ResourceId MUST be set to the ID of the resource that received the discount.
  * If a commitment is not fully utilized, the provider MUST include a row that represents the unused portion of the commitment for that *charge period*. These rows MUST be represented with CommitmentDiscountStatus set to "Unused" and ChargeCategory set to "Usage". Such rows MUST have their CommitmentDiscountId and ResourceId set to the ID assigned to the *commitment discount*.
* Credits that are applied after the fact MUST use a ChargeCategory of "Credit".

### Normative Text v1.3

All rows defined in FOCUS MUST follow the discount handling requirements listed below.

## Attribute ID

DiscountHandling

## Attribute Name

Discount Handling

## Description

Indicates how to include and apply discounts to usage charges or rows in a FOCUS dataset.

## Requirements

* All applicable discounts SHOULD be applied to each row they pertain to and SHOULD NOT be negated in a separate row.
* All discounts applied to a row MUST apply to the entire charge.
  * Multiple discounts MAY apply to a row, but they MUST apply to the entire charge covered by that row.
  * If a discount only applies to a portion of a charge, then the discounted portion of the charge MUST be split into a separate row.
  * Each discount MUST be identifiable using existing FOCUS columns.
    * Rows with a *commitment discount* applied to them MUST include a CommitmentDiscountId.
    * If a service provider applies a discount that cannot be represented by a FOCUS column, they SHOULD include additional columns to identify the source of the discount.
* Purchased discounts (e.g., *commitment discounts*) MUST be amortized.
  * The BilledCost MUST be 0 for any row where the commitment covers the entire cost for the charge period.
  * The EffectiveCost MUST include the portion of the amortized purchase cost that applies to this row.
  * The sum of the EffectiveCost for all rows where CommitmentDiscountStatus is "Used" or "Unused" for each CommitmentDiscountId over the entire commitment [*period*](#glossary:period) MUST be the same as the total BilledCost of the *commitment discount*.
  * The CommitmentDiscountId and ResourceId MUST be set to the ID assigned to the *commitment discount*. ChargeCategory MUST be set to "Purchase" on rows that represent a purchase of a *commitment discount*.
  * CommitmentDiscountStatus MUST be "Used" for ChargeCategory "Usage" rows that received a reduced price from a commitment. CommitmentDiscountId MUST be set to the ID assigned to the discount. ResourceId MUST be set to the ID of the resource that received the discount.
  * If a commitment is not fully utilized, the service provider MUST include a row that represents the unused portion of the commitment for that *charge period*. These rows MUST be represented with CommitmentDiscountStatus set to "Unused" and ChargeCategory set to "Usage". Such rows MUST have their CommitmentDiscountId and ResourceId set to the ID assigned to the *commitment discount*.
* Credits that are applied after the fact MUST use a ChargeCategory of "Credit".

### Diff

 All rows defined in FOCUS MUST follow the discount handling requirements listed below.
 
@@ -30,14 +30,14 @@ Indicates how to include and apply discounts to usage charges or rows in a FOCUS
   * If a discount only applies to a portion of a charge, then the discounted portion of the charge MUST be split into a separate row.
   * Each discount MUST be identifiable using existing FOCUS columns.
     * Rows with a *commitment discount* applied to them MUST include a CommitmentDiscountId.
-    * If a provider applies a discount that cannot be represented by a FOCUS column, they SHOULD include additional columns to identify the source of the discount.
+    * If a service provider applies a discount that cannot be represented by a FOCUS column, they SHOULD include additional columns to identify the source of the discount.
 * Purchased discounts (e.g., *commitment discounts*) MUST be amortized.
   * The BilledCost MUST be 0 for any row where the commitment covers the entire cost for the charge period.
   * The EffectiveCost MUST include the portion of the amortized purchase cost that applies to this row.
-  * The sum of the EffectiveCost for all rows where CommitmentDiscountStatus is "Used" or "Unused" for each CommitmentDiscountId over the entire duration of the commitment MUST be the same as the total BilledCost of the *commitment discount*.
+  * The sum of the EffectiveCost for all rows where CommitmentDiscountStatus is "Used" or "Unused" for each CommitmentDiscountId over the entire commitment [*period*](#glossary:period) MUST be the same as the total BilledCost of the *commitment discount*.
   * The CommitmentDiscountId and ResourceId MUST be set to the ID assigned to the *commitment discount*. ChargeCategory MUST be set to "Purchase" on rows that represent a purchase of a *commitment discount*.
   * CommitmentDiscountStatus MUST be "Used" for ChargeCategory "Usage" rows that received a reduced price from a commitment. CommitmentDiscountId MUST be set to the ID assigned to the discount. ResourceId MUST be set to the ID of the resource that received the discount.
-  * If a commitment is not fully utilized, the provider MUST include a row that represents the unused portion of the commitment for that *charge period*. These rows MUST be represented with CommitmentDiscountStatus set to "Unused" and ChargeCategory set to "Usage". Such rows MUST have their CommitmentDiscountId and ResourceId set to the ID assigned to the *commitment discount*.
+  * If a commitment is not fully utilized, the service provider MUST include a row that represents the unused portion of the commitment for that *charge period*. These rows MUST be represented with CommitmentDiscountStatus set to "Unused" and ChargeCategory set to "Usage". Such rows MUST have their CommitmentDiscountId and ResourceId set to the ID assigned to the *commitment discount*.
 * Credits that are applied after the fact MUST use a ChargeCategory of "Credit".