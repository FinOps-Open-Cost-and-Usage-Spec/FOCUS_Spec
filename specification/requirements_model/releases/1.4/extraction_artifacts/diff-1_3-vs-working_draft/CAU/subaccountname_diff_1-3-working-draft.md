## Diff

SubAccountName [-adheres-]{+MUST adhere+} to the following requirements:

* SubAccountName MUST be[-present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports a *sub account* construct.
-]
[-* SubAccountName MUST be-] of type String.
* SubAccountName MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* SubAccountName {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * SubAccountName MUST be null when [-[SubAccountId](#subaccountid)-]{+[SubAccountId](#datasets.costandusage.subaccountid)+} is null.
  * SubAccountName MUST NOT be null when SubAccountId is not null.
