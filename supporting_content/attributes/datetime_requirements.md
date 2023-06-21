# Datetime Requirements

## Example provider mappings

Current column mappings found in available data sets:

| Provider  | Data set                 | Column                                               |
|:----------|:-------------------------|:-----------------------------------------------------|
| AWS       | CUR                      | lineItem/UsageStartDate, lineItem/UsageEndDate, etc. |
| GCP       | Big Query Billing Export | usage_start_time, usage_end_time, etc.               |
| Microsoft | Cost details             | date, etc.                                           |

### Documentation

* AWS: ?
* GCP: ?
* Microsoft: ?

## Example usage scenarios

Current values observed in billing data for various scenarios:

| Provider  | Data set                                        | Example Value        |
|:----------|:------------------------------------------------|:---------------------|
| AWS       | CUR                                             | 2023-05-13T21:00:00Z |
| GCP       | Big Query Billing Export                        | 2023-05-13T21:00:00Z |
| Microsoft | Cost details via Consumption API (usageDetails) | 2023-05-13T00:00:00Z |
| Microsoft | Cost details via Cost export file               | 05/13/2023           |

## Discussion / Scratch space

* Date related dimension in Azure Cost exports are not aligned with ISO 8601 and those provided in Consumption Usage Details API are (Note: the API will be retired at some point)
* Dates should always have time / timezone to avoid ambiguity. Will result in more space usage but the additional clarity is justified
* Oddities in time / date / timezone
  * Azure provides daily level data without hourly granularity. Is it wasteful to have to specify the full date/time?
  * GCP uses PST for timezone
* All datetime columns currently defined in the FOCUS specification (scope of FOCUS v0.5) provide information about a specific point in time. For this purpose, the extended format with separators (hyphens and colons) was chosen (provides consistency and improved readability). When and if the need arises, additional formats will be specified (e.g., for datetime intervals, duration, etc.).
