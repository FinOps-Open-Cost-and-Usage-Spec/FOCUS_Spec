# Commitment Program Eligibility

Commitment Program Eligibility identifies the [*commitment programs*](#glossary:commitment-program) that could potentially cover [*charges*](#glossary:charge), subject to [*service provider*](#glossary:service-provider) constraints. By distinguishing the pool of spend that was eligible to be covered, Commitment Program Eligibility provides the fundamental denominator for calculating precise commitment coverage metrics. This allows FinOps practitioners to accurately size the pool of uncovered spend that could realistically be covered by a future commitment. In this context, *commitment programs* include both discount-bearing programs (e.g., Flexible Spend Plans, Resource Reservations) and advance resource commitments (e.g., Advance Resource Commitments), provided the service provider treats them as [*commitments*](#glossary:commitment).

## Requirements

CommitmentProgramEligibility MUST adhere to the following requirements:

* CommitmentProgramEligibility MUST be of type String.
* CommitmentProgramEligibility MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* CommitmentProgramEligibility MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* CommitmentProgramEligibility MUST NOT be null when a charge is eligible for a [*commitment program*](#glossary:commitment-program), regardless of whether a [*commitment*](#glossary:commitment) was actually applied to the charge.
* CommitmentProgramEligibility MUST NOT consider transient account configurations or quotas that might temporarily prevent purchase or participation in a *commitment program*.
* CommitmentProgramEligibility MUST include all publicly available *commitment programs* for which the usage is eligible.
* CommitmentProgramEligibility SHOULD include negotiated *commitment programs* for which the usage is eligible.
* CommitmentProgramEligibility MUST NOT include data related to *commitment* [*periods*](#glossary:period) or payment options.
* CommitmentProgramEligibility MUST conform to [CommitmentProgramEligibilityObject](#datasets.costandusage.commitmentprogrameligibility.commitmentprogrameligibilityobject) requirements when CommitmentProgramEligibility is not null.

## Commitment Program Eligibility Object

Commitment Program Eligibility consists of a valid JSON object with a top-level property key `CommitmentPrograms` containing an array of objects describing the specific [*commitment programs*](#glossary:commitment-program) available for the usage charge.

### Object Requirements

CommitmentProgramEligibilityObject MUST adhere to the following requirements:

* CommitmentProgramEligibilityObject MUST have a top-level property key "CommitmentPrograms".
* CommitmentProgramEligibilityObject MAY contain additional data generator-defined top-level property keys.
* CommitmentProgramEligibilityObject MUST have property keys that begin with the string "x_" unless it is a FOCUS-defined property key.
* CommitmentProgramEligibilityObject.CommitmentPrograms MUST adhere to the following requirements:
  * CommitmentProgramEligibilityObject.CommitmentPrograms MUST be of type Array.
  * CommitmentProgramEligibilityObject.CommitmentPrograms MUST contain one or more objects.
  * Each entry in CommitmentProgramEligibilityObject.CommitmentPrograms MUST be of type JSON Object.
  * Each entry in CommitmentProgramEligibilityObject.CommitmentPrograms MUST have a property key "ProgramType".
  * Each entry in CommitmentProgramEligibilityObject.CommitmentPrograms MAY contain additional data generator-defined property keys.
  * Each entry in CommitmentProgramEligibilityObject.CommitmentPrograms MUST have property keys that begin with the string "x_" unless it is a FOCUS-defined property key.
  * CommitmentProgramEligibilityObject.CommitmentPrograms.ProgramType MUST be of type String.
  * CommitmentProgramEligibilityObject.CommitmentPrograms.ProgramType MUST NOT be null.
  * CommitmentProgramEligibilityObject.CommitmentPrograms.ProgramType MUST correspond to a *commitment program* type supported by the service provider (e.g., "FlexibleSpendPlan", "ResourceReservation", "BulkCapacityCredit", "AdvanceResourceCommitment").
  * CommitmentProgramEligibilityObject.CommitmentPrograms.ProgramType MUST equal [CommitmentDiscountType](#datasets.costandusage.commitmentdiscounttype) for one object in CommitmentProgramEligibilityObject.CommitmentPrograms when CommitmentDiscountType is not null.
  * CommitmentProgramEligibilityObject.CommitmentPrograms.ProgramType SHOULD correspond to terminology disclosed by the service provider in public documentation.

### Top-Level Properties

| Property             | Type  | Required | Description                                                                         |
|:----------|:----------|:----------|:---------------------------------------|
| `CommitmentPrograms` | Array | True     | Array of objects identifying *commitment programs* for which the usage is eligible. |

### Example Entries

| Key         | ValueType                            | Required | Description                                                                                                |
|:-------------|:-------------|:-------------|:------------------------------|
| ProgramCategory | [String](#attributes.stringhandling) | True     | Provider-agnostic classification of *commitment program*. |
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

NOTE: The above JSON Type Definition (JTD) is an approximation of the expected contents of this column, but it should not be considered normative because it cannot accurately describe the normative requirements (above) for CommitmentProgramEligibility. Where there are discrepancies, preference will be given to the normative requirements.

## Example Scenarios

The examples below are not exhaustive and may change over time. Service providers are the authoritative source for their [*commitment programs*](#glossary:commitment-program).

### Aura Web (Partially Covered Compute Usage)

Scenario: A compute usage row that is partially covered by a Flexible Spend Plan. The eligibility column still reflects all programs this usage qualifies for, regardless of current coverage.

| ServiceProviderName | ServiceName | CommitmentProgramEligibility                                                                            |
|---------------------|-------------|---------------------------------------------------------------------------------------------------------|
| Aura Web            | Compute     | {"CommitmentPrograms": [{"ProgramType": "FlexibleSpendPlan"}, {"ProgramType": "ResourceReservation"}]} |

### StackLens (Observability with Interval Spend Commitment)

Scenario: An observability platform usage row eligible for Monthly and Annual interval spend commitment pricing, offering lower effective rates than standard usage.

| ServiceProviderName | ServiceName   | CommitmentProgramEligibility                                                                                            |
|---------------------|---------------|-------------------------------------------------------------------------------------------------------------------------|
| StackLens           | Observability | {"CommitmentPrograms": [{"ProgramType": "MonthlyIntervalSpendCommitment"}, {"ProgramType": "AnnualIntervalSpendCommitment"}]} |

### LatticeScale (Ineligible Object Storage Usage)

Scenario: Standard object storage usage or a support fee, which is not eligible for any commitment program.

| ServiceProviderName | ServiceName   | CommitmentProgramEligibility |
|---------------------|---------------|------------------------------|
| LatticeScale        | ObjectStorage | null                         |

### Aura Web (Advance Resource Commitment-Eligible Compute Usage)

Scenario: A compute instance type and tenancy that are eligible for both discount-bearing programs and advance resource commitments. The eligibility column reflects all commitment constructs the usage qualifies for.

| ServiceProviderName | ServiceName | CommitmentProgramEligibility                                                                                                                                                                           |
|---------------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aura Web            | Compute     | {"CommitmentPrograms": [{"ProgramType": "FlexibleSpendPlan"}, {"ProgramType": "ResourceReservation"}, {"ProgramType": "AdvanceResourceCommitment"}, {"ProgramType": "ZonalResourceCommitment"}]} |

### Object ID

CommitmentProgramEligibilityObject

### Object Display Name

Commitment Program Eligibility Object

## Column ID

CommitmentProgramEligibility

## Display Name

Commitment Program Eligibility

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
| Object        | [CommitmentProgramEligibilityObject](#datasets.costandusage.commitmentprogrameligibility.commitmentprogrameligibilityobject) |

## Introduced (version)

1.4