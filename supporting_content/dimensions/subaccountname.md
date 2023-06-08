# Column: SubAccountName

## Example provider mappings


Current column mappings found in available data sets:

| Provider  | Data set                 | Column                                                    |
|-----------|--------------------------|-----------------------------------------------------------|
| AWS       | CUR                      | Not currently available in the CUR, can be gained by the <br> Organizations [list-accounts](https://docs.aws.amazon.com/cli/latest/reference/organizations/list-accounts.html) API call, returning the name column,<br> this can be joined to the CUR by the UsageAccountId |
| GCP       | Big Query Billing Export | project.name                                              |
| Microsoft | Cost details             | SubscriptionName                                          |

- GCP: [Resource Hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#resource-hierarchy-detail) 
- Azure: [Resource Hierarchy](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview), [Organizing resources](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/view-all-accounts)
- AWS: [Org Concepts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html)