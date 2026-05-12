# Examples: Actor Attribution

The examples below illustrate how [Principal ID](#datasets.costandusage.principalid) and [Consumer ID](#datasets.costandusage.consumerid) in the [Cost and Usage](#datasets.costandusage) dataset are populated across different data generators and technology categories to resolve asymmetric actor granularity. Comparing these scenarios demonstrates how FOCUS handles attribution when the infrastructure actor and application actor are distinct, identical, or mutually exclusive.

1. **Generative AI API:** **Acme Corp** uses an internal bot to summarize notes via a LatticeScale API. Security audits the service account (`PrincipalId`), while FinOps allocates token costs to the employee (`ConsumerId`).
2. **Multi-Tenant PaaS:** A shared BI engine runs a query on OmniQuery for a specific client of **GearPeak Outdoors**. Capturing the downstream client (`ConsumerId`) prevents costs from pooling in overhead.
3. **Direct IaaS:** A data engineer at **AeroScale** directly provisions an Aura Web compute cluster. Because the infrastructure is consumed directly by the principal, no downstream application actor exists.
4. **Seat-Based SaaS:** **Acme Corp** pays for SprintCanvas project management licenses. The provider does not attribute an infrastructure actor, but the opaque `ConsumerId` allows safe user-level chargeback.
5. **Direct PaaS Usage:** A data scientist at **Acme Corp** logs into a LatticeScale managed notebook using their individual SSO credential. Because the user authenticated directly to the platform and is the sole consumer of the compute, the same opaque identifier is populated in both columns.

| Scenario | Technology Category | Data Generator | PrincipalId | ConsumerId |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **Generative AI API** | LatticeScale | `svc-acme-docbot-prod` | `emp_hash_84729x` |
| 2 | **Multi-Tenant PaaS** | OmniQuery | `svc-bi-reporting-engine` | `client_gearpeak_001` |
| 3 | **Direct IaaS** | Aura Web | `user_d_engineer_993` | `null` |
| 4 | **Seat-Based SaaS** | SprintCanvas | `null` | `user_uuid_554321` |
| 5 | **Direct PaaS Usage** | LatticeScale | `dev_uuid_112233` | `dev_uuid_112233` |