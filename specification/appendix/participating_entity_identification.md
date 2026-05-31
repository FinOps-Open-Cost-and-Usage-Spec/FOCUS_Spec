# Examples: Participating Entity Identification

Understanding billing data requires identifying the roles of several participating entities involved in resource or service provisioning, invoicing, and data generation. The FOCUS Specification includes multiple columns to identify key participating entities:

* [Service Provider Name](#datasets.costandusage.serviceprovidername)
* [Invoice Issuer Name](#datasets.costandusage.invoiceissuername)
* [Host Provider Name](#datasets.costandusage.hostprovidername)
* [Data Originator Name](#datasets.costandusage.dataoriginatorname)
* [Data Provider Name](#datasets.costandusage.dataprovidername)

The value for each of these may vary depending on how *resources* or *services* are obtained — whether directly from a Cloud Service Provider (CSP) or a SaaS provider, via a Managed Service Provider (MSP), through a cloud marketplace, or from internal service offerings. The table below provides examples that illustrate how the value for each dimension may shift depending on the method of acquisition and other contributing factors.

| # | Scenario | Service Provider | Invoice Issuer | Host Provider | Data Originator | Data Provider |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1.1 | Purchasing cloud resources or services directly from a CSP. | CSP | CSP | CSP | CSP | CSP |
| 1.2 | Purchasing cloud resources or services from a CSP, where the underlying resources are operated by a 3rd party. | CSP | CSP | Entity operating the region for the CSP | CSP | CSP |
| 2.1 | Purchasing cloud resources or services via an MSP, with visibility into the underlying hosting provider. | MSP | MSP | CSP | CSP | MSP |
| 2.2 | Purchasing cloud resources or services via an MSP, without visibility into the underlying hosting provider. | MSP | MSP | MSP | MSP | MSP |
| 2.3 | Purchasing cloud-agnostic resources or services from an MSP. | MSP | MSP | MSP | MSP | MSP |
| 2.4 | Purchasing labor services from an MSP. | MSP | MSP | \<null> | MSP | MSP |
| 3.1.1 | Purchase records for cloud marketplace offerings running on your CSP infrastructure and billed by the CSP. | Marketplace Seller | CSP | CSP | Marketplace Seller | CSP |
| 3.1.2 | CSP Infrastructure usage records for cloud marketplace offerings running on your CSP infrastructure. | CSP | CSP | CSP | CSP | CSP |
| 3.1.3 | Usage records for cloud marketplace offerings running on your CSP infrastructure and billed by the CSP. | Marketplace Seller | CSP | CSP | Marketplace Seller | Marketplace Seller |
| 3.2.1 | Purchase records for cloud marketplace offerings not running on your cloud infrastructure, with visibility into the underlying hosting provider. | Marketplace Seller | CSP | CSP | Marketplace Seller | CSP |
| 3.2.2 | Usage records for cloud marketplace offerings not running on your cloud infrastructure, with visibility into the underlying hosting provider. | Marketplace Seller | CSP | CSP | Marketplace Seller | Marketplace Seller |
| 3.3.1 | Purchase records for cloud marketplace offerings not running on your cloud infrastructure, without visibility into the underlying hosting provider. | Marketplace Seller | CSP | Marketplace Seller | Marketplace Seller | CSP |
| 3.3.2 | Usage records for cloud marketplace offerings not running on your cloud infrastructure, without visibility into the underlying hosting provider. | Marketplace Seller | CSP | Marketplace Seller | Marketplace Seller | Marketplace Seller |
| 3.4.1 | Purchase records for SaaS products not running on your cloud infrastructure, purchased via a reseller. Reseller is issuing payable invoices. | SaaS Provider | Reseller | SaaS Provider | SaaS Provider | Reseller |
| 3.4.2 | Usage records for SaaS products not running on your cloud infrastructure, purchased via a reseller. Reseller is issuing payable invoices. | SaaS Provider | Reseller | SaaS Provider | SaaS Provider | Reseller |
| 3.5.1 | Purchase records for SaaS products not running on your cloud infrastructure, purchased via a reseller. Reseller does not issue payable invoices. | SaaS Provider | SaaS Provider | SaaS Provider | SaaS Provider | SaaS Provider |
| 3.5.2 | Usage records for SaaS products not running on your cloud infrastructure, purchased via a reseller. Reseller does not issue payable invoices. | SaaS Provider | SaaS Provider | SaaS Provider | SaaS Provider | SaaS Provider |
| 3.6.1 | Purchase records for SaaS products that have been white-labeled and sold by a reseller, not running on your cloud infrastructure. Reseller issues payable invoices. | Reseller | Reseller | Reseller | Reseller | Reseller |
| 3.6.2 | Usage records for SaaS products that have been white-labeled and sold by a reseller, not running on your cloud infrastructure. Reseller issues payable invoices. | Reseller | Reseller | Reseller | Reseller | Reseller |
| 4.1 | Purchasing SaaS products directly from a SaaS provider, with visibility into the underlying hosting provider. | SaaS Provider | SaaS Provider | CSP | SaaS Provider | SaaS Provider |
| 4.2 | Purchasing SaaS products directly from a SaaS provider, without visibility into the underlying hosting provider. | SaaS Provider | SaaS Provider | SaaS Provider | SaaS Provider | SaaS Provider |
| 4.3.1 | Purchasing SaaS products running on your cloud infrastructure, purchased directly from a SaaS provider (see 4.3.2 for charges related to the underlying cloud infrastructure). | SaaS Provider | SaaS Provider | \<null> | SaaS Provider | SaaS Provider |
| 4.3.2 | Purchasing resources and services from a CSP used to host SaaS products separately acquired from a SaaS provider (see 4.3.1 for charges related to the SaaS products). | CSP | CSP | CSP | CSP | CSP |
| 5.1 | Purchasing internal resources or services hosted in Data Center. | Internal Name | Internal Name | Internal Name | Internal Name | Internal Name |
| 6.1 | Software license costs, reported separately from the costs of the resources or services they apply to. | Licensable Software Provider | License Seller | \<null> | Licensable Software Provider | License Seller |
| 7.1 | Usage records from a CSP, ingested, processed, and delivered by a 3rd-party FinOps platform or CMP. | CSP | CSP | CSP | CSP | FinOps Platform |
| 7.2 | Usage records from a CSP, retrieved and delivered by an internal centralized IT team without modifying the underlying financial records. | CSP | CSP | CSP | CSP | Internal Team Name |
| 7.3 | Net-new financial records (e.g., custom shared support fees or IT taxes) injected into a dataset by an internal centralized IT team. | Internal Team Name | Internal Team Name | \<null> | Internal Team Name | Internal Team Name |