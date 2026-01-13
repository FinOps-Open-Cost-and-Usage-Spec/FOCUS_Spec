# Invoice Handling

## Overview

The Invoice Handling attribute defines how a [*FOCUS dataset*](#glossary:FOCUS-dataset) should reflect details for the information presented on an [*invoice*](#glossary:invoice).

This attribute introduces requirements for how monetary [*charges*](#glossary:charge) such as usage, taxes, credits, refunds, etc, inclusive of support, training, and marketplace transactions, and any other type of charge should be captured and categorized. It also defines expectations around the completeness and consistency of invoice-level totals within a FOCUS dataset, enabling FOCUS [*dataset artifacts*](#glossary:dataset-artifact) to be used in a system of record for all invoiced costs.

FinOps practitioners must be able to reconcile *FOCUS datasets* with the corresponding invoices and usage statements they receive from [*invoice issuers*](#datasets.contractcommitment.invoiceissuername). In practice, this means ensuring that all *charges* that appear on an invoice or usage statement, including those not tied to metered usage, are represented in a *FOCUS dataset*. Without this alignment, it becomes difficult to perform accurate [*invoice reconciliation*](#glossary:invoice-reconciliation), financial reporting, and chargeback.

### Invoice Reconciliation and Issuance

Prior to [*invoice issuance*](#glossary:issued-invoice), the invoice must undergo a reconciliation process. In this process, the *invoice issuer* ensures that the aggregated cost and usage information presented on the *invoice* matches the detailed cost and usage *charges* presented in a *FOCUS dataset*.

At the conclusion of this process, the total monetary value presented on an invoice must match the total monetary value presented in the [Billed Cost](#datasets.contractcommitment.billedcost) metric of a FOCUS dataset. Further, the detail presented on an invoice must match the values of Billed Cost when aggregated by the related combination of the following FOCUS dataset dimensions:

* [Billing Account ID](#datasets.contractcommitment.billingaccountid)
* [Billing Currency](#datasets.contractcommitment.billingcurrency)
* [Billing Period Start](#datasets.contractcommitment.billingperiodstart)
* [Billing Period End](#datasets.contractcommitment.billingperiodend)
* [Invoice ID](#datasets.contractcommitment.invoiceid)
* [Invoice Issuer Name](#datasets.contractcommitment.invoiceissuername)

Depending on the invoice issuer, reconciliation may also extend to additional metrics and dimensions.

Once an invoice is issued, it becomes an authoritative financial document, and the information it contains is expected not to change. [*Corrections*](#glossary:correction) to *issued charges* (including updates, additions, or omissions) may be permitted under certain conditions. However, such corrections must not compromise the integrity of the associated *issued invoice*. For more information on *corrections* to *issued charges*, refer to the [Correction Handling attribute](#correctionhandling).

This information then allows FinOps practitioners to perform their own *invoice reconciliation* process, in order to ensure that the costs reflected on an invoice are commensurate with the usage they have observed.

### Open and Closed Billing Periods

While a billing period is open, one or more FOCUS dataset artifacts may be generated to represent that timeframe. At some point, the billing period will be closed.

A [*closed billing period*](#glossary:closed-billing-period) represents a billing period for which all expected invoices have been successfully issued by an invoice issuer. Once a billing period is financially closed, no additional invoices are expected to be associated with that timeframe.

The ability to determine whether a billing period is "open" or "closed" is typically documented by the invoice issuer and made accessible to customers. There is typically a documented date and time by which all FOCUS dataset artifacts associated with a previous billing period will be generated, and no further artifacts will be expected. At that time, the data presented in the FOCUS dataset artifacts associated with a closed billing period is considered final, though corrections can be made in subsequent billing periods. For information on *corrections* to *closed billing periods*, refer to the [Correction Handling attribute](#correctionhandling).

## Attribute ID

InvoiceHandling

## Attribute Name

Invoice Handling

## Description

Defines how a *FOCUS dataset* should reflect details for the information presented on an *invoice*.

## Requirements

* All costs that appear on any invoice issued to a [*BillingAccountId*](#datasets.contractcommitment.billingaccountid) MUST be included in one or more FOCUS Cost and Usage *dataset artifacts*.
* If an invoice-level *charge* appears on a customer invoice but cannot be expressed using existing FOCUS columns, data generators MUST include custom columns (e.g., x_ChargeSubType) to capture the non-FOCUS-defined details needed to support invoice *charges* reconciliation using the FOCUS Cost and Usage *dataset artifacts*.
* *Invoice reconciliation* adheres to the following additional requirements:
  * Invoice issuer MUST perform *Invoice reconciliation* between an *invoice* and its associated FOCUS *dataset artifacts* before issuing the invoice.
  * *Invoice reconciliation* process MUST include (but is not limited to) the following metric and dimensions: BilledCost, BillingCurrency, InvoiceId, InvoiceIssuerName, BillingAccountId, BillingPeriodStart, and BillingPeriodEnd.
  * Invoice issuer MUST document which FOCUS dataset columns are included in the *invoice reconciliation* process.
* The data generator MUST notify the customer if the contents of a *dataset artifact* associated with an *issued invoice* are altered after final delivery.
* The *billing period* (i.e., the timeframe from BillingPeriodStart to BillingPeriodEnd) of a charge MUST match the *billing period* of its associated [*InvoiceId*](#datasets.contractcommitment.invoiceid).

## Exceptions

* Informational line items that have zero monetary impact and are included solely for transparency MAY be excluded. Examples include:
  * Tax exemption notifications
  * SLA credit details when the credit is already applied to the charged amount
* If such informational items are excluded, data generators MUST document this in their FOCUS implementation guide and ensure the sum of included charges still equals the invoice total.

## Introduced (version)

1.3
