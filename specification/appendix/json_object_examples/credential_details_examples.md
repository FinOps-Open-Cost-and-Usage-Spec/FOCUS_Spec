# Examples: Credential Details

The examples below are not exhaustive and may change over time. Service providers are the authoritative source for the identity attributes they publish.

## Aura Web (Inference Request via an API Key)

Scenario: A generative AI inference [*charge*](#glossary:charge) authenticated with an API key that acts under a named user. The named user is the [*principal*](#glossary:principal), so the user's attributes sit at the top level, and the API key is the [*credential*](#glossary:credential) recorded in the `Credential` property. The `Credential` object repeats the CredentialId value in its `Id` key, which is optional; the examples that follow omit it.

| ServiceProviderName | ServiceName | PrincipalId | CredentialId | CredentialDetails |
|---------------------|-------------|-------------|--------------|-------------------|
| Aura Web | Inference | user_8842 | key_01HQZX3M8N | {"Name": "Alex Rivera", "Email": "alex.rivera@example.com", "Type": "User", "Credential": {"Id": "key_01HQZX3M8N", "Type": "API Key", "Name": "prod-ingest-key"}} |

## LatticeScale (Direct Console Access)

Scenario: An object storage charge initiated by a user authenticating directly through a console session that the [*service provider*](#glossary:service-provider) identifies separately from the user.

| ServiceProviderName | ServiceName | PrincipalId | CredentialId | CredentialDetails |
|---------------------|-------------|-------------|--------------|-------------------|
| LatticeScale | ObjectStorage | user_4417 | sess_9KD2LM4T | {"Name": "Jordan Lee", "Email": "jordan.lee@example.com", "Type": "User", "Credential": {"Type": "Session"}} |

## Aura Web (Scheduled Job Under a Service Account)

Scenario: A compute charge initiated by a service account, where the *service provider* does not distinguish the *credential* presented from the *principal* that presented it. PrincipalId and CredentialId carry the same value, and the `Credential` property is omitted. A service account has no email address, so Email is omitted and Type distinguishes the *principal* from a human user.

| ServiceProviderName | ServiceName | PrincipalId | CredentialId | CredentialDetails |
|---------------------|-------------|-------------|--------------|-------------------|
| Aura Web | Compute | svc_nightly_etl | svc_nightly_etl | {"Name": "svc-nightly-etl", "Type": "Service Account"} |

## Meridian AI (Credential Without a Determinable Principal)

Scenario: An inference charge authenticated with an API key that the *service provider* cannot map to an entity in its identity and access management model. The *service provider* cannot determine a *principal*, so PrincipalId is null, while the *credential* it does know is recorded.

| ServiceProviderName | ServiceName | PrincipalId | CredentialId | CredentialDetails |
|---------------------|-------------|-------------|--------------|-------------------|
| Meridian AI | Inference | null | key_07PQXR2W9F | {"Credential": {"Type": "API Key", "Name": "eval-sandbox"}} |

## StackLens (No Determinable Principal or Credential)

Scenario: A platform subscription billed at the account level, with no entity in the *service provider's* identity and access management model associated with it and no *credential* presented. PrincipalId, CredentialId, and CredentialDetails are all null.

| ServiceProviderName | ServiceName | PrincipalId | CredentialId | CredentialDetails |
|---------------------|-------------|-------------|--------------|-------------------|
| StackLens | Observability | null | null | null |

## Aura Web (Provider-Specific Attributes)

Scenario: A *service provider* publishes an identity attribute that has no FOCUS-defined property. The attribute is carried as a custom property prefixed with "x_".

| ServiceProviderName | ServiceName | PrincipalId | CredentialId | CredentialDetails |
|---------------------|-------------|-------------|--------------|-------------------|
| Aura Web | Inference | user_8842 | user_8842 | {"Name": "Alex Rivera", "Email": "alex.rivera@example.com", "Type": "User", "x_DirectoryGroup": "platform-engineering"} |

## Cost Attribution by Principal and by Credential

This example demonstrates how the two identifier columns support different attribution questions.

Acme Corp runs generative AI inference and scheduled compute on Aura Web. Four charges land in a single charge period (2025-04-01):

1. **Inference via an API key** (Row 1): Alex Rivera, presenting `prod-ingest-key`. [BilledCost](#datamodel.costandusage.billedcost) is $120.00.
2. **Inference, direct** (Row 2): Alex Rivera, with no *credential* the *service provider* distinguishes from the user. BilledCost is $30.00.
3. **Inference via an API key** (Row 3): Jordan Lee, presenting `batch-key`. BilledCost is $75.00.
4. **Scheduled compute** (Row 4): the `svc-nightly-etl` service account, which has no email address. BilledCost is $45.00.

Grouping by PrincipalId answers which actor incurred the cost, and combines a user's charges regardless of which *credential* was presented:

| PrincipalId | Email | BilledCost |
|:---|:---|:---|
| user_8842 | alex.rivera@example.com | $150.00 |
| user_4417 | jordan.lee@example.com | $75.00 |
| svc_nightly_etl | null (service account) | $45.00 |
| **Total** | | **$270.00** |

Grouping by CredentialId answers which *credential* incurred the cost, and separates the two paths Alex Rivera used:

| CredentialId | Credential Type | BilledCost |
|:---|:---|:---|
| key_01HQZX3M8N | API Key | $120.00 |
| user_8842 | null (no distinct credential) | $30.00 |
| key_04KTMP7B2Q | API Key | $75.00 |
| svc_nightly_etl | null (no distinct credential) | $45.00 |
| **Total** | | **$270.00** |

Rows 1 and 2 combine to $150.00 for Alex Rivera under PrincipalId and separate into $120.00 and $30.00 under CredentialId. Both groupings count every *charge* once and total $270.00, because each identifier appears once per row.
