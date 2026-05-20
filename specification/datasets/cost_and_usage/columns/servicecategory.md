# Service Category

The Service Category is the highest-level classification of a [*service*](#glossary:service) based on the core function of the *service*. Each *service* should have one and only one category that best aligns with its primary purpose. The Service Category is commonly used for scenarios like analyzing costs across service providers and tracking the migration of workloads across fundamentally different architectures.

## Requirements

ServiceCategory MUST adhere to the following requirements:

* ServiceCategory MUST be of type String.
* ServiceCategory MUST NOT be null.
* ServiceCategory MUST be one of the allowed values.

## Allowed Values

| Service Category          | Description                                                                                                                 |
| :------------------------ | :-------------------------------------------------------------------------------------------------------------------------- |
| AI and Machine Learning   | Artificial Intelligence and Machine Learning related technologies.                                                          |
| Analytics                 | Data processing, analytics, and visualization capabilities.                                                                 |
| Business Applications     | Business and productivity applications and services.                                                                        |
| Compute                   | Computing infrastructure and services, including physical, virtual, containerized, serverless, or high-performance.         |
| Databases                 | Database platforms and services that allow for storage and querying of data.                                                |
| Developer Tools           | Software development and delivery tools and services.                                                                       |
| External Data             | Subscriptions to third-party data sets, market intelligence, or external API feeds.                                         |
| Facilities                | Physical space, rent, power, cooling, and colocation services.                                                              |
| Hardware                  | Physical IT equipment including servers, racks, switches, and storage arrays.                                               |
| Identity                  | Identity and access management services.                                                                                    |
| Integration               | Services that allow applications to interact with one another.                                                              |
| Internet of Things        | Development and management of IoT devices and networks.                                                                     |
| Management and Governance | Management, logging, and observability of a customer's infrastructure, applications, and services.                          |
| Media                     | Media and entertainment streaming and processing services.                                                                  |
| Migration                 | Moving applications and data between environments or providers.                                                             |
| Mobile                    | Services enabling applications to interact via mobile technologies.                                                         |
| Multicloud                | Support for the interworking of multiple discrete provider and/or on-premises environments.                                 |
| Networking                | Network connectivity and management.                                                                                        |
| Professional Services     | Consulting, implementation, architectural guidance, and managed service engagements.                                         |
| Security                  | Security monitoring and compliance services.                                                                                |
| Software Licensing        | Standalone software licenses, operating systems, hypervisors, and software subscriptions procured independently. |
| Storage                   | Storage services for structured or unstructured data.                                                                       |
| Support                   | Premium customer support plans, technical assistance, and maintenance contracts.                                            |
| Telecommunications        | External voice and data transmission lines, circuits, and physical connectivity.                                            |
| Web                       | Services enabling applications to interact via the Internet.                                                                |
| Other                     | New or emerging services that do not align with an existing category.                                                       |

## Column ID

ServiceCategory

## Display Name

Service Category

## Description

Highest-level classification of a *service* based on the core function of the *service*.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | Allowed values                                       |

## Version Introduced

0.5
