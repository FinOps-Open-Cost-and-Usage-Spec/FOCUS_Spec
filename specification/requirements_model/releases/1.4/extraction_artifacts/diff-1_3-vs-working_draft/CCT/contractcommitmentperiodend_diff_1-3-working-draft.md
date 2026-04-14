## Diff

@@ -1,9 +1,8 @@
## Requirements

ContractCommitmentPeriodEnd [-adheres-]{+MUST adhere+} to the following requirements:

[-* ContractCommitmentPeriodEnd MUST be present in a Contract Commitment *FOCUS dataset*.-]
* ContractCommitmentPeriodEnd MUST be of type Date/Time.
* ContractCommitmentPeriodEnd MUST conform to DateTimeFormat requirements.
* ContractCommitmentPeriodEnd MUST NOT be null.
* ContractCommitmentPeriodEnd MUST be the *exclusive end bound* of the effective period of the *contract commitment*.
