---
dataset: CostAndUsage
---

# Per-Token AI Model API

For this scenario, Acme Corp consumes an AI model API billed directly by the model developer, Solora AI:

* Input tokens are priced at $5.00 per 1,000,000 tokens, and output tokens at $25.00 per 1,000,000 tokens.
* During the [charge period](#term), the workload consumes 8,400,000 input tokens and 2,100,000 output tokens.

[**CSV Example**](/specification/data/ai_model_billing/per_token_ai_model_api.csv)

Note the following details in the example dataset:

* Solora AI is both the [service provider](#term) and the [invoice issuer](#term), so [ServiceProviderName](#col), [HostProviderName](#col), and [InvoiceIssuerName](#col) are all "Solora AI".
* Each token type is a separate [SKU](#term), distinguished by [SkuMeter](#col) values of "Input Tokens" and "Output Tokens", because the two are priced at different rates.
* [ConsumedQuantity](#col) holds the raw token count and [ConsumedUnit](#col) is "Tokens", while [PricingQuantity](#col) holds the same consumption expressed in the priced block and [PricingUnit](#col) is "1000000 Tokens", so 8,400,000 consumed tokens correspond to a [PricingQuantity](#col) of 8.40.
* No [commitment discount](#term) applies, so [PricingCategory](#col) is ["Standard"](#val:CostAndUsage.PricingCategory) and [BilledCost](#col), [EffectiveCost](#col), [ListCost](#col), and [ContractedCost](#col) are equal on both rows.
