# Provider Tag Prefixes

The [Provider Tag Prefixes](#meta) define the list of prefixes used in the tag name of provider-defined [tags](#col). This metadata is useful for the consumer to identify which tags are provider-defined vs user-defined.

[ProviderTagPrefixes](#meta) adheres to the following requirements:

* [ProviderTagPrefixes](#meta) MUST be present in an object within the [ColumnDefinition](#meta) collection when [ColumnName](#meta) is "[Tags](#col)".
* [ProviderTagPrefixes](#meta) MUST be of type Collection of Strings.
* [ProviderTagPrefixes](#meta) SHOULD be easily associated with the data generator who generated the [dataset instance](#term) and the corresponding [dataset instance artifacts](#term).

## Metadata ID

ProviderTagPrefixes

## Metadata Name

Provider Tag Prefixes

## Content Constraints

| Constraint    | Value                 |
|:--------------|:----------------------|
| Feature level | Conditional           |
| Allows nulls  | False                 |
| Data type     | Collection of Strings |
| Value format  | \<not specified>      |

## Version Introduced

1.0
