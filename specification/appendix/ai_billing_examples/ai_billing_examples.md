# Examples: AI Billing

The following examples illustrate how a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) represents usage-based billing for foundation model APIs, where consumption is measured in tokens rather than in the compute, storage, or networking units common to infrastructure services. Provider and model names below are illustrative.

## Baseline Scenario

The following conditions apply to the scenarios below:

* Acme Corp runs generative AI workloads billed on token consumption.
* Input and output tokens are priced separately, denominated per 1,000,000 tokens, so each token type is carried as its own row rather than blended into a single rate.
* Token billing is represented using existing Cost and Usage columns. No AI-specific column is required.

Note the following column usage common to the scenarios below:

* [ConsumedQuantity](#datamodel.costandusage.consumedquantity) and [ConsumedUnit](#datamodel.costandusage.consumedunit) carry the raw token count and unit of measure.
* [PricingQuantity](#datamodel.costandusage.pricingquantity) and [PricingUnit](#datamodel.costandusage.pricingunit) carry the same consumption expressed in the [*block pricing*](#glossary:block-pricing) increment the provider prices against.
* [SkuId](#datamodel.costandusage.skuid) identifies the priced model offering and [SkuMeter](#datamodel.costandusage.skumeter) distinguishes the token type being charged.
* [ServiceCategory](#datamodel.costandusage.servicecategory) is "AI and Machine Learning" and [ServiceSubcategory](#datamodel.costandusage.servicesubcategory) is "Generative AI".
* Model identity is carried in [SkuPriceDetails](#datamodel.costandusage.skupricedetails) using the properties described in the [Examples: AI Model Identity](#appendix.examples:aimodelidentity) section, which are not restated here.

> **Note:** The examples in this section populate a `PrincipalId` column to identify the actor associated with each charge. That column is proposed and not yet part of the specification. See [PR #2360](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2360).

The following examples illustrate three foundation model billing scenarios. A model served by a cloud provider as its own first-party service is covered in the *Examples: AI Model Identity* section. Charges for a model and its underlying infrastructure appearing on the same invoice are outside the scope of this section.

| Example | Invoice Issuer | Service Provider | Focus |
| :--- | :--- | :--- | :--- |
| Per-Token Foundation Model API | Solora AI | Solora AI | Model developer bills the customer directly |
| Multi-Model Usage | Solora AI | Solora AI | Multiple models on one invoice, each priced separately |
| Foundation Model via CSP Marketplace | Aura Web | Solora AI | Cloud provider invoices for a third-party model |
