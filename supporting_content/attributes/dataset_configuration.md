# Dataset Configuration

## Deferred Requirements

The following requirements were developed as part of the Dataset Configuration attribute but deferred from the initial specification to keep the scope focused on column selection (#1091). These are expected to be integrated as normative requirements in a separate change.

### Row aggregation

* A FOCUS dataset SHOULD sum metric columns by default when the selected dimension columns result in rows with identical values.
* A FOCUS dataset SHOULD allow opting in or out of row aggregation (summing metrics).
  * A FOCUS dataset MUST sum metric column values when rows are aggregated.
  * A FOCUS dataset SHOULD use case-insensitive matching when aggregating rows.

### Time granularity

* A FOCUS dataset MUST allow selecting the time granularity based on ChargePeriodStart, when available.
  * A FOCUS dataset MUST allow selecting daily granularity.
  * A FOCUS dataset MUST allow selecting hourly granularity when the dataset includes costs priced at an hourly or lower grain.
  * A FOCUS dataset SHOULD allow selecting monthly granularity.
  * A FOCUS dataset MUST sum metric columns based on selected dimension columns with identical values when time granularity is changed.

### FOCUS version selection

* A FOCUS dataset SHOULD allow selecting the FOCUS version.
  * A FOCUS dataset MUST NOT add or remove columns when a specific FOCUS version is selected.

### Row filtering

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
| **DatasetConfiguration** | Column selection, row aggregation, time granularity, schema versioning, row filtering | None (all datasets) |
| **DatasetDelivery** | Scheduling, incremental refresh, overwrite vs append, partitioning | Files or Tables |
| **DatasetFileHandling** | File format, compression | Files only |

### Current Scope (1.4)

| Option            | Status | Description                                         |
|-------------------|--------|-----------------------------------------------------|
| Column selection  | 1.4    | Choose which columns to include                     |
| Row aggregation   | 1.4    | Sum metric columns when dimensions are identical    |
| Time granularity  | 1.4    | Choose temporal resolution (daily, monthly, hourly) |
| Schema versioning | 1.4    | Select which schema version to use                  |
| Row filtering     | 1.4    | Filter rows by column values                        |

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

- **Data transformation**: Pivoting or reshaping data changes what the data IS, not how it's made available
- **Access control**: Authentication and authorization are security concerns outside FOCUS scope

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

- Standardized reporting across providers
- Simplified data pipelines
- Initial FOCUS adoption

#### Cost Allocation

Select columns needed for cost allocation workflows:

- BilledCost, EffectiveCost, ContractedCost, ListCost
- BillingAccountId, SubAccountId
- Tags, ResourceId, ResourceName
- ServiceName, ServiceCategory

#### Commitment Analysis

Select columns for commitment optimization:

- CommitmentDiscountId, CommitmentDiscountStatus, CommitmentDiscountType
- CommitmentDiscountQuantity, CommitmentDiscountUnit
- EffectiveCost, BilledCost
- ResourceId, ResourceType

## Row Aggregation

When practitioners select fewer columns, the resulting dataset may contain duplicate rows (rows with identical dimension values). Row aggregation sums metric columns to produce a more efficient dataset.

### Why Aggregate by Default

Returning duplicate rows provides no value to practitioners:

- **Storage waste**: 1 million rows with identical dimension values wastes storage
- **Processing cost**: Practitioners must aggregate the data themselves anyway
- **No data loss**: Summing metrics is mathematically correct; no information is lost

FOCUS recommends aggregation by default because it produces smaller, more efficient datasets without sacrificing accuracy.

### Opting Out of Aggregation

Some practitioners may need unaggregated data for specific use cases:

- Auditing individual charge records
- Debugging data quality issues
- Matching to source system records

Providers should allow practitioners to opt out of aggregation when needed.

## Case Sensitivity

Case sensitivity affects both filtering and aggregation operations.

### Filtering (Case-Insensitive)

FOCUS requires case-insensitive matching when filtering rows. This is practitioner-friendly:

- Practitioners shouldn't need to know exact casing to find their data
- "prod" should match "Prod", "PROD", and "prod"
- Reduces friction and improves usability

### Aggregation (Case-Insensitive Recommended)

FOCUS recommends case-insensitive matching when aggregating rows. From a practitioner perspective, case-insensitive grouping is ideal:

- "Prod" and "prod" likely represent the same environment
- Inconsistent casing is usually a data quality issue, not intentional differentiation

However, case-insensitive aggregation presents implementation challenges:

- When "Prod" and "prod" are merged, which value should be returned?
- Different systems handle this differently (first value, alphabetical, etc.)

Due to these implementation complexities, case-insensitive aggregation is a SHOULD rather than a MUST. Providers that cannot implement case-insensitive aggregation should use case-sensitive matching and document this behavior.

## Time Granularity

Allows practitioners to choose temporal resolution:

| Granularity | Use Case                                    | Data Volume Impact           |
|-------------|---------------------------------------------|------------------------------|
| Hourly      | Real-time monitoring, anomaly detection     | ~720x more rows than monthly |
| Daily       | Standard reporting, cost allocation         | ~30x more rows than monthly  |
| Monthly     | Executive reporting, billing reconciliation | Minimum data volume          |

### Required Granularities

- **Daily**: Required (MUST) - the most common granularity for cost analysis
- **Monthly**: Recommended (SHOULD) - useful for executive reporting and billing reconciliation
- **Hourly**: Required when applicable (MUST) - when the dataset includes costs priced at an hourly or lower grain, hourly granularity must be available to preserve pricing accuracy

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

The Dataset Configuration attribute requires that FOCUS datasets include metadata describing the selected configuration options (`DatasetConfiguration-A-003-M`). This section evaluates what changes would be needed to support this requirement within the existing metadata structure.

### Current Metadata Structure

The FOCUS metadata system has four sections:

| Section              | Purpose                                        |
|----------------------|------------------------------------------------|
| **Data Generator** | Describes the entity delivering the dataset |
| **Dataset Instance** | Describes the nature of the dataset artifact |
| **Recency** | Describes the recency and completeness of data |
| **Schema** | Describes the schema of data within the artifact |

None of these sections currently capture dataset configuration selections.

### What Needs to be Tracked

Configuration metadata should describe the options applied when generating a dataset artifact:

| Configuration Option | Metadata Needed                                                |
|----------------------|----------------------------------------------------------------|
| Column selection | List of included columns (or excluded columns) |
| Row aggregation | Whether aggregation is enabled |
| Time granularity | Selected granularity (hourly, daily, monthly) |
| FOCUS version | Selected version (already captured in Schema as FocusVersion) |
| Row filtering | Applied filter criteria |

### Possible Approaches

#### Option A: Extend Dataset Instance metadata

Add a `Configuration` object to DatasetInstance containing the selected options. This is the most natural fit since DatasetInstance already describes the nature of the dataset artifact, and configuration options directly shape what the artifact contains.

#### Option B: New metadata section

Create a dedicated `Configuration` metadata section alongside Data Generator, Dataset Instance, Recency, and Schema. This provides clear separation but adds a new top-level concept.

#### Option C: Extend Schema metadata

Since Schema already tracks structural information (columns, data types) and triggers a new entry when the dataset structure changes, configuration changes could be captured alongside. However, Schema is focused on the data structure, not on what subset was selected.

### Recommendation

Option A (extending Dataset Instance) is the most natural fit. The configuration options describe how a specific dataset artifact was shaped, which aligns with Dataset Instance's purpose. FOCUS version selection is already partially addressed by Schema's `FocusVersion` property.

### Estimated Scope

This change would require:

- New metadata property definitions in `specification/metadata/dataset_instance/` (5-8 new `.md` files)
- Updates to `dataset_instance.mdpp` template
- New requirements model rules in `specification/requirements_model/model_rules/`
- Updates to `supporting_content/metadata/` for examples

This is a significant change that warrants a separate PR to keep the Dataset Configuration attribute focused on its core requirements.

## Conformance Notes

When practitioners configure their dataset:

1. **Selected columns remain conformant**: Each included column still follows all FOCUS requirements for that column, including requirements that reference columns not included in the dataset
2. **Aggregated data remains conformant**: Summed metric values are mathematically correct representations of the underlying data
3. **Dataset completeness changes**: A configured dataset may not support all analysis scenarios
4. **Filtering affects completeness**: Filtered datasets may not reconcile with invoices or support full cost allocation
