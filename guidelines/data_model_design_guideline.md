# FOCUS Data Model Design Guidelines

When considering the addition of a new dataset (or table) to the FinOps Foundation’s FOCUS specification, which currently consists of a single time-series dataset, the decision should be guided by clear principles to ensure the specification remains coherent, maintainable, and aligned with its goals. Below are some principles to guide when adding a new table is appropriate, tailored to the context of the FOCUS specification and FinOps practices:

## Distinct Purpose and Scope: 

A new table should serve a separate purpose or represent a unique data domain that cannot be effectively or logically accommodated within the existing time-series dataset.
   
### Rationale: 
The FOCUS specification aims to standardize cloud cost and usage data. A new table should address a specific FinOps use case (e.g., cost allocation, forecasting, or resource metadata) that requires different attributes, granularity, or structure than the current time-series data.
### Example: 
If the current table captures usage and cost metrics over time, a new table might be justified for static metadata (e.g. account details, or pricing rules) that isn’t time-dependent and doesn’t fit the time-series structure.

## Alignment with FinOps Use Cases:
The new table should directly support one or more core FinOps practices, such as cost allocation, optimization, forecasting, or reporting, as defined by the FinOps Foundation.
### Rationale:
The FOCUS specification is designed to enable FinOps practitioners to manage cloud costs effectively. Any new table should map to specific entity that is relevant to FinOps.
### Example:
A table for anomaly detection (e.g., unexpected cost spikes) or reserved instance utilization might be justified if it supports optimization workflows not adequately addressed by the time-series data.

## Data Granularity and Structure: 
Table should bear the responsibility of representing a specific entity or construct and its data. These entities and therefore their tables have a distinct represented granularity, structure, or lifecycle that justifies its separation from the existing time-series dataset.
### Rationale:
Different tables represent different entities and may require different datasets may require different levels of detail, update frequencies, or lifecycle. A new table may be appropriate if it captures data at a different granularity (e.g., daily vs. monthly) or has a different temporal nature (e.g., static vs. dynamic). 
### Example: 
A table representing the overtime charges for a vendor represents a charge entity. A table that represents invoices is not the same entity and therefore could be considered appropriate to add as a separate table, should invoices need to be represented as a dedicated entity.

## Interoperability and Integration: 
The new table should integrate seamlessly with the existing dataset, maintaining consistency in terminology, keys, and standards as defined by the FOCUS specification. Linkages to other tables in a primary key and foreign key nature should be identified. Uniqueness scope must be determined and adhered too.
### Rationale: 
The FOCUS specification emphasizes interoperability across cloud providers and tools. A new table should use consistent identifiers (e.g., resource IDs, billing account IDs) and align with the specification’s data model to ensure it can be joined or correlated with the existing table.
### Example: 
A new table for vendor-specific pricing data should include standardized keys to link it to the time-series usage data, enabling cross-referencing for cost analysis.

## Scalability and Maintainability: 
The addition of a new table should not overly complicate facilitating supported features, substantially increase query complexity, or create significant maintenance burdens for implementers.
### Rationale:
Adding tables increases the complexity of data ingestion, validation, and processing for FinOps tools and teams. A table should be justified by its value and designed to minimize overhead (e.g., clear schema, minimal dependencies).
### Example: 
While we could add a tags table that is an overtime history of all relevant tags for a resource the usability as it relates to tracking cost and usage

## Consistency and Conflicting Data:
Tables should provide a clear and consistent view of data without conflicting information. If a new table introduces potential conflicts with existing data, it should be avoided or designed to resolve those conflicts. Tables with linked logic such as over time charges in one and aggregated summations in another table should tie out. 
### Rationale:
FinOps practitioners rely on FOCUS datasets as sources of truth, should two tables provide the same data, there is a risk of introducing inconsistencies or confusion. A new table should not contradict existing data unless it provides a clear resolution or additional context.
### Example:
A summary table for executive dashboards might be justified if it reduces query times for high-level cost reports compared to querying the detailed time-series data.

## Avoid Redundancy:
The new table must not duplicate data or functionality already available in the existing dataset unless it provides significant value through a different perspective or aggregation.
### Rationale:
Redundant tables increase complexity, maintenance overhead, and the risk of inconsistencies. Ensure the new table adds unique value, such as summarizing data for specific analyses (e.g., aggregated spend by business unit) or capturing data not feasible in the current schema.

### Example: Instead of adding a table that repeats time-series cost data, consider whether the existing table can be extended with new columns or whether the new table addresses a fundamentally different need, like contract or licensing data.

## Future-Proofing and Flexibility:
The addition of a table can be done when needed to accommodate both current and future supported features or data model needs.
### Rationale:
Cloud environments evolve rapidly, and the FOCUS specification must remain adaptable. A new table should be flexible enough to handle foreseeable changes without requiring frequent restructuring.
### Example:
A table for multi-cloud or hybrid cloud cost data might be added to support organizations using multiple providers, with a schema that can adapt to new cloud services.

## Compliance with FOCUS Design Goals: 
The new table must align with the FOCUS specification’s core design goals, such as simplicity (wink), consistency, and vendor neutrality.
### Rationale: 
The FOCUS specification aims “‘to create a standardized schema for cloud billing and usage data’” (paraphrased from the FinOps Foundation’s FOCUS mission). Any new table should adhere to these principles to maintain the specification’s integrity.
### Example: 
A new table for usage metadata should use vendor-neutral terminology and avoid provider-specific fields that could fragment the standard.

