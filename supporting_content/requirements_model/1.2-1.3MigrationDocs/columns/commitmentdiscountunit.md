# CommitmentDiscountUnit

## Normative Text v1.2

The CommitmentDiscountUnit column adheres to the following requirements:

* CommitmentDiscountUnit MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountUnit MUST be of type String.
* CommitmentDiscountUnit MUST conform to [StringHandling](#stringhandling) requirements.
* CommitmentDiscountUnit SHOULD conform to [UnitFormat](#unitformat) requirements.
* CommitmentDiscountUnit nullability is defined as follows:
  * CommitmentDiscountUnit MUST be null when CommitmentDiscountQuantity is null.
  * CommitmentDiscountUnit MUST NOT be null when CommitmentDiscountQuantity is not null.
* When CommitmentDiscountUnit is not null, CommitmentDiscountUnit adheres to the following additional requirements:
  * CommitmentDiscountUnit MUST remain consistent over time for a given CommitmentDiscountId.
  * CommitmentDiscountUnit MUST represent the unit used to measure the *commitment discount*.
  * When accounting for [*commitment discount flexibility*](#glossary:commitment-discount-flexibility), the CommitmentDiscountUnit value SHOULD reflect this consideration.

## Normative Text v1.3

## Requirements

CommitmentDiscountUnit adheres to the following requirements:

* CommitmentDiscountUnit MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.
* CommitmentDiscountUnit MUST be of type String.
* CommitmentDiscountUnit MUST conform to [StringHandling](#stringhandling) requirements.
* CommitmentDiscountUnit SHOULD conform to [UnitFormat](#unitformat) requirements.
* CommitmentDiscountUnit nullability is defined as follows:
  * CommitmentDiscountUnit MUST be null when CommitmentDiscountQuantity is null.
  * CommitmentDiscountUnit MUST NOT be null when CommitmentDiscountQuantity is not null.
* When CommitmentDiscountUnit is not null, CommitmentDiscountUnit adheres to the following additional requirements:
  * CommitmentDiscountUnit MUST remain consistent over time for a given CommitmentDiscountId.
  * CommitmentDiscountUnit MUST represent the unit used to measure the *commitment discount*.
  * When accounting for [*commitment discount flexibility*](#glossary:commitment-discount-flexibility), the CommitmentDiscountUnit value SHOULD reflect this consideration.

## Diff

-The CommitmentDiscountUnit column adheres to the following requirements:
+## Requirements
 
-* CommitmentDiscountUnit MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
+CommitmentDiscountUnit adheres to the following requirements:
+
+* CommitmentDiscountUnit MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.
 * CommitmentDiscountUnit MUST be of type String.
 * CommitmentDiscountUnit MUST conform to [StringHandling](#stringhandling) requirements.
 * CommitmentDiscountUnit SHOULD conform to [UnitFormat](#unitformat) requirements.
