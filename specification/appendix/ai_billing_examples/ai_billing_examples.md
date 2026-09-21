# Examples: AI Billing

The following examples illustrate how a [Cost and Usage](#datamodel.costandusage) [*FOCUS dataset*](#glossary:FOCUS-dataset) represents usage-based billing for frontier model APIs, where consumption is measured in tokens rather than in the compute, storage, or networking units common to infrastructure services. Provider and model names below are illustrative.

## Baseline Scenario

The following conditions apply to the scenarios below:

* Acme Corp runs generative AI workloads billed on token consumption.
* Input and output tokens are priced separately, denominated per 1,000,000 tokens, so each token type is carried as its own row rather than blended into a single rate.
* Token billing is represented using existing Cost and Usage columns. No AI-specific column is needed.

Note the following column usage on the token usage rows in the scenarios below:

* [ConsumedQuantity](#datamodel.costandusage.consumedquantity) and [ConsumedUnit](#datamodel.costandusage.consumedunit) carry the raw token count and unit of measure.
* [PricingQuantity](#datamodel.costandusage.pricingquantity) and [PricingUnit](#datamodel.costandusage.pricingunit) carry the same consumption expressed in the [*block pricing*](#glossary:block-pricing) increment the provider prices against.
* [SkuId](#datamodel.costandusage.skuid) identifies the priced model offering and [SkuMeter](#datamodel.costandusage.skumeter) distinguishes the token type being charged.
* [ServiceCategory](#datamodel.costandusage.servicecategory) is "AI and Machine Learning" and [ServiceSubcategory](#datamodel.costandusage.servicesubcategory) is "Generative AI".
* Model identity is carried in [SkuPriceDetails](#datamodel.costandusage.skupricedetails) using the properties described in the [Examples: AI Model Identity](#appendix.examples:aimodelidentity) section, which are not restated here.
* The TokenDirection and TokenCacheAction properties of SkuPriceDetails label the direction of the metered tokens and their interaction with a cache, independently of the SkuMeter name.
* [PrincipalId](#datamodel.costandusage.principalid) identifies the [*principal*](#glossary:principal) associated with a charge, where one applies.

The following examples illustrate frontier model billing scenarios across direct billing, multiple models on one invoice, cloud marketplace resale, a cloud provider first-party offering, commitment drawdown, and cached token metering. Charges for a model and its underlying infrastructure appearing on the same invoice are outside the scope of this section.

| Example | Invoice Issuer | Service Provider | Focus |
| :--- | :--- | :--- | :--- |
| Per-Token Frontier Model API | Solora AI | Solora AI | Model developer bills the customer directly |
| Multi-Model Usage | Solora AI | Solora AI | Multiple models on one invoice, each priced separately |
| Frontier Model via CSP Marketplace | Aura Web | Solora AI | Cloud provider invoices for a third-party model |
| CSP-Served Frontier Model (First-Party) | Aura Web | Aura Web | Cloud provider bills for a first-party generative AI service |
| Drawdown via Prepayment | Solora AI | Solora AI | Commitment purchase with subsequent token drawdown |
| Multi-Model Invoice via CSP Marketplace | LatticeScale | Solora AI | Multiple models and cache meters on one marketplace invoice |
