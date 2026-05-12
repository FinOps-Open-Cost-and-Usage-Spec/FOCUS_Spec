# Consumer ID

A Consumer ID is an identifier representing the [*consumer*](#glossary:consumer): a discrete downstream entity (e.g., end-user, tenant, application, autonomous agent, human actor) that consumed a [*resource*](#glossary:resource) or [*service*](#glossary:service). The Consumer ID is commonly used for user-level cost allocation, showback, and unit economics calculations without exposing raw actor data in the central billing dataset.

Consumer ID works in conjunction with [Principal ID](#datasets.costandusage.principalid) to resolve asymmetric actor granularity. While Principal ID captures the authenticated actor that initiated a request at the infrastructure layer, Consumer ID captures the logical downstream actor at the application layer. For scenarios demonstrating how these columns are populated across different technology categories, see [Examples: Actor Attribution](#appendix.examples:actorattribution).

> Note: While Consumer ID is designed to capture opaque identifiers rather than plain-text names or email addresses, these values may still be classified as Personal Data or Personally Identifiable Information (PII) under privacy frameworks such as GDPR or CCPA (e.g., as pseudonymized data). Organizations need to separately ensure that the ingestion, storage, and processing of datasets containing this column comply with their internal data privacy, security, and retention policies.

## Requirements

ConsumerId MUST adhere to the following requirements:

* ConsumerId MUST be of type String.
* ConsumerId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* ConsumerId MUST adhere to the following nullability requirements:
  * ConsumerId MUST be null when a [*charge*](#glossary:charge) is not attributed to a specific *consumer* by the service provider.
  * ConsumerId MUST NOT be null when a *charge* is attributed to a specific *consumer* by the service provider.
* When ConsumerId is not null, ConsumerId MUST adhere to the following requirements:
  * ConsumerId MUST be a unique identifier within the context of the service provider.
  * ConsumerId MUST NOT contain plain-text personally identifiable information (PII) if the service provider supplies an alternative opaque identifier.

## Column ID

ConsumerId

## Display Name

Consumer ID

## Description

Unique identifier of the downstream entity or end-actor consuming the *resource* or *service*.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Version Introduced

1.5
