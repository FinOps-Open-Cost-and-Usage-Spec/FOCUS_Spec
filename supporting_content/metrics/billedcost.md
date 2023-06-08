## Supporting content

### Column: Billed Cost

#### Example provider mappings 

Current column mappings found in available data sets:

  -----------------------------------------------------------------------
  **Provider**    **Data set**           **Column**
  --------------- ---------------------- --------------------------------
  AWS             CUR                    lineItem/NetUnblendedCost (If
                                         you have an EDP, otherwise
                                         ​​line_item_unblended_cost)

  GCP             Big Query Billing      Cost (The cost of the usage
                  Export                 before any credits, to a
                                         precision of up to six decimal
                                         places)

  Microsoft       Cost details           Cost, CostInBillingCurrency\
                                         \
                                         CostInBillingCurrency: Cost of
                                         the charge in the billing
                                         currency before credits or
                                         taxes.\
                                         \
                                         CostInPricingCurrency: Cost of
                                         the charge in the pricing
                                         currency before credits or
                                         taxes.\
                                         \
                                         EffectivePrice: Blended unit
                                         price for the period. Blended
                                         prices average out any
                                         fluctuations in the unit price,
                                         like graduated tiering, which
                                         lowers the price as quantity
                                         increases over time.
  -----------------------------------------------------------------------

#### Example usage scenarios

See [Supporting_Content: Cost Metrics Examples Spreadsheet](#costmetricsexamples) for examples of billing data for various scenarios.

Current values observed in billing data for various scenarios:

  -----------------------------------------------------------------------------
  **Provider**   **Scenario**        **Pattern**
  -------------- ------------------- ------------------------------------------
  AWS                                

  AWS            No up-front RI      BilledCost will represent the RI Fee
                                     charged per day for the RI (for usage).
                                     Instance that had its usage cost
                                     discounted will show up as \$0 for
                                     BilledCost.

  AWS            Savings Plan        

  GCP                                

  GCP                                

  Microsoft                          

  Microsoft                          

  Microsoft                          

  Microsoft                          

  Microsoft                          

  Microsoft                          
  -----------------------------------------------------------------------------

#### Documentation

AWS:

\>

Microsoft:

\>

GCP:

\>

### Discussion / Scratch space

-   Aggregations can capture billed cost across different charge types.

    -   The cost shown in a single line item may not be the final billed
        > cost of a given resource for a billing period as taxes,
        > discounts and other adjustments for the same resource will be
        > in other rows.

    -   It's important to understand that providers may not spread some
        > charges (like Tax, Credits) to a line-item level. Those rows
        > may be available at a higher granularity which means they
        > can't easily be spread accurately to each usage row. Example,
        > Tax may not come at a resource level. This means you will need
        > to spread tax cost down to individual teams/resources but that
        > assumes all usage would have gotten taxed at the same rate
        > (which is not the case). However, this is likely the best most
        > practitioners will be able to do to spread taxes, fees etc.

-   Variable cost discounts are applied in Billed Cost.

    -   Examples are GCP SUD or equivalent. Ultimately, the spec can't
        > define if these discounts show up as a single line or as
        > multiple as long as negotiated discounts are applied AND the
        > aggregation of rows at charge type (e.g. Usage) provides the
        > correct sum.

-   Accuracy / format of values:

    -   What's the precision for the decimal values? This will be
        > defined as a new attribute

    -   Tim will take a look at open standards to define a valid decimal
        > / precision

-   Must have a currency always with cost data (similar to time needs a
    > timezone)

-   Do we use the billed currency or the pricing currency or both?

    -   Should the following 4 columns be provided: billed cost, billing
        > currency, pricing currency cost?, pricing currency

    -   Pricing cost/currency naming also needs to be 0.5 \@udam

    -   What about conversion rates? As columns? as Metadata? Skip for
        > now

    -   Clear downside here is that a unified data set across providers
        > OR even a dataset for a single multi-currency provider will
        > have cost data in a billed or pricing currency cost that
        > cannot be aggregated (sum, average etc.)

    -   Should there be a column that allows normalization to a single
        > currency across providers

        -   USD would be the logical choice but this would impose USD on
            > non-USD consumers

-   Should a minimum precision be defined in the spec?

    -   They should be consistent within provider

    -   Focus on the outcome not necessarily the specifics on precision.

  ---------------------------------------------------------------------------------------------------
                          **BilledCost**   **BilledCurrency**   **PricedCost**   **PricedCurrency**
  ----------------------- ---------------- -------------------- ---------------- --------------------
  Priced and billed in    123.45           USD                  123.45           USD
  USD, Invoiced in USD                                                           

  Priced and billed in    246.80           USD                  246.80           USD
  USD, Invoice converted                                                         
  to a different currency                                                        
  by provider (current                                                           
  approach by AWS)                                                               

  Priced in USD, billed   1234567890       JPY                  89.08            USD
  in JPY                                                                         

  Priced and billed in    369.15           CNY                  369.15           CNY
  Chinese Yuan                                                                   
  ---------------------------------------------------------------------------------------------------

*Do we just need a THIRD option - CostInBase, BaseCurrency - which is
like UTC - it could be USD? OR are we assuming that PricedCurrency is
always USD?*


-   List price is 5\$ comes in hourly. Providers may decide to modify
    > that cost for various reasons (negotiated discounts, commitment
    > discounts etc.).

  -----------------------------------------------------------------------
                    List Cost         Invoice Cost      Amortized Cost
  ----------------- ----------------- ----------------- -----------------
  One-time /                                            
  recurring                                             
  purchases                                             

  Usage line items                                      

  Fees                                                  

                                                        
  -----------------------------------------------------------------------

Here is an example for purchasing Azure "Compute Savings Plan" for 3
years, no upfront cost at \$1.905 /hour commitment. The purchase of a
savings plan is reported as the "Purchase" charge type. The monthly
recurring amount is \$1,390.65

+-------------+---------------+-----------+-------------+-------------+
| Type        | Charge type   | Pricing   | Cost        | Publisher   |
|             |               | Model     |             | type        |
| (request    |               |           |             |             |
| payload)    |               |           |             |             |
+=============+===============+===========+=============+=============+
| Amortized   | Usage         | OnDemand  | \$7,654.99  | Microsoft   |
| Cost        |               |           |             |             |
+-------------+---------------+-----------+-------------+-------------+
| Amortized   | Usage         | Sa        | \$1,371.60  | Microsoft   |
| Cost        |               | vingsPlan |             |             |
+-------------+---------------+-----------+-------------+-------------+
| Amortized   | Unus          | Sa        | \$0.00      | No          |
| Cost        | edSavingsPlan | vingsPlan |             | publisher   |
+-------------+---------------+-----------+-------------+-------------+
| Amortized   | Round         | OnDemand  | \$-1.36     | No          |
| Cost        | ingAdjustment |           |             | publisher   |
+-------------+---------------+-----------+-------------+-------------+
| Amortized   | Usage         | OnDemand  | \$58.98     | Marketplace |
| Cost        |               |           |             |             |
+-------------+---------------+-----------+-------------+-------------+
| Actual Cost | Usage         | OnDemand  | \$7,597.37  | Microsoft   |
+-------------+---------------+-----------+-------------+-------------+
| Actual Cost | Usage         | OnDemand  | \$58.98     | Marketplace |
+-------------+---------------+-----------+-------------+-------------+
| Actual Cost | Purchase      | Sa        | \$1,390.65  | Microsoft   |
|             |               | vingsPlan |             |             |
+-------------+---------------+-----------+-------------+-------------+

AWS Savings Plan handling

  ----------------------------------------------------------------------------------------------------
  **ChargeType**   **lineItem/LineItemType**   **lineItem/UsageAmount**   **lineItem/UnblendedCost**
  ---------------- --------------------------- -------------------------- ----------------------------
  Purchase         SavingsPlanUpfrontFee       1                          1200

  Purchase         SavingsPlanRecurringFee     1                          100

  Usage            SavingsPlanCoveredUsage     744                        0

  Usage            SavingsPlanNegation         744                        -100

  Usage            Usage                                                  
  ----------------------------------------------------------------------------------------------------

1.  SavingsPlanUpfrontFee - you made an upfront payment of \$1200 for an
    > EC2 Savings Plan

2.  SavingsPlanRecurringFee - monthly recurring cost for your Savings
    > Plan is \$100

3.  SavingsPlanCoveredUsage - you\'ve used 744 hours of EC2 instance
    > time (which is roughly equivalent to a month\'s worth of usage).
    > This usage is covered by your SP. So, the unblended cost is \$0

4.  SavingsPlanNegation is used to negate the on-demand cost covered by
    > SP. In this case, the 744 hours of EC2 usage would have cost \$100
    > at on-demand rates, but this cost is negated by your Savings Plan.
    > This is reflected in the CUR by a SavingsPlanNegation line item
    > with an unblended cost of -\$100
