# Resource Type

A ResourceType is a classifiable description of a corresponding ResourceId.  While the ResourceId identifies a unique instance of a resource, the ResourceType describes the identity of the resource.

The ResourceType column MUST be present within billing data.  ResourceType MUST be of type String and MUST NOT be NULL when a corresponding ResourceId is not NULL.  When a corresponding ResourceId value is NULL, the ResourceType column value MUST be NULL.

## Column ID

ResourceType

## Display Name

Resource Type

## Description

Classifiable description assigned to a corresponding ResourceId

## Normalized?

No

## Data type

String

## Content Constraints

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column required | True            |
| Data type       | String          |
| Allows nulls    | True            |
| Value format    | \<not specified> |

## Introduced (version)

1.0

## Supporting content

The following is a list of potential ResourceType values that could exist across AWS, Azure, and GCP.

| AWS                       | Azure                                 | GCP                               |
|:-----------------------   |:------------------------------------- |:--------------------------------  |
| EC2 Virtual Machine       | Azure Virtual Machine                 | Compute Engine Virtual Machine    |
| EBS Volume                | Managed Disk                          | Persistent Disk                   |
| Lambda Function           | Azure Function                        | Cloud Functions Function          |
| S3 Bucket                 | Blob Storage Container                | GCS Bucket                        |
| EFS File System           | File Storage                          | File Store                        |
| Elastic Load Balancer     | Public Load Balancer                  | Cloud Load Balancer               |
| Relational Database       | Database for MySQL/Postgres Cluster   | CloudSQL Cluster                  |
| Redshift Cluster          | Synapse Analytics Warehouse           | BigQuery Storage/Analysis         |
