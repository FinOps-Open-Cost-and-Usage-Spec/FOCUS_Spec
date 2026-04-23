# Correction Handling

## Overview

The Correction Handling attribute defines how [*corrections*](#glossary:correction) to previously delivered [*FOCUS dataset artifacts*](#glossary:dataset-artifact) are represented in subsequent deliveries.

*Corrections* may consist of one or more simultaneous changes, including updates to or omission of previously delivered records, or the addition of new records that supplement previously delivered data within the affected [*delivery scope*](#glossary:delivery-scope) (e.g., temporal grouping such as a [*billing period*](#glossary:billing-period) or non-temporal, logical grouping such as a [*contract*](#glossary:contract)).

*Corrections* may address a variety of operational or technical causes, such as refunds, late-arriving data, rounding errors, delivery errors, and other post-processing adjustments.

Accurate correction handling is essential to ensure the consistency, integrity, and usability of *FOCUS datasets* over time. Depending on the dataset and delivery configuration, it supports a range of key outcomes, including but not limited to:

* Consistency of delivered data - ensuring that delivered data remains consistent and reliable over time, where applicable, including alignment between related *FOCUS datasets* (e.g., [Invoice Detail](#datasets.invoicedetail) records and the underlying [Cost and Usage](#datasets.costandusage) records).
* Data integrity and [*invoice reconciliation*](#glossary:invoice-reconciliation) - ensuring that corrections do not compromise records associated with [*issued invoices*](#glossary:issued-invoice) or [*closed billing periods*](#glossary:closed-billing-period), and that alignment is maintained in accordance with defined *invoice reconciliation* requirements.
* Auditability and traceability - enabling the tracking of delivered data and applied corrections over time, so that changes and their effects can be understood, verified, and correctly reflected in downstream processes (e.g., cost allocation, chargeback, reporting).

See [Appendix: Invoice and Billing Period Handling](#appendix.invoiceandbillingperiodhandling) for details on corrections to *issued invoices* and *closed billing periods*.

### Correction Styles

FOCUS recognizes three styles for handling corrections within subsequent *dataset artifacts*:

| Correction Style | Delivery Mechanism | Correction Style Description                                                                                                                                              |
| ---------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Replacement      | Overwrite          | Previously delivered records are not corrected individually; each delivery provides a complete snapshot and supersedes any previously delivered data within the affected [*delivery scope*](#glossary:delivery-scope). |
| Delta            | Append             | Previously delivered records are preserved; corrections are appended as additive records applied during aggregation and may include supplemental records as needed. |
| Ledger           | Append             | Previously delivered records are preserved; corrections are appended as additive records representing explicit reversals and re-entries, applied during aggregation, and may include supplemental records as needed. |

For more information on delivery mechanisms for *dataset artifacts*, see the [Delivery Handling attribute](#attributes.deliveryhandling).

#### Replacement Corrections

In the Replacement correction style, a *dataset artifact* uses the Overwrite delivery mechanism to provide a complete snapshot of data for a given *delivery scope*, based on the data available at the time of delivery.

Any given *dataset artifact* completely replaces all previous *dataset artifacts* for the same *delivery scope* to reflect updates, additions, or omissions relative to the previous snapshot. The practitioner only needs to reference the most recent *dataset artifact* for a given *delivery scope* in order to see a complete view; all previously delivered *dataset artifacts* for that *delivery scope* are considered obsolete and can be safely ignored.

Given that changes are not presented as separate entries, this style lacks inherent auditability. Dataset artifact size typically increases within a delivery scope as underlying data accumulates, but net data volume is the lowest of the three correction styles as each dataset artifact supersedes previously delivered ones for the same delivery scope.

#### Delta Corrections

In the Delta correction style, a *dataset artifact* uses the Append delivery mechanism to provide additive records for a given *delivery scope*, based on the data available at the time of delivery.

All previously delivered *dataset artifacts* are preserved, and corrections are expressed as additive records that are applied during aggregation. These records effectively increase or decrease values in selected additive metrics (e.g., cost- and quantity-related columns) of previously delivered records, or supplement previously delivered records, all within the same *delivery scope*. The practitioner must reference all *dataset artifacts* delivered for a given *delivery scope* in order to see a complete and accurate view.

Given that only net changes are presented and previously delivered records are not explicitly reversed, the Delta correction style provides limited inherent auditability compared to Ledger corrections. Net data volume increases over time as all delivered dataset artifacts are preserved, and is typically higher compared to Replacement corrections but lower compared to Ledger corrections.

#### Ledger Corrections

In the Ledger correction style, a *dataset artifact* uses the Append delivery mechanism in combination with a double-entry bookkeeping method to provide detailed updates for a given *delivery scope*, based on the data available at the time of delivery. Depending on the nature of the correction, either or both of the following steps may be required: (1) reversal of the original record using a record in which additive metrics (e.g., cost- and quantity-related columns) carry values with the opposite sign, while all other columns match the original; and (2) a new record with corrected values.

All previously delivered *dataset artifacts* are preserved, and corrections are expressed as additive records that reflect explicit reversals and re-entries, applied during aggregation. These records effectively increase or decrease values in selected additive metrics (e.g., cost- and quantity-related columns) of previously delivered records, or supplement previously delivered records, all within the same *delivery scope*. The practitioner must reference all *dataset artifacts* delivered for a given *delivery scope* in order to see a complete and accurate view.

Given that the entire change history is presented, the Ledger correction style provides full inherent auditability. Net data volume increases over time as all delivered dataset artifacts are preserved, and is typically the highest of the three correction styles as each correction requires explicit reversal and re-entry records.

## Requirements

CorrectionHandling MUST adhere to the following requirements:

* *FOCUS dataset* MUST have its styles for representing corrections in *dataset artifacts* documented and accessible to practitioners (including whether Replacement, Delta, or Ledger style is used and under which conditions each style applies).
* *FOCUS dataset* MUST represent a complete snapshot of data for the affected [*delivery scope*](#glossary:delivery-scope) when using [Replacement correction style](#attributes.correctionhandling.overview.correctionstyles.replacementcorrections).
* *FOCUS dataset* MUST include additive records representing corrections within the same *delivery scope* when using [Delta correction style](#attributes.correctionhandling.overview.correctionstyles.deltacorrections).
* *FOCUS dataset* MUST include explicit reversal and re-entry additive records representing corrections within the same *delivery scope* when using [Ledger correction style](#attributes.correctionhandling.overview.correctionstyles.ledgercorrections).

## Attribute ID

CorrectionHandling

## Attribute Name

Correction Handling

## Description

Defines how *corrections* to previously delivered FOCUS *dataset artifacts* are represented in subsequent deliveries.

## Introduced (version)

1.4
