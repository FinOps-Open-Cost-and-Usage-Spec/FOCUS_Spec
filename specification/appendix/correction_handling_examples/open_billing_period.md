# Corrections within Open Billing Period

The following examples illustrate how corrections within open billing periods, including both current and previous uninvoiced periods, may be represented in FOCUS Cost and Usage datasets, using various delivery mechanisms and correction styles.

## Scenario 1: Intra-period Correction - Partial Reallocation to Correct Resource

During the current open billing period, the Data Generator identifies that a charge record attributed entirely to ResourceId R-111 was misallocated. In reality, only part of the cost and usage belongs to R-111, while the remainder pertains to ResourceId R-222.

Since the billing period is still open and the invoice has not yet been finalized, the correction can be applied within the same billing period, allowing for more flexible correction mechanisms. The correction may be modeled using one of the following approaches:

* Replacement-style correction, which directly updates or replaces the original record.
* Ledger-style correction, using increment and decrement records.
* Accounting-style correction, using negation and corrected records.

CSV Examples:

* [Original Dataset](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=1014183943#gid=1014183943)
* [Replacement Dataset](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=1014183943#gid=1014183943)
* [Ledger-style Append-only Dataset](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=1014183943#gid=1014183943)
* [Accounting-style Append-only Dataset](https://docs.google.com/spreadsheets/d/1UDZCxPqUNEUQt90h8sW-YuhgBsk4pHYcwRlgPJVmwPo/edit?gid=1014183943#gid=1014183943)

Note the following details in the example dataset:

* **TOD:** Add notes

* Original Dataset includes:
  * A charge record attributed entirely to ResourceId R-111.
* Replacement-style correction includes:
  * A direct update to the original record, redistributing cost between R-111 and R-222.
* Ledger-style correction includes:
  * A decrement record for R-111.
  * An increment record for R-222.
* Accounting-style correction includes:
  * A negation record for the original charge.
  * A corrected record for R-111.
  * A corrected record for R-222.
  
**TODO:** Add additional Scenarios
