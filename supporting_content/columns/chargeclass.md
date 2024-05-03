# Column: Charge Class

## References and Resources

### AWS

* [Pricing details - AWS Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/pricing-columns.html)

### GCP

* [Structure of Standard data export | Cloud Billing](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage)

### Microsoft

* [Understand usage details fields - Microsoft Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/automate/understand-usage-details-fields)

### OCI

* [Cost and Usage Reports Overview](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/usagereportsoverview.htm)

## Discussion / Scratch space

### Allowed Values

* Initially planned allowed values were Regular and Correction.
* Discussed alternative names for Regular charges: Regular/Standard/Original/Direct.
* Considered allowing null and Correction as the only allowed value, representing corrections to one or more charges that have been invoiced in a previous billing period.
* Since we plan to use this column as a reference when specifying the `Allow nulls` constraint for SkuId, SkuPriceId, and several other columns (refer to the table below),it was determined that the column should ideally enable identification of:
  * corrections to charges occurring in the same billing period (Current-cycle Correction)
  * as well as corrections to charges invoiced in previous billing periods (Past-cycle Correction).
* Notes:
  * Billing data received from providers who restate the billing period would still contain only "Original" and "Past-cycle Corrections" values.
  * However, billing data from providers that send delta updates would include charges with all three values.

### Impacts of 1.0 ChargeCategory and ChargeClass cleanup

The following table serves as the basis for reviewing the SkuPriceId spec, as well as price, cost, quantity metrics, etc., impacted by the ChargeCategory and ChargeClass columns cleanup

#### Latest version

| ChargeCategory | ChargeClass              | perSku/bulk                    | SkuId            | SkuPriceId       |
|----------------|--------------------------|--------------------------------|------------------|------------------|
| Usage          | Original                 | MUST be perSku and perSkuPrice | MUST not be null | MUST not be null |
| Usage          | Current-cycle Correction | MAY be bulk                    | MAY be null      | MAY be null      |
| Usage          | Past-cycle Correction    | MAY be bulk                    | MAY be null      | MAY be null      |
| Purchase       | Original                 | MUST be perSku and perSkuPrice | MUST not be null | MUST not be null |
| Purchase       | Current-cycle Correction | MAY be bulk                    | MAY be null      | MAY be null      |
| Purchase       | Past-cycle Correction    | MAY be bulk                    | MAY be null      | MAY be null      |
| Credit         | Original                 | MAY be bulk                    | MAY be null      | MAY be null      |
| Credit         | Current-cycle Correction | MAY be bulk                    | MAY be null      | MAY be null      |
| Credit         | Past-cycle Correction    | MAY be bulk                    | MAY be null      | MAY be null      |
| Adjustment     | Original                 | MAY be bulk                    | MAY be null      | MAY be null      |
| Adjustment     | Current-cycle Correction | MAY be bulk                    | MAY be null      | MAY be null      |
| Adjustment     | Past-cycle Correction    | MAY be bulk                    | MAY be null      | MAY be null      |
| Tax            | Original                 | MUST be bulk                   | MUST be null     | MUST be null     |
| Tax            | Current-cycle Correction | MUST be bulk                   | MUST be null     | MUST be null     |
| Tax            | Past-cycle Correction    | MUST be bulk                   | MUST be null     | MUST be null     |

#### Previous version

*Note: Applicable only if we decide to define "Correction" as a correction to previous charges regardless of the billing period.*

| ChargeCategory | ChargeClass                      | perSku/bulk                    | SkuId            | SkuPriceId       |
|----------------|----------------------------------|--------------------------------|------------------|------------------|
| Usage          | Regular/Standard/Original/Direct | MUST be perSku and perSkuPrice | MUST not be null | MUST not be null |
| Usage          | Correction                       | MAY be bulk                    | MAY be null      | MAY be null      |
| Purchase       | Regular/Standard/Original/Direct | MUST be perSku and perSkuPrice | MUST not be null | MUST not be null |
| Purchase       | Correction                       | MAY be bulk                    | MAY be null      | MAY be null      |
| Credit         | Regular/Standard/Original/Direct | MAY be bulk                    | MAY be null      | MAY be null      |
| Credit         | Correction                       | MAY be bulk                    | MAY be null      | MAY be null      |
| Adjustment     | Regular/Standard/Original/Direct | MAY be bulk                    | MAY be null      | MAY be null      |
| Adjustment     | Correction                       | MAY be bulk                    | MAY be null      | MAY be null      |
| Tax            | Regular/Standard/Original/Direct | MUST be bulk                   | MUST be null     | MUST be null     |
| Tax            | Correction                       | MUST be bulk                   | MUST be null     | MUST be null     |
