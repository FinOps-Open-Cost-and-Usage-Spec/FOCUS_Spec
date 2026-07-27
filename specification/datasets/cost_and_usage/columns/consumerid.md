# Consumer ID

A Consumer ID is an identifier representing the [*consumer*](#glossary:consumer): the party to which a [*charge*](#glossary:charge) is attributed for allocation, chargeback, or showback (e.g., end-user, application, autonomous agent). A *consumer* is distinct from the [*principal*](#glossary:principal) to which a service provider grants access to a [*resource*](#glossary:resource) or [*service*](#glossary:service), and need not be an entity in a service provider identity and access management model. The Consumer ID is commonly used for cost allocation, showback and chargeback, and unit economics calculations.

Consumer ID is used in conjunction with [Principal ID](#datasets.costandusage.principalid) when the party a *charge* is attributed to differs from the *principal* the service provider authenticated.

For scenarios demonstrating how these columns are populated across different technology categories, see [Examples: Actor Attribution](#appendix.examples:actorattribution).

> **Note:** While Consumer ID is designed to capture opaque identifiers rather than plain-text names or email addresses, these values may still be classified as Personal Data or Personally Identifiable Information (PII) under privacy frameworks such as GDPR or CCPA (e.g., as pseudonymized data). Organizations need to separately ensure that the ingestion, storage, and processing of datasets containing this column comply with their internal data privacy, security, and retention policies.

## Requirements

ConsumerId MUST adhere to the following requirements:

* ConsumerId MUST be of type String.
* ConsumerId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* ConsumerId MUST adhere to the following nullability requirements:
  * ConsumerId MUST be null when the service provider cannot determine the *consumer* to which the *charge* is attributed.
  * ConsumerId MUST NOT be null when the service provider can determine the *consumer* to which the *charge* is attributed.
* When ConsumerId is not null, ConsumerId MUST adhere to the following requirements:
  * ConsumerId MUST be a unique identifier within the service provider.
  * ConsumerId MUST NOT contain plain-text personally identifiable information (PII) when the service provider supplies an alternative opaque identifier.
  * ConsumerId MAY contain plain-text personally identifiable information (PII) when the service provider does not supply an alternative opaque identifier.

## Column ID

ConsumerId

## Display Name

Consumer ID

## Description

Identifier representing the *consumer* to which a *charge* is attributed.

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
