# Subaccount Name

## Normative Text v1.2

The SubAccountName column adheres to the following requirements:

* SubAccountName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports a *sub account* construct.
* SubAccountName MUST be of type String.
* SubAccountName MUST conform to [StringHandling](#stringhandling) requirements.
* SubAccountName nullability is defined as follows:
  * SubAccountName MUST be null when [SubAccountId](#subaccountid) is null.
  * SubAccountName MUST NOT be null when SubAccountId is not null.

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

-The SubAccountName column adheres to the following requirements:
+## Requirements^M
 
-* SubAccountName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports a *sub account* construct.
+SubAccountName adheres to the following requirements:^M
+^M
+* SubAccountName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports a *sub account* construct.^M
 * SubAccountName MUST be of type String.
 * SubAccountName MUST conform to [StringHandling](#stringhandling) requirements.
 * SubAccountName nullability is defined as follows:


