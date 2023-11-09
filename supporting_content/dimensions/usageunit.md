# Usage Unit

## Example provider mappings 

Current column mappings found in available data sets:

| Provider  | Data set                | Provider column        |
|-----------|-------------------------|------------------------|
| AWS       | CUR                     | pricing/unit	       |
| GCP       | BigQuery Billing Export | usage_unit             |
| Microsoft | Cost details            | UnitOfMeasure Quantity |

## Example scenarios for current provider data

Current values observed in billing data for various scenarios:
| Provider | Provider Column | Example Value                                                   |
|----------|-----------------|-----------------------------------------------------------------|
| AWS      | pricing_unit    | Gigabyte, Month, Requests, GB-MONTH, Hrs, Seconds           |
| GCP      | Usage_unit      | Gigabyte, hour, mebibyte, second, month                        |
| Azure    | UnitOfMeasure   | 1 GB, 1 GB/Month, 100 Hours, 1/Day, 10K, 1 GiB Second      |
