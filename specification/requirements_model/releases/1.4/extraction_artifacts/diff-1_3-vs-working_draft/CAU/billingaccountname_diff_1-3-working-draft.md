## Diff

@@ -1,10 +1,9 @@
## Requirements

BillingAccountName [-adheres-]{+MUST adhere+} to the following requirements:

[-* BillingAccountName MUST be present in a Cost and Usage *FOCUS dataset*.-]
* BillingAccountName MUST be of type String.
* BillingAccountName MUST conform to StringHandling requirements.
* BillingAccountName MUST NOT be null when the [-invoice issuer-]{+*invoice issuer*+} supports assigning a display name for the *billing account*.

See Appendix: Grouping constructs for resources or services for details and examples of the different grouping constructs supported by FOCUS.
