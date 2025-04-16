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

We've identified the following scenarios for double-counting:

1. Amortization
2. Burndown of a previous purchase with no charge for underutilized purchases (aka credit burndown).
3. Burndown of a promise where no money is charged with a potential "unused" charge at the end of the period (aka commit to consume).
4. Rows in a provider's dataset that can also be provided separately in a more detailed format. Examples:
   * SaaS providers have detailed data while cloud providers only have summarized usage/purchases.
   * Cloud providers may have services which include detailed usage breakdowns used for allocation that are outside the main usage data (e.g., container usage).
5. Non-Marketplace rows in a cloud provider's dataset and separately in a SaaS provider's dataset being combined by the practitioner

Evaluating how to cover all scenarios:

* Looking at all known double-counting scnearios, we discover that they are sometimes overlapping and cannot be accurately represented within a single-purpose column. The following table indicates when each scenario overlaps with another:

  |                          | Amortization target | Credit target | Commit target | Marketplace target | Provider target | Examples |
  | ------------------------ | :-----------------: | :-----------: | :-----------: | :----------------: | :-------------: | -------- |
  | Amortization source      | ???  | Yes  | Yes  | Possible | ??? | CD purchases, prepurchase plans<br>Hypothetical: Marketplace purchases, aggregated usage charges |
  | Purchased credit source  | ???  | ???  | Yes  | Yes      | No  | Microsoft monetary commitment |
  | Purchased credit target  | No?  | ---  | ---  | ---      | --- | Provider usage, CD purchases, marketplace? |
  | Commit to consume source | No   | No   | No   | No       | No  | Microsoft MACC |
  | Commit to consume target | No?  | Yes? | ---  | ---      | --- | Provider usage, CD purchases, marketplace? |
  | Marketplace source       | ???  | ???  | ???  | No       | No  | Available via publisher |
  | Marketplace target       | Yes  | Yes  | Yes  | ---      | --- | Marketplace charges |
  | Provider source          | Yes? | Yes? | Yes? | ---      | --- | Internal service usage (e.g., users, traffic) |
  | Provider target          | Yes  | Yes  | Yes  | ---      | --- | Public service usage |

* Based on the table:
  * Credit burndown cannot be combined with amortization because commitment discounts (or other amortizable charges) can be purchased with credit.
  * Burndown of a promise (commit to consume) cannot be combined with amortization for the same reason. Also note that this scenario does not have an original "charge" so it may not even apply.
  * Provider and marketplace/SaaS cannot be combined with amortization since they may be related to amortization. Also note that this scenario presents a different challenge altogether that we don't know how we can address since it is only conditionally an issue. This was scoped out after several discussions.
The most prominent example might be a credit target being used to purchase a commitment discount (or other amortized charge).
* Based on the above table, we cannot cover all scenarios in a single column.
* We decided to focus exclusively on amortization scenarios.

Amortization requirements:

* Must be able to identify (and filter out) the original/source charge.
  * This charge has a BilledCost of some positive value and an EffectiveCost of 0.
  * This charge is the one that will get filtered out when calculating savings.
  * This is typically a purchase but may not always be (e.g., monthly aggregated usage row could be broken down into daily/hourly usage rows).
  * In finance, the original charge is generally referred to as the "principal".
* Must be able to identify (and filter down to) the target or "effective" charges where the principal was amortized out over time.
* All amortized charges should include rows for both the source and target charges to ensure the filtering works as intended.

For amortization specifically:

* We cannot filter out "Purchase" ChargeCategory because not all purchases are amortizable.
* We cannot filter out "Purchase" ChargeCategory when CommitmentDiscountId is specified because that wouldn't cover other purchases (or even usage) that could be amortized.
* We cannot filter down to ChargeCategory == "Usage" because this would leave out any savings from purchases that are not amportized.
* The current behavior for rows that are impacted by amortization includes:
  * All original/source charges that get amortized have a BilledCost != 0 and an EffectiveCost == 0.
  * All effective/target charges that are after amortization is applied have BilledCost == 0 and EffectiveCost != 0.
  * The above 2 facts assume we would not amortize a charge that has no cost.
* Based on these facts, it is possible to filter out the original charges by evaluating BilledCost and EffectiveCost:
  ```sql
  SELECT TotalSavings = SUM(ListCost - EffectiveCost)
  WHERE BilledCost == EffectiveCost OR EffectiveCost != 0
  ```
* While this is nice because it doesn't add a new column, this approach has the following downsides:
  * The logic is not straightforward.
    * Why compare the equality of BilledCost and EffectiveCost? Because those are the rows where amortization is not in play.
    * Why filter out when EffectiveCost is 0? Because those are the original charges that get amortized. 
    * Why are we OR-ing these conditions? Because we want to keep rows where BilledCost == 0 and EffectiveCost == 0 but remove anything where BilledCost != 0 and EffectiveCost == 0. In other words, we don't want 0 EffectiveCost unless BilledCost is also 0. This is important to cover something that was negotiated to be free, which may have a ListCost.
  * It's not clear that practitioners would need to apply this logic.
  * It would be hard to remember the exact filter and will most likely lead to bugs as people misremember and misapply the filter.
* The same query with AmortizationClass would be:
  ```sql
  SELECT TotalSavings = SUM(ListCost - EffectiveCost)
  WHERE AmortizationClass <> "Principal"
  ```

Column name and values:

* We ran a poll for naming in Task Force 1: https://docs.google.com/spreadsheets/d/1iRHiLCMBH9RPWU4s1GGFr0TiEYUP4SCpkxiHsO4kWHw/edit?usp=sharing
* Column name poll:
  * Amortization Class = 6 votes
  * Amortization Category = 2 votes
  * Amortization Effect = 1 vote
  * No votes: Amortization Allocation, Amortization Classification, Charge Method, Charge Subcategory, Transaction Category
* Original/source charge value poll:
  * Principal = 5 votes
  * Source = 4 votes
  * Original = 1 vote
  * No votes: Base, Before Amortization, Charge to Amortize, Initial Expense, Pre Amortization
* Target/effective charge value poll:
  * Amortized Charge = 5 votes
  * Target = 3 votes
  * Effective Charge = 1 vote
  * No votes: After Amortization, Amortization Effect, Amortization Finalized, Amortization Result, Amortized Impact, Outcome, Post Amortization, Result

