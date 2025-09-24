# Contract Commitment

The Contract Commitment dataset is a supporting dataset that describes the terms of contracts agreed between a provider and a customer.

<div class='h4-nonindex'>Columns</div>

| Column                                                             | Column Type | Feature Level | Allows Nulls | Data Type | Value Format            |
| ------------------------------------------------------------------ | ----------- | ------------- | ------------ | --------- | ----------------------- |
| [Billing Currency](#billingcurrency-1)                             | Dimension   | Mandatory     | True         | String    | Currency Format         |
| [Contract Commitment ID](#contractcommitmentid-1)                  | Dimension   | Mandatory     | False        | String    | \<not specified>       |
| [Contract ID](#contractid-1)                                       | Dimension   | Mandatory     | False        | String    | \<not specified>       |
| [Contract Period Start](#contractperiodstart)                      | Dimension   | Mandatory     | False        | Date/Time | Date/Time Format        |
| [Contract Period End](#contractperiodend)                          | Dimension   | Mandatory     | False        | Date/Time | Date/Time Format        |
| [Contract Commitment Period Start](#contractcommitmentperiodstart) | Dimension   | Mandatory     | False        | Date/Time | Date/Time Format        |
| [Contract Commitment Period End](#contractcommitmentperiodend)     | Dimension   | Mandatory     | False        | Date/Time | Date/Time Format        |
| [Contract Commitment Description](#contractcommitmentdescription)  | Dimension   | Mandatory     | True         | String    | \<not specified>       |
| [Contract Commitment Type](#contractcommitmenttype)                | Dimension   | Mandatory     | False        | String    | \<not specified>       |
| [Contract Commitment Category](#contractcommitmentcategory)        | Dimension   | Mandatory     | False        | String    | Allowed Values          |
| [Contract Commitment Unit](#contractcommitmentunit)                | Dimension   | Mandatory     | True         | String    | \<not specified>       |
| [Contract Commitment Quantity](#contractcommitmentquantity)        | Metric      | Mandatory     | True         | Numeric   | Any valid decimal value |
| [Contract Commitment Cost](#contractcommitmentcost)                | Metric      | Mandatory     | True         | Numeric   | Any valid decimal value |

<div class='h4-nonindex'>Relationships</div>

The Contract Commitment dataset can be joined to the Cost and Usage dataset through the use of Contract Commitment ID.

* In the Contract Commitment dataset, Contract Commitment ID is a column.
* In the Cost and Usage dataset, Contract Commitment ID is a property within a JSON object array.

| Dataset A           | Dataset A Column       | Dataset B      | Dataset B Column |
| ------------------- | ---------------------- | -------------- | -----------------|
| Contract Commitment | Contract Commitment ID | Cost and Usage | Contract Applied |

<div class='h4-nonindex'>Requirements</div>

The ContractCommitment dataset adheres to the following requirements:

* ContractCommitment MUST be present when the provider supports *contract commitments*.

<div class='h4-nonindex'>Dataset ID</div>

ContractCommitment

<div class='h4-nonindex'>Display Name</div>

Contract Commitment

<div class='h4-nonindex'>Description</div>

Describes the terms of contracts agreed between a provider and a customer.

<div class='h4-nonindex'>Introduced (version)</div>

1.3
