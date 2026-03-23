# Commitment Eligibility Details

Commitment Eligibility Details indicates which [*commitment*](#glossary:commitment) programs a service provider designates as applicable to a usage row. This reflects the inherent eligibility of the service, subject to any service provider-defined constraints. This column enables practitioners to identify uncovered spend that could have been covered, separating it from spend that is strictly ineligible. For the purposes of this column, *commitment* programs include both discount-bearing constructs (for example, Savings Plans, committed-use discounts) and non-discount constructs that reserve capacity in advance (for example, capacity reservations, zonal reservations), when those constructs are treated by the service provider as commitments.

## Requirements

CommitmentEligibilityDetails MUST adhere to the following requirements:

-   CommitmentEligibilityDetails MUST be of type String.
-   CommitmentEligibilityDetails MUST conform to [StringHandling](#attributes.stringhandling) requirements.
-   CommitmentEligibilityDetails MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
*   CommitmentEligibilityDetails MUST NOT be null when a charge is eligible for a [*commitment program*](#glossary:commitment-program), regardless of whether a [*commitment*](#glossary:commitment) was actually applied to the charge.
*   CommitmentEligibilityDetails MUST NOT consider transient account configurations or quotas that might temporarily prevent purchase or participation in a *commitment program*.
*   CommitmentEligibilityDetails MUST include all publicly available *commitment programs* for which the usage is eligible.
*   CommitmentEligibilityDetails SHOULD include negotiated *commitment programs* for which the usage is eligible.
*   CommitmentEligibilityDetails MUST NOT include data related to *commitment* [*periods*](#glossary:period) or payment options.
-   CommitmentEligibilityDetails MUST conform to [CommitmentEligibilityDetailsObject](#datasets.costandusage.commitmenteligibilitydetails.commitmenteligibilitydetailsobject) requirements when CommitmentEligibilityDetails is not null.

## Commitment Eligibility Details Object

Commitment Eligibility Details consists of a valid JSON object with a top-level property key `CommitmentPrograms` containing an array of objects describing the specific [*commitment programs*](#glossary:commitment-program) available for the usage charge.

### Object Requirements

CommitmentEligibilityDetailsObject MUST adhere to the following requirements: 
* CommitmentEligibilityDetailsObject MUST have at least one top-level property key when not null. 
* CommitmentEligibilityDetailsObject MAY have a top-level property key "CommitmentDiscountTypes". 
* CommitmentEligibilityDetailsObject MAY have a top-level property key "CapacityReservationTypes" for commitment programs whose primary purpose is to reserve capacity rather than to provide a unit discount. 
* CommitmentEligibilityDetailsObject MAY contain additional data generator-defined top-level property keys for future or service provider-specific commitment categories.

-   CommitmentEligibilityDetailsObject MUST have property keys that begin with the string "x\_" unless it is a FOCUS-defined property key.
-   CommitmentEligibilityDetailsObject.CommitmentDiscountTypes MUST adhere to the following requirements:
    -   CommitmentEligibilityDetailsObject.CommitmentDiscountTypes MUST be of type Array.
    -   CommitmentEligibilityDetailsObject.CommitmentDiscountTypes MUST contain one or more objects.
    -   Each entry in CommitmentEligibilityDetailsObject.CommitmentDiscountTypes MUST be of type JSON Object.
    -   CommitmentEligibilityDetailsObject.CommitmentDiscountTypes MUST have a property key "Type".
    -   CommitmentEligibilityDetailsObject.CommitmentDiscountTypes MAY contain additional data generator-defined property keys.
    -   CommitmentEligibilityDetailsObject.CommitmentDiscountTypes MUST have property keys that begin with the string "x\_" unless it is a FOCUS-defined property key.
    -   CommitmentEligibilityDetailsObject.CommitmentDiscountTypes.Type MUST be of type String.
    -   CommitmentEligibilityDetailsObject.CommitmentDiscountTypes.Type MUST NOT be null.
    -   CommitmentEligibilityDetailsObject.CommitmentDiscountTypes.Type MUST correspond to a commitment program type supported by the provider (e.g., "SavingsPlan", "ReservedInstance", "CommittedUseDiscount").
    -    CommitmentEligibilityDetailsObject.CommitmentDiscountTypes.Type MUST equal [CommitmentDiscountType](#datasets.costandusage.commitmentdiscounttype) for  one object in CommitmentEligibilityDetailsObject.CommitmentDiscountTypes when CommitmentDiscountType is not null.
    -   CommitmentEligibilityDetailsObject.CommitmentDiscountTypes.Type SHOULD correspond to terminology disclosed by the service provider in public documentation.
-   CommitmentEligibilityDetailsObject.CapacityReservationTypes MUST adhere to the following requirements:
    -   CommitmentEligibilityDetailsObject.CapacityReservationTypes MUST be of type Array.
    -   CommitmentEligibilityDetailsObject.CapacityReservationTypes MUST contain one or more objects.
    -   Each entry in CommitmentEligibilityDetailsObject.CapacityReservationTypes MUST be of type JSON Object.
    -   CommitmentEligibilityDetailsObject.CapacityReservationTypes MUST have a property key "Type".
    -   CommitmentEligibilityDetailsObject.CapacityReservationTypes MAY contain additional data generator-defined property keys.
    -   CommitmentEligibilityDetailsObject.CapacityReservationTypes MUST have property keys that begin with the string "x\_" unless it is a FOCUS-defined property key.
    -   CommitmentEligibilityDetailsObject.CapacityReservationTypes.Type MUST be of type String.
    -   CommitmentEligibilityDetailsObject.CapacityReservationTypes.Type MUST NOT be null.
    -   CommitmentEligibilityDetailsObject.CapacityReservationTypes.Type MUST correspond to a capacity-reservation-style commitment program supported by the provider (for example, "CapacityReservation", "ZonalReservation").

### Top-Level Properties

| Property             | Type  | Required | Description                                                                        |
|:---------------------|:------|:---------|:-----------------------------------------------------------------------------------|
| `CommitmentPrograms` | Array | True     | Array of objects identifying *commitment programs* for which the usage is eligible. |

### Example Entries

| Key         | ValueType                            | Required | Description                                                                                                |
|:-----------|:-----------|:-----------|:-------------------------------------|
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

**Azure (Partially covered Virtual Machine Usage)**

A Virtual Machine usage row that is partially covered by Savings Plan. The eligibility column still reflects all programs this usage qualifies for, regardless of current coverage.

| ServiceProviderName | ServiceName      | ChargeClass | CommitmentEligibilityDetails                                                         |
|---------------|---------------|---------------|---------------|
| Azure               | Virtual Machines | Usage       | {"CommitmentPrograms": [{"ProgramType": "SavingsPlan"}, {"ProgramType": "ReservedInstance"}]} |

**Datadog (Monthly and Annual Commitment)**

An On-Demand infrastructure host usage row (potentially billed as overage). This usage is eligible for coverage under commitment plans that offer lower rates than On-Demand. Since Datadog does not populate CommitmentDiscountType, the ProgramType values correspond to publicly available program names from Datadog documentation.

| ServiceProviderName | ServiceName    | ChargeClass | CommitmentEligibilityDetails                                                               |
|---------------|---------------|---------------|---------------|
| Datadog             | Infrastructure | Usage       | {"CommitmentPrograms": [{"ProgramType": "MonthlyCommitment"}, {"ProgramType": "AnnualCommitment"}]} |

**AWS (Capacity Reservation-eligible EC2 Usage)**

An EC2 instance type and tenancy that are eligible for both Savings Plans/Reserved Instances and for capacity reservations (e.g., regional reservations, zonal reservations). The eligibility column reflects all commitment constructs the usage qualifies for.

| ServiceProviderName | ServiceName | ChargeClass | CommitmentEligibilityDetails                                                                                                                                                      |
|---------------|---------------|---------------|---------------|
| AWS                 | AmazonEC2   | Usage       | {"CommitmentPrograms": [{"ProgramType": "SavingsPlan"}, {"ProgramType": "ReservedInstance"}, {"ProgramType": "CapacityReservation"}, {"ProgramType": "ZonalReservation"}]} |

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
