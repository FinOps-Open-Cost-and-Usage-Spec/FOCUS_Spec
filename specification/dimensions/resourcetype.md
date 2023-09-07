# Resource Type

A Resource ID is an identifier assigned to a resource by the provider. The Resource ID is commonly used for cost reporting, analysis, and allocation scenarios.  While Resource ID and Resource Name identifies a unique instance of a resource, the Resource Type describes the identity of the resource. Resource Type is commonly used for cost reporting, analysis, and allocation scenarios.

The ResourceType column MUST be present within billing data.  ResourceType MUST be of type String and MUST NOT be NULL when a corresponding ResourceId is not NULL.  When a corresponding ResourceId value is NULL, the ResourceType column value MUST be NULL.

## Column ID

ResourceType

## Display Name

Resource Type

## Description

Classifiable description of a corresponding ResourceId

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
