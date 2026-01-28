# Column Mapping Documentation

## Overview

Column mapping documentation describes how a data generator transforms native billing data into FOCUS columns. This documentation helps practitioners validate FOCUS data accuracy, reconcile discrepancies with native billing, and understand transformation logic.

This section provides guidance for data generators who wish to publish mapping documentation. The guidance is informative and does not establish conformance requirements.

## Recommended Content

Mapping documentation should include the following information for each FOCUS column present in the data generator's dataset:

| Property | Description |
|----------|-------------|
| FOCUS Column | The FOCUS column identifier (e.g., `BilledCost`) |
| Source Field(s) | Native billing column name(s) that map to this FOCUS column |
| Transform Logic | Description of transformation applied |
| Feature Level | Mandatory, Conditional, or Recommended |
| Notes | Additional context, edge cases, or variations |

## Transform Logic Patterns

The following patterns describe common transformation scenarios:

| Pattern | Description | Example |
|---------|-------------|---------|
| Direct | 1:1 mapping with no transformation | `line_item_cost` → `BilledCost` |
| Formula | Calculation or derivation | `UnitPrice * Quantity` |
| Conditional | Logic-based mapping | `If charge_type='RI' then 'Purchase' else 'Usage'` |
| Lookup | Reference to external mapping | `See ServiceCategory mapping table` |
| Not Available | No native equivalent exists | Column populated as null |
| Constant | Fixed value assignment | `ProviderName = 'ACME Cloud'` |

## Example Mapping Entries

The following examples illustrate mapping documentation for common scenarios.

### Direct Mapping

| FOCUS Column | Source Field(s) | Transform Logic | Feature Level | Notes |
|--------------|-----------------|-----------------|---------------|-------|
| BillingPeriodEnd | `bill/BillingPeriodEndDate` | Direct | Mandatory | |

### Conditional Mapping

| FOCUS Column | Source Field(s) | Transform Logic | Feature Level | Notes |
|--------------|-----------------|-----------------|---------------|-------|
| ChargeCategory | `lineItem/LineItemType` | Conditional: `Usage` → Usage, `Fee` → Purchase, `Tax` → Tax, `Credit` → Adjustment | Mandatory | See ChargeCategory mapping table for complete logic |

### Formula Mapping

| FOCUS Column | Source Field(s) | Transform Logic | Feature Level | Notes |
|--------------|-----------------|-----------------|---------------|-------|
| ListCost | `pricing/publicOnDemandRate`, `lineItem/UsageAmount` | Formula: `publicOnDemandRate * UsageAmount` | Mandatory | |

### Not Available

| FOCUS Column | Source Field(s) | Transform Logic | Feature Level | Notes |
|--------------|-----------------|-----------------|---------------|-------|
| CapacityReservationId | — | Not Available | Conditional | Native billing does not expose capacity reservation identifiers |

## Documentation Variations

Data generators should document variations in mapping logic that depend on:

* Billing account type or agreement structure
* Product line or service family
* FOCUS version, when mappings change across versions
* Edge cases where native columns map to different FOCUS columns based on context

## Accessibility

Data generators publishing mapping documentation should:

* Make documentation publicly accessible without authentication
* Version documentation to align with supported FOCUS versions
* Provide clear guidance on where practitioners can locate the documentation

## Reference Template

The [FOCUS Conformance Submission Workbook](https://docs.google.com/spreadsheets/d/11s3xr1gUlJt6isrhuYGgaTU7XE5ZPTek/edit?usp=sharing&ouid=105511592610552198421&rtpof=true&sd=true) provides a reference template for mapping documentation. Data generators may use this template or provide equivalent documentation in their preferred format, provided the documentation addresses the recommended content described above.
