# Correction Handling

## Overview

The Correction Handling attribute defines how [*corrections*](#glossary:correction) to a previously delivered FOCUS [*dataset artifact*](#glossary:dataset-artifact) are represented in a subsequently delivered *dataset artifact*.

Corrections may include some combination of added, updated, or removed *rows*. Corrections may address a variety of operational or technical causes, such as refunds, late-arriving data, rounding errors, delivery errors, and other post-processing adjustments.

Accurate correction handling is essential for a range of business-critical processes, including but not limited to:

* Temporal accuracy - capturing both when the [*charge*](#glossary:charge) was incurred (reflected in [*charge period*](glossary:chargeperiod) columns, i.e., [Charge Period Start](#datasets.costandusage.chargeperiodstart) and [Charge Period End](#datasets.costandusage.chargeperiodend)) and when the correction was invoiced (reflected in [*billing period*](#glossary:billing-period) columns, i.e., [Billing Period Start](#datasets.costandusage.billingperiodstart) and [Billing Period End](#datasets.costandusage.billingperiodend)).
* Financial and legal integrity - ensuring that data presented on [*issued invoices*](#glossary:issued-invoice) remains unchanged and aligned with associated underlying charges provided in the FOCUS dataset artifacts, while any related corrections do not compromise [*invoice reconciliation*](#glossary:invoice-reconciliation).
* Cost allocation and chargeback - attributing corrections to the correct dimensions (e.g., [Billing Account ID](#datasets.costandusage.billingaccountid), [Sub Account ID](#datasets.costandusage.subaccountid), [SKU ID](#datasets.costandusage.skuid), [SKU Price ID](#datasets.costandusage.skupriceid), [Resource ID](#datasets.costandusage.resourceid)) to ensure accurate downstream processing.
* Auditability - tracing the full lifecycle of a *charge* from the original record through all subsequent corrections.

### Correction Styles

FOCUS supports three styles for correcting original records:

| Correction Style | Delivery Mechanism | Correction Style Description                                                                         |
| ---------------- | ------------------ | ---------------------------------------------------------------------------------------------------- |
| Replacement      | Overwrite          | Original records are ignored and replaced by correction records.                                                        |
| Delta            | Append             | Original records are preserved and modified by correction records.                                             |
| Ledger           | Append             | Original records are preserved and decremented/incremented by correction records. |

For more information on delivery mechanisms for *dataset artifacts*, see the [Delivery Handling attribute](#deliveryhandling).

#### Replacement Corrections

In the Replacement correction style, a given *dataset artifact* uses the Overwrite delivery mechanism to provide a complete snapshot of data for a *billing period*, based on the data available at the time of delivery.

Any given *dataset artifact* completely replaces all previous *dataset artifacts* to reflect updates, additions, or omissions relative to the previous snapshot. Therefore, the practitioner only needs to reference the most recent *dataset artifact* for a given *billing period* in order to tell a complete story of *charges*; all previous dataset artifacts for that *billing period* are considered obsolete and can be safely ignored.

Given that changes are not presented as separate entries, this style lacks inherent auditability.

#### Delta Corrections

In the Delta correction style, a given *dataset artifact* uses the Append delivery mechanism to add records that revise or supplement previous *dataset artifacts* within a *billing period*.

In some cases, the correction consists of a new record representing a previously omitted cost. Explicit reversal is not commonly performed, but may be used if the correction itself represents a reversal.

Updates increment or decrement values in selected cost- and quantity-related columns, while all other columns remain unchanged. Therefore, the practitioner must combine all *dataset artifacts* for a given *billing period* in order to tell a complete story of *charges*.

Given that only net changes are presented, this style offers limited inherent auditability.

#### Ledger Corrections

In the Ledger correction style, a given *dataset artifact* uses the Append delivery mechanism in combination with a double-entry bookkeeping method of decrements and increments to represent changes within a *billing period*.  Depending on the nature of the correction, either or both of the following steps may be required: (1) reversal of the original record using a charge in which cost- and quantity-related columns carry values with the opposite sign, while all other columns match the original; and (2) a new record with corrected values.

Updates increment or decrement values in selected cost- and quantity-related columns, while all other columns remain unchanged. Therefore, the practitioner must combine all *dataset artifacts* for a given *billing period* in order to tell a complete story of *charges*.

Given that the entire change history is presented, this style offers full inherent auditability.

### Corrections to Issued Charges

A charge is considered issued when it is associated with an [*issued invoice*](#glossary:issued-invoice).

While corrections to the [*issued charges*](#glossary:issued-charge) (including updates, additions, or omissions) may be permitted, they must not compromise the integrity of the associated *issued invoice*. Only corrections that maintain alignment with the invoice content are acceptable. Any misalignment would invalidate the prior *invoice reconciliation* and undermine the invoice's financial validity.

Corrections to the underlying *issued charges* that do not impact data presented on the associated *issued invoice* are allowed. However, although these corrections do not affect *invoice reconciliation*, they can still result in loss of auditability and traceability, which in turn complicates modifications and mappings required in downstream FinOps activities, such as cost allocation, chargeback, or budgeting. For this reason, such corrections are not preferred and should only be applied when explicitly requested by the end-user.

### Corrections to Closed Billing Periods

A billing period is considered closed when all expected invoices for that timeframe have been issued.

Any necessary corrections to a previously *closed billing period* that require issuing additional invoices are associated with a subsequent *open billing period*, with the charge period indicating when the cost was incurred. This approach establishes a clear temporal boundary between billing cycles, preserving the historical financial accuracy and integrity of closed billing periods while enabling transparent and auditable tracking of corrections in future periods.

## Attribute ID

CorrectionHandling

## Attribute Name

Correction Handling

## Description

Defines how *corrections* to a previously delivered FOCUS *dataset artifact* are represented in a subsequently delivered *dataset artifact*.

## Requirements

All corrections adhere to the following requirements:

* The correction style(s) used to correct FOCUS *dataset artifacts* MUST be documented by the data generator.
* Correction MUST NOT introduce a discrepancy between an *issued invoice* and its associated FOCUS *dataset artifacts*.
* Correction to a previously *closed billing period* that requires issuing additional invoices MUST result in additional charge(s) associated with a subsequent *open billing period*, with the charge period indicating when the cost was incurred.
* Correction delivered using the Append delivery mechanism adheres to the following additional requirements:
  * Correction MUST include exclusively additional charges.
  * Correction MUST NOT include updates or omissions of previously delivered charges.

## Exceptions

* Exceptions to the restrictions on *issued charges*, *issued invoices*, and *closed billing periods* and MAY apply in the following cases:
  * Upon explicit request from the end-user (subject to validation and approval processes).
  * Due to technical issues encountered during or after invoice issuance or billing period closure.

## Introduced (version)

1.3
