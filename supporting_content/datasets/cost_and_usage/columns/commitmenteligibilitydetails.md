# Column: CommitmentEligibilityDetails

## Example

The following scenarios illustrate how CommitmentEligibilityDetails are populated across different providers, including major cloud platforms and SaaS data platforms.

| Provider   | Service           | ServiceSubcategory | ChargeClass | CommitmentEligibilityDetails                                                                                                  |
|---------------|---------------|--------------------|---------------|---------------------------|
| AWS        | AmazonEC2         | Compute            | Usage       | {"CommitmentDiscountTypes": [{"Type": "SavingsPlan"}, {"Type": "ReservedInstance"}]}                                          |
| Azure      | Virtual Machines  | VirtualMachine     | Usage       | {"CommitmentDiscountTypes": [{"Type": "SavingsPlan"}, {"Type": "ReservedInstance"}]}                                          |
| Google     | Kubernetes Engine | Node               | Usage       | {"CommitmentDiscountTypes": [{"Type": "ResourceBasedCommittedUseDiscount"}, {"Type": "ComputeFlexibleCommittedUseDiscount"}]} |
| Snowflake  | Warehouse         | n/a                | Usage       | {"CommitmentDiscountTypes": [{"Type": "CapacityCommitment"}]}                                                                 |
| Databricks | Jobs              | n/a                | Usage       | {"CommitmentDiscountTypes": [{"Type": "CommittedUseDiscount"}]}                                                               |
| Datadog    | Infrastructure    | Host               | Usage       | {"CommitmentDiscountTypes": [{"Type": "MonthlyCommitment"}, {"Type": "AnnualCommitment"}]}                                    |
| AWS        | AmazonS3          | StandardStorage    | Usage       | null                                                                                                                          |

## Example usage scenarios

**AWS (On-Demand EC2 Usage)**

An On-Demand EC2 instance that is not currently covered by any commitment but is eligible for both Savings Plan and Reserved Instance.

| Provider | Service   | ChargeClass | CommitmentDiscountStatus | CommitmentEligibilityDetails                                                         |
|---------------|---------------|---------------|---------------|---------------|
| AWS      | AmazonEC2 | Usage       | null                     | {"CommitmentDiscountTypes": [{"Type": "SavingsPlan"}, {"Type": "ReservedInstance"}]} |

**Google Cloud (Fully covered GKE Usage)**

A GKE cluster usage row that is covered by a Resource-based Committed Use Discount (CUD), but could also have been covered by a Compute Flexible CUD.

| Provider | Service           | ChargeClass | CommitmentDiscountStatus | CommitmentEligibilityDetails                                                                                                  |
|---------------|---------------|---------------|---------------|---------------|
| Google   | Kubernetes Engine | Usage       | null                     | {"CommitmentDiscountTypes": [{"Type": "ResourceBasedCommittedUseDiscount"}, {"Type": "ComputeFlexibleCommittedUseDiscount"}]} |

**Databricks**

Databricks Units (DBUs) consumed by a Jobs cluster. This usage is eligible for coverage under a Databricks Committed Use Discount plan.

| Provider   | Service | ChargeClass | CommitmentDiscountStatus | CommitmentEligibilityDetails                                    |
|---------------|---------------|---------------|---------------|---------------|
| Databricks | Jobs    | Usage       | null                     | {"CommitmentDiscountTypes": [{"Type": "CommittedUseDiscount"}]} |

**Ineligible Usage**

Standard S3 Storage usage or a support fee, which is not eligible for any commitment program.

| Provider | Service  | ChargeClass | CommitmentDiscountStatus | CommitmentEligibilityDetails |
|---------------|---------------|---------------|---------------|---------------|
| AWS      | AmazonS3 | Usage       | null                     | null                         |

**Negotiated commitment (provider opts in)**

OCI Compute usage eligible for Universal Credits. Because Universal Credits are negotiated, providers MAY include them at their discretion. This example shows a provider that chooses to include them.

| Provider | Service         | ChargeClass | CommitmentDiscountStatus | CommitmentEligibilityDetails                                |
|---------------|---------------|---------------|---------------|---------------|
| Oracle   | Virtual Machine | Usage       | null                     | {"CommitmentDiscountTypes": [{"Type": "UniversalCredits"}]} |


