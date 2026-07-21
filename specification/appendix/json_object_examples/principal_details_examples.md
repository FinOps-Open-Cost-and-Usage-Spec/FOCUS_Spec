# Examples: Principal Details

The examples below are not exhaustive and may change over time. Service providers are the authoritative source for the identity attributes they publish.

## Aura Web (Inference Request via an API Key)

Scenario: A generative AI inference charge authenticated with an API key that acts under a named user. The named user is the [*principal*](#glossary:principal), so the user's attributes sit at the top level and the API key is recorded as an intermediate identity.

| ServiceProviderName | ServiceName | PrincipalDetails |
|---------------------|-------------|------------------|
| Aura Web | Inference | {"PrincipalName": "Alex Rivera", "PrincipalEmail": "alex.rivera@example.com", "PrincipalType": "User", "Intermediates": [{"PrincipalType": "API Key", "PrincipalId": "key_01HQZX3M8N", "PrincipalName": "prod-ingest-key"}]} |

## Aura Web (Scheduled Job Under a Service Account)

Scenario: A compute charge initiated by a service account. A service account has no email address, so PrincipalEmail is omitted and PrincipalType distinguishes the *principal* from a human user.

| ServiceProviderName | ServiceName | PrincipalDetails |
|---------------------|-------------|------------------|
| Aura Web | Compute | {"PrincipalName": "svc-nightly-etl", "PrincipalType": "Service Account"} |

## LatticeScale (Direct Console Access)

Scenario: An object storage charge initiated by a user authenticating directly, with no intermediate identity between the user and the [*service provider*](#glossary:service-provider). The `Intermediates` array is omitted.

| ServiceProviderName | ServiceName | PrincipalDetails |
|---------------------|-------------|------------------|
| LatticeScale | ObjectStorage | {"PrincipalName": "Jordan Lee", "PrincipalEmail": "jordan.lee@example.com", "PrincipalType": "User"} |

## StackLens (No Determinable Principal)

Scenario: A subscription charge that accrues without an initiating request. The *service provider* cannot determine a *principal*, so [PrincipalId](#datasets.costandusage.principalid) is null and PrincipalDetails is null.

| ServiceProviderName | ServiceName | PrincipalId | PrincipalDetails |
|---------------------|-------------|-------------|------------------|
| StackLens | Observability | null | null |

## Aura Web (Provider-Specific Attributes)

Scenario: A *service provider* publishes an identity attribute that has no FOCUS-defined property. The attribute is carried as a custom property prefixed with "x_".

| ServiceProviderName | ServiceName | PrincipalDetails |
|---------------------|-------------|------------------|
| Aura Web | Inference | {"PrincipalName": "Alex Rivera", "PrincipalEmail": "alex.rivera@example.com", "PrincipalType": "User", "x_DirectoryGroup": "platform-engineering"} |

## Cost Attribution by Principal

This example demonstrates how the placement of identity attributes affects [*charge*](#glossary:charge) attribution.

Acme Corp runs generative AI inference and scheduled compute on Aura Web. Four charges land in a single charge period (2025-04-01):

1. **Inference via an API key** (Row 1): Alex Rivera, reached through `prod-ingest-key`. [BilledCost](#datasets.costandusage.billedcost) is $120.00.
2. **Inference, direct** (Row 2): Alex Rivera, no intermediate identity. BilledCost is $30.00.
3. **Inference via an API key** (Row 3): Jordan Lee, reached through `batch-key`. BilledCost is $75.00.
4. **Scheduled compute** (Row 4): the `svc-nightly-etl` service account, which has no email address. BilledCost is $45.00.

Because PrincipalEmail is a top-level property, grouping by it reads the value directly from each row and counts every charge once:

| PrincipalEmail | BilledCost |
|:---------------|:-----------|
| alex.rivera@example.com | $150.00 |
| jordan.lee@example.com | $75.00 |
| null (service account) | $45.00 |
| **Total** | **$270.00** |

Rows 1 and 2 combine to $150.00 for Alex Rivera, and the total matches the sum of the four charges.

Had the same attributes been reachable only inside the `Intermediates` array, Rows 1 and 3 would each expand to two entries when the array is flattened, and a sum taken across the flattened result would report $465.00 against a true total of $270.00. Keeping the attributes of the *principal* at the top level means the common attribution query needs no flattening and no de-duplication step.
