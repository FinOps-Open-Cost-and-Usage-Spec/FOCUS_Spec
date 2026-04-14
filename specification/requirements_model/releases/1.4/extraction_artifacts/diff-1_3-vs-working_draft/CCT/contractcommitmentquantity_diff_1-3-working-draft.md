## Diff

@@ -1,11 +1,9 @@
## Requirements

ContractCommitmentQuantity [-adheres-]{+MUST adhere+} to the following requirements:

[-* ContractCommitmentQuantity MUST be present in a Contract Commitment *FOCUS dataset*.-]
* ContractCommitmentQuantity MUST be of type Decimal.
* ContractCommitmentQuantity MUST conform to NumericFormat requirements.
* ContractCommitmentQuantity {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ContractCommitmentQuantity MUST NOT be null when ContractCommitmentCategory is "Usage".
  * ContractCommitmentQuantity MAY be null when ContractCommitmentCategory is "Spend".
[-* ContractCommitmentQuantity MUST be a valid decimal value.-]
