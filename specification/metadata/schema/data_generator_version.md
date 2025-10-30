# Data Generator Version

The DataGeneratorVersion MAY be supplied to declare the version of logic by which the [*FOCUS dataset*](#glossary:FOCUS-dataset) was generated and is separate from FOCUS Version. DataGeneratorVersion allows for the data generator to specify changes that may not result in a structural change in the data. It is suggested that the DataGeneratorVersion use a versioning approach such as [SemVer](https://semver.org) version.

DataGeneratorVersion adheres to the following requirements:

* DataGeneratorVersion MAY be present in an object within the [Schema](#schema) collection.
* DataGeneratorVersion MUST be of type String.
* DataGeneratorVersion MUST conform to [StringHandling](#stringhandling) requirements.
* DataGeneratorVersion MUST NOT be null.
* DataGeneratorVersion MUST be changed when [FocusVersion](#focusversion) is changed.
* Data generators MUST document what changes are present in the DataGeneratorVersion.

## Metadata ID

DataGeneratorVersion

## Metadata Name

Data Generator Version

## Content constraints

| Constraint    | Value            |
|:--------------|:-----------------|
| Feature level | Optional         |
| Allows nulls  | False            |
| Data type     | String           |
| Value format  | \<not specified> |

## Introduced (version)

1.1
