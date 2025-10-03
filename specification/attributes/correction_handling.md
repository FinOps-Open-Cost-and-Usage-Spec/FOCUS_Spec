# Correction Handling

## Overview

The Correction Handling attribute defines how [*corrections*](#glossary:correction) to a previously delivered [*dataset artifact*](#glossary:dataset-artifact) are represented in a subsequently delivered *dataset artifact*.

Corrections may include some combination of added, updated, or removed *charges*. Corrections may address a variety of operational or technical causes, such as refunds, late-arriving data, rounding errors, delivery errors, and other post-processing adjustments.

### Correction Mechanisms

FOCUS supports two delivery mechanisms: Overwrite and Append.  For more information, see the [Delivery Handling attribute](#deliveryhandling).

FOCUS supports three correction mechanisms:

* Replacement. Existing records are replaced by new records.
* Delta. Existing records are preserved, modified by new records. 
* Ledger. Existing records are preserved, fully debited by new records, and then credited by more new records.

#### Replacement Corrections

In the Replacement correction mechanism, a given *dataset artifact* provides a complete snapshot of data for a *billing period*, based on the data available at the time of delivery. Subsequent dataset artifacts use the Overwrite delivery mechanism and completely replace all previous *dataset artifacts* to reflect updates, additions, or omissions relative to the previous snapshot. This mechanism lacks inherent auditability.

#### Delta Corrections

In the Revision correction mechanism, a given *dataset artifact* uses the Append delivery mechanism to add records that update or supplement previous *dataset artifacts* within a *billing period*. Updates increment or decrement values in selected cost- and quantity-related columns, while all other columns remain unchanged. In some cases, the correction consists of a new record representing a previously omitted cost. Explicit reversal is not commonly performed, but may be used if the correction itself represents a reversal. This mechanism offers limited inherent auditability.

### Ledger Corrections

In the Ledger correction mechanism, a given *dataset artifact* uses the Append delivery mechanism in combination with a double-entry bookkeeping style of debits and credits to represent changes within a *billing period*.  Depending on the nature of the correction, either or both of the following steps may be required: (1) reversal of the original record using a charge in which cost- and quantity-related columns carry values with the opposite sign, while all other columns match the original; and (2) a new record with corrected values. This mechanism offers full inherent auditability.




#### Append-only Correction Mechanism

In the Append-only correction mechanism, a subsequent dataset artifact appends new records without modifying or removing previously delivered ones. Corrections in the Append-only mechanism are represented exclusively by adding new records. This mechanism inherently supports auditability, as all original and correction records are retained.

Within the Append-only mechanism, two correction styles are commonly used:

* Ledger-style correction adds records that update or supplement cost and usage data. Updates increment or decrement values in selected cost- and quantity-related columns, while all other columns remain unchanged. In some cases, the correction consists of a new record representing a previously omitted cost. Explicit reversal is not commonly performed, but may be used if the correction itself represents a reversal. This style offers limited audit transparency.
* Accounting-style correction generally follows a two-step representation. Depending on the nature of the correction, either or both of the following steps may be required: (1) reversal of the original record using a charge in which cost- and quantity-related columns carry values with the opposite sign, while all other columns match the original; and (2) a new record with corrected values. This style preserves full correction history.


For *closed billing periods*, auditability is ensured through correction handling rules that typically prohibit updates, deletions, or omissions to *charges* associated with an *issued invoice* if they would impact reconciled invoice data.








Correction Handling attribute defines how [*corrections*](#glossary:correction), i.e., modifications (including updates, additions, or omissions) to previously provided [*charges*](#glossary:charge), whether from an [*open billing period*](#glossary:open-billing-period) or a [*closed billing period*](#glossary:closed-billing-period), are represented in FOCUS Cost and Usage dataset artifacts.

**Terminology Note:** The term "Correction" (capitalized) refers specifically to an allowed value in the [ChargeClass](#chargeclass) column, which designates charge records used to correct cost and usage data from a previously *closed billing period*. In contrast, the Correction Handling attribute covers the broader concept of "corrections" (lowercase), which may include charge records used to correct cost and usage data originally associated with a previously *closed billing period* or an *open billing period* (including both previous and current), as well as the omission of a previously provisioned charge if it is no longer applicable.

Corrections may arise from a variety of operational or technical causes, such as refunds, delayed or missing cost and usage data, rounding errors, post-processing adjustments, etc.

### Business Requirements and Constraints in Closed Billing Periods

Accurate correction handling is essential for a range of business-critical processes, including but not limited to:

* Temporal accuracy - capturing both when the charge was incurred (reflected in [*charge period*](glossary:chargeperiod) columns, i.e., [Charge Period Start](#chargeperiodstart) and [Charge Period End](#chargeperiodend)) and when the correction was invoiced (reflected in [*billing period*](#glossary:billing-period) columns, i.e., [Billing Period Start](#billingperiodstart) and [Billing Period End](#billingperiodend)).
* Financial and legal integrity - ensuring that data presented on issued invoices remains unchanged and aligned with associated underlying charges provided in the FOCUS Cost and Usage dataset artifacts, while any related corrections do not compromise invoice reconciliation.
* Cost allocation and chargeback - attributing corrections to the correct dimensions (e.g., Billing Account, Sub Account, SKU ID, SKU Price ID, Resource ID) to ensure accurate downstream processing.
* Auditability - tracing the full lifecycle of a charge from the original record through all subsequent corrections.

### Delivery Mechanisms and Correction Representation

FOCUS supports two cost and usage data delivery mechanisms: Replacement and Append-only. These mechanisms are not mutually exclusive and hybrid implementations are common, allowing Data Generators to meet specific delivery and auditability requirements.

#### Replacement Mechanism

In the Replacement mechanism, each dataset artifact provides a complete snapshot of cost and usage data for a *billing period*, based on the data collected up to the time of delivery. Subsequent dataset artifacts typically reflect updates, additions, or omissions relative to the previous snapshot. This mechanism lacks a built-in audit trail, as records may be updated or omitted. The Replacement mechanism should support external retention of historical snapshots as an optional capability, allowing end-users to enable traceability. For *closed billing periods*, auditability is ensured through correction handling rules that prohibit updates, deletions, or omissions to charges associated with an issued invoice if they would impact reconciled invoice data.

Subsequent dataset artifacts in the Replacement mechanism may include the following:

* Unchanged records are carried over.
* Updated records overwrite previous values.
* Additional records supplement previously delivered data.
* Omitted records are removed if no longer applicable.

#### Append-only Mechanism

In the Append-only mechanism, each dataset artifact appends new records without modifying or removing previously delivered ones. This mechanism inherently supports auditability, as all original and correction records are retained.

Corrections in the Append-only mechanism are represented exclusively by adding new records.

Within the Append-only mechanism, two correction styles are commonly used:

* Ledger-style correction adds records that update or supplement cost and usage data. Updates increment or decrement values in selected cost- and quantity-related columns, while all other columns remain unchanged. In some cases, the correction consists of a new record representing a previously omitted cost. Explicit reversal is not commonly performed, but may be used if the correction itself represents a reversal. This style offers limited audit transparency.
* Accounting-style correction generally follows a two-step representation. Depending on the nature of the correction, either or both of the following steps may be required: (1) reversal of the original record using a charge in which cost- and quantity-related columns carry values with the opposite sign, while all other columns match the original; and (2) a new record with corrected values. This style preserves full correction history.

### Data Integrity

To ensure data integrity, correction records must not result in double counting of any cost- or quantity-related values. This applies regardless of the correction style or delivery mechanism used.

### Corrections to Issued Charges

While corrections to the [*issued charges*](#glossary:issued-charge) (including updates, additions, or omissions) may be permitted, they must not compromise the integrity of the associated *issued invoice*. Only corrections that maintain alignment with the invoice content are acceptable. Any misalignment would invalidate the prior *invoice reconciliation* and undermine the invoice's financial validity.

Corrections to the underlying *issued charges* that do not impact data presented on the associated *issued invoice* are allowed. However, although these corrections do not affect *invoice reconciliation*, they can still result in loss of auditability and traceability, which in turn complicates modifications and mappings required in downstream FinOps activities, such as cost allocation, chargeback, or budgeting. For this reason, such corrections are not preferred and should only be applied when explicitly requested by the end-user.

### Corrections to Closed Billing Periods

Any necessary corrections to previously *closed billing period* that require issuing additional invoices must be result in additional charge(s) associated with a subsequent *open billing period*, with the charge period indicating when the cost was incurred. (An exception to this rule may apply if explicitly requested by the end-user.)

This approach establishes a clear temporal boundary between billing cycles, preserving the historical financial accuracy and integrity of closed billing periods while enabling transparent and auditable tracking of corrections in future periods.

## Attribute ID

CorrectionHandling

## Attribute Name

Correction Handling

## Description

Defines how modifications (including updates, additions, or omissions) to previously provided *charges*, whether from an *open billing period* or a *closed billing period*, are represented in FOCUS Cost and Usage dataset artifacts.

## Requirements

All corrections adhere to the following requirements:

* Correction handling implementation MUST ensure that the delivery mechanisms and correction styles in use are documented by the Data Generator.
* Correction handling implementation SHOULD support external retention of historical snapshots as an optional capability when Replacement mechanism is used, allowing end-users to enable traceability.
* Correction MUST NOT result in double counting of any cost- or quantity-related values.
* Correction MAY consist of multiple simultaneous modifications, each representing an update or omission of a previously delivered charge, or the addition of a new charge.
* Correction to *issued charges* adheres to the following additional requirements:
  * Correction MUST NOT be applied when it results in discrepancies with the cost and usage data presented on the associated *issued invoice*.
  * Correction SHOULD NOT be applied when it does not results in discrepancies with the cost and usage data presented on the associated *issued invoice*, but still affects downstream FinOps capabilities (e.g., chargeback).
  * Correction MAY include additional charges associated with a different InvoiceId than the original charges.
  * Correction MAY include additional charges associated with a different billing period than the original charges.
* Correction to previously *closed billing period* that requires issuing additional invoices MUST result in additional charge(s) associated with a subsequent *open billing period*, with the charge period indicating when the cost was incurred.
* Correction delivered using the Append-only mechanism adheres to the following additional requirements:
  * Correction MUST include exclusively additional charges.
  * Correction MUST NOT include updates or omissions of previously delivered charges.

## Exceptions

* Exceptions to the restrictions on *issued charges*, *issued invoices*, and *closed billing periods* and MAY apply in the following cases:
  * Upon explicit request from the end-user (subject to validation and approval processes).
  * Due to technical issues encountered during or after invoice issuance or billing period closure.

## Introduced (version)

1.3
