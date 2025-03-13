# Data Generator Version

The DataGeneratorVersion MAY be supplied to declare the version of logic by which the [*FOCUS dataset*](#glossary:FOCUS-dataset) was generated and is separate from FOCUS Version. DataGeneratorVersion allows for the provider to specify changes that may not result in a structural change in the data. It is suggested that the DataGeneratorVersion use a versioning approach such as [SemVer](https://semver.org) version.

DataGeneratorVersion MUST be of type String and MUST NOT contain null values. If FocusVersion is changed a new DataGeneratorVersion MUST be also changed. The provider MUST document what changes are present in the DataGeneratorVersion.

## Metadata ID

DataGeneratorVersion

## Metadata Name

Data Generator Version

## Content constraints

| Constraint    | Value            |
|:--------------|:-----------------|
| Feature level | Optional         |
| Allows nulls  | False            |
| Data type     | STRING           |
| Value format  | \<not specified> |

## Introduced (version)

1.1
