# Resource Relationship

Resource Relationship describes the relationship to to the entity defined in Related Resource ID.

The ResourceRelationship column MUST be present in the billing data when a RelatedResourceID is supplied. This column MUST be of type String, MUST be null when a RelatedResourceID is NOT supplied. The ResourceRelationship MUST be one of the allowed values. 

## Column ID

ResourceRelationship

## Display Name

Resource Relationship

## Description

Indicates whether the charge represents either the consumption of a *capacity reservation* or when a *capacity reservation* is unused.

## Content constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column type     | Dimension      |
| Feature level   | Conditional    |
| Allows nulls    | True           |
| Data type       | String         |
| Value format    | Allowed Values |

Allowed values:

| Value      | Description                                                                 |
| :--------- | :-------------------------------------------------------------------------- |
| Capacity   | This resource benefited from a capaciity commitment line item               |
| NULL       | No related resources consumed                                               |


## Introduced (version)

1.1