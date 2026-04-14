## Diff

@@ -1,11 +1,10 @@
## Requirements

ContractCommitmentUnit [-adheres-]{+MUST adhere+} to the following requirements:

[-* ContractCommitmentUnit MUST be present in a Contract Commitment *FOCUS dataset*.-]
* ContractCommitmentUnit MUST be of type String.
* ContractCommitmentUnit MUST conform to StringHandling requirements.
* ContractCommitmentUnit SHOULD conform to UnitFormat requirements.
* ContractCommitmentUnit {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ContractCommitmentUnit MUST be null when ContractCommitmentQuantity is null.
  * ContractCommitmentUnit MUST NOT be null when ContractCommitmentQuantity is not null.
