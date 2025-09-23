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

### Delivery Mechanisms and Correction Representation

FOCUS supports two cost and usage data delivery mechanisms: Replacement and Append-only. These mechanisms are not mutually exclusive and hybrid implementations are common, allowing Data Generators to meet specific delivery and auditability requirements.

#### Replacement Mechanism

In the Replacement mechanism, each dataset artifact provides a complete snapshot of cost and usage data for a billing period, based on the data collected up to the time of delivery. Subsequent dataset artifacts typically reflect updates, additions, or omissions relative to the previous snapshot. This mechanism lacks a built-in audit trail, as records may be updated or omitted. The Replacement mechanism should support external retention of historical snapshots as an optional capability, allowing end-users to enable traceability. For invoiced billing periods, auditability is ensured through correction handling rules that prohibit updates, deletions, or omissions to charges associated with an issued invoice if they would impact reconciled invoice data.

Subsequent dataset artifacts in the Replacement mechanism may include the following:

* Unchanged records are carried over.
* Updated records overwrite previous values.
* Additional records supplement previously delivered data.
* Omitted records are removed if no longer applicable.

Corrections to charges associated with an issued invoice that impact reconciled invoice data must be represented exclusively through the addition of new records associated with a subsequent open billing period, with the charge period indicating when the cost was incurred.

#### Append-only Mechanism

In the Append-only mechanism, each dataset artifact appends new records without modifying or removing previously delivered ones. This mechanism inherently supports auditability, as all original and correction records are retained.

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

* Correction handling implementation MUST support auditability by enabling traceability from the original record through all subsequent corrections for invoiced billing periods.
* Correction handling implementation MUST ensure that the delivery mechanisms and correction styles in use are documented within the Data Generator documentation.
* ChargeClass MUST be null when the *charge* does not represent a correction to a previously invoiced *billing period*.
* Correction MUST NOT result in double counting of any cost- or quantity-related values.
* Corrections to charges associated with an issued invoice that impact *reconciled invoice* data adhere to the following additional requirements:
  * ChargeClass MUST be "Correction".
  * Correction MUST NOT replace or omit the original record.
  * Corrected row(s) MUST be assigned to a different InvoiceId than the original record.
  * [BillingPeriodStart](#billingperiodstart) and [BillingPeriodEnd](#billingperiodend) MUST equal the [*inclusive start bound*](#glossary:inclusivestartbound) and [*exclusive end bound*](#glossary:exclusiveendbound) of a subsequent open billing period in which the correction is issued.
  * [ChargePeriodStart](#chargeperiodstart) and [ChargePeriodEnd](#chargeperiodend) MUST equal the *inclusive start bound* and *exclusive end bound* of the period in which the cost was originally incurred.
* Corrections to charges associated with an issued invoice that do not impact *reconciled invoice* data but do affect dimensions and metrics used in downstream FinOps capabilities subject to financial data, such as chargeback, SHOULD adhere to the same requirements as corrections that impact *reconciled invoice* data, unless explicitly requested by the end-user.
* Replacement mechanism adheres to the following additional requirements:
  * Corrections for previously invoiced billing periods that impact *reconciled invoice* data MUST be represented exclusively through the addition of new records.
  * Corrections for previously invoiced billing periods that do not impact *reconciled invoice* data but affect dimensions and metrics used in downstream FinOps capabilities (e.g., chargeback) SHOULD be represented exclusively through the addition of new records, unless explicitly requested otherwise by the end-user.
  * Correction handling implementation SHOULD support external retention of historical snapshots as an optional capability, allowing end-users to enable traceability.
  * Corrections for uninvoiced billing periods MAY include updates, additions, or omissions.
* Append-only mechanism adheres to the following additional requirements:
  * All previously delivered records MUST be retained without modification or deletion.
  * All corrections MUST be represented exclusively by adding new records.

## Exceptions

None

## Introduced (version)

1.3
