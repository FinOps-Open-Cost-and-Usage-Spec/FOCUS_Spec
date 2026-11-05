# Purchase Duration Type

[Purchase Duration Type](#col) represents the categorical length of the term of a purchase (e.g., "1 Year", "3 Years"), based on the commercial agreement or pricing model. When the purchase is a [commitment discount](#term), this column represents the term of that [commitment discount](#term).

This column serves as a stable classifier for the purchase's term, distinct from the actual lifespan of the specific record. For example, a three-year purchase term that is exchanged or modified may have a calculated active duration of only a few months, but its [Purchase Duration Type](#col) remains "3 Years". This allows for consistent grouping and reporting on purchase durations, regardless of lifecycle events.

## Requirements

[PurchaseDurationType](#col) MUST adhere to the following requirements:

* [PurchaseDurationType](#col) MUST be of type String.
* [PurchaseDurationType](#col) MUST conform to [StringHandling](#attr) requirements.
* [PurchaseDurationType](#col) MUST adhere to the following nullability requirements:
  * [PurchaseDurationType](#col) MUST be null when [ChargeCategory](#col) is ["Usage"](#val:SkuPrice.ChargeCategory).
  * [PurchaseDurationType](#col) MUST be null when [ChargeCategory](#col) is ["Credit"](#val:SkuPrice.ChargeCategory).
  * [PurchaseDurationType](#col) MAY be null when [ChargeCategory](#col) is ["Purchase"](#val:SkuPrice.ChargeCategory).
* [PurchaseDurationType](#col) SHOULD use the "[Numeric Value] [Unit]" format (e.g., "1 Day", "1 Year", "3 Months", "3 Years").
* [PurchaseDurationType](#col) SHOULD present the unit of time as one of the allowed values.
* [PurchaseDurationType](#col) SHOULD correspond to the standard duration of the purchased offering (e.g., "1 Year", "3 Years") rather than a precise calculation of days or hours.

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

> **Note:** These time units express the term of a purchase and are not measurement units. They intentionally differ from the time-based units in [Unit Format](#attr), which govern how the unit of measure for a quantity is expressed. [Purchase Duration Type](#col) includes "Week" and "Quarter" because they are common purchase terms.

## Expected Format

A given [Purchase Duration Type](#col) value follows a structured format of "[Numeric Value] [Unit]".

* [Numeric Value]: A positive integer.
* [Unit]: A standardized unit of time, singular or plural (e.g., Hour, Year, Years).

## Column ID

PurchaseDurationType

## Display Name

Purchase Duration Type

## Description

Represents the categorical length of the term of a purchase.

## Content Constraints

| Constraint                 | Value                                                                                      |
| :------------------------- | :----------------------------------------------------------------------------------------- |
| Dataset                    | [SKU Price](#ds)                                                                           |
| Operating Model Conditions | [Includes Purchases](#omc)                                                                 |
| Column type                | Dimension                                                                                  |
| Feature level              | Conditional                                                                                |
| Allows nulls               | True                                                                                       |
| Data type                  | String                                                                                     |
| Value format               | [Expected format](#datamodel.skuprice.purchasedurationtype.expectedformat)                 |

## Version Introduced

Preview: 1.5
