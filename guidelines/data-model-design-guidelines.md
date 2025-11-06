# FOCUS Data Model Design Guidelines

When considering the addition of a new dataset to the FinOps Foundation’s FOCUS specification, the decision should be guided by clear principles to ensure the specification remains coherent, maintainable, and aligned with its goals. Below are some principles to guide when adding a new dataset is appropriate, tailored to the context of the FOCUS specification and FinOps practices. 

## Distinct Purpose and Scope

A dataset should represent a specific entity/s and unique data domain that cannot be effectively or logically accommodated in other Datasets. Datasets exist as stand alone entities.  
   
### Rationale

Everything has a place and everything in its place. Datasets should represent distinct entities or constructs that have their own data, metadata, lifecycle, granularity, and data structure. 

### Example

If a supported feature is added to show invoices and their associated data, a new dataset might be justified to capture invoice information (e.g., invoice number, date, total amount, payment status, finalization status). Because this data is not in alignment with the charge records in the current FOCUS dataset, a new dataset would be appropriate to capture this information.

## Alignment with FOCUS Supported Features

The new dataset should directly support one or more core FOCUS [*Supported Features*](#Supported Features). These supported features are guided by the [FinOps Framework](https://www.finops.org/framework/).

### Rationale

The FOCUS specification is designed to enable FinOps practitioners to manage cloud costs effectively. Any new dataset should map to FOCUS Supported Features. These features are driven by the [FinOps Framework](https://www.finops.org/framework/). 

### Example

A dataset for anomaly detection (e.g., unexpected cost spikes) or reserved instance utilization might be justified if it supports optimization workflows not adequately addressed by the FOCUS Cost and Usage dataset.

## Data Granularity and Structure

Datasets should bear the responsibility of representing a specific entity or construct and its data. These entities and therefore their datasets have a distinct represented granularity, structure, or lifecycle that justifies its separation from the FOCUS Cost and Usage dataset.

### Rationale

Different datasets represent different entities and may require different levels of detail, update frequencies, or lifecycle. A new dataset may be appropriate if it captures data at a different granularity (e.g., daily vs. monthly) or has a different temporal nature (e.g., static vs. dynamic). 

### Example

A dataset representing the overtime charges for a vendor represents a charge entity. A dataset that represents invoices is not the same entity and therefore could be considered appropriate to add as a separate dataset, should invoices need to be represented as a dedicated entity.

## Interoperability and Integration

Datasets should integrate with one another, maintaining consistency in terminology, keys, and standards as defined by the FOCUS specification. Linkages to other datasets in a [primary key](https://en.wikipedia.org/wiki/Primary_key) and [foreign key](https://en.wikipedia.org/wiki/Foreign_key) nature should be identified. Uniqueness scope must be determined and adhered to.

### Rationale

The FOCUS specification emphasizes interoperability across cloud providers and tools. A new dataset should use consistent identifiers (e.g., resource IDs, billing account IDs) and align with the specification’s data model to ensure it can be joined or correlated with the FOCUS Cost and Usage dataset.

### Example

A new dataset for vendor-specific pricing data should include standardized keys to link it to the FOCUS Cost and Usage dataset, enabling cross-referencing for cost analysis.

## Scalability and Maintainability

The addition of a new dataset should not overly complicate facilitating supported features, substantially increase query complexity, or create significant maintenance burdens for implementers. This is not to say that the introduction of a new dataset shouldn't cause impact to existing implementations, but rather that the impact should be manageable and justified by the value it provides.

### Rationale

Adding datasets increases the complexity of data ingestion, validation, and processing for FinOps tools and teams. A dataset should be justified by its value and designed to minimize overhead (e.g., clear schema, minimal dependencies).

### Example

While we could add a tags dataset that provides an overtime history of all tags for resources, the addition of this dataset as a replacement for the tags column in the current FOCUS datasets would be problematic as it would unnecessarily increase query complexity.

## Consistency and Conflicting Data

Datasets must provide a clear and consistent view of data without conflicting information. If a new dataset introduces potential conflicts with existing datasets, it should be avoided or designed to resolve those conflicts. Datasets with related logic, such as charges over time in one and aggregated sums in another, should reconcile with each other. 

### Rationale

FinOps practitioners rely on FOCUS datasets as sources of truth. Should two datasets provide the same data, there is a risk of introducing inconsistencies or confusion. A new dataset should not contradict existing data unless it provides a clear resolution or additional context.

### Example

A summary dataset for executive dashboards might be justified if it reduces query times for high-level cost reports compared to querying the higly detailed FOCUS Cost and Usage dataset.

## Avoid Redundancy

The new dataset must not duplicate data or functionality already available in the existing datasets unless it provides significant value through a different perspective or aggregation.

### Rationale

Redundant datasets increase complexity, maintenance overhead, and the risk of inconsistencies. Ensure the new dataset adds unique value, such as summarizing data for specific analyses (e.g., aggregated spend by business unit) or capturing data not feasible in the current schema.

### Example

Instead of adding a dataset that repeats data in the FOCUS Cost and Usage dataset, consider whether the existing datasets can be extended with new columns or whether the new dataset addresses a fundamentally different need, like contract or licensing data.

## Future-Proofing and Flexibility

A new dataset must accommodate current supported features and should facilitate future supported features or data model needs.

### Rationale

Cloud environments evolve rapidly, and the FOCUS specification must remain adaptable. A new dataset should be flexible enough to handle foreseeable changes without requiring frequent restructuring.

### Example

We are considering adding a dataset for contract information. The first implementation of this dataset in the spec may begin with basic contract metadata (e.g., contract ID, start date, end date). However, it should be designed to accommodate future fields like contract terms, renewal options, or pricing tiers without requiring a complete overhaul of the dataset structure.

## Compliance with FOCUS Design Goals

The new dataset must align with the FOCUS specification’s [core design goals](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/multiple_dataset_principles/specification/overview.md#design-principles), such as simplicity (wink), consistency, and vendor neutrality.

### Rationale

The FOCUS specification aims “‘to create a standardized schema for cloud billing and usage data’” (paraphrased from the FinOps Foundation’s FOCUS mission). Any new dataset should adhere to these principles to maintain the specification’s integrity.

### Example

A new dataset for usage metadata should use vendor-neutral terminology and avoid fields specific to a given service provider or data generator that could fragment the standard.
