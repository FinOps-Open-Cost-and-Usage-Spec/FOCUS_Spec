# BillingAccountName

## Normative Text v1.2

The BillingAccountName column adheres to the following requirements:

* BillingAccountName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BillingAccountName MUST be of type String.
* BillingAccountName MUST conform to [StringHandling](#stringhandling) requirements.
* BillingAccountName MUST NOT be null when the provider supports assigning a display name for the *billing account*.

## Normative Text v1.3

## Requirements

BillingAccountName adheres to the following requirements:

* BillingAccountName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BillingAccountName MUST be of type String.
* BillingAccountName MUST conform to [StringHandling](#stringhandling) requirements.
* BillingAccountName MUST NOT be null when the invoice issuer supports assigning a display name for the *billing account*.

## Diff

-The BillingAccountName column adheres to the following requirements:
+## Requirements
 
-* BillingAccountName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
+BillingAccountName adheres to the following requirements:
+
+* BillingAccountName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).
 * BillingAccountName MUST be of type String.
 * BillingAccountName MUST conform to [StringHandling](#stringhandling) requirements.
-* BillingAccountName MUST NOT be null when the provider supports assigning a display name for the *billing account*.
+* BillingAccountName MUST NOT be null when the invoice issuer supports assigning a display name for the *billing account*.