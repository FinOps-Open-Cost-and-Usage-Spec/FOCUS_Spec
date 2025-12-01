# CommitmentDiscountCategory

## Normative Text v1.2

The CommitmentDiscountCategory column adheres to the following requirements:

* CommitmentDiscountCategory MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountCategory MUST be of type String.
* CommitmentDiscountCategory nullability is defined as follows:
  * CommitmentDiscountCategory MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null.
  * CommitmentDiscountCategory MUST NOT be null when CommitmentDiscountId is not null.
* CommitmentDiscountCategory MUST be one of the allowed values.

## Normative Text v1.3-cr

## Requirements

CommitmentDiscountCategory adheres to the following requirements:

* CommitmentDiscountCategory MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.
* CommitmentDiscountCategory MUST be of type String.
* CommitmentDiscountCategory nullability is defined as follows:
  * CommitmentDiscountCategory MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null.
  * CommitmentDiscountCategory MUST NOT be null when CommitmentDiscountId is not null.
* CommitmentDiscountCategory MUST be one of the allowed values.

## Diff

-The CommitmentDiscountCategory column adheres to the following requirements:
+## Requirements
 
-* CommitmentDiscountCategory MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
+CommitmentDiscountCategory adheres to the following requirements:
+
+* CommitmentDiscountCategory MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.
 * CommitmentDiscountCategory MUST be of type String.
 * CommitmentDiscountCategory nullability is defined as follows:
   * CommitmentDiscountCategory MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null.
