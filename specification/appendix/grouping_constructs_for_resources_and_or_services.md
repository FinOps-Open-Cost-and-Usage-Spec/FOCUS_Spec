# Grouping constructs for resources and/or services

Providers natively support various constructs for grouping resources and/or services. These grouping constructs are often used to mimic organizational structures, application architectures, cost attribution/allocation and access management boundaries or other (hierarchical or non-hierarchical) structures based on customer requirements.

Providers may support multiple levels of resource and/or service groupings. FOCUS supports two distinct levels of groupings based on common FinOps needs.

* Billing account: A mandatory container for resources and/or services that are billed together in an invoice. Common scenarios for using billing accounts include grouping based on organizational constructs and hierarchy-based cost allocation approach.
* Sub account: an optional provider-supported construct for organizing resources and services connected to a billing account. Some common scenarios for using sub accounts include grouping based on organizational constructs and access management boundaries. Sub accounts must be associated with a billing account as they do not receive invoices.

The table below highlights key properties of the two grouping constructs supported by FOCUS.

| Property             | Billing account | Sub account                |
|:---------------------|:----------------|:---------------------------|
| Requirement level    | Mandatory       | Optional                   |
| Receives an invoice? | Yes             | No                         |
| Invoiced at          | Self            | Associated billing account |
| Examples             | AWS: Management Account<br>GCP: Billing Account<br>Azure MCA: Billing Profile<br>Snowflake: Organizational Account | AWS: Account<br>GCP: Project<br>Azure MCA: Resource group<br>Snowflake: Account |
