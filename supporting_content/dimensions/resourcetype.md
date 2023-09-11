# Column: ResourceType

## Example Resource Type mappings

The following is a list of potential Resource Type values that could exist across AWS, Azure, and GCP.

| Resource Type             | AWS                       | Azure                                 | GCP                               |
|:------------------------- |:------------------------- |:------------------------------------- |:--------------------------------- |
| Virtual Machine           | EC2 Virtual Machine       | Azure Virtual Machine                 | Compute Engine Virtual Machine    |
| Disk                      | EBS Volume                | Managed Disk                          | Persistent Disk                   |
| Serverless Function       | Lambda Function           | Azure Function                        | Cloud Functions Function          |
| Blob Storage Bucket       | S3 Bucket                 | Blob Storage Container                | GCS Bucket                        |
| File System               | EFS File System           | File Storage                          | File Store                        |
| Load Balancer             | Elastic Load Balancer     | Public Load Balancer                  | Cloud Load Balancer               |
| Relational Database       | Amazon Aurora             | Database for MySQL/Postgres Cluster   | CloudSQL Cluster                  |
| Data Warehouse            | Redshift Cluster          | Synapse Analytics Warehouse           | BigQuery Storage/Analysis         |

## Discussion / Scratch Space

- Too much effort to ask for Resource Type normalization across clouds.
- Provider-based Resource Type is the first step towards potentially normalizing across clouds.
- Happy medium is a provider-based ResourceType
- It should be a required field that is nullable
