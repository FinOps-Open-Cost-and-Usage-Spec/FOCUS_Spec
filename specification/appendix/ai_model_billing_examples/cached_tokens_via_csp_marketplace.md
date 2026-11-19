---
dataset: CostAndUsage
---

# Cached Tokens via CSP Marketplace

For this scenario, Acme Corp consumes a Solora AI model through a cloud provider marketplace operated by Aura Web:

* Cache read input tokens are priced at $0.20 per 1,000,000 tokens, and cache write input tokens at $2.50 per 1,000,000 tokens.
* During the [charge period](#term), the workload consumes 50,000,000 cache read input tokens and 15,000,000 cache write input tokens.

[**CSV Example**](/specification/data/ai_model_billing/cached_tokens_via_csp_marketplace.csv)

Note the following details in the example dataset:

* This dataset is a cache-only slice of a larger workload: uncached input and output token rows are omitted so the example can focus on cache read and cache write metering.
* [ServiceProviderName](#col) is "Solora AI", the marketplace seller (model developer). [HostProviderName](#col) and [InvoiceIssuerName](#col) are "Aura Web", the CSP that hosts the offering and issues the invoice. This example shows one of several marketplace arrangements, matching [Examples: Participating Entity Identification](#appendix.examples:participatingentityidentification) scenario 3.2.2 (marketplace seller as [service provider](#term); CSP as host and [invoice issuer](#term)). Solora AI exposes that the offering runs on Aura Web infrastructure, so [HostProviderName](#col) reflects Aura Web rather than matching [ServiceProviderName](#col).
* Model identity attributes the underlying model to Solora AI through [SkuPriceDetails](#col) (ModelDeveloper, ModelFamily, ModelId, ModelVersion).
* Attributing spend to the model developer remains possible even though the charge settles through the cloud provider, which matters when the same model is consumed through more than one channel.
* Cache reads and cache writes are metered separately, using [SkuMeter](#col) values of "Cache Read Input Tokens" and "Cache Write Input Tokens", each with its own [SkuId](#col) and rate. The TokenCacheAction property of [SkuPriceDetails](#col) labels each row "Read" or "Write", with TokenDirection "Input", so cache operations can be grouped independently of the meter name.
