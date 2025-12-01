# CommitmentDiscountType

## Normative Text v1.2

The CommitmentDiscountType column adheres to the following requirements:

* CommitmentDiscountType MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountType MUST be of type String.
* CommitmentDiscountType MUST conform to [StringHandling](#stringhandling) requirements.
* CommitmentDiscountType nullability is defined as follows:
  * CommitmentDiscountType MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null.
  * CommitmentDiscountType MUST NOT be null when CommitmentDiscountId is not null.

## Normative Text v1.3-cr

## Requirements

CommitmentDiscountType adheres to the following requirements:

* CommitmentDiscountType MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.
* CommitmentDiscountType MUST be of type String.
* CommitmentDiscountType MUST conform to [StringHandling](#stringhandling) requirements.
* CommitmentDiscountType nullability is defined as follows:
  * CommitmentDiscountType MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null.
  * CommitmentDiscountType MUST NOT be null when CommitmentDiscountId is not null.

## Diff

-The CommitmentDiscountType column adheres to the following requirements:
+## Requirements
 
-* CommitmentDiscountType MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
+CommitmentDiscountType adheres to the following requirements:
+
+* CommitmentDiscountType MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.
 * CommitmentDiscountType MUST be of type String.
 * CommitmentDiscountType MUST conform to [StringHandling](#stringhandling) requirements.
 * CommitmentDiscountType nullability is defined as follows:
