# Multi-Model Invoice via CSP Marketplace

For this scenario, Acme Corp consumes three Solora Atlas models through a cloud provider marketplace operated by LatticeScale, with cache meters on one of the models:

* Solora Atlas 5.6 Jupiter is priced at $5.00 per 1,000,000 input tokens and $30.00 per 1,000,000 output tokens.
* Solora Atlas 5.6 Mars is priced at $2.50 per 1,000,000 input tokens and $15.00 per 1,000,000 output tokens.
* Solora Atlas 5.6 Venus is priced at $1.00 per 1,000,000 input tokens and $6.00 per 1,000,000 output tokens, with cache read input tokens at $0.10 per 1,000,000 tokens and cache write input tokens at $1.25 per 1,000,000 tokens.
* During the [*charge period*](#glossary:chargeperiod), the workload consumes 100,000,000 input and 50,000,000 output tokens on Jupiter; 5,000,000 input and 1,500,000 output tokens on Mars; and 750,000 input, 250,000 output, 100,000 cache read input, and 80,000 cache write input tokens on Venus.

[**CSV Example**](/specification/data/ai_billing/multi_model_invoice_via_csp_marketplace.csv)

Note the following details in the example dataset:

* [InvoiceIssuerName](#datamodel.costandusage.invoiceissuername), [ServiceProviderName](#datamodel.costandusage.serviceprovidername), and [HostProviderName](#datamodel.costandusage.hostprovidername) are all "LatticeScale", the cloud marketplace operator. Model identity still attributes each model to Solora AI through SkuPriceDetails. As with other marketplace and managed-inference arrangements, the three participating-entity columns name the platform rather than the model developer.
* Three models share one invoice and service name, while [SkuId](#datamodel.costandusage.skuid) and the ModelId property of [SkuPriceDetails](#datamodel.costandusage.skupricedetails) distinguish each model and rate structure.
* Cache read and cache write input tokens appear only on Venus, using [SkuMeter](#datamodel.costandusage.skumeter) values of "Cache Read Input Tokens" and "Cache Write Input Tokens", with the TokenCacheAction property of *SkuPriceDetails* labeling those rows "Read" or "Write" and TokenDirection "Input".
* Representing each model and token type as its own row keeps unit rates comparable across models on the same marketplace invoice.
