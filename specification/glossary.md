# Glossary

*This section is non-normative.*

**Adjustment**

A charge representing a modification to billing data to account for certain events or circumstances not previously captured, or captured incorrectly. Examples include: billing errors, service disruptions, or pricing changes.

**Amortization**

The distribution of upfront costs over time to accurately reflect the consumption or benefit derived from the associated resources or services. Amortization is valuable when the commitment period (time duration of the cost) extends beyond the granularity of the source report.

**Availability Zone**

Geograhically separated locations containing a data center or cluster of data centers. Each availability zone (AZ) should have its own power, cooling, and networking, to provide redundancy and fault tolerance.

**Billed Cost**

A charge that serves as the basis for invoicing. It includes the total amount of fees and discounts, signifying a monetary obligation. Valuable when reconciling cash outlay with incurred expenses is required, such as cost allocation, budgeting, and invoice reconciliation.

**Billing Account**

A container for resources and/or services that are billed together in an invoice. A billing account may have sub-accounts, all of whose costs are consolidated and invoiced to the billing account.

**Billing Currency**

An identifier that represents the currency that a charge for resources and/or services was billed in.

**Billing Period**

The time window that an organization receives an invoice for, inclusive of the start date and exclusive of the end date. It is independent of the time of usage and consumption of resources and services.

**Block Pricing**

 A pricing approach where the cost of a particular resource or service is determined based on predefined quantities or tiers of usage. In these scenarios, the Pricing Unit and the corresponding Pricing Quantity can be different from the Usage Unit and Usage Quantity.

**Charge**

A row in a FOCUS compatible cost and usage dataset.

**Commitment**

A customer's agreement to consume a specific quantity of a service or resource over a defined period, usually also creating a financial commitment throughout the entirety of the commitment period. Some commitments also hold Providers to certain assurance levels of resource availability.

**Commitment-Based Discount**

Also known as Commitment Discount, this is a pricing strategy or incentive offered by a service provider to encourage customers to commit to a certain level of usage or spend, over a specified period. Offerings vary in specificity of commitment, penalties for underutilization, and possible remedies.

**Cloud Service Provider (CSP)**

A company or organization that provides remote access to computing resources, infrastructure, or applications for a fee.

**Dimension**

A specification-defined categorical attribute that provides context or categorization to billing data.

**Effective Cost**

A measure of the true cost of a service, inclusive of all reduced rates, discounts, and impacts of amortization.

**Finalized Tag**

A tag with one tag value chosen from a set of possible tag values after being processed by a set of provider-defined or user-defined rules.

**FinOps Cost and Usage Specification (FOCUS)**

An open source specification that defines requirements for billing data.

**Interruptible**

A category of compute resources that can be paused or terminated by the CSP within certain criteria, often advertised at reduced unit pricing when compared to the equivalent non-interruptible resource.

**List Unit Price**

The suggested provider-published unit price for a single [Pricing Unit](#pricingunit) of the associated SKU, exclusive of any discounts. This price is denominated in the [Billing Currency](#glossary:billingcurrency).

**Metric**

A FOCUS defined column that provides numeric values, allowing for aggregation operations such as arithmetic operations (sum, multiplication, averaging etc.) and statistical operations.

**Managed Service Provider (MSP)**

A company or organization that provides outsourced management and support of a range of IT services, such as network infrastructure, cybersecurity, cloud computing, and more.

**On-Demand**

A term that describes a service that is available and provided immediately or as needed, without requiring a pre-scheduled appointment or prior arrangement. In Cloud Computing, virtual machines can be created and terminated as needed, i.e. on demand.

**Practitioner**

An individual who performs FinOps within an organization to maximize the business value of using cloud and cloud-like services.

**Provider**

An entity that made internal or 3rd party resources and/or services available for purchase.

**Price List**

A comprehensive list of prices for offerings from a CSP, published by the CSP.

**Resource**

A provisionable infrastructure component that is available to a customer in a cloud environement e.g. virtual machine, storage volume etc.

**Row**

A row in a FOCUS compatible cost and usage dataset.

**Service**

An offering that can be purchased from a provider, and can include many types of usage or other charges; eg., a cloud database service may include compute, storage, and networking charges.

**SKU**

A construct composed of the common properties of a product offering associated with one or many SKU Prices.

**SKU Price**

The unit price used to calculate a charge. Any SKU Price can only be associated to one SKU.

**Sub Account**

A sub account is an optional provider-supported construct for organizing resources and/or services connected to a billing account. Sub accounts are commonly used for scenarios like grouping based on organizational constructs, access management needs and cost allocation strategies. Sub accounts must be associated with a billing account as they do not receive invoices.

**Tag**

A metadata label assigned to a resource to provide information about it or to categorize it for organizational and management purposes.

**Tag Source**

A Resource or Provider-defined construct for grouping resources and/or other Provider-defined construct that a Tag can be assigned to.
