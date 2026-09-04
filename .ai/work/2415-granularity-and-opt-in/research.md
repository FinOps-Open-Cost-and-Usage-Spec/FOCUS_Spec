# AI #2415: Granularity and Opt-In Research

## Scope

Issue #2415 asks for a draft PR, kept in draft, under FR #2358. The PR should propose how FOCUS models a delivery grain or opt-in concept for high-cardinality actor dimensions before PR #2360 adds `PrincipalId` and `ConsumerId`.

This research looked only at this repository:

* Issue #2415
* FR #2358
* PR #2351
* PR #2360
* Prior merged PRs for similar spec patterns: #1816, #1800, and #1501
* Current local spec files

## Findings

### PR #2351 Is Relevant

PR #2351 is directly relevant because it introduced the `conditions/` architecture and the `Operating Model` framing now used by `CostAndUsage` column presence requirements.

Important pattern:

* A condition should represent a verifiable state of the operating model.
* Dataset column presence should link `Conditional` feature levels to formal conditions.
* Conditions should not describe a data generator's dataset-shaping choice.

Implication for actor dimensions:

`IncludesConsumers` and `IncludesPrincipals` from PR #2360 are probably too broad. Most operating models include principals or consumers in some conceptual sense, but that does not mean charges can be attributed to them in billing data. A better condition shape would be:

* `IncludesPrincipalAttribution`
* `IncludesConsumerAttribution`

Those conditions can represent whether the operating model includes charge attribution to those actor roles.

### Dataset Configuration Is the Closest Existing Attribute

PR #1816 added `DatasetConfiguration` and explicitly scoped it to column selection. Its PR body says row aggregation, time granularity selection, row filtering, and configuration metadata were deferred to separate changes.

Issue #2415 is one of those deferred configuration problems. It is not just "include or exclude this column"; it changes record grain and can increase row count.

The current `DatasetConfiguration` attribute already says:

* A FOCUS dataset must be configurable to include a user-defined selection of columns.
* A FOCUS dataset must still adhere to column-level specifications regardless of selected configuration.

That is necessary but insufficient for the actor use case. It does not explain:

* scoped opt-in, such as Service-A actor granularity without Service-B actor granularity;
* multiple granularity levels, such as principal, consumer, session, trace;
* whether granular dataset instances replace or supplement other dataset instances that represent the same underlying usage or charges;
* how practitioners avoid double-counting when multiple dataset instances represent the same underlying charges.

Recommended direction: extend `DatasetConfiguration` to cover granularity configurations, instead of adding a column-level `Delivery grain` field.

### Column-Level "Delivery Grain" Does Not Fit the Use Case

PR #2360 currently proposes:

* a `Delivery Grain` section in `specification/overview.md`;
* a `Delivery grain | Opt-in` row in `principalid.md` and `consumerid.md`;
* dataset presence requirements such as "in at least one dataset instance when ... the customer has opted in to receive data at the consumer grain."

This is a useful starting point, but it is too column-centric for the actual requirement.

Problems:

* A single per-column `Opt-in` label cannot express "turn on `ConsumerId` for Service-A, but not for Service-B."
* It cannot express multiple levels such as consumer, session, and trace.
* It introduces a new content-constraint row that no other column has.
* It puts global design language in the Introduction rather than in an attribute.
* The current wording uses "customer has opted in" inside a dataset requirement, but FOCUS normative language should keep schema-level entities as subjects.

Better framing:

Actor columns should remain normal columns with stable semantics. Optionality should be modeled through documented granularity configurations.

### Split Cost Allocation Is Relevant, But Not the Primary Mechanism

Split cost allocation is relevant as precedent:

* It already has an opt-in concept.
* It already addresses records becoming more granular.
* It already requires a documented method.
* It already has summable-metric preservation rules.

But it should not be the default home for actor dimensions.

Split cost allocation applies when a data generator takes an origin charge and splits it into allocated charges using a documented allocation method. Actor dimensions can be native request dimensions instead. For example, a Service-A usage event may already have a principal at request time, without any allocation ratio being calculated.

Use split cost allocation when:

* a shared origin charge must be apportioned across multiple consumers or resources;
* allocation ratios or allocated charges are part of the method;
* the original charge can be derived from allocated charges.

Do not use split cost allocation when:

* the provider is simply delivering native usage at a more detailed record grain;
* `PrincipalId` or `ConsumerId` are additional dimensions on already-measured usage records;
* future `SessionId` or `TraceId` columns identify request lineage rather than allocation ratios.

### Metric Behavior Must Not Be Assumed

The opt-in logic should not assume every opted-in dimension can validly split every metric field.

There are at least two different cases:

* Native finer-grain delivery: the data generator observes usage and cost at the configured grain. In this case, summable metrics such as cost or quantity can be represented directly at that grain when the provider can produce them accurately.
* Derived finer-grain delivery: the data generator starts from an origin charge and apportions cost or usage into allocated charges. This is split cost allocation and requires method documentation, allocated ratios, and metric conservation rules.

The current split cost allocation attribute already treats metric types differently:

* Dimensions on allocated charges match the origin charge when present.
* Non-summable metrics, such as unit prices, match the origin charge when present.
* Summable metrics, such as costs and quantities, must sum back to the corresponding origin charge.

Rates and unit prices likely align with SKU-level pricing rather than actor/session-level attribution. Since a CostAndUsage record normally has a single SKU context, lower-grain records that are derived by adding actor, session, trace, or similar dimensions would generally retain the same applicable rate or unit price. The cost and quantity metrics may be split, measured, or allocated, but the rate itself should normally remain associated with the SKU and pricing terms rather than be divided across lower-grain records.

Implication for #2415:

* FOCUS dataset granularity configuration documentation should describe how summable metrics behave across configured grains.
* The spec should not imply that unit prices, rates, or other non-summable metrics are "split" by adding high-cardinality dimensions.
* Documentation should clarify whether non-summable metrics such as unit prices are repeated from the parent/SKU-level record, omitted, or otherwise represented at the finer grain.
* When a configured grain uses allocation rather than native measurement, split cost allocation requirements should apply.

Open design question:

* Should DatasetConfiguration add a generic metric-integrity requirement for configured granular dataset instances, or should it only cross-reference Split Cost Allocation when metric values are derived from an origin charge?

### Granularity Representation Modes

Issue #2415 should explicitly weigh how lower-grain detail is represented. A useful working term is `granularity representation mode`, but alternatives include:

* `Granularity delivery mode`
* `Granular detail representation`
* `Detail representation mode`
* `Granularity representation pattern`

Recommendation: use `granularity representation mode` in research and PR framing. It is specific enough to describe the schema/data shape, but it avoids overloading `delivery`, which already has meaning in `DeliveryHandling`.

Recommended values:

1. `Expanded`: multiple CostAndUsage records at the requested grain.
2. `Embedded`: one CostAndUsage record with a JSON breakdown column representing one-to-many granular detail.
3. `Referenced`: a primary CostAndUsage dataset instance plus a supporting detail dataset/file with a one-to-many relationship from cost records to granular actor/session/trace records.

Avoid using `Split` as the generic value for multiple CostAndUsage records. `Split cost allocation` is already a defined FOCUS concept with origin-charge, allocated-charge, allocation-method, and metric-conservation semantics. `Expanded` can cover both native finer-grain rows and split-allocation rows, while `Split` should remain reserved for the allocation-derived subtype.

Mapping to the proposed terms:

| Proposed term | Recommended term | Rationale |
| :--- | :--- | :--- |
| Inline | Embedded | More precise for nested JSON detail within a cost record. |
| Split | Expanded | Avoids conflict with existing Split Cost Allocation terminology. Split allocation can be a subtype of Expanded. |
| Detail | Referenced | Makes the one-to-many join/reference relationship explicit. |

Expanded CostAndUsage records:

* Pros:
  * Simple for practitioners to query with ordinary `GROUP BY` patterns.
  * Keeps costs, quantities, and actor dimensions in one schema.
  * Aligns with the current CostAndUsage column model and PR #2360's proposed columns.
  * Easier for tools that expect one table of cost and usage records.
  * Can represent both native lower-grain measurement and allocation-derived lower-grain records.
* Cons:
  * Can multiply row count substantially.
  * Can duplicate non-summable metrics and dimensional values across many rows.
  * Can increase privacy exposure because actor-grain identifiers appear directly in cost records.
  * Can create double-counting risk when multiple dataset instances represent the same underlying usage or charges.
  * Needs clear distinction between native expanded rows and split allocation rows.

Referenced detail dataset/file:

* Pros:
  * Keeps the primary CostAndUsage dataset stable and smaller.
  * Can represent many-to-one or one-to-many request/session/trace detail without forcing every cost metric into that grain.
  * Can isolate privacy-sensitive identifiers behind a separate access control and retention policy.
  * Can support deeper observability-style detail where cost allocation is not always needed.
* Cons:
  * Requires a stable join key or lineage mechanism between CostAndUsage records and detail records.
  * Requires clear semantics for whether detail records carry costs, ratios, quantities, or only identifiers.
  * Adds complexity for practitioners and tools.
  * May require a new FOCUS dataset or metadata model beyond the scope of PR #2415.

Embedded JSON breakdown column in CostAndUsage:

* Pros:
  * Keeps one primary cost record while carrying one-to-many actor/session/trace detail.
  * Avoids multiplying top-level CostAndUsage rows for every lower-grain entity.
  * Can represent cases where one cost record maps to many consumers, sessions, traces, or requests.
  * Can include per-element metrics such as cost, quantity, allocation ratio, or request count when the breakdown needs to be analytically useful.
  * Can isolate optional high-cardinality detail to a column that practitioners select intentionally through dataset configuration.
* Cons:
  * Makes common analysis harder because practitioners must parse nested JSON rather than group by first-class columns.
  * Can duplicate concepts already represented by first-class columns such as `ConsumerId`, creating ambiguity about which source is authoritative.
  * Requires precise JSON object semantics, including whether element-level costs are measured, allocated, estimated, or informational.
  * Requires conservation rules when element-level costs or quantities are included.
  * Can become a generic escape hatch for arbitrary observability detail unless tightly scoped.

The JSON option resembles `AllocatedMethodDetails`, but it would serve a different purpose. `AllocatedMethodDetails` explains how split cost allocation was calculated, including `AllocatedRatio`; it is not itself a general actor/session/trace relationship model. A future JSON breakdown column would need its own object schema if the group wants one cost record to carry many lower-grain actors or events.

`ClusterId` or `ClusterName` is probably not a breakdown-column example by itself. It is more naturally a first-class dimension or tag-like grouping value when one record has one cluster value. It becomes part of a breakdown structure only when a single CostAndUsage record needs to represent multiple clusters, or when a parent cost record carries a nested list of lower-grain cluster/workload elements.

### AWS Split Cost Allocation Precedent

AWS split cost allocation data is a useful concrete precedent because it shows a provider opting into more granular delivery through additional records and additional split-specific metrics, rather than only adding ordinary grouping dimensions.

According to the AWS CUR/Data Exports documentation:

* Split cost allocation data is opt-in through table configuration and is limited to Amazon ECS, AWS Batch, and Amazon EKS.
* It introduces container-level resources such as ECS tasks and Kubernetes pods into CUR, where costs previously appeared at EC2 instance level.
* It generates new usage records for each ECS task or Kubernetes pod per hour. Standard ECS/EKS split data adds two usage records per task/pod per hour for CPU and memory. EKS accelerated computing can add three usage records per pod per hour for accelerator, CPU, and memory.
* AWS adds split-specific fields under the `split_line_item` header:
  * `split_line_item_actual_usage`
  * `split_line_item_net_split_cost`
  * `split_line_item_net_unused_cost`
  * `split_line_item_parent_resource_id`
  * `split_line_item_public_on_demand_split_cost`
  * `split_line_item_public_on_demand_unused_cost`
  * `split_line_item_reserved_usage`
  * `split_line_item_split_cost`
  * `split_line_item_split_usage`
  * `split_line_item_split_usage_ratio`
  * `split_line_item_unused_cost`
* AWS also uses tags for EKS grouping attributes. The documented EKS split allocation tags include:
  * `aws:eks:cluster-name`
  * `aws:eks:deployment`
  * `aws:eks:namespace`
  * `aws:eks:node`
  * `aws:eks:workload-name`
  * `aws:eks:workload-type`

This precedent supports three conclusions for #2415:

* `ClusterId` / `ClusterName` behaves more like a grouping dimension or tag than a breakdown object when it has one value per split usage record.
* Split allocation needs specialized metric semantics because AWS adds cost, usage, ratio, reserved/actual usage, unused cost, and parent resource fields.
* Provider-specific split allocation can combine first-class split metrics with grouping dimensions/tags, which means the FOCUS model should not assume a single representation pattern for all granular opt-in data.

Recommended direction for the first #2415 PR:

* Define `Expanded` configured CostAndUsage dataset instances as the primary model because it fits current FOCUS architecture and PR #2360's first-class actor columns.
* Treat split cost allocation as a specialized `Expanded` subtype when lower-grain records are derived from an origin charge using an allocation method.
* Do not foreclose future `Embedded` JSON breakdown columns or `Referenced` supporting detail datasets/files.
* Add an open question in the PR description asking whether deep session/trace/actor detail belongs in CostAndUsage, embedded JSON, or a referenced supporting dataset.
* Require documentation of replacement or supplement relationships, representation mode, and metric behavior when multiple dataset instances, embedded breakdowns, or supporting files represent related charges.

### Dataset Instance Is the Right Unit for Multiple Grains

The glossary already defines `dataset instance` as a specific implementation of a FOCUS dataset and says a data generator may provide multiple dataset instances of the same FOCUS dataset with different properties, such as time granularity or custom column inclusion.

That gives us an existing concept for:

* Cost and Usage daily default instance;
* Cost and Usage hourly instance;
* Cost and Usage Service-A actor-grain instance;
* Cost and Usage Kubernetes workload-grain instance;
* Cost and Usage GenAI session-grain instance.

However, dataset instance granularity should not be modeled only as one global setting for the whole dataset instance. A single delivered dataset instance may contain multiple granularity configurations, each scoped by an applicability filter. For example:

* Service-A records can be configured at `[PrincipalId, ConsumerId]`.
* Another service can be configured at `[PrincipalId]`.
* Other services can use the default `[]` actor granularity.

The useful term for each scoped level of detail is `granularity configuration`: applicability scope plus the granularity-defining columns and representation mode. The applicability filter identifies which records in a dataset instance are in that scope, and it can be narrower than a service.

In a wide-file representation, the dataset schema contains the union of selected columns across configured granularities. Columns that do not apply to a record's configured granularity are null for those records. For example, when Service-A is configured at `[PrincipalId, ConsumerId]` and Service-B is configured at `[PrincipalId]`, Service-B records have null `ConsumerId` values.

Embedded JSON makes this harder because one-to-many detail must remain collated. A JSON representation likely needs either one composite JSON object/array containing all more granular fields for the configured granularity, or separate JSON columns with explicit rules for collating array elements across columns.

This is a better model than per-row opt-in flags or per-column content-constraint labels.

The missing piece is documentation/metadata requirements explaining the configured granularity and replacement or supplement behavior across delivered dataset instances.

### Metadata Is Related But Probably Not Enough for This PR

Issue #2358 comments say opt-in state should surface via metadata, and PR #2360 notes metadata is currently optional and needs cleanup before it can be relied on.

The schema metadata currently lists columns present in a dataset instance artifact. That tells a practitioner whether `ConsumerId` is present, but not the semantic grain of the dataset instance, the services it applies to, or whether it supplements another instance.

Recommended short-term approach:

* Require FOCUS dataset granularity configuration documentation for configured granularities.
* Avoid making metadata the only normative source until metadata requirements are strengthened.
* Optionally add non-normative implementation context saying metadata should identify the dataset instance and included columns.
* Avoid requiring a full catalog of all available granularities. The spec should focus on configured granularities delivered in dataset instances, similar to how schema metadata identifies delivered columns rather than every selectable column.

### PII and Privacy-Sensitive Granularity

FR #2358 and PR #2360 raise PII concerns for `PrincipalId` and `ConsumerId`. This is relevant to #2415 because configurable granularity determines whether actor-level identifiers appear in a dataset instance.

PII is orthogonal to granularity, but finer-grain dataset instances can materially increase privacy exposure. Actor identifiers can be personal data even when they are opaque or pseudonymized, because they may still be resolvable through a separate identity system.

The granularity mechanism should not attempt to define a full privacy compliance regime. That contract remains between the provider, practitioner, customer, and applicable legal/privacy policies. However, the granularity mechanism should make privacy-sensitive configurations explicit enough that practitioners understand what they are opting into.

Recommended direction:

* FOCUS dataset granularity configuration documentation should identify granularity configurations that may include actor-level or privacy-sensitive identifiers.
* FOCUS dataset granularity configuration documentation should identify the columns that may contain privacy-sensitive values within those configurations.
* Actor columns such as `ConsumerId` and `PrincipalId` should keep their own column-level privacy notes and, if accepted by the task force, plain-text PII requirements.
* The opt-in concept should be framed as an intentional configuration step partly because high-cardinality actor-grain data can materially increase both dataset size and privacy exposure.

Open requirement-level question:

* Documentation of privacy-sensitive configurations might warrant a `SHOULD` because privacy classification can be context-specific and jurisdiction-specific. A `MUST` may be defensible if it only requires documenting that a configuration may include actor-level identifiers, not classifying those values under a specific privacy law.

## Recommended PR Shape

### Preferred Option: Extend Dataset Configuration

This is the most conservative fit with current spec architecture.

Files likely changed:

* `specification/attributes/dataset_configuration.md`
* `specification/attributes/attributes_overview.md` if the description changes materially
* `specification/requirements_model/releases/1.4/model_rules/attributes/datasetconfiguration.json` for machine-readable requirements
* `specification/datasets/cost_and_usage/dataset.md` only if a specific CostAndUsage requirement is needed
* `supporting_content/attributes/dataset_configuration.md` for design rationale, scoped examples, and deferred metadata details

The PR should explain that it expands the existing `DatasetConfiguration` attribute from column selection only to column selection plus granularity configuration.

Draft concept:

* `DatasetConfiguration` covers user-defined selection of columns and granularity configurations.
* Dataset instance granularities identify the levels of detail represented by records.
* A granularity configuration specifies the level of detail for an applicability scope, including an applicability filter and granularity-defining columns.
* Granularity configurations can use applicability filters that match a service or a narrower subset of records within a service.
* Applicability filters for configured granularities within the same delivered dataset instance should be mutually exclusive.
* Documentation must explain whether delivered dataset instances replace or supplement one another for the same underlying usage or charges.
* A default granularity configuration can be offered for an applicability filter, but it should be the least granular configuration for that applicability filter.

### Alternative Option: New Dataset Granularity Configuration Attribute

Use this if maintainers do not want to expand `DatasetConfiguration`.

Possible file:

* `specification/attributes/dataset_granularity_configuration.md`

Possible Attribute ID:

* `DatasetGranularityConfiguration`

This separates the concept cleanly but creates a second configuration-oriented attribute that overlaps with `DatasetConfiguration`. If chosen, the PR should explicitly state how the two attributes differ:

* `DatasetConfiguration`: column selection.
* `DatasetGranularityConfiguration`: record grain / scoped granularity configuration.

### Avoid: Column Content Constraint Field

Avoid adding `Delivery grain | Opt-in` to individual columns unless the group wants to modify the column definition format across the spec. It does not solve the scoped and multi-level detail cases.

## Suggested Normative Direction

Do not copy this text directly without editorial review, but this is the shape that appears most aligned with current requirements style:

```markdown
Dataset conforming to DatasetConfiguration attribute MUST adhere to the following requirements:

* *FOCUS dataset* MUST be configurable to include only a user-defined selection of columns.
* *FOCUS dataset* MUST be configurable to select a granularity configuration for each applicability filter when more than one granularity configuration is offered for that applicability filter.
* *FOCUS dataset* MUST adhere to all column-level specifications defined in the FOCUS schema, regardless of the selected or default configuration (e.g., column selection, granularity configuration).
* *FOCUS dataset* MUST have mutually exclusive applicability filters for granularity configurations within a delivered dataset instance.
* *FOCUS dataset* granularity configuration documentation MUST adhere to the following requirements when a delivered dataset instance uses one or more granularity configurations:
  * *FOCUS dataset* granularity configuration documentation MUST identify the columns that define the granularity configuration.
  * *FOCUS dataset* granularity configuration documentation MUST identify the applicability filter for the granularity configuration (e.g., ServiceName).
  * *FOCUS dataset* granularity configuration documentation SHOULD identify the representation of more granular detail for the granularity configuration (e.g., expanded records, embedded JSON objects, referenced detail datasets).
  * *FOCUS dataset* granularity configuration documentation MUST describe whether a delivered dataset instance replaces or supplements other delivered dataset instances that represent the same underlying usage or charges.
  * *FOCUS dataset* granularity configuration documentation MUST describe how summable metrics are represented across delivered dataset instances when one delivered dataset instance supplements another delivered dataset instance that represents the same underlying usage or charges.
  * *FOCUS dataset* granularity configuration documentation SHOULD describe how non-summable metrics (e.g., ListUnitPrice, ContractedUnitPrice) are represented across delivered dataset instances that represent the same underlying usage or charges.
  * *FOCUS dataset* granularity configuration documentation SHOULD identify granularity configurations that include privacy-sensitive identifiers (e.g., actor-level identifiers).
* *FOCUS dataset* MAY offer a default granularity configuration for an applicability filter.
* *FOCUS dataset* granularity configuration MUST be the least granular granularity configuration offered for the same applicability filter (e.g., the granularity configuration with the fewest granularity-defining columns) when the granularity configuration is offered as a default.
* *FOCUS dataset* MAY offer a default column set.
* *FOCUS dataset* default column set MUST include all applicable *FOCUS columns* when a default column set is offered.
```

Open editorial questions:

* "FOCUS dataset granularity configuration documentation" is probably a better normative subject than "Dataset configuration documentation" because it avoids implying that the provider must publish a full catalog of configuration choices.
* "User-defined" may not be right for provider-managed scoped detail options. "Configured" might be better.
* "Applicability boundaries" needs glossary review if it becomes a formal term.

## How This Supports PrincipalId and ConsumerId

`PrincipalId` and `ConsumerId` should be stable reusable columns.

The actor column PR should not say the practitioner opts into the columns themselves. It should say the CostAndUsage dataset includes those columns when:

* the operating model includes principal or consumer attribution; and
* the granularity configuration includes principal or consumer attribution.

For future higher-cardinality actor dimensions, such as `SessionId`, `TraceId`, `RequestId`, or `ExecutionId`, the same mechanism can apply without changing `ConsumerId` semantics.

Do not pack session or trace identifiers into `ConsumerId`. That would make the column do too many jobs and would prevent clean grouping at the actual consumer level.

## Example Model

A FOCUS Cost and Usage implementation could offer these granularity configurations:

| Configuration | Applicability | Grain-defining dimensions |
| :--- | :--- | :--- |
| Standard Cost and Usage | All services | Existing default CostAndUsage dimensions |
| Service-A principal attribution | Service-A API-based usage | Standard dimensions plus `PrincipalId` |
| Service-A consumer attribution | Service-A customer-supplied actor metadata | Standard dimensions plus `PrincipalId`, `ConsumerId` |
| Service-A session attribution | Service-A request telemetry | Standard dimensions plus `PrincipalId`, `ConsumerId`, future `SessionId` |
| Kubernetes workload attribution | EKS or Kubernetes usage | Standard dimensions plus relevant workload/pod/namespace custom or future FOCUS columns |

Customers could opt into Service-A consumer attribution but not Service-B workload attribution because the configuration is scoped by applicability, not by a single global column flag.

## Open Questions For PR Description

* Should `DatasetConfiguration` be expanded, or should a new `DatasetGranularityConfiguration` attribute be introduced?
* Should the actor attribution conditions be renamed from `IncludesPrincipals` / `IncludesConsumers` to attribution-specific conditions?
* Should the first PR define only documentation requirements, or also add metadata schema fields for granularity configuration?
* How should supplemental dataset instances be described to prevent double-counting?
* Should split cost allocation be explicitly cross-referenced as the required mechanism only when a more granular configuration apportions a shared origin charge?
* Should privacy-sensitive granularity documentation be a `MUST` or `SHOULD`, given that privacy classification can depend on customer context and jurisdiction?
* Should `granularity representation mode` be the right term, or should the PR use `granularity delivery mode`, `granular detail representation`, or another term?
* Should the representation mode values be `Expanded`, `Embedded`, and `Referenced`, or should the PR use plainer labels such as `Inline`, `Split`, and `Detail`?
* Should deep actor/session/trace detail remain inside CostAndUsage as expanded, higher-row-count dataset instances, be embedded as JSON, or be modeled as a referenced supporting dataset/file with a one-to-many relationship to CostAndUsage records?
* What join key or lineage mechanism would be needed if a supporting detail dataset/file is used?
* Should one-to-many actor/session/trace detail be modeled as a JSON breakdown column inside CostAndUsage, and if so, should element-level metrics such as cost, quantity, or allocation ratio be required?
* If a JSON breakdown column includes element-level costs or quantities, should it inherit split cost allocation conservation rules, define new conservation rules, or be restricted to informational detail without cost metrics?
* Should applicability filters be required to be clearly non-overlapping from the filter definitions alone, without inspecting delivered records? This may be stricter than requiring non-overlap in the delivered data, but overlapping higher-granularity configurations can create exponential fanout as additional granularities are selected.
