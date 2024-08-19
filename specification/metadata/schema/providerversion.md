# Provider Version

The ProviderVersion MAY be provided to allow the provider to declare the version of logic by which the FOCUS dataset was generated and is separate from Focus Version. ProviderVersion allows for the provider to specify changes that may not result in a structural change in the data. It is suggested that the provider version use a versioning approach such as [SemVer](https://semver.org) version.

## Metadata ID

ProviderVersion

## Metadata Name

Provider Version

## Requirements

 - The provider MUST document what changes are present in the ProviderVersion.
 - ProviderVersion MUST be of type String and MUST NOT contain null values.
 - If FOCUSVersion is changed a new ProviderVersion MUST be also changed.

## Content constraints

| Constraint    | Value            |
|:--------------|:-----------------|
| Feature level | Optional         |
| Allows nulls  | False            |
| Data type     | STRING           |
| Value format  | \<not specified> |

## Introduced (version)

1.1
