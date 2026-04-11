## Diff

@@ -1,13 +1,14 @@
## Requirements

CommitmentDiscountId [-adheres-]{+MUST adhere+} to the following requirements:

[-* CommitmentDiscountId MUST be present in a Cost and Usage *FOCUS dataset* when the service provider supports *commitment discounts*.-]
* CommitmentDiscountId MUST be of type String.
* CommitmentDiscountId MUST conform to StringHandling requirements.
* CommitmentDiscountId {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * CommitmentDiscountId MUST be null when a *charge* is not related to a *commitment discount*.
  * CommitmentDiscountId MUST NOT be null when a *charge* is related to a *commitment discount*.
* When CommitmentDiscountId is not null, CommitmentDiscountId [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * CommitmentDiscountId MUST be a unique identifier within the service provider.
  {+* CommitmentDiscountId MUST be equal to ResourceId when ChargeCategory is "Purchase" and the *charge* represents a purchase of that *commitment discount*.+}
{+  * CommitmentDiscountId MUST be equal to ResourceId when ChargeCategory is "Usage" and the *charge* represents an unused portion of that *commitment discount*.+}
  * CommitmentDiscountId SHOULD be a fully-qualified identifier.
