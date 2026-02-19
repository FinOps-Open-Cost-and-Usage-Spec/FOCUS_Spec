# Column: CommitmentEligibilityDetails

## Example

The following scenarios illustrate how CommitmentEligibilityDetails is populated across different providers, including major cloud platforms and SaaS data platforms.

| Provider   | Service           | ChargeClass | CommitmentEligibilityDetails                                                                                                  |
|---------------|---------------|---------------|---------------------------|
| AWS        | AmazonEC2         | Usage       | {"CommitmentDiscountTypes": [{"Type": "SavingsPlan"}, {"Type": "ReservedInstance"}]}                                          |
| Azure      | Virtual Machines  | Usage       | {"CommitmentDiscountTypes": [{"Type": "SavingsPlan"}, {"Type": "ReservedInstance"}]}                                          |
| Google     | Kubernetes Engine | Usage       | {"CommitmentDiscountTypes": [{"Type": "ResourceBasedCommittedUseDiscount"}, {"Type": "ComputeFlexibleCommittedUseDiscount"}]} |
| Snowflake  | Warehouse         | Usage       | {"CommitmentDiscountTypes": [{"Type": "CapacityCommitment"}]}                                                                 |
| Databricks | Jobs              | Usage       | {"CommitmentDiscountTypes": [{"Type": "CommittedUseDiscount"}]}                                                               |
| Datadog    | Infrastructure    | Usage       | {"CommitmentDiscountTypes": [{"Type": "MonthlyCommitment"}, {"Type": "AnnualCommitment"}]}                                    |
| AWS        | AmazonS3          | Usage       | null                                                                                                                          |

## Example usage scenarios

**Scenario 1: AWS (On-Demand EC2 Usage)**

An On-Demand EC2 instance that is not currently covered by any commitment but is eligible for both Savings Plan and Reserved Instance.

| Provider | Service   | ChargeClass | CommitmentDiscountStatus | CommitmentEligibilityDetails                                                         |
|---------------|---------------|---------------|---------------|---------------|
| AWS      | AmazonEC2 | Usage       | null                     | {"CommitmentDiscountTypes": [{"Type": "SavingsPlan"}, {"Type": "ReservedInstance"}]} |

**Scenario 2: Azure (Partially covered Virtual Machine Usage)**

A Virtual Machine usage row that is partially covered by Savings Plan. The eligibility column still reflects all programs this usage qualifies for, regardless of current coverage.

| Provider | Service          | ChargeClass | CommitmentDiscountStatus | CommitmentEligibilityDetails                                                         |
|---------------|---------------|---------------|---------------|---------------|
| Azure    | Virtual Machines | Usage       | null                     | {"CommitmentDiscountTypes": [{"Type": "SavingsPlan"}, {"Type": "ReservedInstance"}]} |

**Scenario 3: Google Cloud (Fully covered GKE Usage)**

A GKE cluster usage row that is covered by a Resource-based Committed Use Discount (CUD), but could also have been covered by a Compute Flexible CUD.

| Provider | Service           | ChargeClass | CommitmentDiscountStatus | CommitmentEligibilityDetails                                                                                                  |
|---------------|---------------|---------------|---------------|---------------|
| Google   | Kubernetes Engine | Usage       | null                     | {"CommitmentDiscountTypes": [{"Type": "ResourceBasedCommittedUseDiscount"}, {"Type": "ComputeFlexibleCommittedUseDiscount"}]} |

**Scenario 4: Datadog (Monthly and Annual Commitment)**

An On-Demand infrastructure host usage row (potentially billed as overage). This usage is eligible for coverage under commitment plans that offer lower rates than On-Demand. Since Datadog does not populate CommitmentDiscountType, the Type values correspond to publicly available program names from Datadog documentation.

| Provider | Service        | ChargeClass | CommitmentDiscountStatus | CommitmentEligibilityDetails                                                               |
|---------------|---------------|---------------|---------------|---------------|
| Datadog  | Infrastructure | Usage       | null                     | {"CommitmentDiscountTypes": [{"Type": "MonthlyCommitment"}, {"Type": "AnnualCommitment"}]} |

**Scenario 5: Databricks**

Databricks Units (DBUs) consumed by a Jobs cluster. This usage is eligible for coverage under a Databricks Committed Use Discount plan.

| Provider   | Service | ChargeClass | CommitmentDiscountStatus | CommitmentEligibilityDetails                                    |
|---------------|---------------|---------------|---------------|---------------|
| Databricks | Jobs    | Usage       | null                     | {"CommitmentDiscountTypes": [{"Type": "CommittedUseDiscount"}]} |

**Scenario 6: Ineligible Usage**

Standard S3 Storage usage or a support fee, which is not eligible for any commitment program.

| Provider | Service  | ChargeClass | CommitmentDiscountStatus | CommitmentEligibilityDetails |
|---------------|---------------|---------------|---------------|---------------|
| AWS      | AmazonS3 | Usage       | null                     | null                         |

**Scenario 7: Negotiated commitment (provider opts in)**

OCI Compute usage eligible for Universal Credits. Because Universal Credits are negotiated, providers MAY include them at their discretion. This example shows a provider that chooses to include them.

| Provider | Service         | ChargeClass | CommitmentDiscountStatus | CommitmentEligibilityDetails                                |
|---------------|---------------|---------------|---------------|---------------|
| Oracle   | Virtual Machine | Usage       | null                     | {"CommitmentDiscountTypes": [{"Type": "UniversalCredits"}]} |
