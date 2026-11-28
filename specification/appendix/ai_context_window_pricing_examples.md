# Examples: AI Context Window Pricing

The following examples illustrate how a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) uses the FOCUS-defined [SKU Price Details](#datamodel.costandusage.skupricedetails) property ContextWindow to identify the context-window pricing tier of each [*charge*](#glossary:charge). Provider and model names below are illustrative.

Some [*service providers*](#glossary:service-provider) price an [*AI model*](#glossary:ai-model) differently depending on how many input [*tokens*](#glossary:token) a single request consumes, as each *service provider* counts them toward the threshold in its pricing terms. Each tier is a distinct [*SKU Price*](#glossary:sku-price), and every price in the tier (input, output, cache read, and cache write) carries the same ContextWindow. ContextWindow holds the label the *service provider* uses for the tier, so a practitioner can group or filter spend by tier without parsing [SKU Meter](#datamodel.costandusage.skumeter) or [Charge Description](#datamodel.costandusage.chargedescription) text. The value is not normalized, so it identifies a tier within one *service provider* rather than across *service providers*.

## Baseline Scenario

The following conditions apply to the scenarios below:

* Acme Corp uses per-token AI model APIs from two *service providers*. Each *service provider* publishes one set of prices for shorter requests and another for longer requests.
* Each tier of each token meter is its own SKU Price, with its own [SkuPriceId](#datamodel.costandusage.skupriceid). The tiers of a meter share a [SkuId](#datamodel.costandusage.skuid).
* Acme Corp pays list price, so [ListCost](#datamodel.costandusage.listcost), [ContractedCost](#datamodel.costandusage.contractedcost), [BilledCost](#datamodel.costandusage.billedcost), and [EffectiveCost](#datamodel.costandusage.effectivecost) are equal on every row, and each equals [ListUnitPrice](#datamodel.costandusage.listunitprice) multiplied by [PricingQuantity](#datamodel.costandusage.pricingquantity).
* All prices are fictitious round values for illustration.

> **Note:** The FOCUS-defined SKU Price Details properties are listed in alphabetical order; the ordering is presentational and does not imply precedence.

## Scenario A: Tiers Labeled with Words

For this scenario, Acme Corp purchases Solora Reasoning Pro directly from Solora AI, which labels its two tiers "Short context" and "Long context". It prices input tokens, output tokens, cache reads, and cache writes in both tiers. Acme Corp also uses Solora General, whose price does not depend on context-window size.

[**CSV Example**](/specification/data/ai_context_window_pricing/ai_context_window_pricing_a.csv)

Note the following details in the example dataset:

* ContextWindow is "Short context" on every short-context row and "Long context" on every long-context row, exactly as Solora AI names the tiers. FOCUS does not define these values.
* In this example, each tier encodes its name in its SkuPriceId (e.g., "SOLORA-REASONING-PRO-INPUT-SHORT" and "SOLORA-REASONING-PRO-INPUT-LONG"). This naming is illustrative and is not required by FOCUS.
* All four token meters in a tier carry the same ContextWindow. The tier is selected by the input tokens the request consumes, so the output row of a long request carries "Long context" even though its tokens are output tokens, and the cache rows carry it as well.
* TokenDirection and TokenCacheAction continue to identify the direction of the metered tokens and their interaction with the cache. ContextWindow identifies a separate pricing qualifier, not an additional value of either property.
* The Solora General row does not carry ContextWindow, because its price does not depend on context-window size.
* A Cost and Usage row aggregates many requests over the [*charge period*](#glossary:chargeperiod). The data generator assigns each request's tokens to the SkuPriceId of the matching tier before aggregation, so the tier of a row cannot be derived from its [ConsumedQuantity](#datamodel.costandusage.consumedquantity).

## Scenario B: Tiers Labeled with Range Text

For this scenario, Acme Corp uses Meridian Command from Meridian AI, which labels its two tiers by the size of the request: "Below 128,000 input tokens" and "128,000 input tokens and above". It prices uncached input tokens, output tokens, and cached input tokens. Meridian AI does not bill cache writes, and does not include them in the uncached input meter.

[**CSV Example**](/specification/data/ai_context_window_pricing/ai_context_window_pricing_b.csv)

Note the following details in the example dataset:

* ContextWindow holds Meridian AI's range text as a string, exactly as Meridian AI words it. The text is not converted to numeric bounds, and FOCUS does not define how it is worded.
* A practitioner reads ContextWindow as the name of a tier, not as a value to compare against token quantities. A row's token quantity aggregates many requests, so it cannot confirm the tier.
* There is no cache write row, because Meridian AI does not bill cache writes. The "Input Tokens" rows hold only tokens that were neither served from nor placed into the cache, so they carry TokenCacheAction "Uncached".

## Spend by Context-Window Tier

Grouping BilledCost by [ServiceProviderName](#datamodel.costandusage.serviceprovidername), the ModelId property, [BillingCurrency](#datamodel.costandusage.billingcurrency), and the ContextWindow property gives the following totals across both CSVs:

| ServiceProviderName | ModelId | BillingCurrency | ContextWindow | BilledCost |
| :--- | :--- | :--- | :--- | ---: |
| Solora AI | solora-reasoning-pro | USD | Short context | 22.2 |
| Solora AI | solora-reasoning-pro | USD | Long context | 15.8 |
| Solora AI | solora-general | USD | *absent* | 3.0 |
| Meridian AI | meridian-command | USD | Below 128,000 input tokens | 13.4 |
| Meridian AI | meridian-command | USD | 128,000 input tokens and above | 5.2 |

* Each group sums every token meter in the tier, so the Solora Reasoning Pro short-context tier is 8.0 + 8.0 + 1.2 + 5.0 = 22.2 and its long-context tier is 4.0 + 6.0 + 0.8 + 5.0 = 15.8.
* The Solora General row stays in its own group. A charge without the property is not short-context spend.
* The groups are compared within one *service provider*. ContextWindow values are not normalized, so "Short context" and "Below 128,000 input tokens" are not equivalent tiers.
