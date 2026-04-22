# Examples: Commitment Program Eligibility Details

The examples below are not exhaustive and may change over time. Service providers are the authoritative source for their [*commitment programs*](#glossary:commitment-program).

## Aura Web (Partially Covered Compute Usage)

Scenario: A compute usage row that is partially covered by a Flexible Spend Plan. The eligibility column still reflects all programs this usage qualifies for, regardless of current coverage.

| ServiceProviderName | ServiceName | CommitmentProgramEligibilityDetails                                                                            |
|---------------------|-------------|---------------------------------------------------------------------------------------------------------|
| Aura Web            | Compute     | {"CommitmentPrograms": [{"ProgramType": "Flexible Spend Plan"}, {"ProgramType": "Resource Reservation"}]} |

## StackLens (Observability with Interval Spend Commitment)

Scenario: An observability platform usage row eligible for Monthly and Annual interval spend commitment pricing, offering lower effective rates than standard usage.

| ServiceProviderName | ServiceName   | CommitmentProgramEligibilityDetails                                                                                            |
|---------------------|---------------|-------------------------------------------------------------------------------------------------------------------------|
| StackLens           | Observability | {"CommitmentPrograms": [{"ProgramType": "Monthly Interval Spend Commitment"}, {"ProgramType": "Annual Interval Spend Commitment"}]} |

## LatticeScale (Ineligible Object Storage Usage)

Scenario: Standard object storage usage or a support fee, which is not eligible for any commitment program.

| ServiceProviderName | ServiceName   | CommitmentProgramEligibilityDetails |
|---------------------|---------------|------------------------------|
| LatticeScale        | ObjectStorage | null                         |

## Aura Web (Advance Resource Commitment-Eligible Compute Usage)

Scenario: A compute instance type and tenancy that are eligible for both discount-bearing programs and advance resource commitments. The eligibility column reflects all commitment constructs the usage qualifies for.

| ServiceProviderName | ServiceName | CommitmentProgramEligibilityDetails                                                                                                                                                                           |
|---------------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aura Web            | Compute     | {"CommitmentPrograms": [{"ProgramType": "Flexible Spend Plan"}, {"ProgramType": "Resource Reservation"}, {"ProgramType": "Advance Resource Commitment"}, {"ProgramType": "Zonal Resource Commitment"}]} |

## Coverage Rate with Eligibility-Adjusted Denominator

This example demonstrates how to calculate an accurate [*commitment*](#glossary:commitment) coverage rate using [CommitmentProgramEligibilityDetails](#datasets.costandusage.commitmentprogrameligibilitydetails) alongside [CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid).

Acme Corp runs compute workloads on Aura Web. Some usage is covered by a Resource Reservation, some is eligible but uncovered, and a support fee is ineligible for any [*commitment program*](#glossary:commitment-program).

Three usage rows for a single charge period (2025-04-01):

1. **Uncovered compute** (Row 1): Eligible for Flexible Spend Plan and Resource Reservation, not currently covered. [BilledCost](#datasets.costandusage.billedcost) and [EffectiveCost](#datasets.costandusage.effectivecost) are both $200.00.
2. **Covered compute** (Row 2): Covered by a Resource Reservation. CommitmentProgramEligibilityDetails is populated. BilledCost is $0.00; EffectiveCost is $150.00.
3. **Support fee** (Row 3): Not eligible for any *commitment program*. Both CommitmentProgramEligibilityDetails and CommitmentDiscountId are null. BilledCost and EffectiveCost are both $50.00.

By filtering the denominator to rows where `CommitmentProgramEligibilityDetails IS NOT NULL`, the $50.00 support fee is correctly excluded from the eligible population:

| Metric | Value |
|:-------|:------|
| Eligible denominator | Row 1 ($200.00) + Row 2 ($150.00) = $350.00 |
| Covered numerator | Row 2 ($150.00) |
| Coverage rate | `150 / 350` = **42.9%** |

Row 3 (support fee) is correctly excluded because CommitmentProgramEligibilityDetails is null for ineligible charges.

[CSV Example](/specification/data/commitment_eligibility/coverage_rate_eligibility_adjusted.csv)

## Uncovered Eligible Spend by Program Type

This example demonstrates how to use [CommitmentProgramEligibilityDetails](#datasets.costandusage.commitmentprogrameligibilitydetails) to identify uncovered savings opportunities across [*commitment program*](#glossary:commitment-program) types and providers.

Acme Corp runs compute workloads on Aura Web and uses StackLens for observability monitoring. Some Aura Web compute usage is covered by a Resource Reservation. StackLens usage is uncovered but eligible for Interval Spend Commitments at monthly or annual terms. A practitioner wants to answer: "Which *commitment program* and provider should I target for my next purchase?"

Six usage rows for a single charge period (2025-04-01):

1. **Uncovered compute** (Rows 1-2): Two Aura Web Compute rows eligible for both Flexible Spend Plan and Resource Reservation. [BilledCost](#datasets.costandusage.billedcost) totals $500.00 across both rows.
2. **Covered compute** (Row 3): Aura Web Compute covered by an existing Resource Reservation. Filtered out by the query because [CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid) is populated.
3. **Ineligible support** (Row 4): Aura Web Support with no CommitmentProgramEligibilityDetails. Filtered out because the column is null.
4. **Uncovered observability** (Rows 5-6): Two StackLens Observability rows eligible for Monthly Interval Spend Commitment and Annual Interval Spend Commitment. BilledCost totals $200.00.

To evaluate these purchasing options, the `CommitmentPrograms` JSON array must be flattened so each eligible program can be analyzed independently. By expanding the array (e.g., via `CROSS JOIN UNNEST`) and grouping the uncovered costs by `ServiceProviderName`, `ServiceName`, and `EligibleProgramType`, the practitioner gets the summary presented in the table below. A reference implementation is available in the [eligible uncovered spend query](#supportedfeatures.commitmentprogrameligibilitydetails) supported feature.

| ServiceProviderName | ServiceName | EligibleProgramType | EligibleUncoveredCost |
|:--------------------|:------------|:--------------------|:---------------------------|
| Aura Web | Compute | Flexible Spend Plan | $500.00 |
| Aura Web | Compute | Resource Reservation | $500.00 |
| StackLens | Observability | Monthly Interval Spend Commitment | $200.00 |
| StackLens | Observability | Annual Interval Spend Commitment | $200.00 |

Aura Web Compute appears as $500.00 under both Flexible Spend Plan and Resource Reservation. This does not mean $1,000.00 is uncovered. The $500.00 is the same spend, and each program type represents an independent purchasing opportunity. Purchasing a Flexible Spend Plan would cover some or all of that $500.00, as would a Resource Reservation. The practitioner must choose between them (or split across both) based on flexibility requirements and discount depth.

The same logic applies to StackLens: $200.00 of observability spend could be covered by either a monthly or annual Interval Spend Commitment. The annual option typically offers a deeper discount in exchange for a longer commitment term.

The query uses BilledCost rather than EffectiveCost because all rows are uncovered (CommitmentDiscountId IS NULL). For uncovered usage, BilledCost equals EffectiveCost and reflects the actual amount paid.

[CSV Example](/specification/data/commitment_eligibility/uncovered_eligible_spend_by_program_type.csv)
