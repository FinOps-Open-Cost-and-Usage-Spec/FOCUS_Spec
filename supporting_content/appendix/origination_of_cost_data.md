# Origination of cost data

## Example usage scenarios

Current values observed in billing data or potential values that should be supplied for various scenarios:

| Scenario                                                                                                                                                                           | Provider                 | Publisher         | Invoicing Entity         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|-------------------|--------------------------|
| Direct cloud usage: You use an instance of CosmosDB (Scenario #1.1)                                                                                                                | Microsoft                | Microsoft         | Microsoft                |
| MSP cloud usage: You purchase GCP through SADA (Scenario #2.1)                                                                                                                     | Google                   | Google            | SADA                     |
| Professional services: IT infrastructure outsourcing (Scenario #2.2)                                                                                                               | Accenture                | Accenture         | Accenture                |
| Professional services: IT labor outsourcing (Scenario #2.3)                                                                                                                        | Accenture                | Accenture         | Accenture                |
| License for cloud usage: You use a Microsoft SQL Server license purchased on AWS Marketplace on EC2 (Scenario #3.1)                                                                | Amazon Web Services, Inc | Microsoft         | Amazon Web Services, Inc |
| Infrastructure via marketplace: You purchase PaloAlto Networks Firewall (charged based on type of VM instance you run on) through AWS Marketplace (Scenario #3.1)                  | Amazon Web Services, Inc | PaloAlto Networks | Amazon Web Services, Inc |
| Purchase business solution via marketplace: You purchase Udemy Business Licenses through AWS Marketplace (Scenario #3.2)                                                           | Amazon Web Services, Inc | Udemy             | Amazon Web Services, Inc |
| SaaS purchase via cloud marketplace: You purchase DataDog through AWS Marketplace (Scenario #3.2)                                                                                  | Amazon Web Services, Inc | DataDog           | Amazon Web Services, Inc |
| Professional services: You purchased Accenture consulting services via GCP Marketplace (Scenario #3.2)                                                                             | Google                   | Accenture         | Google                   |
| Reseller scenario - Purchase DataDog via Azure marketplace through SADA as reseller (Scenario #3.3)                                                                                | Microsoft                | DataDog           | SADA                     |
| Direct SaaS purchase: You purchase DataDog directly from DataDog (Scenario #4.1)                                                                                                   | DataDog                  | DataDog           | DataDog                  |
| Direct SaaS purchase: You purchased and used Databricks Classic  (Scenario #4.1)                                                                                                   | Databricks               | Databricks        | Databricks               |
| Direct SaaS purchase (where a portion runs on your cloud environment): Compute / storage / network cost associated with running Databricks in your AWS environment (Scenario #4.2) | AWS                      | AWS               | AWS                      |
| On premises: You use Kubernetes via an internal PaaS service built in your organization called Kube4U which runs on-prem (Scenario #5.1)                                           | Kube4U                   | Kube4U            | Kube4U                   |
| Internal cloud platform: You use Kubernetes via an internal PaaS service built in your organization called Kube4U which runs in hybrid mode or in AWS (Scenario #5.2)              | Kube4U                   | Kube4U            | Kube4U                   |
| Software Licenses: You purchased SQLServer licenses from Microsoft that are used in an internal DBaaS platform service (Scenario #5.3)                                             | Internal platform name   | Microsoft         | Internal platform name   |

## Discussion / Scratch space

- Provider is the entity through which you're purchasing the products regardless of the purchasing mechanism
- Publisher value matches who developed or produced the customer-facing infrastructure, software or professional service regardless of the purchasing mechanism. Where the infrastructure and services are provided as a 'managed' offering, the branded name of the managed offering may be used as the publisher. E.g. If managed Kubernetes was provided via EKS / AKS / GKE / Internal cloud, the publisher would be the cloud providers, not the Kubernetes project or the CNCF.
- Invoicing Entity always matches who did the billing for the transaction regardless of the purchasing mechanism.
- Invoicing Entity oddities:
  - There would be differentiation between (e.g.) Google France SarL and Google, Inc. USA even though it's really "one Google"
  - Azure in China is operated by SomeCompany, so this will be the invoicing entity, even if it looks like you are buying it from Microsoft. ("franchise model")
