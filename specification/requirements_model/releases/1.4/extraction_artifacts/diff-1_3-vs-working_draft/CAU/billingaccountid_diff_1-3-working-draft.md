## Diff

@@ -1,12 +1,11 @@
## Requirements

BillingAccountId [-adheres-]{+MUST adhere+} to the following requirements:

[-* BillingAccountId MUST be present in a Cost and Usage *FOCUS dataset*.-]
* BillingAccountId MUST be of type String.
* BillingAccountId MUST conform to StringHandling requirements.
* BillingAccountId MUST NOT be null.
* BillingAccountId MUST be a unique identifier within an [-invoice issuer.-]{+*invoice issuer*.+}
* BillingAccountId SHOULD be a fully-qualified identifier.

See Appendix: Grouping constructs for resources or services for details and examples of the different grouping constructs supported by FOCUS.
