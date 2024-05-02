# Usage Unit

## Example provider mappings

Current column mappings found in available data sets:

| Provider  | Data set                | Provider column        |
|:----------|:------------------------|:-----------------------|
| AWS       | CUR                     | pricing/unit (pricing not usage) |
| GCP       | BigQuery Billing Export | usage.unit             |
| Microsoft | Cost details            | UnitOfMeasure Quantity |

## Example scenarios for current provider data

Current values observed in billing data for various scenarios:

| Provider | Provider Column | Example Value                                          |
|:---------|:----------------|:-------------------------------------------------------|
| AWS      | pricing_unit    | Gigabyte, Month, Requests, GB-MONTH, Hrs, Seconds      |
| GCP      | usage.unit      | Gigabyte, hour, mebibyte, second, month                |
| Azure    | UnitOfMeasure   | 1 GB, 1 GB/Month, 100 Hours, 1/Day, 10K, 1 GiB Second  |

## Discussion Topics

* AWS and Azure Usage Units are not currently meeting the requirements recommended by the UnitFormat attribute. As such values from these providers are not recommended to be used directly. The formatting should be updated on values in Actual Unit and Pricing Unit columns.
