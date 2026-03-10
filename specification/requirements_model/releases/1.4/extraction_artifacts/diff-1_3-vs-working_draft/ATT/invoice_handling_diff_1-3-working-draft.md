## Diff

* All costs that appear on any invoice issued to a [-[*BillingAccountId*](#billingaccountid)-]{+[*BillingAccountId*](#datasets.costandusage.billingaccountid)+} MUST be included in the *FOCUS dataset*.
* If an invoice-level *charge* appears on a customer invoice but cannot be expressed using existing FOCUS columns, data generators MUST include provider-defined columns (e.g., x_ChargeSubType) to capture the non-FOCUS-defined details needed to support invoice *charges* reconciliation using the *FOCUS dataset*.