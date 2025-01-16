# Column: SubAccountType

## Example provider mappings

Current column mappings found in available data sets:

| Provider  | Data set                | Column        |
| --------- | ----------------------- | ------------- |
| AWS       | CUR                     | Not available |
| GCP       | BigQuery Billing Export | Not available |
| Microsoft | Cost details            | Not available |

## Documentation

- GCP: [Resource Hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#resource-hierarchy-detail)
- Azure: [Organizing resources](https://learn.microsoft.com/azure/cost-management-billing/manage/view-all-accounts)
- AWS: [Org Concepts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html)

## Example usage scenarios

Current terms used by providers:

| Provider  | Value            |
| --------- | ---------------- |
| AWS       | "Membership Account" |
| GCP       | "Project"        |
| Microsoft | "Subscription"   |
| OCI       | "Tenancy"        |
| OCI       | "Child Tenancy"  |

## Discussion / scratch space

We ran a poll to determine if BillingAccountType and SubAccountType columns were desired. Poll results:
* 4 votes for `Yes, add both columns as REQUIRED for ALL providers`
* 10 votes for `Yes, add both columns as REQUIRED for providers that have DIFFERENT ACCOUNT TYPES`
* 1 vote for `Yes, add both columns as OPTIONAL for all providers`
* 4 votes for `I am fine with or without these columns`
* 0 votes for `No, I do not want/need these columns in the FOCUS dataset`
