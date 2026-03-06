## Diff

SubAccountType [-adheres-]{+MUST adhere+} to the following requirements:

[-* SubAccountType MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports more than one possible SubAccountType value.-]
* SubAccountType MUST be of type String.
* SubAccountType MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* SubAccountType {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * SubAccountType MUST be null when [-[SubAccountId](#subaccountid)-]{+[SubAccountId](#datasets.costandusage.subaccountid)+} is null.
  * SubAccountType MUST NOT be null when SubAccountId is not null.
* SubAccountType MUST be a consistent, readable display value.

