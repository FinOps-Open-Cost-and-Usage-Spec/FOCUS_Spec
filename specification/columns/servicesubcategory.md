# Service Subcategory

The Service Subcategory is a secondary classification of the Service Category for a [*service*](#glossary:service) based on its core function. The Service Subcategory (in conjunction with the Service Category) is commonly used for scenarios like analyzing spend and usage for specific workload types across providers and tracking the migration of workloads across fundamentally different architectures.  

* The ServiceSubcategory column MUST be present in a FOCUS dataset and MUST NOT be null.
* This column is of type String and MUST be one of the allowed values.
* Each Service Subcategory value MUST have one and only one Service Category parent.
* Though a given *service* can have multiple purposes, each *service* SHOULD have one and only one Subcategory that best aligns with its primary purpose.

## Column ID

ServiceSubcategory

## Display Name

Service Subcategory

## Description

Secondary classification of the Service Category for a *service* based on its core function.

## Content Constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column type     | Dimension      |
| Feature level   | Optional      |
| Allows nulls    | False          |
| Data type       | String         |
| Value format    | Allowed Values |

Allowed values:

| Service Category          | Service Subcategory               | Service Subcategory Description                                                                                      |
| ------------------------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| AI and Machine Learning   | AI Platforms                      | Framework of tools for development and deployment of AI-powered applications.                                        |
| AI and Machine Learning   | Bots                              | Automated performance of tasks such as customer service, data collection, and content moderation.                    |
| AI and Machine Learning   | Generative AI                     | Creation of content like text, images, and music by learning patterns from existing data.                            |
| AI and Machine Learning   | Machine Learning                  | Creation, training, and deployment of statistical algorithms that learn from and perform tasks based on data.        |
| AI and Machine Learning   | Natural Language Processing       | Generation of human language, handling tasks like translation, sentiment analysis, and text summarization.           |
| AI and Machine Learning   | Other (AI and Machine Learning)   | AI and Machine Learning services that do not fall into one of the defined subcategories.                             |
| Analytics                 | Analytics Platforms               | Unified solution that combines technologies across the entire analytics lifecycle.          |
| Analytics                 | Business Intelligence             | Semantic models, dashboards, reports, and data visualizations to track performance and identify trends.              |
| Analytics                 | Data Processing                   | Integration and transformation tasks to prepare data for analysis.                                                   |
| Analytics                 | Search                            | Discovery of information by indexing and retrieving data from various sources.                                       |
| Analytics                 | Streaming Analytics               | Real-time data stream processes to detect patterns, trends, and anomalies as they occur.                             |
| Analytics                 | Other (Analytics)                 | Analytics services that do not fall into one of the defined subcategories.                                           |
| Business Applications     | Business Functions                | Tools that pertain to specific departments or subject areas within an organization.                                  |
| Business Applications     | Productivity and Collaboration    | Tools that facilitate individuals managing tasks and working together.                                               |
| Business Applications     | Other (Business Applications)     | Business Applications services that do not fall into one of the defined subcategories.                               |
| Compute                   | Containers                        | Management and orchestration of containerized compute platforms.                                                     |
| Compute                   | End User Computing                | Virtualized desktop infrastructure and device / endpoint management.                                                 |
| Compute                   | Quantum                           | Resources and simulators that leverage the principles of quantum mechanics.                                          |
| Compute                   | Serverless Compute                | Enablement of compute capabilities without provisioning or managing servers.                                         |
| Compute                   | Virtual Machines                  | Computing environments created by abstracting resources from physical hardware.                                      |
| Compute                   | Other (Compute)                   | Compute services that do not fall into one of the defined subcategories.                                             |
| Databases                 | Cache Databases                   | Low-latency and high-throughput access to frequently accessed data.                                                  |
| Databases                 | Data Warehouses                   | Big data storage and querying capabilities.                                                                          |
| Databases                 | Ledger Databases                  | Immutable and transparent databases to record tamper-proof and cryptographically secure transactions.                |
| Databases                 | NoSQL Databases                   | Unstructured or semi-structured data storage and querying capabilities.                                              |
| Databases                 | Relational Databases              | Structured data storage and querying capabilities.                                                                   |
| Databases                 | Time Series Databases             | Time-stamped data storage and querying capabilities.                                                                 |
| Databases                 | Other (Databases)                 | Database services that do not fall into one of the defined subcategories.                                            |
| Developer Tools           | Developer Platforms               | Unified solution that combines technologies across multiple areas of the software development lifecycle.                                                  |
| Developer Tools           | Continuous Integration and Deployment                        | CI/CD tools and services that support building and deploying code for software and systems.           |
| Developer Tools           | Development                       | Tools and services that support authoring code for software and systems.                                             |
| Developer Tools           | Quality Assurance                 | Tools and services that support testing code for software and systems.                                               |
| Developer Tools           | Other (Developer Tools)           | Developer Tools services that do not fall into one of the defined subcategories.                                     |
| Identity                  | Identity and Access Management    | Technologies that ensure users have appropriate access to resources.                                                 |
| Identity                  | Other (Identity)                  | Identity services that do not fall into one of the defined subcategories.                                            |
| Integration               | API Management                    | Creation, publishing, and management of application programming interfaces.                                          |
| Integration               | Integration Platforms             | Unified solution that combines technologies across messaging, management, and automation.                     |
| Integration               | Messaging                         | Asynchronous communication between distributed applications.                                                         |
| Integration               | Workflow Automation               | Design, execution, and management of business processes and workflows.                                               |
| Integration               | Other (Integration)               | Integration services that do not fall into one of the defined subcategories.                                         |
| Internet of Things        | IoT Analytics                     | Examination of data collected from IoT devices.                                                                      |
| Internet of Things        | IoT Platforms                     | Unified solution that combines technologies across IoT data collection, processing, visualization, and device management. |
| Internet of Things        | Other (Internet of Things)        | Internet of Things (IoT) services that do not fall into one of the defined subcategories.                            |
| Management and Governance | Architecture                      | Planning, design, and construction of software systems.                                                              |
| Management and Governance | Compliance                        | Adherance to regulatory standards and industry best practices.                                                       |
| Management and Governance | Cost Management                   | Monitoring and controlling expenses of systems and services.                                                         |
| Management and Governance | Data Governance                   | Management of the availability, usability, integrity, and security of data.                                          |
| Management and Governance | Disaster Recovery                 | Plans and procedures that ensure systems and services can recover from disruptions.                                  |
| Management and Governance | Endpoint Management               | Tools that configure and secure access to devices.                                                                   |
| Management and Governance | Observability                     | Monitoring, logging, and tracing of data to track the performance and health of systems.                             |
| Management and Governance | Support                           | Assistance and expertise supplied by providers.                                                                      |
| Management and Governance | Other (Management and Governance) | Management and governance services that do not fall into one of the defined subcategories.                           |
| Media                     | Content Creation                  | Production and sharing of media content.                                                                             |
| Media                     | Gaming                            | Development and consumption of games.                                                                                |
| Media                     | Media Streaming                   | Multimedia delivered and rendered in real-time on devices.                                                           |
| Media                     | Mixed Reality                     | Technologies that blend real-world and computer-generated environments.                                              |
| Media                     | Other (Media)                     | Media services that do not fall into one of the defined subcategories.                                               |
| Migration                 | Data Migration                    | Movement of data workloads from one location to another.                                                             |
| Migration                 | Resource Migration                | Movement of resources from one location to another.                                                                  |
| Migration                 | Other (Migration)                 | Migration services that do not fall into one of the defined subcategories.                                           |
| Mobile                    | Other (Mobile)                    | All Mobile services.                                                                                                 |
| Multicloud                | Multicloud Platforms              | Environments that facilitate consumption of services from multiple cloud providers.                                  |
| Multicloud                | Other (Multicloud)                | Multicloud services that do not fall into one of the defined subcategories.                                          |
| Networking                | Content Delivery                  | Distribution of digital content using a network of servers (CDNs).                                                   |
| Networking                | Load Balancing                    | Distribution of incoming network traffic across multiple servers to prevent server overload.                         |
| Networking                | Network Connectivity              | Movement of data between systems, locations, or formats via data migration, synchronization, and replication tasks.  |
| Networking                | Network Infrastructure            | Configuration, monitoring, and troubleshooting of network devices.                                                   |
| Networking                | Network Security                  | Protection from unauthorized network access and cyber threats using firewalls, VPNs, and anti-malware tools.         |
| Networking                | Other (Networking)                | Networking services that do not fall into one of the defined subcategories.                                          |
| Security                  | Secret Management                 | Information used to authenticate users and systems, including secrets, certificates, tokens, and other keys.         |
| Security                  | Security Posture Management       | Tools that help organizations configure, monitor, and improve system security.                                       |
| Security                  | Threat Detection and Response     | Collect and analyze security data to identify and respond to potential security threats and vulnerabilities.         |
| Security                  | Other (Security)                  | Security services that do not fall into one of the defined subcategories.                                            |
| Storage                   | Backup Storage                    | Secondary storage to protect against data loss.                                                                      |
| Storage                   | Block Storage                     | High performance, low latency storage that provides random access.                                                   |
| Storage                   | Data Transfer                     | Secure, high-speed, and offline transfer of stored data from one location to another.                                |
| Storage                   | File Storage                      | Scalable, sharable storage for file-based data.                                                                      |
| Storage                   | Object Storage                    | Highly available, durable storage for unstructured data.                                                             |
| Storage                   | Storage Platforms                 | Unified solution that supports multiple storage types.                                                               |
| Storage                   | Other (Storage)                   | Storage services that do not fall into one of the defined subcategories.                                             |
| Web                       | Application Frameworks            | Standardized software components used in application development.                                                    |
| Web                       | Web Platforms                     | Integrated environments that run web applications.                                                                   |
| Web                       | Other (Web)                       | Web services that do not fall into one of the defined subcategories.                                                 |
| Other                     | Other (Other)                     | Services that do not fall into one of the defined categories.                                                        |

## Introduced (version)

1.1
