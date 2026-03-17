## Diff

CommitmentDiscountUnit [-adheres-]{+MUST adhere+} to the following requirements:

[-* CommitmentDiscountUnit MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.-]
* CommitmentDiscountUnit MUST be of type String.
* CommitmentDiscountUnit MUST conform to StringHandling requirements.
* CommitmentDiscountUnit SHOULD conform to UnitFormat requirements.
* CommitmentDiscountUnit {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * CommitmentDiscountUnit MUST be null when CommitmentDiscountQuantity is null.
  * CommitmentDiscountUnit MUST NOT be null when CommitmentDiscountQuantity is not null.
* When CommitmentDiscountUnit is not null, CommitmentDiscountUnit [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * CommitmentDiscountUnit MUST remain consistent over time for a given CommitmentDiscountId.
  * CommitmentDiscountUnit MUST represent the unit used to measure the *commitment discount*.
  * When accounting for [*commitment discount flexibility*](#glossary:commitment-discount-flexibility), the CommitmentDiscountUnit value SHOULD reflect this consideration.

