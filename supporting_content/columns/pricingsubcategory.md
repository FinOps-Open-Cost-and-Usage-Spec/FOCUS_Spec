# Column: PricingSubcategory

## Discussion

Separating PricingModel into 2 distinct categories could address some of the concerns around "on-demand" being too broad of a group that applies to multiple pricing models. This would also allow for a more granular view of the pricing models used by cloud providers.

PricingCategory and PricingSubcategory should be used together to describe the pricing model used for a charge. For example, a charge that leverages a spot price based on market demand would have a PricingCategory of "Dynamic" and a PricingSubcategory of "Spot".

Alternatives considered:

- ChargeSubcategory for "On-Demand" with PricingModel as a breakdown.
  - This seemed to overload ChargeSubcategory too much, which would make it lose its purpose.
- PricingModelType as a provider-specific columns to describe the type of pricing using provider terms.
  - This information should be in SKU columns and need not be explicitly in the pricing-related columns.

Should we have "Fixed" pricing for purchases? It could have "All Upfront", "Partial Upfront", and "No Upfront" as subcategories.

See [Discount Handling notes](../attributes/discount_handling.md) for details about the various pricing options that enable practitioners to save compared to their on-demand prices.

Spot pricing details:

1. _"The spot price is the current market price of a security, currency, or commodity available to be bought/sold for immediate settlement. In other words, it is the price at which the sellers and buyers value an asset right now."<br>Source: https://corporatefinanceinstitute.com/resources/career-map/sell-side/capital-markets/spot-price_
2. _"The spot price is the current price in the marketplace at which a given asset—such as a security, commodity, or currency—can be bought or sold for immediate delivery. While spot prices are specific to both time and place, in a global economy the spot price of most securities or commodities tends to be fairly uniform worldwide when accounting for exchange rates. In contrast to the spot price, a futures price is an agreed upon price for future delivery of the asset."<br>Source: https://www.investopedia.com/terms/s/spotprice.asp_

Why are PricingSubcategory and CommitmentDiscountCategory so similar when PricingCategory is "Commitment-Based"?

- PricingSubcategory describes the pricing model used for commitment-based discounts.
- CommitmentDiscountCategory provides a provider-agnostic grouping of commitment-based discount types.
- While the two columns are similar _today_, they serve different purposes and could possibly differ in the future.
