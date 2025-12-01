# BillingAccountType

## Normative Text v1.2

The BillingAccountType column adheres to the following requirements:

* BillingAccountType MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports more than one possible BillingAccountType value.
* BillingAccountType MUST be of type String.
* BillingAccountType MUST conform to [StringHandling](#stringhandling) requirements.
* BillingAccountType nullability is defined as follows:
  * BillingAccountType MUST be null when [BillingAccountId](#billingaccountid) is null.
  * BillingAccountType MUST NOT be null when BillingAccountId is not null.
* BillingAccountType MUST be a consistent, readable display value.

## Normative Text v1.3

## Requirements

BillingAccountType adheres to the following requirements:

* BillingAccountType MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the invoice issuer supports more than one possible BillingAccountType value.
* BillingAccountType MUST be of type String.
* BillingAccountType MUST conform to [StringHandling](#stringhandling) requirements.
* BillingAccountType nullability is defined as follows:
  * BillingAccountType MUST be null when [BillingAccountId](#billingaccountid) is null.
  * BillingAccountType MUST NOT be null when BillingAccountId is not null.
* BillingAccountType MUST be a consistent, readable display value.

## Diff

-The BillingAccountType column adheres to the following requirements:
+## Requirements
 
-* BillingAccountType MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports more than one possible BillingAccountType value.
+BillingAccountType adheres to the following requirements:
+
+* BillingAccountType MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the invoice issuer supports more than one possible BillingAccountType value.
 * BillingAccountType MUST be of type String.
 * BillingAccountType MUST conform to [StringHandling](#stringhandling) requirements.
 * BillingAccountType nullability is defined as follows:
