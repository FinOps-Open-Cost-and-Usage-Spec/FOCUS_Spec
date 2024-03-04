# Charge Category

A Charge Category indicates whether the row represents an upfront or recurring fee, cost of usage that already occurred,
an after-the-fact [*adjustment*](#glossary:adjustment) (e.g., credits), or taxes. The Charge Category is commonly used to identify prepaid purchases
separately from usage-based charges, to separate taxes that may require special handling, or to apply finer-grained
allocation logic to purchases or *adjustments*.

The ChargeCategory column MUST be present and MUST NOT be null. This column is of type String and MUST be one of the allowed values.

## Column ID

ChargeCategory

## Display Name

Charge Category

## Description

Indicates whether the row represents an upfront or recurring fee, cost of usage that already occurred, an after-the-fact *adjustment* (e.g., credits), or taxes.

## Content Constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column type     | Dimension      |
| Column required | True           |
| Allows nulls    | False          |
| Data type       | String         |
| Value format    | Allowed values |

Allowed values:

| Value      | Description                          |
| :--------- | :------------------------------------|
| Refund     | Any adjustments that are applied after the original usage or purchase row. Adjustments may be related to multiple charges. (NOTE: Tax excluded)   |
| Tax Refund | Tax related to any adjustments that are applied after the original usage or purchase row. Adjustments may be related to multiple charges.  |
| Credit     | Credits assoicated with promotional usage or incentives   |
| Purchase   | Charges for the acquisition of a service or resource bought upfront or on a recurring basis.              |
| Tax        | Applicable taxes that are levied by the relevant authorities. Tax charges may vary depending on factors such as the location, jurisdiction, and local or federal regulations. |
| Usage      | Charges based on the quantity of a service or resource that was consumed over a given period of time.     |

show all 3 options ... add to supporting content sub field for refund (refund for tax and usage and purchase)
is credit usage vs purchase relevant or just one parent credit?

Option 2:

CC:
Usage
Purchase
Tax

Adjustment Category:
NULL
Refund - ( includes rounding errors ??)
Credit 

Usage -- NULL -- general usage
Usage -- Refund - specific redunds /..e.g miss billing
Usage -- Credit - service specific incentives?
Purchase -- NULL - general marketplace or 3rd party purchase
Purchase -- Refund - 
Purchase -- Credit - non-service /usage specific credits
Tax -- NULL - general tax
Tax -- Refund - specific tax refund
Tax -- Credit - NOT APPLICABLE
Other - I got 10K that can go anywhere :)

--------------
Option 3:

CC:
Usage
Purchase
Tax
Credit (for external incentives???)

Adjustment Category:
NULL
Refund - ( includes rounding errors ??)
Bulk Refund

Usage -- NULL -- general usage
Usage -- Refund - specific redunds /..e.g miss billing
Credit  NULL - service specific incentives?
Purchase -- NULL - general marketplace or 3rd party purchase
Purchase -- Refund - specific 3rd party refund
Credit - NULL - non-service /usage specific credits
Tax -- NULL - general tax
Tax -- Refund - specific tax refund
Other - I got 10K that can go anywhere :)

ADD as as seprate branch?

## Introduced (version)

0.5
