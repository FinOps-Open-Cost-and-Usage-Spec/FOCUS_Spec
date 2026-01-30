# Commitment Eligibility Details

Commitment Eligibility Details presents all types of usage based [*commitment*](#glossary:commitment) programs available for a specific usage line item. This column allows practitioners to distinguish between usage that is or in the past has been eligible for a [*commitment discount*](#glossary:commitment-discount) and usage that lacks such an option, enabling the calculation of true coverage.

## Requirements

CommitmentEligibilityDetails adheres to the following requirements:

* CommitmentEligibilityDetailsDetails MUST be present in Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports at least one type of [*commitment discount*](#glossary:commitment-discount) program.
* CommitmentEligibilityDetails MUST be of type String.
* CommitmentEligibilityDetails MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* CommitmentEligibilityDetails MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* CommitmentEligibilityDetails MUST be null if the usage is not eligible for any non-negotiated commitment.
* CommitmentEligibilityDetails MUST correspond to defined [commitment](#glossary:commitment) program types (e.g., "SavingsPlan", "ReservedInstance", "CUD") or vendor-specific pricing tiers (e.g., "MonthlyCommitment").
* The values in CommitmentEligibilityDetails MUST be consistent with strings used in [CommitmentDiscountType](#datasets.costandusage.commitmentdiscounttype) for the provider.
* CommitmentEligibilityDetails MUST NOT include data related to [term](#glossary:term) lengths or payment options.

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
| Feature level   | Recommended   |
| Allows nulls    | True          |
| Data type       | String        |
| Value format    | [JsonObjectFormat](#attributes.jsonobjectformat) |

## Introduced (version)

1.4