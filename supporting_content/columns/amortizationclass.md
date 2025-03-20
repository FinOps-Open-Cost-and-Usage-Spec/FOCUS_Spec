# Column: Amortization Class

Objective: We need a method to calculate savings that accurately accounts for commitment discount purchase costs without creating duplication in the usage rows.

## Example provider mappings

Current column mappings found in available data sets:

| Provider     | Data set                | Column                                                                                                                                                |
| ------------ | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS          | CUR                     | lineItem/lineItemType                                                                                                                                 |
| Google Cloud | BigQuery Billing Export | ??N/A because no upfront payments??                                                                                                                   |
| Microsoft    | Cost details            | ChargeType indicates purchases and PricingModel indicates commitment discounts. There is no column that identifies when and how amortization applies. |
| OCI          | Cost reports            | ???                                                                                                                                                   |

## Example usage scenarios

This example demonstrates a commitment discount that gets 50% off list price when the organization has an 20% discount on all usage.

| ChargeDescription | AmortizationClass | ChargePeriodStart |  ListCost | ContractedCost | BilledCost | EffectiveCost |
| ----------------- | ---------------- | ----------------- | --------: | -------------: | ---------: | ------------: |
| Reservation       | Principal        | Jan 1             |   $365.00 |        $365.00 |    $365.00 |         $0.00 |
| VM usage          | Amortized Charge | Jan 1             |     $2.00 |          $1.80 |      $0.00 |         $1.00 |
| VM usage          | Amortized Charge | Jan 2             |     $2.00 |          $1.80 |      $0.00 |         $1.00 |
| VM usage          | Amortized Charge | ...               |       ... |            ... |        ... |           ... |
| VM usage          | Amortized Charge | Dec 31            |     $2.00 |          $1.80 |      $0.00 |         $1.00 |
| Sum of 365 days   | (sum)            | Jan 1-Dec 31      | $1,095.00 |      $1,022.00 |       $365 |          $365 |

If you SUM the ListCost or ContractedCost columns as is, you'll be double counting the original "Reservation" charge and over-counting the savings present in the e.g. EffectiveCost column. We need an attribute that allows us to selectively exclude upfront payments from such calculations, so that we are only SUMming the usage charges that benefit from the original upfront payment (or "unused commitment" line items).

`SUMIF(ListCost, AmortizationClass != "Principal")` would give you the correct total of $730.00, which is the sum of the usage charges that benefit from the original upfront payment.

## Discussion / Scratch space

We discussed the idea of using AmortizationClass to identify commitment discount eligibility, but determined this should be in a separate column (possibly multiple columns for usage and spend commitment discounts).

* For calculating something like "commitment coverage", you can use the "Eligible - Covered" and "Eligible - Not Covered" values. For example, if you want to know the balance of covered to "not covered, but potentially coverable" you could use:

  ```sql
  SELECT
      SUM(ListCost) as TotalCost,
      AmortizationClass
  ...
  GROUP BY AmortizationClass
  ```

There are 4 known scenarios for double-counting:

1. Amortization
2. Burndown of a previous purchase with no charge for underutilized purchases
3. Burndown of a promise where no money is charged with a potential "unused" charge at the end of the period
4. Rows in a provider's dataset that can also be provided separately in a more detailed format. Examples:
   * SaaS providers have detailed data while cloud providers only have summarized usage/purchases.
   * Cloud providers may have services which include detailed usage breakdowns used for allocation that are outside the main usage data (e.g., container usage).
5. Non-Marketplace rows in a cloud provider's dataset and separately in a SaaS provider's dataset being combined by the practitioner

Amortization requirements:

* Must be able to identify (and filter out) the original/source charge.
  * This charge has a BilledCost of some positive value and an EffectiveCost of 0.
  * This charge is the one that will get filtered out when calculating savings.
  * This is typically a purchase but may not always be (e.g., monthly aggregated usage row could be broken down into daily/hourly usage rows).
  * In finance, the original charge is generally referred to as the "principal".
* Must be able to identify (and filter down to) the target or "effective" charges where the principal was amortized out over time.
* All amortized charges should include rows for both the source and target charges to ensure the filtering works as intended.
