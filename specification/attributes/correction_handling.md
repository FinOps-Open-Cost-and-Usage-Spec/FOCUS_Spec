# Correction Handling

## Overview

### Definition and Scope of Corrections

Correction Handling attribute defines how updates to previously provided charge records are represented in FOCUS datasets.

**Terminology Note:** The term "Correction" (capitalized) refers specifically to an allowed value in the [ChargeClass](#chargeclass) column, which designates charge records used to correct cost and usage data from a previously invoiced [*billing period*](#glossary:billing-period). In contrast, the Correction Handling attribute covers the broader concept of "corrections" (lowercase), which may include charge records used to correct cost and usage data originally associated with a previously invoiced billing period or an uninvoiced billing period (including both previous and current), as well as the omission of a previously provisioned charge if it is no longer applicable, subject to applicable correction handling restrictions.

Corrections may arise from a variety of operational or technical causes, such as refunds, delayed or missing cost and usage data, rounding errors, post-processing adjustments, etc.

### Business Requirements and Constraints in Invoiced Billing Periods

Accurate correction handling is essential for a range of business-critical processes, including but not limited to:

* Temporal accuracy - capturing both when the charge was incurred (reflected in charge period columns, i.e., Charge Period Start and Charge Period End) and when the correction was invoiced (reflected in billing period columns, i.e., Billing Period Start and Billing Period End columns).
* Financial and legal integrity - preserving original charge records associated with finalized invoices while recording changes to those records separately, as finalized invoices represent binding financial documents requiring immutability and traceability.
* Cost allocation and chargeback - attributing corrections to the correct dimensions (e.g., Billing Account, Sub Account, SKU ID, SKU Price ID, Resource ID).
* Auditability - tracing the full lifecycle of a charge from the original record through all subsequent corrections.

Once an invoice is issued, it serves as the authoritative financial document and is considered finalized and immutable. All charge records associated with an issued invoice are also considered finalized and must remain unchanged (i.e., corrections to finalized charge records, whether as updates, deletions or omissions, are not permitted). Furthermore, no additional charge records may be associated with an invoice once it has been issued. This ensures that issued invoices and their underlying charge records remain immutable for financial, auditing, and compliance purposes.

A billing period is considered invoiced (or closed) once all invoices for that period have been issued and all charge records for that period are finalized. After a billing period is invoiced, no new charge records may be associated with it, and all previously finalized charge records remain unchanged. Any necessary corrections to charges originally incurred in an invoiced billing period must instead be reflected in a subsequent open billing period, with the charge period indicating when the cost was incurred. This provides a clear temporal boundary between billing cycles, preserving immutability while still allowing corrections to be tracked transparently in later billing periods.

### Delivery Mechanisms and Correction Representation

FOCUS supports two cost and usage data delivery mechanisms: Replacement and Append-only.

#### Replacement Mechanism

In the Replacement mechanism, each dataset provides a complete snapshot of cost and usage data for a billing period, based on the data collected up to the time of delivery. Subsequent datasets typically reflect updates, additions, or omissions relative to the previous snapshot. Subsequent datasets typically reflect updates, additions, or omissions relative to the previous snapshot. For uninvoiced billing periods (including both previous and current) this mechanism lacks a built-in audit trail, as records may be updated or omitted. To support traceability in uninvoiced billing periods, the Replacement mechanism should support optional external retention of historical snapshots. For invoiced billing periods, auditability is ensured through immutable finalized records and correction handling rules that prohibit updates, deletions, or omissions.

Subsequent datasets in the Replacement mechanism may include the following:

* Unchanged charge records - carried over unchanged from the previously delivered dataset.
* Updated charge records - overwritten with the latest values.
* Additional charge records - new entries representing either billing period segments not previously reported, or supplements to segments included in the previously delivered dataset (e.g., refunds or delayed cost and usage data).
* Omitted charge records - removed from the dataset because they are no longer applicable.

Corrections in the Replacement mechanism are modeled through updates, additions, or omissions relative to the previous snapshot — with the restriction that corrections to charges originally incurred in previously invoiced billing periods must be represented exclusively through the addition of new records. Updated or omissions of finalized records are not allowed, as they would compromise the immutability of issued invoices and the integrity of audit trails.

#### Append-only Mechanism

In the Append-only mechanism, each dataset appends new records without modifying or removing previously delivered ones. This mechanism inherently supports auditability, as all original and correction records are retained.

Corrections in the Append-only mechanism are represented exclusively by adding new records.

Within the Append-only mechanism, two correction styles are commonly used:

* Ledger-style correction adds records that update or supplement cost and usage data. Updates increment or decrement values in selected cost- and quantity-related columns, while all other columns remain unchanged. In some cases, the correction consists of a new record representing a previously omitted cost. Explicit reversal is not commonly performed, but may be used if the correction itself represents a reversal. This style offers limited audit transparency.
* Accounting-style correction generally follows a two-step representation. Depending on the nature of the correction, either or both of the following steps may be required: (1) reversal of the original record using a charge in which cost- and quantity-related columns carry values with the opposite sign, while all other columns match the original; and (2) a new record with corrected values. This style preserves full correction history.

### Data Integrity

To ensure data integrity, correction records must not result in double counting of any cost- or quantity-related values. This applies regardless of the correction style or delivery mechanism used.

## Attribute ID

CorrectionHandling

## Attribute Name

Correction Handling

## Description

Defines how updates to previously provided [*charges*](#glossary:charge) are represented in FOCUS datasets.

## Requirements

All corrections adhere to the following requirements:

### Invoice and Billing Period Requirements

* Invoice MUST be considered finalized and immutable once issued.
* Once the associated invoice is issued, each underlying *charges* adheres to the following additional requirements:
  * *Charge* MUST be considered finalized and immutable.
  * *Charge* MUST NOT be updated, deleted, or omitted.
* Billing period MUST be considered invoiced and closed once all invoices for that period are issued.
* Additional *charges* MUST NOT be associated with an invoice once it is issued.
* Additional *charges* MUST NOT be associated with a billing period once it is invoiced and closed.

### General Requirements for Corrections

* Correction handling implementation MUST support auditability by enabling traceability from the original record through all subsequent corrections for invoiced billing periods.
* Correction handling implementation MUST ensure that the delivery mechanisms and correction styles in use are documented within the Data Generator documentation.
* ChargeClass MUST be null when the *charge* does not represent a correction to a previously invoiced *billing period*.
* Correction MUST NOT result in double counting of any cost- or quantity-related values.

### Constraints in an Invoiced Billing Period

* Corrections to charges from a previously invoiced and closed billing period adhere to the following additional requirements:
  * ChargeClass MUST be "Correction".
  * Correction MUST NOT replace or omit the original record.
  * Corrected row(s) MUST be assigned to a different InvoiceId than the original record.
  * [BillingPeriodStart](#billingperiodstart) and [BillingPeriodEnd](#billingperiodend) MUST equal the [*inclusive start bound*](#glossary:inclusivestartbound) and [*exclusive end bound*](#glossary:exclusiveendbound) of a subsequent open billing period in which the correction is issued.
  * [ChargePeriodStart](#chargeperiodstart) and [ChargePeriodEnd](#chargeperiodend) MUST equal the *inclusive start bound* and *exclusive end bound* of the period in which the cost was originally incurred.

### Constraints in the Replacement Mechanism

* Replacement mechanism adheres to the following additional requirements:
  * Correction handling implementation SHOULD support optional external retention of historical snapshots to enable traceability in uninvoiced billing periods (including both previous and current).
  * Corrections for previously invoiced billing periods MUST be represented exclusively through the addition of new records.
  * Corrections for uninvoiced billing periods MAY include updates, additions, or omissions.

### Constraints in the Append-only Mechanism

* Append-only mechanism adheres to the following additional requirements:
  * All previously delivered records MUST be retained without modification or deletion.
  * All corrections MUST be represented exclusively by adding new records.

## Exceptions

* Exceptions to the restrictions on issued invoices, invoiced billing periods, and finalized charge records MAY apply in the following cases:
  * Upon explicit request from the end-user (subject to validation and approval processes).
  * Due to technical issues encountered during or after invoice issuance or billing period closure.

## Introduced (version)

1.3
