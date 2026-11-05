# Invoice Issue Status

[Invoice Issue Status](#col) indicates the publication state of the invoice and the reliability of its associated delivered [Cost and Usage](#ds) and [Invoice Detail](#ds) data. It distinguishes between provisional data that is subject to change, invoices that have been formally issued as valid financial obligations with finalized associated data, and invoices that have been explicitly retracted.

## Requirements

[InvoiceIssueStatus](#col) MUST adhere to the following requirements:

* [InvoiceIssueStatus](#col) MUST be of type String.
* [InvoiceIssueStatus](#col) MUST conform to [StringHandling](#attr) requirements.
* [InvoiceIssueStatus](#col) MUST NOT be null.
* [InvoiceIssueStatus](#col) MUST be one of the allowed values.
* [InvoiceIssueStatus](#col) MUST represent the current publication state of the invoice.
* [InvoiceIssueStatus](#col) MUST NOT be ["Open"](#val:InvoiceIssueStatus) following a previous status of ["Issued"](#val:InvoiceIssueStatus), except when explicitly requested or approved by the customer.

## Allowed Values

| Value  | Description |
| :---   | :---        |
| Open   | The invoice is provisional and subject to change. It is not a valid financial obligation and the associated delivered data is preliminary. |
| Issued | The invoice has been formally issued by the provider. It represents a valid financial obligation with finalized associated data. |
| Voided | The invoice was previously issued but has been retracted or nullified. It is not a valid financial obligation. |

## Implementation Guidance

The transition from ["Open"](#val:InvoiceIssueStatus) to ["Issued"](#val:InvoiceIssueStatus) typically signifies that an invoice has been finalized, invoice reconciliation has been performed, and the delivered data is accurate. However, when the delivered data is found to be inaccurate or incomplete, it may be necessary to apply corrections to records associated with the issued invoice.

If needed, a previously issued invoice may be reopened to apply such corrections, but this transition from ["Issued"](#val:InvoiceIssueStatus) to ["Open"](#val:InvoiceIssueStatus) must be explicitly requested or approved by the customer to maintain auditability.

Corrections to underlying records that do not impact invoice reconciliation are allowed regardless of [Invoice Issue Status](#col), but may reduce auditability and traceability or affect downstream processes (e.g., cost allocation, chargeback, reporting).

FinOps tools and reporting engines should be designed to detect [Invoice Issue Status](#col) transitions and corrections to records associated with issued invoices, and trigger updates to downstream processes to ensure financial accuracy.

For more information, please see the [Invoice and Billing Period Handling](#appendix.invoiceandbillingperiodhandling) appendix and the [Correction Handling](#attr) attribute.

## Column ID

InvoiceIssueStatus

## Display Name

Invoice Issue Status

## Description

The publication state of the invoice and the reliability of its associated delivered data, indicating if it is provisional (["Open"](#val:InvoiceIssueStatus)), issued (["Issued"](#val:InvoiceIssueStatus)), or voided (["Voided"](#val:InvoiceIssueStatus)).

## Content Constraints

| Constraint                 | Value                                      |
| :------------------------- | :----------------------------------------- |
| Dataset                    | [Invoice Detail](#ds)                      |
| Operating model conditions | Not applicable                             |
| Column type                | Dimension                                  |
| Feature level              | Mandatory                                  |
| Allows nulls               | False                                      |
| Data type                  | String                                     |
| Value format               | Allowed values                             |

## Version Introduced

1.4
