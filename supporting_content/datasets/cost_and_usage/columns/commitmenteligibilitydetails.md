# Column: CommitmentEligibilityDetails

## Example

The following scenarios illustrate how CommitmentEligibilityDetails are populated across different providers, including major cloud platforms and SaaS data platforms.

| ServiceProviderName | ServiceName       | ChargeClass | CommitmentEligibilityDetails                                                                                                  |
|--------------|--------------|--------------|-----------------|
| AWS                 | AmazonEC2         | Usage       | {"CommitmentDiscountTypes": [{"Type": "SavingsPlan"}, {"Type": "ReservedInstance"}]}                                          |
| Azure               | Virtual Machines  | Usage       | {"CommitmentDiscountTypes": [{"Type": "SavingsPlan"}, {"Type": "ReservedInstance"}]}                                          |
| Google              | Kubernetes Engine | Usage       | {"CommitmentDiscountTypes": [{"Type": "ResourceBasedCommittedUseDiscount"}, {"Type": "ComputeFlexibleCommittedUseDiscount"}]} |
| Snowflake           | Warehouse         | Usage       | {"CommitmentDiscountTypes": [{"Type": "CapacityCommitment"}]}                                                                 |
| Databricks          | Jobs              | Usage       | {"CommitmentDiscountTypes": [{"Type": "CommittedUseDiscount"}]}                                                               |
| Datadog             | Infrastructure    | Usage       | {"CommitmentDiscountTypes": [{"Type": "MonthlyCommitment"}, {"Type": "AnnualCommitment"}]}                                    |
| AWS                 | AmazonS3          | Usage       | null                                                                                                                          |

## Example usage scenarios

**AWS (On-Demand EC2 Usage)**

An On-Demand EC2 instance that is not currently covered by any commitment but is eligible for both Savings Plan and Reserved Instance.

| ServiceProviderName | ServiceName | ChargeClass | CommitmentEligibilityDetails                                                         |
|---------------|---------------|---------------|---------------|
| AWS                 | AmazonEC2   | Usage       | {"CommitmentDiscountTypes": [{"Type": "SavingsPlan"}, {"Type": "ReservedInstance"}]} |

**Google Cloud (Fully covered GKE Usage)**

A GKE cluster usage row that is covered by a Resource-based Committed Use Discount (CUD), but could also have been covered by a Compute Flexible CUD.

| ServiceProviderName | ServiceName       | ChargeClass | CommitmentEligibilityDetails                                                                                                  |
|---------------|---------------|---------------|---------------|
| Google              | Kubernetes Engine | Usage       | {"CommitmentDiscountTypes": [{"Type": "ResourceBasedCommittedUseDiscount"}, {"Type": "ComputeFlexibleCommittedUseDiscount"}]} |

**Databricks**

Databricks Units (DBUs) consumed by a Jobs cluster. This usage is eligible for coverage under a Databricks Committed Use Discount plan.

| ServiceProviderName | ServiceName | ChargeClass | CommitmentEligibilityDetails                                    |
|---------------|---------------|---------------|---------------|
| Databricks          | Jobs        | Usage       | {"CommitmentDiscountTypes": [{"Type": "CommittedUseDiscount"}]} |

**Ineligible Usage**

Standard S3 Storage usage or a support fee, which is not eligible for any commitment program.

| ServiceProviderName | ServiceName | ChargeClass | CommitmentEligibilityDetails |
|---------------|---------------|---------------|---------------|
| AWS                 | AmazonS3    | Usage       | null                         |

**Negotiated commitment (provider opts in)**

OCI Compute usage eligible for Universal Credits. Because Universal Credits are negotiated, providers MAY include them at their discretion. This example shows a provider that chooses to include them.

| ServiceProviderName | ServiceName     | ChargeClass | CommitmentEligibilityDetails                                |
|---------------|---------------|---------------|---------------|
| Oracle              | Virtual Machine | Usage       | {"CommitmentDiscountTypes": [{"Type": "UniversalCredits"}]} |
