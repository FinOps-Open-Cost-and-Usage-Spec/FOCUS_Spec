# FOCUS Compliance

The FOCUS specification is designed to assist FinOps practitioners in performing common FinOps capabilities by utilizing a standardized set of instructions, regardless of the billing data generator. It does so by establishing compliance criteria that account for provider-level variances in the cost and usage datasets providers produce. This section outlines the two primary types of cost datasets that FinOps practitioners currently work with and explains how FOCUS can enhance the interoperability between these different datasets.

## Differences in Cost and Usage Datasets

Cost and usage datasets can vary considerably depending on the provider, the method used to calculate costs (e.g. fixed vs consumption-based billing), and provider support for different concepts like usage and commitment-based discounts. The maturity level of the provider's billing system also plays a role in determining the depth of the cost and usage datasets.

Cloud Service Providers (CSPs) and some SaaS providers generate detailed cost and usage data in near real-time, which enables a wide range of FinOps capabilities. These capabilities help organizations make data-driven decisions to maximize the value they extract from the providers.

Most other providers typically offer billing datasets that lack the same level of detail. However, those less-detailed datasets meeting an essential set of requirements can enable some important FinOps capabilities like invoice reconciliation, data ingestion, and data normalization. Simplified versions of additional FinOps capabilities like cost reporting, chargeback, showback, and budgeting/forecasting can also be performed using less-detailed billing datasets when these essential requirements are met.

The essential set of data requirements needed to perform the most important FinOps capabilities is referred to as the 'FOCUS Essential' requirements.

## Meeting FOCUS Requirements

*This section is normative.*

All [columns](#columns) presented in a FOCUS-compliant dataset MUST meet the requirements specified in the normative prose of each column. These requirements may include nullability, value and format restrictions, and other scenario-specific requirements. Additionally, all FOCUS-compliant datasets MUST meet all [attributes](#attributes) defined in the FOCUS specification.

The set of columns defined as FOCUS Essential MUST be present in a FOCUS-compliant dataset. The non-FOCUS Essential columns MAY be omitted from the billing dataset based on the conditions defined in the normative prose of such columns.

For example, if a provider doesn't support commitment-based discounts, the columns related to commitment-based discounts can be omitted. Providers that support the commitment-based discount construct must provide the commitment-based discount columns and meet the requirements defined in the normative prose of those columns. If a provider doesn’t support commitment-based discounts and chooses to include commitment-based discount-related columns, the data presented in those columns must still meet all requirements specified in the normative prose of the commitment-based discount columns that were included.
