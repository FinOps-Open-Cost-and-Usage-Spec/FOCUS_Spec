Note: Tags is the generic term standardized in FOCUS but for the examples below, I try to refer to the provider's native term to prevent confusion (e.g. GCP has concepts named "labels" and "tags" with different properties and capabilities).

[TagDetails](#datasets.costandusage.tagdetails) column is intended to be supplementary information that helps a practitioner 
* Determine the provenance of the contents of the [Tags](#datasets.costandusage.tags) column
* Find the other tags present which were not part of the finalized tags (whether provider supports tag finalization or not)
* Identify if it would have been possible to have tagged this charge

There are many different ways and places to provide tagging
* Many tags can be set at the resource level
  * In most cases, tags can be set at an ancestor level (Azure subscription or resource group, GCP project, etc.)
* Some labels are explicitly not included in the cost and usage data. E.g [GCP BigQuery table-level labels](https://docs.cloud.google.com/bigquery/docs/adding-labels#adding_table_and_view_labels)
* In some cases tags can be set for charges in a novel or non-obvious place.
  * For certain offerings, labels can be added to the job or API call to specify the labels for that charge. E.g. [GCP BigQuery job labels](https://docs.cloud.google.com/bigquery/docs/adding-labels#job-label)
  * Sometimes tags can be applied to a principal that calls the API to apply to the charges for using that API. E.g. [The tags property of Azure App manifest](https://learn.microsoft.com/en-us/entra/identity-platform/reference-microsoft-graph-app-manifest#tags-attribute)
