| Column                          | Column Type | Feature Level | Allows nulls | Data Type | Value Format             |
| ------------------------------- | ----------- | ------------- | ------------ | --------- | ------------------------ |
| [Contract Commitment ID](#contractcommitmentid)          | Dimension   | Mandatory     | FALSE        | String    | \<not specified>         |
| Contract ID                     | Dimension   | Mandatory     | FALSE        | String    | \<not specified>         |
| Contract Start                  | Dimension   | Mandatory     | FALSE        | Date/Time | Date/Time Format         |
| Contract End                    | Dimension   | Mandatory     | FALSE        | Date/Time | Date/Time Format         |
| Contract Commitment Start       | Dimension   | Mandatory     | FALSE        | Date/Time | Date/Time Format         |
| Contract Commitment End         | Dimension   | Mandatory     | FALSE        | Date/Time | Date/Time Format         |
| Contract Commitment Description | Dimension   | Mandatory     | TRUE         | String    | \<not specified>         |
| Contract Commitment Type        | Dimension   | Mandatory     | TRUE         | String    | \<not specified>         |
| Contract Commitment Category    | Dimension   | Mandatory     | FALSE        | String    | Allowed Values           |
| Contract Commitment Unit        | Dimension   | Mandatory     | TRUE         | String    | \<not specified>         |
| Contract Commitment Quantity    | Metric      | Mandatory     | TRUE         | Numeric   | Any valid decimal value  |
| Contract Commitment Cost        | Metric      | Mandatory     | TRUE         | Numeric   | Any valid decimal value  |
