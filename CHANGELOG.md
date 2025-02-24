# FinOps Open Cost and Usage Specification Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!--
## v1.2

[All unreleased changes](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/compare/1.1...working_draft)

<br>
-->

## v1.1

<sup>Announced November 2024</sup>

**Added:**

- `CapacityReservationId` column
- `CapacityReservationStatus` column
- `CommitmentDiscountQuantity` column
- `CommitmentDiscountUnit` column
- `ServiceSubcategory` column
- `SkuMeter` column
- `SkuPriceDetails` column
- `ProviderVersion` metadata schema property

**Changed:**

- `CommitmentDiscountId` column updates:
  - Must be globally unique within the provider.
  - Should be a fully-qualified identifier.
- `ConsumedQuantity` column updates:
  - Must be null when `CommitmentDiscountStatus` is "Unused".
- `ConsumedUnit` column updates:
  - Must be null when `ChargeClass` is not "Correction" and `ChargeCategory` is not "Usage".
  - Must be null when `ChargeClass` is not "Correction" and `ChargeCategory` is "Usage" and `CommitmentDiscountStatus` is "Unused".
  - May be null when `ChargeCategory` is "Usage" and `ChargeClass` is "Correction".
- `EffectiveCost` column updates:
  - When `CommitmentDiscountStatus` is "Unused", must be the difference between the used commitment discount amount and the portion of the total commitment discount purchase applicable for the charge period.
- `PricingCategory` column updates:
  - Must not be "Committed" when the charge is for a commitment discount purchase.
- `SkuPriceId` column updates:
  - `SkuId` can be used if the provider does not have a `SkuPriceId` but other requirements must be met.
- Metadata updates:
  - Must be provided in the defined metadata schema.
  - Must be an object.
  - Must not be null.
  - Must include a reference to the schema of the data.
  - Schema reference must not be in the FOCUS dataset itself.
  - Must be an accurate and complete representation of the provided FOCUS dataset.
  - Metadata implementation should be publicly documented.
- `SchemaId` metadata schema property updates:
  - Recommended to be a globally unique identifier (GUID) instead of a universally unique identifier (UUID) or SemVer version.

[All 1.1 changes](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/compare/v1.0...v1.1-cr)

<br>

## v1.0

<sup>Announced June 20, 2024</sup>

**Added:**

- `String handling` attribute
- `ChargeClass` column
- `CommitmentDiscountStatus` column
- `ContractedCost` column
- `ContractedUnitPrice` column
- `RegionId` column
- `RegionName` column
- `DataGenerator` metadata property
- `CreationDate` metadata schema property
- `FocusVersion` metadata schema property
- `SchemaId` metadata schema property
- `ColumnName` metadata column definition property
- `DataType` metadata column definition property
- `NumberScale` metadata column definition property
- `NumberPrecision` metadata column definition property
- `ProviderTagPrefix` metadata column definition property
- `StringEncoding` metadata column definition property
- `StringMaxLength` metadata column definition property

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
- `RegionId` column updates:
  - `Region` column was renamed to `RegionId` when `RegionName` column was introduced
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

[All 1.0 changes](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/compare/v1.0-preview...v1.0)

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

[All 1.0-preview changes](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/compare/v0.5...v1.0-preview)

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

[All 0.5 changes](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/compare/7106bbe...v0.5)

<br>

## Columns History

This table maps the evolution of the specification, showcasing column introductions and updates from its initial version 0.5 to the comprehensive revisions in "1.0-preview", "1.0" and beyond.

| **Column ID**                | **Revision Introduced** | **Status**        |
|------------------------------|-------------------------|-------------------|
| AmortizedCost                | 0.5                     | Renamed to EffectiveCost in v1.0-preview |
| AvailabilityZone             | 0.5                     |                   |
| BilledCost                   | 0.5                     |                   |
| BillingAccountId             | 0.5                     |                   |
| BillingAccountName           | 0.5                     |                   |
| BillingCurrency              | 0.5                     |                   |
| BillingPeriodEnd             | 0.5                     |                   |
| BillingPeriodStart           | 0.5                     |                   |
| CapacityReservationId        | 1.1                     |                   |
| CapacityReservationStatus    | 1.1                     |                   |
| ChargeType                   | 0.5                     | Renamed to ChargeCategory in v1.0-preview |
| ChargeCategory               | 1.0-preview             | Renamed from ChargeType in v1.0-preview |
| ChargeClass                  | 1.0                     |                   |
| ChargeDescription            | 1.0-preview             |                   |
| ChargeFrequency              | 1.0-preview             |                   |
| ChargePeriodEnd              | 0.5                     |                   |
| ChargePeriodStart            | 0.5                     |                   |
| ChargeSubcategory            | 1.0-preview             | Removed in v1.0   |
| CommitmentDiscountCategory   | 1.0-preview             |                   |
| CommitmentDiscountId         | 1.0-preview             |                   |
| CommitmentDiscountName       | 1.0-preview             |                   |
| CommitmentDiscountStatus     | 1.0                     |                   |
| CommitmentDiscountType       | 1.0-preview             |                   |
| CommitmentDiscountQuantity   | 1.1                     |                   |
| CommitmentDiscountUnit       | 1.1                     |                   |
| ConsumedQuantity             | 1.0                     | Renamed from UsageQuantity in v1.0 |
| ConsumedUnit                 | 1.0                     | Renamed from UsageUnit in v1.0 |
| ContractedCost               | 1.0                     |                   |
| ContractedUnitPrice          | 1.0                     |                   |
| EffectiveCost                | 1.0-preview             | Renamed from AmortizedCost in v1.0-preview |
| InvoiceIssuerName            | 0.5                     |                   |
| ListCost                     | 1.0-preview             |                   |
| ListUnitPrice                | 1.0-preview             |                   |
| PricingCategory              | 1.0-preview             |                   |
| PricingQuantity              | 1.0-preview             |                   |
| PricingUnit                  | 1.0-preview             |                   |
| ProviderName                 | 0.5                     |                   |
| PublisherName                | 0.5                     |                   |
| Region                       | 0.5                     | Renamed to RegionId in v1.0 |
| RegionId                     | 1.0                     | Renamed from Region in v1.0 |
| RegionName                   | 1.0                     |                   |
| ResourceId                   | 0.5                     |                   |
| ResourceName                 | 0.5                     |                   |
| ResourceType                 | 1.0-preview             |                   |
| ServiceCategory              | 0.5                     |                   |
| ServiceName                  | 0.5                     |                   |
| ServiceSubcategory           | 1.1                     |                   |
| SkuId                        | 1.0-preview             |                   |
| SkuMeter                     | 1.1                     |                   |
| SkuPriceDetails              | 1.1                     |                   |
| SkuPriceId                   | 1.0-preview             |                   |
| SubAccountId                 | 0.5                     |                   |
| SubAccountName               | 0.5                     |                   |
| Tags                         | 1.0-preview             |                   |
| UsageQuantity                | 1.0-preview             | Renamed to ConsumedQuantity in v1.0 |
| UsageUnit                    | 1.0-preview             | Renamed to ConsumedUnit in v1.0 |
