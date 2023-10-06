# Product Class

Product Class is an optional, fourth-level of classification of a product just below Product Family. Each product MAY have one and only one class that categorizes products into a subset with specific attributes and characteristics. As an example, the Product Class "On-demand" may be used to identify products in the "Compute" category, "Linux VM" group, and "Memory Optimized" family as being virtual machine products running the Linux operating system that have specifications optimized for high-memory workloads that are being used on-demand as opposed to VMs that are reserved or purchased as an interruptible or spot instance.

Product Class is commonly used to track usage patterns for specific subset of products within a family or to analyze costs in similar classes across multiple families and groups.

The ProductClass column MAY be present and when present SHOULD NOT be null or empty. ProductClass may contain provider-specific values and is not restricted to a set of allowed values.

## Column ID

ProductClass

## Display Name

Product Class

## Description

Product Class is the fourth level of classification of a product just below Product Family.

## Content Constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column required | False            |
| Data type       | String           |
| Allows nulls    | False            |
| Value format    | \<not specified> |

## Introduced (version)

1.0
