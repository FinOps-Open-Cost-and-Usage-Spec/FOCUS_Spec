# Correction Handling

Correction Handling attribute defines how updates to previously provided charge records are represented in FOCUS datasets.

**Terminology Note:** The term "Correction" (capitalized) refers specifically to an allowed value in the [ChargeClass](#chargeclass) column, which designates charge records used to correct cost and usage data from a previously invoiced [*billing period*](#glossary:billing-period). In contrast, the Correction Handling attribute covers the broader concept of "corrections" (lowercase), which includes charge records used to correct cost and usage data originally associated with a previously invoiced billing period, an uninvoiced billing period, or the current billing period, as well as the omission of a previously provisioned charge if it is no longer applicable.

Corrections may arise from a variety of operational or technical causes, such as refunds, delayed or missing cost and usage data, rounding errors, post-processing adjustments, etc.

Accurate correction handling is essential for a range of business-critical processes, including but not limited to:

* Temporal accuracy - capturing both when the charge was incurred (reflected in charge period columns, i.e., Charge Period Start and Charge Period End) and when the correction was invoiced (reflected in billing period columns, i.e., Billing Period Start and Billing Period End columns).
* Financial and legal integrity - preserving original charge records associated with finalized invoices while recording changes to those records separately, as finalized invoices represent binding financial documents requiring immutability and traceability.
* Cost allocation and chargeback - attributing corrections to the correct dimensions (e.g., Billing Account, Sub Account, SKU ID, SKU Price ID, Resource ID).
* Auditability - tracing the full lifecycle of a charge from the original record through all subsequent corrections.

Once an invoice is issued, it serves as the authoritative financial document and is considered finalized and immutable. All charge records associated with an issued invoice are also considered finalized and must remain unchanged (i.e., corrections to finalized charge records, whether as updates, deletions or omissions, are not permitted). Furthermore, no additional charge records may be associated with an invoice once it has been issued. This ensures that issued invoices and their underlying charge records remain immutable for financial, auditing, and compliance purposes.

A billing period is considered invoiced (or closed) once all invoices for that period have been issued and all charge records for that period are finalized. After a billing period is invoiced, no new charge records may be associated with it, and all previously finalized charge records remain unchanged. Any necessary corrections to charges originally incurred in an invoiced billing period must instead be reflected in a subsequent open billing period, with the charge period indicating when the cost was  incurred. This provides a clear temporal boundary between billing cycles, preserving immutability while still allowing corrections to be tracked transparently in later billing periods.

FOCUS supports two cost and usage data delivery mechanisms: Replacement and Append-only.

In the Replacement mechanism, each dataset provides a complete snapshot of cost and usage data for a billing period, based on the data collected up to the time of delivery. Subsequent datasets typically reflect updates, additions, or omissions relative to the previous snapshot. This mechanism lacks a built-in audit trail, and therefore historical snapshots must be retained externally to support traceability.

Subsequent datasets in the Replacement mechanism may include the following:

* Unchanged charge records - carried over unchanged from the previously delivered dataset.
* Updated charge records - overwritten with the latest values.
* Additional charge records - new entries representing either billing period segments not previously reported, or supplements to segments included in the previously delivered dataset (e.g., refunds or delayed cost and usage data).
* Omitted charge records - removed from the dataset because they are no longer applicable.

Corrections in the Replacement mechanism are modeled through updates, additions, or omissions relative to the previous snapshot — with the restriction that corrections to charges originally incurred in previously invoiced billing periods must be represented exclusively through the addition of new records. Modifications or deletions of finalized records are not allowed, as they would compromise the immutability of issued invoices and the integrity of audit trails.

In the Append-only mechanism, each dataset appends new records without modifying or removing previously delivered ones. This mechanism inherently supports auditability, as all original and correction records are retained.

Corrections in the Append-only mechanism are represented exclusively by adding new records, and duplicate entries are explicitly disallowed.

Within the Append-only mechanism, two correction styles are commonly used:

* Ledger-style correction: Adds records that adjust selected cost- and quantity-related columns by incrementing or decrementing their values. All other columns remain unchanged. No explicit reversal is performed. This style offers limited audit transparency.
* Accounting-style correction: Uses a two-step representation. First, the original record is reversed using a charge, in which all cost- and quantity-related columns carry values with the opposite sign, while all other columns match the original. This reversal charge is typically followed by a new record with the corrected values, although in some cases only the reversal is provided. This style preserves full correction history.

To ensure data integrity, correction records must not result in double counting of any cost- or quantity-related values. This applies regardless of the correction style or delivery mechanism used.

All correction charge records adhere to the correction handling requirements listed below.

## Attribute ID

CorrectionHandling

## Attribute Name

Correction Handling

## Description

Defines how updates to previously provided charge records are represented in FOCUS datasets.

## Requirements

> WORK IN PROGRESS !!!

* Data Generator MUST publish the provisioning and correction styles in use (Replacement, Ledger-style, Accounting-style) within their respective documentation.
* Correction MUST NOT result in double counting of any cost- or quantity-related values.

### Invoice and Billing Period

* Invoice MUST be considered finalized and immutable once issued.
* Once the associated invoice is issued, each underlying charge record adheres to the following additional requirements:
  * Charge record MUST be considered finalized and immutable.
  * Charge record MUST NOT be updated, deleted, or omitted.
* Additional charge records MUST NOT be associated with an invoice once it is issued.
* Billing period MUST be considered invoiced and closed once all invoices for that period are issued.
* Additional charge records MUST NOT be associated with a billing period once it is invoiced and closed.

### Corrections to charges from a previously invoiced and closed billing period

* Corrections to charges from a previously invoiced and closed billing period adhere to the following additional requirements:
  * ChargeClass MUST be "Correction".
  * Correction MUST NOT replace or omit the original record.
  * Corrected row(s) MUST be assigned to a different `InvoiceId` than the original record.
  * [BillingPeriodStart](#billingperiodstart) and [BillingPeriodEnd](#billingperiodend) MUST equal the [*inclusive start bound*](#glossary:inclusivestartbound) and [*exclusive end bound*](#glossary:exclusiveendbound) of a subsequent open billing period in which the correction is issued.
  * [ChargePeriodStart](#chargeperiodstart) and [ChargePeriodEnd](#chargeperiodend) MUST equal the *inclusive start bound* and *exclusive end bound* of the period in which the cost was originally incurred.

## Exceptions

> WORK IN PROGRESS !!!

Potential exceptions, to be discussed:

* Restatement of Dimensions Not on Original Invoice: Determine whether exceptions will be allowed for corrections that modify only non-invoiced dimensions.
* Technical issues mentioned by Riley.
* Replacment over Append-only explicitly specified by the end-user.

* Replacement provisioning style MAY be applied, even for charges included in datasets associated with previously invoiced billing periods, when xplicitly requested by the end-user.
* Providers MAY apply the Replacement provisioning style instead of Append-only, even for charges included in datasets associated with previously invoiced billing periods, provided that updates affect only non-invoiced dimensions and the integrity of finalized invoices is preserved.
* (TODO) Technical issues mentioned by Riley.

## Introduced (version)

1.3
