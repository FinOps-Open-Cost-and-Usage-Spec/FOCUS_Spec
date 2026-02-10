# Column: CommitmentEligibilityDetails

## Example

The following scenarios illustrate how CommitmentEligibilityDetails is populated across different providers, including major cloud platforms and SaaS data platforms.

| Provider | Service | ChargeClass | CommitmentEligibilityDetails |
|----------|---------|-------------|------------------------------|
| AWS | AmazonEC2 | Usage | {"EligibleCommitmentTypes": ["SavingsPlan", "ReservedInstance"]} |
| Azure | Virtual Machines | Usage | {"EligibleCommitmentTypes": ["SavingsPlan"]} |
| Google | Kubernetes Engine | Usage | {"EligibleCommitmentTypes": ["CommittedUseDiscount"]} |
| Oracle | Virtual Machine | Usage | {"EligibleCommitmentTypes": ["UniversalCredits"]} |
| Snowflake | Warehouse | Usage | {"EligibleCommitmentTypes": ["CapacityCommitment"]} |
| Databricks | Jobs | Usage | {"EligibleCommitmentTypes": ["CommittedUseDiscount"]} |
| AWS | AmazonS3 | Usage | null |

## Example usage scenarios

Current values observed in billing data for various scenarios:

**Scenario 1: AWS (On-Demand EC2 Usage)**
An On-Demand EC2 instance that is not currently covered by any commitment but is eligible for both Savings Plan and Reserved Instance.
`AWS` | `AmazonEC2` | `Usage` | `null` | `{"EligibleCommitmentTypes": ["SavingsPlan", "ReservedInstance"]}`

**Scenario 2: Azure (Partially covered Virtual Machine Usage)**
A Virtual Machine usage row that is partially covered by Savings Plan.
`Azure` | `Virtual Machines` | `Usage` | `null` | `{"EligibleCommitmentTypes": ["SavingsPlan", "ReservedInstance"]}`

**Scenario 3: Google Cloud (Fully covered GKE Usage)**
A GKE cluster usage row that is covered by a Resource-based Committed Use Discount (CUD), but could also have been covered by a Compute Flexible CUD.
`Google` | `Kubernetes Engine` | `Usage` | `null` | `{"EligibleCommitmentTypes": ["ResourceBasedCommittedUseDiscount", "ComputeFlexibleCommittedUseDiscount"]}`

**Scenario 4: Oracle Cloud Infrastructure (Standard Rates)**
OCI Compute usage that is charged at standard rates but is eligible to burn down a "Universal Credits" commitment contract.
`Oracle` | `Virtual Machine` | `Usage` | `null` | `{"EligibleCommitmentTypes": ["UniversalCredits"]}`

**Scenario 5: Datadog (Monthly and Annual Commitment)**
An On-Demand infrastructure host usage row (potentially billed as overage). This usage is eligible for coverage under a Monthly commitment plan (e.g., Pro Monthly) or an Annual commitment plan, both of which offer lower rates than On-Demand.
`Datadog` | `Infrastructure` | `Usage` | `null` | `{"EligibleCommitmentTypes": ["MonthlyCommitment", "AnnualCommitment"]}`

**Scenario 6: Databricks**
Databricks Units (DBUs) consumed by a Jobs cluster. This usage is eligible for coverage under a Databricks Committed Use Discount plan.
`Databricks` | `Jobs` | `Usage` | `null` | `{"EligibleCommitmentTypes": ["CommittedUseDiscount"]}`

**Scenario 7: Ineligible Usage**
Standard S3 Storage usage or a support fee, which is strictly not eligible for any standard commitment discount program.
`AWS` | `AmazonS3` | `Usage` | `null` | `null`