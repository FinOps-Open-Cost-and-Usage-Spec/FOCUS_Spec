# SubaccountId

## Normative Text v1.2

The SubAccountId column adheres to the following requirements:

* SubAccountId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports a *sub account* construct.
* SubAccountId MUST be of type String.
* SubAccountId MUST conform to [StringHandling](#stringhandling) requirements.
* SubAccountId nullability is defined as follows:
  * SubAccountId MUST be null when a [*charge*](#glossary:charge) is not related to a *sub account*.
  * SubAccountId MUST NOT be null when a *charge* is related to a *sub account*.

## Normative Text v1.3

## Requirements

SubAccountId adheres to the following requirements:

* SubAccountId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports a *sub account* construct.
* SubAccountId MUST be of type String.
* SubAccountId MUST conform to [StringHandling](#stringhandling) requirements.
* SubAccountId nullability is defined as follows:
  * SubAccountId MUST be null when a [*charge*](#glossary:charge) is not related to a *sub account*.
  * SubAccountId MUST NOT be null when a *charge* is related to a *sub account*.

## Diff

-The SubAccountId column adheres to the following requirements:
+## Requirements
 
-* SubAccountId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports a *sub account* construct.
+SubAccountId adheres to the following requirements:
+
+* SubAccountId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports a *sub account* construct.
 * SubAccountId MUST be of type String.
 * SubAccountId MUST conform to [StringHandling](#stringhandling) requirements.
 * SubAccountId nullability is defined as follows: