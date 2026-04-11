## Diff

@@ -1,18 +1,7 @@
## Requirements

[-* A FOCUS dataset-]{+Column conforming to DataGeneratorCalculatedSplitCostAllocationHandling attribute+} MUST [-include-]{+adhere to+} the following [-columns when the data generator supports data generator-calculated split cost allocation:-]
[-  * AllocatedMethodId-]
[-  * AllocatedResourceId-]
[-  * AllocatedResourceName-]
[-  * AllocatedResourceTags-]{+requirements:+}

* [-A FOCUS-]{+*FOCUS+} dataset [-SHOULD include the following column when the data generator supports data generator-calculated split cost allocation:-]
[-  * AllocatedMethodDetails-]
[-* Allocated charge records in-]{+column* representing+} a[-FOCUS dataset MUST sum up to the origin charge record for all aggregatable metric columns.-]
[-* For each allocated charge records in a FOCUS dataset, all-] dimension[-columns and non-aggregatable metric columns-] MUST match the [-values of-]{+corresponding value in+} the [-origin charge record.-]{+*origin charge* when present in an *allocated charge*.+}
* [-Allocated charge records-]{+*FOCUS dataset column* representing a non-summable *metric* (e.g., unit prices)+} MUST [-include-]{+match+} the [-same keys and values present-]{+corresponding value+} in the [-Tags column for the origin charge.-]
[-* Allocated charge records MUST satisfy normative requirements for all columns.-]{+*origin charge* when present in an *allocated charge*.+}
* The [-method used for allocating origin charges to create allocated charges-]{+sum of *FOCUS dataset column* across *allocated charges*+} MUST [-be documented by-]{+match+} the [-data generator and accessible to practitioners.-]
[-* A FOCUS-]{+*FOCUS+} dataset [-MAY contain records for concepts not related to resource usage, if documented-]{+column*+} in the [-split cost allocation method.-]
[-* A FOCUS dataset MAY contain records for the unused or unallocated usage from the origin charge as separate allocated charges, if it aligns to-]{+corresponding *origin charge* when+} the [-data generator's documented allocation method.-]
[-* Allocated charge records MAY contain apportioned-]{+*FOCUS dataset column* represents a summable metric (e.g.,+} costs [-for the unused or unallocated usage from the origin charge, if it aligns to the data generator's documented allocation method.-]
[-* Split cost allocation is RECOMMENDED to be applied to charges on an opt-in basis.-]{+and quantities).+}
