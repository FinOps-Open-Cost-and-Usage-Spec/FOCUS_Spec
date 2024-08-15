# Service Subcategory

The Service Subcategory is the second-highest-level classification of a [*service*](#glossary:service) based on its core function.  The Service Subcategory (in conjunction with the Service Category) is commonly used for scenarios like analyzing costs across providers and tracking the migration of workloads across fundamentally different architectures.  The Service Subcategory is a child of the Service Category, and each Service Subcategory value must have one and only one Service Category parent. Though a given *service* can have multiple purposes, each *service* should have one and only one Subcategory that best aligns with its primary purpose. 

The ServiceSubcategory column MUST be present in a FOCUS dataset and MUST NOT be null. This column is of type String and MUST be one of the allowed values.

## Column ID

ServiceSubcategory

## Display Name

Service Subcategory

## Description

Second-highest-level classification of a *service* based on its core function.

## Content Constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column type     | Dimension      |
| Feature level   | Mandatory      |
| Allows nulls    | False          |
| Data type       | String         |
| Value format    | Allowed Values |

Allowed values:

| Service Category          | Service Subcategory               | Service Subcategory Description |
| ------------------------- | --------------------------------- | ------------------------------- |
| AI and Machine Learning   | Generative AI                     |                                 |
|                           | Language AI                       |                                 |
|                           | Machine Learning                  |                                 |
|                           | Search                            |                                 |
|                           | Bots                              |                                 |
|                           | Other (AI and Machine Learning)   |                                 |
|                           |                                   |                                 |
| Analytics                 | Analytics Platform                |                                 |
|                           | Business Intelligence             |                                 |
|                           | Streaming Analytics               |                                 |
|                           | Data Processing                   |                                 |
|                           | Other (Analytics)                 |                                 |
|                           |                                   |                                 |
| Business Applications     | Other (Business Applications)     |                                 |
|                           |                                   |                                 |
| Compute                   | Virtual Machines                  |                                 |
|                           | End User Computing                |                                 |
|                           | Containers                        |                                 |
|                           | Serverless Compute                |                                 |
|                           | Quantum                           |                                 |
|                           | Other (Compute)                   |                                 |
|                           |                                   |                                 |
| Databases                 | Data Warehouse                    |                                 |
|                           | Relational                        |                                 |
|                           | NoSQL                             |                                 |
|                           | Caching                           |                                 |
|                           | Ledger                            |                                 |
|                           | Time Series                       |                                 |
|                           | Other (Databases)                 |                                 |
|                           |                                   |                                 |
| Developer Tools           | Other (Developer Tools)           |                                 |
|                           |                                   |                                 |
| Identity                  | Other (Identity)                  |                                 |
|                           |                                   |                                 |
| Integration               | API Management                    |                                 |
|                           | Messaging                         |                                 |
|                           | Workflow Automation               |                                 |
|                           | Other (Integration)               |                                 |
|                           |                                   |                                 |
| Internet of Things        | Other (Internet of Things)        |                                 |
|                           |                                   |                                 |
| Management and Governance | Administration                    |                                 |
|                           | Architecture                      |                                 |
|                           | Cost Management                   |                                 |
|                           | Compliance                        |                                 |
|                           | Data Governance                   |                                 |
|                           | Disaster Recovery                 |                                 |
|                           | Observability                     |                                 |
|                           | Support                           |                                 |
|                           | Other (Management and Governance) |                                 |
|                           |                                   |                                 |
| Media                     | Other (Media)                     |                                 |
|                           |                                   |                                 |
| Migration                 | Other (Migration)                 |                                 |
|                           |                                   |                                 |
| Mobile                    | Other (Mobile)                    |                                 |
|                           |                                   |                                 |
| Multicloud                | Other (Multicloud)                |                                 |
|                           |                                   |                                 |
| Networking                | Virtual Network                   |                                 |
|                           | NAT                               |                                 |
|                           | VPN                               |                                 |
|                           | Content Delivery Network          |                                 |
|                           | Dedicated Network                 |                                 |
|                           | Load Balancing                    |                                 |
|                           | DNS                               |                                 |
|                           | Network Monitoring                |                                 |
|                           | Private Link                      |                                 |
|                           | Remote Access                     |                                 |
|                           | Data Transfer                     |                                 |
|                           | Firewall                          |                                 |
|                           | Telecommunications                |                                 |
|                           | Other (Networking)                |                                 |
|                           |                                   |                                 |
| Security                  | CSPM                              |                                 |
|                           | Secrets, Certificates, and Keys   |                                 |
|                           | SIEM                              |                                 |
|                           | Threat Detection                  |                                 |
|                           | Other (Security)                  |                                 |
|                           |                                   |                                 |
| Storage                   | Object Storage                    |                                 |
|                           | Disk                              |                                 |
|                           | Files                             |                                 |
|                           | Bulk Transfer                     |                                 |
|                           | Backups                           |                                 |
|                           | Other (Storage)                   |                                 |
|                           |                                   |                                 |
| Web                       | Other (Web)                       |                                 |
|                           |                                   |                                 |
| Other                     | Other (Other)                     |

## Introduced (version)

1.1
