## Diff

@@ -1,13 +1,13 @@
## Requirements

ResourceId [-adheres-]{+MUST adhere+} to the following requirements:

[-* ResourceId MUST be present in a Cost and Usage *FOCUS dataset* when the service provider supports billing based on provisioned *resources*.-]
* ResourceId MUST be of type String.
* ResourceId MUST conform to StringHandling requirements.
* ResourceId {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ResourceId MUST be null when a *charge* is not related to a *resource*.
  * ResourceId MUST NOT be null when a *charge* is related to a *resource*.
* When ResourceId is not null, ResourceId [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * ResourceId MUST be a unique identifier within the service provider.
  * ResourceId SHOULD be a fully-qualified identifier.
  {+* ResourceId MUST be the identifier of the *resource* that received the *commitment discount* when CommitmentDiscountStatus is "Used".+}
