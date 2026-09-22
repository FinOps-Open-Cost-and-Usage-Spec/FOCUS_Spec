# CSP-Served Third-Party Model

For this scenario, Acme Corp consumes a Solora Jupiter model through Aura Web Foundry, a first-party generative AI service billed by the cloud provider:

* Input tokens are priced at $0.75 per 1,000,000 tokens, and output tokens at $4.50 per 1,000,000 tokens.
* During the [*charge period*](#glossary:chargeperiod), the workload consumes 3,000,000 input tokens and 500,000 output tokens.

[**CSV Example**](/specification/data/ai_billing/csp_served_third_party_model.csv)

Note the following details in the example dataset:

* Aura Web is the [*service provider*](#glossary:service-provider), host provider, and [*invoice issuer*](#glossary:invoice-issuer), so [ServiceProviderName](#datamodel.costandusage.serviceprovidername), [HostProviderName](#datamodel.costandusage.hostprovidername), and [InvoiceIssuerName](#datamodel.costandusage.invoiceissuername) are all "Aura Web", while [ServiceName](#datamodel.costandusage.servicename) is "Aura Web Foundry".
* Model identity still attributes the underlying model to Solora AI through the ModelDeveloper, ModelFamily, ModelId, and ModelVersion properties of [SkuPriceDetails](#datamodel.costandusage.skupricedetails), even though Aura Web is the billed service provider. ModelId is namespaced by the *service provider* ("aura-web.solora-jupiter-5"), matching [Scenario B in Examples: AI Model Identity](#appendix.examples:aimodelidentity).
* Aura Web serves the model as its own first-party service, the arrangement Scenario B describes with a different cloud provider, placed here so the AI Billing scenarios cover first-party serving alongside direct billing and marketplace resale.
* Each token type is a separate [*SKU*](#glossary:sku), distinguished by [SkuMeter](#datamodel.costandusage.skumeter) values of "Input Tokens" and "Output Tokens", with the TokenDirection property of *SkuPriceDetails* labeling each row "Input" or "Output".
* No [*commitment discount*](#glossary:commitment-discount) applies, so [PricingCategory](#datamodel.costandusage.pricingcategory) is "Standard" and [BilledCost](#datamodel.costandusage.billedcost), [EffectiveCost](#datamodel.costandusage.effectivecost), [ListCost](#datamodel.costandusage.listcost), and [ContractedCost](#datamodel.costandusage.contractedcost) are equal on both rows.
