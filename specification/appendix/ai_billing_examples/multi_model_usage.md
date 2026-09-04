# Multi-Model Usage

For this scenario, Acme Corp routes requests across two models from the same model developer, Solora AI, depending on task complexity:

* Solora Atlas 5.5 is priced at $5.00 per 1,000,000 input tokens and $25.00 per 1,000,000 output tokens.
* Solora Atlas 5.4 Mini is priced at $0.75 per 1,000,000 input tokens and $4.50 per 1,000,000 output tokens.
* During the [*charge period*](#glossary:chargeperiod), the workload consumes 10,000,000 input and 2,000,000 output tokens on Solora Atlas 5.5, and 3,000,000 input and 500,000 output tokens on Solora Atlas 5.4 Mini.

[**CSV Example**](/specification/data/ai_billing/multi_model_usage.csv)

Note the following details in the example dataset:

* Both models are delivered through the same [*service*](#glossary:service), so [ServiceName](#datamodel.costandusage.servicename) is common to all four rows, while [SkuId](#datamodel.costandusage.skuid) and the ModelId property of [SkuPriceDetails](#datamodel.costandusage.skupricedetails) distinguish the models.
* Rate structures differ between the two models. Solora Atlas 5.5 prices output tokens at five times its input rate, while Solora Atlas 5.4 Mini prices output tokens at six times its input rate.
* Representing each token type as a separate row keeps both rate structures visible, which supports comparing cost per token across models.
