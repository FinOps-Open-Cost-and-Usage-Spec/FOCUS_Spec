# Commitment Program Eligibility Details

[Commitment Program Eligibility Details](#col) identifies the [commitment programs](#term) that could potentially cover [charges](#term), subject to [service provider](#term) constraints. By distinguishing the pool of spend that was eligible to be covered, [Commitment Program Eligibility Details](#col) provides the fundamental denominator for calculating precise commitment coverage metrics. This allows FinOps practitioners to accurately size the pool of uncovered spend that could realistically be covered by a future commitment. In this context, [commitment programs](#term) include discount-bearing programs such as [commitment discounts](#term) and [capacity reservations](#term), provided the service provider treats them as [commitments](#term).

## Requirements

### Column Requirements

[CommitmentProgramEligibilityDetails](#col) MUST adhere to the following requirements:

* [CommitmentProgramEligibilityDetails](#col) MUST be of type JSON Object (serialized as a String where necessary).
* [CommitmentProgramEligibilityDetails](#col) MUST conform to [StringHandling](#attr) requirements.
* [CommitmentProgramEligibilityDetails](#col) MUST conform to [JsonObjectFormat](#attr) requirements.
* [CommitmentProgramEligibilityDetails](#col) MUST NOT be null when a charge is eligible for a [commitment program](#term), regardless of whether a [commitment](#term) was actually applied to the charge.
* [CommitmentProgramEligibilityDetails](#col) MUST NOT reflect restrictions (e.g., transient account configurations, quotas) that might temporarily prevent purchase or participation in a [commitment program](#term).
* [CommitmentProgramEligibilityDetails](#col) MUST include all publicly available [commitment programs](#term) for which the usage is eligible.
* [CommitmentProgramEligibilityDetails](#col) MAY include negotiated [commitment programs](#term) when the usage is eligible and the program is not broadly applicable across the service provider's service catalog.
* [CommitmentProgramEligibilityDetails](#col) MUST NOT include data related to [commitment](#term) [periods](#term) or payment options.
* [CommitmentProgramEligibilityDetails](#col) MUST conform to [CommitmentProgramEligibilityDetailsObject](#obj) requirements when [CommitmentProgramEligibilityDetails](#col) is not null.

## Commitment Program Eligibility Details Object

[Commitment Program Eligibility Details](#col) consists of a valid JSON object with a top-level property key `CommitmentPrograms` containing an array of objects describing the specific [commitment programs](#term) available for the usage charge.

### Object Requirements

[CommitmentProgramEligibilityDetailsObject](#obj) MUST adhere to the following requirements:

* [CommitmentProgramEligibilityDetailsObject](#obj) MUST conform to the [CommitmentProgramEligibilityDetailsObjectSchema](#schema) JSON Schema.
* CommitmentProgramEligibilityDetailsObject.CommitmentPrograms[\*].ProgramType MUST correspond to a [commitment program](#term) type supported by the service provider.
* CommitmentProgramEligibilityDetailsObject.CommitmentPrograms[\*].ProgramType MUST match [CommitmentDiscountType](#col) for one object in CommitmentProgramEligibilityDetailsObject.CommitmentPrograms when [CommitmentDiscountType](#col) is not null.
* CommitmentProgramEligibilityDetailsObject.CommitmentPrograms[\*].ProgramType SHOULD correspond to terminology disclosed by the service provider in public documentation.

### Object Schema Structure

<div class="h7-nonindex">Top-Level Properties</div>

| Property             | Type  | Required | Description                                                                         |
|:----------|:----------|:----------|:---------------------------------------|
| `CommitmentPrograms` | Array | True     | Array of objects identifying *commitment programs* for which the usage is eligible. |

<div class="h7-nonindex">CommitmentPrograms Object</div>

The `CommitmentPrograms` array contains one or more objects, each of which contains the following entries:

| Key         | ValueType                            | Required | Description                                                                                                |
|:-------------|:-------------|:-------------|:------------------------------|
| ProgramType | [String](#attributes.stringhandling) | True     | The specific type of commitment program (e.g., discount or capacity reservation) available for this usage. |

### Object Implementation Guidance

<div class="h7-nonindex">Custom Properties</div>

To facilitate querying data across allocations and across service providers, a data generator may include one or more custom properties. These may be placed at the top level of the object (alongside `CommitmentPrograms`) or nested within the individual `CommitmentPrograms` objects. Custom keys must be prefixed with "x_" followed by PascalCase format (e.g., `x_MyCustomKey`) to make them easy to identify as well as prevent collisions with FOCUS-defined keys.

### Object Example

Here is a basic example of the object format.

* For more detailed examples, please see this column's entry in the JSON Object Examples appendix entry [here](#appendix.examples:jsonobject.examples:commitmentprogrameligibilitydetails).
* For the JSON schema, please see [Commitment Program Eligibility Details Object Schema](#schema).

``` json
{
  "CommitmentPrograms": [
    { "ProgramType": "Flexible Spend Plan" },
    { "ProgramType": "Resource Reservation" },
    { "ProgramType": "Advance Resource Commitment" },
    { "ProgramType": "Zonal Resource Commitment" }
  ]
}
```

### Object ID

CommitmentProgramEligibilityDetailsObject

### Object Display Name

Commitment Program Eligibility Details Object

## Column ID

CommitmentProgramEligibilityDetails

## Display Name

Commitment Program Eligibility Details

## Description

The types of [commitment programs](#term) available for a specific usage row.

## Content Constraints

| Constraint                 | Value                                              |
| :------------------------- | :------------------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                              |
| Operating model conditions | [Includes Commitment Programs](#omc)                                                 |
| Column type                | Dimension                                          |
| Feature level              | Conditional                                        |
| Allows nulls               | True                                               |
| Data type                  | JSON                                               |
| Value format               | [JSON Object Format](#attr)                        |
| Object                     | [CommitmentProgramEligibilityDetailsObject](#obj)                                                                                                  |

## Version Introduced

1.4
