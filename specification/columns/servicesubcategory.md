# Service Subcategory

The Service Subcategory is a secondary classification of the Service Category for a [*service*](#glossary:service) based on its core function. The Service Subcategory (in conjunction with the Service Category) is commonly used for scenarios like analyzing spend and usage for specific workload types across providers and tracking the migration of workloads across fundamentally different architectures.  

- The ServiceSubcategory column MUST be present in a FOCUS dataset and MUST NOT be null. 
- This column is of type String and MUST be one of the allowed values.  
- Each Service Subcategory value MUST have one and only one Service Category parent. 
- Though a given *service* can have multiple purposes, each *service* SHOULD have one and only one Subcategory that best aligns with its primary purpose. 

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
| Feature level   | Mandatory      |
| Allows nulls    | False          |
| Data type       | String         |
| Value format    | Allowed Values |

Allowed values:

| Service Category          | Service Subcategory               | Service Subcategory Description                                                                                                                                                                        |
| ------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AI and Machine Learning   | Bots                              | Automated performance of tasks such as customer service, data collection, and content moderation.                                                                                                      |
|                           | Generative AI                     | Creation of content like text, images, and music by learning patterns from existing data.                                                                                                              |
|                           | Machine Learning                  | Creation, training, and deployment of statistical algorithms that learn from and perform tasks based on data.                                                                                          |
|                           | Natural Language Processing       | Generation of human language, handling tasks like translation, sentiment analysis, and text summarization.                                                                                             |
|                           | Other (AI and Machine Learning)   | AI and Machine Learning services that do not fall into one of the defined subcategories.                                                                                                               |
| Analytics                 | Analytics Platform                | Unified solution that combines technologies to meet enterprise needs across the entire analytics lifecycle.                                                                                            |
|                           | Business Intelligence             | Semantic models, dashboards, reports, and data visualizations to track performance and identify trends.                                                                                                |
|                           | Data Processing                   | Integration and transformation tasks to prepare data for analysis.                                                                                                                                     |
|                           | Search                            | Discovery of information by indexing and retrieving data from various sources.                                                                                                                         |
|                           | Streaming Analytics               | Real-time data stream processes to detect patterns, trends, and anomalies as they occur.                                                                                                               |
|                           | Other (Analytics)                 | Analytics services that do not fall into one of the defined subcategories.                                                                                                                             |
| Business Applications     | Other (Business Applications)     | All Business Applications services.                                                                                                                                                                    |
| Compute                   | Containers                        | Management and orchestration of containerized compute platforms.                                                                                                                                       |
|                           | End User Computing                | Virtualized desktop infrastructure and device / endpoint management.                                                                                                                                   |
|                           | Quantum                           | Resources and simulators that leverage the principles of quantum mechanics.                                                                                                                            |
|                           | Serverless Compute                | Enablement of compute capabilities without provisioning or managing servers.                                                                                                                           |
|                           | Virtual Machines                  | Computing environments created by abstracting resources from physical hardware.                                                                                                                        |
|                           | Other (Compute)                   | Compute services that do not fall into one of the defined subcategories.                                                                                                                               |
| Databases                 | Caching                           | Low-latency and high-throughput access to frequently accessed data.                                                                                                                                    |
|                           | Data Warehouse                    | Big data storage and querying capabilities.                                                                                                                                                            |
|                           | Relational                        | Structured data storage and querying capabilities.                                                                                                                                                     |
|                           | NoSQL                             | Unstructured or semi-structured data storage and querying capabilities.                                                                                                                                |
|                           | Ledger                            | Immutable and transparent databases to record tamper-proof and cryptographically secure transactions.                                                                                                  |
|                           | Time Series                       | Time-stamped data storage and querying capabilities.                                                                                                                                                   |
|                           | Other (Databases)                 | Database services that do not fall into one of the defined subcategories.                                                                                                                              |
| Developer Tools           | Other (Developer Tools)           | All Developer Tools services.                                                                                                                                                                          |
| Identity                  | Other (Identity)                  | All Identity services.                                                                                                                                                                                 |
| Integration               | API Management                    | Creation, publishing, and management of application programming interfaces.                                                                                                                            |
|                           | Messaging                         | Asynchronous communication between distributed applications.                                                                                                                                           |
|                           | Workflow Automation               | Use of software to complete orchestration tasks and activities without the need for human input.                                                                                                       |
|                           | Other (Integration)               | Integration services that do not fall into one of the defined subcategories.                                                                                                                           |
| Internet of Things        | Other (Internet of Things)        | All Internet of Things (IoT) services.                                                                                                                                                                 |
| Management and Governance | Architecture                      | Planning, design, and construction of cloud systems.                                                                                                                                                   |
|                           | Compliance                        | Adherance to regulatory standards and industry best practices.                                                                                                                                         |
|                           | Cost Management                   | Monitoring and controlling expenses of cloud systems.                                                                                                                                                  |
|                           | Data Governance                   | Management of the availability, usability, integrity, and security of data.                                                                                                                            |
|                           | Disaster Recovery                 | Plans and procedures that ensure cloud systems can recover quickly from disruptions.                                                                                                                   |
|                           | Observability                     | Monitoring, logging, and tracing of data to track the performance and health of systems.                                                                                                               |
|                           | Support                           | Planning, advice, and expertise supplied by cloud providers.                                                                                                                                           |
|                           | Other (Management and Governance) | Management and governance services that do not fall into one of the defined subcategories.                                                                                                             |
| Media                     | Other (Media)                     | All Media services.                                                                                                                                                                                    |
| Migration                 | Other (Migration)                 | All Migration services.                                                                                                                                                                                |
| Mobile                    | Other (Mobile)                    | All Mobile services.                                                                                                                                                                                   |
| Multicloud                | Other (Multicloud)                | All Multicloud services.                                                                                                                                                                               |
| Networking                | Content Delivery                  | Distribution of digital content using a network of servers (CDNs).                                                                                                                                     |
|                           | Data Transfer                     | Movement of data between systems, locations, or formats via data migration, synchronization, and replication tasks.                                                                                    |
|                           | Load Balancing                    | Distribution of incoming network traffic across multiple servers to prevent server overload.                                                                                                           |
|                           | Network Management                | Configuration, monitoring, and troubleshooting of network devices.                                                                                                                                     |
|                           | Network Security                  | Protection from unauthorized network access and cyber threats using firewalls, VPNs, and anti-malware tools.                                                                                           |
|                           | Other (Networking)                | Networking services that do not fall into one of the defined subcategories.                                                                                                                            |
| Security                  | CSPM                              | Cloud Security Posture Management (CSPM) tools that help organizations configure, monitor, and improve their cloud security.                                                                           |
|                           | Credentials                       | Information used to authenticate users and systems, including secrets, certificates, tokens, and other keys.                                                                                           |
|                           | SIEM                              | Security Information and Event Management (SIEM) systems collect and analyze security data from various sources to automatically detect and respond to threats.                                        |
|                           | Threat Detection                  | Identification of potential security threats and vulnerabilities within a cloud environment using various techniques, including anomaly detection, signature-based detection, and behavioral analysis. |
|                           | Other (Security)                  | Security services that do not fall into one of the defined subcategories.                                                                                                                              |
| Storage                   | Backup                            | Secondary storage to protect against data loss.                                                                                                                                                        |
|                           | Block                             | High performance, low latency storage that provides random access.                                                                                                                                     |
|                           | File                              | Scalable, sharable storage for file-based data.                                                                                                                                                        |
|                           | Object                            | Highly available, durable storage for unstructured data.                                                                                                                                               |
|                           | Storage Transfer                  | Secure, high-speed, and offline transfer of stored data from one location to another.                                                                                                                  |
|                           | Other (Storage)                   | Storage services that do not fall into one of the defined subcategories.                                                                                                                               |
| Web                       | Other (Web)                       | All Web services.                                                                                                                                                                                      |
| Other                     | Other (Other)                     | All services that do not fall into one of the defined categories.                                                                                                                                      |

## Introduced (version)

1.1
