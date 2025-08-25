# Contract Commitment

The Contract Commitment dataset is a supporting dataset that describes the terms of contracts agreed between a provider and a customer.

## Columns

| Column                                                             | Column Type | Feature Level | Allows Nulls | Data Type | Value Format            |
| ------------------------------------------------------------------ | ----------- | ------------- | ------------ | --------- | ----------------------- |
| [Contract Commitment ID](#contractcommitmentid-1)                  | Dimension   | Mandatory     | False        | String    | \<not specified>        |
| [Contract ID](#contractid-1)                                       | Dimension   | Mandatory     | False        | String    | \<not specified>        |
| [Contract Period Start](#contractperiodstart)                      | Dimension   | Mandatory     | False        | Date/Time | Date/Time Format        |
| [Contract Period End](#contractperiodend)                          | Dimension   | Mandatory     | False        | Date/Time | Date/Time Format        |
| [Contract Commitment Period Start](#contractcommitmentperiodstart) | Dimension   | Mandatory     | False        | Date/Time | Date/Time Format        |
| [Contract Commitment Period End](#contractcommitmentperiodend)     | Dimension   | Mandatory     | False        | Date/Time | Date/Time Format        |
| [Contract Commitment Description](#contractcommitmentdescription)  | Dimension   | Mandatory     | True         | String    | \<not specified>        |
| [Contract Commitment Type](#contractcommitmenttype)                | Dimension   | Mandatory     | False        | String    | \<not specified>        |
| [Contract Commitment Category](#contractcommitmentcategory)        | Dimension   | Mandatory     | False        | String    | Allowed Values          |
| [Contract Commitment Unit](#contractcommitmentunit)                | Dimension   | Conditional   | True         | String    | \<not specified>        |
| [Contract Commitment Quantity](#contractcommitmentquantity)        | Metric      | Conditional   | True         | Numeric   | Any valid decimal value |
| [Contract Commitment Cost](#contractcommitmentcost)                | Metric      | Conditional   | True         | Numeric   | Any valid decimal value |

## Relationships

The Contract Commitment dataset can be joined to the Cost and Usage dataset through the use of the Contract Commitment ID field.

| Dataset A           | Dataset A Column       | Dataset B      | Dataset B Column       |
| ------------------- | ---------------------- | -------------- | ---------------------- |
| Contract Commitment | Contract Commitment ID | Cost and Usage | Contract Commitment ID |

## Requirements

The ContractCommitment dataset adheres to the following requirements:

* ContractCommitment MUST be present when the provider supports *contract commitments*.

## Dataset ID

ContractCommitment

## Display Name

Contract Commitment

## Description

Describes the terms of contracts agreed between a provider and a customer.

## Introduced (version)

1.3
