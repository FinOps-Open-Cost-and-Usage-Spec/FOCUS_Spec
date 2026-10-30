# Grouping Constructs for Resources or Services

Service Providers natively support various constructs for grouping [resources](#term) or [services](#term). These grouping constructs are often used to mimic organizational structures, technical architectures, cost attribution/allocation and access management boundaries, or other customer-specific structures based on requirements.

Service Providers may support multiple levels of resource or service grouping mechanisms. FOCUS supports two distinct levels of groupings that are commonly needed for FinOps capabilities like chargeback, invoice reconciliation and cost allocation.

* [Billing account](#term): A mandatory container for [resources](#term) or [services](#term) that are billed together in an invoice. [Billing accounts](#term) are commonly used for scenarios like grouping based on organizational constructs, invoice reconciliation and cost allocation strategies.
* [Sub account](#term): An optional service-provider-supported construct for organizing [resources](#term) and [services](#term) connected to a [billing account](#term). [Sub accounts](#term) are commonly used for scenarios like grouping based on organizational constructs, access management needs and cost allocation strategies. [Sub accounts](#term) must be associated with a [billing account](#term) as they do not receive invoices.

The table below highlights key properties of the two grouping constructs supported by FOCUS.

| Property             | Billing account | Sub account                |
|:---------------------|:----------------|:---------------------------|
| Requirement level    | Mandatory       | Optional                   |
| Receives an invoice? | Yes             | No                         |
| Invoiced at          | Self            | Associated billing account |
| Examples             | AWS: Management Account<sup>*</sup><br>GCP: Billing Account<br>Azure MCA: Billing Profile<br>Snowflake: Organizational Account | AWS: Member Account<br>GCP: Project<br>Azure MCA: Subscription<br>Snowflake: Account |

<sup>*</sup> For organizations that have multiple AWS Member Accounts within an AWS Organization, consolidated billing is enabled by default and invoices are received at Management Account level. A Member Account can be removed from AWS consolidated billing whereby the removed account receives independent invoices and is responsible for payments.
