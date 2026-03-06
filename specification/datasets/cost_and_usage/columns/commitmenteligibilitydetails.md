# Commitment Eligibility Details

Commitment Eligibility Details indicates which [*commitment*](#glossary:commitment) programs a provider designates as applicable to a usage line item. This reflects the inherent eligibility of the service, subject to any provider-defined constraints. This column enables practitioners to identify uncovered spend that could have been covered, separating it from spend that is strictly ineligible.For the purposes of this column, [*commitment*](#glossary:commitment) programs include both discount-bearing constructs (for example, Savings Plans, committed-use discounts) and non-discount constructs that reserve capacity in advance (for example, capacity reservations, zonal reservations), when those constructs are treated by the provider as commitments.

## Requirements

The CommitmentEligibilityDetails column adheres to the following requirements:

* CommitmentEligibilityDetails MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports at least one type of [*commitment*](#glossary:commitment) program.
* CommitmentEligibilityDetails MUST be of type String.
* CommitmentEligibilityDetails MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* CommitmentEligibilityDetails MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* CommitmentEligibilityDetails MUST be null when a charge is not eligible for any commitment program.
* CommitmentEligibilityDetails MUST be populated when a charge is eligible for a commitment program, regardless of whether a commitment was actually applied to the line item.
* CommitmentEligibilityDetails MUST NOT consider transient account configurations or quotas that might temporarily prevent purchase or participation in a commitment program.
* CommitmentEligibilityDetails MUST include all publicly available commitment programs for which the usage is eligible.
* CommitmentEligibilityDetails SHOULD include negotiated commitment programs for which the usage is eligible.
* CommitmentEligibilityDetails MUST NOT include data related to [term](#glossary:term) lengths or payment options.
* CommitmentEligibilityDetails MUST conform to [CommitmentEligibilityDetailsObject](#datasets.costandusage.commitmenteligibilitydetails.commitmenteligibilitydetailsobject) requirements when CommitmentEligibilityDetails is not null.

## Commitment Eligibility Details Object

Commitment Eligibility Details consists of a valid JSON object with top-level property keys representing categories of commitment programs. Each key contains an array of objects describing the specific commitment types available for the line item's usage.

### Object Requirements

The CommitmentEligibilityDetailsObject adheres to the following requirements:
* CommitmentEligibilityDetailsObject MUST have at least one top-level property key when not null.
* CommitmentEligibilityDetailsObject MAY have a top-level property key "CommitmentDiscountTypes".
* CommitmentEligibilityDetailsObject MAY have a top-level property key "CapacityReservationTypes" for commitment programs whose primary purpose is to reserve capacity rather than to provide a unit discount.
* CommitmentEligibilityDetailsObject MAY contain additional data generator-defined top-level property keys for future or provider-specific commitment categories.
* CommitmentEligibilityDetailsObject MUST have property keys that begin with the string "x\_" unless it is a FOCUS-defined property key.
* CommitmentEligibilityDetailsObject.CommitmentDiscountTypes adheres to the following requirements:
  * CommitmentEligibilityDetailsObject.CommitmentDiscountTypes MUST be of type Array.
  * CommitmentEligibilityDetailsObject.CommitmentDiscountTypes MUST contain one or more objects.
  * Each entry in CommitmentEligibilityDetailsObject.CommitmentDiscountTypes MUST be of type JSON Object.
  * CommitmentEligibilityDetailsObject.CommitmentDiscountTypes MUST have a property key "Type".
  * CommitmentEligibilityDetailsObject.CommitmentDiscountTypes MAY contain additional data generator-defined property keys.
  * CommitmentEligibilityDetailsObject.CommitmentDiscountTypes MUST have property keys that begin with the string "x\_" unless it is a FOCUS-defined property key.
  * CommitmentEligibilityDetailsObject.CommitmentDiscountTypes.Type MUST be of type String.
  * CommitmentEligibilityDetailsObject.CommitmentDiscountTypes.Type MUST NOT be null.
  * CommitmentEligibilityDetailsObject.CommitmentDiscountTypes.Type MUST correspond to a commitment program type supported by the provider (e.g., "SavingsPlan", "ReservedInstance", "CommittedUseDiscount").
  * CommitmentEligibilityDetailsObject.CommitmentDiscountTypes.Type MUST be consistent with strings used in [CommitmentDiscountType](#datasets.costandusage.commitmentdiscounttype) when CommitmentDiscountType is populated by the provider.
  * CommitmentEligibilityDetailsObject.CommitmentDiscountTypes.Type SHOULD correspond to terminology disclosed by the provider in public documentation when CommitmentDiscountType is not populated by the provider.
* CommitmentEligibilityDetailsObject.CapacityReservationTypes adheres to the following requirements:
  * CommitmentEligibilityDetailsObject.CapacityReservationTypes MUST be of type Array.
  * CommitmentEligibilityDetailsObject.CapacityReservationTypes MUST contain one or more objects.
  * Each entry in CommitmentEligibilityDetailsObject.CapacityReservationTypes MUST be of type JSON Object.
  * CommitmentEligibilityDetailsObject.CapacityReservationTypes MUST have a property key "Type".
  * CommitmentEligibilityDetailsObject.CapacityReservationTypes MAY contain additional data generator-defined property keys.
  * CommitmentEligibilityDetailsObject.CapacityReservationTypes MUST have property keys that begin with the string "x_" unless it is a FOCUS-defined property key.
  * CommitmentEligibilityDetailsObject.CapacityReservationTypes.Type MUST be of type String.
  * CommitmentEligibilityDetailsObject.CapacityReservationTypes.Type MUST NOT be null.
  * CommitmentEligibilityDetailsObject.CapacityReservationTypes.Type MUST correspond to a capacity-reservation-style commitment program supported by the provider (for example, "CapacityReservation", "ZonalReservation").
  
### Top-Level Properties

| Property                  | Type  | Required    | Description                                                                                                                   |
|:-----------------|:-----------------|:-----------------|:-----------------|
| `CommitmentDiscountTypes` | Array | Conditional | Array of objects identifying [*commitment discount*](#glossary:commitment-discount) programs for which the usage is eligible. |
| `CapacityReservationTypes` | Array | Conditional | Array of objects identifying capacity-reservation commitment programs (for example, capacity reservations, zonal reservations) for which the usage is eligible. |

### CommitmentDiscountTypes Entry

| Key  | ValueType                            | Required | Description                                                                |
|:-----------------|:-----------------|:-----------------|:-----------------|
| Type | [String](#attributes.stringhandling) | True     | The specific type of commitment discount program available for this usage. |

### CapacityReservationTypes Entry

| Key  | ValueType                            | Required | Description                                                                |
|:-----------------|:-----------------|:-----------------|:-----------------|
| Type | [String](#attributes.stringhandling) | True     | The specific type of capacity-reservation commitment program available for this usage. |

### Object Example

``` json
{
  "CommitmentDiscountTypes": [
    { "Type": "SavingsPlan" },
    { "Type": "ReservedInstance" }
  ],
  "CapacityReservationTypes": [
    { "Type": "CapacityReservation" },
    { "Type": "ZonalReservation" }
  ]
}
```

### JSON Type Definition

``` json
{
  "definitions": {
    "commitmentDiscountTypeEntry": {
      "properties": {
        "Type": { "type": "string" }
      }
    }
  },
  "optionalProperties": {
    "CommitmentDiscountTypes": {
      "elements": { "ref": "commitmentDiscountTypeEntry" }
    }
  }
}
```

NOTE: The above JSON Type Definition (JTD) is an approximation of the expected contents of this column, but it should not be considered normative because it cannot accurately describe the normative requirements (above) for CommitmentEligibilityDetails. Where there are discrepancies, deference will be given to the normative requirements.

### Object ID

CommitmentEligibilityDetailsObject

### Object Display Name

Commitment Eligibility Details Object

## Column ID

CommitmentEligibilityDetails

## Display Name

Commitment Eligibility Details

## Description

The types of [*commitment*](#glossary:commitment) programs available for a specific usage line item.

## Content constraints

| Constraint    | Value                                                                                                                        |
|:-------------------------------------|:---------------------------------|
| Dataset       | [Cost and Usage](#datasets.costandusage)                                                                                     |
| Column type   | Dimension                                                                                                                    |
| Feature level | Conditional                                                                                                                  |
| Allows nulls  | True                                                                                                                         |
| Data type     | String                                                                                                                       |
| Value format  | [JsonObjectFormat](#attributes.jsonobjectformat)                                                                             |
| Object        | [CommitmentEligibilityDetailsObject](#datasets.costandusage.commitmenteligibilitydetails.commitmenteligibilitydetailsobject) |

## Introduced (version)

1.4