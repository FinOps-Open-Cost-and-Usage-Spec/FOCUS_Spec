# Glossary

<a name="glossary:adjustment"><b>Adjustment</b></a>

A charge representing a modification to billing data to account for certain events or circumstances not previously captured, or captured incorrectly. Examples include billing errors, service disruptions, or pricing changes.

<a name="glossary:amortization"><b>Amortization</b></a>

The distribution of upfront costs over time to accurately reflect the consumption or benefit derived from the associated resources or services. Amortization is valuable when the commitment period (time duration of the cost) extends beyond the granularity of the source report.

<a name="glossary:availability-zone"><b>Availability Zone</b></a>

A collection of geographically separated locations containing a data center or cluster of data centers. Each availability zone (AZ) should have its own power, cooling, and networking, to provide redundancy and fault tolerance.

<a name="glossary:billed-cost"><b>Billed Cost</b></a>

A charge that serves as the basis for invoicing. It includes the total amount of fees and discounts, signifying a monetary obligation. Valuable when reconciling cash outlay with incurred expenses is required, such as cost allocation, budgeting, and invoice reconciliation.

<a name="glossary:billing-account"><b>Billing Account</b></a>

A container for resources and/or services that are billed together in an invoice. A billing account may have sub accounts, all of whose costs are consolidated and invoiced to the billing account.

<a name="glossary:billing-currency"><b>Billing Currency</b></a>

An identifier that represents the currency that a charge for resources and/or services was billed in.

<a name="glossary:billing-period"><b>Billing Period</b></a>

The time window that an organization receives an invoice for, inclusive of the start date and exclusive of the end date. It is independent of the time of usage and consumption of resources and services.

<a name="glossary:block-pricing"><b>Block Pricing</b></a>

A pricing approach where the cost of a particular resource or service is determined based on predefined quantities or tiers of usage. In these scenarios, the Pricing Unit and the corresponding Pricing Quantity can be different from the Consumed Unit and Consumed Quantity.

<a name="glossary:build-up-commitment"><b>Build-Up Commitment</b></a>

A commitment model in which a customer gradually contributes ("builds up") toward a predefined commitment amount over a specified [*term*](#glossary:term) (e.g., one year, two years). This commitment may be structured either as spend-based, defined by monetary value, or usage-based, defined by the quantity of resources or services. The total committed amount is typically distributed evenly across defined [*commitment intervals*](#glossary:commitment-interval) (such as monthly or yearly), with contributions tracked accordingly. If the target for a given interval is not met, a true-up charge may apply. Commitments are generally made in exchange for commercial benefits, such as discounted pricing. Build-Up Commitments are typically offered as [*Negotiated Build-Up Commitments*](#glossary:negotiated-build-up-commitment). While [*Non-Negotiated Build-Up Commitments*](#glossary:non-negotiated-build-up-commitment) also exist, though they are less common.

<a name="glossary:burn-down-commitment"><b>Burn-Down Commitment</b></a>

A commitment model in which a customer prepays (either All-Upfront, No-Upfront, or Partial Upfront) and gradually consumes ("burns down") a predefined commitment amount over a specified [*term*](#glossary:term) (e.g., one or two years). This commitment may be structured either as spend-based, defined by monetary value, or usage-based, defined by the quantity of resources or services. The total committed amount is typically distributed evenly across defined [*commitment intervals*](#glossary:commitment-interval) (such as hourly, monthly, yearly, or custom), with consumption tracked accordingly. Any unused portion may expire at the end of a *commitment interval* and cannot be carried over. Commitments are generally made in exchange for commercial benefits, such as discounted pricing, and may include provider obligations related to resource availability or service levels. Burn-Down Commitments may be offered as [*Negotiated Burn-Down Commitments*](#glossary:negotiated-burn-down-commitment)] or [*Non-Negotiated Burn-Down Commitments*](#glossary:non-negotiated-burn-down-commitment).

<a name="glossary:capacity-reservation"><b>Capacity Reservation</b></a>

A capacity reservation is an agreement that secures a dedicated amount of resources or services for a specified period. This ensures the reserved capacity is always available and accessible, even if it's not fully utilized. Customers are typically charged for the reserved capacity, regardless of actual consumption.

<a name="glossary:charge"><b>Charge</b></a>

A row in a FOCUS-compatible cost and usage dataset.

<a name="glossary:chargeperiod"><b>Charge Period</b></a>

The time window for which a charge is effective, inclusive of the start date and exclusive of the end date. The charge period for continuous usage should match the time granularity of the dataset (e.g., 1 hour for hourly, 1 day for daily). The charge period for a non-usage charge with time boundaries should match the duration of eligibility.

<a name="glossary:cloud-service-provider"><b>Cloud Service Provider (CSP)</b></a>

A company or organization that provides remote access to computing resources, infrastructure, or applications for a fee.

<a name="glossary:commitment"><b>Commitment</b></a>

A customer's agreement to either spend a defined monetary amount or use a specific quantity of resources or services over a specified [*term*](#glossary:term). Commitments are generally made in exchange for commercial benefits, such as discounted pricing, and may include provider obligations related to resource availability or service levels. Commitment models vary in structure and mechanics, with [*Burn-Down Commitment*](#glossary:burn-down-commitment) and [*Build-Up Commitment*](#glossary:build-up-commitment) being the core types.

<a name="glossary:commitment-discount"><b>Commitment Discount</b></a>

A billing discount model that offers reduced rates on preselected SKUs in exchange for an obligated usage or spend amount over a predefined term.  Commitment discount purchases, made upfront and/or with recurring monthly payments are amortized evenly across predefined charge periods (i.e., hourly), and unused amounts cannot be carried over to subsequent charge periods. Commitment discounts are publicly available to customers without special contract arrangements.

<a name="glossary:commitment-discount-flexibility"><b>Commitment Discount Flexibility</b></a>

A feature of [*commitment discounts*](#glossary:commitment-discount) that may further transform the predetermined amount of usage purchased or consumed based on additional, provider-specific requirements.

<a name="glossary:commitment-interval"><b>Commitment Interval</b></a>

A discrete unit of time used to measure and track consumption or contribution across various commitment models. Common examples include hourly, monthly, or yearly, and custom intervals may also apply.

<a name="glossary:contracted-unit-price"><b>Contracted Unit Price</b></a>

The agreed-upon unit price for a single [Pricing Unit](#pricingunit) of the associated SKU, inclusive of negotiated discounts, if present, and exclusive of any other discounts. This price is denominated in the [Billing Currency](#glossary:billing-currency).

<a name="glossary:correction"><b>Correction</b></a>

A charge to correct cost or usage data in a previously invoiced [*billing period*](#glossary:billing-period).

<a name="glossary:credit"><b>Credit</b></a>

A financial incentive or allowance granted by a provider unrelated to other past/current/future charges.

<a name="glossary:dimension"><b>Dimension</b></a>

A specification-defined categorical attribute that provides context or categorization to billing data.

<a name="glossary:effective-cost"><b>Effective Cost</b></a>

The amortized cost of the charge after applying all reduced rates, discounts, and the applicable portion of relevant, prepaid purchases (one-time or recurring) that covered this charge.

<a name="glossary:exclusiveendbound"><b>Exclusive End Bound</b></a>

A Date/Time Format value that is not contained within the ending bound of a time period.

<a name="glossary:finalized-tag"><b>Finalized Tag</b></a>

A tag with one tag value chosen from a set of possible tag values after being processed by a set of provider-defined or user-defined rules.

<a name="glossary:finops-cost-and-usage-specification"><b>FinOps Cost and Usage Specification (FOCUS)</b></a>

An open-source specification that defines requirements for billing data.

<a name="glossary:FOCUS-dataset"><b>FOCUS Dataset</b></a>

A structured collection of cost and usage data that meets the [BCP14](https://tools.ietf.org/html/bcp14) criteria defined by FOCUS. In addition to FOCUS columns, the dataset should include custom provider columns (prefixed with `x_`) when these columns provide additional information not captured by the existing FOCUS columns. If introducing a custom column could result in splitting original charge records into multiple entries, the data generator is responsible for ensuring that the FOCUS dataset fully conforms to all aggregation-related requirements for metric columns, particularly those concerning costs and quantities.

<a name="glossary:inclusivestartbound"><b>Inclusive Start Bound</b></a>

A Date/Time Format value that is contained within the beginning bound of a time period.

<a name="glossary:interruptible"><b>Interruptible</b></a>

A category of compute resources that can be paused or terminated by the CSP within certain criteria, often advertised at reduced unit pricing when compared to the equivalent non-interruptible resource.

<a name="glossary:list-unit-price"><b>List Unit Price</b></a>

The suggested provider-published unit price for a single [Pricing Unit](#pricingunit) of the associated [SKU](#glossary:sku), exclusive of any discounts. This price is denominated in the [Billing Currency](#glossary:billing-currency).

<a name="glossary:managed-service-provider"><b>Managed Service Provider (MSP)</b></a>

A company or organization that provides outsourced management and support of a range of IT services, such as network infrastructure, cybersecurity, cloud computing, and more.

<a name="glossary:metric"><b>Metric</b></a>

A FOCUS-defined column that provides numeric values, allowing for aggregation operations such as arithmetic operations (sum, multiplication, averaging etc.) and statistical operations.

<a name="glossary:national-currency"><b>National Currency</b></a>

A government-issued currency (e.g., US dollars, Euros).

<a name="glossary:negotiated-build-up-commitment"><b>Negotiated Build-Up Commitment</b></a>

A variant of the [*Build-Up Commitment*](#glossary:build-up-commitment) model in which the terms and conditions, such as spend or usage targets (structured either as spend-based, defined by monetary value, or usage-based, defined by the quantity of resources or services), custom pricing, duration, contribution tracking, true-up mechanisms, and provider obligations, are explicitly negotiated between the customer and the provider. This variant retains all core characteristics of the *Build-Up Commitment*, with added flexibility to align with specific business needs. Negotiated Build-Up Commitments are typically used by large enterprises or strategic partners.

<a name="glossary:negotiated-burn-down-commitment"><b>Negotiated Burn-Down Commitment</b></a>

A variant of the [*Burn-Down Commitment*](#glossary:burn-down-commitment) model in which the terms and conditions, such as monetary amount, resources or services quantity, custom pricing, duration, and consumption tracking, and provider obligations, are explicitly negotiated between the customer and the provider. This variant retains all core characteristics of the *Burn-Down Commitment*, with added flexibility to align with specific business needs.

<a name="glossary:non-negotiated-build-up-commitment"><b>Non-Negotiated Build-Up Commitment</b></a>

A less common variant of the [*Build-Up Commitment*](#glossary:build-up-commitment) model offered under standardized terms and conditions, such as commitment amount (structured either as spend-based, defined by monetary value, or usage-based, defined by the quantity of resources or services), pricing, duration, contribution tracking, true-up mechanisms, and provider obligations. This variant retains all core characteristics of the *Build-Up Commitment* but is not subject to individual negotiation.

<a name="glossary:non-negotiated-burn-down-commitment"><b>Non-Negotiated Burn-Down Commitment</b></a>

A variant of the [*Burn-Down Commitment*](#glossary:burn-down-commitment) model offered under standardized terms and conditions, such as commitment amount (structured either as spend-based, defined by monetary value, or usage-based, defined by the quantity of resources or services), pricing, duration, consumption tracking, and provider obligations. This variant retains all core characteristics of the *Burn-Down Commitment* but is not subject to individual negotiation. Non-Negotiated Burn-Down Commitments are typically available through public pricing models or self-service platforms.

<a name="glossary:on-demand"><b>On-Demand</b></a>

A term that describes a service that is available and provided immediately or as needed, without requiring a pre-scheduled appointment or prior arrangement. In cloud computing, virtual machines can be created and terminated as needed, i.e., on demand.

<a name="glossary:pascalcase"><b>Pascal Case</b></a>

Pascal Case (PascalCase, also known as UpperCamelCase) is a format for identifiers which contain one or more words meaning the words are concatenated together with no delimiter and the first letter of each word is capitalized.

<a name="glossary:potato"><b>Potato</b></a>

A long and often painful conversation had by the FOCUS contributors. Sometimes the name of a thing that we could not yet name. No starchy root vegetables were harmed during the production of this specification. We thank potato for its contribution in the creation of this specification.

<a name="glossary:practitioner"><b>Practitioner</b></a>

An individual who performs FinOps within an organization to maximize the business value of using cloud and cloud-like services.

<a name="glossary:price-list"><b>Price List</b></a>

A comprehensive list of prices offered by a provider.

<a name="glossary:provider"><b>Provider</b></a>

An entity that made internal or 3rd party resources and/or services available for purchase.

<a name="glossary:refund"><b>Refund</b></a>

A return of funds that have previously been charged.

<a name="glossary:resource"><b>Resource</b></a>

A unique component that incurs a charge.

<a name="glossary:row"><b>Row</b></a>

A row in a FOCUS-compatible cost and usage dataset.

<a name="glossary:service"><b>Service</b></a>

An offering that can be purchased from a provider, and can include many types of usage or other charges; eg., a cloud database service may include compute, storage, and networking charges.

<a name="glossary:sku"><b>SKU</b></a>

A construct composed of the common properties of a product offering associated with one or many SKU Prices.

<a name="glossary:sku-price"><b>SKU Price</b></a>

A pricing construct that encompasses SKU properties (e.g., functionality and technical specifications), along with core stable pricing details for a particular SKU, while excluding dynamic or negotiable pricing elements such as unit price amounts, currency (and related exchange rates), temporal validity (e.g., effective dates), and contract- or negotiation-specific factors (e.g., contract or account identifiers, and negotiable discounts).

<a name="glossary:sub-account"><b>Sub Account</b></a>

A sub account is an optional provider-supported construct for organizing resources and/or services connected to a billing account. Sub accounts must be associated with a billing account as they do not receive invoices.

<a name="glossary:tag"><b>Tag</b></a>

A metadata label assigned to a resource to provide information about it or to categorize it for organizational and management purposes.

<a name="glossary:tag-source"><b>Tag Source</b></a>

A Resource or Provider-defined construct for grouping resources and/or other Provider-defined construct that a Tag can be assigned to.

<a name="glossary:term"><b>Term</b></a>

A duration of a contractual agreement like with a [*commitment discount*](#glossary:commitment-discount) or [*negotiated discount*](#glossary:negotiated-discount).

<a name="glossary:virtual-currency"><b>Virtual Currency</b></a>

A proprietary currency (e.g., credits, tokens) issued by providers and independent of government regulation.
