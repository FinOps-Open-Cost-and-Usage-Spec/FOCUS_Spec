# Product Category

The Product Category is the highest-level classification of a product that can be used or purchased within an overarching service based on its core function. Each product should have one and only one category that best aligns to its primary purpose. The Product Category may be the same as the Service Category, but can also differ as many services utilize multiple products based on their needs. As an example, a virtual machine may use compute, network, and storage products in order to deliver its core compute service functionality. The Product Category is commonly used for scenarios like analyzing cost trends across providers and identifying anomalous cost patterns.

The ProductCategory column MUST be present and MUST NOT be null or empty. This column is of type String and MUST be one of the allowed values.

## Column ID

ProductCategory

## Display Name

Product Category

## Description

Highest-level classification of a product that can be used or purchased within an overarching service based on its core function.

## Content Constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column required | True           |
| Data type       | String         |
| Allows nulls    | False          |
| Value format    | List of values |

Allowed values:

| Product Category          | Description                                                                                    |
| ------------------------- | ---------------------------------------------------------------------------------------------- |
| AI and Machine Learning   | Artificial Intelligence and Machine Learning related technologies.                             |
| Analytics                 | Data processing, analytics, and visualization capabilities.                                    |
| Business Applications     | Business and productivity applications and products.                                           |
| Compute                   | Virtual, containerized, serverless, or high-performance computing infrastructure and products. |
| Databases                 | Database platforms and products that allow for storage and querying of data.                   |
| Developer Tools           | Software development and delivery tools and products.                                          |
| Multicloud                | Support for interworking of multiple cloud and/or on-premises environments.                    |
| Identity                  | Identity and access management products.                                                       |
| Integration               | Products that allow applications to interact with one another.                                 |
| Internet of Things        | Development and management of IoT devices and networks.                                        |
| Management and Governance | Management, logging, and observability of a customer's use of cloud.                           |
| Media                     | Media and entertainment streaming and processing products.                                     |
| Migration                 | Moving applications and data to the cloud.                                                     |
| Mobile                    | Products enabling cloud applications to interact via mobile technologies.                      |
| Networking                | Network connectivity and management.                                                           |
| Security                  | Security monitoring and compliance products.                                                   |
| Storage                   | Storage products for structured or unstructured data.                                          |
| Web                       | Products enabling cloud applications to interact via the Internet.                             |
| Other                     | New or emerging products that do not align with an existing category.                          |

## Introduced (version)

1.0
