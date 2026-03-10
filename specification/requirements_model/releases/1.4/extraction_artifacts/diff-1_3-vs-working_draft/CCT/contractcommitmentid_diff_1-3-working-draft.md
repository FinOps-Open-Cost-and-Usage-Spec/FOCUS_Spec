## Diff

ContractCommitmentId [-adheres-]{+MUST adhere+} to the following requirements:

[-* ContractCommitmentId MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).-]
* ContractCommitmentId MUST be of type String.
* ContractCommitmentId MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* ContractCommitmentId MUST NOT be null.
*[-When ContractCommitmentId is not null, ContractCommitmentId adheres to the following additional requirements:-]
[-  *-] ContractCommitmentId MUST be a unique identifier within the service provider.
* ContractCommitmentId SHOULD be a fully-qualified identifier.
* ContractCommitmentId MUST have one and only one parent [-[ContractId](#contractid).-]{+[ContractId](#datasets.contractcommitment.contractid).+}
* ContractCommitmentId MAY be equal to ContractId.
* ContractCommitmentId MUST be unique across the Contract Commitment dataset.

