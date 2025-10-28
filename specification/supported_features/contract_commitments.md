# Contract Commitments

## Description

FOCUS supports the tracking of commitments made via contractual agreements between a provider and a customer. Each row in the Cost and Usage dataset is associated with one or more unique identifiers representing those contracts and contract commitments, stored in a JSON column called Contract Applied. A richer amount of detail that describes those commitments is carried in a separate Contract Commitment dataset, which can be joined to the Cost and Usage datset to facilitate various queries involving filtering and aggregation.

The Contract Applied column contains several FOCUS-defined properties.  For more information, see the definition of Contract Applied [here](#contractapplied).

## Directly Dependent Columns

* CostAndUsage
  * ContractApplied

## Supporting Columns

* ContractCommitment
  * BillingCurrency
  * ContractCommitmentCategory
  * ContractCommitmentCost
  * ContractCommitmentDescription
  * ContractCommitmentId
  * ContractCommitmentPeriodEnd
  * ContractCommitmentPeriodStart
  * ContractCommitmentQuantity
  * ContractCommitmentType
  * ContractCommitmentUnit
  * ContractId
  * ContractPeriodEnd
  * ContractPeriodStart

## Example SQL Query

### Report on Initial Contract Commitment

TBD

```sql
SELECT
  MIN(ChargePeriodStart) AS ChargePeriodStart,
  MAX(ChargePeriodEnd) AS ChargePeriodEnd,
  ServiceProviderName,
  JSON_VALUE(ContractApplied, '$.ContractId') AS ContractId,
  JSON_VALUE(ContractApplied, '$.ContractCommitmentId') AS ContractCommitmentId,
  BillingAccountId
  ChargeFrequency,
  SUM(BilledCost) AS TotalBilledCost
FROM CostAndUsage
WHERE ChargePeriodStart >= ? AND ChargePeriodEnd < ?
  AND ChargeCategory = 'Purchase'
GROUP BY
  ServiceProviderName,
  BillingAccountId
```

### Report on Usage Against Contract Commitment

TBD

```sql
SELECT
  MIN(ChargePeriodStart) AS ChargePeriodStart,
  MAX(ChargePeriodEnd) AS ChargePeriodEnd,
  ServiceProviderName,
  JSON_VALUE(ContractApplied, '$.ContractId') AS ContractId,
  JSON_VALUE(ContractApplied, '$.ContractCommitmentId') AS ContractCommitmentId,
  BillingAccountId
  ChargeFrequency,
  SUM(BilledCost) AS TotalBilledCost
FROM CostAndUsage
WHERE ChargePeriodStart >= ? AND ChargePeriodEnd < ?
  AND ChargeCategory = 'Usage'
GROUP BY
  ServiceProviderName,
  BillingAccountId
```

### Report on Usage Against Contract Commitment by Category

TBD

## Introduced (Version)

1.3
