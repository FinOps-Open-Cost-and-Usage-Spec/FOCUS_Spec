# CommitmentDiscountId

## Normative Text v1.2

The CommitmentDiscountId column adheres to the following requirements:

* CommitmentDiscountId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountId MUST be of type String.
* CommitmentDiscountId MUST conform to [StringHandling](#stringhandling) requirements.
* CommitmentDiscountId nullability is defined as follows:
  * CommitmentDiscountId MUST be null when a [*charge*](#glossary:charge) is not related to a *commitment discount*.
  * CommitmentDiscountId MUST NOT be null when a *charge* is related to a *commitment discount*.
* When CommitmentDiscountId is not null, CommitmentDiscountId adheres to the following additional requirements:
  * CommitmentDiscountId MUST be a unique identifier within the provider.
  * CommitmentDiscountId SHOULD be a fully-qualified identifier.

## Normative Text v1.3-cr

## Requirements

CommitmentDiscountId adheres to the following requirements:

* CommitmentDiscountId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.
* CommitmentDiscountId MUST be of type String.
* CommitmentDiscountId MUST conform to [StringHandling](#stringhandling) requirements.
* CommitmentDiscountId nullability is defined as follows:
  * CommitmentDiscountId MUST be null when a [*charge*](#glossary:charge) is not related to a *commitment discount*.
  * CommitmentDiscountId MUST NOT be null when a *charge* is related to a *commitment discount*.
* When CommitmentDiscountId is not null, CommitmentDiscountId adheres to the following additional requirements:
  * CommitmentDiscountId MUST be a unique identifier within the service provider.
  * CommitmentDiscountId SHOULD be a fully-qualified identifier.

## Diff

-The CommitmentDiscountId column adheres to the following requirements:
+## Requirements
 
-* CommitmentDiscountId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
+CommitmentDiscountId adheres to the following requirements:
+
+* CommitmentDiscountId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.
 * CommitmentDiscountId MUST be of type String.
 * CommitmentDiscountId MUST conform to [StringHandling](#stringhandling) requirements.
 * CommitmentDiscountId nullability is defined as follows:
   * CommitmentDiscountId MUST be null when a [*charge*](#glossary:charge) is not related to a *commitment discount*.
   * CommitmentDiscountId MUST NOT be null when a *charge* is related to a *commitment discount*.
 * When CommitmentDiscountId is not null, CommitmentDiscountId adheres to the following additional requirements:
-  * CommitmentDiscountId MUST be a unique identifier within the provider.
+  * CommitmentDiscountId MUST be a unique identifier within the service provider.
   * CommitmentDiscountId SHOULD be a fully-qualified identifier.