## Diff

CommitmentDiscountStatus [-adheres-]{+MUST adhere+} to the following requirements:

[-* CommitmentDiscountStatus MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.-]
* CommitmentDiscountStatus MUST be of type String.
* CommitmentDiscountStatus {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * CommitmentDiscountStatus MUST be null when CommitmentDiscountId is null.
  * CommitmentDiscountStatus MUST NOT be null when CommitmentDiscountId is not null and [Charge [-Category](#chargecategory)-]{+Category](#datasets.costandusage.chargecategory)+} is "Usage".
* CommitmentDiscountStatus MUST be one of the allowed values.

