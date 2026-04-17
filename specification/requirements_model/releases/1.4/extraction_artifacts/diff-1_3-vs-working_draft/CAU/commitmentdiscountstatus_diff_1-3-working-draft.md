## Diff

@@ -1,10 +1,11 @@
## Requirements

CommitmentDiscountStatus [-adheres-]{+MUST adhere+} to the following requirements:

[-* CommitmentDiscountStatus MUST be present in a Cost and Usage *FOCUS dataset* when the service provider supports *commitment discounts*.-]
* CommitmentDiscountStatus MUST be of type String.
* CommitmentDiscountStatus {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * CommitmentDiscountStatus MUST be null when CommitmentDiscountId is null.
  * CommitmentDiscountStatus MUST NOT be null when CommitmentDiscountId is not null and [-Charge Category-]{+ChargeCategory+} is "Usage".
* CommitmentDiscountStatus MUST be one of the allowed values.
{+* CommitmentDiscountStatus MUST be "Used" when the *charge* utilizes a specific amount of a given CommitmentDiscountId.+}
{+* CommitmentDiscountStatus MUST be "Unused" when the *charge* represents the unused portion of the given CommitmentDiscountId.+}
