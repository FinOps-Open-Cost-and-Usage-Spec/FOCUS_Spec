# Column: QuantityTierName

> **Note:** This column was designed for the SKU Price dataset and deferred before the first release. It is not part of the specification. The definition is preserved here so the analysis is available if the column is reconsidered in a later cycle.

## Why it was deferred

Task Force One removed the column on July 28, 2026, before the SKU Price dataset shipped. Three reasons:

* **The available condition did not match the column's applicability.** QuantityTierName was gated on Includes quantity tier pricing, the same condition gating QuantityTierMinimum and QuantityTierMaximum. That asks every service provider supporting quantity tier pricing for a tier name whether or not they publish one. A condition keyed on whether tiers are *named*, rather than on whether tiered pricing exists, would have been one to one with the column itself.
* **Naming tiers is not current provider practice.** No service provider surveyed during the dataset's design publishes tier names as a distinct field.
* **The value is derivable rather than provider-supplied.** The tier a quantity falls into is determined by QuantityTierMinimum and QuantityTierMaximum, and a display label can be composed from those boundaries. The underlying need is closer to a calculated or derivable column, a concept raised for a later cycle rather than for the first release of this dataset.

The bar applied was that a column whose utility and applicability are not obvious does not belong in the first release cycle. The column can be reconsidered once there is signal that it is missing.

## Definition as designed

Quantity Tier Name represents a service-provider-specified display name or label for a specific quantity-based pricing tier associated with a *SKU Price*.

While Quantity Tier Minimum and Quantity Tier Maximum define the strict mathematical boundaries of the quantity envelope, Quantity Tier Name provides a human-readable identifier. This column is commonly used for displaying rate cards in reports, reconciling against vendor pricing pages, or understanding the sequential order of tiers (e.g., "First 1000 Units", "Tier 1", "Over 50 TB").

### Requirements as designed

QuantityTierName MUST adhere to the following requirements:

* QuantityTierName MUST be of type String.
* QuantityTierName MUST conform to StringHandling requirements.
* QuantityTierName MAY be null.
* QuantityTierName MUST be semantically equivalent to the tier name or label published in the service-provider-published *price list*.

### Content constraints as designed

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | SKU Price                                            |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Condition       | Includes quantity tier pricing                       |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |
