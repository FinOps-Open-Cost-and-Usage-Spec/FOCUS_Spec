# Purchase Duration Type

Purchase Duration Type represents the categorical length of the term of a purchase (e.g., "1 Year", "3 Years"), based on the commercial agreement or pricing model. When the purchase is a [*commitment discount*](#glossary:commitment-discount), this column represents the term of that *commitment discount*.

This column serves as a stable classifier for the purchase's term, distinct from the actual lifespan of the specific record. For example, a 3-year purchase term that is exchanged or modified may have a calculated active duration of only a few months, but its Purchase Duration Type remains "3 Years". This allows for consistent grouping and reporting on purchase durations, regardless of lifecycle events.

## Requirements

PurchaseDurationType MUST adhere to the following requirements:

* PurchaseDurationType MUST be of type String.
* PurchaseDurationType MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* PurchaseDurationType MUST adhere to the following nullability requirements:
  * PurchaseDurationType MUST be null when [ChargeCategory](#datasets.skuprice.chargecategory) is "Usage".
  * PurchaseDurationType MUST NOT be null when ChargeCategory is "Purchase".
* PurchaseDurationType SHOULD be expressed with a quantity and time unit, where quantity is a positive integer, and time-unit is a standardized unit of time, either singular or plural (e.g., "1 Day", "1 Year", "3 Months", "3 Years").
* PurchaseDurationType SHOULD present the unit of time as one of the allowed values.
* PurchaseDurationType SHOULD correspond to the standard duration of the purchased offering (e.g., "1 Year", "3 Years") rather than a precise calculation of days or hours.

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

A given Purchase Duration Type value follows a structured format of "[Numeric Value] [Unit]".

* [Numeric Value]: A positive integer.
* [Unit]: A standardized unit of time, singular or plural (e.g., Hour, Year, Years).

## Column ID

PurchaseDurationType

## Display Name

Purchase Duration Type

## Description

Represents the categorical length of the term of a purchase.

## Content Constraints

| Constraint      | Value                                                                                      |
| :-------------- | :----------------------------------------------------------------------------------------- |
| Dataset         | [SKU Price](#datasets.skuprice)                                                            |
| Column type     | Dimension                                                                                  |
| Feature level   | Conditional                                                                                |
| Condition       | [Includes purchases](#conditions.includespurchases)                                        |
| Allows nulls    | True                                                                                       |
| Data type       | String                                                                                     |
| Value format    | [Expected format](#datasets.skuprice.purchasedurationtype.expectedformat)                  |

## Version Introduced

1.5
