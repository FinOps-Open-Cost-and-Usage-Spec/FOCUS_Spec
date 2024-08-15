# Column: ServiceSubcategory

## Example provider mappings

Current column mappings found in available data sets:

| Provider  | Data set                 | Column                                     |
| --------- | ------------------------ | ------------------------------------------ |
| AWS       | FOCUS; CUR                      | None                                       |
| GCP       | FOCUS; Big Query Billing Export | None                                       |
| Microsoft | FOCUS; Cost details             | None |
| OCI | FOCUS; Cost reports | None |

The creation of this publically-available column shall be net-new for the cloud service providers, though they may already maintain their own proprietary Subcategories.  For example, AWS describes their Database Subcategories [here](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/database.html).

## Discussion / Scratch space

### Sample provider mappings
Here are sample subcategorizations of various services across the AWS, Azure, and GCP landscape.

To be clear, this list is neither prescriptive nor suggestive; it shall be up to the providers to decide where to assign their services, and FOCUS shall merely provide the list of available Subcategories.  This list was generated merely for illustrative purposes when constructing the subcategories.

| Category                | Subcategory                     | AWS                                                     | Azure                                     | GCP                                                              |
| ----------------------- | ------------------------------- | ------------------------------------------------------- | ----------------------------------------- | ---------------------------------------------------------------- |
| AI and Machine Learning | Generative AI                   | Bedrock, Q                                              | Azure OpenAI                              | Gemini                                                           |
|                         | Language AI                     | Polly, Transcribe, Translate, Lex                       | AI Services, Speech Services              | natural language AI, text-to-speech, Speech-to-text, Document AI |
|                         | Machine Learning                | Sagemaker, Sagemaker Savings Plan, Lookout, Personalize | Machine Learning                          |                                                                  |
|                         | Search                          | Cognitive Search, CloudSearch, Elasticsearch, Kendra    | Azure AI Search                           | Vertex AI Search                                                 |
|                         | Bots                            | Lex, Robomaker                                          | Bot Service, Health Bot                   |                                                                  |
|                         | Other (AI and Machine Learning) | Capacity Blocks, Rekognition                            | Video Indexer, Autonomous Systems, Syntex |                                                                  |
|                         |                                 |                                                         |                                           |                                                                  |
| Analytics               | Analytics Platform              | Athena                                                  | Fabric, Synapse                           |                                                                  |
|                         | Business Intelligence           | QuickSight, Grafana                                     | Power BI, Grafana, Analysis Services      | Looker                                                           |
|                         | Streaming Analytics             | Kinesis                                                 | Stream Analytics, Data Explorer           |                                                                  |
|                         | Data Processing                 | EMR, Batch, Glue, Data Pipeline                         | (none)                                    | Cloud Composer, Dataflow, Dataproc                               |

### Principles

- Undercategorize rather than overcategorize where there is not broad consensus.  Allow the community to advocate for new Subcategories (and Categories) in future releases, and leave Services uncategorized and/or unsubcategorized in the meantime.

### Discussions

A series of open questions were discussed over the course of July and August 2024, both in the [draft spreadsheet](https://docs.google.com/spreadsheets/d/1aYq79sWp8TK4zbcSKUb-gRIBei3fERVwAgDJ5ezZf1w/edit?usp=sharing) and in Task Force (TF) and Member calls.  This section attempts to describe the largest of those discussions.

#### Shall the Category composition change from FOCUS 1.0?

With Subcategories now in scope for FOCUS 1.1, there was then the potential of changing Categories.  For example: 

- `Identity` could become a child Subcategory of `Security`.
- `Web` and `Mobile` could be grouped together into a net-new category (proposed `Front-end` or `Application Tools`).
- Activity that is truly cross-categorical could be placed in a net-new category (proposed `Crossfunctional`) separate from `Other`, which is more of an uncategorized placeholder.
- `Integration` could be rescoped and renamed `Data Management` to be more inclusive of Service Subcategories such as Data Processing and API Management.
- `Multicloud` could be rescoped and renamed `Hybrid and Multicloud` to be more inclusive of on-premises Services.

After much discussion, particularly on the Aug 6 TF1 call, it became clear that the "burden of proof" for changing existing Categories is higher, given that some of the group feels this to constitute a "breaking change".  Some of the group felt that the Service hierarchy should be considered more of a "living document" that is revisited from one FOCUS release to another, in order to stay more tightly aligned with the slowly-changing nature of Service categorizations; others felt that would be prohibitively disruptive for FOCUS consumers who have constructed various downstream artifacts and depend on a certain Category and Subcategory composition.

_Outcome_: leave the Category composition in place for FOCUS 1.1 and narrow scope of this release to only add Subcategories underneath them, leaving the door open to alter the Category composition in a future release (either major or not, pending a larger decision around what constitutes a "breaking change").

#### Where do Commitment Discounts belong?

Commitment Discounts have various models that could belong in various places of a Service category hierarchy.  For example:

- An Azure reservation for D8as v5 can be both Categorized (i.e. `Compute`) and Subcategorized (i.e. `Virtual Machines`).
- An AWS Compute savings plan can be Categorized (i.e. `Compute`) but not Subcategorized (e.g. it can be applied to both `Virtual Machines` and `Serverless Compute`).
- An OCI Credit can neither be Categorized nor Subcategorized (e.g. it can be applied to a wide variety of usage).

Based on that, there was a robust discussion, particularly on the Jul 23 TF1 and Aug 8 Member calls, as to where Commitment Discounts belong.  Do they deserve their own Subcategories (e.g. `Commitments (Compute)`, `Commitments (Databases)`) underneath each Category?  Do they also deserve their own Category (e.g. `Commitments` or `Crossfunctional`)?

_Outcome_: given the decision not to change the Category composition, and given the principle of undercategorizing rather than overcategorizing: 

- Commitment Discounts with a natural Category / Subcategory shall be placed therein.
- Commitment Discounts with a natural Category but no Subcategory shall be placed in `Other (<Category>)`.
- Commitment Discounts with no natural Category or Subcategory shall be placed in `Other (Other)`.

#### Shall certain technologies be given their own Categories?

The group discussed the possibility of "graduating" Services to their own net-new categories, such as `Blockchain`, `Containers`, and `Mixed Reality`.  These are technologies for which some or all of the three major cloud service providers have created their own Categories, and there is certainly a use case for being able to easily build reports to show those (and only those) Services.

Given the decision not to change the Category composition on the Aug 6 TF1 call, this became a moot discussion.  However, the group did discuss some specific examples, particularly on the Jul 23 TF1 and Jul 25 Member calls:

- `Blockchain` belongs under `Databases > Ledger`.
- `Containers` belongs under `Compute > Containers`.
- `Support` belongs under `Management and Governance`.
- `Mixed Reality` does not deserve its own Category.
- `Industry Specific` does not deserve its own Category.
- `Marketplace` Services shall be placed into the Category and Subcategory aligned with their purpose, rather than placed into a `Marketplace` Category.

_Outcome_: No Category additions or changes at this time.

#### What shall we call the "unsubcategorized" Subcategory?

Each Category carries an "Other" Subcategory to allow the providers to provide a Category without a Subcategory.  A vote was issued via Slack on Aug 13 with the following options:

:one: `Uncategorized (<Category Name>)`  
:two: `Other (<Category Name>)`  
:three: `Uncategorized`  
:four: `Other`  

The following considerations were included:

- Brevity, simplicity, and consistency of Subcategory names (e.g. “Uncategorized (Management and Governance)” is pretty long).
- Delineation of Category values from Subcategory values (e.g. use of Subcategory “Other” underneath all Categories “Compute”, “Databases” and “Other” could be confusing).
- Analytical utility of Subcategory without Category context (e.g. uncategorized Compute from uncategorized Databases are automatically separated in a bar chart).

_Outcome_: Option :two: was chosen.

#### Shall this column be mandatory or optional?

There was some discussion around this at the 8/15 Member call.  Some felt that Service Subcategory should be mandatory because Service Category is mandatory, and together they form a hierarchy.  Others felt that provider adoption would be easier if the column were not required.  Still others felt that making the column mandatory, even populated completely with Other, would entice FOCUS consumers to petition their provider(s) to populate the column with actual Subcategories.

Ultimately, it seemed that the majority leaned towards making it optional.

_Outcome_: Optional.




