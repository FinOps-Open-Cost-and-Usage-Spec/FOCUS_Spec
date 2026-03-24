# Column: CommitmentEligibilityDetails

## Example

The following scenarios illustrate how CommitmentEligibilityDetails are populated across different providers, including major cloud and SaaS platforms.

| ServiceProviderName | ServiceName      | CommitmentEligibilityDetails                                                                                                           |
|----------|----------|-------------------------------------------|
| Provider A          | ComputeService   | {"CommitmentPrograms": [{"ProgramType": "SavingsPlan"}, {"ProgramType": "ReservedInstance"}]}                                          |
| Provider B          | Container Engine | {"CommitmentPrograms": [{"ProgramType": "ResourceBasedCommittedUseDiscount"}, {"ProgramType": "ComputeFlexibleCommittedUseDiscount"}]} |
| Provider C          | Infrastructure   | {"CommitmentPrograms": [{"ProgramType": "MonthlyCommitment"}, {"ProgramType": "AnnualCommitment"}]}                                    |
| Provider D          | ObjectStorage    | null                                                                                                                                   |

## Example usage scenarios

**Provider A (Flexible Compute Usage)**

Scenario: A compute instance that is not currently covered by any commitment but is eligible for Savings Plan and Reserved Instance programs, offering flexibility in pricing models.

| ServiceProviderName | ServiceName    | CommitmentEligibilityDetails                                                                  |
|------------|------------|---------------------------------------|
| Provider A          | ComputeService | {"CommitmentPrograms": [{"ProgramType": "SavingsPlan"}, {"ProgramType": "ReservedInstance"}]} |

**Provider B (Committed Container Cluster Usage)**

Scenario: A container cluster usage row that is covered by a Resource-based Committed Use Discount but could also have been covered by a Compute Flexible plan.

| ServiceProviderName | ServiceName      | CommitmentEligibilityDetails                                                                                                           |
|----------|----------|-------------------------------------------|
| Provider B          | Container Engine | {"CommitmentPrograms": [{"ProgramType": "ResourceBasedCommittedUseDiscount"}, {"ProgramType": "ComputeFlexibleCommittedUseDiscount"}]} |

**Provider C (Infrastructure with Subscription Commitment)**

Scenario: An infrastructure host usage row eligible for Monthly and Annual commitment-based pricing, offering lower effective rates than On-Demand usage.

| ServiceProviderName | ServiceName    | CommitmentEligibilityDetails                                                                        |
|-----------|-----------|----------------------------------------|
| Provider C          | Infrastructure | {"CommitmentPrograms": [{"ProgramType": "MonthlyCommitment"}, {"ProgramType": "AnnualCommitment"}]} |

**Provider D (Ineligible Object Storage Usage)**

Scenario: Standard object storage usage or a support fee, which is not eligible for any commitment program.

| ServiceProviderName | ServiceName   | CommitmentEligibilityDetails |
|---------------------|---------------|------------------------------|
| Provider D          | ObjectStorage | null                         |
