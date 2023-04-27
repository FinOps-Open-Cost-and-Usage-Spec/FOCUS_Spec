### Resource ID

#### Example mappings

|Provider|Data set|Vendor column|
|---|---|---|
|AWS|CUR|line_item_resource_id|
|GCP|Big Query Billing Export|resource.name? resource.global_name?|
|Microsoft|EA|ResourceId|
|Microsoft|MCA|resourceId|#### Examples
#### Examples
|Provider|Scenario|Pattern|
|---|---|---|
|AWS|ARN provided which includes a resource name or id|arn:partition:service:region:account-id:resource-id<br />arn:partition:service:region:account-id:resource-type/resource-id<br />arn:partition:service:region:account-id:resource-type:resource-id|
|AWS|Some cases, just a resource-id is provided|I-0b21f4c4434558933 OR my-cur-bucket|
|AWS|Tax, API call charges etc.|(null)|
|GCP|Resource based|//container.googleapis.com/projects/\<project_id>/locations/\<location>/clusters/\<cluster>|
|GCP|Non-resource based (e.g. network egress)|(null)|
|Microsoft|Resource group resources|/subscriptions/\<guid>/resourceGroups/\<name>/providers/\<provider>/\<resource-type>/<resource-name>|
|Microsoft|Subscription resources|/subscriptions/\<guid>/providers/\<provider>/\<resource-type>/\<resource-name>|
|Microsoft|Tenant resources|/providers/\<provider>/\<resource-type>/\<resource-name>|
|Microsoft|Purchase charges|(null)|
|Microsoft|Reservation purchases|/providers/Microsoft.Capacity/reservationOrders/\<guid>|

#### Reading:

AWS: <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html>

> Interesting note on the "The resource identifier" which is at the end of the ARN: This is the name of the resource, the ID of the resource, or a [resource path](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html#arns-paths). Some resource identifiers include a parent resource (sub-resource-type/parent-resource/sub-resource) or a qualifier such as a version (resource-type:resource-name:qualifier)."

GCP: <https://cloud.google.com/apis/design/resource_names> <https://cloud.google.com/asset-inventory/docs/resource-name-format> 

#### Discussion / Scratch space:

-   Should this be prefixed with 'Vendor' e.g. VendorResourceID to show that it's a 1:1 mapping to a vendor provided column. 

-   Should governance say "Nullable where cost is not associated with a resource"

-   Do we make any statements about uniqueness? Or is this where we request a uniqueness composite key to be specified in a schema document

-   Can uniqueness and can it change over time?

-   Empty values should not be allowed if a user/systematically generated value is null (should this be an attribute specified as a higher level attribute OR within this scope)?

-   (Erik Peterson) Future attribute/dimension duggestion: Embrace a "Cloud Resource ID (CRID)" convention such as:
<br />crid:provider:service-type:region:owner-account-id:resource-type:cloud-local-id
