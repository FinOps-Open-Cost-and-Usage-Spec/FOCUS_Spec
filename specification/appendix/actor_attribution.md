# Examples: Actor Attribution

The examples below illustrate how [Principal ID](#datasets.costandusage.principalid) is populated in the [Cost and Usage](#datasets.costandusage) dataset across technology categories. Each scenario identifies the [*principal*](#glossary:principal) to which a [*service provider*](#glossary:service-provider) grants access to a [*resource*](#glossary:resource) or [*service*](#glossary:service), and notes where the party that benefits from the [*charge*](#glossary:charge) differs from that *principal*.

1. **Generative AI API:** **Acme Corp** uses an internal bot to summarize notes via a LatticeScale API. The bot authenticates as a service account, which LatticeScale records as the *principal* (`PrincipalId`). The employee whose notes are summarized benefits from the *charge* and is not the *principal*.
2. **Multi-Tenant PaaS:** A shared BI engine runs a query on OmniQuery for a specific client of **GearPeak Outdoors**. OmniQuery grants access to the engine's service account, which is the *principal* (`PrincipalId`). The client that requested the report benefits from the *charge* and is not the *principal*.
3. **Network Edge Processing:** At **Acme Corp**, traffic routed through an Aura Web edge network authenticates at the gateway, which Aura Web records as the *principal* (`PrincipalId`). The end users behind the aggregated traffic benefit from the *charge* and are not resolvable in the billing data.
4. **Seat-Based SaaS:** **Acme Corp** pre-purchases SprintCanvas seats assigned to individual users. SprintCanvas grants each seat holder access under its own identity and access management model, so the seat holder is the *principal* (`PrincipalId`) and also the party that benefits from the *charge*.
5. **Seat-Plus-Token SaaS:** **Acme Corp** subscribes to PipelCRM and uses its embedded AI assistant. The seat license and the per-token AI usage are reported as separate *charges* under the same seat holder (`PrincipalId`), who also benefits from both *charges*, so attribution follows the user as *service providers* shift from seat-based to hybrid seat and consumption-based pricing.
6. **Direct PaaS Usage:** A data scientist at **Acme Corp** logs into a LatticeScale managed notebook using their individual SSO credential. LatticeScale grants access to that user identity, which is the *principal* (`PrincipalId`), and the same user benefits from the *charge*.
7. **Billing System Charge:** **Acme Corp** receives a promotional credit or is charged applicable tax from LatticeScale. The *charge* originates in the *service provider's* billing system and is not associated with any entity in its identity and access management model, so `PrincipalId` is `null`.

| # | Scenario | Data Generator | PrincipalId |
| :--- | :--- | :--- | :--- |
| 1 | **Generative AI API** | LatticeScale | `svc-acme-docbot-prod` |
| 2 | **Multi-Tenant PaaS** | OmniQuery | `svc-bi-reporting-engine` |
| 3 | **Network Edge Processing** | Aura Web | `svc-edge-gateway-prod` |
| 4 | **Seat-Based SaaS** | SprintCanvas | `user_uuid_554321` |
| 5 | **Seat-Plus-Token SaaS** | PipelCRM | `user_uuid_887766` |
| 6 | **Direct PaaS Usage** | LatticeScale | `dev_uuid_112233` |
| 7 | **Billing System Charge** | LatticeScale | `null` |
