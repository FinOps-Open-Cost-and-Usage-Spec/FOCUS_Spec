# Context Window Pricing

Solora AI and Meridian AI each price an [*AI model*](#glossary:ai-model) differently depending on how many input [*tokens*](#glossary:token), including cached input *tokens*, a single request consumes. Context-window pricing is represented as one record per tier for each priced token meter, each carrying its own unit price and the same [ContextWindowMinimum](#datamodel.skuprice.contextwindowminimum) and [ContextWindowMaximum](#datamodel.skuprice.contextwindowmaximum) boundaries. These scenarios use their own fictitious price lists rather than extracts from the Aura Web rate card. All prices are fictitious round values for illustration.

The fictitious operating models include unit pricing, usage measurement, and context-window pricing. They do not include regions, purchases, commitment discounts, or quantity tier pricing, so the conditional columns for those conditions are omitted. All records are public list usage rates, globally eligible, with a null ContractId.

[**CSV Example: Scenario A**](/specification/data/sku_price_examples/sku_price_context_window_a.csv)

[**CSV Example: Scenario B**](/specification/data/sku_price_examples/sku_price_context_window_b.csv)

Note the following details in the example dataset:

* Each tier of each token meter carries its own [SkuPriceId](#datamodel.skuprice.skupriceid), encoding its boundaries, for example "SOLORA-REASONING-PRO-INPUT-0-200000" and "SOLORA-REASONING-PRO-INPUT-200000-PLUS". The tiers of a meter share a [SkuId](#datamodel.skuprice.skuid).
* ContextWindowMinimum is an exclusive lower bound and ContextWindowMaximum is an inclusive upper bound, the same convention as [QuantityTierMinimum](#datamodel.skuprice.quantitytierminimum) and [QuantityTierMaximum](#datamodel.skuprice.quantitytiermaximum). The tiers cover the following request sizes, measured in input tokens per request:

| Service provider | Published threshold | Request size | ContextWindowMinimum | ContextWindowMaximum |
| :--- | :--- | :--- | ---: | ---: |
| Solora AI | "Over 200,000" | Up to and including 200,000 | 0 | 200000 |
| Solora AI | "Over 200,000" | Above 200,000 | 200000 | *null* |
| Meridian AI | "128,000 and above" | Below 128,000 | 0 | 127999 |
| Meridian AI | "128,000 and above" | 128,000 and above | 127999 | *null* |

* Meridian AI's inclusive threshold converts to an exclusive lower bound one token below it, because token counts are whole numbers. A request of exactly 128,000 input tokens falls in the long-context tier, and a request of exactly 200,000 input tokens falls in the Solora AI standard tier.
* Every record in a tier carries the same boundaries, including the output and cache records, because the tier is selected by the input tokens the request consumes.
* The Solora General record has a null ContextWindowMinimum and a null ContextWindowMaximum, because its price does not depend on context-window size. It is not represented as a tier from 0 to null.
