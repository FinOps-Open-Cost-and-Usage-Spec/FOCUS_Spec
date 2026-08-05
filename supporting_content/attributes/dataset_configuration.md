# Dataset Configuration

## Deferred Requirements

The following requirements were developed as part of the Dataset Configuration attribute but deferred from the initial specification to keep the scope focused on column selection (#1091). These may be integrated as normative requirements in a separate change.

### Row Aggregation

The Dataset Configuration requirements establish a default expectation that duplicate records are aggregated after the delivered detail is determined. The ability to select an alternative aggregation behavior remains deferred.

* A FOCUS dataset SHOULD allow opting in or out of row aggregation (summing metrics).
  * A FOCUS dataset MUST sum metric column values when rows are aggregated.
  * A FOCUS dataset SHOULD use case-insensitive matching when aggregating rows.

### Time Granularity

* A FOCUS dataset MUST allow selecting the time granularity based on ChargePeriodStart, when available.
  * A FOCUS dataset MUST allow selecting daily granularity.
  * A FOCUS dataset MUST allow selecting hourly granularity when the dataset includes costs priced at an hourly or lower grain.
  * A FOCUS dataset SHOULD allow selecting monthly granularity.
  * A FOCUS dataset MUST sum metric columns based on selected dimension columns with identical values when time granularity is changed.

### FOCUS Version Selection

* A FOCUS dataset SHOULD allow selecting the FOCUS version.
  * A FOCUS dataset MUST NOT add or remove columns when a specific FOCUS version is selected.

### Row Filtering

* A FOCUS dataset SHOULD allow filtering rows by column values.
  * A FOCUS dataset MUST use case-insensitive matching when filtering rows.

## Dataset Access Mechanisms

FOCUS datasets can be made available through various mechanisms:

| Mechanism       | Description                                                                    |
|-----------------|--------------------------------------------------------------------------------|
| API             | Programmatic access to cost data through REST or GraphQL endpoints             |
| Data export     | Scheduled or on-demand export to storage accounts, data lakes, or file systems |
| Database        | Direct access to tables in a data warehouse or database system                 |
| Query interface | Interactive query tools or consoles for ad-hoc analysis                        |
| Application     | Reports, dashboards, and other application experiences                         |

The Dataset Configuration attribute requirements apply regardless of how the dataset is accessed.

## Configuration Options

Dataset Configuration encompasses practitioner choices about how FOCUS data is made available. Options are organized by the delivery medium they apply to, following a pattern similar to how columns have feature levels based on provider capabilities.

### Delivery Mediums

FOCUS datasets can be delivered through different mediums:

| Medium | Examples |
|--------|----------|
| **Files** | S3 exports, file downloads, API file responses |
| **Tables** | Database tables, BigQuery, data warehouse |
| **UX** | Dashboards, reports, cost management portals |

### Applicability by Medium

| Option | Files | Tables | UX |
|--------|:-----:|:------:|:--:|
| **All Mediums** | | | |
| Column selection | ✓ | ✓ | ✓ |
| Row aggregation | ✓ | ✓ | ✓ |
| Time granularity | ✓ | ✓ | ✓ |
| Schema versioning | ✓ | ✓ | ✓ |
| Row filtering | ✓ | ✓ | ✓ |
| **Files + Tables** | | | |
| Partitioning | ✓ | ✓ | - |
| Incremental refresh | ✓ | ✓ | - |
| Overwrite vs append | ✓ | ✓ | - |
| Scheduling | ✓ | ✓ | - |
| **Files Only** | | | |
| File format | ✓ | - | - |
| Compression | ✓ | - | - |

### Future Attribute Organization

Based on applicability, configuration options may be split into separate attributes in future versions:

| Attribute | Options | Feature Level |
|-----------|---------|---------------|
| **DatasetConfiguration** | Column selection, scoped detail configuration, row aggregation, time granularity, schema versioning, row filtering | None (all datasets) |
| **DatasetDelivery** | Scheduling, incremental refresh, overwrite vs append, partitioning | Files or Tables |
| **DatasetFileHandling** | File format, compression | Files only |

### Developed for 1.4

The following options were developed for the Dataset Configuration attribute. Column selection is included in the initial specification. The remaining options are deferred to a separate change.

| Option            | Status   | Description                                         |
|-------------------|----------|-----------------------------------------------------|
| Column selection  | Included | Choose which columns to include                     |
| Row aggregation   | Deferred | Sum metric columns when dimensions are identical    |
| Time granularity  | Deferred | Choose temporal resolution (daily, monthly, hourly) |
| Schema versioning | Deferred | Select which schema version to use                  |
| Row filtering     | Deferred | Filter rows by column values                        |

### Developed for 1.5

The following options were developed for the Dataset Configuration attribute for 1.5.

| Option                     | Status   | Description                                                      |
|----------------------------|----------|------------------------------------------------------------------|
| Scoped detail configuration | Included | Select optional detail for documented data coverage |

### Future Options

| Option              | Attribute           | Description                                         |
|---------------------|---------------------|-----------------------------------------------------|
| Partitioning        | DatasetDelivery     | Choose how data is partitioned (by date, account)   |
| Scheduling          | DatasetDelivery     | Configure delivery frequency (hourly, daily)        |
| Incremental refresh | DatasetDelivery     | Receive only changed/new data vs. full refresh      |
| Overwrite vs append | DatasetDelivery     | New data overwrites or appends to existing          |
| File format         | DatasetFileHandling | Choose output format (Parquet, CSV, JSON)           |
| Compression         | DatasetFileHandling | Choose compression method (gzip, snappy, none)      |

### What Doesn't Fit

Some capabilities are outside the scope of Dataset Configuration attributes:

* **Data transformation**: Pivoting or reshaping data changes what the data IS, not how it's made available
* **Access control**: Authentication and authorization are security concerns outside FOCUS scope

## Column Selection

### When Column Selection Matters

Column selection is valuable when:

| Scenario            | Example                                                                                     |
|---------------------|---------------------------------------------------------------------------------------------|
| Large datasets      | AWS CUR includes over 200 columns                                                           |
| Static columns      | Some FOCUS columns have a single value for a provider (e.g., BillingAccountType)            |
| Large columns       | Some columns may contain significant data (e.g., JSON columns with detailed metadata)       |
| Scoped analysis     | Practitioners ingesting data for specific workflows only need relevant columns              |
| Non-technical users | Spreadsheet users may need summarized views with key columns due to row/column limits       |
| Cost optimization   | Reducing columns decreases storage costs and data transfer time                             |

### Common Selection Patterns

#### FOCUS-Only

Select only FOCUS standard columns, excluding all custom (x_) columns. Useful for:

* Standardized reporting across providers
* Simplified data pipelines
* Initial FOCUS adoption

#### Cost Allocation

Select columns needed for cost allocation workflows:

* BilledCost, EffectiveCost, ContractedCost, ListCost
* BillingAccountId, SubAccountId
* Tags, ResourceId, ResourceName
* ServiceName, ServiceCategory

#### Commitment Analysis

Select columns for commitment optimization:

* CommitmentDiscountId, CommitmentDiscountStatus, CommitmentDiscountType
* CommitmentDiscountQuantity, CommitmentDiscountUnit
* EffectiveCost, BilledCost
* ResourceId, ResourceType

## Row Aggregation

When practitioners select fewer columns, the resulting dataset may contain duplicate rows (rows with identical dimension values). Row aggregation sums metric columns to produce a more efficient dataset.

### Why Aggregate by Default

Returning duplicate rows provides no value to practitioners:

* **Storage waste**: 1 million rows with identical dimension values wastes storage
* **Processing cost**: Practitioners must aggregate the data themselves anyway
* **No data loss**: Summing metrics is mathematically correct; no information is lost

FOCUS recommends aggregation by default because it produces smaller, more efficient datasets without sacrificing accuracy.

### Opting Out of Aggregation

Some practitioners may need unaggregated data for specific use cases:

* Auditing individual charge records
* Debugging data quality issues
* Matching to source system records

Providers should allow practitioners to opt out of aggregation when needed.

## Case Sensitivity

Case sensitivity affects both filtering and aggregation operations.

### Filtering (Case-Insensitive)

When row filtering is introduced, FOCUS will require case-insensitive matching. This is practitioner-friendly:

* Practitioners shouldn't need to know exact casing to find their data
* "prod" should match "Prod", "PROD", and "prod"
* Reduces friction and improves usability

### Aggregation (Case-Insensitive Recommended)

When row aggregation is introduced, FOCUS will recommend case-insensitive matching. From a practitioner perspective, case-insensitive grouping is ideal:

* "Prod" and "prod" likely represent the same environment
* Inconsistent casing is usually a data quality issue, not intentional differentiation

However, case-insensitive aggregation presents implementation challenges:

* When "Prod" and "prod" are merged, which value should be returned?
* Different systems handle this differently (first value, alphabetical, etc.)

Due to these implementation complexities, case-insensitive aggregation will be a SHOULD rather than a MUST. Providers that cannot implement case-insensitive aggregation should use case-sensitive matching and document this behavior.

## Time Granularity (Deferred)

When introduced, time granularity will allow practitioners to choose temporal resolution:

| Granularity | Use Case                                    | Data Volume Impact           |
|-------------|---------------------------------------------|------------------------------|
| Hourly      | Real-time monitoring, anomaly detection     | ~720x more rows than monthly |
| Daily       | Standard reporting, cost allocation         | ~30x more rows than monthly  |
| Monthly     | Executive reporting, billing reconciliation | Minimum data volume          |

### Planned Granularity Requirements

* **Daily**: Will be required (MUST) - the most common granularity for cost analysis
* **Monthly**: Will be recommended (SHOULD) - useful for executive reporting and billing reconciliation
* **Hourly**: Will be required when applicable (MUST) - when the dataset includes costs priced at an hourly or lower grain, hourly granularity will need to be available to preserve pricing accuracy

## Scoped Detail Configuration

Scoped detail configuration allows practitioners to include optional detail for documented areas of cost data. Data generators often omit high-cardinality or privacy-sensitive columns from a default dataset. When such data is available, the data generator documents the data coverage and the columns that are populated, then the practitioner elects to include that detail.

The requirements define the resulting dataset and the documentation needed to assess it. They deliberately do not define a request payload, property name, or transport mechanism. A provider can expose the selection through an API parameter, an export setting, a query interface, or another access mechanism.

### Detail Scopes and Data Coverage

A detail scope is a documented area of a FOCUS dataset for which a practitioner can select an offered detail level. Its data coverage is expressed using FOCUS dimension criteria so that a practitioner can evaluate the documented coverage against the delivered data. A detail scope can apply to one service, multiple services, or records defined by non-service dimension criteria. For example, a provider might describe the coverage of an AI user-attribution detail scope as records where ServiceName is `"Example AI Service"` and ResourceType is `"ModelInference"`.

A detail scope can contain more than one offered detail level, but a configured dataset selects one detail level for that scope. Each detail level documents the columns that are populated when it is selected. Those columns can be FOCUS columns or custom columns. A custom column is appropriate when the detail is not standardized by FOCUS.

### Delivery Methods

A delivery method describes how records at a selected detail level are delivered. When a detail level can be delivered through more than one method, the practitioner can select one method either for the complete dataset or separately for each detail scope. The selection mechanism and names for delivery methods are provider-defined.

Common delivery methods include:

* **Inline**: The selected detail is included in the same dataset records as additional populated columns.
* **Replacement**: Detailed records replace the less detailed records that represent the same underlying usage or charges.
* **Separate companion artifact**: Detailed records are delivered outside the less detailed [*dataset artifact*](#glossary:dataset-artifact), such as in a provider-defined file or table.

The documentation for each method identifies its relationship to other delivered dataset artifacts or provider-defined companion artifacts that represent the same underlying usage or charges. When detail is delivered outside the corresponding FOCUS dataset artifact, the companion artifact is provider-defined unless FOCUS defines a standard dataset for that detail. The documentation identifies the column or columns used to relate the companion artifact to the corresponding less-detailed dataset artifact. This enables practitioners to determine whether records replace one another or must be combined without double-counting.

### Record Minimization

Additional detail can increase the number of records substantially. After the delivered dimensions and non-summable metrics are determined, records with identical values in those columns can be represented by one record whose summable metrics preserve the aggregate values of the represented records. This minimizes the dataset without removing the selected detail.

This aggregation guidance does not replace the aggregation guidance for individual columns. Practitioners must continue to apply the documented aggregation treatment for columns such as PricingQuantity, ListCost, and ContractedCost when calculating a use-case-specific total.

### Actor Attribution

Actor-level detail is useful for shared platforms and pass-through services where the service account that initiates usage is not the entity that should bear the cost. For example, an AI gateway service account may initiate all LLM requests while costs should be attributed to the calling team, application, or user.

A provider that natively measures usage at the actor grain can offer actor attribution as scoped detail without requiring split cost allocation. When a provider starts from a coarser [*origin charge*](#glossary:origin-charge) and distributes it across actors or workloads using an allocation method, the actor-attribution detail uses [Data Generator-Calculated Split Cost Allocation Handling](#attributes.datagenerator-calculatedsplitcostallocationhandling).

### Relationship to Split Cost Allocation

Scoped detail configuration is the broader opt-in and documentation mechanism for selecting additional detail. Data Generator-Calculated Split Cost Allocation Handling is a defined subset of that pattern for detail levels that split an origin charge into [*allocated charges*](#glossary:allocated-charge). A detail level can add scoped detail without split cost allocation when the provider already measures the underlying usage or charges at that detail level.

Detail-scope documentation identifies whether each offered detail level uses Data Generator-Calculated Split Cost Allocation Handling. This disclosure helps practitioners understand when records are allocated charges and apply the split cost allocation requirements for matching dimensions, matching non-summable metrics, and preserving the sum of summable metrics across the corresponding origin charge.

## Future Configuration Options

### Format Selection

Allows practitioners to choose output format for file-based exports:

| Format  | Pros                                   | Cons                            |
|---------|----------------------------------------|---------------------------------|
| Parquet | Columnar, compressed, fast queries     | Requires specialized tools      |
| CSV     | Universal compatibility, human-readable| Large files, slow queries       |
| JSON    | Flexible schema, web-friendly          | Verbose, poor query performance |

### Compression Options

For file-based exports, compression reduces storage and transfer costs:

| Method | Compression Ratio | Speed   | Compatibility                   |
|--------|-------------------|---------|---------------------------------|
| gzip   | High              | Slower  | Universal                       |
| snappy | Medium            | Faster  | Parquet default, big data tools |
| none   | None              | Fastest | Maximum compatibility           |

## Provider Examples

Major cloud providers support various configuration options:

| Provider  | Column Selection | Format Selection | Time Granularity | Compression |
|-----------|------------------|------------------|------------------|-------------|
| AWS       | CUR 2.0          | Parquet, CSV     | Hourly, Daily    | gzip        |
| GCP       | BigQuery queries | Parquet, CSV     | N/A (raw data)   | Various     |
| Microsoft | Limited          | CSV              | Daily            | None        |

## Configuration Metadata

The Dataset Configuration attribute requires documentation for offered scoped detail configurations, but it does not yet define structured metadata for all selected configuration options. This section evaluates what changes would be needed to support structured configuration metadata within the existing metadata structure.

### Current Metadata Structure

The FOCUS metadata system has four sections:

| Section              | Purpose                                        |
|----------------------|------------------------------------------------|
| **Data Generator** | Describes the entity delivering the dataset |
| **Dataset Instance** | Describes the nature of the dataset artifact |
| **Recency** | Describes the recency and completeness of data |
| **Schema** | Describes the schema of data within the artifact |

None of these sections currently capture dataset configuration selections.

### What Needs to Be Tracked

Configuration metadata should describe the options applied when generating a dataset artifact:

| Configuration Option | Metadata Needed                                                |
|----------------------|----------------------------------------------------------------|
| Column selection | List of included columns (or excluded columns) |
| Scoped detail configuration | Selected detail levels, documented data coverage, populated columns, split cost allocation disclosure, relationship to related dataset artifacts or provider-defined companion artifacts, and columns used to relate separately delivered detail |
| Row aggregation | Whether aggregation is enabled |
| Time granularity | Selected granularity (hourly, daily, monthly) |
| FOCUS version | Selected version (already captured in Schema as FocusVersion) |
| Row filtering | Applied filter criteria |

### Possible Approaches

#### Option A: Extend Dataset Instance Metadata

Add a `Configuration` object to DatasetInstance containing the selected options. This is the most natural fit since DatasetInstance already describes the nature of the dataset artifact, and configuration options directly shape what the artifact contains.

#### Option B: New Metadata Section

Create a dedicated `Configuration` metadata section alongside Data Generator, Dataset Instance, Recency, and Schema. This provides clear separation but adds a new top-level concept.

#### Option C: Extend Schema Metadata

Since Schema already tracks structural information (columns, data types) and triggers a new entry when the dataset structure changes, configuration changes could be captured alongside. However, Schema is focused on the data structure, not on what subset was selected.

### Recommendation

Option A (extending Dataset Instance) is the most natural fit. The configuration options describe how a specific dataset artifact was shaped, which aligns with Dataset Instance's purpose. FOCUS version selection is already partially addressed by Schema's `FocusVersion` property.

### Example Scoped Detail Metadata

The following example illustrates one possible shape for recording selected scoped detail in dataset instance metadata. The field names are illustrative and would need task force review before becoming part of the formal metadata schema.

```json
{
  "DatasetInstanceId": "178151-dbad145e-178151-dbad145e-178151",
  "Configuration": {
    "ScopedDetail": [
      {
        "DataCoverage": {
          "ServiceName": "Example AI Service",
          "ResourceType": "ModelInference"
        },
        "DetailLevel": "user"
      }
    ]
  }
}
```

### Estimated Scope

This change would require:

* New metadata property definitions in `specification/metadata/dataset_instance/` (5-8 new `.md` files)
* Updates to `dataset_instance.mdpp` template
* New requirements model rules in `specification/requirements_model/model_rules/`
* Updates to `supporting_content/metadata/` for examples

This is a significant change that warrants a separate PR to keep the Dataset Configuration attribute focused on its core requirements.

## Conformance Notes

When practitioners configure their dataset:

1. **Selected columns remain conformant**: Each included column still follows all FOCUS requirements for that column, including requirements that reference columns not included in the dataset
2. **Dataset completeness changes**: A configured dataset may not support all analysis scenarios

When deferred features (row aggregation, row filtering) are introduced:

1. **Aggregated data remains conformant**: Summed metric values are mathematically correct representations of the underlying data
2. **Filtering affects completeness**: Filtered datasets may not reconcile with invoices or support full cost allocation
