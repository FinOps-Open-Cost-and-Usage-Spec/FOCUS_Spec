## Diff

CommitmentDiscountType [-adheres-]{+MUST adhere+} to the following requirements:

[-* CommitmentDiscountType MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.-]
* CommitmentDiscountType MUST be of type String.
* CommitmentDiscountType MUST conform to StringHandling requirements.
* CommitmentDiscountType {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * CommitmentDiscountType MUST be null when CommitmentDiscountId is null.
  * CommitmentDiscountType MUST NOT be null when CommitmentDiscountId is not null.

