# SKU Categorization

## Example provider mappings

Current column mappings for each level of the hierarchy found in available data sets:

| Level    | AWS                                                        | GCP                     | Microsoft                     | Oracle                      |
| -------- | ---------------------------------------------------------- | ----------------------- | ----------------------------- | --------------------------- |
| Data set | CUR                                                        | BigQuery                | Cost details                  | Cost report                 |
| Category | None                                                       | None                    | ServiceFamily                 | None                        |
| Brand    | Part of servicename                                        | None                    | Provider (MCA only)           | None                        |
| Group    | product_group<br>product_servicename                       | SKU Group (not in data) | MeterCategory                 | product/service             |
| Family   | product_product_family                                     | service.description     | None                          | Part of product/Description |
| Class    | product_instance_family<br>product_abd_instance_class?     | None                    | ProductCategory (not in data) | Part of product/Description |
| Line     | product_instance_type_family                               | None                    | MeterSubcategory              | None                        |
| Type     | product_instance_type<br>product_transfer_type<br>instance | Part of sku.description | Part of ProductName           | Part of product/Description |

## Example values

Current values observed in billing data for various scenarios:

| Provider  | Category      | Brand                       | Group                       | Family                                  | Class                         | Line              | Type              |
| --------- | ------------- | --------------------------- | --------------------------- | --------------------------------------- | ----------------------------- | ----------------- | ----------------- |
| AWS       | None          | Amazon Web Services         | Relational Database Service | Database Instance                       | R5b                           | None              | db.r5b.16xlarge   |
| AWS       | None          | Amazon Web Services         | Elastic Compute Cloud       | Compute Instance                        | General Purpose               | m3                | m3.medium         |
| AWS       | None          | Amazon Web Services         | AWS Data Transfer           | None                                    | None                          | None              | AWS Outbound      |
| GCP       | None          | Google Cloud                | Google Kubernetes Engine    | Anthos Service Mesh<br>(3DAD-B96D-BE09) | Anthos Service Mesh Endpoints | None              |                   |
| Microsoft | Compute       | Azure                       | Virtual Machines            | Spot VMs                                | General Purpose               | DS Flex Series VM | D16s_Flex         |
| Microsoft | Business Apps | Microsoft 365               | Office 365 Global           | None                                    | None                          | Enterprise        | E3                |
| Oracle    | None          | Oracle Cloud Infrastructure | Compute                     | None                                    | Memory Optimized              | Standard          | E3                |
| Oracle    | None          | Oracle Cloud Infrastructure | Block Storage               | None                                    | None                          | Block Volume      | Performance Units |

## Discussion / Scratch space

"Product" vs. "service":

- A product is a tangible item that is sold to a customer.
- A service is an intangible offering that involves a deed, performance, or effort that cannot be physically possessed.
- In cloud computing:
  - A product is a tangible item (e.g., a specific VM size/shape) within an overarching service (e.g., the core virtual server offering).
  - Every resource or service uses multiple products behind the scenes.
  - Not all resources or services charge for the different products that are being used. Some group the usage of those products into a custom "unit" (e.g., "throughput units" or "tokens").
- FOCUS decided to use the term "service" to refer to the overarching offering and "SKU" to refer to the specific product being used or purchased.

General product categorization hierarchies used outside of cloud computing:

1. **Need** – Primary purpose of or reason for the existence of the product.
2. **Family** – Grouping of products that address the same core need.
3. **Class** – Group of similar products which can somewhat substitute each other. Products within a class often have similar features and functions.
4. **Line** – Group of products that perform a comparable function, are purchased by the same group of customers, or fall within a certain price range. A company may have multiple product lines with a certain number of products per line.
5. **Type** – Various products within a product line or series, there are multiple types of customizations.
6. **Unit** – A specific variation of a product. This is also referred to as the stock keeping unit (SKU) and is a discrete item within a product type that can distinguish itself by size, price, availability, or any other feature or capability. A product becomes an individual product unit if it is independent and no other product types is dependent on it.

Additional attributes:

- Brand name
- Line of business

Notes based on the generic product categorization hierarchy as it pertains to FOCUS (starting from the bottom):

- While "Unit" is already used in FOCUS to refer to the unit of measure, the more specific "SKU" term has been adopted to refer to that lowest-level item, which encapsulates all variations of the offering, including but not limited to:
  - How a Purchase charge it was paid (i.e., full, partial, or no upfront fees).
  - The length of time a Purchase charge is applicable (e.g., 1 year, 3 years, 5 years).
  - Region or location the SKU is operated within, which may differ from the resource region.
  - How granular usage is charged (e.g., per month, day, hour, minute, second).
  - How Usage charges are measured (e.g., by size, by time, by amount).
- Given all of the attributes that make up the specific SKU must be independently defined for analysis, the primary defining characteristic of the SKU is the size/shape/tier/version/edition of that service offering. Given existing patterns in FOCUS, we can refer to this as the "Type". This also aligns well to clouds that use "instance type" to define this value.
- If an instance type or VM size is a "SKU Type", then the "SKU Line" would be the family that SKU type falls within.
- Given all level of the SKU categorization schema may not be applicable, should level's be applied top-down, bottom-up, or as they fit the description, which could be in the middle of the hierarchy?
  - Pro for top-down is it's always consistent.
  - Con for top-down is a service may define additional layers in the future and something like a SKU line would change over time.
  - Pro for bottom-up is the concept of a SKU line is more intuitive and easier to understand and most likely to be consistent over time as SKUs change and mature.
  - Con for bottom-up is if there are multiple levels of null values, it may be difficult to understand determine what the SKU is.
    - This also applies to top-down.
    - We could use the same value from the level above, but that would increase data size with little value (other than easier to understand reporting aggregations, which may mkae it worth it).
  - Pro for mixed is values to into the columns that make the most sense.
  - Con for mixed is it's more unpredectable that you don't know whether there will be lower-level values when a null is hit.
- What name should we use in place of the "Need" level?
  - "SKU Service" might be confusing given "Service" is already used to refer to the overarching offering. (Or maybe this binds them together?)
  - Google uses "SKU Group", which makes sense. "Product Group" is a common term in the industry and since we replaced "product" with "SKU", that makes sense.
  - One thing that feels missing from the categorization is a "brand" or "line of business" level. This might be the logical equivalent of the "Need", but is more specific in its purpose.
  - Other options: Domain, Segment, Offering.

Product categorization sources:

- https://catsy.com/blog/product-categorization
- https://www.cleverism.com/lexicon/product-hierarchy
- https://www.yourarticlelibrary.com/products/product-management-product-levels-product-hierarchy-product-mix-and-other-details/22202
- https://airfocus.com/blog/how-to-setup-product-hierarchies
- https://www.indeed.com/career-advice/career-development/product-hierarchy
- https://www.marketing91.com/product-class
- https://www.marketing91.com/understanding-product-hierarchy
- https://docs.bmc.com/docs/ac2105/product-categorization-1002218039.html
- https://medusajs.com/blog/what-i-learned-from-studying-500-b2b-ecommerce-sites
- https://study.com/academy/lesson/products-services-definitions-classifications.html
- https://www.marketing91.com/product-classification
- https://jisajournal.springeropen.com/articles/10.1007/s13174-011-0027-x

The following are common SKU categorization columns in AWS (see [service attributes](https://docs.aws.amazon.com/cur/latest/userguide/samples/Column_Attribute_Service.zip)):

- AWS: servicecode, servicename, productFamily, group, productname, operatingSystem, instanceFamily, instanceType (EC2, GameLift)
- AWS: servicecode, servicename, productFamily, group, productname, instanceFamily, instanceType (DocDB, ElastiCache, Neptune, RDS)
- AWS: servicecode, servicename, productFamily, group, workforceType, productname, instanceType (SageMaker)
- AWS: servicecode, servicename, productFamily, group, productname, instanceType (CloudSearch, Redshift)
- AWS: servicecode, servicename, productFamily, group, productname (CloudDirectory, CloudFront, CloudWatch, Comprehend, DynamoDB, Glacier, GuardDuty, Kinesis, Lex, Lightsail, Pinpoint, Quicksight, Rekognition, Route53, S3, SES, SNS, States, SWF, VPC, WorkSpaces, Glue, IoTAnalytics, kms, Lambda, OpsWorks, QueueService, SecretsManager, waf, XRay)
- AWS: servicecode, servicename, productFamily, group (SnowBall)
- AWS: servicecode, servicename, productFamily, category, productname (Config)
- AWS: servicecode, servicename, productFamily, productname, operatingSystem, instanceFamily, instanceFunction, instanceType (AppStream)
- AWS: servicecode, servicename, productFamily, productname, instanceFamily, instanceType (DAX, ElasticMapReduce, ES, DatabaseMigrationSvc)
- AWS: servicecode, servicename, productFamily, productname, operatingSystem (CodeBuild)
- AWS: servicecode, servicename, productFamily, productname, instanceFamily (CloudHSM)
- AWS: servicecode, servicename, productFamily, productname, instanceType (Amplify, SimpleDB)
- AWS: servicecode, servicename, productFamily, storageclass, productname (EFS, MQ, ElementalMediaStore, StorageGateway)
- AWS: servicecode, servicename, productFamily, storagetype, productname (ECR, Backup)
- AWS: servicecode, servicename, productFamily, productname (API Gateway, Athena, Chime, Cognito, Connect, ECS, EI, EKS, Inspector, Macie, MSK, Polly, Sumerian, Translate, WorkDocs, WorkLink, AppSync, CertificateManager, CloudMap, CloudTrail, CodeDeploy, CodePipeline, CostExplorer, DataSync, DataTransfer, DeviceFarm, DirectConnect, DirectoryService, ElementalMediaConvert, ElementalMediaLive, ElementalMediaPackage, ElementalMediaTailor, Events, FMS, Greengrass, IoT, IoT1Click, IoTDeviceDefender, IoTDeviceManagement, RoboMaker, SystemsManager, Transfer)
- AWS: servicecode, productFamily, group, productname (DataPipeline, ML, WAM, CodeCommit)
- AWS: servicecode, productFamily, productname (AlexaTopSites, AlexaWebInfoService, CognitoSync, WorkMail, Budgets, DeveloperSupport, ServiceCatalog, SupportBusiness, SupportEnterprise)
- AWS: servicecode, servicename, productFamily (Transcribe)
- AWS: servicecode, productFamily (MobileAnalytics)

[Other potential columns](https://docs.aws.amazon.com/cur/latest/userguide/product-columns.html) that could not be validated:

- AWS: product/databaseedition
- AWS: product/instance
- AWS: product/classificationType
- AWS: product/cloudSearchVersion
- AWS: product/computeFamily
- AWS: product/contentType
- AWS: product/deviceType
- AWS: product/directoryType
- AWS: product/endpointType
- AWS: product/eventType
- AWS: product/flowType
- AWS: product/instancesku
- AWS: product/operatingSystem
- AWS: product/requestType
- AWS: product/storageClass
- AWS: product/storageFamily
- AWS: product/subscriptionType
- AWS: product/usageFamily
- AWS: product/type
- AWS: product/version
- AWS: product/releaseType
- AWS: product/snowballType

Example JSON description of a products from AWS:

```json
{
  "formatVersion": "v1.0",
  "disclaimer": "This pricing list is for informational purposes only. All prices are subject to the additional terms included in the pricing pages on http://aws.amazon.com. All Free Tier prices are also subject to the terms included at https://aws.amazon.com/free/",
  "offerCode": "AmazonRDS",
  "version": "20230328234721",
  "publicationDate": "2023-03-28T23:47:21Z",
  "products": {
    "6ERZSWKKAH5TDEQ2": {
      "sku": "6ERZSWKKAH5TDEQ2",
      "productFamily": "Database Instance",
      "attributes": {
        // Product categorization (also note productFamily above)
        "servicecode": "AmazonRDS",
        "servicename": "Amazon Relational Database Service",
        "databaseEngine": "PostgreSQL",
        "instanceFamily": "Memory optimized",
        "instanceTypeFamily": "R5b",
        "instanceType": "db.r5b.16xlarge",

        // Where the product is available
        "locationType": "AWS Region",
        "location": "US East (N. Virginia)",
        "regionCode": "us-east-1",
        "deploymentOption": "Single-AZ",

        // How the product is used/measured
        "usagetype": "InstanceUsage:db.r5b.16xl",
        "operation": "CreateDBInstance:0014",

        // Non-operational metadata
        "licenseModel": "No license required",

        // Technical specs
        "currentGeneration": "Yes",
        "physicalProcessor": "Intel Xeon Platinum 8000 series",
        "vcpu": "64",
        "clockSpeed": "Up to 3.1 GHz",
        "memory": "512 GiB",
        "storage": "EBS Only",
        "networkPerformance": "20 Gigabit",
        "processorArchitecture": "64-bit",
        "engineCode": "14",
        "dedicatedEbsThroughput": "5000 Mbps",
        "enhancedNetworkingSupported": "Yes",
        "normalizationSizeFactor": "128"
      }
    }
  }
}
```

Examples of SKU groups in Google Cloud ([see all](https://cloud.google.com/skus/sku-groups)):

- App Engine
- BigQuery
- CDN
- Chronicle
- Cloud Armor
- Cloud SQL Enterprise
- Data Analytics
- Databases
- Google Kubernetes Engine
- Networking
- VMs (1 Year CUD)
- Vertex Prediction

Google also makes note of additional "service families" in https://cloud.google.com/skus/other
