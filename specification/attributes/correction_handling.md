# Correction Handling

## Overview

The Correction Handling attribute defines how [*corrections*](#glossary:correction) to previously delivered FOCUS [*dataset artifacts*](#glossary:dataset-artifact) are represented in subsequent deliveries.

*Corrections* may consist of one or more simultaneous changes, including updates to or omission of previously delivered records, or the addition of new records that supplement previously delivered data within the affected [*delivery scope*](#glossary:delivery-scope) (e.g., temporal grouping such as a [*billing period*](#glossary:billing-period) or non-temporal, logical grouping such as a [*contract*](#glossary:contract)). This concept applies across all [*FOCUS datasets*](#glossary:FOCUS-dataset).

Corrections may address a variety of operational or technical causes, such as refunds, late-arriving data, rounding errors, delivery errors, and other post-processing adjustments.

Accurate correction handling is essential to ensure the consistency, integrity, and usability of *FOCUS datasets* over time. Depending on the dataset and delivery configuration, it supports a range of key outcomes, including but not limited to:

* Consistency of delivered data - ensuring that delivered data remains consistent and reliable over time, where applicable, including alignment between related *FOCUS datasets* (e.g., [Invoice Detail](#datasets.invoicedetail) records and the underlying [Cost and Usage](#datasets.costandusage) records).
* Data integrity and [*invoice reconciliation*](#glossary:invoice-reconciliation) - ensuring that corrections do not compromise records associated with [*issued invoices*](#glossary:issued-invoice) and that alignment is maintained in accordance with defined *invoice reconciliation* requirements.
* Auditability and traceability - enabling the tracking of delivered data and applied corrections over time, so that changes and their effects can be understood, verified, and correctly reflected in downstream processes (e.g., cost allocation, chargeback, reporting).

### Correction Styles

FOCUS recognizes three styles for handling corrections within subsequent *dataset artifacts*:

| Correction Style | Delivery Mechanism | Correction Style Description                                                                                                                                              |
| ---------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Replacement      | Overwrite          | Previously delivered records are not corrected individually; each delivery provides a complete snapshot and supersedes any previously delivered data within the affected [*delivery scope*](#glossary:delivery-scope). |
| Delta            | Append             | Previously delivered records are preserved; corrections are appended as additive records applied during aggregation and may include supplemental records as needed. |
| Ledger           | Append             | Previously delivered records are preserved; corrections are appended as additive records representing explicit reversals and re-entries, applied during aggregation, and may include supplemental records as needed. |

For more information on delivery mechanisms for *dataset artifacts*, see the [Delivery Handling attribute](#deliveryhandling).

#### Replacement Corrections

In the Replacement correction style, a *dataset artifact* uses the Overwrite delivery mechanism to provide a complete snapshot of data for a given *delivery scope*, based on the data available at the time of delivery.

Any given *dataset artifact* completely replaces all previous *dataset artifacts* for the same *delivery scope* to reflect updates, additions, or omissions relative to the previous snapshot. The practitioner only needs to reference the most recent *dataset artifact* for a given *delivery scope* in order to see a complete view; all previously delivered *dataset artifacts* for that *delivery scope* are considered obsolete and can be safely ignored.

Given that changes are not presented as separate entries, this style lacks inherent auditability.

#### Delta Corrections

In the Delta correction style, a *dataset artifact* uses the Append delivery mechanism to provide additive records for a given *delivery scope*, based on the data available at the time of delivery.

All previously delivered *dataset artifacts* are preserved, and corrections are expressed as additive records that are applied during aggregation. These records effectively increase or decrease values in selected additive metrics (e.g., cost- and quantity-related columns) of previously delivered records, or supplement previously delivered records, all within the same *delivery scope*. The practitioner must reference all *dataset artifacts* delivered for a given *delivery scope* in order to see a complete and accurate view.

Given that only net changes are presented and previously delivered records are not explicitly reversed, the Delta correction style provides limited inherent auditability compared to Ledger corrections.

#### Ledger Corrections

In the Ledger correction style, a *dataset artifact* uses the Append delivery mechanism in combination with a double-entry bookkeeping method to provide detailed updates for a given *delivery scope*, based on the data available at the time of delivery. Depending on the nature of the correction, either or both of the following steps may be required: (1) reversal of the original record using a record in which additive metrics (e.g., cost- and quantity-related columns) carry values with the opposite sign, while all other columns match the original; and (2) a new record with corrected values.

All previously delivered *dataset artifacts* are preserved, and corrections are expressed as additive records that reflect explicit reversals and re-entries, applied during aggregation. These records effectively increase or decrease values in selected additive metrics (e.g., cost- and quantity-related columns) of previously delivered records, or supplement previously delivered records, all within the same *delivery scope*. The practitioner must reference all *dataset artifacts* delivered for a given *delivery scope* in order to see a complete and accurate view.

Given that the entire change history is presented, the Ledger correction style provides full inherent auditability.

### Corrections to Issued Invoices

Corrections to data in FOCUS Invoice Detail and Cost and Usage *dataset artifacts* associated with an *issued invoice* that would affect the integrity of the *issued invoice* representation or invalidate the *invoice reconciliation* performed by the [*invoice issuer*](#glossary:invoice-issuer) prior to invoice issuance may only be applied if the corresponding [Invoice Status](#datasets.invoicedetail.invoicestatus) (within Invoice Detail *FOCUS dataset*) transitions from "Closed" to "Open". Such a transition must be explicitly requested or approved by the customer to ensure auditability, traceability, and the integrity of *invoice reconciliation*.

Corrections to underlying records that do not impact *invoice reconciliation* are allowed regardless of Invoice Status, but even in this case they may reduce auditability and traceability or affect downstream processes (e.g., cost allocation, chargeback, reporting).

For more details and requirements regarding consistency and integrity of delivered Invoice Detail and Cost and Usage *dataset artifacts* for *issued invoices*, see the [Invoice Handling attribute](#invoicehandling).

### Corrections to Closed Billing Periods

Corrections to previously *closed billing periods* that would require issuing additional [*invoices*](#glossary:invoice) may only be applied if the corresponding [BillingPeriodStatus](#datasets.billingperiod.billingperiodstatus) (within [Billing Period](#datasets.billingperiod) *FOCUS dataset*) transitions from "Closed" to "Open". Such a transition must be explicitly requested or approved by the customer to ensure auditability, traceability, and the integrity of financial reporting.

Corrections that do not impact the integrity of the closed billing period, such as informational or metadata updates, are allowed regardless of BillingPeriodStatus.

If the original closed period is not reopened, corrections that require issuing additional invoices must always be represented in the context of a subsequent *open billing period*, in accordance with the [Invoice Handling attribute](#invoicehandling).

This approach preserves historical financial accuracy, ensures clear temporal boundaries between billing cycles, and guarantees that all corrections are transparently tracked and auditable in future periods.

For more details and requirements regarding consistency and integrity of delivered Billing Period, Invoice Detail and Cost and Usage *dataset artifacts* for *closed billing periods*, see the [Invoice Handling attribute](#invoicehandling).

## Attribute ID

CorrectionHandling

## Attribute Name

Correction Handling

## Description

Defines how *corrections* to previously delivered FOCUS *dataset artifacts* are represented in subsequent deliveries.

## Requirements

CorrectionHandling MUST adhere to the following requirements:

* *FOCUS dataset* MUST have its styles for representing corrections in *dataset artifacts* documented and accessible to practitioners (including whether Replacement, Delta, or Ledger style is used and under which conditions each style applies).
* *FOCUS dataset* MUST represent a complete snapshot of data for the affected *delivery scope* when using Replacement correction style.
* *FOCUS dataset* MUST include additive records representing corrections within the same *delivery scope* when using Delta correction style.
* *FOCUS dataset* MUST include explicit reversal and re-entry additive records representing corrections within the same *delivery scope* when using Ledger correction style.
* *FOCUS dataset* MUST ensure that InvoiceDetail.InvoiceStatus for an *issued invoice* transitions from "Closed" to "Open" only if explicitly requested or approved by the customer.
* *FOCUS dataset* MUST ensure that BillingPeriod.BillingPeriodStatus for a *closed billing period* transitions from "Closed" to "Open" only if explicitly requested or approved by the customer.

## Exceptions

None

## Introduced (version)

1.4
