# Property: ProcessingTier (SkuPriceDetails)

Background for the FOCUS-defined `ProcessingTier` property of `SkuPriceDetails`, added under FR #2437. Records why the property exists, why it carries allowed values rather than examples, how the value set was chosen, how it relates to `PricingCategory`, and what was left out of scope.

## The Axis

Service providers price the same AI model at more than one processing tier. Each tier trades processing speed or availability against price, and each is metered on its own SKU. The tier is a property of the price: two charges for the same model and the same token direction carry different unit prices because one was billed at a batch rate and the other at a standard rate.

Each provider exposes the axis differently. The table below reflects provider documentation reviewed in November 2026.

| Provider | Term for the axis | Levels | Price relative to Standard |
|---|---|---|---|
| AWS Bedrock | "service tier" (`service_tier` parameter), plus batch inference | Priority, Standard (`default`), Flex; Batch | Priority +75%, Flex -50%, Batch -50% |
| Google Cloud Vertex AI | "consumption options" | Priority PayGo, Standard PayGo, Flex PayGo; Batch | Priority 1.8x, Flex 0.5x, Batch 0.5x |
| OpenAI | "service tier" (`service_tier` parameter), plus the Batch API | priority, default, flex; Batch | Priority premium, Flex and Batch about 0.5x |
| Azure OpenAI | "deployment type", plus priority processing | Global Standard, Global Priority, Global Batch (and Data Zone variants) | Priority premium, Batch -50% |
| Anthropic | "service tier" (`service_tier` in the usage object) | Standard, Priority Tier, Batch | Batch -50%; Priority Tier is commitment-based |

Every provider in the table distinguishes a default synchronous tier and an asynchronous batch tier. Four of five offer a premium synchronous tier, and three offer a discounted synchronous tier. The levels converge on four words: Standard, Priority, Flex, and Batch.

## Why Allowed Values

The FR asked for a common value set, and its maintainer assessment identified that the mechanism in place when the FR was filed could not deliver one: every FOCUS-defined string property in `SkuPriceDetails` was illustrated with examples, and the requirements constrained property type but not value.

That changed with PR #2682 (FR #2099), which added the requirement that a FOCUS-defined property value be one of the allowed values specified for that property, and gave `TokenCacheAction` and `TokenDirection` closed value lists with one requirement per value. `ProcessingTier` follows that precedent. Without it, the cross-provider comparison in Scenario A against Scenario B of the appendix would hold only where providers happened to choose the same words, and the provider table above shows that they do not: `default` against Standard, PayGo suffixes, and deployment-type names.

`RegionScope` (FR #2414, PR #2613) takes the other route and lists examples, leaving values to the provider. The difference is the convergence in the table above. Region scope vocabularies diverge across providers at the middle level, while processing tier vocabularies converge on four levels.

## The Value Set

| Value | Defined by | Why this word |
|---|---|---|
| `Standard` | The default synchronous processing a provider offers | Used by AWS, Google Cloud, Azure, and Anthropic. OpenAI's `default` maps to it. |
| `Priority` | Synchronous processing served ahead of `Standard` | Used by all five providers. |
| `Flex` | Synchronous processing served after `Standard` | Used by AWS, Google Cloud, and OpenAI. |
| `Batch` | Asynchronous processing of work submitted as a job and completed within a stated window | Used by all five providers. |
| `Other` | A processing tier to which none of the other values apply | Follows the `TokenCacheAction` precedent, so a new provider tier does not force a spec change before it can be represented. |

Each value is defined by processing behavior rather than by price. Prices differ by model and provider (Priority is +75% on AWS and 1.8x on Google Cloud), so a price-based definition would not classify consistently. The requirements state the order in which tiers are served, which is what each provider documents.

`Flex` and `Batch` are kept apart even where they carry the same price, as they do in Scenario B of the appendix. Flex is a synchronous call with relaxed latency, and Batch is an asynchronous job with a completion window. Practitioners moving a workload from Standard need to know which of the two it would move to, since the engineering change differs.

## Relationship to PricingCategory

`PricingCategory` describes the pricing model of a charge: "Standard" for pricing predetermined at the agreed upon rate, "Dynamic" for a variable rate the provider can change without notice, and "Committed" for reduced pricing from an applied commitment discount. Every processing tier in the table above is a predetermined rate, so `PricingCategory` is "Standard" on all of them.

`Flex` is the case most likely to be misread. It is lower priority, and the `PricingCategory` "Dynamic" description names interruptible or low priority resources as an example. Flex is not dynamically priced, though: its rate is published and fixed, so the lower priority is a property of the tier, not of the pricing model. "Standard" therefore appears twice on a "Standard" tier row, once in `PricingCategory` and once in `ProcessingTier`, with different meanings. Footnote 5 on `SkuPriceDetails` states this.

## Billed Tier, Not Requested Tier

Google Cloud bills Priority PayGo requests served without spare priority capacity at Standard PayGo rates. Anthropic's `service_tier="auto"` falls back from Priority Tier to Standard. In both cases the usage response reports the tier assigned rather than the tier requested.

`ProcessingTier` is a property of the SKU Price, so it can only describe the tier at which a price applies. Tokens requested at Priority and billed at Standard appear on the Standard row. Scenario B of the appendix shows this. A practitioner measuring how often priority requests fall back cannot do it from the Cost and Usage dataset alone, since nothing on the Standard row records what was requested.

## Naming

The FR proposed `ProcessingTier`, and this PR keeps it.

| Candidate | Why not |
|---|---|
| `ServiceTier` | The term AWS, OpenAI, and Anthropic use for the API parameter. In FOCUS, "service" names a column family (`ServiceName`, `ServiceCategory`, `ServiceSubcategory`) with a different meaning, and `ServiceTier` reads as a tier of the service rather than of processing. |
| `InferenceTier` | Accurate for every current case, but ties the key to AI. Processing tiers with the same shape may appear on non-AI services (e.g., batch and priority queues on transcoding or data processing services). |
| `ConsumptionOption` | Google Cloud's term. It also covers provisioned throughput, which is out of scope here. |
| `Tier` | Bare, and collides with quantity-based pricing tiers, which the `SkuPriceDetails` introduction already calls "tiers". |

The word "tier" is shared with quantity-based pricing tiers in the SKU Price dataset. The qualifier "Processing" distinguishes the two, and footnote 5 states that quantity-based tiers are not values of this property.

## Out of Scope

* **Provisioned throughput and reserved capacity.** Azure's Provisioned deployment type, AWS reserved capacity, Google Cloud Provisioned Throughput, OpenAI Scale Tier, and Anthropic's Priority Tier commitments are capacity bought through a commitment. They belong to FR #2371, which addresses them as commitment constructs. Footnote 5 excludes them from `ProcessingTier`.
* **Region scope.** Azure prices Priority and Batch in Global and Data Zone variants. That is the region scope axis of FR #2414, orthogonal to processing tier, and a row may carry both properties.
* **Context window size.** FR #2521, also orthogonal.

## Open Questions

* **SKU property or SKU price property.** The same question raised on FR #2414. The appendix gives each tier its own `SkuId`, as most providers do, but a provider could price tiers under one SKU with separate SKU Prices. The property works either way, since it sits in `SkuPriceDetails`.
* **Non-AI services.** No FOCUS example yet uses `ProcessingTier` outside AI. The definitions do not depend on AI, so the property is not restricted to it.
* **Interaction with FR #2371.** Before either publishes, FR #2371 should confirm that it treats provisioned capacity as a commitment construct rather than as a processing tier value.

## Reference

* FR #2437, Distinguish AI inference processing tiers
* PR #2682 (FR #2099), which introduced allowed values for FOCUS-defined `SkuPriceDetails` properties
* PR #2613 (FR #2414), RegionScope, for the property pattern this PR follows
* [AWS Bedrock service tiers](https://docs.aws.amazon.com/bedrock/latest/userguide/service-tiers-inference.html)
* [Google Cloud Vertex AI consumption options](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/deploy/consumption-options)
* [OpenAI Priority processing FAQ](https://help.openai.com/en/articles/11647665-priority-processing-faq)
* [Azure OpenAI pricing](https://azure.microsoft.com/pricing/details/azure-openai/)
* [Anthropic service tiers](https://platform.claude.com/docs/en/api/service-tiers)
