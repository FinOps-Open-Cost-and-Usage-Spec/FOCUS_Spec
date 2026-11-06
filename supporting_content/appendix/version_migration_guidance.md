# Version Migration Guidance

This appendix provides guidance for practitioners and data generators migrating between FOCUS specification versions. Migration guidance is organized in reverse chronological order, with the most recent migration listed first.

## Document Structure

This guide serves two audiences, and each migration below is organized the same way:

| Audience | Relevant Sections |
|----------|-------------------|
| **All readers** | Overview, What's Unchanged, What's New, What Requires Migration |
| **Practitioners** | Practitioner-facing migration topics covering query and pipeline impact, including decision trees, query examples, and verification steps where applicable |
| **Data Generators** | Data generator guidance covering implementation sequencing and attribute or column changes for the transition |

Practitioners should focus on the What Requires Migration summary and the practitioner topics for their version transition. Data generators should review the data generator guidance for the same transition.

## Migrating from FOCUS 1.4 to FOCUS 1.5

### Overview

FOCUS 1.5 introduces changes across the categories defined by the [Change Impact Classification](/guidelines/contributors/spec-change-guidelines.md):

| Classification | Summary |
|----------------|---------|
| **Compatible** | A new SKU Price dataset (preview), new columns for requester attribution and split cost allocation, new `SkuPriceDetails` properties for AI model billing, three new supported features (two preview), and column presence requirements expressed through operating model conditions. No changes required to existing queries. |
| **Migration Compatible** | Revised definitions of the list and contracted price and cost columns, consumption currency in place of virtual currency, SKU identifiers scoped to `ServiceProviderName`, a largest-whole-unit rule for `ContractCommitmentDurationType`, and a new "Bare Metal" `ServiceSubcategory` value split from "Virtual Machines". Queries or implementations that depend on these require review. |
| **Incompatible** | None |

FOCUS 1.5 removes and renames no columns, attributes, or datasets. Most of its migration impact is on values, not on schema: the same columns are present, but some of them hold different values for affected service providers. A query that runs without error against FOCUS 1.5 data can still return different results than it did against FOCUS 1.4 data. Practitioners should review the What Requires Migration summary and the Practitioner Guidance below; data generators should review the Data Generator Guidance.

### What's Unchanged

All columns, attributes, and datasets from FOCUS 1.4 carry forward into FOCUS 1.5 under the same names. No column was deprecated or removed, and no column changed data type or feature level. Existing queries that do not depend on the revised values noted below continue to work without modification. The only removed appendix entry is the informative Virtual Currency Pricing Model, which the Consumption Currency Pricing Model entry replaces.

### What's New in FOCUS 1.5

The following additive changes do not require migration but may affect data pipelines expecting a fixed schema:

* **New Dataset (preview):** [`SkuPrice`](/specification/datasets/sku_price/dataset.md) describes the full set of unit prices a service provider offers, independent of whether a price was used. It is a preview in FOCUS 1.5:
  * Implementing it is optional, and its requirements are not evaluated for conformance, whether or not a data generator provides it.
  * Two requirements outside the dataset are also excluded from conformance while it is a preview: the [Data Model](/specification/datasets/data_model.md) requirement to include `SkuPrice`, and the [`ChargeCategory`](/specification/datasets/cost_and_usage/columns/chargecategory.md) requirement to match `SkuPrice.ChargeCategory`.
  * Its columns, requirements, and relationships may change in the next version without a deprecation notice. So may the Includes Purchases and Includes Quantity Tier Pricing operating model conditions and the SKU Price Eligibility object schema, which are part of the preview.
  * See the [Preview](/specification/overview.md#preview) section of the specification overview and the Preview note on the dataset page for the full scope.
* **New Supported Features:**
  * [AI Model Billing](/specification/supported_features/ai_model_billing.md)
  * [Catalog Discovery and Price Estimation](/specification/supported_features/catalog_discovery_and_price_estimation.md) (preview, depends on `SkuPrice`)
  * [Rate Optimization and Contract Evaluation](/specification/supported_features/rate_optimization_and_contract_evaluation.md) (preview, depends on `SkuPrice`)
* **New Cost and Usage Columns:**
  * [`AllocatedServiceName`](/specification/datasets/cost_and_usage/columns/allocatedservicename.md), for split cost allocation
  * [`PrincipalId`](/specification/datasets/cost_and_usage/columns/principalid.md), [`CredentialId`](/specification/datasets/cost_and_usage/columns/credentialid.md), and [`RequesterDetails`](/specification/datasets/cost_and_usage/columns/requesterdetails.md), for requester attribution. The Cost and Usage dataset now notes that it can carry personal data, such as identity attributes in `RequesterDetails` and customer-defined values in `Tags`. Practitioners who store or share FOCUS data should review their data handling for these columns.
* **New `SkuPriceDetails` Properties:** [`SkuPriceDetails`](/specification/datasets/cost_and_usage/columns/skupricedetails.md) adds model identity properties (`ModelDeveloper`, `ModelFamily`, `ModelId`, `ModelVersion`) and token metering properties (`TokenDirection`, `TokenCacheAction`). [`ConsumedQuantity`](/specification/datasets/cost_and_usage/columns/consumedquantity.md) adds a requirement that tokens reported on a separate cache "Read" or "Write" row are not counted twice.
* **Operating Model Conditions:** 26 named [operating model conditions](/specification/operating_model_conditions/operating_model_conditions_overview.md) (two of them part of the SKU Price preview) now express when a column or dataset is required (e.g., Includes Regions, Includes Unit Pricing). Dataset presence requirements moved to the new [Data Model](/specification/datasets/data_model.md) level. See [Revised Presence Requirements](#revised-presence-requirements) below.
* **New Allowed and Recommended Values:** [`UnitFormat`](/specification/attributes/unit_format.md) adds the count-based units `Characters`, `Images`, `Jobs`, `Messages`, `Pages`, and `Sessions`, and the time-based unit `Weeks`.
* **New Appendix Entries:**
  * [Requester Attribution](/specification/appendix/requester_attribution.md)
  * [Split Cost Allocation Field Mapping](/specification/appendix/split_cost_allocation_field_mapping.md)
  * [Consumption Currency Pricing Model](/specification/appendix/saas_examples/consumption_currency_pricing_model.md), which replaces the Virtual Currency Pricing Model entry
  * Worked examples for AI model billing, AI model identity, AI prompt caching, requester details, and split cost allocation
  * Worked examples for SKU Price and SKU Price eligibility (preview, part of the `SkuPrice` dataset preview)

See the [CHANGELOG](/CHANGELOG.md) for complete details.

### What Requires Migration

The following changes require review. Each is detailed in the Practitioner Guidance or Data Generator Guidance below.

| Change | Audience | Action |
|--------|----------|--------|
| List and contracted price and cost columns redefined around negotiated pricing terms and commitment programs | Practitioners, Data Generators | Revalidate savings queries that compare List, Contracted, and Effective Cost. Recompute list and contracted values under the revised definitions. |
| Consumption currency replaces virtual currency in `CurrencyFormat` and `PricingCurrency` | Practitioners, Data Generators | Stop inferring currency type from the value format. Classify each `PricingCurrency` value and document how to tell the types apart. |
| SKU identifiers scoped to `ServiceProviderName`, with new `SkuPriceId` requirements | Practitioners, Data Generators | Include `ServiceProviderName` in joins and groupings on SKU identifiers. Check `SkuPriceId` assignment against the new requirements. |
| `ContractCommitmentDurationType` uses the largest whole time-based unit | Practitioners, Data Generators | Update queries that match on duration strings. Normalize emitted values (e.g., "1 Year", not "12 Months"; "3 Months", not "1 Quarter"). |
| "Bare Metal" `ServiceSubcategory` split from "Virtual Machines" | Practitioners, Data Generators | Update filters on "Virtual Machines" that should include bare-metal charges. Reclassify bare-metal services. |
| Column presence expressed through operating model conditions | Data Generators | Re-evaluate which columns are required, since some columns are now required in more operating models. |
| Entity anchors renamed from `#datasets.` to `#datamodel.` | Practitioners, Data Generators | Update deep links into the specification. |
| Requirements model rule key renamed from `ApplicabilityCriteria` to `Conditions` | Data Generators, tool builders | Update tools that read the requirements model JSON. |

The presence row is classified as Compatible, since it does not change existing queries, but it changes what data generators provide. The last two rows are structural changes to the specification and its requirements model; the changelog lists them under Changed specification structure and New requirements model features, outside its Change Impact Classification sections. They break tools and links that depend on the old names.

### Practitioner Guidance

#### List and Contracted Price Redefinition

FOCUS 1.5 revises [`ListCost`](/specification/datasets/cost_and_usage/columns/listcost.md), [`ListUnitPrice`](/specification/datasets/cost_and_usage/columns/listunitprice.md), [`ContractedCost`](/specification/datasets/cost_and_usage/columns/contractedcost.md), [`ContractedUnitPrice`](/specification/datasets/cost_and_usage/columns/contractedunitprice.md), [`PricingCurrencyListUnitPrice`](/specification/datasets/cost_and_usage/columns/pricingcurrencylistunitprice.md), and [`PricingCurrencyContractedUnitPrice`](/specification/datasets/cost_and_usage/columns/pricingcurrencycontractedunitprice.md). The revision separates negotiated pricing terms from discount-bearing commitment programs:

| Column | FOCUS 1.4 | FOCUS 1.5 |
|--------|-----------|-----------|
| `ListUnitPrice` | The suggested service-provider-published unit price, exclusive of any discounts | The service-provider-suggested unit price, before any negotiated pricing terms or discount-bearing commitment programs. It is not necessarily public and can come from a customer-specific price list. It does not reflect a negotiated tier configuration or a negotiated currency exchange rate. |
| `ContractedUnitPrice` | The agreed-upon unit price, inclusive of negotiated discounts and excluding negotiated commitment discounts or any other discounts | The negotiated unit price, reflecting negotiated pricing terms (e.g., a negotiated unit price, tier configuration, or currency exchange rate) that are independent of any discount-bearing commitment program. Equals `ListUnitPrice` when no negotiated pricing terms apply. |
| `PricingCurrencyContractedUnitPrice` | The agreed-upon unit price in Pricing Currency, inclusive of negotiated discounts | Reflects negotiated non-FX pricing terms only, before any currency exchange rate conversion. Equals `PricingCurrencyListUnitPrice` when no negotiated non-FX pricing terms apply. |

`ListCost` and `ContractedCost` follow the same split for "Usage" and "Purchase" charges that are not corrections.

Two consequences matter for savings analysis:

* The revised definition states explicitly that a negotiated discount received in exchange for a spend commitment is reflected in Contracted Unit Price. The effect of applying a commitment discount to covered charges is not; it remains in `EffectiveCost`.
* The gap between List Cost and Contracted Cost measures the effect of negotiated pricing terms. The gap between Contracted Cost and Effective Cost measures the effect of commitment programs. For providers whose FOCUS 1.4 data placed a negotiated term in a different column, savings will move from one gap to the other, and List Cost itself can change where FOCUS 1.4 list values reflected a negotiated tier configuration or exchange rate.

Practitioners with savings, negotiation, or unit price tracking reports should run them for the same period against FOCUS 1.4 and FOCUS 1.5 data from each provider, and review differences before trending across the version boundary. The [Cost Comparison](/specification/supported_features/cost_comparison.md) supported feature adds a query for commitment discount savings over a charge period range that uses the FOCUS 1.5 definitions.

#### Consumption Currency

FOCUS 1.4 allowed `PricingCurrency` to hold a national or virtual currency (e.g., tokens, credits). FOCUS 1.5 replaces virtual currency with consumption currency, a proprietary currency a service provider issues to measure consumption within its ecosystem (e.g., platform credits, normalized billing units):

* [`PricingCurrency`](/specification/datasets/cost_and_usage/columns/pricingcurrency.md) in Cost and Usage and [`PricingCurrency`](/specification/datasets/contract_commitment/columns/pricingcurrency.md) in Contract Commitment represent a national currency or a consumption currency, and their documentation specifies how to tell the two apart.
* [`CurrencyFormat`](/specification/attributes/currency_format.md) prohibits ISO 4217 codes for values that are not a national currency.
* The glossary now defines a token used by an AI model as a unit of measure for the content it processes, distinct from a token issued as a virtual currency.

Whether a value is a national currency follows from the column's documentation, not from the format of the value, and a single column can carry both types (e.g., a national currency on purchase rows and a consumption currency on usage rows). Queries that treat every three-letter `PricingCurrency` value as an ISO 4217 code, or that sum Pricing Currency columns without grouping by `PricingCurrency`, should be revised. Use the data generator's documentation to identify consumption currency values. See [Consumption Currency Pricing Model](/specification/appendix/saas_examples/consumption_currency_pricing_model.md) for a worked example.

#### SKU Identifier Scope

[`SkuId`](/specification/datasets/cost_and_usage/columns/skuid.md), [`SkuMeter`](/specification/datasets/cost_and_usage/columns/skumeter.md), [`SkuPriceId`](/specification/datasets/cost_and_usage/columns/skupriceid.md), and [`SkuPriceDetails`](/specification/datasets/cost_and_usage/columns/skupricedetails.md) consistency requirements now hold for a given `ServiceProviderName`. Two service providers can use the same identifier value for different SKUs. Queries that join or group on SKU identifiers across providers should include `ServiceProviderName`:

```sql
SELECT
  ServiceProviderName,
  SkuPriceId,
  PricingUnit,
  BillingCurrency,
  SUM(PricingQuantity) AS TotalPricingQuantity,
  SUM(EffectiveCost) AS TotalEffectiveCost
FROM CostAndUsage
WHERE SkuPriceId IS NOT NULL
GROUP BY ServiceProviderName, SkuPriceId, PricingUnit, BillingCurrency
```

Each SKU Price ID now has one and only one Pricing Unit for a given `ServiceProviderName`, so `PricingUnit` in this grouping does not split a SKU Price ID. A SKU Price ID can have prices in more than one Billing Currency, so the query groups by `BillingCurrency` to avoid adding costs across currencies. The `SkuPriceId` column introduction also describes two cases that produce distinct SKU Price IDs: each tier of a tiered price, and a negotiated tier configuration. Practitioners tracking a price over time by SKU Price ID can see new SKU Price IDs when a negotiated tier configuration takes effect.

#### Duration and Subcategory Values

* When [`ContractCommitmentDurationType`](/specification/datasets/contract_commitment/columns/contractcommitmentdurationtype.md) expresses a time-based unit, it uses the largest `UnitFormat` time unit that expresses the duration as a whole number (e.g., "1 Year" rather than "12 Months", "1 Week" rather than "7 Days"). The column's own allowed values table, which included "Quarter", is replaced by the `UnitFormat` time units from Minute through Year, which do not include it, so a quarterly term is expressed as "3 Months". Queries that match on duration strings should match the normalized form, or both forms while FOCUS 1.4 data is still in use.
* [`ServiceSubcategory`](/specification/datasets/cost_and_usage/columns/servicesubcategory.md) adds "Bare Metal" under "Compute" and narrows "Virtual Machines" to hypervisor-based instances. Queries on "Virtual Machines" no longer return bare-metal charges. To keep a view of all compute instances, filter on both values. [`ServiceCategory`](/specification/datasets/cost_and_usage/columns/servicecategory.md) allowed value descriptions are now technology-agnostic; the values are unchanged.

#### Deep Links and Example Queries

The specification's "Datasets" section is now the [Data Model](/specification/datasets/data_model.md), and entity anchors changed from `#datasets.` to `#datamodel.` (e.g., `#datamodel.costandusage.billedcost`). Internal documentation, dashboards, or tools that deep-link into the published specification need their links updated. Supported feature SQL examples now read from named datasets (e.g., `FROM CostAndUsage`) instead of `focus_data_table`; practitioners copying them should map the dataset names to their own tables.

### Data Generator Guidance

#### Revised Presence Requirements

Column presence requirements are now written against named operating model conditions, and each column's Content Constraints table names the conditions that apply. Most conditions restate the FOCUS 1.4 trigger in a named form. Some change which operating models require a column:

| Column | Required in FOCUS 1.4 when the service provider | Required in FOCUS 1.5 when the operating model |
|--------|-------------------------------------------------|------------------------------------------------|
| `ListUnitPrice` | Publishes unit prices exclusive of discounts | Includes unit pricing |
| `ContractedUnitPrice` | Supports negotiated pricing concepts | Includes unit pricing |
| `SkuId`, `SkuMeter`, `SkuPriceDetails`, `SkuPriceId` | Supports unit pricing concepts and publishes price lists | Includes unit pricing |
| `PricingCurrencyEffectiveCost` | Supports prices in virtual currency and publishes unit prices exclusive of discounts (MUST); supports pricing and billing in different currencies and publishes unit prices exclusive of discounts (SHOULD) | Includes consumption currency (MUST); includes pricing and billing currency differences (SHOULD) |
| `PricingCurrencyListUnitPrice`, `PricingCurrencyContractedUnitPrice` | Supports prices in virtual currency and publishes unit prices exclusive of discounts (MUST); supports pricing and billing in different currencies and publishes unit prices exclusive of discounts (SHOULD) | Includes consumption currency and includes unit pricing (MUST); includes pricing and billing currency differences and includes unit pricing (SHOULD) |

A data generator with unit pricing and no negotiated pricing could omit `ContractedUnitPrice` under FOCUS 1.4. Under FOCUS 1.5 it includes the column, which equals `ListUnitPrice` when no negotiated pricing terms apply. Dataset presence requirements (e.g., include `InvoiceDetail` when the operating model includes payable invoices) moved from each dataset to the [Data Model](/specification/datasets/data_model.md). Data generators should map their operating model to each condition in the [Operating Model Conditions](/specification/operating_model_conditions/operating_model_conditions_overview.md) list and confirm the columns and datasets they provide.

#### Value Changes to Existing Columns

* **List and contracted prices.** Recompute list and contracted values under the revised definitions. `ListUnitPrice` and `ContractedUnitPrice` add Implementation Guidance. For a negotiated tier configuration, `ListUnitPrice` is the service-provider-suggested unit price for the same quantity under the suggested tier configuration. `PricingCurrencyContractedUnitPrice` reflects negotiated non-FX pricing terms only. `ListCost` and `ContractedCost` equal `BilledCost` for "Credit" charges and are calculated from related charges for "Tax" charges, whether or not a unit price is present.
* **Currency.** Classify each `PricingCurrency` value as a national or consumption currency, and stop using ISO 4217 codes for values that are not a national currency. Document how practitioners can tell the types apart, in a form accessible to them. Other virtual currencies, such as cryptocurrency, are not valid `PricingCurrency` values. The same applies to `PricingCurrency` in Contract Commitment, and [`CustomColumnHandling`](/specification/attributes/custom_column_handling.md) currency requirements now apply to any currency custom column.
* **SKU Price ID.** The FOCUS 1.4 rules that a `SkuPriceId` has one parent `SkuId` and stays consistent over time and across billing accounts or contracts now apply for a given `ServiceProviderName`. The `SkuPriceId` column adds these requirements, each for a given `ServiceProviderName`:
  * one and only one `PricingUnit`
  * no association with both "Usage" and "Purchase" charges
  * one and only one `ListUnitPrice` per `BillingCurrency` and `ChargePeriodStart`
  * one and only one `ContractedUnitPrice` per contract, `BillingAccountId`, `BillingCurrency`, and `ChargePeriodStart`
* **SKU Price Details.** `SkuPriceDetails` property values use the allowed values where a property defines them.
* **Duration type.** Express time-based `ContractCommitmentDurationType` values in the largest whole `UnitFormat` time unit; the "[Numeric Value] [Unit]" format is recommended. "Quarter" is no longer among the units, so quarterly terms become "3 Months". `UnitFormat` also recommends the largest whole time unit for any time-based unit.
* **Service subcategory.** Classify services provisioned as physical servers without a provider-managed hypervisor as "Bare Metal".
* **JSON columns.** [`JsonObjectFormat`](/specification/attributes/json_object_format.md) now allows a top-level array. Objects in an array also must not be empty, and should not exceed three levels of nesting.
* **Tags.** [`Tags`](/specification/datasets/cost_and_usage/columns/tags.md) restores, and [`AllocatedTags`](/specification/datasets/cost_and_usage/columns/allocatedtags.md) adds, the requirement that user-defined tag keys match the keys assigned at the tag source, with or without a tag scheme-specific prefix.

#### Requirements Model Key Rename

The FOCUS 1.5 release of the requirements model renames the model rule key `ApplicabilityCriteria` to `Conditions`, and `conditions.json` replaces `applicability_criteria.json`. `Conditions` holds the IDs of operating model conditions. Earlier model releases keep the old key. Tools that read the model JSON, such as validators, need to read the new key for FOCUS 1.5. See [Writing Requirements Model Guidelines](/guidelines/contributors/writing-requirements-model-guidelines.md).

#### Recommended Implementation Sequence

For a release with multiple changes, data generators can reduce consumer disruption by sequencing the transition:

* Adopt additive changes first. New columns and `SkuPriceDetails` properties do not affect existing consumers and can be introduced independently. Implementing the SKU Price preview is optional; data generators that implement it help answer its open questions and should expect it to change.
* Re-evaluate presence. Map the operating model to each operating model condition and add any column that is now required, such as `ContractedUnitPrice`.
* Apply identifier and categorical value changes. Scope SKU identifiers to `ServiceProviderName`, normalize `ContractCommitmentDurationType`, reclassify bare-metal services, and classify `PricingCurrency` values. Document each change for consumers.
* Apply the list and contracted price redefinition last, and document for consumers which negotiated terms moved between List, Contracted, and Effective Cost, since this change alters savings results.

During staggered adoption, practitioners may receive FOCUS 1.4 and FOCUS 1.5 data from different providers during the same period. Because the affected columns keep their names, consumers cannot tell the versions apart from the schema. They should read the [FOCUS Version](/specification/metadata/schema/focus_version.md) metadata of each dataset and apply the definitions for that version.

### Affected Supported Features

The following supported features reference columns, attributes, or behaviors changed in FOCUS 1.5. Several reflect additive changes and require no query updates; the list and contracted price redefinition, the SKU identifier scope, and the "Bare Metal" split require review (see What Requires Migration above):

* [Cost Comparison](/specification/supported_features/cost_comparison.md), for the list and contracted price redefinition
* [Verify, Compare, and Track Unit Prices](/specification/supported_features/verify_compare_track_unit_prices.md), for the list and contracted price redefinition and the SKU identifier scope, since a SKU Price ID identifies a price only within a given `ServiceProviderName`
* [Service Categorization](/specification/supported_features/service_categorization.md), for the "Bare Metal" `ServiceSubcategory` value
* [Resource Usage](/specification/supported_features/resource_usage.md), which adds cache hit rate and input-to-output token ratio queries
* [Data Generator-Calculated Split Cost Allocation](/specification/supported_features/data_generator_calculated_split_cost_allocation.md), for the new `AllocatedServiceName` column
* [Effective Cost](/specification/supported_features/effective_cost.md) and [Invoice Reconciliation](/specification/supported_features/invoice_reconciliation.md), which add example queries

### Additional Resources

* [FOCUS 1.5 CHANGELOG](/CHANGELOG.md), the complete list of 1.5 changes by classification
* [Operating Model Conditions](/specification/operating_model_conditions/operating_model_conditions_overview.md), the conditions that now determine column and dataset presence
* The [Preview](/specification/overview.md#preview) section of the specification overview and the [Preview Process](/guidelines/contributors/spec-change-guidelines.md#preview-process), for what preview status means for the SKU Price dataset
* [Consumption Currency Pricing Model](/specification/appendix/saas_examples/consumption_currency_pricing_model.md), a worked example of consumption currency pricing

---

## Migrating from FOCUS 1.3 to FOCUS 1.4

### Overview

FOCUS 1.4 introduces changes across the categories defined by the [Change Impact Classification](/guidelines/contributors/spec-change-guidelines.md):

| Classification | Summary |
|----------------|---------|
| **Compatible** | Two new datasets, new columns, six new attributes, two new supported features, and revised requirements for existing cost columns. No changes required to existing queries. |
| **Migration Compatible** | Removal of the deprecated `ProviderName` and `PublisherName` columns, a revised `ContractApplied` format, and removal of three attributes whose requirements moved to successor attributes, datasets, and columns. Queries or implementations referencing these require updates. |
| **Incompatible** | None |

FOCUS 1.4 is a larger release than FOCUS 1.3, but most changes are additive and compatible, with no incompatible changes. The items requiring migration are concentrated in a few areas, including the removal of columns deprecated during the 1.3 cycle. Practitioners should review the What Requires Migration summary and the Practitioner Guidance below; data generators should review the Data Generator Guidance.

### What's Unchanged

All columns, attributes, and behaviors from FOCUS 1.3 carry forward into FOCUS 1.4 except for the removed columns and attributes noted below. Existing queries that do not reference the removed columns and do not parse the revised JSON object structure continue to work without modification.

### What's New in FOCUS 1.4

The following additive changes do not require migration but may affect data pipelines expecting a fixed schema:

* **New Datasets** (together, they support reconciling usage to issued invoices):
  * [`BillingPeriod`](/specification/datasets/billing_period/dataset.md) provides invoice-issuer-aware billing period boundaries and status.
  * [`InvoiceDetail`](/specification/datasets/invoice_detail/dataset.md) carries the financial record of charges as they appear on issued invoices (payment currency, terms, due date, purchase order number).
* **Expanded Dataset:** the [`ContractCommitment`](/specification/datasets/contract_commitment/dataset.md) dataset grows from 13 to 30 columns, covering identification, lifecycle and periods, commitment structure, and cost and quantity.
* **New Supported Features:**
  * [Invoice Reconciliation](/specification/supported_features/invoice_reconciliation.md)
  * [Commitment Program Eligibility Details](/specification/supported_features/commitment_program_eligibility_details.md)
* **New Cost and Usage Columns:**
  * [`CommitmentProgramEligibilityDetails`](/specification/datasets/cost_and_usage/columns/commitmentprogrameligibilitydetails.md)
  * [`InvoiceDetailId`](/specification/datasets/cost_and_usage/columns/invoicedetailid.md)
* **New Attributes:**
  * [`CorrectionHandling`](/specification/attributes/correction_handling.md)
  * [`CustomColumnHandling`](/specification/attributes/custom_column_handling.md)
  * [`DatasetCompleteness`](/specification/attributes/dataset_completeness.md)
  * [`DatasetConfiguration`](/specification/attributes/dataset_configuration.md)
  * [`DeliveryHandling`](/specification/attributes/delivery_handling.md)
  * [`FocusColumnHandling`](/specification/attributes/focus_column_handling.md)
* **New Appendix Entries:**
  * [Discount Handling](/specification/appendix/discount_handling.md)
  * [Rounding Variance Tolerance](/specification/appendix/rounding_variance_tolerance.md)
  * [Invoice and Billing Period Handling](/specification/appendix/invoice_and_billing_period_handling.md)
  * Worked examples for commitment program eligibility details, contract commitments, correction handling, invoice detail, and JSON objects

See the [CHANGELOG](/CHANGELOG.md) for complete details.

### What Requires Migration

The following changes require action. Each is detailed in the Practitioner Guidance or Data Generator Guidance below.

| Change | Audience | Action |
|--------|----------|--------|
| `ProviderName` and `PublisherName` removed | Practitioners | Migrate any remaining queries to the successor columns identified during the 1.3 cycle. |
| `ContractApplied` format revised to the JSON Object Schema format | Practitioners | Update queries that parse the `ContractApplied` JSON structure. |
| `ColumnHandling`, `DiscountHandling`, and `InvoiceHandling` attributes removed | Data Generators | Apply the requirements that moved to successor attributes, datasets, and columns. |

### Practitioner Guidance

#### Provider and Publisher Column Removal

The `ProviderName` and `PublisherName` columns were deprecated in FOCUS 1.3 and are removed in FOCUS 1.4. Their use cases were redistributed to `ServiceProviderName`, `HostProviderName`, `InvoiceIssuerName`, and the `DataGenerator` metadata property during the 1.3 cycle.

Practitioners who have not yet migrated queries away from these columns should follow the [Provider and Publisher Column Changes](#provider-and-publisher-column-changes) guidance for the 1.2 to 1.3 transition below, which provides the column-by-column decision tree, the acquisition-method scenario matrix, and verification steps. The successor columns and their mapping are unchanged in FOCUS 1.4; only the removal of the deprecated columns is new.

#### ContractApplied Format Change

The [`ContractApplied`](/specification/datasets/cost_and_usage/columns/contractapplied.md) column was revised in FOCUS 1.4 to follow the JSON Object Schema format. The concepts represented by the column are unchanged; the change is to the structure of the JSON value.

Practitioners whose queries parse the `ContractApplied` value should update their parsing logic to the FOCUS 1.4 schema. Queries that test only for the presence of `ContractApplied`, or that do not inspect its internal structure, are unaffected. See the [Examples: JSON Object](/specification/appendix/json_object_examples/json_object_examples_overview.md) appendix for the JSON Object Schema format.

#### Revised Cost Column Requirements

These changes are classified as Compatible and do not require query changes, but they refine how core cost values are defined. Practitioners performing invoice reconciliation or commitment amortization analysis should review the updated definitions:

* [`BilledCost`](/specification/datasets/cost_and_usage/columns/billedcost.md) and [`EffectiveCost`](/specification/datasets/cost_and_usage/columns/effectivecost.md) requirements were revised to clarify the treatment of pricing adjustments, covered and covering charges, and cross-record sum validation. When a covering charge (a purchase that pays for other charges, such as a reserved instance prepayment) and the charges it covers are both present in the same dataset instance, `EffectiveCost` and `BilledCost` sum to the same total within the covering charge's charge period; the totals may differ when only one side of that relationship is present, or when the charges span multiple billing periods or billing accounts.
* [`InvoiceId`](/specification/datasets/cost_and_usage/columns/invoiceid.md) changed from a Recommended to a Conditional feature level. Values are populated for charges associated with an issued or pre-generated provisional invoice.

### Data Generator Guidance

#### Attribute Restructuring

Three attributes were broken down and their requirements moved to other attributes, datasets, and columns in FOCUS 1.4:

| Removed Attribute | Requirements Moved To |
|-------------------|-----------------------|
| `ColumnHandling` | `FocusColumnHandling` and `CustomColumnHandling` attributes |
| `DiscountHandling` | `CostAndUsage` dataset and its specific columns; see the Discount Handling appendix for more details |
| `InvoiceHandling` | `DeliveryHandling` and `DatasetCompleteness` attributes, and the `CostAndUsage`/`InvoiceDetail`/`BillingPeriod` datasets and their specific columns; see the Invoice and Billing Period Handling appendix for more details |

Data generators applying these attributes should map their existing implementation to the successor requirements.

#### Recommended Implementation Sequence

For a release with multiple changes, data generators can reduce consumer disruption by sequencing the transition:

* Adopt additive changes first. New datasets, columns, and attributes do not affect existing consumers and can be introduced independently.
* Apply the attribute restructuring. Map `ColumnHandling`, `DiscountHandling`, and `InvoiceHandling` implementations to their successors.
* Complete the column changes last. Remove `ProviderName` and `PublisherName` once consumers have migrated, and adopt the revised `ContractApplied` format.

During staggered adoption, practitioners may receive FOCUS 1.3 and FOCUS 1.4 data from different providers during the same period. Consumers should determine the FOCUS version of each dataset they process and apply the column expectations for that version, since the removed columns are absent from FOCUS 1.4 data but may remain present in FOCUS 1.3 data during the transition.

### Affected Supported Features

The following supported features reference columns, attributes, or behaviors changed in FOCUS 1.4. Most reflect additive or clarifying changes and require no query updates; only the `ContractApplied` format change and the removed `ProviderName`/`PublisherName` columns require action (see What Requires Migration above):

* [Participating Entity Identification](/specification/supported_features/participating_entity_identification.md), for the successor columns to the removed `ProviderName` and `PublisherName`
* [Contract Commitments](/specification/supported_features/contract_commitments.md), for the revised `ContractApplied` format
* [Billed Cost and Invoice Alignment](/specification/supported_features/billed_cost_and_invoice_alignment.md) and [Effective Cost](/specification/supported_features/effective_cost.md), for the revised cost column requirements
* [Cost Comparison](/specification/supported_features/cost_comparison.md), for the expanded cash-based versus accrual-based comparison guidance

### Additional Resources

* [FOCUS 1.4 CHANGELOG](/CHANGELOG.md), the complete list of 1.4 changes by classification
* The [Migrating from FOCUS 1.2 to FOCUS 1.3](#migrating-from-focus-12-to-focus-13) section below, for the Provider and Publisher migration decision tree that remains relevant in FOCUS 1.4

---

## Migrating from FOCUS 1.2 to FOCUS 1.3

### Overview

FOCUS 1.3 introduces changes across three categories defined by the [Change Impact Classification](/guidelines/contributors/spec-change-guidelines.md):

| Classification | Summary |
|----------------|---------|
| **Compatible** | New columns, new dataset, and new metadata. No changes required to existing queries. |
| **Migration Compatible** | Deprecated `ProviderName` and `PublisherName` columns replaced by `ServiceProviderName` and `HostProviderName`. Queries referencing deprecated columns require updates. |
| **Incompatible** | None |

Most practitioners can adopt FOCUS 1.3 without changes. Only queries referencing `ProviderName` or `PublisherName` require migration.

### What's Unchanged

All columns, attributes, and behaviors from FOCUS 1.2 remain compatible in FOCUS 1.3 except for the deprecated columns noted below. Existing queries that do not reference `ProviderName` or `PublisherName` will continue to work without modification.

### What's New in FOCUS 1.3

The following additive changes do not require migration but may affect data pipelines expecting a fixed schema:

| Change Type | Summary |
|-------------|---------|
| **New Dataset** | [`ContractCommitment`](/specification/datasets/contract_commitment/dataset.md) — 13 columns tracking contract and commitment details separately from usage rows |
| **Split Cost Allocation** | 5 new columns (`AllocatedMethodId`, `AllocatedMethodDetails`, `AllocatedResourceId`, `AllocatedResourceName`, `AllocatedTags`) enabling data generator-calculated cost allocation |
| **Contract Tracking** | [`ContractApplied`](/specification/datasets/cost_and_usage/columns/contractapplied.md) column links usage rows to contract commitments via JSON object references |
| **Entity Identification** | [`ServiceProviderName`](/specification/datasets/cost_and_usage/columns/serviceprovidername.md) and [`HostProviderName`](/specification/datasets/cost_and_usage/columns/hostprovidername.md) provide explicit entity role identification |
| **New Metadata** | [Dataset Instance](/specification/metadata/dataset_instance/dataset_instance_overview.md) and [Recency](/specification/metadata/recency/recency_overview.md) metadata for tracking data identity and freshness |
| **New Attributes** | `InvoiceHandling`, `JsonObjectFormat`, and `DataGeneratorCalculatedSplitCostAllocationHandling` |

See the [CHANGELOG](/CHANGELOG.md) for complete details.

### What Requires Migration

Only the `ProviderName` and `PublisherName` columns are deprecated in FOCUS 1.3. These columns have been removed in FOCUS 1.4.

---

## Provider and Publisher Column Changes

### Before You Begin (Practitioners)

Practitioners should complete this assessment before migrating queries:

* [ ] Identify all queries, reports, and dashboards that reference `ProviderName` or `PublisherName`
* [ ] For each usage, determine what business question the column was answering
* [ ] Review [Participating Entity Identification Examples](/specification/appendix/participating_entity_identification.md) for scenarios matching your acquisition methods
* [ ] Plan migration timeline (deprecated columns will be removed in FOCUS 1.4+)

### Why This Change Was Made

The original `ProviderName` and `PublisherName` columns suffered from definitional ambiguity:

| Problem | Impact |
|---------|--------|
| `ProviderName` lacked specificity about which provider role was being described | Data generators inconsistently populated values, making cross-provider analysis unreliable |
| `PublisherName` overlapped conceptually with Provider and Invoice Issuer | The column was often null, duplicated `ProviderName`, or populated inconsistently |
| Neither column distinguished between the entity selling a service and the entity hosting the infrastructure | Practitioners couldn't determine who to contact for support vs. billing inquiries |

FOCUS 1.3 resolves this by introducing two purpose-specific columns that align with the distinct entity roles documented in [Participating Entity Identification](/specification/appendix/participating_entity_identification.md).

### Migration Decision Tree (Practitioners)

The correct mapping from deprecated columns depends on what business question your queries were answering, not a simple column rename.

#### Migrating ProviderName

| If you used ProviderName to identify... | Use this column in 1.3 | Notes |
|-----------------------------------------|------------------------|-------|
| Who sells the service you're consuming | `ServiceProviderName` | Most common case for direct CSP purchases |
| The cloud platform hosting marketplace purchases | `HostProviderName` | Marketplace scenarios where ProviderName held the CSP |
| The entity for billing inquiries | `InvoiceIssuerName` | Already existed in 1.2 |

#### Migrating PublisherName

| If you used PublisherName to identify... | Use this column in 1.3 | Notes |
|------------------------------------------|------------------------|-------|
| Who sells the service (e.g., SaaS vendor in marketplace) | `ServiceProviderName` | Primary intended use |
| Who hosts the underlying infrastructure | `HostProviderName` | Rare; usually null or duplicated ProviderName |
| Who issues the invoice | `InvoiceIssuerName` | Already existed in 1.2 |
| Who generates the billing data | `DataGenerator` (metadata) | Metadata property, not a column |

#### Key Insight: Acquisition Method Matters

The mapping varies by how resources or services were acquired. Review these common scenarios:

| Scenario | Old ProviderName | Old PublisherName | New ServiceProviderName | New HostProviderName |
|----------|------------------|-------------------|-------------------------|----------------------|
| Direct CSP purchase | CSP | CSP (or null) | CSP | CSP |
| Marketplace: SaaS on CSP infrastructure | CSP | SaaS Vendor | SaaS Vendor | CSP |
| Marketplace: SaaS on vendor infrastructure | CSP | SaaS Vendor | SaaS Vendor | SaaS Vendor |
| MSP-managed services | MSP | MSP | MSP | CSP (if visible) or MSP |
| Direct SaaS purchase | SaaS Vendor | SaaS Vendor | SaaS Vendor | CSP (if visible) or SaaS Vendor |

For the complete scenario matrix, see [Participating Entity Identification Examples](/specification/appendix/participating_entity_identification.md).

### New Column: HostProviderName

| Attribute | Value |
|-----------|-------|
| Column ID | `HostProviderName` |
| Display Name | Host Provider Name |
| Feature Level | Mandatory |
| Allows Nulls | True |
| Introduced | 1.3 |

**Purpose:** Identifies the entity providing the underlying infrastructure on which the Service Provider's resources or services are deployed.

**Nullability rules:**
* MAY be null when the service does not involve deployment on infrastructure (e.g., professional services, software licenses)
* MAY be null when the hosting provider cannot be uniquely determined (e.g., Tax or Adjustment charges)
* MUST match `ServiceProviderName` when the service provider hosts their own services and does not expose the underlying host

### Query Migration Examples (Practitioners)

#### Basic Provider Query

**FOCUS 1.2:**
```sql
SELECT ProviderName, SUM(BilledCost) AS TotalCost
FROM focus_data
GROUP BY ProviderName
```

**FOCUS 1.3:**
```sql
SELECT ServiceProviderName, SUM(BilledCost) AS TotalCost
FROM focus_data
GROUP BY ServiceProviderName
```

#### Multi-Entity Analysis

**FOCUS 1.2:**
```sql
SELECT 
    ProviderName, 
    PublisherName, 
    InvoiceIssuerName, 
    SUM(BilledCost) AS TotalCost
FROM focus_data
GROUP BY ProviderName, PublisherName, InvoiceIssuerName
```

**FOCUS 1.3:**
```sql
SELECT 
    ServiceProviderName, 
    HostProviderName, 
    InvoiceIssuerName, 
    SUM(BilledCost) AS TotalCost
FROM focus_data
GROUP BY ServiceProviderName, HostProviderName, InvoiceIssuerName
```

#### Marketplace Cost Analysis

**FOCUS 1.2** (common pattern to find marketplace purchases):
```sql
SELECT 
    ProviderName,
    PublisherName, 
    SUM(BilledCost) AS TotalCost
FROM focus_data
WHERE ProviderName != PublisherName
GROUP BY ProviderName, PublisherName
```

**FOCUS 1.3** (different semantics):
```sql
SELECT 
    ServiceProviderName,
    HostProviderName, 
    SUM(BilledCost) AS TotalCost
FROM focus_data
WHERE ServiceProviderName != HostProviderName
GROUP BY ServiceProviderName, HostProviderName
```

### Verification (Practitioners)

After migrating queries, practitioners should verify results:

1. **Direct CSP purchases:** Query results should match pre-migration outputs when grouping by `ServiceProviderName` instead of `ProviderName`
2. **Marketplace scenarios:** Results may show different groupings than before—this is intentional and reflects the corrected entity identification
3. **Null handling:** `HostProviderName` may be null for charges that don't involve infrastructure (licenses, professional services, adjustments)

---

## Guidance for Data Generators

### Dual-Column Support During Transition

Data generators SHOULD include both deprecated and new columns in FOCUS 1.3 datasets to support practitioners transitioning their queries. This allows practitioners to:
* Continue using existing queries during migration
* Validate new queries against old results
* Transition at their own pace before FOCUS 1.4

### Deprecation Metadata

FOCUS 1.2 introduced metadata properties to signal column deprecation:
* `Deprecated`: Boolean indicating whether a column is deprecated
* `PreviousColumnName`: References the column this one replaces (if applicable)

Data generators SHOULD populate these properties in their metadata schema to help practitioners identify deprecated columns programmatically.

### Deprecation Timeline

| Version | ProviderName Status | PublisherName Status |
|---------|---------------------|----------------------|
| 1.2 | Active | Active |
| 1.3 | Deprecated | Deprecated |
| 1.4+ | Removed | Removed |

---

## Affected Supported Features

The following supported features reference participating entity columns and may require documentation or query updates:

* [Charge Categorization](/specification/supported_features/charge_categorization.md)
* [Commit Usage and Under Usage](/specification/supported_features/commit_usage_and_under_usage.md)
* [Cost Comparison](/specification/supported_features/cost_comparison.md)
* [Effective Cost](/specification/supported_features/effective_cost.md)
* [Marketplace Purchases](/specification/supported_features/marketplace_purchases.md)
* [Participating Entity Identification](/specification/supported_features/participating_entity_identification.md)
* [Service Provider Services](/specification/supported_features/service_provider_services.md)
* [Resource Usage](/specification/supported_features/resource_usage.md)
* [Service Categorization](/specification/supported_features/service_categorization.md)

---

## Additional Resources

* [Participating Entity Identification Examples](/specification/appendix/participating_entity_identification.md) — Scenarios showing how entity values vary by acquisition method
* [ServiceProviderName Column Specification](/specification/datasets/cost_and_usage/columns/serviceprovidername.md)
* [HostProviderName Column Specification](/specification/datasets/cost_and_usage/columns/hostprovidername.md)
* [FOCUS 1.3 Changelog](/CHANGELOG.md)
