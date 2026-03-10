## Diff

SubAccountId [-adheres-]{+MUST adhere+} to the following requirements:

[-* SubAccountId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports a *sub account* construct.-]
* SubAccountId MUST be of type String.
* SubAccountId MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* SubAccountId {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * SubAccountId MUST be null when a [*charge*](#glossary:charge) is not related to a *sub account*.
  * SubAccountId MUST NOT be null when a *charge* is related to a *sub account*.

