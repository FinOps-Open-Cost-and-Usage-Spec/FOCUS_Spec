## Diff

@@ -1,9 +1,8 @@
## Requirements

ChargeFrequency [-adheres-]{+MUST adhere+} to the following requirements:

[-* ChargeFrequency is RECOMMENDED to be present in a Cost and Usage *FOCUS dataset*.-]
* ChargeFrequency MUST be of type String.
* ChargeFrequency MUST NOT be null.
* ChargeFrequency MUST be one of the allowed values.
* ChargeFrequency MUST NOT be "Usage-Based" when ChargeCategory is "Purchase".
