# Provider Tag Prefixes

The Provider Tag Prefixes define the list of prefixes used in the tag name of provider-defined [tags](#datasets.costandusage.tags). This metadata is useful for the consumer to identify which tags are provider-defined vs user-defined.

ProviderTagPrefixes adheres to the following requirements:

* ProviderTagPrefixes MUST be present in an object within the [ColumnDefinition](#metadata.schema.columndefinition) collection when [ColumnName](#metadata.schema.columndefinition.columnname) is "Tags".
* ProviderTagPrefixes MUST be of type Collection of Strings.
* ProviderTagPrefixes SHOULD be easily associated with the data generator who generated the [*dataset instance*](#glossary:dataset-instance) and the corresponding [*dataset instance artifacts*](#glossary:dataset-instance-artifact).

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

## Introduced (version)

1.0
