## Diff

The ContractApplied column [-adheres-]{+MUST adhere+} to the following requirements:

* ContractApplied MUST[-be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *contract commitments*.-]
[-* ContractApplied MUST-] conform to JsonObjectFormat requirements.
* ContractApplied MUST NOT be null when one or more *contract commitments* are applied to the *charge*.

### Object Schema Requirements

Contract Applied consists of a valid JSON object which contains an array of key-value objects describing the one or more contract commitments applied to the charge. Each object consists of FOCUS-defined keys but can be extended to provide additional details about the contract application.

* If ContractApplied is not null, ContractApplied [-adheres-]{+MUST adhere+} to the following requirements:
  * ContractApplied MUST have a top-level key "Elements" which contains an array.
  * ContractApplied root object MAY contain custom objects, in addition to "Elements".
  * Each item in "Elements" MUST be an object.
  * "Elements" objects MUST conform to KeyValueFormat requirements.
  * "Elements" objects MUST contain key-value pairs (contract application properties).
  * Contract application property keys SHOULD conform to [PascalCase](#glossary:pascalcase) format.
  * "Elements" objects MUST contain four key-value pairs, representing "ContractCommitmentID", "ContractCommitmentAppliedCost", "ContractCommitmentAppliedQuantity", and "ContractCommitmentAppliedUnit".
@@ -39,7 +38,7 @@ Contract Applied consists of a valid JSON object which contains an array of key-
    * Contract application property custom key-value pairs MUST be prefixed with a consistent `x_` prefix to identify them as external, custom columns and distinguish them from FOCUS columns to avoid conflicts in future releases.
    * Contract application property custom key-value pairs MUST be documented by the data generator.
    * Contract application property custom key-value pairs MUST NOT be nested.
  * FOCUS-defined contract application properties {+MUST+} adhere to the following[-additional-] requirements:
    * Contract application property key MUST match the spelling and casing specified for the FOCUS-defined property.
    * Contract application property value MUST be of the type specified for that property.
    * Contract application property MUST adhere to additional normative requirements specific to that property.
@@ -53,15 +52,15 @@ The following keys are used for contract application properties to facilitate qu

Contract ID is a service-provider-assigned identifier for a contract describing the agreed terms between a service provider and a customer.  Contracts can include commitment to a certain amount of spend or usage over an agreed period of time.

[-The-]"ContractId" property [-adheres-]{+MUST adhere+} to the following requirements:

* "ContractId" MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *contract commitments*.
* "ContractId" MUST be of type String.
* "ContractId" MUST conform to StringHandling requirements.
* "ContractId" nullability is defined as follows:
  * "ContractId" MUST be null when a [*charge*](#glossary:charge) is not related to a *contract commitment*.
  * "ContractId" MUST NOT be null when a *charge* is related to a *contract commitment*.
* When "ContractId" is not null, "ContractId" [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * "ContractId" MUST be a unique identifier within the service provider.
  * "ContractId" SHOULD be a fully-qualified identifier.

@@ -69,15 +68,15 @@ The "ContractId" property adheres to the following requirements:

A Contract Commitment ID is a service-provider-assigned identifier describing an agreement agreed between a service provider and a customer.  Contracts can include commitment to a certain amount of spend or usage over an agreed period of time.

[-The-]"ContractCommitmentID" property [-adheres-]{+MUST adhere+} to the following requirements:

* "ContractCommitmentID" MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *contract commitments*.
* "ContractCommitmentID" MUST be of type String.
* "ContractCommitmentID" MUST conform to StringHandling requirements.
* "ContractCommitmentID" nullability is defined as follows:
  * "ContractCommitmentID" MUST be null when a [*charge*](#glossary:charge) is not related to a *contract commitment*.
  * "ContractCommitmentID" MUST NOT be null when a *charge* is related to a *contract commitment*.
* When "ContractCommitmentID" is not null, "ContractCommitmentID" [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * "ContractCommitmentID" MUST be a unique identifier within the service provider.
  * "ContractCommitmentID" SHOULD be a fully-qualified identifier.
  * "ContractCommitmentID" MUST have one and only one parent "ContractID".
@@ -88,12 +87,12 @@ The "ContractCommitmentID" property adheres to the following requirements:

Contract Commitment Applied Cost represents the cost of the charge applied to the contract line item.  Contract Commitment Applied Cost is associated with the contract line item via Contract Commitment ID.  Contract Commitment Applied Cost is commonly used for monitoring the progress towards fulfilling contractual commitments that may facilitate discounts for [*resources*](#glossary:resource) or [*services*](#glossary:service) as agreed between a service provider and a customer.

[-The-]"ContractCommitmentAppliedCost" property [-adheres-]{+MUST adhere+} to the following requirements:

* "ContractCommitmentAppliedCost" MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider associates the *charge's* value with one or more *contract commitments*.
* "ContractCommitmentAppliedCost" MUST be of type Decimal.
* "ContractCommitmentAppliedCost" MUST conform to NumericFormat requirements.
* "ContractCommitmentAppliedCost" {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * "ContractCommitmentAppliedCost" MUST NOT be null when "ContractCommitmentAppliedQuantity" is null.
  * "ContractCommitmentAppliedCost" MAY be null in all other cases.
* "ContractCommitmentAppliedCost" MUST be a valid decimal value.
@@ -103,12 +102,12 @@ The "ContractCommitmentAppliedCost" property adheres to the following requiremen

Contract Commitment Applied Quantity represents the quantity of the charge applied to the contract line item.  Contract Commitment Applied Quantity is associated with the contract line item via Contract Commitment ID.  Contract Commitment Applied Quantity is commonly used for monitoring the progress towards fulfilling contractual commitments that may facilitate discounts for [*resources*](#glossary:resource) or [*services*](#glossary:service) as agreed between a service provider and a customer.

[-The-]"ContractCommitmentAppliedQuantity" property [-adheres-]{+MUST adhere+} to the following requirements:

* "ContractCommitmentAppliedQuantity" MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider associates the *charge's* quantity with one or more *contract commitments*.
* "ContractCommitmentAppliedQuantity" MUST be of type Decimal.
* "ContractCommitmentAppliedQuantity" MUST conform to NumericFormat requirements.
* "ContractCommitmentAppliedQuantity" {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * "ContractCommitmentAppliedQuantity" MUST NOT be null when "ContractCommitmentAppliedCost" is null.
  * "ContractCommitmentAppliedQuantity" MAY be null in all other cases.
* "ContractCommitmentAppliedQuantity" MUST be a valid decimal value.
@@ -122,8 +121,8 @@ The "ContractCommitmentAppliedUnit" property adheres to the following requiremen

* "ContractCommitmentAppliedUnit" MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider associates the *charge's* quantity with one or more *contract commitments*.
* "ContractCommitmentAppliedUnit" MUST be of type String.
* "ContractCommitmentAppliedUnit" MUST conform to StringHandling requirements.
* "ContractCommitmentAppliedUnit" SHOULD conform to UnitFormat requirements.
* "ContractCommitmentAppliedUnit" nullability is defined as follows:
  * "ContractCommitmentAppliedUnit" MUST be null when "ContractCommitmentAppliedQuantity" is null.
  * "ContractCommitmentAppliedUnit" MUST NOT be null when "ContractCommitmentAppliedQuantity" is not null.
@@ -191,7 +190,7 @@ The `Elements` array contains one or more objects, each of which contains the fo
}
```

