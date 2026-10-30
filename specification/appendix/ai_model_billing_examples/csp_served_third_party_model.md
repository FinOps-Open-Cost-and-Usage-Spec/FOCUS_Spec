---
dataset: CostAndUsage
---

# CSP-Served Third-Party Model

For this scenario, Acme Corp consumes a Solora Jupiter model through Aura Web Foundry, a first-party AI model service billed by the cloud provider:

* Input tokens are priced at $0.75 per 1,000,000 tokens, and output tokens at $4.50 per 1,000,000 tokens.
* During the [charge period](#term), the workload consumes 3,000,000 input tokens and 500,000 output tokens.

[**CSV Example**](/specification/data/ai_model_billing/csp_served_third_party_model.csv)

Note the following details in the example dataset:

* Aura Web is the [service provider](#term), host provider, and [invoice issuer](#term), so [ServiceProviderName](#col), [HostProviderName](#col), and [InvoiceIssuerName](#col) are all "Aura Web", while [ServiceName](#col) is "Aura Web Foundry".
* Model identity still attributes the underlying model to Solora AI through the ModelDeveloper, ModelFamily, ModelId, and ModelVersion properties of [SkuPriceDetails](#col), even though Aura Web is the billed service provider. ModelId is namespaced by the [service provider](#term) ("aura-web.solora-jupiter-5"), matching [Scenario B in Examples: AI Model Identity](#appendix.examples:aimodelidentity).
* Aura Web serves the model as its own first-party service, the arrangement Scenario B describes with a different cloud provider, placed here so the AI Model Billing scenarios cover first-party serving alongside direct billing and marketplace purchases.
* Each token type is a separate [SKU](#term), distinguished by [SkuMeter](#col) values of "Input Tokens" and "Output Tokens", with the TokenDirection property of [SkuPriceDetails](#col) labeling each row "Input" or "Output". The input row also carries TokenCacheAction "Uncached" because Aura Web meters cache reads and cache writes separately from uncached input tokens.
* No [commitment discount](#term) applies, so [PricingCategory](#col) is ["Standard"](#val:CostAndUsage.PricingCategory) and [BilledCost](#col), [EffectiveCost](#col), [ListCost](#col), and [ContractedCost](#col) are equal on both rows.
