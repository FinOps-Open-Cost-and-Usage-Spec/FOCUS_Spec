SKU Price Details is intended to contain properties of the SKU / SKU Price ID (I'll refer to these two collectively as SKU for simplicity and will differentiate where necessary).

Considerations:
- Region can be both a property of a resource (where the resource is deployed) as well as the property of a SKU (which region or collection of regions the pricing is based off of)
  - Where the region chosen impacts pricing, it would constitute a separate SKU
  - E.g. GCP sku 3E94-1AB5-33F5 "N2 Custom Instance Core running in Americas" the SKU region (proposed key PricingRegion) would be "Americas" whereas the RegionId column would contain the region that the virtual machine is deployed in (e.g. us-east1)
- Time Normalization: The pricing unit for 1 SKU may be per month and another sku may be per hour, which would make it more difficult to use this field to calculated
- Unit Size: GB was used to mean either GB and GiB in differnt contexts, prior to ISO 80000-3; there may be some services truly measured in GB (or other Base10 units) which would be difficult to state in GiB (or other Base2 units)
  - Also one services make sense measured at different scales (e.g. L1 cache is measured in KiB versus disks that are measured in GiB or TiB).
- With regards to SKU sizing / naming, different CSPs think about the problem in different ways. E.g. in Azure, SizeName would be the property of the sku, but in GCP SizeName would be the property of the resource.
- For some SKUs, the Size & Shape property _feels_ duplicative with the unit of measure (pricing unit, consumed unit). 
  - It is often the case that the unit of measure will be time based, whereas these Size & Shape properties represent what you have for that period of time. E.g. 1 Hour (unit of measure) * 16 cores (SizeVcpu) = 16 core-hours
 
| Category | ProposedKey | Explanation | Concerns |
| ---- | ---- | ---- | ---- |
| Size & Shape | SizeVcpu | This is to capture the size in terms of cores / vCPUs per the Pricing Unit of the SKU | Time Normalization |
| Size & Shape | SizeGib | This is to capture the size in terms of GiB per Pricing Unit; this was intentionally kept generic to allow it to be used for multiple different types of SKUs | Time Normalization, Unit Size, a SKU may have 2 different things that could be measured in GiB (e.g. memory + ephemeral disk) |
| Size & Shape | SizeName | This is to capture the name of the size/shape so that it can be used for aggregation independent of other factors that make up the SKU (e.g. region) | 
| Size & Shape | SkuVersionName | This is to capture the name of the version or family to aggregate like SKUs | |
| Size & Shape | SkuXUnits | This is to capture units specific to a PaaS offering which often conatain a measure of processing power (RUs, PTUs, DBUs, etc.) | X is a placeholder for another word |


| ID | Type | CSP | Description | SizeVcpu | SizeGib | SizeName | SkuVersionName | SkuXUnits |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1e0af169-e265-53c0-832b-c5e6a58395d1 | IaaS | Azure | Virtual Machines Ddsv5 Series - D32ds v5 - US West 2 | 32 | 128 | D32ds v5 | Ddsv5 | |
| | IaaS | Azure | P50 LRS Disk | | 4096 | P50 | P-series disk | |
| A03E-E620-7389 | IaaS | GCP | N2D AMD Instance Core running in Americas | 1 | | | N2D | |
| 38529ded-5b8e-4b49-b078-ce81794a3543 | PaaS | Azure | Azure Cosmos DB - 100 RU/s - US West | | | | | 100 |

Use Cases:
- Capacity Planning
  - There are often times that you need to understand the total quantity of something you have in a common unit to be able to plan for migrations, growth, etc.
- Unit Economics
  - To understand your average price per unit, you need to be able to group like SKUs together and get the comparable units from each
 

Other ideas:
- Storage Redundancy (LRS, GRS)
- Storage Access Tier (Hot, Cold, Archive)
- More PaaS examples...
