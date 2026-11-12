# FinOps Open Cost and Usage Specification Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## v1.5

<sup>Announced December 2026</sup>

v1.5 adds 1 dataset (`SkuPrice`, preview), 27 new columns, 3 new supported features (2 preview), 26 operating model conditions (2 preview), 6 new `SkuPriceDetails` properties, and 16 new glossary entries.

### Changes to Supported Features by [Change Impact Classification](/guidelines/contributors/spec-change-guidelines.md)

#### Compatible Changes

* New `SkuPriceDetails` properties and an informative supported feature to support [AI Model Billing](/specification/supported_features/ai_model_billing.md): model identity (`ModelDeveloper`, `ModelFamily`, `ModelId`, `ModelVersion`) and token metering (`TokenDirection`, `TokenCacheAction`). `ConsumedQuantity` adds a requirement that prevents cached tokens from being counted twice. Affecting:
  * [Resource Usage](/specification/supported_features/resource_usage.md), which adds cache hit rate and input-to-output token ratio queries.
* New dataset and columns to support [Catalog Discovery and Price Estimation](/specification/supported_features/catalog_discovery_and_price_estimation.md) (preview) and [Rate Optimization and Contract Evaluation](/specification/supported_features/rate_optimization_and_contract_evaluation.md) (preview).
* New columns for requester attribution (`PrincipalId`, `CredentialId`, `RequesterDetails`), with a [Requester Attribution](/specification/appendix/requester_attribution.md) appendix entry and a dataset note on personal data in Cost and Usage.
* New [`AllocatedServiceName`](/specification/datasets/cost_and_usage/columns/allocatedservicename.md) column, with a [Split Cost Allocation Field Mapping](/specification/appendix/split_cost_allocation_field_mapping.md) appendix entry and new example queries. `AllocatedMethodDetails`, `AllocatedMethodId`, `AllocatedResourceId`, `AllocatedResourceName`, and `AllocatedTags` presence now depends on whether the operating model includes split cost allocation; previously it depended on whether the data generator supported data generator-calculated split cost allocation. Affecting:
  * [Data Generator-Calculated Split Cost Allocation](/specification/supported_features/data_generator_calculated_split_cost_allocation.md)
* Column and dataset presence requirements are now expressed through named [operating model conditions](/specification/operating_model_conditions/operating_model_conditions_overview.md) (e.g., `CostAndUsage MUST include RegionId when the operating model includes regions`). Dataset presence requirements moved to a new Data Model level. Each column's Content Constraints table names its operating model conditions.
* Presence of [`ListUnitPrice`](/specification/datasets/cost_and_usage/columns/listunitprice.md), `SkuId`, `SkuMeter`, `SkuPriceDetails`, and `SkuPriceId` now depends on whether the operating model includes unit pricing. Previously it depended on whether the service provider published undiscounted prices or supported unit pricing and published price lists. `PricingCurrencyEffectiveCost` presence no longer depends on publishing undiscounted prices.
* Removed the duplicative cost-formula requirement from [`PricingQuantity`](/specification/datasets/cost_and_usage/columns/pricingquantity.md). The same formula remains on `ListCost` and `ContractedCost`.
* [`Tags`](/specification/datasets/cost_and_usage/columns/tags.md) and [`AllocatedTags`](/specification/datasets/cost_and_usage/columns/allocatedtags.md): added the requirement that user-defined tag keys match the keys assigned at the tag source, with or without a tag scheme-specific prefix. For `Tags`, this restores the key preservation that v1.0 and v1.1 required and v1.2 removed.
* [`ChargeCategory`](/specification/datasets/cost_and_usage/columns/chargecategory.md): added a cross-dataset requirement to match `SkuPrice.ChargeCategory` for the same `SkuPriceId` and `ServiceProviderName` when `ChargeCategory` is "Usage" or "Purchase". Excluded from conformance while SKU Price is a preview.
* [`ServiceCategory`](/specification/datasets/cost_and_usage/columns/servicecategory.md) allowed value descriptions are now technology-agnostic. Values are unchanged.
* New example queries in [Cost Comparison](/specification/supported_features/cost_comparison.md) (commitment discount savings, billing period vs. charge period), [Effective Cost](/specification/supported_features/effective_cost.md) (consumed vs. pricing quantity), and [Invoice Reconciliation](/specification/supported_features/invoice_reconciliation.md) (reconciliation by Invoice Detail ID).

#### Migration Compatible Changes

* Revised [`ListCost`](/specification/datasets/cost_and_usage/columns/listcost.md), [`ListUnitPrice`](/specification/datasets/cost_and_usage/columns/listunitprice.md), [`ContractedCost`](/specification/datasets/cost_and_usage/columns/contractedcost.md), [`ContractedUnitPrice`](/specification/datasets/cost_and_usage/columns/contractedunitprice.md), [`PricingCurrencyListUnitPrice`](/specification/datasets/cost_and_usage/columns/pricingcurrencylistunitprice.md), and [`PricingCurrencyContractedUnitPrice`](/specification/datasets/cost_and_usage/columns/pricingcurrencycontractedunitprice.md) to separate *negotiated pricing terms* from discount-bearing *commitment programs*. A negotiated discount received in exchange for a spend commitment is now reflected in Contracted Unit Price; the effect of applying a commitment discount is not. List values do not reflect negotiated tier configurations or negotiated FX pricing terms. Savings queries that compare List, Contracted, and Effective Cost may return different results for affected providers. Affecting:
  * [Cost Comparison](/specification/supported_features/cost_comparison.md)
  * [Verify, Compare, and Track Unit Prices](/specification/supported_features/verify_compare_track_unit_prices.md)
* Replaced the virtual currency allowance with *consumption currency* (e.g., platform credits, normalized billing units). [`CurrencyFormat`](/specification/attributes/currency_format.md) prohibits ISO 4217 codes for values that are not a national currency, and [`PricingCurrency`](/specification/datasets/cost_and_usage/columns/pricingcurrency.md) (Cost and Usage and Contract Commitment) MUST be a national or consumption currency, with documentation of how to tell them apart. `PricingCurrencyEffectiveCost`, `PricingCurrencyListUnitPrice`, and `PricingCurrencyContractedUnitPrice` presence now depends on consumption currency.
* `SkuId`, `SkuMeter`, `SkuPriceId`, and `SkuPriceDetails` identity requirements are now scoped to a given `ServiceProviderName`. Queries that join or group on SKU identifiers across providers should include `ServiceProviderName`. [`SkuPriceId`](/specification/datasets/cost_and_usage/columns/skupriceid.md) adds requirements for one `PricingUnit`, one `ListUnitPrice` per `BillingCurrency` and `ChargePeriodStart`, one `ContractedUnitPrice` per contract, `BillingAccountId`, `BillingCurrency`, and `ChargePeriodStart`, and no mix of "Usage" and "Purchase" charges. Providers with tiered pricing use a distinct `SkuPriceId` for each tier, so queries that count or group on `SkuPriceId` may return more values.
* [`ContractedUnitPrice`](/specification/datasets/cost_and_usage/columns/contractedunitprice.md) presence now depends on whether the operating model includes unit pricing. Previously it depended on whether the service provider supported negotiated pricing concepts. A dataset whose operating model includes negotiated pricing but not unit pricing (e.g., a flat-fee contract) may omit `ContractedUnitPrice`, so queries that select it may need updating.
* [`ContractCommitmentDurationType`](/specification/datasets/contract_commitment/columns/contractcommitmentdurationtype.md) MUST use the largest whole time-based unit (e.g., "1 Year", not "12 Months"). Queries that match on duration strings may need updating.
* [`ServiceSubcategory`](/specification/datasets/cost_and_usage/columns/servicesubcategory.md): split a new "Bare Metal" value out of "Virtual Machines" under "Compute". Queries on "Virtual Machines" no longer return bare-metal charges.

#### Incompatible Changes

* None

### Added

#### New supported features

* [AI Model Billing](/specification/supported_features/ai_model_billing.md)
* [Catalog Discovery and Price Estimation](/specification/supported_features/catalog_discovery_and_price_estimation.md) (preview)
* [Rate Optimization and Contract Evaluation](/specification/supported_features/rate_optimization_and_contract_evaluation.md) (preview)

#### New datasets

* [`SkuPrice`](/specification/datasets/sku_price/dataset.md) (preview). The [Data Model](/specification/datasets/data_model.md) requirement to include `SkuPrice` is excluded from conformance while the dataset is a preview.

#### New columns

* [`CostAndUsage`](/specification/datasets/cost_and_usage/dataset.md)
  * [`AllocatedServiceName`](/specification/datasets/cost_and_usage/columns/allocatedservicename.md)
  * [`CredentialId`](/specification/datasets/cost_and_usage/columns/credentialid.md)
  * [`PrincipalId`](/specification/datasets/cost_and_usage/columns/principalid.md)
  * [`RequesterDetails`](/specification/datasets/cost_and_usage/columns/requesterdetails.md)
* [`SkuPrice`](/specification/datasets/sku_price/dataset.md) (preview)
  * [`ChargeCategory`](/specification/datasets/sku_price/columns/chargecategory.md)
  * [`CommitmentDiscountCategory`](/specification/datasets/sku_price/columns/commitmentdiscountcategory.md)
  * [`ContractId`](/specification/datasets/sku_price/columns/contractid.md)
  * [`PricingCurrency`](/specification/datasets/sku_price/columns/pricingcurrency.md)
  * [`PricingCurrencyCategory`](/specification/datasets/sku_price/columns/pricingcurrencycategory.md)
  * [`PricingRegionId`](/specification/datasets/sku_price/columns/pricingregionid.md)
  * [`PricingServiceName`](/specification/datasets/sku_price/columns/pricingservicename.md)
  * [`PricingUnit`](/specification/datasets/sku_price/columns/pricingunit.md)
  * [`PurchaseDurationType`](/specification/datasets/sku_price/columns/purchasedurationtype.md)
  * [`PurchasePaymentModel`](/specification/datasets/sku_price/columns/purchasepaymentmodel.md)
  * [`QuantityTierMaximum`](/specification/datasets/sku_price/columns/quantitytiermaximum.md)
  * [`QuantityTierMinimum`](/specification/datasets/sku_price/columns/quantitytierminimum.md)
  * [`ServiceProviderName`](/specification/datasets/sku_price/columns/serviceprovidername.md)
  * [`SkuId`](/specification/datasets/sku_price/columns/skuid.md)
  * [`SkuPriceCreated`](/specification/datasets/sku_price/columns/skupricecreated.md)
  * [`SkuPriceDescription`](/specification/datasets/sku_price/columns/skupricedescription.md)
  * [`SkuPriceEffectiveEnd`](/specification/datasets/sku_price/columns/skupriceeffectiveend.md)
  * [`SkuPriceEffectiveStart`](/specification/datasets/sku_price/columns/skupriceeffectivestart.md)
  * [`SkuPriceEligibility`](/specification/datasets/sku_price/columns/skupriceeligibility.md)
  * [`SkuPriceId`](/specification/datasets/sku_price/columns/skupriceid.md)
  * [`SkuPriceLastUpdated`](/specification/datasets/sku_price/columns/skupricelastupdated.md)
  * [`UnitPrice`](/specification/datasets/sku_price/columns/unitprice.md)
  * [`UnitPriceType`](/specification/datasets/sku_price/columns/unitpricetype.md)

#### New column properties

* [`SkuPriceDetails`](/specification/datasets/cost_and_usage/columns/skupricedetails.md)
  * `ModelDeveloper`
  * `ModelFamily`
  * `ModelId`
  * `ModelVersion`
  * `TokenCacheAction`
  * `TokenDirection`

#### New operating model conditions

Operating model conditions are a new specification entity. Each is a named, verifiable state (e.g., Includes Regions) that evaluates to true or false for the *operating model* behind a dataset: the combined capabilities of the participating entities (e.g., service provider, host provider, invoice issuer, data generator). v1.4 stated each presence trigger inline and tied it to one party (e.g., "when the host provider supports deploying resources or services within a region"). v1.5 replaces those triggers with references to these conditions, so each is defined once, reused across datasets, and shown in each column's Content Constraints table and in the requirements model's `Conditions` key. Most conditions restate a v1.4 trigger, generalized from one party to the operating model. The exceptions are described under Changes to Supported Features: Includes Unit Pricing replaces three separate triggers, and Includes Split Cost Allocation no longer requires the data generator to calculate the split.

* [Operating Model Conditions](/specification/operating_model_conditions/operating_model_conditions_overview.md)
  * Includes Aggregation Level Currency Differences
  * Includes Availability Zones
  * Includes Billing and Payment Currency Differences
  * Includes Capacity Reservations
  * Includes Commitment Discounts
  * Includes Commitment Programs
  * Includes Consumption Currency
  * Includes Contract Commitments
  * Includes Multiple Billing Account Types
  * Includes Multiple Pricing Categories
  * Includes Multiple Sub Account Types
  * Includes Partial Upfront Payments
  * Includes Payable Invoices
  * Includes Pricing-Billing Currency Differences
  * Includes Provisioned Resources
  * Includes Purchase Order Numbers
  * Includes Purchases (preview)
  * Includes Quantity Tier Pricing (preview)
  * Includes Regions
  * Includes Requester Attribution
  * Includes Resource Type Assignment
  * Includes Split Cost Allocation
  * Includes Sub Accounts
  * Includes Tags
  * Includes Unit Pricing
  * Includes Usage Measurement

#### New allowed and recommended values

* [`ServiceSubcategory`](/specification/datasets/cost_and_usage/columns/servicesubcategory.md): "Bare Metal" (Compute)
* [`UnitFormat`](/specification/attributes/unit_format.md): count-based units `Characters`, `Images`, `Jobs`, `Messages`, `Pages`, `Sessions`; time-based unit `Weeks`

#### New appendix entries

* [Examples: AI Model Billing](/specification/appendix/ai_model_billing_examples/ai_model_billing_examples.md)
* [Examples: AI Model Identity](/specification/appendix/ai_model_identity_examples.md)
* [Examples: AI Prompt Caching](/specification/appendix/ai_prompt_caching_examples.md)
* [Examples: Requester Details](/specification/appendix/json_object_examples/requester_details_examples.md)
* [Examples: SKU Price](/specification/appendix/sku_price_examples/sku_price_examples_overview.md)
* [Examples: SKU Price Eligibility](/specification/appendix/json_object_examples/sku_price_eligibility_examples.md)
* [Examples: Split Cost Allocation](/specification/appendix/split_cost_allocation_examples.md)
* [Consumption Currency Pricing Model](/specification/appendix/saas_examples/consumption_currency_pricing_model.md) (replaces Virtual Currency Pricing Model)
* [Requester Attribution](/specification/appendix/requester_attribution.md)
* [Split Cost Allocation Field Mapping](/specification/appendix/split_cost_allocation_field_mapping.md)

#### New glossary entries

* [Glossary](/specification/glossary.md)
  * `AI Model`
  * `Consumption Currency`
  * `Credential`
  * `Foreign Exchange (FX)`
  * `General Availability (GA)`
  * `Negotiated FX Pricing Terms`
  * `Negotiated Non-FX Pricing Terms`
  * `Negotiated Pricing Terms`
  * `Operating Model`
  * `Preview`
  * `Principal`
  * `Prompt Cache`
  * `Requester`
  * `Split Cost Allocation`
  * `Token`
  * `Unit Pricing`

#### New requirements model features

* Added the v1.5 requirements model release, including `conditions.json` for operating model conditions and JSON schemas for datasets.
* Breaking: renamed the model rule key `ApplicabilityCriteria` to `Conditions`, added a `Condition` entity type, and added `Preview` as a rule status. Tools that read the model JSON need to use the new key name. See [Writing Requirements Model Guidelines](/guidelines/contributors/writing-requirements-model-guidelines.md).
* Requirements model extraction now runs in GitHub Actions.
* Build-time validation for JSON blocks, JSON schemas, SQL example blocks, and specification links.

### Changed

#### Changed datasets

* [`CostAndUsage`](/specification/datasets/cost_and_usage/dataset.md), [`BillingPeriod`](/specification/datasets/billing_period/dataset.md), [`ContractCommitment`](/specification/datasets/contract_commitment/dataset.md), and [`InvoiceDetail`](/specification/datasets/invoice_detail/dataset.md): column presence requirements now use operating model conditions. Dataset presence requirements moved to the [Data Model](/specification/datasets/data_model.md).
* [`CostAndUsage`](/specification/datasets/cost_and_usage/dataset.md): added a note that the dataset can carry personal data, such as identity attributes in `RequesterDetails` and customer-defined values in `Tags`.

#### Changed columns

* [`ContractCommitment`](/specification/datasets/contract_commitment/dataset.md)
  * [`ContractCommitmentDurationType`](/specification/datasets/contract_commitment/columns/contractcommitmentdurationtype.md): SHOULD use the "[Numeric Value] [Unit]" format with `UnitFormat` time units, and MUST use the largest whole time-based unit.
  * [`PricingCurrency`](/specification/datasets/contract_commitment/columns/pricingcurrency.md): MUST be a national or consumption currency, with documentation requirements.
* [`CostAndUsage`](/specification/datasets/cost_and_usage/dataset.md)
  * [`AllocatedTags`](/specification/datasets/cost_and_usage/columns/allocatedtags.md): added user-defined tag key requirements.
  * [`ChargeCategory`](/specification/datasets/cost_and_usage/columns/chargecategory.md): added a requirement to match `SkuPrice.ChargeCategory` for the same `SkuPriceId` and `ServiceProviderName` on "Usage" and "Purchase" charges (excluded from conformance while SKU Price is a preview).
  * [`ConsumedQuantity`](/specification/datasets/cost_and_usage/columns/consumedquantity.md): MUST NOT double count tokens reported on a separate cache "Read" or "Write" row.
  * [`ContractedCost`](/specification/datasets/cost_and_usage/columns/contractedcost.md): redefined around negotiated pricing terms, with requirements for "Usage" and "Purchase" charges that are not corrections. The "Credit" and "Tax" rules no longer depend on `ContractedUnitPrice` being null.
  * [`ContractedUnitPrice`](/specification/datasets/cost_and_usage/columns/contractedunitprice.md): redefined around negotiated pricing terms; added Implementation Guidance.
  * [`ListCost`](/specification/datasets/cost_and_usage/columns/listcost.md): redefined around service-provider-suggested pricing, with requirements for "Usage" and "Purchase" charges that are not corrections. The "Credit" and "Tax" rules no longer depend on `ListUnitPrice` being null.
  * [`ListUnitPrice`](/specification/datasets/cost_and_usage/columns/listunitprice.md): redefined around service-provider-suggested pricing; added Implementation Guidance.
  * [`PricingCurrency`](/specification/datasets/cost_and_usage/columns/pricingcurrency.md): MUST be a national or consumption currency, with documentation requirements.
  * [`PricingCurrencyContractedUnitPrice`](/specification/datasets/cost_and_usage/columns/pricingcurrencycontractedunitprice.md): redefined to reflect negotiated non-FX pricing terms.
  * [`PricingCurrencyEffectiveCost`](/specification/datasets/cost_and_usage/columns/pricingcurrencyeffectivecost.md): clarified that values are before any currency exchange rate conversion.
  * [`PricingCurrencyListUnitPrice`](/specification/datasets/cost_and_usage/columns/pricingcurrencylistunitprice.md): redefined around service-provider-suggested pricing.
  * [`PricingQuantity`](/specification/datasets/cost_and_usage/columns/pricingquantity.md): removed the duplicative cost-formula requirement; revised the aggregation note.
  * [`ServiceCategory`](/specification/datasets/cost_and_usage/columns/servicecategory.md): allowed value descriptions are now technology-agnostic (e.g., Compute includes physical infrastructure; Migration covers moves between any environments).
  * [`ServiceSubcategory`](/specification/datasets/cost_and_usage/columns/servicesubcategory.md): added "Bare Metal" and narrowed "Virtual Machines" to hypervisor-based instances.
  * [`SkuId`](/specification/datasets/cost_and_usage/columns/skuid.md) and [`SkuMeter`](/specification/datasets/cost_and_usage/columns/skumeter.md): consistency requirements scoped to a given `ServiceProviderName`.
  * [`SkuPriceDetails`](/specification/datasets/cost_and_usage/columns/skupricedetails.md): added AI model and token properties with requirements; properties MUST use allowed values where specified; requirements scoped to a given `ServiceProviderName`.
  * [`SkuPriceId`](/specification/datasets/cost_and_usage/columns/skupriceid.md): scoped to a given `ServiceProviderName`; replaced the valid-reference requirements with requirements for one `PricingUnit`, one list and contracted unit price per scope, and no mix of "Usage" and "Purchase" charges.
  * [`Tags`](/specification/datasets/cost_and_usage/columns/tags.md): added user-defined tag key preservation requirements, restoring the key preservation in v1.0 and v1.1.

#### Changed attributes

* [`CurrencyFormat`](/specification/attributes/currency_format.md): replaced virtual currency with consumption currency; ISO 4217 codes MUST NOT be used for values that are not a national currency; added Implementation Context.
* [`CustomColumnHandling`](/specification/attributes/custom_column_handling.md): currency requirements now apply to any currency custom column, not only national currency, and documentation SHOULD say how to identify a national currency.
* [`JsonObjectFormat`](/specification/attributes/json_object_format.md): allows a top-level array as well as an object; objects in an array MUST NOT be empty and SHOULD NOT exceed 3 levels of nesting.
* [`UnitFormat`](/specification/attributes/unit_format.md): added recommended count-based units and descriptions, the `Weeks` time unit, and a SHOULD to use the largest whole time unit.

#### Changed guidelines

* [Normative Requirements Guidelines](/guidelines/contributors/normative-requirements-guidelines.md): refactored (Part 2), replaced Normative Subject with Constrainable Entity, and added composite-to-atomic resolution diagrams.
* [Spec Change Guidelines](/guidelines/contributors/spec-change-guidelines.md): added the Preview Process for designating, marking, and exiting a preview.
* [Editorial Guidelines](/guidelines/contributors/editorial-guidelines.md): added rules for note labels, informative status notes, inequalities, structural anchors, spelling out numbers, and brand-free identifiers in examples.
* [Spec Design Guidelines](/guidelines/contributors/spec-design-guidelines.md): added Example Data rules for consistent identifiers and agreement between data files and narrative.
* [Writing Requirements Model Guidelines](/guidelines/contributors/writing-requirements-model-guidelines.md) and [Dataset Mapping Documentation](/guidelines/data-generators/dataset-mapping-documentation.md): Feature Level lists now include Recommended; the requirements model guidelines also document the `Conditions` key and `Preview` status.
* [Markdown++ Guidelines](/guidelines/contributors/markdownpp-guidelines.md): updated file paths to hyphenated names.
* [Repository Naming Conventions](/guidelines/contributors/repository-naming-conventions.md): added conventions for non-Markdown file types.

#### Changed glossary entries

* [Glossary](/specification/glossary.md)
  * `Contracted Unit Price`: Revised definition.
  * `List Unit Price`: Revised definition.
  * `SKU Price`: Revised definition.
  * `Virtual Currency`: Revised definition, distinguished from *token* as a unit of measure.

#### Changed specification structure

* "Datasets" section renamed to [Data Model](/specification/datasets/data_model.md), with its own requirements and entity ID.
* Supported feature SQL examples now read from named datasets (e.g., `FROM CostAndUsage`) instead of `focus_data_table`.
* Entity anchors renamed from `#datasets.` to `#datamodel.` (e.g., `#datamodel.costandusage.billedcost`). Deep links that use the old anchors need updating.
* Each column's Content Constraints table adds an Operating model conditions row.
* The [Overview](/specification/overview.md) adds a Preview section and a Conventions statement: the Introduction, Supported Features, and Appendix (except Rounding Variance Tolerance) are informative and non-normative, as are examples and notes wherever they appear.
* Notes reformatted as labeled blockquotes across the specification, and display names capitalized consistently in column introductions.

### Removed

* Virtual Currency Pricing Model appendix entry (replaced by [Consumption Currency Pricing Model](/specification/appendix/saas_examples/consumption_currency_pricing_model.md))

## v1.4

<sup>Announced June 2026</sup>

v1.4 adds 2 datasets (`BillingPeriod`, `InvoiceDetail`), 47 new columns, 6 new attributes, 2 new supported features, and 17 new glossary entries.

### Changes to Supported Features by [Change Impact Classification](/guidelines/contributors/spec-change-guidelines.md)

#### Compatible Changes

* New Datasets and Columns to support [Invoice Reconciliation](/specification/supported_features/invoice_reconciliation.md)
* New Columns to support [Commitment Program Eligibility Details](/specification/supported_features/commitment_program_eligibility_details.md)
* Revised normative requirements for [`BilledCost`](/specification/datasets/cost_and_usage/columns/billedcost.md) and [`EffectiveCost`](/specification/datasets/cost_and_usage/columns/effectivecost.md), affecting:
  * [Billed Cost and Invoice Alignment](/specification/supported_features/billed_cost_and_invoice_alignment.md)
  * [Effective Cost](/specification/supported_features/effective_cost.md)
* Expanded [Cost Comparison](/specification/supported_features/cost_comparison.md) with cash-based vs accrual-based comparison guidance, new dependent columns, and additional example queries.
* Tightened [`InvoiceId`](/specification/datasets/cost_and_usage/columns/invoiceid.md) Feature level from Recommended to Conditional (MUST when the invoice issuer supports payable invoices).

#### Migration Compatible Changes

* Revised `ContractApplied` format to use the JSON Object Schema format. Queries that parse the `ContractApplied` JSON structure will need to be updated to the new schema. Affecting:
  * [Contract Commitments](/specification/supported_features/contract_commitments.md)
* Removal of the `ColumnHandling` attribute, with requirements shifted to `FocusColumnHandling` and `CustomColumnHandling`.
* Removal of the `DiscountHandling` attribute, with content moved to the [Discount Handling](/specification/appendix/discount_handling.md) appendix entry.
* Removal of the `InvoiceHandling` attribute, with requirements shifted to `DeliveryHandling` and `DatasetCompleteness`.
* Removal of deprecated `ProviderName` and `PublisherName` columns. Use cases were migrated to `ServiceProviderName`, `HostProviderName`, `InvoiceIssuerName`, and `DataGenerator` metadata during the v1.3 cycle. See [Participating Entity Identification](/specification/supported_features/participating_entity_identification.md) for guidance on selecting the correct successor column.

#### Incompatible Changes

* None

### Added

#### New supported features

* [Invoice Reconciliation](/specification/supported_features/invoice_reconciliation.md)
* [Commitment Program Eligibility Details](/specification/supported_features/commitment_program_eligibility_details.md)

#### New datasets

* [`BillingPeriod`](/specification/datasets/billing_period/dataset.md)
* [`InvoiceDetail`](/specification/datasets/invoice_detail/dataset.md)

#### New columns

* [`BillingPeriod`](/specification/datasets/billing_period/dataset.md)
  * [`BillingPeriodCreated`](/specification/datasets/billing_period/columns/billingperiodcreated.md)
  * [`BillingPeriodEnd`](/specification/datasets/billing_period/columns/billingperiodend.md)
  * [`BillingPeriodLastUpdated`](/specification/datasets/billing_period/columns/billingperiodlastupdated.md)
  * [`BillingPeriodStart`](/specification/datasets/billing_period/columns/billingperiodstart.md)
  * [`BillingPeriodStatus`](/specification/datasets/billing_period/columns/billingperiodstatus.md)
  * [`InvoiceIssuerName`](/specification/datasets/billing_period/columns/invoiceissuername.md)
* [`ContractCommitment`](/specification/datasets/contract_commitment/dataset.md)
  * [`ContractCommitmentApplicability`](/specification/datasets/contract_commitment/columns/contractcommitmentapplicability.md)
  * [`ContractCommitmentBenefitCategory`](/specification/datasets/contract_commitment/columns/contractcommitmentbenefitcategory.md)
  * [`ContractCommitmentCreated`](/specification/datasets/contract_commitment/columns/contractcommitmentcreated.md)
  * [`ContractCommitmentDiscountPercentage`](/specification/datasets/contract_commitment/columns/contractcommitmentdiscountpercentage.md)
  * [`ContractCommitmentDurationType`](/specification/datasets/contract_commitment/columns/contractcommitmentdurationtype.md)
  * [`ContractCommitmentFulfillmentInterval`](/specification/datasets/contract_commitment/columns/contractcommitmentfulfillmentinterval.md)
  * [`ContractCommitmentLastUpdated`](/specification/datasets/contract_commitment/columns/contractcommitmentlastupdated.md)
  * [`ContractCommitmentLifecycleStatus`](/specification/datasets/contract_commitment/columns/contractcommitmentlifecyclestatus.md)
  * [`ContractCommitmentModel`](/specification/datasets/contract_commitment/columns/contractcommitmentmodel.md)
  * [`ContractCommitmentOfferCategory`](/specification/datasets/contract_commitment/columns/contractcommitmentoffercategory.md)
  * [`ContractCommitmentPaymentInterval`](/specification/datasets/contract_commitment/columns/contractcommitmentpaymentinterval.md)
  * [`ContractCommitmentPaymentModel`](/specification/datasets/contract_commitment/columns/contractcommitmentpaymentmodel.md)
  * [`ContractCommitmentPaymentUpfrontPercentage`](/specification/datasets/contract_commitment/columns/contractcommitmentpaymentupfrontpercentage.md)
  * [`InvoiceIssuerName`](/specification/datasets/contract_commitment/columns/invoiceissuername.md)
  * [`PricingCurrency`](/specification/datasets/contract_commitment/columns/pricingcurrency.md)
  * [`PricingCurrencyContractCommitmentCost`](/specification/datasets/contract_commitment/columns/pricingcurrencycontractcommitmentcost.md)
  * [`ServiceProviderName`](/specification/datasets/contract_commitment/columns/serviceprovidername.md)
* [`CostAndUsage`](/specification/datasets/cost_and_usage/dataset.md)
  * [`CommitmentProgramEligibilityDetails`](/specification/datasets/cost_and_usage/columns/commitmentprogrameligibilitydetails.md)
  * [`InvoiceDetailId`](/specification/datasets/cost_and_usage/columns/invoicedetailid.md)
* [`InvoiceDetail`](/specification/datasets/invoice_detail/dataset.md)
  * [`BilledCost`](/specification/datasets/invoice_detail/columns/billedcost.md)
  * [`BillingAccountId`](/specification/datasets/invoice_detail/columns/billingaccountid.md)
  * [`BillingCurrency`](/specification/datasets/invoice_detail/columns/billingcurrency.md)
  * [`BillingPeriodEnd`](/specification/datasets/invoice_detail/columns/billingperiodend.md)
  * [`BillingPeriodStart`](/specification/datasets/invoice_detail/columns/billingperiodstart.md)
  * [`ChargeCategory`](/specification/datasets/invoice_detail/columns/chargecategory.md)
  * [`InvoiceDetailCreated`](/specification/datasets/invoice_detail/columns/invoicedetailcreated.md)
  * [`InvoiceDetailDescription`](/specification/datasets/invoice_detail/columns/invoicedetaildescription.md)
  * [`InvoiceDetailGrain`](/specification/datasets/invoice_detail/columns/invoicedetailgrain.md)
  * [`InvoiceDetailId`](/specification/datasets/invoice_detail/columns/invoicedetailid.md)
  * [`InvoiceDetailLastUpdated`](/specification/datasets/invoice_detail/columns/invoicedetaillastupdated.md)
  * [`InvoiceId`](/specification/datasets/invoice_detail/columns/invoiceid.md)
  * [`InvoiceIssueDate`](/specification/datasets/invoice_detail/columns/invoiceissuedate.md)
  * [`InvoiceIssueStatus`](/specification/datasets/invoice_detail/columns/invoiceissuestatus.md)
  * [`InvoiceIssuerName`](/specification/datasets/invoice_detail/columns/invoiceissuername.md)
  * [`PaymentCurrency`](/specification/datasets/invoice_detail/columns/paymentcurrency.md)
  * [`PaymentCurrencyBilledCost`](/specification/datasets/invoice_detail/columns/paymentcurrencybilledcost.md)
  * [`PaymentCurrencyInvoiceDetailId`](/specification/datasets/invoice_detail/columns/paymentcurrencyinvoicedetailid.md)
  * [`PaymentDueDate`](/specification/datasets/invoice_detail/columns/paymentduedate.md)
  * [`PaymentTerms`](/specification/datasets/invoice_detail/columns/paymentterms.md)
  * [`PurchaseOrderNumber`](/specification/datasets/invoice_detail/columns/purchaseordernumber.md)
  * [`ReferenceInvoiceId`](/specification/datasets/invoice_detail/columns/referenceinvoiceid.md)

#### New attributes

* [`CorrectionHandling`](/specification/attributes/correction_handling.md)
* [`CustomColumnHandling`](/specification/attributes/custom_column_handling.md)
* [`DatasetCompleteness`](/specification/attributes/dataset_completeness.md)
* [`DatasetConfiguration`](/specification/attributes/dataset_configuration.md)
* [`DeliveryHandling`](/specification/attributes/delivery_handling.md)
* [`FocusColumnHandling`](/specification/attributes/focus_column_handling.md)

#### New appendix entries

* [Discount Handling](/specification/appendix/discount_handling.md)
* [Examples: Commitment Program Eligibility Details](/specification/appendix/commitment_program_eligibility_details_examples.md)
* [Examples: Contract Commitments](/specification/appendix/contract_commitments/contract_commitments.md)
* [Examples: Correction Handling](/specification/appendix/correction_handling_examples/correction_handling_examples_overview.md)
* [Examples: Invoice Detail](/specification/appendix/invoice_detail/invoice_detail.md)
* [Examples: JSON Object](/specification/appendix/json_object_examples/json_object_examples_overview.md)
* [Invoice and Billing Period Handling](/specification/appendix/invoice_and_billing_period_handling.md)
* [Rounding Variance Tolerance](/specification/appendix/rounding_variance_tolerance.md)

#### New guidelines

* [AGENTS.md](/AGENTS.md)
* [AI Usage Guidelines](/guidelines/contributors/ai-usage-guidelines.md)
* [Dataset Mapping Documentation](/guidelines/data-generators/dataset-mapping-documentation.md)
* [Decision Brief Guidelines](/guidelines/contributors/decision-brief-guidelines.md)
* [Editorial Guidelines](/guidelines/contributors/editorial-guidelines.md)
* [Normative Requirements Guidelines](/guidelines/contributors/normative-requirements-guidelines.md)
* [Writing Requirements Model Guidelines](/guidelines/contributors/writing-requirements-model-guidelines.md)

#### New glossary entries

* [Glossary](/specification/glossary.md)
  * `Accrual-Based Accounting`
  * `Cash-Based Accounting`
  * `Closed Billing Period`
  * `Commitment Program`
  * `Covered Charge`
  * `Covering Charge`
  * `Custom Column`
  * `Delivery Scope`
  * `FOCUS Column`
  * `FOCUS Dataset Column`
  * `Invoice`
  * `Invoice Issuer`
  * `Invoice Reconciliation`
  * `Issued Invoice`
  * `Native Dataset`
  * `Open Billing Period`
  * `Tag Scheme`

#### New requirements model features

* Added `applicability_criteria.json` and `check_functions.json` to define baseline validation functions.
* Added `Schema` entity type (RMId format `-S-`) to allow reusable JSON Schema definitions across the requirements model. See [Writing Requirements Model Guidelines](/guidelines/contributors/writing-requirements-model-guidelines.md) for authoring details.

### Changed

#### Changed datasets

* [`CostAndUsage`](/specification/datasets/cost_and_usage/dataset.md) and [`ContractCommitment`](/specification/datasets/contract_commitment/dataset.md): Column presence requirements relocated from individual column files to dataset-level requirements, now expressed in dataset-subject form (e.g., `CostAndUsage MUST include ColumnId when Condition`). Promotes the "Column Presence in Dataset" pattern from future-use to active, centralizing presence rules previously scattered across column files. The [Normative Requirements Guidelines](/guidelines/contributors/normative-requirements-guidelines.md) were updated to document the new pattern.

#### Changed columns

* [`CostAndUsage`](/specification/datasets/cost_and_usage/dataset.md)
  * [`BilledCost`](/specification/datasets/cost_and_usage/columns/billedcost.md): Expanded requirements to clarify handling of pricing adjustments, *covered charges*, non-invoicing entities, and introduced a Rounding Variance Tolerance for invoice matching.
  * [`ContractApplied`](/specification/datasets/cost_and_usage/columns/contractapplied.md): Revised format to follow new JSON Object Schema format.
  * [`EffectiveCost`](/specification/datasets/cost_and_usage/columns/effectivecost.md): Heavily revised requirements to detail its exact relationship with `BilledCost` across various charge categories, including strict rules for amortizing *covering charges* and cross-record sum validations.
  * [`InvoiceId`](/specification/datasets/cost_and_usage/columns/invoiceid.md): Changed Feature level from Recommended to Conditional.
  * [`PricingCurrencyEffectiveCost`](/specification/datasets/cost_and_usage/columns/pricingcurrencyeffectivecost.md): Description expanded to position it as the `PricingCurrency`-denominated equivalent of `EffectiveCost`. Added a requirement that values MUST equal the `PricingCurrency`-denominated equivalent of `EffectiveCost`.

#### Changed attributes

* [`CurrencyFormat`](/specification/attributes/currency_format.md): Requirements simplified to mandate ISO 4217:2015 three-letter codes for all currency values. Removed the prior allowance for virtual currency values to use `StringHandling` rules.
* [`JsonObjectFormat`](/specification/attributes/json_object_format.md): Removed the requirement for data generators to document JSON object schemas for custom columns. Retained other requirements.
* [`NullHandling`](/specification/attributes/null_handling.md): Clarified that empty-string and placeholder-value prohibitions apply to absent-value scenarios, and split into separate rules for string and numeric columns.
* [`NumericFormat`](/specification/attributes/numeric_format.md): Added normative tables specifying allowed Data Types and Allowed Precisions, replacing the v1.3 pattern that delegated precision to data generator documentation.
* [`StringHandling`](/specification/attributes/string_handling.md): Restructured rules for mutable versus immutable string values into an explicit set, and added new guidance on handling corrections to previously closed billing periods.
* [`UnitFormat`](/specification/attributes/unit_format.md): Significantly expanded with normative rules for base units (data size, time-based, count-based), compound units, ratio units, and unit quantities. New definitions section clarifies terminology.
* All attributes additionally refactored to a consistent structural format shared with datasets, columns, and other entities.

#### Changed guidelines

* Deprecated the normative keyword "RECOMMENDED" in favor of "SHOULD" to align with [BCP-14](https://www.rfc-editor.org/info/bcp14), which treats the two as synonyms. Improves terminology consistency without changing the conformance strength of existing requirements.

#### Changed glossary entries

* [Glossary](/specification/glossary.md)
  * `Allocated Charge`: Revised definition.
  * `Allocated Method`: Revised definition.
  * `Commitment Discount`: Revised definition.
  * `Contracted Unit Price`: Revised definition.
  * `Correction`: Revised definition.
  * `Dataset Instance`: Revised definition.
  * `Dataset Instance Artifact`: Revised definition.
  * `List Unit Price`: Revised definition.
  * `Negotiated Discount`: Revised definition.
  * `Origin Charge`: Revised definition.
  * `Service`: Revised definition.
  * `Term`: Updated definition to apply to agreements specified on a contract *or* invoice.

### Removed

* `ProviderName` column (deprecated in v1.3, removed in v1.4)
* `PublisherName` column (deprecated in v1.3, removed in v1.4)
* `ColumnHandling` attribute (requirements shifted to `FocusColumnHandling` and `CustomColumnHandling`)
* `DiscountHandling` attribute (content moved to the [Discount Handling](/specification/appendix/discount_handling.md) appendix entry)
* `InvoiceHandling` attribute (requirements shifted to `DeliveryHandling` and `DatasetCompleteness`)
* `Billed Cost` glossary entry
* `Effective Cost` glossary entry

## v1.3

<sup>Announced December 2025</sup>

> ⚠️ **Note: Errata Available**
> A list of non-material editorial corrections and clarifications for this release can be found in the [FOCUS 1.3 Errata](ERRATA.md#version-13). Please review this document alongside the 1.3 specification.

### Changes to Supported Features by [Change Impact Classification](/guidelines/contributors/spec-change-guidelines.md)

#### Compatible Changes

* New Columns to support [Data Generator-Calculated Split Cost Allocation](/specification/supported_features/data_generator_calculated_split_cost_allocation.md)
* New Dataset and Columns to support [Contract Commitments](/specification/supported_features/contract_commitments.md)
* New Columns to support [Participating Entity Identification](/specification/supported_features/participating_entity_identification.md)
* New Metadata to support [Dataset Instance Metadata](/specification/supported_features/dataset_instance_metadata.md)
* New Metadata to support [Recency Metadata](/specification/supported_features/recency_metadata.md)

#### Migration Compatible Changes

* Replacement of Provider and Publisher Columns, affecting:
  * [Charge Categorization](/specification/supported_features/charge_categorization.md)
  * [Commit Usage and Under Usage](/specification/supported_features/commit_usage_and_under_usage.md)
  * [Cost Comparison](/specification/supported_features/cost_comparison.md)
  * [Effective Cost](/specification/supported_features/effective_cost.md)
  * [Marketplace Purchases](/specification/supported_features/marketplace_purchases.md)
  * [Participating Entity Identification](/specification/supported_features/participating_entity_identification.md)
  * [Provider Services](/specification/supported_features/provider_services.md)
  * [Resource Usage](/specification/supported_features/resource_usage.md)
  * [Service Categorization](/specification/supported_features/service_categorization.md)

#### Incompatible Changes

* None

### Added

#### New supported features

* [Contract Commitments](/specification/supported_features/contract_commitments.md)
* [Dataset Instance Metadata](/specification/supported_features/dataset_instance_metadata.md)
* [Participating Entity Identification](/specification/supported_features/participating_entity_identification.md)
* [Data Generator-Calculated Split Cost Allocation](/specification/supported_features/data_generator_calculated_split_cost_allocation.md)
* [Recency Metadata](/specification/supported_features/recency_metadata.md)

#### New datasets

* [`ContractCommitment`](/specification/datasets/contract_commitment/dataset.md)

#### New columns

* [`CostAndUsage`](/specification/datasets/cost_and_usage/dataset.md)
  * [`AllocatedMethodDetails`](/specification/datasets/cost_and_usage/columns/allocatedmethoddetails.md)
  * [`AllocatedMethodId`](/specification/datasets/cost_and_usage/columns/allocatedmethodid.md)
  * [`AllocatedResourceId`](/specification/datasets/cost_and_usage/columns/allocatedresourceid.md)
  * [`AllocatedResourceName`](/specification/datasets/cost_and_usage/columns/allocatedresourcename.md)
  * [`AllocatedTags`](/specification/datasets/cost_and_usage/columns/allocatedtags.md)
  * [`ContractApplied`](/specification/datasets/cost_and_usage/columns/contractapplied.md)
  * [`HostProviderName`](/specification/datasets/cost_and_usage/columns/hostprovidername.md)
  * [`ServiceProviderName`](/specification/datasets/cost_and_usage/columns/serviceprovidername.md)
* [`ContractCommitment`](/specification/datasets/contract_commitment/dataset.md)
  * [`BillingCurrency`](/specification/datasets/contract_commitment/columns/billingcurrency.md)
  * [`ContractCommitmentCategory`](/specification/datasets/contract_commitment/columns/contractcommitmentcategory.md)
  * [`ContractCommitmentCost`](/specification/datasets/contract_commitment/columns/contractcommitmentcost.md)
  * [`ContractCommitmentId`](/specification/datasets/contract_commitment/columns/contractcommitmentid.md)
  * [`ContractCommitmentPeriodEnd`](/specification/datasets/contract_commitment/columns/contractcommitmentperiodend.md)
  * [`ContractCommitmentPeriodStart`](/specification/datasets/contract_commitment/columns/contractcommitmentperiodstart.md)
  * [`ContractCommitmentQuantity`](/specification/datasets/contract_commitment/columns/contractcommitmentquantity.md)
  * [`ContractCommitmentType`](/specification/datasets/contract_commitment/columns/contractcommitmenttype.md)
  * [`ContractCommitmentUnit`](/specification/datasets/contract_commitment/columns/contractcommitmentunit.md)
  * [`ContractId`](/specification/datasets/contract_commitment/columns/contractid.md)
  * [`ContractPeriodEnd`](/specification/datasets/contract_commitment/columns/contractperiodend.md)
  * [`ContractPeriodStart`](/specification/datasets/contract_commitment/columns/contractperiodstart.md)

#### New attributes

* [`InvoiceHandling`](/specification/attributes/invoice_handling.md)
* [`JsonObjectFormat`](/specification/attributes/json_object_format.md)
* [`DataGeneratorCalculatedSplitCostAllocationHandling`](/specification/attributes/data_generator_calculated_split_cost_allocation_handling.md)

#### New appendix entries

* [Dataset Instance metadata example](/specification/appendix/metadata_examples/dataset_instance_metadata_example.md)
* [Recency metadata example](/specification/appendix/metadata_examples/recency_metadata_example.md)
* [Recency metadata updating over time](/specification/appendix/metadata_examples/recency_metadata_updating_over_time_dataset_example.md)
* [Recency metadata updating not over time](/specification/appendix/metadata_examples/recency_metadata_updating_non_over_time_dataset_example.md)
* [Schema Dataset Instance ID example](/specification/appendix/metadata_examples/schema_dataset_instance_id_example.md)

#### New metadata column definition properties

* [`DatasetInstance`](/specification/metadata/dataset_instance/dataset_instance_overview.md)
  * [`DatasetInstanceId`](/specification/metadata/dataset_instance/dataset_instance_id.md)
  * [`DatasetInstanceName`](/specification/metadata/dataset_instance/dataset_instance_name.md)
  * [`FocusDatasetId`](/specification/metadata/dataset_instance/focus_dataset_id.md)
* [`Recency`](/specification/metadata/recency/recency_overview.md)
  * [`DatasetInstanceComplete`](/specification/metadata/recency/dataset_instance_complete.md)
  * [`DatasetInstanceId`](/specification/metadata/recency/dataset_instance_id.md)
  * [`DatasetInstanceLastUpdated`](/specification/metadata/recency/dataset_instance_last_updated.md)
  * [`RecencyLastUpdated`](/specification/metadata/recency/recency_last_updated.md)
  * [`TimeSectors`](/specification/metadata/recency/time_sectors/time_sectors_overview.md)
    * [`TimeSectorComplete`](/specification/metadata/recency/time_sectors/time_sector_complete.md)
    * [`TimeSectorEnd`](/specification/metadata/recency/time_sectors/time_sector_end.md)
    * [`TimeSectorLastUpdated`](/specification/metadata/recency/time_sectors/time_sector_last_updated.md)
    * [`TimeSectorStart`](/specification/metadata/recency/time_sectors/time_sector_start.md)

#### New glossary entries

* [Glossary](/specification/glossary.md)
  * `Allocated Charge`
  * `Allocated Method`
  * `Contract`
  * `Contract Commitment`
  * `Dataset Artifact`
  * `Dataset Instance`
  * `Dataset Instance Artifact`
  * `JSON`
  * `Origin Charge`
  * `Period`

#### New requirements model

The specification's normative requirements are now maintained in a structured, graph-based collection of rules.  Version 1.2 of the requirements model is available as of this writing; 1.3 will be released during the 1.4 development cycle.  This requirements model is designed to be leveraged by a conformance validator, maintained [here](https://github.com/finopsfoundation/focus_validator).  For more information on the requirements model, see [here](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/working_draft/specification/requirements_model/README.md).

### Changed

#### Changed datasets

* [`CostAndUsage`](/specification/datasets/cost_and_usage/dataset.md)
  * FOCUS had only one dataset prior to 1.3, and thus it did not have a name.  See below for a list of changed columns.
* Datasets are now explicitly associated with attributes via normative requirements; this was previously implied.
* Datasets now have their column set laid out in tabular format within their respective entries.

#### Changed columns

* [`CostAndUsage`](/specification/datasets/cost_and_usage/dataset.md)
  * [`CommitmentDiscountQuantity`](/specification/datasets/cost_and_usage/columns/commitmentdiscountquantity.md)
    * CommitmentDiscountQuantity MUST be null when SkuPriceId is null.  This requirement was previously implied, but not directly stated.
  * [`ConsumedQuantity`](/specification/datasets/cost_and_usage/columns/consumedquantity.md)
    * ConsumedQuantity MUST be null when SkuPriceId is null.  This requirement was previously implied, but not directly stated.
  * [`ContractedCost`](/specification/datasets/cost_and_usage/columns/contractedcost.md)
    * ContractedCost MUST equal the product of ContractedUnitPrice and PricingQuantity when ContractedUnitPrice is not null and PricingQuantity is not null.  This requirement was previously implied, but not directly stated.
  * [`ContractedUnitPrice`](/specification/datasets/cost_and_usage/columns/contractedunitprice.md)
    * ContractedUnitPrice MUST be null when SkuPriceId is null.  This requirement was previously implied, but not directly stated.
    * ContractedUnitPrice MUST NOT be null when SkuPriceId is not null.  This requirement was previously implied, but not directly stated.
  * [`InvoiceId`](/specification/datasets/cost_and_usage/columns/invoiceid.md)
    * The sum of BilledCost for a given InvoiceId MUST match the sum of the payable amount provided in the corresponding invoice with the same id generated by the InvoiceIssuerName.  This requirement was previously implied, but not directly stated.
  * [`InvoiceIssuerName`](/specification/datasets/cost_and_usage/columns/invoiceissuername.md)
    * The display name has changed from `Invoice Issuer` to `Invoice Issuer Name`. The column ID and definition remains the same.
  * [`ListCost`](/specification/datasets/cost_and_usage/columns/listcost.md)
    * Discrepancies are no longer allowed for corrections.  Now, in all cases, ListCost MUST equal the product of ListUnitPrice and PricingQuantity when ListUnitPrice is not null and PricingQuantity is not null.
  * [`ListUnitPrice`](/specification/datasets/cost_and_usage/columns/listunitprice.md)
    * ListUnitPrice MUST be null when SkuPriceId is null.  This requirement was previously implied, but not directly stated.
    * ListUnitPrice MUST NOT be null when SkuPriceId is not null.  This requirement was previously implied, but not directly stated.
  * [`PricingCategory`](/specification/datasets/cost_and_usage/columns/pricingcategory.md)
    *  PricingCategory MUST be null when SkuPriceId is null.  This requirement was previously implied, but not directly stated.
  * [`PricingCurrencyContractedUnitPrice`](/specification/datasets/cost_and_usage/columns/pricingcurrencycontractedunitprice.md)
    * PricingCurrencyContractedUnitPrice MUST be null when SkuPriceId is null.  This requirement was previously implied, but not directly stated.
    * PricingCurrencyContractedUnitPrice MUST NOT be null when SkuPriceId is not null.  This requirement was previously implied, but not directly stated.
  * [`PricingCurrencyListUnitPrice`](/specification/datasets/cost_and_usage/columns/pricingcurrencylistunitprice.md)
    * PricingCurrencyListUnitPrice MUST be null when SkuPriceId is null.  This requirement was previously implied, but not directly stated.
    * PricingCurrencyListUnitPrice MUST NOT be null when SkuPriceId is not null.  This requirement was previously implied, but not directly stated.
  * [`PricingQuantity`](/specification/datasets/cost_and_usage/columns/pricingquantity.md)
    * PricingQuantity MUST be null when SkuPriceId is null.  This requirement was previously implied, but not directly stated.
    * PricingQuantity MUST be a valid decimal value when not null.  This requirement was previously implied, but not directly stated.

#### Changed attributes

* None

#### Changed appendix entries

* Metadata examples now include use of `DatasetInstanceId`.
* [Participating Entity Identification](/specification/appendix/participating_entity_identification.md) replaces Origination of Cost Data.  
  * The layout and functionality is the same, but the entities have been renamed, and new entries have been included.

#### Changed metadata

##### Changed metadata properties

* None

#### Changed glossary entries

* [Glossary](/specification/glossary.md)
  * `Commitment` has been changed to include both spend and usage, not just usage.
  * `FOCUS Dataset` is now more narrowly defined alongside `Dataset Artifact` and `Dataset Instance`.
  * `Term` is now strictly associated with agreements specified on a contract.  Some legacy use of that term was associated with length of time, and that use has now been replaced by `Period`.

### Deprecated

#### Deprecated columns
This functionality will be removed in a future release of FOCUS.

* [`CostAndUsage`](/specification/datasets/cost_and_usage/dataset.md)
  * [`ProviderName`](/specification/datasets/cost_and_usage/columns/providername.md)
    * Due to definitional conflicts between the Provider and Publisher columns, this column is deprecated and will be removed in a future release. This column was replaced with the new ServiceProviderName column.  
  * [`PublisherName`](/specification/datasets/cost_and_usage/columns/publishername.md)
    * Due to definitional conflicts between the Provider and Publisher columns, this column is deprecated and will be removed in a future release.

<br>

## v1.2

<sup>Announced June 2025</sup>

### Added

#### New columns

* `BillingAccountType`
* `InvoiceID`
* `PricingCurrency`
* `PricingCurrencyContractedUnitPrice`
* `PricingCurrencyEffectiveCost`
* `PricingCurrencyListUnitPrice`
* `SubAccountType`

#### New appendix entries

* Added examples for commitment discount flexibility.
* Added examples for SaaS scenarios.

#### New supported features

* Added list of features the specification supports.  See the `supported_features` subfolder for a full list.

#### New metadata column definition properties

* `Deprecated`
* `PreviousColumnName`

### Changed

#### Changed columns

* Normative requirements guidelines have been applied to all columns. While the formatting has changed significantly, the vast majority of such changes are not material unless specifically called out in the below list.
* `AvailabilityZone`
  * Added a requirement that the value must be null when a charge is not specific to an availability zone.
* `BilledCost`
  * Added requirement that the value must be 0 when payments are received by a third-party (e.g., marketplace).
  * Added requirement that the sum of BilledCost for an Invoice ID must match the payable amount on a corresponding invoice.
* `BillingAccountName`
  * Removed requirement of uniqueness within a customer context.
* `ChargeDescription`
  * Changed recommendation to specify maximum length in the Metadata Schema instead of publicly available documentation.
* `CommitmentDiscountQuantity`
  * Revised requirement of value range to allow any valid decimal value.
* `CommitmentDiscountUnit`
  * Revised requirement of nullability to be tied to the nullability of CommitmentDiscountQuantity (e.g., must be null when CommitmentDiscountQuantity is null).
* `ConsumedQuantity`
  * Revised requirement of value range to allow any valid decimal value.
* `ConsumedUnit`
  * Revised requirement of nullability to be tied to the nullability of ConsumedQuantity (e.g., must be null when ConsumedQuantity is null).
* `EffectiveCost`
  * Clarified requirements for aggregation of values.
* `PricingUnit`
  * Revised requirement of nullability to be tied to the nullability of PricingQuantity (e.g., must be null when PricingQuantity is null).
* `RegionName`
  * Revised requirement of nullability to be tied to the nullability of RegionId (e.g., must be null when RegionId is null).
* `ResourceId`
  * Revised requirement for uniqueness: the value must be unique within the provider.
* `ServiceName`
  * Added requirement for mapping the value to a single ServiceCategory or "Other".
  * Added recommendation for mapping the value to a single ServiceSubcategory or "Other".
* `SkuId`
  * Revised column definition to position SkuId as a stable, functional identifier beyond pricing constructs.
  * Revised requirement for presence: the value must be present when the provider supports unit pricing and publishes price lists.
  * Added requirements for a SkuId to be consistent across variations of billing accounts, contracts, and prices.
* `SkuMeter`
  * Revised requirement for presence: the value must be present when the provider supports unit pricing and publishes price lists.
* `SkuPriceDetails`
  * Defined a set of FOCUS-specified property names and units, and added requirements for how they are used.
  * Added requirement that custom properties must prefix names with "x_".
  * Revised requirement for presence: the value must be present when the provider supports unit pricing and publishes price lists.
* `SkuPriceId`
  * Revised requirement for presence: the value must be present when the provider supports unit pricing and publishes price lists.
  * Revised requirement that the value must have a single parent SkuId, removing the prior exception for commitment discount flexibility.
  * Added requirement that the value must be associated with a given resource or service when ChargeCategory is "Usage" or "Purchase".
  * Added requirements for a SkuPriceId to be consistent across variations of billing accounts and contracts.
* `SubAccountName`
  * Revised requirement of nullability to be tied to the nullability of SubAccountId (e.g., must be null when SubAccountId is null).
* `Tags`
  * Resolved bug involving multiple user-defined tag structures.

#### Changed attributes

* `ColumnNamingAndOrdering`
  * Renamed attribute to `ColumnHandling`.
* `CurrencyCodeFormat`
  * Renamed attribute to `CurrencyFormat`.
  * Augmented definition to handle for virtual currencies.

#### Changed appendix entries

* Revised the ordering of appendix entries.
* Moved appendix examples to CSV section.

#### Changed metadata

##### Changed metadata properties

* `ProviderVersion`
  * Renamed field to `DataGeneratorVersion`.

<br>

## v1.1

<sup>Announced November 2024</sup>

**Added:**

* `CapacityReservationId` column
* `CapacityReservationStatus` column
* `CommitmentDiscountQuantity` column
* `CommitmentDiscountUnit` column
* `ServiceSubcategory` column
* `SkuMeter` column
* `SkuPriceDetails` column
* `ProviderVersion` metadata schema property

**Changed:**

* `CommitmentDiscountId` column updates:
  * Must be globally unique within the provider.
  * Should be a fully-qualified identifier.
* `ConsumedQuantity` column updates:
  * Must be null when `CommitmentDiscountStatus` is "Unused".
* `ConsumedUnit` column updates:
  * Must be null when `ChargeClass` is not "Correction" and `ChargeCategory` is not "Usage".
  * Must be null when `ChargeClass` is not "Correction" and `ChargeCategory` is "Usage" and `CommitmentDiscountStatus` is "Unused".
  * May be null when `ChargeCategory` is "Usage" and `ChargeClass` is "Correction".
* `EffectiveCost` column updates:
  * When `CommitmentDiscountStatus` is "Unused", must be the difference between the used commitment discount amount and the portion of the total commitment discount purchase applicable for the charge period.
* `PricingCategory` column updates:
  * Must not be "Committed" when the charge is for a commitment discount purchase.
* `SkuPriceId` column updates:
  * `SkuId` can be used if the provider does not have a `SkuPriceId` but other requirements must be met.
* Metadata updates:
  * Must be provided in the defined metadata schema.
  * Must be an object.
  * Must not be null.
  * Must include a reference to the schema of the data.
  * Schema reference must not be in the FOCUS dataset itself.
  * Must be an accurate and complete representation of the provided FOCUS dataset.
  * Metadata implementation should be publicly documented.
* `SchemaId` metadata schema property updates:
  * Recommended to be a globally unique identifier (GUID) instead of a universally unique identifier (UUID) or SemVer version.

[All 1.1 changes](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/compare/v1.0...v1.1)

<br>

## v1.0

<sup>Announced June 20, 2024</sup>

**Added:**

New use cases:
* Compare Billed Cost per Sub Account to budget

New attributes:
* `String handling`

New columns:
* `ChargeClass`
* `CommitmentDiscountStatus`
* `ContractedCost`
* `ContractedUnitPrice`
* `RegionId`
* `RegionName`

New metadata properties:
* `DataGenerator`

New metadata schema properties:
* `CreationDate`
* `FocusVersion`
* `SchemaId`

New metadata column definition properties:
* `ColumnName`
* `DataType`
* `NumberScale`
* `NumberPrecision`
* `ProviderTagPrefix`
* `StringEncoding`
* `StringMaxLength`

**Changed:**

* `Column naming convention` attribute includes the following new provisions:
  * Column IDs should not exceed 50 characters.
  * Attribute renamed to `Column naming and ordering` to denote it also includes rules for column ordering.
* `ChargeCategory` column updates:
  * Added "Credit" value for credits and any applicable credit corrections. See added `ChargeClass` column.
  * Updated "Usage", "Purchase", and "Tax" to include refunds/corrections. See added `ChargeClass` column.
  * Updated "Adjustment" value to exclude credits and refunds.
* `ChargeFrequency` column updates:
  * Column is recommended and may not be present.
* `CommitmentDiscountCategory` column updates:
  * Column is conditional and only required when the provider supports commitment discounts.
* `CommitmentDiscountId` column updates:
  * Column is conditional and only required when the provider supports commitment discounts.
* `CommitmentDiscountName` column updates:
  * Column is conditional and only required when the provider supports commitment discounts.
* `CommitmentDiscountType` column updates:
  * Column is conditional and only required when the provider supports commitment discounts.
* `ConsumedQuantity` column updates:
  * Column renamed from UsageQuantity. It is now limited to ChargeType "Usage" rows.
  * Column is conditional and only required when the provider supports the measurement of usage.
  * Column must not be null when `ChargeCategory` is "Usage" and `ChargeClass` is not "Correction".
* `ConsumedUnit` column updates:
  * Column renamed from UsageUnit. It is now limited to ChargeType "Usage" rows.
  * Column is conditional and only required when the provider supports the measurement of usage.
  * Column must not be null when `ChargeCategory` is "Usage" and `ChargeClass` is not "Correction".
* `EffectiveCost` column updates:
  * Clarified that effective cost does not mix or "blend" costs across multiple charges.
  * Specified that in the case of a purchase charge paid to cover future eligible charges, the Effective Cost is set to 0.
* `ListUnitPrice` column updates:
  * Column is conditional and only required when the provider publishes a price list that excludes discounts.
  * Must not be null when `ChargeClass` is not "Correction" and `ChargeCategory` is "Usage" or "Purchase".
  * Must be null when `ChargeCategory` is "Tax".
* `PricingCategory` column updates:
  * Column is conditional and only required when the provider supports more than one pricing category value.
  * Changed "On-Demand" to "Standard".
  * Changed "Commitment-Based" to "Committed".
  * Must not be null when `ChargeClass` is not "Correction" and `ChargeCategory` is "Usage" or "Purchase".
  * Must be null when `ChargeCategory` is "Tax".
* `PricingQuantity`
  * Must not be null when `ChargeClass` is not "Correction" and `ChargeCategory` is "Usage" or "Purchase".
  * Must be null when `ChargeCategory` is "Tax".
* `PricingUnit`
  * Must not be null when `ChargeClass` is not "Correction" and `ChargeCategory` is "Usage" or "Purchase".
  * Must be null when `ChargeCategory` is "Tax".
* `RegionId` column updates:
  * `Region` column was renamed to `RegionId` when `RegionName` column was introduced
* `ResourceId` column updates:
  * Column is conditional and only required when the provider supports billing based on provisioned resource instances.
* `ResourceName` column updates:
  * Column is conditional and only required when the provider supports billing based on provisioned resource instances.
* `ResourceType` column updates:
  * Column is conditional and only required when the provider supports billing based on provisioned resource instances and supports multiple "types" of resources.
* `SkuId` column updates:
  * Column is conditional and only required when the provider publishes a SKU list.
  * Must not be null when `ChargeClass` is not "Correction" and `ChargeCategory` is "Usage" or "Purchase".
  * Must be null when `ChargeCategory` is "Tax".
* `SkuPriceId` column updates:
  * Column is conditional and only required when the provider publishes a SKU price list.
  * Must not be null when `ChargeClass` is not "Correction" and `ChargeCategory` is "Usage" or "Purchase".
  * Must be null when `ChargeCategory` is "Tax".
* `SubAccountId` column updates:
  * Column is conditional and only required when the provider supports a sub account construct.
* `SubAccountName` column updates:
  * Column is conditional and only required when the provider supports a sub account construct.
* `Tags` column updates:
  * Column is conditional and only required when the provider supports setting user- or provider-defined tags.
  * Tag keys that cannot have a value must use a boolean `true` as the tag value.

**Fixed:**

* `CommitmentDiscountType` column constraints were updated to show the column as required to align with the normative text.

**Removed:**

* `ChargeSubcategory` column - See `ChargeCategory` and `ChargeClass` columns

[All 1.0 changes](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/compare/v1.0-preview...v1.0)

<br>

## v1.0-preview

<sup>Announced November 15, 2023</sup>

**Added:**

* `Discount handling` attribute
* `Key/value format` attribute
* `Numeric format` attribute
* `Unit format` attribute
* `ChargeDescription` column
* `ChargeFrequency` column
* `ChargeSubcategory` column
* `CommitmentDiscountCategory` column
* `CommitmentDiscountId` column
* `CommitmentDiscountName` column
* `CommitmentDiscountType` column
* `ListCost` column
* `ListUnitPrice` column
* `PricingCategory` column
* `PricingQuantity` column
* `PricingUnit` column
* `ResourceType` column
* `SkuId` column
* `SkuPriceId` column
* `Tags` column
* `UsageQuantity` column
* `UsageUnit` column

**Changed:**

* `Column naming convention` attribute includes the following new provisions:
  * Columns with a `Category` suffix must be normalized.
  * External, custom columns can be added but must be prefixed by `x_`.
  * FOCUS columns must be listed before custom columns in the dataset.
  * Added "SKU" as an exception to the "no acronyms" rule. The display name is "SKU" and column ID is `Sku`.
* `AmortizedCost` column renamed to `EffectiveCost`
* `ChargeType` column renamed to `ChargeCategory`

[All 1.0-preview changes](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/compare/v0.5...v1.0-preview)

<br>

## v0.5

<sup>Announced June 24, 2023</sup>

**Added:**

* `Column naming convention` attribute
* `Currency code format` attribute
* `Date/time format` attribute
* `Null handling` attribute
* `AmortizedCost` column
* `AvailabilityZone` column
* `BilledCost` column
* `BillingAccountId` column
* `BillingAccountName` column
* `BillingCurrency` column
* `BillingPeriodEnd` column
* `BillingPeriodStart` column
* `ChargePeriodEnd` column
* `ChargePeriodStart` column
* `ChargeType` column
* `InvoiceIssuerName` column
* `ProviderName` column
* `PublisherName` column
* `Region` column
* `ResourceId` column
* `ResourceName` column
* `ServiceCategory` column
* `ServiceName` column
* `SubAccountId` column
* `SubAccountName` column

[All 0.5 changes](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/compare/7106bbe...v0.5)

<br>

## Columns History

This table maps the evolution of the specification, showcasing column introductions and updates from its initial version 0.5 to the comprehensive revisions in "1.0-preview", "1.0" and beyond.

| **Column ID**                | **Revision Introduced** | **Status**        |
|------------------------------|-------------------------|-------------------|
| AmortizedCost                | 0.5                     | Renamed to EffectiveCost in v1.0-preview |
| AvailabilityZone             | 0.5                     |                   |
| BilledCost                   | 0.5                     |                   |
| BillingAccountId             | 0.5                     |                   |
| BillingAccountName           | 0.5                     |                   |
| BillingAccountType           | 1.2                     |                   |
| BillingCurrency              | 0.5                     |                   |
| BillingPeriodEnd             | 0.5                     |                   |
| BillingPeriodStart           | 0.5                     |                   |
| CapacityReservationId        | 1.1                     |                   |
| CapacityReservationStatus    | 1.1                     |                   |
| ChargeType                   | 0.5                     | Renamed to ChargeCategory in v1.0-preview |
| ChargeCategory               | 1.0-preview             | Renamed from ChargeType in v1.0-preview |
| ChargeClass                  | 1.0                     |                   |
| ChargeDescription            | 1.0-preview             |                   |
| ChargeFrequency              | 1.0-preview             |                   |
| ChargePeriodEnd              | 0.5                     |                   |
| ChargePeriodStart            | 0.5                     |                   |
| ChargeSubcategory            | 1.0-preview             | Removed in v1.0   |
| CommitmentDiscountCategory   | 1.0-preview             |                   |
| CommitmentDiscountId         | 1.0-preview             |                   |
| CommitmentDiscountName       | 1.0-preview             |                   |
| CommitmentDiscountStatus     | 1.0                     |                   |
| CommitmentDiscountType       | 1.0-preview             |                   |
| CommitmentDiscountQuantity   | 1.1                     |                   |
| CommitmentDiscountUnit       | 1.1                     |                   |
| ConsumedQuantity             | 1.0                     | Renamed from UsageQuantity in v1.0 |
| ConsumedUnit                 | 1.0                     | Renamed from UsageUnit in v1.0 |
| ContractedCost               | 1.0                     |                   |
| ContractedUnitPrice          | 1.0                     |                   |
| EffectiveCost                | 1.0-preview             | Renamed from AmortizedCost in v1.0-preview |
| InvoiceId                    | 1.2                     |                   |
| InvoiceIssuerName            | 0.5                     |                   |
| ListCost                     | 1.0-preview             |                   |
| ListUnitPrice                | 1.0-preview             |                   |
| PricingCategory              | 1.0-preview             |                   |
| PricingCurrency              | 1.2                     |                   |
| PricingCurrencyContractedUnitPrice | 1.2               |                   |
| PricingCurrencyEffectiveCost | 1.2                     |                   |
| PricingCurrencyListUnitPrice | 1.2                     |                   |
| PricingQuantity              | 1.0-preview             |                   |
| PricingUnit                  | 1.0-preview             |                   |
| ProviderName                 | 0.5                     |                   |
| PublisherName                | 0.5                     |                   |
| Region                       | 0.5                     | Renamed to RegionId in v1.0 |
| RegionId                     | 1.0                     | Renamed from Region in v1.0 |
| RegionName                   | 1.0                     |                   |
| ResourceId                   | 0.5                     |                   |
| ResourceName                 | 0.5                     |                   |
| ResourceType                 | 1.0-preview             |                   |
| ServiceCategory              | 0.5                     |                   |
| ServiceName                  | 0.5                     |                   |
| ServiceSubcategory           | 1.1                     |                   |
| SkuId                        | 1.0-preview             |                   |
| SkuMeter                     | 1.1                     |                   |
| SkuPriceDetails              | 1.1                     |                   |
| SkuPriceId                   | 1.0-preview             |                   |
| SubAccountId                 | 0.5                     |                   |
| SubAccountName               | 0.5                     |                   |
| SubAccountType               | 1.2                     |                   |
| Tags                         | 1.0-preview             |                   |
| UsageQuantity                | 1.0-preview             | Renamed to ConsumedQuantity in v1.0 |
| UsageUnit                    | 1.0-preview             | Renamed to ConsumedUnit in v1.0 |

