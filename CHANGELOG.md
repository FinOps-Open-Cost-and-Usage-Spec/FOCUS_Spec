# FinOps Open Cost and Usage Specification Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## v1.3

<sup>Announced December 2025</sup>

### Changes to Supported Features by [Change Impact Classification](/guidelines/spec-change-guidelines.md)

#### Compatible Changes

- New Columns to support [Data Generator-Calculated Split Cost Allocation](/specification/supported_features/data_generator_calculated_split_cost_allocation.md)
- New Dataset and Columns to support [Contract Commitments](/specification/supported_features/contract_commitments.md)
- New Columns to support [Participating Entity Identification](/specification/supported_features/participating_entity_identification.md)
- New Metadata to support [Dataset Instance Metadata](/specification/supported_features/dataset_instance_metadata.md)
- New Metadata to support [Recency Metadata](/specification/supported_features/recency_metadata.md)

#### Migration Compatible Changes

- Replacement of Provider and Publisher Columns, affecting:
  - [Charge Categorization](/specification/supported_features/charge_categorization.md)
  - [Commit Usage and Under Usage](/specification/supported_features/commit_usage_and_under_usage.md)
  - [Cost Comparison](/specification/supported_features/cost_comparison.md)
  - [Effective Cost](/specification/supported_features/effective_cost.md)
  - [Marketplace Purchases](/specification/supported_features/marketplace_purchases.md)
  - [Participating Entity Identification](/specification/supported_features/participating_entity_identification.md)
  - [Provider Services](/specification/supported_features/provider_services.md)
  - [Resource Usage](/specification/supported_features/resource_usage.md)
  - [Service Categorization](/specification/supported_features/service_categorization.md)

#### Incompatible Changes

- None

### Added

#### New supported features

- [Contract Commitments](/specification/supported_features/contract_commitments.md)
- [Dataset Instance Metadata](/specification/supported_features/dataset_instance_metadata.md)
- [Participating Entity Identification](/specification/supported_features/participating_entity_identification.md)
- [Data Generator-Calculated Split Cost Allocation](/specification/supported_features/data_generator_calculated_split_cost_allocation.md)
- [Recency Metadata](/specification/supported_features/recency_metadata.md)

#### New datasets

- [`ContractCommitment`](/specification/datasets/contract_commitment/dataset.md)

#### New columns

- [`CostAndUsage`](/specification/datasets/cost_and_usage/dataset.md)
  - [`AllocatedMethodDetails`](/specification/datasets/cost_and_usage/columns/allocatedmethoddetails.md)
  - [`AllocatedMethodId`](/specification/datasets/cost_and_usage/columns/allocatedmethodid.md)
  - [`AllocatedResourceId`](/specification/datasets/cost_and_usage/columns/allocatedresourceid.md)
  - [`AllocatedResourceName`](/specification/datasets/cost_and_usage/columns/allocatedresourcename.md)
  - [`AllocatedTags`](/specification/datasets/cost_and_usage/columns/allocatedtags.md)
  - [`ContractApplied`](/specification/datasets/cost_and_usage/columns/contractapplied.md)
  - [`HostProviderName`](/specification/datasets/cost_and_usage/columns/hostprovidername.md)
  - [`ServiceProviderName`](/specification/datasets/cost_and_usage/columns/serviceprovidername.md)
- [`ContractCommitment`](/specification/datasets/contract_commitment/dataset.md)
  - [`BillingCurrency`](/specification/datasets/contract_commitment/columns/billingcurrency.md)
  - [`ContractCommitmentCategory`](/specification/datasets/contract_commitment/columns/contractcommitmentcategory.md)
  - [`ContractCommitmentCost`](/specification/datasets/contract_commitment/columns/contractcommitmentcost.md)
  - [`ContractCommitmentId`](/specification/datasets/contract_commitment/columns/contractcommitmentid.md)
  - [`ContractCommitmentPeriodEnd`](/specification/datasets/contract_commitment/columns/contractcommitmentperiodend.md)
  - [`ContractCommitmentPeriodStart`](/specification/datasets/contract_commitment/columns/contractcommitmentperiodstart.md)
  - [`ContractCommitmentQuantity`](/specification/datasets/contract_commitment/columns/contractcommitmentquantity.md)
  - [`ContractCommitmentType`](/specification/datasets/contract_commitment/columns/contractcommitmenttype.md)
  - [`ContractCommitmentUnit`](/specification/datasets/contract_commitment/columns/contractcommitmentunit.md)
  - [`ContractId`](/specification/datasets/contract_commitment/columns/contractid.md)
  - [`ContractPeriodEnd`](/specification/datasets/contract_commitment/columns/contractperiodend.md)
  - [`ContractPeriodStart`](/specification/datasets/contract_commitment/columns/contractperiodstart.md)

#### New attributes

- [`InvoiceHandling`](/specification/attributes/invoice_handling.md)
- [`JsonObjectFormat`](/specification/attributes/json_object_format.md)
- [`DataGeneratorCalculatedSplitCostAllocationHandling`](/specification/attributes/data_generator_calculated_split_cost_allocation_handling.md)

#### New appendix entries

- [Dataset Instance metadata example](/specification/appendix/metadata_examples/dataset_instance_metadata_example.md)
- [Recency metadata example](/specification/appendix/metadata_examples/recency_metadata_example.md)
- [Recency metadata updating over time](/specification/appendix/metadata_examples/recency_metadata_updating_over_time_dataset_example.md)
- [Recency metadata updating not over time](/specification/appendix/metadata_examples/recency_metadata_updating_non_over_time_dataset_example.md)
- [Schema Dataset Instance ID example](/specification/appendix/metadata_examples/schema_dataset_instance_id_example.md)

#### New metadata column definition properties

- [`DatasetInstance`](/specification/metadata/dataset_instance/dataset_instance_overview.md)
  - [`DatasetInstanceId`](/specification/metadata/dataset_instance/dataset_instance_id.md)
  - [`DatasetInstanceName`](/specification/metadata/dataset_instance/dataset_instance_name.md)
  - [`FocusDatasetId`](/specification/metadata/dataset_instance/focus_dataset_id.md)
- [`Recency`](/specification/metadata/recency/recency_overview.md)
  - [`DatasetInstanceComplete`](/specification/metadata/recency/dataset_instance_complete.md)
  - [`DatasetInstanceId`](/specification/metadata/recency/dataset_instance_id.md)
  - [`DatasetInstanceLastUpdated`](/specification/metadata/recency/dataset_instance_last_updated.md)
  - [`RecencyLastUpdated`](/specification/metadata/recency/recency_last_updated.md)
  - [`TimeSectors`](/specification/metadata/recency/time_sectors/time_sectors_overview.md)
    - [`TimeSectorComplete`](/specification/metadata/recency/time_sectors/time_sector_complete.md)
    - [`TimeSectorEnd`](/specification/metadata/recency/time_sectors/time_sector_end.md)
    - [`TimeSectorLastUpdated`](/specification/metadata/recency/time_sectors/time_sector_last_updated.md)
    - [`TimeSectorStart`](/specification/metadata/recency/time_sectors/time_sector_start.md)

#### New glossary entries

- [Glossary](/specification/glossary.md)
  - `Allocated Charge`
  - `Allocated Method`
  - `Contract`
  - `Contract Commitment`
  - `Dataset Artifact`
  - `Dataset Instance`
  - `Dataset Instance Artifact`
  - `JSON`
  - `Origin Charge`
  - `Period`

#### New requirements model

The specification's normative requirements are now maintained in a structured, graph-based collection of rules.  Version 1.2 of the requirements model is available as of this writing; 1.3 will be released during the 1.4 development cycle.  This requirements model is designed to be leveraged by a conformance validator, maintained [here](https://github.com/finopsfoundation/focus_validator).  For more information on the requirements model, see [here](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/working_draft/specification/requirements_model/README.md).

### Changed

#### Changed datasets

- [`CostAndUsage`](/specification/datasets/cost_and_usage/dataset.md)
  - FOCUS had only one dataset prior to 1.3, and thus it did not have a name.  See below for a list of changed columns.
- Datasets are now explicitly associated with attributes via normative requirements; this was previously implied.
- Datasets now have their column set laid out in tabular format within their respective entries.

#### Changed columns

- [`CostAndUsage`](/specification/datasets/cost_and_usage/dataset.md)
  - [`CommitmentDiscountQuantity`](/specification/datasets/cost_and_usage/columns/commitmentdiscountquantity.md)
    - CommitmentDiscountQuantity MUST be null when SkuPriceId is null.  This requirement was previously implied, but not directly stated.
  - [`ConsumedQuantity`](/specification/datasets/cost_and_usage/columns/consumedquantity.md)
    - ConsumedQuantity MUST be null when SkuPriceId is null.  This requirement was previously implied, but not directly stated.
  - [`ContractedCost`](/specification/datasets/cost_and_usage/columns/contractedcost.md)
    - ContractedCost MUST equal the product of ContractedUnitPrice and PricingQuantity when ContractedUnitPrice is not null and PricingQuantity is not null.  This requirement was previously implied, but not directly stated.
  - [`ContractedUnitPrice`](/specification/datasets/cost_and_usage/columns/contractedunitprice.md)
    - ContractedUnitPrice MUST be null when SkuPriceId is null.  This requirement was previously implied, but not directly stated.
    - ContractedUnitPrice MUST NOT be null when SkuPriceId is not null.  This requirement was previously implied, but not directly stated.
  - [`InvoiceId`](/specification/datasets/cost_and_usage/columns/invoiceid.md)
    - The sum of BilledCost for a given InvoiceId MUST match the sum of the payable amount provided in the corresponding invoice with the same id generated by the InvoiceIssuerName.  This requirement was previously implied, but not directly stated.
  - [`InvoiceIssuerName`](/specification/datasets/cost_and_usage/columns/invoiceissuername.md)
    - The display name has changed from `Invoice Issuer` to `Invoice Issuer Name`. The column ID and definition remains the same.
  - [`ListCost`](/specification/datasets/cost_and_usage/columns/listcost.md)
    - Discrepancies are no longer allowed for corrections.  Now, in all cases, ListCost MUST equal the product of ListUnitPrice and PricingQuantity when ListUnitPrice is not null and PricingQuantity is not null.
  - [`ListUnitPrice`](/specification/datasets/cost_and_usage/columns/listunitprice.md)
    - ListUnitPrice MUST be null when SkuPriceId is null.  This requirement was previously implied, but not directly stated.
    - ListUnitPrice MUST NOT be null when SkuPriceId is not null.  This requirement was previously implied, but not directly stated.
  - [`PricingCategory`](/specification/datasets/cost_and_usage/columns/pricingcategory.md)
    -  PricingCategory MUST be null when SkuPriceId is null.  This requirement was previously implied, but not directly stated.
  - [`PricingCurrencyContractedUnitPrice`](/specification/datasets/cost_and_usage/columns/pricingcurrencycontractedunitprice.md)
    - PricingCurrencyContractedUnitPrice MUST be null when SkuPriceId is null.  This requirement was previously implied, but not directly stated.
    - PricingCurrencyContractedUnitPrice MUST NOT be null when SkuPriceId is not null.  This requirement was previously implied, but not directly stated.
  - [`PricingCurrencyListUnitPrice`](/specification/datasets/cost_and_usage/columns/pricingcurrencylistunitprice.md)
    - PricingCurrencyListUnitPrice MUST be null when SkuPriceId is null.  This requirement was previously implied, but not directly stated.
    - PricingCurrencyListUnitPrice MUST NOT be null when SkuPriceId is not null.  This requirement was previously implied, but not directly stated.
  - [`PricingQuantity`](/specification/datasets/cost_and_usage/columns/pricingquantity.md)
    - PricingQuantity MUST be null when SkuPriceId is null.  This requirement was previously implied, but not directly stated.
    - PricingQuantity MUST be a valid decimal value when not null.  This requirement was previously implied, but not directly stated.

#### Changed attributes

- None

#### Changed appendix entries

- Metadata examples now include use of `DatasetInstanceId`.
- [Participating Entity Identification](/specification/appendix/participating_entity_identification.md) replaces Origination of Cost Data.  
  - The layout and functionality is the same, but the entities have been renamed, and new entries have been included.

#### Changed metadata

##### Changed metadata properties

- None

#### Changed glossary entries

- [Glossary](/specification/glossary.md)
  - `Commitment` has been changed to include both spend and usage, not just usage.
  - `FOCUS Dataset` is now more narrowly defined alongside `Dataset Artifact` and `Dataset Instance`.
  - `Term` is now strictly associated with agreements specified on a contract.  Some legacy use of that term was associated with length of time, and that use has now been replaced by `Period`.

### Deprecated

#### Deprecated columns
This functionality will be removed in a future release of FOCUS.

- [`CostAndUsage`](/specification/datasets/cost_and_usage/dataset.md)
  - [`ProviderName`](/specification/datasets/cost_and_usage/columns/providername.md)
    - Due to definitional conflicts between the Provider and Publisher columns, this column is deprecated and will be removed in a future release. This column was replaced with the new ServiceProviderName column.  
  - [`PublisherName`](/specification/datasets/cost_and_usage/columns/publishername.md)
    - Due to definitional conflicts between the Provider and Publisher columns, this column is deprecated and will be removed in a future release.

<br>

## v1.2

<sup>Announced June 2025</sup>

### Added

#### New columns

- `BillingAccountType`
- `InvoiceID`
- `PricingCurrency`
- `PricingCurrencyContractedUnitPrice`
- `PricingCurrencyEffectiveCost`
- `PricingCurrencyListUnitPrice`
- `SubAccountType`

#### New appendix entries

- Added examples for commitment discount flexibility.
- Added examples for SaaS scenarios.

#### New supported features

- Added list of features the specification supports.  See the `supported_features` subfolder for a full list.

#### New metadata column definition properties

- `Deprecated`
- `PreviousColumnName`

### Changed

#### Changed columns

- Normative requirements guidelines have been applied to all columns. While the formatting has changed significantly, the vast majority of such changes are not material unless specifically called out in the below list.
- `AvailabilityZone`
  - Added a requirement that the value must be null when a charge is not specific to an availability zone.
- `BilledCost`
  - Added requirement that the value must be 0 when payments are received by a third-party (e.g., marketplace).
  - Added requirement that the sum of BilledCost for an Invoice ID must match the payable amount on a corresponding invoice.
- `BillingAccountName`
  - Removed requirement of uniqueness within a customer context.
- `ChargeDescription`
  - Changed recommendation to specify maximum length in the Metadata Schema instead of publicly available documentation.
- `CommitmentDiscountQuantity`
  - Revised requirement of value range to allow any valid decimal value.
- `CommitmentDiscountUnit`
  - Revised requirement of nullability to be tied to the nullability of CommitmentDiscountQuantity (e.g., must be null when CommitmentDiscountQuantity is null).
- `ConsumedQuantity`
  - Revised requirement of value range to allow any valid decimal value.
- `ConsumedUnit`
  - Revised requirement of nullability to be tied to the nullability of ConsumedQuantity (e.g., must be null when ConsumedQuantity is null).
- `EffectiveCost`
  - Clarified requirements for aggregation of values.
- `PricingUnit`
  - Revised requirement of nullability to be tied to the nullability of PricingQuantity (e.g., must be null when PricingQuantity is null).
- `RegionName`
  - Revised requirement of nullability to be tied to the nullability of RegionId (e.g., must be null when RegionId is null).
- `ResourceId`
  - Revised requirement for uniqueness: the value must be unique within the provider.
- `ServiceName`
  - Added requirement for mapping the value to a single ServiceCategory or "Other".
  - Added recommendation for mapping the value to a single ServiceSubcategory or "Other".
- `SkuId`
  - Revised column definition to position SkuId as a stable, functional identifier beyond pricing constructs.
  - Revised requirement for presence: the value must be present when the provider supports unit pricing and publishes price lists.
  - Added requirements for a SkuId to be consistent across variations of billing accounts, contracts, and prices.
- `SkuMeter`
  - Revised requirement for presence: the value must be present when the provider supports unit pricing and publishes price lists.
- `SkuPriceDetails`
  - Defined a set of FOCUS-specified property names and units, and added requirements for how they are used.
  - Added requirement that custom properties must prefix names with "x_".
  - Revised requirement for presence: the value must be present when the provider supports unit pricing and publishes price lists.
- `SkuPriceId`
  - Revised requirement for presence: the value must be present when the provider supports unit pricing and publishes price lists.
  - Revised requirement that the value must have a single parent SkuId, removing the prior exception for commitment discount flexibility.
  - Added requirement that the value must be associated with a given resource or service when ChargeCategory is "Usage" or "Purchase".
  - Added requirements for a SkuPriceId to be consistent across variations of billing accounts and contracts.
- `SubAccountName`
  - Revised requirement of nullability to be tied to the nullability of SubAccountId (e.g., must be null when SubAccountId is null).
- `Tags`
  - Resolved bug involving multiple user-defined tag structures.

#### Changed attributes

- `ColumnNamingAndOrdering`
  - Renamed attribute to `ColumnHandling`.
- `CurrencyCodeFormat`
  - Renamed attribute to `CurrencyFormat`.
  - Augmented definition to handle for virtual currencies.

#### Changed appendix entries

- Revised the ordering of appendix entries.
- Moved appendix examples to CSV section.

#### Changed metadata

##### Changed metadata properties

- `ProviderVersion`
  - Renamed field to `DataGeneratorVersion`.

<br>

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

[All 1.1 changes](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/compare/v1.0...v1.1)

<br>

## v1.0

<sup>Announced June 20, 2024</sup>

**Added:**

New use cases:
- Compare Billed Cost per Sub Account to budget

New attributes:
- `String handling`

New columns:
- `ChargeClass`
- `CommitmentDiscountStatus`
- `ContractedCost`
- `ContractedUnitPrice`
- `RegionId`
- `RegionName`

New metadata properties:
- `DataGenerator`

New metadata schema properties:
- `CreationDate`
- `FocusVersion`
- `SchemaId`

New metadata column definition properties:
- `ColumnName`
- `DataType`
- `NumberScale`
- `NumberPrecision`
- `ProviderTagPrefix`
- `StringEncoding`
- `StringMaxLength`

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
| BillingAccountType           | 1.2                     |                   |
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
| InvoiceId                    | 1.2                     |                   |
| InvoiceIssuerName            | 0.5                     |                   |
| ListCost                     | 1.0-preview             |                   |
| ListUnitPrice                | 1.0-preview             |                   |
| PricingCategory              | 1.0-preview             |                   |
| PricingCurrency              | 1.2                     |                   |
| PricingCurrencyContractedUnitPrice | 1.2               |                   |
| PricingCurrencyEffectiveCost | 1.2                     |                   |
| PricingCurrencyListUnitPrice | 1.2                     |                   |
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
| SubAccountType               | 1.2                     |                   |
| Tags                         | 1.0-preview             |                   |
| UsageQuantity                | 1.0-preview             | Renamed to ConsumedQuantity in v1.0 |
| UsageUnit                    | 1.0-preview             | Renamed to ConsumedUnit in v1.0 |

