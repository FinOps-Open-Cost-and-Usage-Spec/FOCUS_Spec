## Diff

@@ -1,9 +1,8 @@
## Requirements

ContractPeriodEnd [-adheres-]{+MUST adhere+} to the following requirements:

[-* ContractPeriodEnd MUST be present in a Contract Commitment *FOCUS dataset*.-]
* ContractPeriodEnd MUST be of type Date/Time.
* ContractPeriodEnd MUST conform to DateTimeFormat requirements.
* ContractPeriodEnd MUST NOT be null.
* ContractPeriodEnd MUST be the *exclusive end bound* of the effective period of the *contract*.
