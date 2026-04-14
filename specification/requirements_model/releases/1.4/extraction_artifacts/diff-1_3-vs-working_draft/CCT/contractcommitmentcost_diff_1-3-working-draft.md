## Diff

@@ -1,12 +1,10 @@
## Requirements

ContractCommitmentCost [-adheres-]{+MUST adhere+} to the following requirements:

[-* ContractCommitmentCost MUST be present in a Contract Commitment *FOCUS dataset*.-]
* ContractCommitmentCost MUST be of type Decimal.
* ContractCommitmentCost MUST conform to NumericFormat requirements.
* ContractCommitmentCost {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ContractCommitmentCost MUST NOT be null when ContractCommitmentCategory is "Spend".
  * ContractCommitmentCost MAY be null when ContractCommitmentCategory is "Usage".
[-* ContractCommitmentCost MUST be a valid decimal value.-]
* ContractCommitmentCost MUST be denominated in the BillingCurrency.
