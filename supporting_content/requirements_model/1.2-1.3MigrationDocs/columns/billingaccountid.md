# BillingAccountID

## Normative Text v1.2

The BillingAccountId column adheres to the following requirements:

* BillingAccountId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BillingAccountId MUST be of type String.
* BillingAccountId MUST conform to [StringHandling](#stringhandling) requirements.
* BillingAccountId MUST NOT be null.
* BillingAccountId MUST be a unique identifier within a provider.
* BillingAccountId SHOULD be a fully-qualified identifier.

## Normative Text v1.3

## Requirements

BillingAccountId adheres to the following requirements:

* BillingAccountId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BillingAccountId MUST be of type String.
* BillingAccountId MUST conform to [StringHandling](#stringhandling) requirements.
* BillingAccountId MUST NOT be null.
* BillingAccountId MUST be a unique identifier within an invoice issuer.
* BillingAccountId SHOULD be a fully-qualified identifier.

## Diff

-The BillingAccountId column adheres to the following requirements:
+## Requirements
 
-* BillingAccountId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
+BillingAccountId adheres to the following requirements:
+
+* BillingAccountId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).
 * BillingAccountId MUST be of type String.
 * BillingAccountId MUST conform to [StringHandling](#stringhandling) requirements.
 * BillingAccountId MUST NOT be null.
-* BillingAccountId MUST be a unique identifier within a provider.
+* BillingAccountId MUST be a unique identifier within an invoice issuer.
 * BillingAccountId SHOULD be a fully-qualified identifier.