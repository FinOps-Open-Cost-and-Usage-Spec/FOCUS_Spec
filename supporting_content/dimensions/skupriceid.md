## Example provider mappings 

Current column mappings found in available data sets:

| **Provider** | **Data set**                | **Column**                             |
| ------------ | --------------------------- | -------------------------------------- |
| AWS          | CUR                         | pricing/rate\_code \| pricing/rate\_id |
| Azure        | Cost details export or API  | ProductID                              |
| GCP          | Big Query Export            | sku.id                                 |
| OCI          | Cost Reports                | cost/productSKU (no price level ID)    |


## Example scenarios for current provider data

Current values observed in billing data for various scenarios:

| **Provider** | **Scenario**               | **Pattern**                                                              |
| ------------ | -------------------------- | ------------------------------------------------------------------------ |
| AWS          | CUR                        | rate\_code: KF338J7FCKZPUBD9.JRTCKXETXF.6YS6EN2CT7 rate\_id: 20457007287 |
| Azure        | Cost Details export or API | DZH318Z0BNZH006F                                                                         |
| GCP          | Big Query                  | F1ED-0732-5BDA                                                           |
| OCI          | Cost Reports               | B93382 (no price level ID)                                               |
