# Correction Handling

## Overview

The Correction Handling attribute defines how [*corrections*](#glossary:correction) to previously delivered FOCUS [*dataset artifacts*](#glossary:dataset-artifact) are represented in subsequent deliveries.

*Corrections* may consist of one or more simultaneous changes, including updates to or omission of previously delivered records, or the addition of new records that supplement previously delivered data within the affected [*delivery scope*](#glossary:delivery-scope) (e.g., temporal grouping such as a [*billing period*](#glossary:billing-period) or non-temporal, logical grouping such as a [*contract*](#glossary:contract)). This concept applies across all FOCUS datasets.

Corrections may address a variety of operational or technical causes, such as refunds, late-arriving data, rounding errors, delivery errors, and other post-processing adjustments.

Accurate correction handling is essential to ensure the consistency, integrity, and usability of FOCUS datasets over time. Depending on the dataset and delivery configuration, it supports a range of key outcomes, including but not limited to:

* Consistency of delivered data – ensuring that delivered data remains consistent and reliable over time, where applicable, including alignment between related FOCUS datasets (e.g., Invoice Detail records and the underlying Cost and Usage records).
* Data integrity and [*invoice reconciliation*](#glossary:invoice-reconciliation) – ensuring that corrections do not compromise records associated with issued invoices and that alignment is maintained in accordance with defined *invoice reconciliation* requirements.
* Auditability and traceability – enabling the tracking of delivered data and applied corrections over time, so that changes and their effects can be understood, verified, and correctly reflected in downstream processes (e.g., cost allocation, chargeback, reporting).

### Correction Styles

FOCUS recognizes three styles for handling corrections within subsequent dataset artifacts:

| Correction Style | Delivery Mechanism | Correction Style Description                                                                                                                                              |
| ---------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Replacement      | Overwrite          | Previously delivered records are not corrected individually; each delivery provides a complete snapshot and supersedes any previously delivered data within the affected [*delivery scope*](#glossary:delivery-scope). |
| Delta            | Append             | Previously delivered records are preserved; corrections are appended as additive adjustment records applied during aggregation and may include supplemental records as needed. |
| Ledger           | Append             | Previously delivered records are preserved; corrections are appended as explicit reversal and re-entry records applied during aggregation and may include supplemental records as needed. |

For more information on delivery mechanisms for *dataset artifacts*, see the [Delivery Handling attribute](#deliveryhandling).

#### Replacement Corrections

In the Replacement correction style, a *dataset artifact* uses the Overwrite delivery mechanism to provide a complete snapshot of data for a given *delivery scope*, based on the data available at the time of delivery.

Any given *dataset artifact* completely replaces all previous *dataset artifacts* for the same *delivery scope* to reflect updates, additions, or omissions relative to the previous snapshot. The practitioner only needs to reference the most recent *dataset artifact* for a given *delivery scope* in order to see a complete view; all previously delivered *dataset artifacts* for that *delivery scope* are considered obsolete and can be safely ignored.

Given that changes are not presented as separate entries, this style lacks inherent auditability.

#### Delta Corrections

In the Delta correction style, a *dataset artifact* uses the Append delivery mechanism to provide incremental updates to data for a given delivery scope, based on the data available at the time of delivery.

All previously delivered *dataset artifacts* are preserved, and corrections are expressed as incremental adjustment records that are applied during aggregation. These records effectively increase or decrease values in selected additive metrics (e.g., cost- and quantity-related columns) of previously delivered records, or supplement previously delivered records, all within the same *delivery scope*. The practitioner must reference all *dataset artifacts* delivered for a given *delivery scope* in order to see a complete and accurate view.

Given that only net changes are presented and previously delivered records are not explicitly reversed, the Delta correction style provides limited inherent auditability compared to Ledger corrections.

#### Ledger Corrections

In the Ledger correction style, a *dataset artifact* uses the Append delivery mechanism in combination with a double-entry bookkeeping method to provide detailed updates for a given delivery scope, based on the data available at the time of delivery. Depending on the nature of the correction, either or both of the following steps may be required: (1) reversal of the original record using a record in which additive metrics (e.g., cost- and quantity-related columns) carry values with the opposite sign, while all other columns match the original; and (2) a new record with corrected values.

All previously delivered dataset artifacts are preserved, and corrections are expressed as incremental records that reflect explicit reversals and re-entries, applied during aggregation. These records effectively increase or decrease values in selected additive metrics (e.g., cost- and quantity-related columns) of previously delivered records, or supplement previously delivered records, all within the same delivery scope. The practitioner must reference all *dataset artifacts* delivered for a given *delivery scope* in order to see a complete and accurate view.

Given that the entire change history is presented, the Ledger correction style provides full inherent auditability.

### Corrections to Issued Invoices

While corrections to data in FOCUS Invoice Detail and Cost and Usage dataset artifacts associated with an [*issued invoice*](#glossary:issued-invoice) may be permitted, they must not compromise the integrity of the *issued invoice* representation. Any correction that invalidates the *invoice reconciliation* performed by the [*invoice issuer*](#glossary:invoice-issuer) prior to invoice issuance would undermine the consistency and integrity of delivered FOCUS dataset artifacts. Corrections that would have this effect are therefore prohibited for *issued invoices*, unless explicitly requested by the end-user.

Corrections to underlying records that do not impact the *invoice reconciliation* are permitted. However, even when *invoice reconciliation* remains intact, such corrections can reduce auditability and traceability and may affect downstream processes (e.g., cost allocation, chargeback, reporting), with more significant implications for closed billing periods.

### Corrections to Closed Billing Periods

Corrections to a previously *closed billing period* that require issuing additional invoices must be handled in the context of a subsequent *open billing period*. This approach preserves the historical financial accuracy and integrity of closed billing periods, establishes a clear temporal boundary between billing cycles, and ensures that such corrections are transparently tracked and auditable in future periods.

## Attribute ID

CorrectionHandling

## Attribute Name

Correction Handling

## Description

Defines how *corrections* to previously delivered FOCUS *dataset artifacts* are represented in subsequent deliveries.

## Requirements

All corrections adhere to the following requirements:

* The correction style(s) used to correct FOCUS *dataset artifacts* MUST be documented by the data generator.
* Correction MUST NOT introduce a discrepancy between an *issued invoice* and its associated FOCUS *dataset artifacts*.
* Correction to a previously *closed billing period* that requires issuing additional invoices MUST result in additional charge(s) associated with a subsequent *open billing period*, with the charge period indicating when the cost was incurred.
* Correction delivered using the Append delivery mechanism adheres to the following additional requirements:
  * Correction MUST include exclusively additional charges.
  * Correction MUST NOT include updates or omissions of previously delivered charges.

* Dataset instance MUST have its styles for representing corrections in Dataset Instance Artifacts documented and accessible to practitioners (including whether Replacement, Delta or Ledger is used and under which conditions).
* Dataset Instance MUST NOT deliver correction that invalidates the *invoice reconciliation* when [InvoiceStatus]((#datasets.invoicedetail.invoicestatus)) is "Closed" for a given InvoiceId.
* When including correction acssociated to *closed billing period* Dataset instance adheres to the following additional requirements:
  * Dataset instance MUST NOT deliver records that results in issuing additional invoices for the given billing period.
  * Dataset instance MAY deliver one or more records that results in issuing additional invoices for subsequent *open billing period*.

## Exceptions

* Exceptions to the restrictions on *issued charges*, *issued invoices*, and *closed billing periods* and MAY apply in the following cases:
  * Upon explicit request from the end-user (subject to validation and approval processes).
  * Due to technical issues encountered during or after invoice issuance or billing period closure.

## Introduced (version)

1.4
