# Threshold-Based Tiered Pricing

## Overview

Threshold-based tiered pricing is a pricing model where the applicable unit price is determined based on reaching predefined thresholds during a defined aggregation interval and aggregation scope.

Thresholds represent achieved quantity, duration, or spend levels. When a threshold is reached, the pricing tier associated with that threshold becomes applicable according to the defined tier application model.

Threshold-based tiered pricing is based on achieved usage, duration, or spend and does not require a prior customer commitment or contractual obligation.

## Threshold Categories

Thresholds may be based on different metrics:

* **Quantity-based thresholds:** Thresholds based on accumulated billable quantity during the aggregation interval.
  Examples:
  * storage capacity consumed (for example, GB-months)
  * number of API requests
  * compute usage hours

* **Duration-based thresholds:** Thresholds based on accumulated usage duration during the aggregation interval.
  Examples:
  * sustained usage over a billing period
  * continuous resource utilization duration

* **Spend-based thresholds:** Thresholds based on accumulated customer spend during the aggregation interval.
  Examples:
  * cumulative spend reaching predefined levels during a billing period

## Aggregation Scope and Aggregation Interval

Threshold-based tiered pricing requires defining the scope and interval over which the measured value is aggregated.

Typical aggregation dimensions include:

* **Aggregation scope:** The entity across which quantity, duration, or spend is accumulated to determine the applicable pricing tier.
  Examples:
  * billing account
  * customer account
  * subscription
  * project

* **Aggregation interval:** The period over which quantity, duration, or spend is accumulated for the purpose of determining the applicable pricing tier.
  Examples:
  * daily billing interval
  * monthly billing interval

Aggregation is commonly performed at the billing account level over a monthly billing interval aligned with the billing cycle.

## Tier Application Models

The applicability of a pricing tier depends on the tier application model.

### Graduated Pricing

Graduated pricing is a tier application model where each portion of usage is priced according to the pricing tier applicable to that portion of usage.

Example:

| Usage range | Applicable unit price |
| --- | --- |
| First 100 units | Price A |
| Next 900 units | Price B |
| Above 1000 units | Price C |

When a higher threshold is reached, only the usage within that tier range is priced using the corresponding tier unit price.

### Retroactive Volume Pricing

Retroactive volume pricing is a tier application model where reaching a higher threshold causes the applicable unit price for all usage within the aggregation interval to be adjusted to the newly reached tier.

Example:

| Usage range | Applicable unit price |
| --- | --- |
| Up to 1000 units | Price A |
| Above 1000 units | Price B |

When the 1000-unit threshold is reached, all usage within the aggregation interval is priced using Price B.

## Relationship to Commitment Pricing

Threshold-based tiered pricing should not be confused with commitment-based pricing.

Threshold-based tiered pricing determines pricing based on purchased or consumed quantity, duration, or spend during a defined aggregation interval. The customer does not need to make a prior commitment to obtain the applicable pricing tier.

Commitment pricing determines pricing based on a customer's prior commitment to a specified level of usage, capacity, or spend over a defined commitment period.

The key distinction is:

* Threshold-based tiered pricing rewards purchased or consumed quantity, duration, or spend.
* Commitment pricing rewards committed usage, capacity, or spend.

A commitment may influence the applicable unit price, but it is not itself a pricing tier determined by crossing a predefined threshold.
