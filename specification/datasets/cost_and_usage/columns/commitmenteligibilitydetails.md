# Commitment Eligibility Details

Commitment Eligibility Details presents all types of usage based [*commitment*](#glossary:commitment) programs available for a specific usage line item. This column allows practitioners to distinguish between usage that is or in the past has been eligible for a [*commitment discount*](#glossary:commitment-discount) and usage that lacks such an option, enabling the calculation of true coverage.

## Requirements

CommitmentEligibilityDetails adheres to the following requirements:

* CommitmentEligibilityDetailsDetails MUST be present in Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports at least one type of [*commitment discount*](#glossary:commitment-discount) program.
* CommitmentEligibilityDetails MUST be of type String.
* CommitmentEligibilityDetails MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* CommitmentEligibilityDetails MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* CommitmentEligibilityDetails nullability is defined as follows:
  * CommitmentEligibilityDetails MUST be null if the usage is not eligible for any non-negotiated commitment.
  * CommitmentEligibilityDetails MUST NOT be null if the usage is eligible for any non-negotiated commitment.
* CommitmentEligibilityDetails MUST correspond to defined [commitment](#glossary:commitment) program types (e.g., "SavingsPlan", "ReservedInstance", "CUD") or vendor-specific pricing tiers (e.g., "MonthlyCommitment").
* The values in CommitmentEligibilityDetails MUST be consistent with strings used in [CommitmentDiscountType](#datasets.costandusage.commitmentdiscounttype) for the provider.
* CommitmentEligibilityDetails MUST NOT include data related to [term](#glossary:term) lengths or payment options.

### Object Schema Requirements

CommitmentEligibilityDetails consists of a valid JSON object which contains a list of commitment discount types that are applicable to the line item's usage.

When CommitmentEligibilityDetails is not null, the JsonObjectFormat for CommitmentEligibilityDetails adheres to the following requirements:

* CommitmentEligibilityDetails MUST have a top-level key "EligibleCommitmentTypes" which contains an array.
* The "EligibleCommitmentTypes" array MUST contain one or more strings.
* Each string in the "EligibleCommitmentTypes" array MUST correspond to a valid commitment discount program type supported by the provider (e.g., "SavingsPlan", "ReservedInstance", "CommittedUseDiscount").
* Where possible, values in "EligibleCommitmentTypes" SHOULD correspond to values used in the [CommitmentDiscountType](#datasets.costandusage.commitmentdiscounttype) column for consistency.
* CommitmentEligibilityDetails root object MAY contain additional data generator-defined keys (e.g., vendor-specific eligibility constraints), provided they do not conflict with FOCUS-defined keys.

### Examples

The CommitmentEligibilityDetails object contains a list of commitment discount programs that are applicable to the line item's usage.

### Array Entries

Array contains one or more strings, representing the specific commitment programs:

| Value | ValueType | Required | Description |
| ----- | ---- | ---------- | ----------- |
| [CommitmentDiscountType](#datasets.costandusage.commitmentdiscounttype) | [String](#attributes.stringhandling) | True | The specific type of commitment discount (e.g., "SavingsPlan", "ReservedInstance", "CommittedUseDiscount") or vendor-specific pricing model (e.g., "MonthlyCommitment") available for this usage. |

### Example

```json
{
  "EligibleCommitmentTypes": [
    "SavingsPlan",
    "ReservedInstance"
  ]
}
```

## Column ID

CommitmentEligibilityDetails

## Display Name

Commitment Eligibility Details

## Description

The types of non-negotiated *commitment* programs available for the specific usage line item.

## Content constraints

| Constraint      | Value         |
|:----------------|:--------------|
| Column type     | Dimension     |
| Feature level   | Conditional   |
| Allows nulls    | True          |
| Data type       | String        |
| Value format    | [JsonObjectFormat](#attributes.jsonobjectformat) |

## Introduced (version)

1.4