## Diff

BillingAccountType [-adheres-]{+MUST adhere+} to the following requirements:

[-* BillingAccountType MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the invoice issuer supports more than one possible BillingAccountType value.-]
* BillingAccountType MUST be of type String.
* BillingAccountType MUST conform to StringHandling requirements.
* BillingAccountType {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * BillingAccountType MUST be null when BillingAccountId is null.
  * BillingAccountType MUST NOT be null when BillingAccountId is not null.
* BillingAccountType MUST be a consistent, readable display value.

