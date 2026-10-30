---
aliases:
  covered-charge: [covered]
  cash-based-accounting: [cash-based]
---

# Glossary

<a name="glossary:accrual-based-accounting"><b>Accrual-Based Accounting</b></a>

An accounting method used in technology cost management to record costs in the period when resources are utilized, services are delivered, or entitlements are available for or actually consumed (including unused or expired entitlements). This approach ensures that expenses are recognized in the same timeframe as the value they provide, independent of when charges are invoiced.

<a name="glossary:adjustment"><b>Adjustment</b></a>

A charge representing a modification to billing data to account for certain events or circumstances not previously captured, or captured incorrectly. Examples include billing errors, service disruptions, or pricing changes.

<a name="glossary:ai-model"><b>AI Model</b></a>

A trained machine learning system (e.g., a large language model) that produces output, such as text, images, or embeddings, from input content.

<a name="glossary:allocated-charge"><b>Allocated Charge</b></a>

The [charge](#term) that was created as the result of an allocation operation. This is used in the context of [Data Generator-Calculated Split Cost Allocation](#supportedfeatures.datagenerator-calculatedsplitcostallocation) to identify the charges that were created from the [origin charge](#term) resulting from the application of Data Generator-Calculated Split Cost Allocation.

<a name="glossary:allocated-method"><b>Allocated Method</b></a>

The process or formula by which cost is being allocated from an [origin charge](#term) to produce [allocated charges](#term). This is used in the context of [Data Generator-Calculated Split Cost Allocation](#supportedfeatures.datagenerator-calculatedsplitcostallocation) which requires documentation of the method to be provided for any and all allocated methods used. May also be colloquially referred to as allocation method.

<a name="glossary:amortization"><b>Amortization</b></a>

The distribution of upfront costs over time to accurately reflect the consumption or benefit derived from the associated resources or services. Amortization is valuable when the commitment [period](#term) extends beyond the granularity of the source report.

<a name="glossary:availability-zone"><b>Availability Zone</b></a>

A collection of geographically separated locations containing a data center or cluster of data centers. Each availability zone (AZ) should have its own power, cooling, and networking, to provide redundancy and fault tolerance.

<a name="glossary:billing-account"><b>Billing Account</b></a>

A container for resources and/or services that are billed together in an invoice. A billing account may have sub accounts, all of whose costs are consolidated and invoiced to the billing account.

<a name="glossary:billing-currency"><b>Billing Currency</b></a>

An identifier that represents the currency that a charge for resources and/or services was billed in.

<a name="glossary:billing-period"><b>Billing Period</b></a>

The time window that an organization receives an invoice for, inclusive of the start date and exclusive of the end date. It is independent of the time of usage and consumption of resources and services.

<a name="glossary:block-pricing"><b>Block Pricing</b></a>

A pricing approach where the cost of a particular resource or service is determined based on predefined quantities or tiers of usage. In these scenarios, the [Pricing Unit](#col:CostAndUsage.PricingUnit) and the corresponding [Pricing Quantity](#col) can be different from the [Consumed Unit](#col) and [Consumed Quantity](#col).

<a name="glossary:cash-based-accounting"><b>Cash-Based Accounting</b></a>

An accounting method used in technology cost management to record costs in the period when charges are invoiced. This approach aligns expenses with billing cycles, independent of when resources are utilized, services are delivered, or entitlements are available for or actually consumed (including unused or expired entitlements).

<a name="glossary:capacity-reservation"><b>Capacity Reservation</b></a>

A capacity reservation is an agreement that secures a dedicated amount of resources or services for a specified period. This ensures the reserved capacity is always available and accessible, even if it's not fully utilized. Customers are typically charged for the reserved capacity, regardless of actual consumption.

<a name="glossary:charge"><b>Charge</b></a>

A row in a FOCUS-compatible cost and usage dataset.

<a name="glossary:chargeperiod"><b>Charge Period</b></a>

The time window for which a charge is effective, inclusive of the start date and exclusive of the end date. The charge period for continuous usage should match the time granularity of the [dataset instance](#term) (e.g., 1 hour for hourly, 1 day for daily). The charge period for a non-usage charge with time boundaries should match the period of eligibility.

<a name="glossary:closed-billing-period"><b>Closed Billing Period</b></a>

A [billing period](#term) with [Billing Period Status](#col) set to "Closed". The period has been financially closed after all anticipated invoices for the period have been [issued](#term:issued-invoice) by designated [invoice issuers](#term) and no additional invoices will be associated with this period. Exceptionally, additional invoices may be associated with a closed billing period if explicitly requested or approved by the customer.

<a name="glossary:cloud-service-provider"><b>Cloud Service Provider (CSP)</b></a>

A company or organization that provides remote access to computing resources, infrastructure, or applications for a fee.

<a name="glossary:commitment"><b>Commitment</b></a>

A customer's agreement to either spend a defined monetary amount or consume a specific quantity of resources or services over a specified [period](#term).

<a name="glossary:commitment-discount"><b>Commitment Discount</b></a>

A publicly available [contract commitment](#term) that provides discounted pricing on preselected SKUs in exchange for a commitment to specific spend or usage goals over a specified [period](#term), based on publicly disclosed standard terms and pricing. Committed spend or usage is evenly distributed across predefined [Contract Commitment Fulfillment Intervals](#col:ContractCommitmentFulfillmentInterval) (e.g., hourly), and unused benefits cannot be carried over to subsequent Intervals. Only one commitment discount may be applied to a single charge at a time, and it may overlap with one or more [negotiated discounts](#term).

This term has been used in the past by FinOps teams managing Public Cloud to refer to specific [contract commitments](#term) (including Reserved Instances, Savings Plans and Committed Use Discounts) offered by cloud providers, and is defined here to maintain consistency with the terms of that subset of [contract commitments](#term).

Commitment discounts are classified with the following designations:

* [Contract Commitment Offer Category](#col): "Public"
* [Contract Commitment Benefit Category](#col): "Discount"
* [Contract Commitment Model](#col): "Continuous"
* Unused benefits cannot be carried over to subsequent Contract Commitment Fulfillment Intervals

<a name="glossary:commitment-discount-flexibility"><b>Commitment Discount Flexibility</b></a>

A feature of [commitment discounts](#term) that may further transform the predetermined amount of usage purchased or consumed based on additional, service-provider-specific requirements.

<a name="glossary:commitment-program"><b>Commitment Program</b></a>

A service-provider offering that allows a customer to enter into a [commitment](#term). Commitment programs include [commitment discounts](#term), [capacity reservations](#term), and other constructs that require advance spend or usage agreements.

<a name="glossary:consumption-currency"><b>Consumption Currency</b></a>

A proprietary [virtual currency](#term) issued by a [service provider](#term) to normalize, measure, and aggregate the consumption of [resources](#term) or [services](#term) within their specific ecosystem.

Unlike a [national currency](#term), a consumption currency acts as an intermediate balance and holds no purchasing power outside of the issuing provider's platform. Pricing models that utilize a consumption currency require a secondary conversion rate to calculate the final financial cost of the usage. Common examples include proprietary platform credits and normalized billing units.

<a name="glossary:contract"><b>Contract</b></a>

A collection of agreed terms between a service provider and a customer.

<a name="glossary:contract-commitment"><b>Contract Commitment</b></a>

A specific term within a [contract](#term) that defines a measurable obligation agreed upon by a provider and a customer, such as a minimum spend or usage over an agreed period of time.

<a name="glossary:contracted-unit-price"><b>Contracted Unit Price</b></a>

The negotiated unit price per [Pricing Unit](#col:CostAndUsage.PricingUnit) for the [SKU Price](#term) identified by the given [SKU Price ID](#col:CostAndUsage.SkuPriceId). Contracted Unit Price reflects [negotiated pricing terms](#term) for the associated [SKU Price](#term) that are independent of any discount-bearing [commitment programs](#term) (e.g., [commitment discount](#term)) being applied to the [charge](#term). It does not reflect any unit price impact dependent on a discount-bearing [commitment program](#term) being applied to the [charge](#term).

<a name="glossary:correction"><b>Correction</b></a>

Any modification (including updates, additions, or omissions) to previously delivered records within a defined [delivery scope](#term) (e.g., temporal grouping such as a [billing period](#term) or non-temporal, logical grouping such as a [contract](#term)).

A correction (lowercase) may consist of one or more simultaneous changes, including updates to or omission of previously delivered records, or the addition of new records that supplement previously delivered data within the affected [delivery scope](#term). This concept applies across all FOCUS datasets.

In contrast to the broader concept of correction (lowercase), the term "Correction" (capitalized) refers to a specific allowed value in the [Charge Class](#col) column in [Cost and Usage](#ds) datasets. It designates [charges](#term) used to correct cost or usage data from a previously [closed billing period](#term).

<a name="glossary:covered-charge"><b>Covered Charge</b></a>

A [charge](#term) whose [Billed Cost](#col:CostAndUsage.BilledCost) is fully or partially absorbed by a corresponding [covering charge](#term). Common examples include usage charges applied against [commitment discounts](#term), or consumption of SaaS offerings drawn from a prepayment, such as marketplace purchases.

<a name="glossary:covering-charge"><b>Covering Charge</b></a>

A purchase [charge](#term) whose cost is applied against one or more [covered charges](#term), offsetting their [Billed Cost](#col:CostAndUsage.BilledCost). Common examples include [commitment discount](#term) purchases, prepayment charges, and marketplace purchases that cover consumption-based usage.

<a name="glossary:credential"><b>Credential</b></a>

The means by which a [principal](#term) is authenticated on an individual request (e.g., API key, access token, session). A credential is distinct from the principal it authenticates, and the same principal may be authenticated by different credentials on different requests. A credential is separate from any published identifier that references it; a credential with no such identifier cannot be represented in a FOCUS dataset.

<a name="glossary:credit"><b>Credit</b></a>

A financial incentive or allowance granted by a service provider unrelated to other past/current/future charges.

<a name="glossary:custom-column"><b>Custom Column</b></a>

A column not defined by FOCUS and included in a [FOCUS dataset](#term). Custom columns are prefixed with `x_` and provide additional context from [native datasets](#term) beyond what is captured in FOCUS columns. See [Dataset Completeness](#attr) for inclusion requirements.

<a name="glossary:dataset-artifact"><b>Dataset Artifact</b></a>

An abbreviated term for [dataset instance artifact](#term).

<a name="glossary:dataset-instance"><b>Dataset Instance</b></a>

A specific implementation of a [FOCUS dataset](#term) provided by a [data generator](#meta). A Data Generator may provide multiple dataset instances of the same [FOCUS dataset](#term), each with different properties such as time granularity or differing custom column inclusions. For example, the same 'FOCUS [Cost and Usage](#ds)' [FOCUS dataset](#term) may be provided at an hourly or daily time granularity by a Data Generator. Each would be a distinct Dataset Instance.

<a name="glossary:dataset-instance-artifact"><b>Dataset Instance Artifact</b></a>

A physical representation of a specific [dataset instance](#term) delivered by a [data generator](#meta).

<a name="glossary:delivery-scope"><b>Delivery Scope</b></a>

A dataset-specific boundary or set of boundaries that determines which records are included in a [dataset artifact](#term:dataset-instance-artifact) delivery. Scopes can be temporal (e.g., a [billing period](#term)) or non-temporal (e.g., a [contract](#term) or other logical grouping), and multiple scopes may be applicable for a single dataset depending on use case or delivery configuration. Scopes determine how Overwrite and Append [dataset artifact](#term) deliveries, as well as corrections, are applied.

<a name="glossary:dimension"><b>Dimension</b></a>

A specification-defined categorical attribute that provides context or categorization to billing data.

<a name="glossary:exclusiveendbound"><b>Exclusive End Bound</b></a>

A [Date/Time Format](#attr) value that is not contained within the ending bound of a time period.

<a name="glossary:finalized-tag"><b>Finalized Tag</b></a>

A tag with one tag value chosen from a set of possible tag values after being processed by a set of service-provider-defined or user-defined rules.

<a name="glossary:finops-cost-and-usage-specification"><b>FinOps Cost and Usage Specification (FOCUS)</b></a>

An open-source specification that defines requirements for billing data.

<a name="glossary:FOCUS-column"><b>FOCUS Column</b></a>

A column defined by FOCUS and included in a [FOCUS dataset](#term). See the Columns section of each dataset for definitions.

<a name="glossary:FOCUS-dataset"><b>FOCUS Dataset</b></a>

A structured collection of columns that conforms to the BCP14 criteria established by FOCUS. All columns included must be defined in the FOCUS Columns section of the specification.

In addition to these standardized columns, [data generators](#meta:DataGenerator) include [custom columns](#term) to capture information from [native datasets](#term) that is not represented by [FOCUS columns](#term). If custom columns introduce record-splitting (i.e., a single original charge results in multiple rows), the data generator is responsible for ensuring that all cost and quantity metrics still meet the aggregation and consistency rules required by the specification.

The collection of datasets are designed to provide billing insight, additional context, metadata, mapping, or enrichment information that enhances the interpretability or completeness. See also: [Native Dataset](#term).

<a name="glossary:FOCUS-dataset-column"><b>FOCUS Dataset Column</b></a>

A column included in a [FOCUS dataset](#term). A FOCUS dataset column is either a [FOCUS column](#term) or a [custom column](#term).

<a name="glossary:foreign-exchange"><b>Foreign Exchange (FX)</b></a>

The conversion of an amount from one currency to another using a currency exchange rate.

<a name="glossary:general-availability"><b>General Availability (GA)</b></a>

The version of FOCUS in which a [FOCUS dataset](#term), or a supporting entity on a preview's scope list, is promoted from [preview](#term) status or initially published without preview status.

<a name="glossary:inclusivestartbound"><b>Inclusive Start Bound</b></a>

A [Date/Time Format](#attr) value that is contained within the beginning bound of a time period.

<a name="glossary:interruptible"><b>Interruptible</b></a>

A category of compute resources that can be paused or terminated by the CSP within certain criteria, often advertised at reduced unit pricing when compared to the equivalent non-interruptible resource.

<a name="glossary:invoice"><b>Invoice</b></a>

A document that summarizes the charges for resources or services consumed by a customer.

<a name="glossary:invoice-issuer"><b>Invoice Issuer</b></a>

An entity responsible for issuing payable [invoices](#term) for the [resources](#term) or [services](#term) consumed. Common examples include [cloud service providers](#term), [managed service providers](#term), or marketplace operators.

<a name="glossary:invoice-reconciliation"><b>Invoice Reconciliation</b></a>

The process of verifying that the costs, quantities, and applied adjustments on an [invoice](#term) are equal to the underlying usage records and contracted rates for a specific [billing period](#term).

In the context of FOCUS, this process ensures consistency by reconciling cost and usage data across the invoice, the [Invoice Detail](#ds) dataset, and the [Cost and Usage](#ds) dataset to identify and resolve any discrepancies.

<a name="glossary:issued-invoice"><b>Issued Invoice</b></a>

An [invoice](#term) that has been formally [reconciled](#term:invoice-reconciliation) and issued by the designated [invoice issuer](#term) ([Invoice Issue Status](#col) set to "Issued"). Once issued, the invoice becomes the authoritative financial document and is considered finalized. The financial data presented on the invoice is not expected to change.

<a name="glossary:json"><b>JSON</b></a>

A common acronym for JavaScript Object Notation, a data format codified in [ECMA-404](https://ecma-international.org/wp-content/uploads/ECMA-404_2nd_edition_december_2017.pdf) as a standard for human-readable, serializable data objects. This data format is used in FOCUS to communicate multiple pieces of information about a charge (tags, properties, etc.) in a single column.

<a name="glossary:list-unit-price"><b>List Unit Price</b></a>

The service-provider-suggested unit price per [Pricing Unit](#col:CostAndUsage.PricingUnit) for the [SKU Price](#term) identified by the given [SKU Price ID](#col:CostAndUsage.SkuPriceId). List Unit Price does not reflect [negotiated pricing terms](#term) for the associated [SKU Price](#term) or any unit price impact dependent on a discount-bearing [commitment program](#term) (e.g., [commitment discount](#term)) being applied to the [charge](#term).

<a name="glossary:managed-service-provider"><b>Managed Service Provider (MSP)</b></a>

A company or organization that provides outsourced management and support of a range of IT services, such as network infrastructure, cybersecurity, cloud computing, and more.

<a name="glossary:metric"><b>Metric</b></a>

A FOCUS-defined column that provides numeric values, allowing for aggregation operations such as arithmetic operations (sum, multiplication, averaging etc.) and statistical operations.

<a name="glossary:national-currency"><b>National Currency</b></a>

A government-issued currency (e.g., US dollars, Euros).

<a name="glossary:native-dataset"><b>Native Dataset</b></a>

A dataset provided by a [*data generator*](#metadata.datagenerator) in a format other than FOCUS. For [service providers](#term), this typically refers to their proprietary data exports (e.g., billing exports, contract details, or other FinOps-related datasets). For FinOps tool vendors, this refers to any non-FOCUS dataset they offer to [practitioners](#term). See also: [FOCUS Dataset](#term).

<a name="glossary:negotiated-discount"><b>Negotiated Discount</b></a>

A privately agreed [contract commitment](#term) that provides discounted pricing in exchange for a commitment to specific spend or usage goals over a specified [period](#term), with terms and pricing specifically modified from standard. Multiple negotiated discounts may be applied to a single charge at a time, and they may overlap with a [commitment discount](#term).

Negotiated discounts are classified with the following designations:

* [Contract Commitment Offer Category](#col): "Negotiated"
* [Contract Commitment Benefit Category](#col): "Discount"

<a name="glossary:negotiated-fx-pricing-terms"><b>Negotiated FX Pricing Terms</b></a>

[Negotiated pricing terms](#term) that affect the [foreign exchange](#term) conversion between the applicable record's [Pricing Currency](#col:CostAndUsage.PricingCurrency) and [Billing Currency](#col:CostAndUsage.BillingCurrency).

<a name="glossary:negotiated-non-fx-pricing-terms"><b>Negotiated Non-FX Pricing Terms</b></a>

[Negotiated pricing terms](#term) that do not affect the [foreign exchange](#term) conversion between the applicable record's [Pricing Currency](#col:CostAndUsage.PricingCurrency) and [Billing Currency](#col:CostAndUsage.BillingCurrency).

<a name="glossary:negotiated-pricing-terms"><b>Negotiated Pricing Terms</b></a>

Privately agreed [terms](#term) between a service provider and a customer that modify pricing from the service-provider-suggested pricing. Negotiated pricing terms consist of [negotiated non-FX pricing terms](#term) (e.g., negotiated unit prices, negotiated tiered pricing configurations) and [negotiated FX pricing terms](#term) (e.g., negotiated currency exchange rates).

<a name="glossary:on-demand"><b>On-Demand</b></a>

A service that is available and provided immediately or as needed, without requiring a pre-scheduled appointment or prior arrangement. In cloud computing, virtual machines can be created and terminated as needed, i.e., on demand.

<a name="glossary:open-billing-period"><b>Open Billing Period</b></a>

A [billing period](#term) with [Billing Period Status](#col) set to "Open". Billing activities are ongoing, and the period remains subject to updates until formally closed.

<a name="glossary:operating-model"><b>Operating Model</b></a>

The collective set of capabilities, business concepts, and data constructs underlying a FOCUS-compliant dataset. It encompasses features and metadata enrichments supported across participating entities (e.g., [service providers](#term), host providers, [invoice issuers](#term), and [*data generators*](#metadata.datagenerator)), reflecting the verifiable state of these elements at the time of dataset creation.

<a name="glossary:origin-charge"><b>Origin Charge</b></a>

The [charge](#term) that existed prior to an operation. This is used in the context of [Data Generator-Calculated Split Cost Allocation](#supportedfeatures.datagenerator-calculatedsplitcostallocation) to identify the charge that existed prior to the application of Data Generator-Calculated Split Cost Allocation to produce [allocated charges](#term).

<a name="glossary:pascalcase"><b>Pascal Case</b></a>

Pascal Case (PascalCase, also known as UpperCamelCase) is a format for identifiers which contain one or more words meaning the words are concatenated together with no delimiter and the first letter of each word is capitalized.

<a name="glossary:period"><b>Period</b></a>

A time window, with a specifically defined start and end date/time.

<a name="glossary:potato"><b>Potato</b></a>

A long and often painful conversation had by the FOCUS contributors. Sometimes the name of a thing that we could not yet name. No starchy root vegetables were harmed during the production of this specification. We thank potato for its contribution in the creation of this specification.

<a name="glossary:practitioner"><b>Practitioner</b></a>

An individual who performs FinOps within an organization to maximize the business value of using cloud and cloud-like services.

<a name="glossary:preview"><b>Preview</b></a>

A status for a [FOCUS dataset](#term) that is published in a version of FOCUS so implementers can build it and report what they find, and that may change in the next version without a deprecation notice. See [Preview](#introduction.preview) and [General Availability (GA)](#term).

<a name="glossary:price-list"><b>Price List</b></a>

A comprehensive list of prices offered by a service provider.

<a name="glossary:principal"><b>Principal</b></a>

An entity defined in an identity and access management model (e.g., user, service account) to which access to [resources](#term) or [services](#term) is granted. A principal is distinct from the credential (e.g., API key, access token) presented with an individual request, and from the organizational container (e.g., project, workspace) within which the request runs. The same principal may be associated with multiple credentials.

<a name="glossary:prompt-cache"><b>Prompt Cache</b></a>

A storage mechanism that allows a generative AI workload to reuse previously processed input content across requests to an [AI model](#term). Service providers may meter cache reads, cache writes, and cache retention differently.

<a name="glossary:service-provider"><b>Service Provider</b></a>

An entity that provides the [resources](#term) or [services](#term) available for usage or purchase.

<a name="glossary:refund"><b>Refund</b></a>

A return of funds that have previously been charged.

<a name="glossary:requester"><b>Requester</b></a>

An entity defined in an identity and access management model on whose behalf a request is initiated, resulting in a [charge](#term). A [service provider](#term) commonly represents a requester at more than one level, such as the [principal](#term) to which access to [resources](#term) or [services](#term) is granted and the [credential](#term) presented on the request. A requester is distinct from the party that benefits from the usage or purchase, which a FOCUS dataset does not identify.

<a name="glossary:resource"><b>Resource</b></a>

A unique component that incurs a charge.

<a name="glossary:row"><b>Row</b></a>

A row in a FOCUS-compatible cost and usage dataset.

<a name="glossary:service"><b>Service</b></a>

An offering that can be purchased from a service provider, and can include many types of usage or other charges; e.g., a cloud database service may include compute, storage, and networking charges.

<a name="glossary:sku"><b>SKU</b></a>

A construct composed of the common properties of a product offering associated with one or many SKU Prices.

<a name="glossary:sku-price"><b>SKU Price</b></a>

A pricing construct that encompasses [SKU](#term) properties (e.g., functionality and technical specifications) and core stable pricing details for a particular [SKU](#term). It excludes dynamic or negotiable pricing elements such as unit price amounts, currency, [foreign exchange](#term) rates, effective dates, contract or account identifiers, and negotiated discounts. However, modifications to the pricing structure itself (such as a negotiated tier configuration) are included.

<a name="glossary:split-cost-allocation"><b>Split Cost Allocation</b></a>

A mechanism that splits a single [origin charge](#term) into multiple [allocated charges](#term) to distribute cost and usage across [resources](#term) at a more granular level, using a defined [allocated method](#term).

<a name="glossary:sub-account"><b>Sub Account</b></a>

A sub account is an optional service-provider-supported construct for organizing resources and/or services connected to a billing account. Sub accounts must be associated with a billing account as they do not receive invoices.

<a name="glossary:tag"><b>Tag</b></a>

A metadata label assigned to a resource to provide information about it or to categorize it for organizational and management purposes.

<a name="glossary:tag-scheme"><b>Tag Scheme</b></a>

A distinct framework for assigning metadata to charges, resources, or other assets. Different metadata types within a single provider (e.g., "tags" vs. "labels") are considered separate schemes. They can be user-defined (i.e., allowing user input) or provider-defined (i.e., controlled by the service provider).

<a name="glossary:tag-source"><b>Tag Source</b></a>

A Resource or Service-Provider-defined construct for grouping resources and/or other Service-Provider-defined construct that a Tag can be assigned to.

<a name="glossary:term"><b>Term</b></a>

An agreement specified on a [contract](#term) or [invoice](#term).

<a name="glossary:token"><b>Token</b></a>

A unit of measure representing a discrete quantity of content processed by an [AI model](#term). The amount of content a single token represents is determined by the model, so token counts are not directly comparable across models. Distinct from a token issued as a [virtual currency](#term), which denominates value.

<a name="glossary:unit-pricing"><b>Unit Pricing</b></a>

A billing concept where the cost of a [charge](#term) is deterministically derived as the product of a unit price (defined per [SKU Price](#term)) and the corresponding [Pricing Quantity](#col), representing purchased or consumed volume of a [SKU](#term).

<a name="glossary:virtual-currency"><b>Virtual Currency</b></a>

A digital representation of value that is independent of government regulation or central banks (e.g., cryptocurrency, digital credits). Distinct from a [token](#term) as a unit of measure for content processed by an [AI model](#term).
