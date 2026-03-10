## Diff

CommitmentDiscountCategory [-adheres-]{+MUST adhere+} to the following requirements:

[-* CommitmentDiscountCategory MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.-]
* CommitmentDiscountCategory MUST be of type String.
* CommitmentDiscountCategory {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * CommitmentDiscountCategory MUST be null when [-[CommitmentDiscountId](#commitmentdiscountid)-]{+[CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid)+} is null.
  * CommitmentDiscountCategory MUST NOT be null when CommitmentDiscountId is not null.
* CommitmentDiscountCategory MUST be one of the allowed values.

