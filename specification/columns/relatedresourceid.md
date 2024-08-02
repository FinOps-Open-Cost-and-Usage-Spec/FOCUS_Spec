# Related Resource ID

Related Resource ID is populated when a usage resource line item is impacted by another line item that modifies its billing behaviour, e.g. when the charge has consumed a [*capacity reservation*](#glossary:capacity-reservation).

The RelatedResourceID column MUST be present in the billing data when the provider supports *capacity-reservations*. This column MUST be of type String, MUST be null when the charge is not related to another line item that impacts its billing behaviour, and MUST NOT be null when the charge is related to another line item that impacts its billing behaviour e.g a capacity reservation. The RelatedResourceID MUST match the ResourceID of thhe line item that has impacted the billing behaviour.

## Column ID

RelatedResourceID

## Display Name

Related Resource ID

## Description

Indicates whether the charge represents either the consumption of a *capacity reservation* or when a *capacity reservation* is unused.

## Content constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.1