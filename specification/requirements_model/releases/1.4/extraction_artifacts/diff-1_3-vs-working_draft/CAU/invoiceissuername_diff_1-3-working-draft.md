## Diff

@@ -1,10 +1,10 @@
## Requirements

InvoiceIssuerName [-adheres-]{+MUST adhere+} to the following requirements:

[-* InvoiceIssuerName MUST be present in a Cost and Usage *FOCUS dataset*.-]
* InvoiceIssuerName MUST be of type String.
* InvoiceIssuerName MUST conform to StringHandling requirements.
* InvoiceIssuerName MUST NOT be null.
{+* InvoiceIssuerName MUST represent the entity that issues invoices.+}

See Appendix: Participating Entity Identification Examples section for examples of Invoice Issuer Name values across various use case scenarios.
