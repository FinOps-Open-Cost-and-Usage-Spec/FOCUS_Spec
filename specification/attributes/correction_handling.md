# Correction Handling

## Overview

The [Correction Handling](#attr) attribute defines how [corrections](#term) to previously delivered [FOCUS dataset artifacts](#term:dataset-artifact) are represented in subsequent deliveries.

[Corrections](#term) may consist of one or more simultaneous changes, including updates to or omission of previously delivered records, or the addition of new records that supplement previously delivered data within the affected [delivery scope](#term) (e.g., temporal grouping such as a [billing period](#term) or non-temporal, logical grouping such as a [contract](#term)).

[Corrections](#term) may address a variety of operational or technical causes, such as refunds, late-arriving data, rounding errors, delivery errors, and other post-processing adjustments.

Accurate correction handling is essential to ensure the consistency, integrity, and usability of [FOCUS datasets](#term) over time. Depending on the dataset and delivery configuration, it supports a range of key outcomes, including but not limited to:

* Consistency of delivered data - ensuring that delivered data remains consistent and reliable over time, where applicable, including alignment between related [FOCUS datasets](#term) (e.g., [Invoice Detail](#ds) records and the underlying [Cost and Usage](#ds) records).
* Data integrity and [invoice reconciliation](#term) - ensuring that corrections do not compromise records associated with [issued invoices](#term) or [closed billing periods](#term), and that alignment is maintained in accordance with defined [invoice reconciliation](#term) requirements.
* Auditability and traceability - enabling the tracking of delivered data and applied corrections over time, so that changes and their effects can be understood, verified, and correctly reflected in downstream processes (e.g., cost allocation, chargeback, reporting).

See [Appendix: Invoice and Billing Period Handling](#appendix.invoiceandbillingperiodhandling) for details on corrections to [issued invoices](#term) and [closed billing periods](#term).

### Correction Styles

FOCUS recognizes three styles for handling corrections within subsequent [dataset artifacts](#term):

| Correction Style | Delivery Mechanism | Correction Style Description                                                                                                                                              |
| ---------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Replacement      | Overwrite          | Previously delivered records are not corrected individually; each delivery provides a complete snapshot and supersedes any previously delivered data within the affected [*delivery scope*](#glossary:delivery-scope). |
| Delta            | Append             | Previously delivered records are preserved; corrections are appended as additive records applied during aggregation and may include supplemental records as needed. |
| Ledger           | Append             | Previously delivered records are preserved; corrections are appended as additive records representing explicit reversals and re-entries, applied during aggregation, and may include supplemental records as needed. |

For more information on delivery mechanisms for [dataset artifacts](#term), see the [Delivery Handling attribute](#attr:DeliveryHandling).

#### Replacement Corrections

In the Replacement correction style, a [dataset artifact](#term) uses the Overwrite delivery mechanism to provide a complete snapshot of data for a given [delivery scope](#term), based on the data available at the time of delivery.

Any given [dataset artifact](#term) completely replaces all previous [dataset artifacts](#term) for the same [delivery scope](#term) to reflect updates, additions, or omissions relative to the previous snapshot. The practitioner only needs to reference the most recent [dataset artifact](#term) for a given [delivery scope](#term) in order to see a complete view; all previously delivered [dataset artifacts](#term) for that [delivery scope](#term) are considered obsolete and can be safely ignored.

Given that changes are not presented as separate entries, this style lacks inherent auditability. Dataset artifact size typically increases within a delivery scope as underlying data accumulates, but net data volume is the lowest of the three correction styles as each dataset artifact supersedes previously delivered ones for the same delivery scope.

#### Delta Corrections

In the Delta correction style, a [dataset artifact](#term) uses the Append delivery mechanism to provide additive records for a given [delivery scope](#term), based on the data available at the time of delivery.

All previously delivered [dataset artifacts](#term) are preserved, and corrections are expressed as additive records that are applied during aggregation. These records effectively increase or decrease values in selected additive metrics (e.g., cost- and quantity-related columns) of previously delivered records, or supplement previously delivered records, all within the same [delivery scope](#term). The practitioner must reference all [dataset artifacts](#term) delivered for a given [delivery scope](#term) in order to see a complete and accurate view.

Given that only net changes are presented and previously delivered records are not explicitly reversed, the Delta correction style provides limited inherent auditability compared to Ledger corrections. Net data volume increases over time as all delivered dataset artifacts are preserved, and is typically higher compared to Replacement corrections but lower compared to Ledger corrections.

#### Ledger Corrections

In the Ledger correction style, a [dataset artifact](#term) uses the Append delivery mechanism in combination with a double-entry bookkeeping method to provide detailed updates for a given [delivery scope](#term), based on the data available at the time of delivery. Depending on the nature of the correction, either or both of the following steps may be required: (1) reversal of the original record using a record in which additive metrics (e.g., cost- and quantity-related columns) carry values with the opposite sign, while all other columns match the original; and (2) a new record with corrected values.

All previously delivered [dataset artifacts](#term) are preserved, and corrections are expressed as additive records that reflect explicit reversals and re-entries, applied during aggregation. These records effectively increase or decrease values in selected additive metrics (e.g., cost- and quantity-related columns) of previously delivered records, or supplement previously delivered records, all within the same [delivery scope](#term). The practitioner must reference all [dataset artifacts](#term) delivered for a given [delivery scope](#term) in order to see a complete and accurate view.

Given that the entire change history is presented, the Ledger correction style provides full inherent auditability. Net data volume increases over time as all delivered dataset artifacts are preserved, and is typically the highest of the three correction styles as each correction requires explicit reversal and re-entry records.

## Requirements

Dataset conforming to [CorrectionHandling](#attr) attribute MUST adhere to the following requirements:

* [FOCUS dataset](#term) MUST have its styles for representing corrections in [dataset artifacts](#term) documented and accessible to practitioners (including whether Replacement, Delta, or Ledger style is used and under which conditions each style applies).
* [FOCUS dataset](#term) MUST represent a complete snapshot of data for the affected [delivery scope](#term) when using [Replacement correction style](#attributes.correctionhandling.overview.correctionstyles.replacementcorrections).
* [FOCUS dataset](#term) MUST include additive records representing corrections within the same [delivery scope](#term) when using [Delta correction style](#attributes.correctionhandling.overview.correctionstyles.deltacorrections).
* [FOCUS dataset](#term) MUST include explicit reversal and re-entry additive records representing corrections within the same [delivery scope](#term) when using [Ledger correction style](#attributes.correctionhandling.overview.correctionstyles.ledgercorrections).

## Attribute ID

CorrectionHandling

## Attribute Name

Correction Handling

## Description

Defines how [corrections](#term) to previously delivered FOCUS [dataset artifacts](#term) are represented in subsequent deliveries.

## Version Introduced

1.4
