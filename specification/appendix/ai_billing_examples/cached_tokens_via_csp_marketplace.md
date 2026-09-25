# Cached Tokens via CSP Marketplace

For this scenario, Acme Corp consumes a Solora AI model through a cloud provider marketplace operated by Aura Web:

* Cache read input tokens are priced at $0.20 per 1,000,000 tokens, and cache write input tokens at $2.50 per 1,000,000 tokens.
* During the [*charge period*](#glossary:chargeperiod), the workload consumes 50,000,000 cache read input tokens and 15,000,000 cache write input tokens.

[**CSV Example**](/specification/data/ai_billing/cached_tokens_via_csp_marketplace.csv)

Note the following details in the example dataset:

* This dataset is a cache-only slice of a larger workload: uncached input and output token rows are omitted so the example can focus on cache read and cache write metering.
* [ServiceProviderName](#datamodel.costandusage.serviceprovidername) is "Solora AI", the marketplace seller (model developer). [HostProviderName](#datamodel.costandusage.hostprovidername) and [InvoiceIssuerName](#datamodel.costandusage.invoiceissuername) are "Aura Web", the CSP that hosts the offering and issues the invoice. This matches Participating Entity Identification scenario 3.1.3 (marketplace seller as service provider; CSP as host and invoice issuer). Because HostProviderName differs from ServiceProviderName, the customer selected the host or the seller exposes the host.
* Model identity attributes the underlying model to Solora AI through SkuPriceDetails (ModelDeveloper, ModelFamily, ModelId, ModelVersion).
* Attributing spend to the model developer remains possible even though the charge settles through the cloud provider, which matters when the same model is consumed through more than one channel.
* Cache reads and cache writes are metered separately, using [SkuMeter](#datamodel.costandusage.skumeter) values of "Cache Read Input Tokens" and "Cache Write Input Tokens", each with its own [SkuId](#datamodel.costandusage.skuid) and rate. The TokenCacheAction property of [SkuPriceDetails](#datamodel.costandusage.skupricedetails) labels each row "Read" or "Write", with TokenDirection "Input", so cache operations can be grouped independently of the meter name.
