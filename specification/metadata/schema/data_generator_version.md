# Data Generator Version

The [DataGeneratorVersion](#meta) may be supplied to declare the version of logic by which the [dataset instance artifact](#term) was generated and is separate from [FOCUS Version](#meta). [DataGeneratorVersion](#meta) allows for the provider to specify changes that may not result in a structural change in the data. It is suggested that the [DataGeneratorVersion](#meta) use a versioning approach such as [SemVer](https://semver.org) version.

[DataGeneratorVersion](#meta) adheres to the following requirements:

* [DataGeneratorVersion](#meta) MAY be present in an object within the [Schema](#meta) collection.
* [DataGeneratorVersion](#meta) MUST be of type String.
* [DataGeneratorVersion](#meta) MUST conform to [StringHandling](#attr) requirements.
* [DataGeneratorVersion](#meta) MUST NOT be null.
* [DataGeneratorVersion](#meta) MUST be changed when [FocusVersion](#meta) is changed.
* Data generators MUST document what changes are present in the [DataGeneratorVersion](#meta).

## Metadata ID

DataGeneratorVersion

## Metadata Name

Data Generator Version

## Content Constraints

| Constraint    | Value            |
|:--------------|:-----------------|
| Feature level | Optional         |
| Allows nulls  | False            |
| Data type     | String           |
| Value format  | \<not specified> |

## Version Introduced

1.1
