# Per-Token Foundation Model API

For this scenario, Acme Corp consumes a foundation model API billed directly by the model developer, Solora AI:

* Input tokens are priced at $5.00 per 1,000,000 tokens, and output tokens at $25.00 per 1,000,000 tokens.
* During the [*charge period*](#glossary:chargeperiod), the workload consumes 8,400,000 input tokens and 2,100,000 output tokens.

[**CSV Example**](/specification/data/ai_billing/per_token_foundation_model_api.csv)

Note the following details in the example dataset:

* Solora AI is both the [*service provider*](#glossary:service-provider) and the invoice issuer, so [ServiceProviderName](#datamodel.costandusage.serviceprovidername), [HostProviderName](#datamodel.costandusage.hostprovidername), and [InvoiceIssuerName](#datamodel.costandusage.invoiceissuername) are all "Solora AI".
* Each token type is a separate [*SKU*](#glossary:sku), distinguished by [SkuMeter](#datamodel.costandusage.skumeter) values of "Input Tokens" and "Output Tokens", because the two are priced at different rates.
* [ConsumedQuantity](#datamodel.costandusage.consumedquantity) holds the raw token count and [ConsumedUnit](#datamodel.costandusage.consumedunit) is "Tokens", while [PricingQuantity](#datamodel.costandusage.pricingquantity) holds the same consumption expressed in the priced block and [PricingUnit](#datamodel.costandusage.pricingunit) is "1000000 Tokens", so 8,400,000 consumed tokens correspond to a *PricingQuantity* of 8.40.
* No commitment discount applies, so [PricingCategory](#datamodel.costandusage.pricingcategory) is "Standard" and [BilledCost](#datamodel.costandusage.billedcost), [EffectiveCost](#datamodel.costandusage.effectivecost), [ListCost](#datamodel.costandusage.listcost), and [ContractedCost](#datamodel.costandusage.contractedcost) are equal on both rows.
