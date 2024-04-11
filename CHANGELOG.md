# FinOps Open Cost and Usage Specification Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

**Added:**

- `RegionId` column

**Changed:**

- `Column naming convention` attribute includes the following new provisions:
  - Column IDs should not exceed 50 characters.
- `EffectiveCost` column updated to clarify it does not mix or "blend" costs across multiple charges.
- `Region` column renamed to `RegionName`.
- `Tags` column updated to include:
  - Tag keys that cannot have a value must use a boolean `true` as the tag value.

**Fixed:**

- `CommitmentDiscountType` column constraints were updated to show the column as required to align with the normative text.

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

## Columns History
This table maps the evolution of the billing data, showcasing column introductions and updates from its initial version 0.5 to the comprehensive revisions in "1.0-preview", "1.0" and beyond.

| **Column Title**                  | **Revision Introduced** | **Latest Update**
|-----------------------------------|-------------------|--------------------------|
| Availability Zone                             | 0.5                          |                                          |                  
| Billed Cost                      | 0.5               |                                            |         
| Billing Account ID               | 0.5               |                                          |    
| Billing Account Name             | 0.5               |                                          |    
| Billing Currency                 | 0.5               |                                          |    
| Billing Period End               | 0.5               |                                          |    
| Billing Period Start             | 0.5               |                                          |    
| Charge Category                  | 0.5               |                                          |    
| Charge Description               | 1.0-preview               |                                          |    
| Charge Frequency                 | 1.0-preview              |                                          |    
| Charge Period End                | 0.5               |                                          |    
| Charge Period Start              | 0.5               |                                          |    
| Charge Subcategory               | 1.0-preview              |                                          |    
| Commitment Discount Category     | 1.0-preview               |                                          |    
| Commitment Discount ID           | 1.0-preview              |                                          |    
| Commitment Discount Name         | 1.0-preview               |                                          |    
| Commitment Discount Type         | 1.0-preview             |                                          |    
| Contracted Cost                  | 1.0               |                                          |    
| Contracted Unit Price            | 1.0               |                                          |    
| Effective Cost                   | 0.5               |                                          |    
| Invoice Issuer                   | 0.5              |                                          |    
| List Cost                        | 1.0-preview              |                                          |    
| List Unit Price                  | 1.0-preview               |                                          |    
| Pricing Category                 | 1.0-preview               |                                          |    
| Pricing Quantity                 | 1.0-preview              |                                          |    
| Pricing Unit                     | 1.0-preview               |                                          |    
| Provider                         | 0.5               |                                          |    
| Publisher                        | 0.5               |                                          |    
| Region ID                        | 1.0               |                                          |    
| Region Name                      | 1.0               |                                          |    
| Resource ID                      | 0.5               |                                          |    
| Resource Name                    | 0.5               |                                          |    
| Resource Type                    | 1.0-preview              |                                          |    
| Service Category                 | 0.5               |                                          |    
| Service Name                     | 0.5               |                                          |    
| SKU ID                           | 1.0-preview             |                                          |    
| SKU Price ID                     | 1.0-preview              |                                          |    
| Sub Account ID                   | 0.5               |                                          |    
| Sub Account Name                 | 0.5               |                                          |    
| Tags                             | 1.0-preview               |                                          |    
| Usage Quantity                   | 1.0-preview             |                                          |    
| Usage Unit                       | 1.0-preview              |                                          |    
