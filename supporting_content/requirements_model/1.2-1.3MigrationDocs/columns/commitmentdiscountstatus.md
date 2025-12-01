# CommitmentDiscountStatus

## Normative Text v1.2

The CommitmentDiscountStatus column adheres to the following requirements:

* CommitmentDiscountStatus MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountStatus MUST be of type String.
* CommitmentDiscountStatus nullability is defined as follows:
  * CommitmentDiscountStatus MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null.
  * CommitmentDiscountStatus MUST NOT be null when CommitmentDiscountId is not null and [Charge Category](#chargecategory) is "Usage".
* CommitmentDiscountStatus MUST be one of the allowed values.

## Normative Text v1.3-cr

## Requirements

CommitmentDiscountStatus adheres to the following requirements:

* CommitmentDiscountStatus MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.
* CommitmentDiscountStatus MUST be of type String.
* CommitmentDiscountStatus nullability is defined as follows:
  * CommitmentDiscountStatus MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null.
  * CommitmentDiscountStatus MUST NOT be null when CommitmentDiscountId is not null and [Charge Category](#chargecategory) is "Usage".
* CommitmentDiscountStatus MUST be one of the allowed values.

## Diff

-The CommitmentDiscountStatus column adheres to the following requirements:
+## Requirements
 
-* CommitmentDiscountStatus MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
+CommitmentDiscountStatus adheres to the following requirements:
+
+* CommitmentDiscountStatus MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.
 * CommitmentDiscountStatus MUST be of type String.
 * CommitmentDiscountStatus nullability is defined as follows:
   * CommitmentDiscountStatus MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null.
