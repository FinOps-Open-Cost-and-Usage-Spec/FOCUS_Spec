# Service Category

The Service Category is the highest-level classification of a [*service*](#glossary:service) based on the core function of the *service*. In the Recommendation dataset, the Service Category is commonly used to analyze recommendations across service providers and by workload type. Each *service* should have one and only one category that best aligns with its primary purpose.

## Requirements

ServiceCategory MUST adhere to the following requirements:

* ServiceCategory MUST be of type String.
* ServiceCategory MUST adhere to the following nullability requirements:
  * ServiceCategory MUST be null when a recommendation is not associated with a single *service*.
  * ServiceCategory MUST NOT be null when a recommendation is associated with a single *service*.
* When not null, ServiceCategory MUST be one of the allowed values.

## Allowed Values

| Service Category          | Description                                                                                                                      |
| :------------------------ | :------------------------------------------------------------------------------------------------------------------------------- |
| AI and Machine Learning   | Artificial Intelligence and Machine Learning related technologies.                                                               |
| Analytics                 | Data processing, analytics, and visualization capabilities.                                                                      |
| Business Applications     | Business and productivity applications and services.                                                                             |
| Compute                   | Virtual, containerized, serverless, or high-performance computing infrastructure and services.                                   |
| Databases                 | Database platforms and services that allow for storage and querying of data.                                                     |
| Developer Tools           | Software development and delivery tools and services.                                                                            |
| Identity                  | Identity and access management services.                                                                                         |
| Integration               | Services that allow applications to interact with one another.                                                                   |
| Internet of Things        | Development and management of IoT devices and networks.                                                                          |
| Management and Governance | Management, logging, and observability of a customer's infrastructure, applications, and services.                               |
| Media                     | Media and entertainment streaming and processing services.                                                                       |
| Migration                 | Moving applications and data between environments or providers.                                                                  |
| Mobile                    | Services enabling applications to interact via mobile technologies.                                                              |
| Multicloud                | Support for the interworking of multiple distinct environments across different service providers or on-premises infrastructure. |
| Networking                | Network connectivity and management.                                                                                             |
| Security                  | Security monitoring and compliance services.                                                                                     |
| Storage                   | Storage services for structured or unstructured data.                                                                            |
| Web                       | Services enabling applications to interact via the Internet.                                                                     |
| Other                     | New or emerging services that do not align with an existing category.                                                            |

## Column ID

ServiceCategory

## Display Name

Service Category

## Description

Highest-level classification of a *service* based on the core function of the *service*.

## Content Constraints

| Constraint      | Value                                          |
| :-------------- | :--------------------------------------------- |
| Dataset         | [Recommendation](#datasets.recommendation)     |
| Column type     | Dimension                                      |
| Feature level   | Mandatory                                      |
| Allows nulls    | True                                           |
| Data type       | String                                         |
| Value format    | Allowed values                                 |

## Version Introduced

1.5
