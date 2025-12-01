# SubAccountType

## Normative Text v1.2

The SubAccountType column adheres to the following requirements:

* SubAccountType MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports more than one possible SubAccountType value.
* SubAccountType MUST be of type String.
* SubAccountType MUST conform to [StringHandling](#stringhandling) requirements.
* SubAccountType nullability is defined as follows:
  * SubAccountType MUST be null when [SubAccountId](#subaccountid) is null.
  * SubAccountType MUST NOT be null when SubAccountId is not null.
* SubAccountType MUST be a consistent, readable display value.

## Normative Text v1.3-cr

## Requirements

SubAccountName adheres to the following requirements:

* SubAccountName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports a *sub account* construct.
* SubAccountName MUST be of type String.
* SubAccountName MUST conform to [StringHandling](#stringhandling) requirements.
* SubAccountName nullability is defined as follows:
  * SubAccountName MUST be null when [SubAccountId](#subaccountid) is null.
  * SubAccountName MUST NOT be null when SubAccountId is not null.

## Diff

-The SubAccountType column adheres to the following requirements:
+## Requirements
 
-* SubAccountType MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports more than one possible SubAccountType value.
+SubAccountType adheres to the following requirements:
+
+* SubAccountType MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports more than one possible SubAccountType value.
 * SubAccountType MUST be of type String.
 * SubAccountType MUST conform to [StringHandling](#stringhandling) requirements.
 * SubAccountType nullability is defined as follows:
