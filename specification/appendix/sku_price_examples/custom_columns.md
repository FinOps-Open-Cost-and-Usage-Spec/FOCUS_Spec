# Custom Columns

Aura Web embeds structured detail in [SkuPriceDescription](#datamodel.skuprice.skupricedescription) that is not captured by any [*FOCUS column*](#glossary:FOCUS-column). A [*data generator*](#metadata.datagenerator) promotes two of those facts into [*custom columns*](#glossary:custom-column) so they can be filtered and grouped without parsing free text.

[**CSV Example**](/specification/data/sku_price_examples/sku_price_custom_columns.csv)

The extract carries the three virtual machine rates alongside one object storage rate, so the effect of a custom column that applies to some records and not others is visible in one place.

Note the following details in the example dataset:

* The virtual machine descriptions of "Standard VM 8 vCPU 32 GB, Linux, ..." carry a vCPU count and an operating system that no FOCUS column represents. The data generator adds `x_ComputeVcpuCount` and `x_ComputeOperatingSystem` to expose those two facts as columns rather than leaving them inside the description string.
* Both column IDs carry the `x_` prefix that identifies a custom column and distinguishes it from a FOCUS column. The portion following the prefix uses [*Pascal case*](#glossary:pascalcase) and only alphanumeric characters, and neither exceeds 50 characters. See the [Custom Column Handling](#attributes.customcolumnhandling) attribute for the naming, formatting, and value requirements a custom column conforms to.
* `x_ComputeVcpuCount` carries a single numeric value of 8 and `x_ComputeOperatingSystem` carries a string value of "Linux". A custom column containing numeric values holds one number, and a custom column containing string values conforms to the same string handling requirements as a FOCUS column.
* The three virtual machine records repeat the same custom column values because the vCPU count and operating system are properties of the SKU, not of the price. They stay constant across the on-demand rate, the euro rate, and the negotiated rate, none of which change what the machine is.
* The object storage record carries a null value in both custom columns, because a vCPU count and an operating system do not describe object storage. A custom column that applies to some records and not others is null on the records it does not describe, in the same way a FOCUS column is.
* Neither custom column is a member of the composite key. Adding a custom column exposes existing detail as a column and does not change which records are distinct, so the virtual machine records remain separated by [PricingCurrency](#datamodel.skuprice.pricingcurrency) and [ContractId](#datamodel.skuprice.contractid) exactly as they were before the columns were added.
