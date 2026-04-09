## Diff

@@ -1,11 +1,10 @@
## Requirements

ContractId [-adheres-]{+MUST adhere+} to the following requirements:

[-* ContractId MUST be present in a Contract Commitment *FOCUS dataset*.-]
* ContractId MUST be of type String.
* ContractId MUST conform to StringHandling requirements.
* ContractId MUST NOT be null.
* When ContractId is not null, ContractId [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * ContractId MUST be a unique identifier within the service provider.
  * ContractId SHOULD be a fully-qualified identifier.
