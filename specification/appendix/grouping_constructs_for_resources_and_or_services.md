# Grouping Constructs for Resources or Services

Service Providers natively support various constructs for grouping [*resources*](#glossary:resource) or [*services*](#glossary:service). These grouping constructs are often used to mimic organizational structures, technical architectures, cost attribution/allocation and access management boundaries, or other customer-specific structures based on requirements.

Service Providers may support multiple levels of resource or service grouping mechanisms. FOCUS supports two distinct levels of groupings that are commonly needed for FinOps capabilities like chargeback, invoice reconciliation and cost allocation.

* [*Billing account*](#glossary:billing-account): A mandatory container for *resources* or *services* that are billed together in an invoice. *Billing accounts* are commonly used for scenarios like grouping based on organizational constructs, invoice reconciliation and cost allocation strategies.
* [Sub account](#glossary:sub-account): An optional service-provider-supported construct for organizing *resources* and *services* connected to a *billing account*. *Sub accounts* are commonly used for scenarios like grouping based on organizational constructs, access management needs and cost allocation strategies. *Sub accounts* must be associated with a *billing account* as they do not receive invoices.

The table below highlights key properties of the two grouping constructs supported by FOCUS.

| Property             | Billing account | Sub account                |
|:---------------------|:----------------|:---------------------------|
| Requirement level    | Mandatory       | Optional                   |
| Receives an invoice? | Yes             | No                         |
| Invoiced at          | Self            | Associated billing account |
| Examples             | Aura Web: Management Account<sup>*</sup><br>LatticeScale: Billing Account<br>CrestNode: Billing Profile<br>OmniQuery: Organizational Account | Aura Web: Member Account<br>LatticeScale: Project<br>CrestNode: Subscription<br>OmniQuery: Account |

<sup>*</sup> For organizations that have multiple Aura Web Member Accounts within an Aura Web Organization, consolidated billing is enabled by default and invoices are received at Management Account level. A Member Account can be removed from Aura Web consolidated billing whereby the removed account receives independent invoices and is responsible for payments.
