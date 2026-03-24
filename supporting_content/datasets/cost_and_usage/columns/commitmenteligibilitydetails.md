# Column: CommitmentEligibilityDetails

## Example

The following scenarios illustrate how CommitmentEligibilityDetails are populated across different providers, including major cloud platforms and SaaS data platforms.

| ServiceProviderName | ServiceName       | ChargeClass | CommitmentEligibilityDetails                                                                                                  |
|--------------|--------------|--------------|-----------------|
| AWS                 | AmazonEC2         | Usage       | {"CommitmentPrograms": [{"ProgramType": "SavingsPlan"}, {"ProgramType": "ReservedInstance"}]}                                          |
| Azure               | Virtual Machines  | Usage       | {"CommitmentPrograms": [{"ProgramType": "SavingsPlan"}, {"ProgramType": "ReservedInstance"}]}                                          |
| Google              | Kubernetes Engine | Usage       | {"CommitmentPrograms": [{"ProgramType": "ResourceBasedCommittedUseDiscount"}, {"ProgramType": "ComputeFlexibleCommittedUseDiscount"}]} |
| Snowflake           | Warehouse         | Usage       | {"CommitmentPrograms": [{"ProgramType": "CapacityCommitment"}]}                                                                 |
| Databricks          | Jobs              | Usage       | {"CommitmentPrograms": [{"ProgramType": "CommittedUseDiscount"}]}                                                               |
| Datadog             | Infrastructure    | Usage       | {"CommitmentPrograms": [{"ProgramType": "MonthlyCommitment"}, {"ProgramType": "AnnualCommitment"}]}                                    |
| AWS                 | AmazonS3          | Usage       | null                                                                                                                          |

## Example usage scenarios

**AWS (On-Demand EC2 Usage)**

An On-Demand EC2 instance that is not currently covered by any commitment but is eligible for Savings Plan, Reserved Instance, and capacity reservations.

| ServiceProviderName | ServiceName | ChargeClass | CommitmentEligibilityDetails                                                         |
|---------------|---------------|---------------|---------------|
| AWS                 | AmazonEC2   | Usage       | {"CommitmentPrograms": [{"ProgramType": "SavingsPlan"}, {"ProgramType": "ReservedInstance"}, {"ProgramType": "CapacityReservation"}]} |

**Google Cloud (Fully covered GKE Usage)**

A GKE cluster usage row that is covered by a Resource-based Committed Use Discount (CUD), but could also have been covered by a Compute Flexible CUD.

| ServiceProviderName | ServiceName       | ChargeClass | CommitmentEligibilityDetails                                                                                                  |
|---------------|---------------|---------------|---------------|
| Google              | Kubernetes Engine | Usage       | {"CommitmentPrograms": [{"ProgramType": "ResourceBasedCommittedUseDiscount"}, {"ProgramType": "ComputeFlexibleCommittedUseDiscount"}]} |

**Databricks**

Databricks Units (DBUs) consumed by a Jobs cluster. This usage is eligible for coverage under a Databricks Committed Use Discount plan.

| ServiceProviderName | ServiceName | ChargeClass | CommitmentEligibilityDetails                                    |
|---------------|---------------|---------------|---------------|
| Databricks          | Jobs        | Usage       | {"CommitmentPrograms": [{"ProgramType": "CommittedUseDiscount"}]} |

**Ineligible Usage**

Standard S3 Storage usage or a support fee, which is not eligible for any commitment program.

| ServiceProviderName | ServiceName | ChargeClass | CommitmentEligibilityDetails |
|---------------|---------------|---------------|---------------|
| AWS                 | AmazonS3    | Usage       | null                         |

**Negotiated commitment (provider opts in)**

OCI Compute usage eligible for Universal Credits. Because Universal Credits are negotiated, providers MAY include them at their discretion. This example shows a provider that chooses to include them.

| ServiceProviderName | ServiceName     | ChargeClass | CommitmentEligibilityDetails                                |
|---------------|---------------|---------------|---------------|
| Oracle              | Virtual Machine | Usage       | {"CommitmentPrograms": [{"ProgramType": "UniversalCredits"}]} |