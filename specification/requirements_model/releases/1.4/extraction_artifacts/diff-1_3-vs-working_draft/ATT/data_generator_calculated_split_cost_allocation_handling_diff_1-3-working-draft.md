## Diff

  * AllocatedMethodId
  * AllocatedResourceId
  * AllocatedResourceName
  * [-AllocatedResourceTags-]{+AllocatedTags+}
* A FOCUS dataset SHOULD include the following column when the data generator supports data generator-calculated split cost allocation:
  * AllocatedMethodDetails
* Allocated charge records in a FOCUS dataset MUST sum up to the origin charge record for all aggregatable metric columns.
* A FOCUS dataset MAY contain records for concepts not related to resource usage, if documented in the split cost allocation method.
* A FOCUS dataset MAY contain records for the unused or unallocated usage from the origin charge as separate allocated charges, if it aligns to the data generator's documented allocation method.
* Allocated charge records MAY contain apportioned costs for the unused or unallocated usage from the origin charge, if it aligns to the data generator's documented allocation method.
* Split cost allocation [-is RECOMMENDED to-]{+SHOULD+} be applied to charges on an opt-in basis.
