# Commitment Program Eligibility Details

Commitment Program Eligibility Details identifies the [*commitment programs*](#glossary:commitment-program) that could potentially cover [*charges*](#glossary:charge), subject to [*service provider*](#glossary:service-provider) constraints. By distinguishing the pool of spend that was eligible to be covered, Commitment Program Eligibility Details provides the fundamental denominator for calculating precise commitment coverage metrics. This allows FinOps practitioners to accurately size the pool of uncovered spend that could realistically be covered by a future commitment. In this context, *commitment programs* include both discount-bearing programs (e.g., Flexible Spend Plans, Resource Reservations) and advance resource commitments (e.g., Advance Resource Commitments), provided the service provider treats them as [*commitments*](#glossary:commitment).

## Requirements

CommitmentProgramEligibilityDetails MUST adhere to the following requirements:

* CommitmentProgramEligibilityDetails MUST be of type String.
* CommitmentProgramEligibilityDetails MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* CommitmentProgramEligibilityDetails MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* CommitmentProgramEligibilityDetails MUST NOT be null when a charge is eligible for a [*commitment program*](#glossary:commitment-program), regardless of whether a [*commitment*](#glossary:commitment) was actually applied to the charge.
* CommitmentProgramEligibilityDetails MUST NOT consider transient account configurations or quotas that might temporarily prevent purchase or participation in a *commitment program*.
* CommitmentProgramEligibilityDetails MUST include all publicly available *commitment programs* for which the usage is eligible.
* CommitmentProgramEligibilityDetails SHOULD include negotiated *commitment programs* for which the usage is eligible.
* CommitmentProgramEligibilityDetails MUST NOT include data related to *commitment* [*periods*](#glossary:period) or payment options.
* CommitmentProgramEligibilityDetails MUST conform to [CommitmentProgramEligibilityDetailsObject](#datasets.costandusage.CommitmentProgramEligibilityDetails.CommitmentProgramEligibilityDetailsobject) requirements when CommitmentProgramEligibilityDetails is not null.

## Commitment Program Eligibility Details Object

Commitment Program Eligibility Details consists of a valid JSON object with a top-level property key `CommitmentPrograms` containing an array of objects describing the specific [*commitment programs*](#glossary:commitment-program) available for the usage charge.

### Object Requirements

CommitmentProgramEligibilityDetailsObject MUST adhere to the following requirements:

* CommitmentProgramEligibilityDetailsObject MUST have a top-level property key "CommitmentPrograms".
* CommitmentProgramEligibilityDetailsObject MAY contain additional data generator-defined top-level property keys.
* CommitmentProgramEligibilityDetailsObject MUST have property keys that begin with the string "x_" unless it is a FOCUS-defined property key.
* CommitmentProgramEligibilityDetailsObject.CommitmentPrograms MUST adhere to the following requirements:
  * CommitmentProgramEligibilityDetailsObject.CommitmentPrograms MUST be of type Array.
  * CommitmentProgramEligibilityDetailsObject.CommitmentPrograms MUST contain one or more objects.
  * Each entry in CommitmentProgramEligibilityDetailsObject.CommitmentPrograms MUST be of type JSON Object.
  * Each entry in CommitmentProgramEligibilityDetailsObject.CommitmentPrograms MUST have a property key "ProgramType".
  * Each entry in CommitmentProgramEligibilityDetailsObject.CommitmentPrograms MAY contain additional data generator-defined property keys.
  * Each entry in CommitmentProgramEligibilityDetailsObject.CommitmentPrograms MUST have property keys that begin with the string "x_" unless it is a FOCUS-defined property key.
  * CommitmentProgramEligibilityDetailsObject.CommitmentPrograms.ProgramType MUST be of type String.
  * CommitmentProgramEligibilityDetailsObject.CommitmentPrograms.ProgramType MUST NOT be null.
  * CommitmentProgramEligibilityDetailsObject.CommitmentPrograms.ProgramType MUST correspond to a *commitment program* type supported by the service provider (e.g., "FlexibleSpendPlan", "ResourceReservation", "BulkCapacityCredit", "AdvanceResourceCommitment").
  * CommitmentProgramEligibilityDetailsObject.CommitmentPrograms.ProgramType MUST equal [CommitmentDiscountType](#datasets.costandusage.commitmentdiscounttype) for one object in CommitmentProgramEligibilityDetailsObject.CommitmentPrograms when CommitmentDiscountType is not null.
  * CommitmentProgramEligibilityDetailsObject.CommitmentPrograms.ProgramType SHOULD correspond to terminology disclosed by the service provider in public documentation.

### Top-Level Properties

| Property             | Type  | Required | Description                                                                         |
|:----------|:----------|:----------|:---------------------------------------|
| `CommitmentPrograms` | Array | True     | Array of objects identifying *commitment programs* for which the usage is eligible. |

### Example Entries

| Key         | ValueType                            | Required | Description                                                                                                |
|:-------------|:-------------|:-------------|:------------------------------|
| ProgramType | [String](#attributes.stringhandling) | True     | The specific type of commitment program (e.g., discount or capacity reservation) available for this usage. |

### Object Example

``` json
{
  "CommitmentPrograms": [
    { "ProgramType": "FlexibleSpendPlan" },
    { "ProgramType": "ResourceReservation" },
    { "ProgramType": "AdvanceResourceCommitment" },
    { "ProgramType": "ZonalResourceCommitment" }
  ]
}
```

### JSON Type Definition

``` json
{
  "definitions": {
    "commitmentProgramEntry": {
      "properties": {
        "ProgramType": { "type": "string" }
      }
    }
  },
  "properties": {
    "CommitmentPrograms": {
      "elements": { "ref": "commitmentProgramEntry" }
    }
  }
}
```

NOTE: The above JSON Type Definition (JTD) is an approximation of the expected contents of this column, but it should not be considered normative because it cannot accurately describe the normative requirements (above) for CommitmentProgramEligibilityDetails. Where there are discrepancies, preference will be given to the normative requirements.

## Example Scenarios

The examples below are not exhaustive and may change over time. Service providers are the authoritative source for their [*commitment programs*](#glossary:commitment-program).

### Aura Web (Partially Covered Compute Usage)

Scenario: A compute usage row that is partially covered by a Flexible Spend Plan. The eligibility column still reflects all programs this usage qualifies for, regardless of current coverage.

| ServiceProviderName | ServiceName | CommitmentProgramEligibilityDetails                                                                            |
|---------------------|-------------|---------------------------------------------------------------------------------------------------------|
| Aura Web            | Compute     | {"CommitmentPrograms": [{"ProgramType": "FlexibleSpendPlan"}, {"ProgramType": "ResourceReservation"}]} |

### StackLens (Observability with Interval Spend Commitment)

Scenario: An observability platform usage row eligible for Monthly and Annual interval spend commitment pricing, offering lower effective rates than standard usage.

| ServiceProviderName | ServiceName   | CommitmentProgramEligibilityDetails                                                                                            |
|---------------------|---------------|-------------------------------------------------------------------------------------------------------------------------|
| StackLens           | Observability | {"CommitmentPrograms": [{"ProgramType": "MonthlyIntervalSpendCommitment"}, {"ProgramType": "AnnualIntervalSpendCommitment"}]} |

### LatticeScale (Ineligible Object Storage Usage)

Scenario: Standard object storage usage or a support fee, which is not eligible for any commitment program.

| ServiceProviderName | ServiceName   | CommitmentProgramEligibilityDetails |
|---------------------|---------------|------------------------------|
| LatticeScale        | ObjectStorage | null                         |

### Aura Web (Advance Resource Commitment-Eligible Compute Usage)

Scenario: A compute instance type and tenancy that are eligible for both discount-bearing programs and advance resource commitments. The eligibility column reflects all commitment constructs the usage qualifies for.

| ServiceProviderName | ServiceName | CommitmentProgramEligibilityDetails                                                                                                                                                                           |
|---------------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aura Web            | Compute     | {"CommitmentPrograms": [{"ProgramType": "FlexibleSpendPlan"}, {"ProgramType": "ResourceReservation"}, {"ProgramType": "AdvanceResourceCommitment"}, {"ProgramType": "ZonalResourceCommitment"}]} |

### Coverage Rate with Eligibility-Adjusted Denominator

This example demonstrates how to calculate an accurate [*commitment*](#glossary:commitment) coverage rate using [CommitmentProgramEligibilityDetails](#datasets.costandusage.CommitmentProgramEligibilityDetails) alongside [CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid).

Acme Corp runs compute workloads on Aura Web. Some usage is covered by a Resource Reservation, some is eligible but uncovered, and a support fee is ineligible for any [*commitment program*](#glossary:commitment-program). While the specification mandates that CommitmentProgramEligibilityDetails must not be null when a charge is eligible, practitioners may encounter non-compliant provider data where this column is omitted on covered rows. This creates a gap in naive coverage calculations that rely solely on CommitmentProgramEligibilityDetails to define the eligible population.

Four usage rows for a single charge period (2025-04-01):

1. **Uncovered compute** (Row 1): Eligible for FlexibleSpendPlan and ResourceReservation, not currently covered. [BilledCost](#datasets.costandusage.billedcost) and [EffectiveCost](#datasets.costandusage.effectivecost) are both &dollar;200.00.
2. **Covered compute with eligibility** (Row 2): Covered by a ResourceReservation. CommitmentProgramEligibilityDetails is populated. BilledCost is &dollar;0.00; EffectiveCost is &dollar;150.00.
3. **Covered compute without eligibility** (Row 3): Also covered by the same ResourceReservation. The provider omits CommitmentProgramEligibilityDetails on this row. BilledCost is &dollar;0.00; EffectiveCost is &dollar;100.00.
4. **Support fee** (Row 4): Not eligible for any *commitment program*. Both CommitmentProgramEligibilityDetails and CommitmentDiscountId are null. BilledCost and EffectiveCost are both &dollar;50.00.

A defensive approach adds an OR condition to the denominator, catching covered rows even when a provider omits CommitmentProgramEligibilityDetails:

`CommitmentDiscountId IS NOT NULL OR CommitmentProgramEligibilityDetails IS NOT NULL`

**Without OR** (using only `CommitmentProgramEligibilityDetails IS NOT NULL`):

| Metric | Value |
|:-------|:------|
| Eligible denominator | Row 1 (&dollar;200.00) + Row 2 (&dollar;150.00) = &dollar;350.00 |
| Covered numerator | Row 2 (&dollar;150.00) |
| Coverage rate | `150 / 350` = **42.9%** |

Row 3 is excluded from both numerator and denominator because its CommitmentProgramEligibilityDetails is null, even though it is actively covered.

**With OR** (using `CommitmentDiscountId IS NOT NULL OR CommitmentProgramEligibilityDetails IS NOT NULL`):

| Metric | Value |
|:-------|:------|
| Eligible denominator | Row 1 (&dollar;200.00) + Row 2 (&dollar;150.00) + Row 3 (&dollar;100.00) = &dollar;450.00 |
| Covered numerator | Row 2 (&dollar;150.00) + Row 3 (&dollar;100.00) = &dollar;250.00 |
| Coverage rate | `250 / 450` = **55.6%** |

The OR condition catches Row 3 via its CommitmentDiscountId. This produces an accurate rate that reflects all covered and eligible spend. Row 4 (support fee) is correctly excluded from both approaches because neither column is populated.

[CSV Example](/specification/data/commitment_eligibility/coverage_rate_eligibility_adjusted.csv)

### Uncovered Eligible Spend by Program Type

This example demonstrates how to use [CommitmentProgramEligibilityDetails](#datasets.costandusage.CommitmentProgramEligibilityDetails) to identify uncovered savings opportunities across [*commitment program*](#glossary:commitment-program) types and providers.

Acme Corp runs compute workloads on Aura Web and uses StackLens for observability monitoring. Some Aura Web compute usage is covered by a Resource Reservation. StackLens usage is uncovered but eligible for Interval Spend Commitments at monthly or annual terms. A practitioner wants to answer: "Which *commitment program* and provider should I target for my next purchase?"

Six usage rows for a single charge period (2025-04-01):

1. **Uncovered compute** (Rows 1-2): Two Aura Web Compute rows eligible for both FlexibleSpendPlan and ResourceReservation. [BilledCost](#datasets.costandusage.billedcost) totals &dollar;500.00 across both rows.
2. **Covered compute** (Row 3): Aura Web Compute covered by an existing ResourceReservation. Filtered out by the query because [CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid) is populated.
3. **Ineligible support** (Row 4): Aura Web Support with no CommitmentProgramEligibilityDetails. Filtered out because the column is null.
4. **Uncovered observability** (Rows 5-6): Two StackLens Observability rows eligible for MonthlyIntervalSpendCommitment and AnnualIntervalSpendCommitment. BilledCost totals &dollar;200.00.

The [eligible uncovered spend query](#supportedfeatures.commitmentprogrameligibilitydetails) expands the CommitmentPrograms array via CROSS JOIN UNNEST, then groups by provider, service, and ProgramType:

| ServiceProviderName | ServiceName | EligibleProgramType | TotalEligibleUncoveredCost |
|:--------------------|:------------|:--------------------|:---------------------------|
| Aura Web | Compute | FlexibleSpendPlan | &dollar;500.00 |
| Aura Web | Compute | ResourceReservation | &dollar;500.00 |
| StackLens | Observability | MonthlyIntervalSpendCommitment | &dollar;200.00 |
| StackLens | Observability | AnnualIntervalSpendCommitment | &dollar;200.00 |

Aura Web Compute appears as &dollar;500.00 under both FlexibleSpendPlan and ResourceReservation. This does not mean &dollar;1,000.00 is uncovered. The &dollar;500.00 is the same spend, and each program type represents an independent purchasing opportunity. Purchasing a FlexibleSpendPlan would cover some or all of that &dollar;500.00, as would a ResourceReservation. The practitioner must choose between them (or split across both) based on flexibility requirements and discount depth.

The same logic applies to StackLens: &dollar;200.00 of observability spend could be covered by either a monthly or annual Interval Spend Commitment. The annual option typically offers a deeper discount in exchange for a longer commitment term.

The query uses BilledCost rather than EffectiveCost because all rows are uncovered (CommitmentDiscountId IS NULL). For uncovered usage, BilledCost equals EffectiveCost and reflects the actual amount paid.

[CSV Example](/specification/data/commitment_eligibility/uncovered_eligible_spend_by_program_type.csv)

### Object ID

CommitmentProgramEligibilityDetailsObject

### Object Display Name

Commitment Program Eligibility Details Object

## Column ID

CommitmentProgramEligibilityDetails

## Display Name

Commitment Program Eligibility Details

## Description

The types of [*commitment programs*](#glossary:commitment-program) available for a specific usage row.

## Content Constraints

| Constraint    | Value                                                                                                                        |
|:-------------------------------------|:---------------------------------|
| Dataset       | [Cost and Usage](#datasets.costandusage)                                                                                     |
| Column type   | Dimension                                                                                                                    |
| Feature level | Conditional                                                                                                                  |
| Allows nulls  | True                                                                                                                         |
| Data type     | JSON                                                                                                                         |
| Value format  | [JsonObjectFormat](#attributes.jsonobjectformat)                                                                             |
| Object        | [CommitmentProgramEligibilityDetailsObject](#datasets.costandusage.CommitmentProgramEligibilityDetails.CommitmentProgramEligibilityDetailsobject) |

## Introduced (version)

1.4
