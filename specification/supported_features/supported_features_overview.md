# Supported Features

The FOCUS specification is designed to meet the needs of FinOps practitioners in numerous scenarios. The following section contains features supported by the FOCUS specification. This list does not represent all possible combinations or use of FOCUS data but does represent core capabilities that the FOCUS specification supports.  

## Supported Feature List<!--SkipTOC-->

| Feature | Description |
| :--- | :--- |
| [Account Structures](#supportedfeatures.accountstructures) | Supports breaking costs down by billing and sub-accounts to facilitate chargeback and budgeting scenarios. |
| [Billed Cost and Invoice Alignment](#supportedfeatures.billedcostandinvoicealignment) | Ensures data is consistent with payable invoices regarding total cost and the period of time covered. |
| [Charge Categorization](#supportedfeatures.chargecategorization) | Supports classification of charges including purchases, usage, tax, credits, and adjustments. |
| [Commit Usage and Under Usage](#supportedfeatures.commitusageandunderusage) | Tracks the usage and under-usage of commitment discounts and capacity reservations. |
| [Contract Commitments](#supportedfeatures.contractcommitments) | Tracks commitments made via contractual agreements using identifiers joined between Cost and Usage and Contract Commitment datasets. |
| [Cost and Usage Attribution](#supportedfeatures.costandusageattribution) | Facilitates the inclusion of provider-defined or user-defined metadata (tags) at a row level for organizational analysis. |
| [Cost Comparison](#supportedfeatures.costcomparison) | Supports comparing Billed, Contracted, Effective, and List cost columns to identify savings or amortization. |
| [Custom Columns](#supportedfeatures.customcolumns) | Allows the inclusion of additional columns to facilitate reporting capabilities not covered by the standard specification. |
| [Data Generator-Calculated Split Cost Allocation](#supportedfeatures.datagenerator-calculatedsplitcostallocation) | Enables tracking resources split by internal consumption metrics, common for shared clusters like Kubernetes. |
| [Data Granularity](#supportedfeatures.datagranularity) | Supports multiple levels of granularity, from high-level account charges down to individual resource-level data. |
| [Dataset Instance Metadata](#supportedfeatures.datasetinstancemetadata) | Provides metadata describing dataset artifacts, unique identifiers, and alignment with specific FOCUS datasets. |
| [Effective Cost Analysis](#supportedfeatures.effectivecostanalysis) | Enables analysis of costs after discounts and the amortization of upfront fees to track spending trends. |
| [Location](#supportedfeatures.location) | Provides structured data for regions and availability zones to analyze costs based on deployment geography. |
| [Marketplace Purchases](#supportedfeatures.marketplacepurchases) | Supports analysis of marketplace purchase data and reporting Effective Cost for service provider usage. |
| [Participating Entity Identification](#supportedfeatures.participatingentityidentification) | Allows identification of entities involved in hosting, invoicing, and data generation (e.g., Service Provider vs. Host Provider). |
| [Recency Metadata](#supportedfeatures.recencymetadata) | Indicates what portion of a dataset is complete and how recently it was updated to inform FinOps functions like chargeback. |
| [Resource Usage](#supportedfeatures.resourceusage) | Enables tracking consumption by providing information on which resources were used, in what quantities, and with what units. |
| [Schema Metadata](#supportedfeatures.schemametadata) | Communicates important attributes about data structure, types, and versions to facilitate structure changes. |
| [Service Categorization](#supportedfeatures.servicecategorization) | Standardizes the classification of services into high-level functional categories and granular subcategories. |
| [Service Provider Services](#supportedfeatures.serviceproviderservices) | Aligns costs with familiar service and product offering names for easier reporting and verification. |
| [Verification, Comparison, and Fluctuation Tracking of Unit Prices](#supportedfeatures.verificationcomparisonandfluctuationtrackingofunitprices) | Facilitates verification of List and Contracted unit prices and tracks fluctuations over time. |
