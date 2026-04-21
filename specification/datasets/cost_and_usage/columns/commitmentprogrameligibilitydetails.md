# Commitment Program Eligibility Details

Commitment Program Eligibility Details identifies the [*commitment programs*](#glossary:commitment-program) that could potentially cover [*charges*](#glossary:charge), subject to [*service provider*](#glossary:service-provider) constraints. By distinguishing the pool of spend that was eligible to be covered, Commitment Program Eligibility Details provides the fundamental denominator for calculating precise commitment coverage metrics. This allows FinOps practitioners to accurately size the pool of uncovered spend that could realistically be covered by a future commitment. In this context, *commitment programs* include both [*commitment discounts*](#glossary:commitment-discount) and [*capacity reservations*](#glossary:capacity-reservation), provided the service provider treats them as [*commitments*](#glossary:commitment).

## Requirements

### Column Requirements

CommitmentProgramEligibilityDetails MUST adhere to the following requirements:

* CommitmentProgramEligibilityDetails MUST be of type JSON Object (serialized as a String where necessary).
* CommitmentProgramEligibilityDetails MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* CommitmentProgramEligibilityDetails MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* CommitmentProgramEligibilityDetails MUST NOT be null when a charge is eligible for a [*commitment program*](#glossary:commitment-program), regardless of whether a [*commitment*](#glossary:commitment) was actually applied to the charge.
* CommitmentProgramEligibilityDetails MUST NOT reflect restrictions (e.g., transient account configurations, quotas) that might temporarily prevent purchase or participation in a *commitment program*.
* CommitmentProgramEligibilityDetails MUST include all publicly available *commitment programs* for which the usage is eligible.
* CommitmentProgramEligibilityDetails MAY include negotiated *commitment programs* when the usage is eligible and the program is not broadly applicable across the service provider's service catalog.
* CommitmentProgramEligibilityDetails MUST NOT include data related to *commitment* [*periods*](#glossary:period) or payment options.
* CommitmentProgramEligibilityDetails MUST conform to [CommitmentProgramEligibilityDetailsObject](#datasets.costandusage.commitmentprogrameligibilitydetails.commitmentprogrameligibilitydetailsobject) requirements when CommitmentProgramEligibilityDetails is not null.

## Commitment Program Eligibility Details Object

Commitment Program Eligibility Details consists of a valid JSON object with a top-level property key `CommitmentPrograms` containing an array of objects describing the specific [*commitment programs*](#glossary:commitment-program) available for the usage charge.

### Object Requirements

CommitmentProgramEligibilityDetailsObject MUST adhere to the following requirements:

* CommitmentProgramEligibilityDetailsObject MUST conform to the [CommitmentProgramEligibilityDetailsObjectSchema](#schemas.datasets.costandusage.commitmentprogrameligibilitydetailsobjectschema) JSON Schema.
* CommitmentProgramEligibilityDetailsObject.CommitmentPrograms[\*].ProgramType MUST correspond to a *commitment program* type supported by the service provider.
* CommitmentProgramEligibilityDetailsObject.CommitmentPrograms[\*].ProgramType MUST equal [CommitmentDiscountType](#datasets.costandusage.commitmentdiscounttype) for one object in CommitmentProgramEligibilityDetailsObject.CommitmentPrograms when CommitmentDiscountType is not null.
* CommitmentProgramEligibilityDetailsObject.CommitmentPrograms[\*].ProgramType SHOULD correspond to terminology disclosed by the service provider in public documentation.

## Schema Structure

### Top-Level Properties

| Property             | Type  | Required | Description                                                                         |
|:----------|:----------|:----------|:---------------------------------------|
| `CommitmentPrograms` | Array | True     | Array of objects identifying *commitment programs* for which the usage is eligible. |

### CommitmentPrograms Object

The `CommitmentPrograms` array contains one or more objects, each of which contains the following entries:

| Key         | ValueType                            | Required | Description                                                                                                |
|:-------------|:-------------|:-------------|:------------------------------|
| ProgramType | [String](#attributes.stringhandling) | True     | The specific type of commitment program (e.g., discount or capacity reservation) available for this usage. |

## Object Example

Here is a basic example of the object format.

* For more detailed examples, please see this column's entry in the JSON Object Examples appendix entry [here](#appendix.examples:jsonobject.examples:commitmentprogrameligibilitydetails).
* For the JSON schema, please see [Commitment Program Eligibility Details Object Schema](#schemas.datasets.costandusage.commitmentprogrameligibilitydetailsobjectschema).

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

## Implementation Guidance

### Custom Properties

To facilitate querying data across allocations and across service providers, a data generator may include one or more custom properties. These may be placed at the top level of the object (alongside `CommitmentPrograms`) or nested within the individual `CommitmentPrograms` objects. Custom keys must be prefixed with "x_" followed by PascalCase format (e.g., `x_MyCustomKey`) to make them easy to identify as well as prevent collisions with FOCUS-defined keys.

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
| Object        | [CommitmentProgramEligibilityDetailsObject](#datasets.costandusage.commitmentprogrameligibilitydetails.commitmentprogrameligibilitydetailsobject) |

## Introduced (version)

1.4
