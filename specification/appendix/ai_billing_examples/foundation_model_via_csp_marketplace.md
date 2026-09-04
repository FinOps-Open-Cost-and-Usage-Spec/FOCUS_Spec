# Foundation Model via CSP Marketplace

For this scenario, Acme Corp consumes a Solora AI model through a cloud provider marketplace operated by Aura Web:

* Cache read input tokens are priced at $0.20 per 1,000,000 tokens, and cache write input tokens at $2.50 per 1,000,000 tokens.
* During the [*charge period*](#glossary:chargeperiod), the workload consumes 50,000,000 cache read input tokens and 15,000,000 cache write input tokens.

[**CSV Example**](/specification/data/ai_billing/foundation_model_via_csp_marketplace.csv)

Note the following details in the example dataset:

* [InvoiceIssuerName](#datamodel.costandusage.invoiceissuername) is "Aura Web" while [ServiceProviderName](#datamodel.costandusage.serviceprovidername) and [HostProviderName](#datamodel.costandusage.hostprovidername) are "Solora AI", which matches the participating entity arrangement described in [Participating Entity Identification](#appendix.examples:participatingentityidentification) for a service resold through a marketplace.
* Cache reads and cache writes are metered separately, using [SkuMeter](#datamodel.costandusage.skumeter) values of "Cache Read Input Tokens" and "Cache Write Input Tokens", each with its own [SkuId](#datamodel.costandusage.skuid) and rate. The TokenType property of *SkuPriceDetails* labels each row "CacheRead" or "CacheWrite", so cache operations can be grouped by token type independently of the meter name.
* The x_ContextWindow property of [SkuPriceDetails](#datamodel.costandusage.skupricedetails) records the model context window in tokens. It is expressed as a string because it describes the model rather than a quantity priced per [PricingUnit](#datamodel.costandusage.pricingunit). Properties prefixed with `x_` are provider-defined rather than FOCUS-defined, as required for *SkuPriceDetails* properties.
* The x_ContextWindow property of *SkuPriceDetails* records the model context window in tokens. It is expressed as a string because it describes the model rather than a quantity priced per *PricingUnit*. Properties prefixed with `x_` are provider-defined rather than FOCUS-defined, as required for *SkuPriceDetails* properties.
