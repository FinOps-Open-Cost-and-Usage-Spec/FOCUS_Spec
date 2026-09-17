# Foundation Model via CSP Marketplace

For this scenario, Acme Corp consumes a Solora AI model through a cloud provider marketplace operated by Aura Web:

* Cache read input tokens are priced at $0.20 per 1,000,000 tokens, and cache write input tokens at $2.50 per 1,000,000 tokens.
* During the [*charge period*](#glossary:chargeperiod), the workload consumes 50,000,000 cache read input tokens and 15,000,000 cache write input tokens.

[**CSV Example**](/specification/data/ai_billing/foundation_model_via_csp_marketplace.csv)

Note the following details in the example dataset:

* This dataset is a cache-only slice of a larger workload: uncached input and output token rows are omitted so the example can focus on cache read and cache write metering.
* [InvoiceIssuerName](#datamodel.costandusage.invoiceissuername) is "Aura Web" while [ServiceProviderName](#datamodel.costandusage.serviceprovidername) and [HostProviderName](#datamodel.costandusage.hostprovidername) are "Solora AI", which matches the participating entity arrangement described in [Participating Entity Identification](#appendix.examples:participatingentityidentification) for a service resold through a marketplace.
* Attributing spend to the model developer remains possible even though the charge settles through the cloud provider, which matters when the same model is consumed through more than one channel.
* Cache reads and cache writes are metered separately, using [SkuMeter](#datamodel.costandusage.skumeter) values of "Cache Read Input Tokens" and "Cache Write Input Tokens", each with its own [SkuId](#datamodel.costandusage.skuid) and rate. The TokenCacheAction property of [SkuPriceDetails](#datamodel.costandusage.skupricedetails) labels each row "Read" or "Write", with TokenDirection "Input", so cache operations can be grouped independently of the meter name.
