# Context-window pricing

This document records design intent and is not normative.

Background for [FR #2521](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2521). Some service providers price an AI model differently depending on how many input tokens a single request consumes. A charge and a catalog record both need to identify the input-token range for which a SKU Price applies. That range is not the maximum context length of the model, the observed length of a request, a quantity tier measured in the Pricing Unit, or a token direction or cache action.

This note is self-contained. A 24-model inventory, as of November 3, is in the [November 3 inventory comment](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2521#issuecomment-6611147187). Published threshold wording is in the [November 4 boundary-wording comment](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2521#issuecomment-6633163337) on [FR #2521](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2521).

## Placements considered

* Provider-specific `x_` keys in SKU Price Details. No change to the specification, but no cross-provider query.
* FOCUS-defined ContextWindowMinimum and ContextWindowMaximum properties in SKU Price Details on Cost and Usage. Each charge carries its range without a catalog join.
* Named Context Window Minimum and Context Window Maximum columns in the SKU Price dataset. The catalog carries the range as named fields.
* Carrying the bounds in both places, sharing one definition. When a provider delivers both the Cost and Usage dataset and the SKU Price dataset, the provider fills in the same bounds in both. Practitioners read whichever dataset they use.

Task Force 1 discussed this on November 10, and carrying the bounds in both places is the direction for now; see the [November 10 Task Force 1 record](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2521#issuecomment-6780497157). The SKU Price dataset is still a preview, and some providers and practitioners do not yet use it, so the design supports both the properties on Cost and Usage, which is generally available, and the columns in SKU Price. The two representations are intended to carry the same values: ContextWindowMinimum and ContextWindowMaximum represent the same bounds on both sides. This note does not add a requirement that they be equal. It records that baseline: the shared definition, the boundary convention, the same-values intent, and the worked-example framing. The properties are specified in SKU Price Details and the columns in the SKU Price dataset. That direction does not settle the exact key names, mandatory inclusion, or release status.

## Shared definition

ContextWindowMinimum is the exclusive lower bound, and ContextWindowMaximum the inclusive upper bound, of the input tokens consumed from a single request, including cached input tokens, for which the SKU Price applies. Every price in a tier (input, output, cache read, and cache write) carries the same range, because the tier is selected by the request's input size rather than by the tokens a given meter counts.

The range is assigned per request, before aggregation. A Cost and Usage row aggregates tokens from many requests over a charge period, so the tier of a row cannot be recovered from [ConsumedQuantity](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/12770c1a7a0b1c84ba5ec24b87eea708bedb9897/specification/datasets/cost_and_usage/columns/consumedquantity.md) or PricingQuantity.

## Boundary convention

The definition uses an exclusive minimum and an inclusive maximum, the convention of [Quantity Tier Minimum](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/12770c1a7a0b1c84ba5ec24b87eea708bedb9897/specification/datasets/sku_price/columns/quantitytierminimum.md) and [Quantity Tier Maximum](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/12770c1a7a0b1c84ba5ec24b87eea708bedb9897/specification/datasets/sku_price/columns/quantitytiermaximum.md). A request falls in a tier when its input token count is strictly greater than ContextWindowMinimum and, when ContextWindowMaximum is not null, less than or equal to ContextWindowMaximum. Adjacent tiers meet at a shared boundary value with no gap or overlap.

Providers word their thresholds differently. Token counts are whole numbers, so an inclusive starting threshold ("128,000 tokens and above") converts to an exclusive minimum one token below it (127999), while an exclusive threshold ("over 200,000") converts directly (200000). The data generator makes the conversion once, so a practitioner applies one comparison to every provider. A per-bound inclusivity flag was considered and not proposed, because every consumer query would then have to handle each combination.

When the price does not depend on context-window size, the qualifier is absent: the properties omit both keys, and the columns are null. That case is not represented as a tier from 0 to null. An unbounded top tier has a non-null minimum and a null maximum.

## Worked-example framing

The worked examples use two fictitious service providers and fictitious round prices. Solora AI publishes an exclusive threshold ("over 200,000"). Meridian AI publishes an inclusive threshold ("128,000 and above"). Solora General is a price that does not depend on context-window size. Each tier of each token meter has its own SkuPriceId, and the example identifiers are uppercase, for example `SOLORA-REASONING-PRO-INPUT-0-200000`.

| Service provider | Published threshold | Request size | ContextWindowMinimum | ContextWindowMaximum |
| :--- | :--- | :--- | ---: | ---: |
| Solora AI | "Over 200,000" | Up to and including 200,000 | 0 | 200000 |
| Solora AI | "Over 200,000" | Above 200,000 | 200000 | *null* |
| Meridian AI | "128,000 and above" | Below 128,000 | 0 | 127999 |
| Meridian AI | "128,000 and above" | 128,000 and above | 127999 | *null* |

A request of exactly 200,000 input tokens falls in the Solora AI standard tier. A request of exactly 128,000 input tokens falls in the Meridian AI long-context tier.

## Open questions

* **Zero input tokens.** With an exclusive minimum of 0, a request with zero input tokens falls in no tier. Whether any provider bills such a request has not been established.
* **Full-session wording.** Some provider pages describe the threshold as applying to a full session rather than a request. A session is not assumed to equal one request.
* **Mandatory inclusion and key names.** Whether the properties use MUST inclusion of both keys, a non-null SkuPriceDetails for prices that depend on context-window size, and an explicit JSON null for an unbounded maximum, along with the exact key names, is addressed in the properties pull request.
* **Release status.** Whether the properties enter 1.6 as a Cost and Usage change, and how the preview SKU Price columns are classified, is addressed in the properties pull request and the columns pull request.
* **Inference providers.** Whether an inference provider that serves another provider's model, or an open-weight model, follows the same context-window tiers.

## Reference

* [FR #2521](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2521) and the [November 10 Task Force 1 record](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2521#issuecomment-6780497157)
* [PR #2442](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2442) and [PR #2606](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2606), for the SKU Price Details property pattern
* [PR #2424](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2424), for the SKU Price dataset and the quantity-tier boundary convention
* [SKU Price Details](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/12770c1a7a0b1c84ba5ec24b87eea708bedb9897/specification/datasets/cost_and_usage/columns/skupricedetails.md), [Quantity Tier Minimum](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/12770c1a7a0b1c84ba5ec24b87eea708bedb9897/specification/datasets/sku_price/columns/quantitytierminimum.md), [Quantity Tier Maximum](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/12770c1a7a0b1c84ba5ec24b87eea708bedb9897/specification/datasets/sku_price/columns/quantitytiermaximum.md), [Null Handling](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/12770c1a7a0b1c84ba5ec24b87eea708bedb9897/specification/attributes/null_handling.md), and [Numeric Format](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/12770c1a7a0b1c84ba5ec24b87eea708bedb9897/specification/attributes/numeric_format.md)
