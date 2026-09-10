# Examples: Requester Details

The examples below are not exhaustive and may change over time. The authoritative source for each identity attribute is the party that publishes it.

## Aura Web (Inference Request via an API Key)

Scenario: A generative AI inference [*charge*](#glossary:charge) authenticated with an API key that acts under a named user. The named user is the [*principal*](#glossary:principal), described by the `Principal` entry, and the API key is the [*credential*](#glossary:credential), described by the `Credential` entry. The opaque identifiers are carried by the PrincipalId and CredentialId columns, so each entry's `value` holds only descriptive attributes.

| ServiceProviderName | ServiceName | PrincipalId | CredentialId | RequesterDetails |
|---------------------|-------------|-------------|--------------|-------------------|
| Aura Web | Inference | user_8842 | key_01HQZX3M8N | [{"key": "Principal", "value": {"Name": "Alex Rivera", "Email": "alex.rivera@example.com", "Type": "User"}}, {"key": "Credential", "value": {"Type": "API Key", "Name": "prod-ingest-key"}}] |

## LatticeScale (Direct Console Access)

Scenario: An object storage charge initiated by a user authenticating directly through a console session that is identified separately from the user.

| ServiceProviderName | ServiceName | PrincipalId | CredentialId | RequesterDetails |
|---------------------|-------------|-------------|--------------|-------------------|
| LatticeScale | ObjectStorage | user_4417 | sess_6BN3XR8P | [{"key": "Principal", "value": {"Name": "Jordan Lee", "Email": "jordan.lee@example.com", "Type": "User"}}, {"key": "Credential", "value": {"Type": "Session"}}] |

## Aura Web (Scheduled Job Under a Service Account)

Scenario: A compute charge initiated by a service account, where the *credential* the service account presented has no published identifier. CredentialId is null and the `Credential` entry is omitted. A service account has no email address, so Email is omitted and Type distinguishes the *principal* from a human user.

| ServiceProviderName | ServiceName | PrincipalId | CredentialId | RequesterDetails |
|---------------------|-------------|-------------|--------------|-------------------|
| Aura Web | Compute | svc_nightly_etl | null | [{"key": "Principal", "value": {"Name": "svc-nightly-etl", "Type": "Service Account"}}] |

## Meridian AI (Credential Without a Determinable Principal)

Scenario: An inference charge authenticated with an API key that cannot be mapped to an entity in the identity and access management model. No *principal* can be determined, so PrincipalId is null, while the known *credential* is recorded in the `Credential` entry.

| ServiceProviderName | ServiceName | PrincipalId | CredentialId | RequesterDetails |
|---------------------|-------------|-------------|--------------|-------------------|
| Meridian AI | Inference | null | key_07PQXR2W9F | [{"key": "Credential", "value": {"Type": "API Key", "Name": "eval-sandbox"}}] |

## StackLens (No Determinable Principal or Credential)

Scenario: A platform subscription billed at the account level, with no entity in the identity and access management model associated with it and no *credential* presented. PrincipalId, CredentialId, and RequesterDetails are all null.

| ServiceProviderName | ServiceName | PrincipalId | CredentialId | RequesterDetails |
|---------------------|-------------|-------------|--------------|-------------------|
| StackLens | Observability | null | null | null |

## Aura Web (Custom Identity Attribute)

Scenario: An identity attribute is published that has no FOCUS-defined property. The attribute describes the *principal*, so it is carried as a custom property prefixed with "x_" within the `value` of the `Principal` entry.

| ServiceProviderName | ServiceName | PrincipalId | CredentialId | RequesterDetails |
|---------------------|-------------|-------------|--------------|-------------------|
| Aura Web | Inference | user_8842 | key_01HQZX3M8N | [{"key": "Principal", "value": {"Name": "Alex Rivera", "Email": "alex.rivera@example.com", "Type": "User", "x_DirectoryGroup": "platform-engineering"}}, {"key": "Credential", "value": {"Type": "API Key", "Name": "prod-ingest-key"}}] |

## Aura Web (Assumed Role with a Delegating Identity)

Scenario: An engineer assumes a deployment role to run a compute job. Access to the [*resource*](#glossary:resource) is granted to the role, so the role is the *principal*, and the assumed-role session is the *credential*. The delegating user is a level of the [*requester*](#glossary:requester) that is neither the *principal* nor the *credential*, so it is carried as a custom entry whose `value` uses the same properties as the FOCUS-defined entries.

| ServiceProviderName | ServiceName | PrincipalId | CredentialId | RequesterDetails |
|---------------------|-------------|-------------|--------------|-------------------|
| Aura Web | Compute | role_deploy_prod | sess_R7D3PK5V | [{"key": "Principal", "value": {"Name": "deploy-prod", "Type": "Role"}}, {"key": "Credential", "value": {"Type": "Session"}}, {"key": "x_DelegatingIdentity", "value": {"Name": "Priya Nair", "Email": "priya.nair@example.com", "Type": "User"}}] |

## Meridian AI (Agent Harnesses Under One User)

Scenario: An engineer at Acme Corp runs two agent harnesses against the same inference service, a command-line agent and an IDE extension. Both authenticate as the engineer through single sign-on. Meridian AI defines each client application in its identity and access management model and identifies which one presented each session. The engineer is the *principal* on both rows and each harness's session is its own *credential*. The client application is a level of the *requester* that is neither, so it is carried as a custom entry whose `value` uses the same properties as the FOCUS-defined entries. Grouping by PrincipalId combines the engineer's spend across harnesses, and grouping by the `x_ClientApplication` entry separates it.

| ServiceProviderName | ServiceName | PrincipalId | CredentialId | RequesterDetails |
|---------------------|-------------|-------------|--------------|-------------------|
| Meridian AI | Inference | user_5108 | sess_9QT4LM2A | [{"key": "Principal", "value": {"Name": "Sam Okafor", "Email": "sam.okafor@example.com", "Type": "User"}}, {"key": "Credential", "value": {"Type": "Session"}}, {"key": "x_ClientApplication", "value": {"Name": "Forge CLI", "Type": "Application"}}] |
| Meridian AI | Inference | user_5108 | sess_2WD8XN7C | [{"key": "Principal", "value": {"Name": "Sam Okafor", "Email": "sam.okafor@example.com", "Type": "User"}}, {"key": "Credential", "value": {"Type": "Session"}}, {"key": "x_ClientApplication", "value": {"Name": "Forge IDE Extension", "Type": "Application"}}] |

Where a [*service provider*](#glossary:service-provider) does not define client applications in its identity and access management model but issues each harness its own API key under the engineer, the harness is an attribute of the *credential* rather than a level of the *requester*, and the same information is carried as a custom property within the `Credential` entry.

| ServiceProviderName | ServiceName | PrincipalId | CredentialId | RequesterDetails |
|---------------------|-------------|-------------|--------------|-------------------|
| Meridian AI | Inference | user_5108 | key_08RRTX5M2B | [{"key": "Principal", "value": {"Name": "Sam Okafor", "Email": "sam.okafor@example.com", "Type": "User"}}, {"key": "Credential", "value": {"Type": "API Key", "Name": "forge-cli", "x_ClientApplication": "Forge CLI"}}] |

## LatticeScale (Autonomous Agent Under a Workload Identity)

Scenario: Acme Corp operates a code review agent that runs without a person initiating each run. Each run exchanges a short-lived federated token for access to LatticeScale's inference service. The agent's service account is the *principal*, and LatticeScale assigns each exchange a federated session identifier, which is the *credential*. The token itself is never published. The team that operates the agent is published as an attribute of the service account, so it is carried as a custom property within the `Principal` entry. Two runs produce two rows that share a PrincipalId and differ in CredentialId, so grouping by PrincipalId yields the agent's total and grouping by CredentialId yields cost per run. The engineers whose pull requests the agent reviewed are not represented in either column.

| ServiceProviderName | ServiceName | PrincipalId | CredentialId | RequesterDetails |
|---------------------|-------------|-------------|--------------|-------------------|
| LatticeScale | Inference | svc-review-agent | fedsess_3HN8KW2D | [{"key": "Principal", "value": {"Name": "svc-review-agent", "Type": "Service Account", "x_OwningTeam": "platform-engineering"}}, {"key": "Credential", "value": {"Type": "Federated Session"}}] |
| LatticeScale | Inference | svc-review-agent | fedsess_7MP1QZ6R | [{"key": "Principal", "value": {"Name": "svc-review-agent", "Type": "Service Account", "x_OwningTeam": "platform-engineering"}}, {"key": "Credential", "value": {"Type": "Federated Session"}}] |

## Cost Attribution by Principal and by Credential

This example demonstrates how the two identifier columns support different attribution questions.

Acme Corp runs generative AI inference and scheduled compute on Aura Web. Four charges land in a single charge period (2025-04-01):

1. **Inference via an API key** (Row 1): Alex Rivera, presenting `prod-ingest-key`. [BilledCost](#datamodel.costandusage.billedcost) is $120.00.
2. **Inference via a console session** (Row 2): Alex Rivera, working in the Aura Web console, where the session is identified separately from the user. BilledCost is $30.00.
3. **Inference via an API key** (Row 3): Jordan Lee, presenting `batch-key`. BilledCost is $75.00.
4. **Scheduled compute** (Row 4): the `svc-nightly-etl` service account, which has no email address and for which no *credential* identifier is published. BilledCost is $45.00.

Grouping by PrincipalId answers which *requester* incurred the cost, and combines a user's charges regardless of which *credential* was presented:

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
| sess_AW7C2K91 | Session | $30.00 |
| key_04KTMP7B2Q | API Key | $75.00 |
| null | null | $45.00 |
| **Total** | | **$270.00** |

Rows 1 and 2 combine to $150.00 for Alex Rivera under PrincipalId and separate into $120.00 and $30.00 under CredentialId. Row 4 carries no CredentialId, so grouping on that column collects it under null rather than attributing it to a *credential*. Both groupings count every *charge* once and total $270.00, because each identifier appears once per row.

Grouping by the `Type` property of the `Principal` entry separates the cost incurred by human users from the cost incurred by workloads:

| Principal Type | BilledCost |
|:---|:---|
| User | $225.00 |
| Service Account | $45.00 |
| **Total** | **$270.00** |

Principal Type is read from the entry whose `key` is `Principal`. Because RequesterDetails is an array, a query that flattens every entry before aggregating counts each row once per entry. In this example, where Rows 1 through 3 each carry a `Credential` entry as well as a `Principal` entry, a sum over the flattened entries reaches $495.00 rather than $270.00, with Row 1 counted under both "User" and "API Key". Filtering to the `Principal` entry before aggregating, or extracting its `Type` as a scalar, keeps each *charge* counted once.
