# FinOps Open Cost and Usage Specification Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

**Added:**

- `String handling` attribute
- `ChargeClass` column
- `CommitmentDiscountStatus` column
- `ContractedCost` column
- `ContractedUnitPrice` column
- `RegionId` column
- `RegionName` column

**Changed:**

- `Column naming convention` attribute includes the following new provisions:
  - Column IDs should not exceed 50 characters.
  - Attribute renamed to `Column naming and ordering` to denote it also includes rules for column ordering.
- `ChargeCategory` column updates:
  - Added "Credit" value for credits and any applicable credit corrections. See added `ChargeClass` column.
  - Updated "Usage", "Purchase", and "Tax" to include refunds/corrections. See added `ChargeClass` column.
  - Updated "Adjustment" value to exclude credits and refunds.
- `ChargeFrequency` column updates:
  - Column is recommended and may not be present.
- `CommitmentDiscountCategory` column updates:
  - Column is conditional and only required when the provider supports commitment discounts.
- `CommitmentDiscountId` column updates:
  - Column is conditional and only required when the provider supports commitment discounts.
- `CommitmentDiscountName` column updates:
  - Column is conditional and only required when the provider supports commitment discounts.
- `CommitmentDiscountType` column updates:
  - Column is conditional and only required when the provider supports commitment discounts.
- `ConsumedQuantity` column updates:
  - Column renamed from UsageQuantity. It is now limited to ChargeType "Usage" rows.
  - Column is conditional and only required when the provider supports the measurement of usage.
  - Column must not be null when `ChargeCategory` is "Usage" and `ChargeClass` is not "Correction".
- `ConsumedUnit` column updates:
  - Column renamed from UsageUnit. It is now limited to ChargeType "Usage" rows.
  - Column is conditional and only required when the provider supports the measurement of usage.
  - Column must not be null when `ChargeCategory` is "Usage" and `ChargeClass` is not "Correction".
- `EffectiveCost` column updates:
  - Clarified that effective cost does not mix or "blend" costs across multiple charges.
  - Specified that in the case of a purchase charge paid to cover future eligible charges, the Effective Cost is set to 0.
- `ListUnitPrice` column updates:
  - Column is conditional and only required when the provider publishes a price list that excludes discounts.
  - Must not be null when `ChargeClass` is not "Correction" and `ChargeCategory` is "Usage" or "Purchase".
  - Must be null when `ChargeCategory` is "Tax".
- `PricingCategory` column updates:
  - Column is conditional and only required when the provider supports more than one pricing category value.
  - Changed "On-Demand" to "Standard".
  - Changed "Commitment-Based" to "Committed".
  - Must not be null when `ChargeClass` is not "Correction" and `ChargeCategory` is "Usage" or "Purchase".
  - Must be null when `ChargeCategory` is "Tax".
- `PricingQuantity`
  - Must not be null when `ChargeClass` is not "Correction" and `ChargeCategory` is "Usage" or "Purchase".
  - Must be null when `ChargeCategory` is "Tax".
- `PricingUnit`
  - Must not be null when `ChargeClass` is not "Correction" and `ChargeCategory` is "Usage" or "Purchase".
  - Must be null when `ChargeCategory` is "Tax".
- `ResourceId` column updates:
  - Column is conditional and only required when the provider supports billing based on provisioned resource instances.
- `ResourceName` column updates:
  - Column is conditional and only required when the provider supports billing based on provisioned resource instances.
- `ResourceType` column updates:
  - Column is conditional and only required when the provider supports billing based on provisioned resource instances and supports multiple "types" of resources.
- `SkuId` column updates:
  - Column is conditional and only required when the provider publishes a SKU list.
  - Must not be null when `ChargeClass` is not "Correction" and `ChargeCategory` is "Usage" or "Purchase".
  - Must be null when `ChargeCategory` is "Tax".
- `SkuPriceId` column updates:
  - Column is conditional and only required when the provider publishes a SKU price list.
  - Must not be null when `ChargeClass` is not "Correction" and `ChargeCategory` is "Usage" or "Purchase".
  - Must be null when `ChargeCategory` is "Tax".
- `SubAccountId` column updates:
  - Column is conditional and only required when the provider supports a sub account construct.
- `SubAccountName` column updates:
  - Column is conditional and only required when the provider supports a sub account construct.
- `Tags` column updates:
  - Column is conditional and only required when the provider supports setting user- or provider-defined tags.
  - Tag keys that cannot have a value must use a boolean `true` as the tag value.

**Fixed:**

- `CommitmentDiscountType` column constraints were updated to show the column as required to align with the normative text.

**Removed:**

- `ChargeSubcategory` column - See `ChargeCategory` and `ChargeClass` columns
- `Region` column - See `RegionId` and `RegionName` columns

[All unreleased changes](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/compare/v1.0-preview-cr...working_draft)

<br>

## v1.0-preview
<sup>Announced November 15, 2023</sup>

**Added:**

- `Discount handling` attribute
- `Key/value format` attribute
- `Numeric format` attribute
- `Unit format` attribute
- `ChargeDescription` column
- `ChargeFrequency` column
- `ChargeSubcategory` column
- `CommitmentDiscountCategory` column
- `CommitmentDiscountId` column
- `CommitmentDiscountName` column
- `CommitmentDiscountType` column
- `ListCost` column
- `ListUnitPrice` column
- `PricingCategory` column
- `PricingQuantity` column
- `PricingUnit` column
- `ResourceType` column
- `SkuId` column
- `SkuPriceId` column
- `Tags` column
- `UsageQuantity` column
- `UsageUnit` column

**Changed:**

- `Column naming convention` attribute includes the following new provisions:
  - Columns with a `Category` suffix must be normalized.
  - External, custom columns can be added but must be prefixed by `x_`.
  - FOCUS columns must be listed before custom columns in the dataset.
  - Added "SKU" as an exception to the "no acronyms" rule. The display name is "SKU" and column ID is `Sku`.
- `AmortizedCost` column renamed to `EffectiveCost`
- `ChargeType` column renamed to `ChargeCategory`

[All 1.0-preview changes](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/compare/v0.5-cr...v1.0-preview-cr)

<br>

## v0.5
<sup>Announced June 24, 2023</sup>

**Added:**
- `Column naming convention` attribute
- `Currency code format` attribute
- `Date/time format` attribute
- `Null handling` attribute
- `AmortizedCost` column
- `AvailabilityZone` column
- `BilledCost` column
- `BillingAccountId` column
- `BillingAccountName` column
- `BillingCurrency` column
- `BillingPeriodEnd` column
- `BillingPeriodStart` column
- `ChargePeriodEnd` column
- `ChargePeriodStart` column
- `ChargeType` column
- `InvoiceIssuerName` column
- `ProviderName` column
- `PublisherName` column
- `Region` column
- `ResourceId` column
- `ResourceName` column
- `ServiceCategory` column
- `ServiceName` column
- `SubAccountId` column
- `SubAccountName` column

[All 0.5 changes](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/compare/7106bbe...v0.5-cr)

<br>

## Columns History

This table maps the evolution of the billing data, showcasing column introductions and updates from its initial version 0.5 to the comprehensive revisions in "1.0-preview", "1.0" and beyond.

| **Column ID**                | **Revision Introduced** | **Latest Update** |
|------------------------------|-------------------------|-------------------|
| AvailabilityZone             | 0.5                     |                   |
| BilledCost                   | 0.5                     |                   |
| BillingAccountId             | 0.5                     |                   |
| BillingAccountName           | 0.5                     |                   |
| BillingCurrency              | 0.5                     |                   |
| BillingPeriodEnd             | 0.5                     |                   |
| BillingPeriodStart           | 0.5                     |                   |
| ChargeCategory               | 0.5                     | 1.0               |
| ChargeClass                  | 1.0                     |                   |
| ChargeDescription            | 1.0-preview             |                   |
| ChargeFrequency              | 1.0-preview             |                   |
| ChargePeriodEnd              | 0.5                     |                   |
| ChargePeriodStart            | 0.5                     |                   |
| ChargeSubcategory            | 1.0-preview             | Removed in 1.0    |    
| CommitmentDiscountCategory   | 1.0-preview             |                   |
| CommitmentDiscountId         | 1.0-preview             |                   |
| CommitmentDiscountName       | 1.0-preview             |                   |
| CommitmentDiscountStatus     | 1.0                     |                   |
| CommitmentDiscountType       | 1.0-preview             |                   |
| ConsumedQuantity             | 1.0                     |                   |
| ConsumedUnit                 | 1.0                     |                   |
| ContractedCost               | 1.0                     |                   |
| ContractedUnitPrice          | 1.0                     |                   |
| EffectiveCost                | 0.5                     |                   |    
| InvoiceIssuerName            | 0.5                     |                   |    
| ListCost                     | 1.0-preview             |                   |
| ListUnitPrice                | 1.0-preview             |                   |
| PricingCategory              | 1.0-preview             | 1.0               |
| PricingQuantity              | 1.0-preview             |                   |
| PricingUnit                  | 1.0-preview             |                   |
| ProviderName                 | 0.5                     |                   |
| PublisherName                | 0.5                     |                   |
| Region                       | 0.5                     | Removed in 1.0    |
| RegionId                     | 1.0                     |                   |
| RegionName                   | 1.0                     |                   |
| ResourceId                   | 0.5                     |                   |
| ResourceName                 | 0.5                     |                   |
| ResourceType                 | 1.0-preview             |                   |
| ServiceCategory              | 0.5                     |                   |
| ServiceName                  | 0.5                     |                   |
| SkuId                        | 1.0-preview             |                   |
| SkuPriceId                   | 1.0-preview             | 1.0               |
| SubAccountId                 | 0.5                     |                   |
| SubAccountName               | 0.5                     |                   |
| Tags                         | 1.0-preview             | 1.0               |
| UsageQuantity                | 1.0-preview             | Removed in 1.0    |
| UsageUnit                    | 1.0-preview             | Removed in 1.0    |
