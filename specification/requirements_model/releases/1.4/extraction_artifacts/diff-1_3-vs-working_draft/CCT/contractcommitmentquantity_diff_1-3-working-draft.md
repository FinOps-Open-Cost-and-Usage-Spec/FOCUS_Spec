## Diff

ContractCommitmentQuantity [-adheres-]{+MUST adhere+} to the following requirements:

[-* ContractCommitmentQuantity MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* ContractCommitmentQuantity MUST be of type Decimal.
* ContractCommitmentQuantity MUST conform to [-[NumericFormat](#numericformat)-]{+[NumericFormat](#attributes.numericformat)+} requirements.
* ContractCommitmentQuantity {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ContractCommitmentQuantity MUST NOT be null when [-[ContractCommitmentCategory](#contractcommitmentcategory)-]{+[ContractCommitmentCategory](#datasets.contractcommitment.contractcommitmentcategory)+} is "Usage".
  * ContractCommitmentQuantity MAY be null when ContractCommitmentCategory is "Spend".
* ContractCommitmentQuantity MUST be a valid decimal value.

