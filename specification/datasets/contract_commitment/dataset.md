| Column                                          | Column Type | Feature Level | Allows Nulls | Data Type | Value Format            |
| ----------------------------------------------- | ----------- | ------------- | ------------ | --------- | ----------------------- |
| [Contract Commitment ID](#contractcommitmentid-1) | Dimension   | Mandatory     | False        | String    | \<not specified>       |
| Contract ID                                     | Dimension   | Mandatory     | False        | String    | \<not specified>       |
| Contract Start                                  | Dimension   | Mandatory     | False        | Date/Time | Date/Time Format        |
| Contract End                                    | Dimension   | Mandatory     | False        | Date/Time | Date/Time Format        |
| Contract Commitment Start                       | Dimension   | Mandatory     | False        | Date/Time | Date/Time Format        |
| Contract Commitment End                         | Dimension   | Mandatory     | False        | Date/Time | Date/Time Format        |
| Contract Commitment Description                 | Dimension   | Mandatory     | True         | String    | \<not specified>       |
| Contract Commitment Type                        | Dimension   | Mandatory     | True         | String    | \<not specified>       |
| Contract Commitment Category                    | Dimension   | Mandatory     | False        | String    | Allowed Values          |
| Contract Commitment Unit                        | Dimension   | Mandatory     | True         | String    | \<not specified>       |
| Contract Commitment Quantity                    | Metric      | Mandatory     | True         | Numeric   | Any valid decimal value |
| Contract Commitment Cost                        | Metric      | Mandatory     | True         | Numeric   | Any valid decimal value |
