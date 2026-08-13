# Threshold-Based Tiered Pricing

## Candidate Terms Comparison

> **Note:** The phrase "volume-based" is not used consistently even among the sources checked.
>
> * AWS, Azure use it for the threshold dimension (a Quantity denominated in Pricing Unit), where the graduated pricing threshold-based tier application model is assumed (each charge priced at the threshold-based pricing tier reached).
> * Stripe, Oracle NetSuite use "Volume(-based) pricing" for the retroactive pricing threshold-based tier application model (all charges within the aggregation interval repriced to the threshold-based pricing tier reached)
>
> Same word, two unrelated meanings, depending on source.

### Umbrella Term

| Candidate Term | FOCUS Usage | Same Meaning Elsewhere | Different Meaning Elsewhere | Pros | Cons |
|---|---|---|---|---|---|
| **Tiered Pricing** (bare) | "tiered pricing" ×8 | AWS, Azure, Stripe | SaaS subscription/feature tiers | Strong external precedent | Not used as an umbrella anywhere; quantity-only bias; collides with SaaS offering tiers |
| **Threshold-Based Tiered Pricing** | None found | None found | — | Explicit umbrella covering quantity/spend/duration; unambiguous against SaaS offering tiers | No external precedent |

### Quantity-Based Sub-Type

| Candidate Term | FOCUS Usage | Same Meaning Elsewhere | Different Meaning Elsewhere | Pros | Cons |
|---|---|---|---|---|---|
| **Quantity-Based Tiered Pricing** | "quantity-based" ×2, but unrelated context (Contract Commitment, not tiering) | None found | — | Self-explanatory; matches `PricingQuantity`/`PricingUnit`; matches the `QuantityTier*` columns and `IncludesQuantityTierPricing` condition drafted in #2424 | No external precedent |
| **Volume-Based Tiered Pricing** | ×1 "volume-based tiers" (`SkuId`); no columns carry this name | AWS, Azure | Stripe, NetSuite (different axis — see note above) | Matches AWS/Azure | Collides with Stripe/NetSuite meaning; not self-explanatory |

### Decision

**Threshold-Based Tiered Pricing** and **Threshold-Based Pricing Tier** are adopted as the FOCUS terms.

SaaS providers also use "tier" for their offerings (e.g., subscription or feature tiers), which is easily confused with a pricing level in the threshold-based sense. Qualifying the term with a prefix is the only reliable way to prevent that misinterpretation, so bare `Tier`, `Pricing Tier`, and `Tiered Pricing` are not used. See the [Domain Terminology](../../guidelines/contributors/editorial-guidelines.md) editorial guideline.

---

## Threshold-Based Tiered Pricing Context

### Overview

Threshold-based tiered pricing is a pricing model in which the unit price applied to a charge is determined by the applicable threshold-based pricing tier.

Under flat-rate pricing, each pricing unit is assigned a fixed unit price regardless of the quantity consumed, which makes costs straightforward to forecast. Threshold-based tiered pricing differs in that the unit price is not fixed — it depends on which threshold-based pricing tier applies.

A threshold-based tiered pricing model consists of one or more threshold-based pricing tiers. Each threshold-based pricing tier defines a threshold range and an associated unit price. The applicable threshold-based pricing tier is determined based on quantity, duration, or spend within a defined aggregation scope and aggregation interval according to the threshold-based tier application model.

Threshold-based tiered pricing does not require a prior customer commitment or contractual obligation.

``` text
Threshold-Based Tiered Pricing Model
│
├── Threshold-Based Pricing Tiers
│     ├── Threshold-Based Pricing Tier 1
│     │     ├── Threshold Range
│     │     └── Unit Price
│     │
│     ├── Threshold-Based Pricing Tier 2
│     │     ├── Threshold Range
│     │     └── Unit Price
│     │
│     └── Threshold-Based Pricing Tier N
│           ├── Threshold Range
│           └── Unit Price
│
├── Aggregation Scope
│
├── Aggregation Interval
│
└── Threshold-Based Tier Application Model
              │
              ▼
 Determines Applicable Threshold-Based Pricing Tier
              │
              ▼
        Applicable Unit Price
```

For example, in quantity-based tiered pricing, threshold ranges represent accumulated billable quantity levels. Other threshold-based tiered pricing models may define threshold ranges based on duration or spend.

### Threshold-Based Pricing Tiers

A threshold-based pricing tier is a predefined pricing level within a threshold-based tiered pricing model.

Each threshold-based pricing tier defines:

* a threshold range
* an associated unit price

The threshold range defines the range of quantity, duration, or spend values for which the threshold-based pricing tier may become applicable. The associated unit price defines the unit price applied when that threshold-based pricing tier is applicable.

Unit prices commonly decrease as higher threshold ranges are reached, so that accumulated usage lowers the effective unit cost. This is a common pattern rather than a requirement — overage pricing, for example, associates a higher unit price with the higher threshold range.

A free tier is a threshold-based pricing tier whose associated unit price is zero, typically covering an introductory usage level at the lowest threshold range.

### Threshold Categories

Threshold-based pricing tiers may define threshold ranges using different measurement dimensions.

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

Quantity-based tiered pricing is a common form of threshold-based tiered pricing.

### Aggregation Scope and Aggregation Interval

Threshold-based tiered pricing requires defining the aggregation scope and aggregation interval used to determine the applicable threshold-based pricing tier.

Typical aggregation dimensions include:

* **Aggregation scope:** The entity across which quantity, duration, or spend is accumulated to determine the applicable threshold-based pricing tier.
  Examples:
  * billing account
  * subaccount

* **Aggregation interval:** The period over which quantity, duration, or spend is accumulated for the purpose of determining the applicable threshold-based pricing tier.
  Examples:
  * daily billing interval
  * monthly billing interval

Accumulated quantity, duration, or spend resets at the start of each aggregation interval; the applicable threshold-based pricing tier is therefore determined anew in each interval.

Aggregation is commonly performed at the billing account level over a monthly billing interval aligned with the billing cycle.

### Threshold-Based Tier Application Models

The threshold-based tier application model defines how the applicable threshold-based pricing tier is determined and applied.

#### Graduated Pricing

Graduated pricing is a threshold-based tier application model in which the applicable threshold-based pricing tier is determined independently for each threshold range.

Example:

| Usage range | Applicable unit price |
| --- | --- |
| First 100 units | Price A |
| Next 900 units | Price B |
| Above 1000 units | Price C |

Each threshold range is priced using the unit price associated with its applicable threshold-based pricing tier.

#### Retroactive Pricing

Retroactive pricing is a threshold-based tier application model in which reaching a higher threshold causes a higher threshold-based pricing tier to be applied retroactively to all charges within the aggregation interval.

Example:

| Usage range | Applicable unit price |
| --- | --- |
| Up to 1000 units | Price A |
| Above 1000 units | Price B |

When the higher threshold is reached, the higher threshold-based pricing tier is applied to all charges within the aggregation interval.

#### Worked Example

The same threshold-based tiered pricing model produces different charges depending on the threshold-based tier application model applied.

Threshold-based pricing tier configuration:

|  | Lower threshold-based pricing tier | Higher threshold-based pricing tier |
| --- | --- | --- |
| Threshold range start (inclusive) | 0 GB | 10 GB |
| Threshold range end (exclusive) | 10 GB | 100 GB |
| List Unit Price | 1.00 | 0.50 |
| Pricing Unit | 1 GB | 1 GB |
| Pricing Currency | USD | USD |

Scenario: 12 GB consumed within a single aggregation interval.

| Threshold-based tier application model | PricingQuantity | PricingUnit | ListUnitPrice | ListCost |
| --- | ---: | --- | ---: | ---: |
| Graduated pricing | 10 | 1 GB | 1.00 | 10.00 |
| Graduated pricing | 2 | 1 GB | 0.50 | 1.00 |
| Retroactive pricing | 12 | 1 GB | 0.50 | 6.00 |

Under graduated pricing, the 12 GB spans two threshold ranges, each priced at its own unit price, resulting in two charge rows totaling 11.00. Under retroactive pricing, reaching the higher threshold reprices all 12 GB at the higher threshold-based pricing tier's unit price, resulting in a single charge row totaling 6.00.

### Relationship to Commitment Pricing

Threshold-based tiered pricing should not be confused with commitment pricing.

In threshold-based tiered pricing, the applicable threshold-based pricing tier is determined based on quantity, duration, or spend within a defined aggregation scope and aggregation interval.

In commitment pricing, the applicable unit price is determined based on a customer's prior commitment to a specified level of usage, capacity, or spend over a defined commitment period.

The key distinction is:

* Threshold-based tiered pricing determines the applicable threshold-based pricing tier based on quantity, duration, or spend evaluated within a defined aggregation scope and aggregation interval.
* Commitment pricing determines the applicable unit price based on committed usage, capacity, or spend.

A customer commitment may influence the applicable unit price, but it does not determine the applicable threshold-based pricing tier.
