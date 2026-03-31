# Commitment Eligibility Details

Commitment Eligibility Details identifies the [*commitment programs*](#glossary:commitment-program) that could potentially [*cover charges*](#glossary:covered-charge), subject to [*service provider*](#glossary:service-provider) constraints. By distinguishing the pool of spend that was eligible to be covered, Commitment Eligibility Details provides the fundamental denominator for calculating precise commitment coverage metrics. This allows FinOps practitioners to accurately size the pool of uncovered spend that could realistically be covered by a future commitment. In this context, *commitment programs* include both discount-bearing constructs (e.g., Savings Plans, committed-use discounts) and advance capacity reservations (e.g., zonal reservations), provided the service provider treats them as [*commitments*](#glossary:commitment).

## Requirements

CommitmentEligibilityDetails MUST adhere to the following requirements:

* CommitmentEligibilityDetails MUST be of type String.
* CommitmentEligibilityDetails MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* CommitmentEligibilityDetails MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* CommitmentEligibilityDetails MUST NOT be null when a charge is eligible for a [*commitment program*](#glossary:commitment-program), regardless of whether a [*commitment*](#glossary:commitment) was actually applied to the charge.
* CommitmentEligibilityDetails MUST NOT consider transient account configurations or quotas that might temporarily prevent purchase or participation in a *commitment program*.
* CommitmentEligibilityDetails MUST include all publicly available *commitment programs* for which the usage is eligible.
* CommitmentEligibilityDetails SHOULD include negotiated *commitment programs* for which the usage is eligible.
* CommitmentEligibilityDetails MUST NOT include data related to *commitment* [*periods*](#glossary:period) or payment options.
* CommitmentEligibilityDetails MUST conform to [CommitmentEligibilityDetailsObject](#datasets.costandusage.commitmenteligibilitydetails.commitmenteligibilitydetailsobject) requirements when CommitmentEligibilityDetails is not null.

## Commitment Eligibility Details Object

Commitment Eligibility Details consists of a valid JSON object with a top-level property key `CommitmentPrograms` containing an array of objects describing the specific [*commitment programs*](#glossary:commitment-program) available for the usage charge.

### Object Requirements

CommitmentEligibilityDetailsObject MUST adhere to the following requirements:

* CommitmentEligibilityDetailsObject MUST have a top-level property key "CommitmentPrograms".
* CommitmentEligibilityDetailsObject MAY contain additional data generator-defined top-level property keys.
* CommitmentEligibilityDetailsObject MUST have property keys that begin with the string "x\_" unless it is a FOCUS-defined property key.
* CommitmentEligibilityDetailsObject.CommitmentPrograms MUST adhere to the following requirements:
  * CommitmentEligibilityDetailsObject.CommitmentPrograms MUST be of type Array.
  * CommitmentEligibilityDetailsObject.CommitmentPrograms MUST contain one or more objects.
  * Each entry in CommitmentEligibilityDetailsObject.CommitmentPrograms MUST be of type JSON Object.
  * CommitmentEligibilityDetailsObject.CommitmentPrograms MUST have a property key "ProgramType".
  * CommitmentEligibilityDetailsObject.CommitmentPrograms MAY contain additional data generator-defined property keys.
  * CommitmentEligibilityDetailsObject.CommitmentPrograms MUST have property keys that begin with the string "x\_" unless it is a FOCUS-defined property key.
  * CommitmentEligibilityDetailsObject.CommitmentPrograms.ProgramType MUST be of type String.
  * CommitmentEligibilityDetailsObject.CommitmentPrograms.ProgramType MUST NOT be null.
  * CommitmentEligibilityDetailsObject.CommitmentPrograms.ProgramType MUST correspond to a *commitment program* type supported by the service provider (e.g., "SavingsPlan", "ReservedInstance", "CommittedUseDiscount", "CapacityReservation", "ZonalReservation").
  * CommitmentEligibilityDetailsObject.CommitmentPrograms.ProgramType MUST equal [CommitmentDiscountType](#datasets.costandusage.commitmentdiscounttype) for one object in CommitmentEligibilityDetailsObject.CommitmentPrograms when CommitmentDiscountType is not null.
  * CommitmentEligibilityDetailsObject.CommitmentPrograms.ProgramType SHOULD correspond to terminology disclosed by the service provider in public documentation.

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
    { "ProgramType": "SavingsPlan" },
    { "ProgramType": "ReservedInstance" },
    { "ProgramType": "CapacityReservation" },
    { "ProgramType": "ZonalReservation" }
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

NOTE: The above JSON Type Definition (JTD) is an approximation of the expected contents of this column, but it should not be considered normative because it cannot accurately describe the normative requirements (above) for CommitmentEligibilityDetails. Where there are discrepancies, preference will be given to the normative requirements.

## Example Scenarios

The examples below are not exhaustive and may change over time. Service providers are the authoritative source for their [*commitment programs*](#glossary:commitment-program).

### Provider A (Partially covered Virtual Machine Usage)

Scenario: A Virtual Machine usage row that is partially covered by Savings Plan. The eligibility column still reflects all programs this usage qualifies for, regardless of current coverage.

| ServiceProviderName | ServiceName      | CommitmentEligibilityDetails                                                                  |
|------------------|------------------|------------------|
| Provider A          | Virtual Machines | {"CommitmentPrograms": [{"ProgramType": "SavingsPlan"}, {"ProgramType": "ReservedInstance"}]} |

### Provider B (Infrastructure with Subscription Commitment)

Scenario: An infrastructure host usage row eligible for Monthly and Annual commitment-based pricing, offering lower effective rates than On-Demand usage.

| ServiceProviderName | ServiceName    | CommitmentEligibilityDetails                                                                        |
|-----------|-----------|----------------------------------------|
| Provider B          | Infrastructure | {"CommitmentPrograms": [{"ProgramType": "MonthlyCommitment"}, {"ProgramType": "AnnualCommitment"}]} |

### Provider C (Ineligible Object Storage Usage)

Scenario: Standard object storage usage or a support fee, which is not eligible for any commitment program.

| ServiceProviderName | ServiceName   | CommitmentEligibilityDetails |
|---------------------|---------------|------------------------------|
| Provider C          | ObjectStorage | null                         |

### Provider D (Capacity Reservation-eligible Compute Usage)

A compute instance type and tenancy that are eligible for both Savings Plans/Reserved Instances and for capacity reservations (e.g., regional reservations, zonal reservations). The eligibility column reflects all commitment constructs the usage qualifies for.

| ServiceProviderName | ServiceName    | CommitmentEligibilityDetails                                                                                                                                               |
|------------------|------------------|------------------|
| Provider D          | Compute | {"CommitmentPrograms": [{"ProgramType": "SavingsPlan"}, {"ProgramType": "ReservedInstance"}, {"ProgramType": "CapacityReservation"}, {"ProgramType": "ZonalReservation"}]} |

### Object ID

CommitmentEligibilityDetailsObject

### Object Display Name

Commitment Eligibility Details Object

## Column ID

CommitmentEligibilityDetails

## Display Name

Commitment Eligibility Details

## Description

The types of [*commitment programs*](#glossary:commitment-program) available for a specific usage row.

## Content constraints

| Constraint    | Value                                                                                                                        |
|:-------------------------------------|:---------------------------------|
| Dataset       | [Cost and Usage](#datasets.costandusage)                                                                                     |
| Column type   | Dimension                                                                                                                    |
| Feature level | Conditional                                                                                                                  |
| Allows nulls  | True                                                                                                                         |
| Data type     | JSON                                                                                                                         |
| Value format  | [JsonObjectFormat](#attributes.jsonobjectformat)                                                                             |
| Object        | [CommitmentEligibilityDetailsObject](#datasets.costandusage.commitmenteligibilitydetails.commitmenteligibilitydetailsobject) |

## Introduced (version)

1.4