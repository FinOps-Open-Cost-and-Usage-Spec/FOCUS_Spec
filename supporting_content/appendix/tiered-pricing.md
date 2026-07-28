# Tiered Pricing

## Candidate Terms Comparison

> **Note on "volume-based":** this phrase is not used consistently even among the sources checked. FOCUS and AWS/Azure use it for the **threshold dimension** (a quantity of Pricing Unit). Stripe and Oracle NetSuite use "Volume(-based) pricing" for a completely different axis — the **tier application model** (the whole quantity repriced at the tier reached, as opposed to "Graduated," where only the portion within each tier is repriced). Same word, two unrelated meanings, depending on source.

| Concept | Candidate Term | FOCUS Usage | Same Meaning Elsewhere | Different Meaning Elsewhere | Pros | Cons |
|---|---|---|---|---|---|---|
| Threshold-Based Tiered Pricing (umbrella) | **Threshold-Based Tiered Pricing** | None found | None found | — | Explicit umbrella covering quantity/spend/duration | No external precedent |
| | **Tiered Pricing** (bare) | "tiered pricing" ×8 | AWS, Azure, Stripe | — | Strong external precedent | Not used as an umbrella anywhere; quantity-only bias |
| Quantity-Based sub-type | **Volume-Based Tiered Pricing** | ×3 "volume-based tier(s)" + existing (unratified) columns `VolumeTier*` | AWS, Azure | Stripe, NetSuite (different axis — see note above) | Matches unratified column names; matches AWS/Azure | Collides with Stripe/NetSuite meaning; not self-explanatory |
| | **Quantity-Based Tiered Pricing** | "quantity-based" ×3, but unrelated context (Contract Commitment, not tiering) | None found | — | Self-explanatory; matches `PricingQuantity`/`PricingUnit`; lowest rename cost (dataset unratified) | No external precedent |
| | **Usage-Based Tiered Pricing** | "usage-based" ×56 (general); `ContractCommitmentCategory` = "Usage"/"Spend" is FOCUS's closest ratified dichotomy | Industry-wide, but for consumption pricing generally | "Usage-based" already means "any metered pricing" elsewhere in FOCUS/industry | Reuses FOCUS's own Usage/Spend dichotomy | Not applicable for Purchase assuming tiered pricing is not limited to Usage |

---

## Overview

Tiered pricing is a pricing model in which the unit price applied to a charge is determined by the applicable pricing tier.

A tiered pricing model consists of one or more pricing tiers. Each pricing tier defines a threshold range and an associated unit price. The applicable pricing tier is determined based on quantity, duration, or spend within a defined aggregation scope and aggregation interval according to the pricing tier application model.

Tiered pricing does not require a prior customer commitment or contractual obligation.

``` text
Tiered Pricing Model
│
├── Pricing Tiers
│     ├── Pricing Tier 1
│     │     ├── Threshold Range
│     │     └── Unit Price
│     │
│     ├── Pricing Tier 2
│     │     ├── Threshold Range
│     │     └── Unit Price
│     │
│     └── Pricing Tier N
│           ├── Threshold Range
│           └── Unit Price
│
├── Aggregation Scope
│
├── Aggregation Interval
│
└── Pricing Tier Application Model
              │
              ▼
 Determines Applicable Pricing Tier
              │
              ▼
    Applicable Unit Price
```

For example, in quantity-based tiered pricing, threshold ranges represent accumulated billable quantity levels. Other tiered pricing models may define threshold ranges based on duration or spend.

## Pricing Tiers

A pricing tier is a predefined pricing level within a tiered pricing model.

Each pricing tier defines:

* a threshold range
* an associated unit price

The threshold range defines the range of quantity, duration, or spend values for which the pricing tier may become applicable. The associated unit price defines the unit price applied when that pricing tier is applicable.

## Threshold Categories

Pricing tiers may define threshold ranges using different measurement dimensions.

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

Quantity-based tiered pricing is a common form of tiered pricing.

## Aggregation Scope and Aggregation Interval

Tiered pricing requires defining the aggregation scope and aggregation interval used to determine the applicable pricing tier.

Typical aggregation dimensions include:

* **Aggregation scope:** The entity across which quantity, duration, or spend is accumulated to determine the applicable pricing tier.
  Examples:
  * billing account
  * subaccount

* **Aggregation interval:** The period over which quantity, duration, or spend is accumulated for the purpose of determining the applicable pricing tier.
  Examples:
  * daily billing interval
  * monthly billing interval

Aggregation is commonly performed at the billing account level over a monthly billing interval aligned with the billing cycle.

## Tier Application Models

The pricing tier application model defines how the applicable pricing tier is determined and applied.

### Graduated Pricing

Graduated pricing is a tier application model in which the applicable pricing tier is determined independently for each threshold range.

Example:

| Usage range | Applicable unit price |
| --- | --- |
| First 100 units | Price A |
| Next 900 units | Price B |
| Above 1000 units | Price C |

Each threshold range is priced using the unit price associated with its applicable pricing tier.

### Retroactive Pricing

Retroactive pricing is a tier application model in which reaching a higher threshold causes a higher pricing tier to be applied retroactively to all charges within the aggregation interval.

Example:

| Usage range | Applicable unit price |
| --- | --- |
| Up to 1000 units | Price A |
| Above 1000 units | Price B |

When the higher threshold is reached, the higher pricing tier is applied to all charges within the aggregation interval.

## Relationship to Commitment Pricing

Tiered pricing should not be confused with commitment pricing.

In tiered pricing, the applicable pricing tier is determined based on quantity, duration, or spend within a defined aggregation scope and aggregation interval.

In commitment pricing, the applicable unit price is determined based on a customer's prior commitment to a specified level of usage, capacity, or spend over a defined commitment period.

The key distinction is:

* Tiered pricing determines the applicable pricing tier based on quantity, duration, or spend evaluated within a defined aggregation scope and aggregation interval.
* Commitment pricing determines the applicable unit price based on committed usage, capacity, or spend.

A customer commitment may influence the applicable unit price, but it does not determine the applicable pricing tier.
