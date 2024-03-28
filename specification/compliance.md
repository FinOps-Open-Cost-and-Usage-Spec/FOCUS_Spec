# FOCUS Compliance

The FOCUS specification is designed to assist FinOps practitioners in performing common FinOps capabilities by utilizing a standardized set of instructions, regardless of the billing data generator. It does so by establishing compliance criteria that account for provider-level variances in the cost and usage datasets providers produce. This section outlines the multiple levels of compliance a FOCUS dataset can satisfy to support these variances.

## Differences in Cost and Usage Datasets

Cost and usage datasets can vary considerably depending on the provider, the method used to calculate costs (e.g. fixed vs consumption-based billing), and provider support for different concepts like usage and commitment-based discounts. The maturity level of the provider's billing system also plays a role in determining the depth of the cost and usage datasets.

Cloud Service Providers (CSPs) and some SaaS providers generate detailed cost and usage data in near real-time, which enables a wide range of FinOps capabilities. These capabilities help organizations make data-driven decisions to maximize the value they extract from the providers.

Most other providers typically offer billing datasets that lack the same level of detail. However, those less-detailed datasets meeting an essential set of requirements can enable some important FinOps capabilities like invoice reconciliation, data ingestion, and data normalization. Simplified versions of additional FinOps capabilities like cost reporting, chargeback, showback, and budgeting/forecasting can also be performed using less-detailed billing datasets when these essential requirements are met.

## Meeting FOCUS Requirements

*This section is normative.*

FOCUS defines four levels of compliance: Basic, Standard, Full, and Enhanced. All [columns](#columns) presented in a FOCUS-compliant dataset MUST meet the requirements specified in the normative prose of each column. Compliance (and compliance level) MUST be applied to the full dataset only and cannot be achieved if part of a dataset is excluded. These requirements may include nullability, value and format restrictions, and other scenario-specific requirements. Additionally, all FOCUS-compliant datasets MUST meet all [attributes](#attributes) defined in the FOCUS specification.

Each column defines the compliance level at which that column is required. These columns MUST be present in the dataset to conform to the specified compliance level of FOCUS. Additional columns MAY be omitted from the dataset based on the conditions defined in the normative prose of such columns.

For example, if a provider does not support commitment-based discounts, the columns related to commitment-based discounts can be omitted. Providers that support the commitment-based discount construct must provide the commitment-based discount columns and meet the requirements defined in the normative prose of those columns. If a provider does not support commitment-based discounts and chooses to include commitment-based discount-related columns, the data presented in those columns must still meet all requirements specified in the normative prose of the commitment-based discount columns that were included.

### Compliance Levels

**Basic** is the minimum compliance level. Datasets that do not meet the requirements of the Basic level do not conform to FOCUS. To reach the Basic level, the dataset MUST meet the requirements defined by all attributes and MUST include all Basic level columns. These columns are applicable to most types of data providers or are required for basic analysis by FinOps practitioners.

**Standard** extends the Basic level to include columns that describe features the provider supports, such as [_commitment-based discounts_](#glossary:commitment-based-discounts). The goal of Standard is to encourage providers to support more than the minimum to meet the level of analysis required by FinOps practitioners to understand and optimize all the provider's supported features. To reach the Standard level, the dataset MUST meet all Basic requirements and MUST include all Standard level columns that describe features the provider supports.

**Full** indicates that all columns are included in the dataset. Full is beneficial for FinOps practitioners because it reduces the work required to populate optional columns when merging datasets from providers with different levels of support and corresponding columns. Providers that support Full compliance stand out as exemplary. To reach the Full level, the dataset MUST meet all Standard requirements and MUST include every column defined by the FOCUS specification, including related requirements.

**Enhanced** extends the Full level and indicates that all "SHOULD" requirements defined in columns and attributes have also been met. Providers that support Enhanced compliance stand out as cutting edge and role models. To reach the Enhanced level, the dataset MUST meet all Full requirements and MUST meet all "SHOULD" requirements defined in every column and attribute.

While compliance can only be achieved at the stated levels, providers SHOULD document any progress toward meeting all requirements beyond the achieved level of compliance.
