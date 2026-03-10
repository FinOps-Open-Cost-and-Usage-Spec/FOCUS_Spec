## Diff


* A FOCUS dataset MUST include the following columns when the data generator supports data generator-calculated split cost allocation:
  * [-[AllocatedMethodId](#allocatedmethodid)-]{+[AllocatedMethodId](#datasets.costandusage.allocatedmethodid)+}
  * [-[AllocatedResourceId](#allocatedresourceid)-]{+[AllocatedResourceId](#datasets.costandusage.allocatedresourceid)+}
  * [-[AllocatedResourceName](#allocatedresourcename)-]{+[AllocatedResourceName](#datasets.costandusage.allocatedresourcename)+}
  * [-[AllocatedResourceTags](#allocatedresourcetags)-]{+[AllocatedResourceTags](#datasets.costandusage.allocatedtags)+}
* A FOCUS dataset SHOULD include the following column when the data generator supports data generator-calculated split cost allocation:
  * [-[AllocatedMethodDetails](#allocatedmethoddetails)-]{+[AllocatedMethodDetails](#datasets.costandusage.allocatedmethoddetails)+}
* Allocated charge records in a FOCUS dataset MUST sum up to the origin charge record for all aggregatable metric columns.
* For each allocated charge records in a FOCUS dataset, all dimension columns and non-aggregatable metric columns MUST match the values of the origin charge record.
* Allocated charge records MUST include the same keys and values present in the [-[Tags](#tags)-]{+[Tags](#datasets.costandusage.tags)+} column for the origin charge.
* Allocated charge records MUST satisfy normative requirements for all columns.
* The method used for allocating origin charges to create allocated charges MUST be documented by the data generator and accessible to practitioners.
* A FOCUS dataset MAY contain records for concepts not related to resource usage, if documented in the split cost allocation method.
* A FOCUS dataset MAY contain records for the unused or unallocated usage from the origin charge as separate allocated charges, if it aligns to the data generator's documented allocation method.
* Allocated charge records MAY contain apportioned costs for the unused or unallocated usage from the origin charge, if it aligns to the data generator's documented allocation method.
* Split cost allocation [-is RECOMMENDED to-]{+SHOULD+} be applied to charges on an opt-in basis.



