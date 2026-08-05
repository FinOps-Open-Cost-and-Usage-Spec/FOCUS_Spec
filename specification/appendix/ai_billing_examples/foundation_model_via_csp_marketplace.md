# Foundation Model via CSP Marketplace

For this scenario, Acme Corp consumes a Solora AI model through a cloud provider marketplace operated by Aura Web:

* Cached input tokens are priced at $0.20 per 1,000,000 tokens, and cached output tokens at $2.50 per 1,000,000 tokens.
* During the [*charge period*](#glossary:chargeperiod), the workload consumes 50,000,000 cached input tokens and 15,000,000 cached output tokens.

[**CSV Example**](/specification/data/ai_billing/foundation_model_via_csp_marketplace.csv)

Note the following details in the example dataset:

* [InvoiceIssuerName](#datamodel.costandusage.invoiceissuername) is "Aura Web" while [ServiceProviderName](#datamodel.costandusage.serviceprovidername) and [HostProviderName](#datamodel.costandusage.hostprovidername) are "Solora AI", which matches the participating entity arrangement described in [Participating Entity Identification](#appendix.examples:participatingentityidentification) for a service resold through a marketplace.
* Attributing spend to the model developer remains possible even though the charge settles through the cloud provider, which matters when the same model is consumed through more than one channel.
* Cached tokens are metered separately from uncached tokens, using *SkuMeter* values of "Input Cache" and "Output Cache", each with its own *SkuId* and rate.
* The x_ContextWindow property of *SkuPriceDetails* records the model context window in tokens. It is expressed as a string because it describes the model rather than a quantity priced per *PricingUnit*. Properties prefixed with `x_` are provider-defined rather than FOCUS-defined, as required for *SkuPriceDetails* properties.
