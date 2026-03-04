# Column Mapping Documentation

## Overview

Dataset mapping documentation describes the relationship between a data generator's native datasets and corresponding FOCUS datasets. This reference helps practitioners validate the accuracy of FOCUS data, reconcile it against native billing data, and understand the specific definitions used to populate FOCUS fields.

This section provides guidance for data generators who wish to publish mapping documentation. The guidance is informative and does not establish conformance requirements.

## Recommended Content

Mapping documentation should include the following information for each column included in the FOCUS dataset:

| Property | Description |
|----------|-------------|
| FOCUS Column | The FOCUS column identifier (e.g., `BilledCost`) |
| Source Field(s) | Native billing column name(s) that map to this FOCUS column |
| Transform Logic | How the native field value is converted to the FOCUS column value |
| Feature Level | The requirement level for the FOCUS column's inclusion in the FOCUS dataset (Mandatory, Conditional, or Optional) |
| Notes | Additional context, edge cases, or variations |

## Transform Logic Patterns

The following patterns describe common transformation scenarios:

| Pattern | Description | Example |
|---------|-------------|---------|
| Direct | 1:1 mapping with no transformation | `line_item_cost` → `BilledCost` |
| Formula | Calculation or derivation | `UnitPrice * Quantity` |
| Conditional | Logic-based mapping | `If charge_type='RI' then 'Purchase' else 'Usage'` |
| Lookup | Reference to external mapping (include location or link) | `See ServiceCategory mapping table` |
| Not Available | No native equivalent exists | Column populated as null |
| Constant | Fixed value assignment | `ServiceProviderName = 'ACME Cloud'` |
| Composite | Multiple source fields or rows combined | `Sum of line_item_cost where usage_type matches` |

## Example Mapping Entries

The following examples illustrate mapping documentation for common scenarios.

### Direct Mapping

| FOCUS Column | Source Field(s) | Transform Logic | Feature Level | Notes |
|--------------|-----------------|-----------------|---------------|-------|
| BillingPeriodEnd | `bill/BillingPeriodEndDate` | Direct | Mandatory | |

### Conditional Mapping

| FOCUS Column | Source Field(s) | Transform Logic | Feature Level | Notes |
|--------------|-----------------|-----------------|---------------|-------|
| ChargeCategory | `lineItem/LineItemType` | Conditional: `Usage` → Usage, `Fee` → Purchase, `Tax` → Tax, `Credit` → Adjustment | Mandatory | Native terminology may differ from FOCUS terminology. See ChargeCategory mapping table for complete logic |

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
* Pricing model or commitment type (e.g., on-demand, reserved, spot)
* FOCUS version, when mappings change across versions
* Edge cases where native columns map to different FOCUS columns based on context

## Accessibility

Data generators publishing mapping documentation should:

* Make documentation publicly accessible without authentication
* Align version documentation with supported FOCUS versions. 
* Ensure the documentation clearly states which FOCUS version (e.g., 1.0 vs 1.1) it applies to
* Provide clear guidance on where practitioners can locate the documentation (e.g., include a URL in FOCUS metadata or reference it from the provider's FOCUS data export documentation)

## Reference Template

The [FOCUS Conformance Submission Workbook](https://docs.google.com/spreadsheets/d/11s3xr1gUlJt6isrhuYGgaTU7XE5ZPTek/edit?usp=sharing&ouid=105511592610552198421&rtpof=true&sd=true) provides a reference template for mapping documentation. Data generators may use this template or provide equivalent documentation in their preferred format, provided the documentation addresses the recommended content described above. Where feasible, data generators are encouraged to provide mapping documentation in both human-readable and machine-readable formats (e.g., JSON, YAML, CSV).
