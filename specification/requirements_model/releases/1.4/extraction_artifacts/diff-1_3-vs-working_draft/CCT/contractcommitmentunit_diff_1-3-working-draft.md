## Diff

ContractCommitmentUnit [-adheres-]{+MUST adhere+} to the following requirements:

[-* ContractCommitmentUnit MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* ContractCommitmentUnit MUST be of type String.
* ContractCommitmentUnit MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* ContractCommitmentUnit SHOULD conform to [-[UnitFormat](#unitformat)-]{+[UnitFormat](#attributes.unitformat)+} requirements.
* ContractCommitmentUnit {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ContractCommitmentUnit MUST be null when ContractCommitmentQuantity is null.
  * ContractCommitmentUnit MUST NOT be null when ContractCommitmentQuantity is not null.

