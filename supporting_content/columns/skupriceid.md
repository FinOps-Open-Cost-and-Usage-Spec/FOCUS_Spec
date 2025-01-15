# Column: SKU Price ID

## Example provider mappings

Current column mappings found in available data sets:

| Provider | Data set                | Column                             |
| ------------ | --------------------------- | -------------------------------------- |
| AWS          | CUR                         | pricing/rate\_code \| pricing/rate\_id |
| Azure        | Cost details export or API  | Not publically available                              |
| GCP          | BigQuery Billing Export            | Not publically available, but can be derived from sku.id and price.tier_start_amount                                 |
| OCI          | Cost Reports                | Not available (no price level ID)    |

## Example scenarios for current provider data

Current values observed in billing data for various scenarios:

| Provider | Scenario               | Pattern                                                              |
| ------------ | -------------------------- | ------------------------------------------------------------------------ |
| AWS          | CUR                        | rate\_code: KF338J7FCKZPUBD9.JRTCKXETXF.6YS6EN2CT7 rate\_id: 20457007287 |
| Azure        | Cost Details export or API | Not publically available                                                                         |
| GCP          | BigQuery Billing Export                  | sku.id: 947D-3B46-7781 price.tier_start_amount: 10                                                          |
| OCI          | Cost Reports               | Not available (no price level ID)                                                |

## Discussion / Scratch space

### References

* AWS - <https://docs.aws.amazon.com/cur/latest/userguide/pricing-columns.html>
* Azure - <https://learn.microsoft.com/en-us/azure/cost-management-billing/automate/understand-usage-details-fields>
* Big Query - <https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage>
* OCI - <https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/usagereportsoverview.htm>
* Potato / Tomato v1 discussion: <https://docs.google.com/document/d/1-flGM09zj3QkjSk8hlJolujZiCzVVmwi3TxDTaFJ7qM/edit#heading=h.u4wfvautplvp>
* Potato / Tomato v2 discussion:\
<https://docs.google.com/document/d/18eL6G8WhbmEIHtrjqQlWqckgMRUQSs1aZwmwuRKQfqU/edit#heading=h.swm58hl317f3>

### Impacts of 1.0 ChargeCategory and ChargeClass cleanup

The following table serves as the basis for reviewing the SkuPriceId spec, as well as price, cost, quantity metrics, etc., impacted by the ChargeCategory and ChargeClass columns cleanup.

| ChargeCategory | ChargeClass                             | perSku/bulk                       | SkuId            | SkuPriceId       |
|----------------|-----------------------------------------|-----------------------------------|------------------|------------------|
| Usage          | Regular/Standard/Original/Direct/(null) | MUST be perSku and perSkuPrice    | MUST not be null | MUST not be null |
| Usage          | Correction                              | MAY be bulk                       | MAY be null      | MAY be null      |
| Purchase       | Regular/Standard/Original/Direct/(null) | MUST be perSku and perSkuPrice    | MUST not be null | MUST not be null |
| Purchase       | Correction                              | MAY be bulk                       | MAY be null      | MAY be null      |
| Credit         | Regular/Standard/Original/Direct/(null) | MAY be bulk                       | MAY be null      | MAY be null      |
| Credit         | Correction                              | MAY be bulk                       | MAY be null      | MAY be null      |
| Adjustment     | Regular/Standard/Original/Direct/(null) | MAY be bulk                       | MAY be null      | MAY be null      |
| Adjustment     | Correction                              | MAY be bulk                       | MAY be null      | MAY be null      |
| Tax            | Regular/Standard/Original/Direct/(null) | MUST be bulk                      | MUST be null     | MUST be null     |
| Tax            | Correction                              | MUST be bulk                      | MUST be null     | MUST be null     |

### SKU ID, SKU Price ID and SKU Price Details clarification (FOCUS 1.2)

#### General Notes

* While terminology may vary, the majority, if not all, CSP and SaaS providers have equivalent concepts to SKU ID, SKU Price ID, and SKU Price Details.
* Even if some providers do not explicitly support SKU ID, SKU Price ID, and SKU Price Details concepts, all providers must have public or custom price sheets—either published or shared directly with customers. These necessitate the ability to create and share unique identifiers for unit prices (e.g., even for a single invoice line item, providers should be able to generate a unique identifier for the product or service being charged).
* SKU ID (or equivalent): Represents a higher-level grouping construct compared to SKU Price ID. It identifies the core product configuration (e.g., virtual machine type, storage tier), independent of pricing details.
* SKU Price ID (or equivalent): Represents a specific pricing instance of a SKU. It inherits SKU properties and adds associated price-specific attributes.
* SKU Price Details (or equivalent): Represents a list of unit price properties, encompassing those related to both SKU ID and SKU Price ID. As SKU ID is a higher-level construct, properties associated with SKU Price ID are implied to inherit from the parent SKU.
* Even if concepts like SKU ID, SKU Price ID, and SKU Price Details are not currently exposed in cost and usage data or price sheets, providers should have the capability to include them over time.
* If only one identifier can be supported, the same value may appear in both SKU ID and SKU Price ID columns. Additionally, even when both concepts are supported, the same value might be used in both columns, particularly when there is only one SKU Price instance for a given SKU.

#### SKU Price ID Notes

* Current SKU Price ID column definition specifies that SKU Price ID represents the unit price used to calculate the charge, while **the composition of the properties associated with SKU Price ID may differ across providers**. While it is clear that SKU Price ID can be used for pricing-related scenarios, the varying composition of its properties across providers means that **for more specific use cases, practitioners should consult the provider's documentation**.
* To define which use cases this column can or should consistently support across providers, we need to be more specific about its purpose and provide greater clarity on:
  * **which pricing-related properties should be represented in SKU Price ID** (and included in SKU Price Details),
  * versus those that are relevant to pricing (and available in price sheets) but **should not (or even must not) be reflected in these columns**.
* Of course, these columns will always contain **provider-specific values**, but they should serve the **same purpose** and be based on a **similar concept**.
* By providing guidance on what must be included and excluded, we can establish a more consistent framework for analysis, despite variations across SKUs and providers. While it may not be feasible to explicitly define all properties that must be included (as these can vary significantly even between SKUs within a single provider), we can offer greater precision regarding which price-related properties must be excluded. As long as the SKU Price ID adheres to these requirements, the following use cases should be consistently supported:
  * **Price Analysis Over Time** by excluding dynamic or negotiable properties such as unit price amount and temporal validity (e.g., effective dates).
  * **Price Comparison Across Different Contracts** by excluding dynamic or negotiable properties such as unit price amount and contract-specific or negotiation-specific elements,

##### Suggested updates to SKU Price ID Specification

* Definition Breakdown
  * OLD:
    * A SKU Price ID is a unique identifier that defines the unit price used to calculate the charge. SKU Price ID **can be referenced** on a price list published by a provider to look up detailed information, including a corresponding list unit price. The composition of the properties associated with the SKU Price ID may differ across providers. SKU Price ID is commonly used **for analyzing cost** based on pricing properties such as Terms and Tiers.
  * NEW:
    * A SKU Price ID is a unique identifier that defines the unit price used to calculate the charge. It **can serve as a key reference** to a price list published by a provider, allowing **practitioners** to look up detailed information, including the associated list unit prices and pricing properties. **Although** the composition of properties associated with the SKU Price ID may differ across providers, **the SKU Price ID is designed to represent the core, stable properties of a SKU Price, excluding dynamic or negotiable properties such as unit price amount, currency (and related exchange rates), temporal validity (e.g., effective dates), and contract- or negotiation-specific elements (e.g., contract or account identifiers, and negotiable discounts). This ensures that the SKU Price ID remains consistent across different pricing scenarios, even though variable aspects (e.g., unit price, currency, effective dates) might fluctuate, facilitating the filtering of charges with the same stable SKU Price properties and allowing for tracking price fluctuations (e.g., changes in unit price amount) over time — for both list unit prices and contracted prices.** **The** SKU Price ID is **also** commonly used **to analyze** costs based on pricing properties such as Terms and Tiers.

* Normative requirements Breakdown:
  * OLD:
    * SkuPriceId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes a SKU price list and MUST be of type String.
    * SkuPriceId MUST define a single unit price used for calculating the charge.
    * [ListUnitPrice](#listunitprice) MUST be associated with the SkuPriceId in the provider published price list.
    * SkuPriceId MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction" and [ChargeCategory](#chargecategory) is "Usage" or "Purchase", MUST be null when ChargeCategory is "Tax", and MAY be null for all other combinations of ChargeClass and ChargeCategory.
    * A given value of SkuPriceId MUST be associated with one and only one [SkuId](#skuid), except in cases of [commitment discount flexibility](#glossary:commitment-discount-flexibility).
    * If a provider does not have a SkuPriceId and wants to include information in columns linked to SkuPriceId such as ListUnitPrice or [SkuPriceDetails](#skupricedetails), the SkuId MAY be used in the SkuPriceId column as long as it adheres to the above conditions.

  * NEW:
    * SkuPriceId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes a SKU price list and MUST be of type String.
    * SkuPriceId MUST define a single unit price used for calculating the charge, **reflecting a stable grouping of core properties of a SKU Price while excluding fluctuations in dynamic or negotiable properties such as unit price amount, currency, temporal validity (e.g., effective dates), and contract- or negotiation-specific elements.**
    * [ListUnitPrice](#listunitprice) MUST be associated with the SkuPriceId in the provider published price list **but is not inherently part of the SkuPriceId itself**.
    * SkuPriceId MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction" and [ChargeCategory](#chargecategory) is "Usage" or "Purchase", MUST be null when ChargeCategory is "Tax", and MAY be null for all other combinations of ChargeClass and ChargeCategory.
    * A given value of SkuPriceId MUST be associated with one and only one [SkuId](#skuid), except in cases of [commitment discount flexibility](#glossary:commitment-discount-flexibility).
    * If a provider does not have a SkuPriceId and wants to include information in columns linked to SkuPriceId such as ListUnitPrice or [SkuPriceDetails](#skupricedetails), the SkuId MAY be used in the SkuPriceId column as long as it adheres to the above conditions.

* Discussion topics:
  * *The SKU Price ID is also commonly used to analyze costs based on pricing properties such as Terms and Tiers.*
    * Considering that the SKU Price ID doesn't remain the same across different tiers, such an analysis would require **not only cost and unit price metrics and the SKU Price ID** but also the **SKU ID** (consistent across tiers) and **SKU Price Details** — the former to more easily filter SKUs that make sense to compare, and the latter to obtain information about the tiers.
  * *A given value of SkuPriceId MUST be associated with one and only one SkuId, **except in cases of commitment discount flexibility**.*
    * Do we need to keep on emphasizing this exception? 
    * Based on discussion in WorkItem #644, even in cases of commitment discount flexibility SkuPriceId is still associated to the same, one and only SkuId. To be more precise, in that case the SkuId, SkuPriceId, SkuPriceDetails, ListUnitPrice, and ContractedUnitPrice reflect the running resource's SKU/SKU Price-related properties, while only the unit price amount of the purchased commitment SKU Price is provided in CommitmentDiscountUnitPrice.
