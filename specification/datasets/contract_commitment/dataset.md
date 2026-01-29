# Contract Commitment

The Contract Commitment dataset is a supporting dataset that describes the terms of contracts agreed between a service provider and a customer.

## Columns<!--SkipTOC-->

| Column                                                             | Column Type | Feature Level | Allows Nulls | Data Type |
| ------------------------------------------------------------------ | ----------- | ------------- | ------------ | --------- |
| [Billing Currency](#datasets.contractcommitment.billingcurrency)                             | Dimension   | Mandatory     | True         | String    |
| [Contract Commitment Category](#datasets.contractcommitment.contractcommitmentcategory)        | Dimension   | Mandatory     | False        | String    |
| [Contract Commitment Cost](#datasets.contractcommitment.contractcommitmentcost)                | Metric      | Mandatory     | True         | Numeric   |
| [Contract Commitment Description](#datasets.contractcommitment.contractcommitmentdescription)  | Dimension   | Mandatory     | True         | String    |
| [Contract Commitment ID](#datasets.contractcommitment.contractcommitmentid)                  | Dimension   | Mandatory     | False        | String    |
| [Contract Commitment Period End](#datasets.contractcommitment.contractcommitmentperiodend)     | Dimension   | Mandatory     | False        | Date/Time |
| [Contract Commitment Period Start](#datasets.contractcommitment.contractcommitmentperiodstart) | Dimension   | Mandatory     | False        | Date/Time |
| [Contract Commitment Quantity](#datasets.contractcommitment.contractcommitmentquantity)        | Metric      | Mandatory     | True         | Numeric   |
| [Contract Commitment Type](#datasets.contractcommitment.contractcommitmenttype)                | Dimension   | Mandatory     | False        | String    |
| [Contract Commitment Unit](#datasets.contractcommitment.contractcommitmentunit)                | Dimension   | Mandatory     | True         | String    |
| [Contract ID](#datasets.contractcommitment.contractid)                                       | Dimension   | Mandatory     | False        | String    |
| [Contract Period End](#datasets.contractcommitment.contractperiodend)                          | Dimension   | Mandatory     | False        | Date/Time |
| [Contract Period Start](#datasets.contractcommitment.contractperiodstart)                      | Dimension   | Mandatory     | False        | Date/Time |

## Relationships<!--SkipTOC-->

The Contract Commitment dataset can be joined to the Cost and Usage dataset through the use of Contract Commitment ID.

* In the Contract Commitment dataset, Contract Commitment ID is a column.
* In the Cost and Usage dataset, Contract Commitment ID is a property within a JSON object array provided in Contract Applied column.

| Dataset A           | Dataset A Column       | Dataset B      | Dataset B Column |
| ------------------- | ---------------------- | -------------- | -----------------|
| Contract Commitment | Contract Commitment ID | Cost and Usage | Contract Applied |

## Requirements<!--SkipTOC-->

ContractCommitment adheres to the following requirements:

* ContractCommitment MUST be present when the service provider supports *contract commitments*.
* ContractCommitment MUST conform to [ColumnHandling](#attributes.columnhandling) requirements.
* ContractCommitment MUST conform to [DatasetCompleteness](#attributes.datasetcompleteness) requirements.
* ContractCommitment MUST conform to [NullHandling](#attributes.nullhandling) requirements.

## Dataset ID<!--SkipTOC-->

ContractCommitment

## Display Name<!--SkipTOC-->

Contract Commitment

## Description<!--SkipTOC-->

Describes the terms of contracts agreed between a service provider and a customer.

## Introduced (version)<!--SkipTOC-->

1.3
