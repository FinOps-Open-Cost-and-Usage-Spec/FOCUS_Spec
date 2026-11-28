# Context-window pricing

This document records design intent and is not normative.

Background for FR [#2521](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2521). Some service providers price an AI model differently depending on how many input tokens a single request consumes. A charge needs to identify the context-window pricing tier to which its SKU Price applies. That tier is not the maximum context length of the model, the observed length of a request, a quantity tier measured in the Pricing Unit, or a token direction or cache action.

This note is self-contained. A 24-model inventory, as of November 3, is in the [November 3 inventory comment](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2521#issuecomment-6611147187). Published threshold wording is in the [November 4 boundary-wording comment](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2521#issuecomment-6633163337) on FR [#2521](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2521).

## Placements considered

* Provider-specific `x_` keys in SKU Price Details. No change to the specification, but no cross-provider query.
* A FOCUS-defined ContextWindow property in SKU Price Details on Cost and Usage. Each charge carries the tier label without a catalog join.
* A named column in the SKU Price dataset, delivered in a separate pull request.

## Direction

Task Force 1 discussed this on November 10 and November 24. On November 24 the group agreed to replace the two numeric bounds with one String property that holds what the service provider calls the tier, such as "long" or a token range as the provider writes it. See the [November 24 Task Force 1 record](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2521#issuecomment-7145099005).

Two observations drove the change:

* A Cost and Usage row aggregates many requests over a charge period, so a numeric bound cannot be checked against the token quantity on the row.
* Some service providers label a tier only in words (e.g., "long context") and publish no token numbers, so a numeric bound cannot be filled in for them.

## Definition

ContextWindow is the label or range text the service provider uses for the context-window pricing tier to which the SKU Price applies. The value is defined by the service provider and is not normalized, so values are not comparable across service providers. The tier is selected by the input tokens a single request consumes, as the service provider counts them toward the threshold in its pricing terms. Every price in a tier (input, output, cache read, and cache write) carries the same label, because the tier is selected by the request's input size rather than by the tokens a given meter counts.

The property is a String. It states no numeric bounds, so it carries no boundary convention, and the tier of a row is not recoverable from [ConsumedQuantity](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/12770c1a7a0b1c84ba5ec24b87eea708bedb9897/specification/datasets/cost_and_usage/columns/consumedquantity.md) or PricingQuantity.

When the price does not depend on context-window size, the property is omitted. Because null is not a label, the property is omitted rather than set to null.

## Name

The name is a bare concept name with no reserved suffix, as with SkuMeter, StorageClass, ModelFamily, and InstanceSeries, which are open, provider-defined strings. FOCUS Column Handling reserves the "Category" suffix for normalized values and requires the "Name" suffix for a column that represents a name, so neither fits a label or range text. The name also avoids the "Type" suffix, which FOCUS uses for provider values that sit under a normalized category, and "Tier", which ProcessingTier in PR [#2873](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2873) uses for a value with FOCUS-defined allowed values.

## Worked-example framing

The worked examples use two fictitious service providers and fictitious round prices. Solora AI labels its tiers with words ("Short context" and "Long context"). Meridian AI labels its tiers with range text ("Below 128,000 input tokens" and "128,000 input tokens and above"). Solora General is a price that does not depend on context-window size, so its rows omit the property. Each tier of each token meter has its own SkuPriceId, and the example identifiers are uppercase, for example `SOLORA-REASONING-PRO-INPUT-SHORT`. This naming is illustrative and is not required by FOCUS.

| Service provider | Published tier | ContextWindow |
| :--- | :--- | :--- |
| Solora AI | Shorter requests | "Short context" |
| Solora AI | Longer requests | "Long context" |
| Meridian AI | Requests below 128,000 input tokens | "Below 128,000 input tokens" |
| Meridian AI | Requests of 128,000 input tokens and above | "128,000 input tokens and above" |

## Open questions

* **Full-session wording.** Some provider pages describe the threshold as applying to a full session rather than a request. A session is not assumed to equal one request.
* **Inference providers.** Whether an inference provider that serves another provider's model, or an open-weight model, follows the same context-window tiers.
* **Release status.** Whether the property enters 1.6 as a Cost and Usage change, and how the preview SKU Price columns are classified, is addressed in the properties pull request and the columns pull request.

## Reference

* FR [#2521](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2521), the [November 10 Task Force 1 record](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2521#issuecomment-6780497157), and the [November 24 Task Force 1 record](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2521#issuecomment-7145099005)
* PR [#2442](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2442) and PR [#2606](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2606), for the SKU Price Details property pattern
* [SKU Price Details](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/12770c1a7a0b1c84ba5ec24b87eea708bedb9897/specification/datasets/cost_and_usage/columns/skupricedetails.md)
