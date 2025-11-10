# Contract Commitment

The Contract Commitment dataset is a supporting dataset that describes the terms of contracts agreed between a service provider and a customer.

<div class='h4-nonindex'>Columns</div>

| Column                                                             | Column Type | Feature Level | Allows Nulls | Data Type |
| ------------------------------------------------------------------ | ----------- | ------------- | ------------ | --------- |
| [Billing Currency](#billingcurrency-1)                             | Dimension   | Mandatory     | True         | String    |
| [Contract Commitment Category](#contractcommitmentcategory)        | Dimension   | Mandatory     | False        | String    |
| [Contract Commitment Cost](#contractcommitmentcost)                | Metric      | Mandatory     | True         | Numeric   |
| [Contract Commitment Description](#contractcommitmentdescription)  | Dimension   | Mandatory     | True         | String    |
| [Contract Commitment ID](#contractcommitmentid-1)                  | Dimension   | Mandatory     | False        | String    |
| [Contract Commitment Period End](#contractcommitmentperiodend)     | Dimension   | Mandatory     | False        | Date/Time |
| [Contract Commitment Period Start](#contractcommitmentperiodstart) | Dimension   | Mandatory     | False        | Date/Time |
| [Contract Commitment Quantity](#contractcommitmentquantity)        | Metric      | Mandatory     | True         | Numeric   |
| [Contract Commitment Type](#contractcommitmenttype)                | Dimension   | Mandatory     | False        | String    |
| [Contract Commitment Unit](#contractcommitmentunit)                | Dimension   | Mandatory     | True         | String    |
| [Contract ID](#contractid-1)                                       | Dimension   | Mandatory     | False        | String    |
| [Contract Period End](#contractperiodend)                          | Dimension   | Mandatory     | False        | Date/Time |
| [Contract Period Start](#contractperiodstart)                      | Dimension   | Mandatory     | False        | Date/Time |

<div class='h4-nonindex'>Relationships</div>

The Contract Commitment dataset can be joined to the Cost and Usage dataset through the use of Contract Commitment ID.

* In the Contract Commitment dataset, Contract Commitment ID is a column.
* In the Cost and Usage dataset, Contract Commitment ID is a property within a JSON object array provided in Contract Applied column.

| Dataset A           | Dataset A Column       | Dataset B      | Dataset B Column |
| ------------------- | ---------------------- | -------------- | -----------------|
| Contract Commitment | Contract Commitment ID | Cost and Usage | Contract Applied |

<div class='h4-nonindex'>Requirements</div>

ContractCommitment adheres to the following requirements:

* ContractCommitment MUST be present when the service provider supports *contract commitments*.
* ContractCommitment MUST conform to [ColumnHandling](#columnhandling) requirements.
* ContractCommitment MUST conform to [NullHandling](#nullhandling) requirements.

<div class='h4-nonindex'>Dataset ID</div>

ContractCommitment

<div class='h4-nonindex'>Display Name</div>

Contract Commitment

<div class='h4-nonindex'>Description</div>

Describes the terms of contracts agreed between a service provider and a customer.

<div class='h4-nonindex'>Introduced (version)</div>

1.3
