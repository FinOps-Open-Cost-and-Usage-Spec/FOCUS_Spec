## Diff

@@ -1,10 +1,9 @@
## Requirements

CommitmentDiscountCategory [-adheres-]{+MUST adhere+} to the following requirements:

[-* CommitmentDiscountCategory MUST be present in a Cost and Usage *FOCUS dataset* when the service provider supports *commitment discounts*.-]
* CommitmentDiscountCategory MUST be of type String.
* CommitmentDiscountCategory {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * CommitmentDiscountCategory MUST be null when CommitmentDiscountId is null.
  * CommitmentDiscountCategory MUST NOT be null when CommitmentDiscountId is not null.
* CommitmentDiscountCategory MUST be one of the allowed values.
