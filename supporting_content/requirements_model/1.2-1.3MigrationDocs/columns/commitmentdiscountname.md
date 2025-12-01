# CommitmentDiscountName

## Normative Text v1.2

The CommitmentDiscountName column adheres to the following requirements:

* CommitmentDiscountName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountName MUST be of type String.
* CommitmentDiscountName MUST conform to [StringHandling](#stringhandling) requirements.
* CommitmentDiscountName nullability is defined as follows:
  * CommitmentDiscountName MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null.
  * When CommitmentDiscountId is not null, CommitmentDiscountName adheres to the following additional requirements:
    * CommitmentDiscountName MUST NOT be null when a display name can be assigned to a *commitment discount*.
    * CommitmentDiscountName MAY be null when a display name cannot be assigned to a *commitment discount*.

## Normative Text v1.3-cr

## Requirements

CommitmentDiscountName adheres to the following requirements:

* CommitmentDiscountName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.
* CommitmentDiscountName MUST be of type String.
* CommitmentDiscountName MUST conform to [StringHandling](#stringhandling) requirements.
* CommitmentDiscountName nullability is defined as follows:
  * CommitmentDiscountName MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null.
  * When CommitmentDiscountId is not null, CommitmentDiscountName adheres to the following additional requirements:
    * CommitmentDiscountName MUST NOT be null when a display name can be assigned to a *commitment discount*.
    * CommitmentDiscountName MAY be null when a display name cannot be assigned to a *commitment discount*.

## Diff

-The CommitmentDiscountName column adheres to the following requirements:
+## Requirements
 
-* CommitmentDiscountName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
+CommitmentDiscountName adheres to the following requirements:
+
+* CommitmentDiscountName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.
 * CommitmentDiscountName MUST be of type String.
 * CommitmentDiscountName MUST conform to [StringHandling](#stringhandling) requirements.
 * CommitmentDiscountName nullability is defined as follows:
