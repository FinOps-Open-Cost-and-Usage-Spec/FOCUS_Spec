# Examples: AI Context Window Pricing

The following examples illustrate how a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) uses the FOCUS-defined [SKU Price Details](#datamodel.costandusage.skupricedetails) properties ContextWindowMinimum and ContextWindowMaximum to identify the context-window pricing tier of each [*charge*](#glossary:charge). Provider and model names below are illustrative.

Some [*service providers*](#glossary:service-provider) price an [*AI model*](#glossary:ai-model) differently depending on how many input [*tokens*](#glossary:token), including cached input *tokens*, a single request consumes. Each tier is a distinct [*SKU Price*](#glossary:sku-price), and every price in the tier (input, output, cache read, and cache write) carries the same bounds. Because the bounds sit on each charge, a practitioner can group or filter spend by tier without a catalog join and without parsing [SKU Meter](#datamodel.costandusage.skumeter) or [Charge Description](#datamodel.costandusage.chargedescription) text.

## Baseline Scenario

The following conditions apply to the scenarios below:

* Acme Corp uses per-token AI model APIs from two *service providers*. Each *service provider* publishes one set of prices for shorter requests and another for longer requests.
* Each tier of each token meter is its own SKU Price, with its own [SkuPriceId](#datamodel.costandusage.skupriceid). The tiers of a meter share a [SkuId](#datamodel.costandusage.skuid).
* Acme Corp pays list price, so [ListCost](#datamodel.costandusage.listcost), [ContractedCost](#datamodel.costandusage.contractedcost), [BilledCost](#datamodel.costandusage.billedcost), and [EffectiveCost](#datamodel.costandusage.effectivecost) are equal on every row, and each equals [ListUnitPrice](#datamodel.costandusage.listunitprice) multiplied by [PricingQuantity](#datamodel.costandusage.pricingquantity).
* All prices are fictitious round values for illustration.

> **Note:** The FOCUS-defined SKU Price Details properties are listed in alphabetical order; the ordering is presentational and does not imply precedence.

## Scenario A: Exclusive Published Threshold

For this scenario, Acme Corp purchases Solora Reasoning Pro directly from Solora AI, which publishes one price for requests of up to 200,000 input tokens and another for requests over 200,000 input tokens. It prices input tokens, output tokens, cache reads, and cache writes in both tiers. Acme Corp also uses Solora General, whose price does not depend on context-window size.

[**CSV Example**](/specification/data/ai_context_window_pricing/ai_context_window_pricing_a.csv)

Note the following details in the example dataset:

* "Over 200,000" converts directly to a boundary of 200000. The standard tier carries ContextWindowMinimum 0 and ContextWindowMaximum 200000, and the long-context tier carries ContextWindowMinimum 200000 and a ContextWindowMaximum of null. A request of exactly 200,000 input tokens falls in the standard tier only.
* Each tier encodes its bounds in its SkuPriceId, for example "SOLORA-REASONING-PRO-INPUT-0-200000" and "SOLORA-REASONING-PRO-INPUT-200000-PLUS".
* All four token meters in a tier carry the same bounds. The tier is selected by the input tokens the request consumes, including cached input tokens, so the output row of a long request carries the long-context bounds even though its tokens are output tokens, and the cache rows carry them because cached tokens count toward the request's input.
* TokenDirection and TokenCacheAction continue to identify the direction of the metered tokens and their interaction with the cache. ContextWindowMinimum and ContextWindowMaximum identify a separate pricing qualifier, not an additional value of either property.
* The Solora General row carries neither ContextWindowMinimum nor ContextWindowMaximum, because its price does not depend on context-window size. It is not represented as a tier from 0 to null.
* A Cost and Usage row aggregates many requests over the [*charge period*](#glossary:chargeperiod). The data generator assigns each request's tokens to the SkuPriceId of the matching tier before aggregation, so the tier of a row cannot be derived from its [ConsumedQuantity](#datamodel.costandusage.consumedquantity).

## Scenario B: Inclusive Published Threshold

For this scenario, Acme Corp uses Meridian Command from Meridian AI, which publishes one price for requests below 128,000 input tokens and another for requests of 128,000 input tokens and above. It prices uncached input tokens, output tokens, and cached input tokens. Meridian AI does not bill cache writes, and does not include them in the uncached input meter.

[**CSV Example**](/specification/data/ai_context_window_pricing/ai_context_window_pricing_b.csv)

Note the following details in the example dataset:

* "128,000 input tokens and above" includes the threshold in the long-context tier. Token counts are whole numbers, so the inclusive starting threshold converts to an exclusive lower bound one token below it, 127999. The standard tier carries ContextWindowMinimum 0 and ContextWindowMaximum 127999, and the long-context tier carries ContextWindowMinimum 127999 and a ContextWindowMaximum of null. A request of exactly 128,000 input tokens falls in the long-context tier, as the published terms state.
* The data generator makes this conversion once, so a practitioner applies the same comparison to every *service provider*: a request falls in a tier when its input token count is strictly greater than ContextWindowMinimum and, when ContextWindowMaximum is not null, less than or equal to ContextWindowMaximum.
* There is no cache write row, because Meridian AI does not bill cache writes. The "Input Tokens" rows hold only tokens that were neither served from nor placed into the cache, so they carry TokenCacheAction "Uncached".

## Spend by Context-Window Tier

Grouping BilledCost by [ServiceProviderName](#datamodel.costandusage.serviceprovidername), the ModelId property, [BillingCurrency](#datamodel.costandusage.billingcurrency), and the two bounds gives the following totals across both CSVs:

| ServiceProviderName | ModelId | BillingCurrency | ContextWindowMinimum | ContextWindowMaximum | BilledCost |
| :--- | :--- | :--- | ---: | ---: | ---: |
| Solora AI | solora-reasoning-pro | USD | 0 | 200000 | 22.2 |
| Solora AI | solora-reasoning-pro | USD | 200000 | *null* | 15.8 |
| Solora AI | solora-general | USD | *absent* | *absent* | 3.0 |
| Meridian AI | meridian-command | USD | 0 | 127999 | 13.4 |
| Meridian AI | meridian-command | USD | 127999 | *null* | 5.2 |

* Each group sums every token meter in the tier, so the Solora Reasoning Pro standard tier is 8.0 + 8.0 + 1.2 + 5.0 = 22.2 and its long-context tier is 4.0 + 6.0 + 0.8 + 5.0 = 15.8.
* The Solora General row stays in its own group. A charge without the properties is not standard-context spend.
* The same query applies to both *service providers*, even though one publishes an exclusive threshold and the other an inclusive one, because the conversion happened when the data was generated.
