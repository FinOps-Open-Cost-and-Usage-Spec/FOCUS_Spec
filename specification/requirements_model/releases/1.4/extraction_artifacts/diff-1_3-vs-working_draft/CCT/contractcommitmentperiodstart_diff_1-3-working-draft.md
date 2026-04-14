## Diff

@@ -1,9 +1,8 @@
## Requirements

ContractCommitmentPeriodStart [-adheres-]{+MUST adhere+} to the following requirements:

[-* ContractCommitmentPeriodStart MUST be present in a Contract Commitment *FOCUS dataset*.-]
* ContractCommitmentPeriodStart MUST be of type Date/Time.
* ContractCommitmentPeriodStart MUST conform to DateTimeFormat requirements.
* ContractCommitmentPeriodStart MUST NOT be null.
* ContractCommitmentPeriodStart MUST be the *inclusive start bound* of the effective period of the *contract commitment*.
