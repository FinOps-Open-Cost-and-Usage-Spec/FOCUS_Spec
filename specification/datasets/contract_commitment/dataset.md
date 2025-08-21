| Column                                                             | Column Type | Feature Level | Allows Nulls | Data Type | Value Format            |
| ------------------------------------------------------------------ | ----------- | ------------- | ------------ | --------- | ----------------------- |
| [Contract Commitment ID](#contractcommitmentid-1)                  | Dimension   | Mandatory     | False        | String    | \<not specified>        |
| [Contract ID](#contractid-1)                                       | Dimension   | Mandatory     | False        | String    | \<not specified>        |
| [Contract Start](#contractstart)                                   | Dimension   | Mandatory     | False        | Date/Time | Date/Time Format        |
| [Contract End](#contractend)                                       | Dimension   | Mandatory     | False        | Date/Time | Date/Time Format        |
| [Contract Commitment Period Start](#contractcommitmentperiodstart) | Dimension   | Mandatory     | False        | Date/Time | Date/Time Format        |
| [Contract Commitment Period End](#contractcommitmentperiodend)     | Dimension   | Mandatory     | False        | Date/Time | Date/Time Format        |
| [Contract Commitment Description](#contractcommitmentdescription)  | Dimension   | Mandatory     | True         | String    | \<not specified>        |
| [Contract Commitment Type](#contractcommitmenttype)                | Dimension   | Mandatory     | True         | String    | \<not specified>        |
| [Contract Commitment Category](#contractcommitmentcategory)        | Dimension   | Mandatory     | False        | String    | Allowed Values          |
| [Contract Commitment Unit](#contractcommitmentunit)                | Dimension   | Mandatory     | True         | String    | \<not specified>        |
| [Contract Commitment Quantity](#contractcommitmentquantity)        | Metric      | Mandatory     | True         | Numeric   | Any valid decimal value |
| [Contract Commitment Cost](#contractcommitmentcost)                | Metric      | Mandatory     | True         | Numeric   | Any valid decimal value |
