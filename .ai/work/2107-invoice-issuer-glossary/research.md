# Research: Issue #2107 — Add Invoice Issuer to Glossary

## Issue Summary

"Invoice Issuer" is a core concept used 80+ times across all four FOCUS datasets but has no glossary entry. "Service Provider" has one — it's inconsistent that "Invoice Issuer" doesn't. Issue was split: #2107 covers the glossary entry only; #2256 (dependent) covers updating all spec references to link to it.

## Current State

### No glossary entry exists
The glossary has "Invoice", "Invoice Reconciliation", and "Issued Invoice", but nothing for the entity concept "Invoice Issuer".

### One broken link already exists
`specification/datasets/invoice_detail/columns/paymentduedate.md:12` references `[*invoice issuer*](#glossary:invoice-issuer)` which points to nothing.

### Definition is well-established across column descriptions
All 4 InvoiceIssuerName column files use nearly identical language: "the entity responsible for issuing payable invoices for the resources or services consumed".

### Usage across the spec (~80+ occurrences)
- All 4 InvoiceIssuerName column definitions (Cost and Usage, Invoice Detail, Billing Period, Contract Commitment)
- Billing Period dataset description
- Invoice Detail dataset description
- Multiple appendix examples
- Glossary entries for "Closed Billing Period" and "Issued Invoice"
- Various column definitions (BilledCost, BillingCurrency, BillingAccountId, PaymentDueDate, PaymentTerms, InvoiceIssueDate, InvoiceId, etc.)
- Requirements model JSON files

### Comparable pattern
"Service Provider" entry at glossary.md:263 uses `<a name="glossary:service provider">` (space-separated anchor).

## Decisions

1. **Anchor format**: Use space-separated `glossary:invoice issuer` to replicate the Service Provider pattern.
2. **Alphabetical placement**: Between "Invoice" (line 186) and "Invoice Reconciliation" (line 188).
3. **Definition text** (draft, subject to group confirmation):

   > An entity responsible for issuing payable invoices for the resources or services consumed. Common examples include cloud service providers, managed service providers, or marketplace operators.

4. **Broken link fix**: Update `paymentduedate.md` from `#glossary:invoice-issuer` to `#glossary:invoice issuer`.

## Out of Scope (#2256)
Updating the ~80+ other "invoice issuer" references to link to this glossary entry. Many are in column contexts where the InvoiceIssuerName column reference is more appropriate than a glossary link — needs significant human review.
