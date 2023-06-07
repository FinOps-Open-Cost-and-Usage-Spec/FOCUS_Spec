# Grouping constructs for resources and/or services

## Example provider mappings

The table below contains providers' resource and/or service grouping constructs and points out how those map to billing accounts and sub accounts. Billing accounts, sub accounts and resources are part of the FOCUS specification v0.5 scope.

| Provider    | Level 1                        | Level 2                     | Level 3                    | Level 4             | Level 5                    | Level 6  |
|:------------|:-------------------------------|:----------------------------|:---------------------------|:--------------------|:---------------------------|:---------|
| AWS         | Management Account<sup>1</sup> | Organization unit           | Member Account<sup>2</sup> | Resource Group      | Resource                   |          |
| GCP         | Organization                   | Billing Account<sup>1</sup> | Folder                     | Project<sup>2</sup> | Resource                   |          |
| MS EA       | Billing Account<sup>1</sup>    | Department                  | Account                    | Subscription        | Resource group<sup>2</sup> | Resource |
| MS MCA      | Billing Account                | Billing profile<sup>1</sup> | Invoice section            | Subscription        | Resource group<sup>2</sup> | Resource |
| MS PAYG     | Billing Account                | Subscription<sup>1</sup>    | Resource group<sup>2</sup> | Resource            |                            |          |
| MS Internal | Subscription<sup>1</sup>       | Resource group<sup>2</sup>  | Resource                   |                     |                            |          |

<sup>1</sup> invoice scope, mapped to billing account (scope of FOCUS spec v0.5)<br>
<sup>2</sup> mapped to sub account (scope of FOCUS spec v0.5)

### Documentation

- AWS:
  - [AWS Organizations terminology and concepts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html)

- GCP:
  - [Resource hierarchy | Resource Manager Documentation | Google Cloud](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#resource-hierarchy-detail)
  - [Guide to Cloud Billing Resource Organization & Access Management](https://cloud.google.com/billing/docs/onboarding-checklist#resource_hierarchy)

- Microsoft:
  - [Organize your resources with management groups - Azure Governance](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview)
  - [View your billing accounts in Azure portal - Microsoft Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/view-all-accounts)

## Discussion / Scratch space

- Use provider terminology - or customers will get confused
  - However, we need a way for users to be able to see a normalized csolumn with this level of information (can't just be n number of vendor columns that a consumer has to look at)

- How about if we start with a definition:
  - Logical grouping of resources
  - May contain access restrictions

- Billing Account (L1), Account Group (L2), Account (L3)
  - Will there be confusion about Account vs Billing Account
  - What about "Usage Account" for L3
  - Billing account could say "grouping of Usage accounts"

- Names considered:
  - Billing Account / Account
  - Billing Account / Member Account
  - Billing Account / Sub Account
  - Billing Account / Resource Account
  - Billing Scope / Service Scope
  - Invoice Scope / Resource Management Scope
  - Billed to / Managed in

- Other descriptions considered:
  - Logical grouping of resources based on usage, access and/or billing boundaries.
  - Resource Container
  - Base level organizing entity of resources / resource container
  - A usage account is an organizing entity of provider resources.
  - (Combined) A usage account is a base-level organizing entity of provider resources often used to manage access and cost. A usage account is one of several structural elements of provider hierarchies.
  - Resource container

- What are the practitioner use cases

- Do billing and sub account dimensions need names? Can they use a level_n type naming scheme and have it flexibly map to customers and providers specifics?
  - Name is preferred as the level_n doesn't clearly explain which one is which

- To consider in v.1.0+:
  - Quote from Slack channel: ... we could have something like ScopeHierarchy, which is a JSON representation of the full hierarchy (e.g., [{ id: "", type: "PayerAccount", name: "" }, { id: "", type: "MemberAccount", name: "" }]). This allows anyone who cares about the full hierarchy to get it in a consistent way...
