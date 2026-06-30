# Contract Commitment Duration Type

Contract Commitment Duration Type represents the categorical length of a [*contract commitment*](#glossary:contract-commitment) (e.g., "1 Year", "3 Years") based on the commercial agreement or pricing model.

This column serves as a stable classifier for the commitment's duration, distinct from the actual lifespan of the specific record. For example, a 3-year commitment pricing term that is exchanged or modified may have a calculated active duration of only a few months, but its Contract Commitment Duration Type remains "3 Years". This allows for consistent grouping and reporting on commitment durations, regardless of lifecycle events.

## Requirements

ContractCommitmentDurationType MUST adhere to the following requirements:

* ContractCommitmentDurationType MUST be of type String.
* ContractCommitmentDurationType MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* ContractCommitmentDurationType MAY be null.
* ContractCommitmentDurationType SHOULD be expressed with a quantity and time unit, where quantity is a positive integer, and time-unit is a standardized unit of time, either singular or plural (e.g., "1 Day", "1 Year", "3 Months", "3 Years").
* ContractCommitmentDurationType SHOULD present the unit of time as one of the allowed values.
* ContractCommitmentDurationType SHOULD correspond to the standard duration of the purchased offering (e.g., "1 Year", "3 Years") rather than a precise calculation of days or hours.

## Allowed Values

The following units should be used for the representation of time:

| Time Unit |
| :--- |
| Minute |
| Minutes |
| Hour |
| Hours |
| Day |
| Days |
| Week |
| Weeks |
| Month |
| Months |
| Quarter |
| Quarters |
| Year |
| Years |

## Expected Format

A given Contract Commitment Duration Type value follows a structured format of "[Numeric Value] [Unit]".

* [Numeric Value]: A positive integer.
* [Unit]: A standardized unit of time, singular or plural (e.g., Hour, Year, Years).

## Column ID

ContractCommitmentDurationType

## Display Name

Contract Commitment Duration Type

## Description

Represents the categorical length of the *contract commitment* offering.

## Content Constraints

| Constraint      | Value                                                                                      |
| :-------------- | :----------------------------------------------------------------------------------------- |
| Dataset         | [SKU Price](#datasets.skuprice)                                                            |
| Column type     | Dimension                                                                                  |
| Feature level   | Conditional                                                                                |
| Condition       | [Includes contract commitments](#conditions.includescontractcommitments)                   |
| Allows nulls    | True                                                                                       |
| Data type       | String                                                                                     |
| Value format    | [Expected format](#datasets.skuprice.contractcommitmentdurationtype.expectedformat)        |

## Version Introduced

1.5
