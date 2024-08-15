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

A series of open questions were discussed over the course of July and August 2024, both in the [draft spreadsheet](https://docs.google.com/spreadsheets/d/1aYq79sWp8TK4zbcSKUb-gRIBei3fERVwAgDJ5ezZf1w/edit?usp=sharing) and in Task Force (TF) and Member calls.  This section attempts to capture the largest of those discussions.

#### Shall the Category composition from FOCUS 1.0?

With Subcategories now in scope for FOCUS 1.1, it unlocks the potential of rolling existing Categories together.  For example: 

- `Identity` could become a child Subcategory of `Security`.
- `Web` and `Mobile` could be grouped together into a net-new category (proposed `Front-end` or `Application Tools`).
- Activity that is truly cross-categorical could be placed in a net-new category (proposed `Crossfunctional`).

After much discussion, particularly on the 8/6 TF1 call, it became clear that the "burden of proof" for changing existing Categories is higher, given that some of the group feels this to constitute a "breaking change".  Some of the group felt that Service Categories and Subcategories should be considered more of a "living document" that is revisited from one FOCUS release to another, in order to stay more tightly aligned with the slowly-changing nature of Service categorizations; others felt that would be disruptive for FOCUS consumers who have constructed various downstream artifacts that depend on a certain Category and Subcategory composition.

_Outcome_: leave the Category composition in place for FOCUS 1.1 and narrow scope of this release to only add Subcategories underneath them, leaving the door open to alter the Category composition in a future major release.

#### Where do Commitment Discounts belong?

Commitment Discounts have various models that could belong in various places of a Service category hierarchy.  For example:

- An Azure reservation for D8as v5 can be both Categorized (i.e. `Compute`) and Subcategorized (i.e. `Virtual Machines`).
- An AWS Compute savings plan can be Categorized (i.e. `Compute`) but not Subcategorized (e.g. it can be applied to both `Virtual Machines` and `Serverless Compute`).
- An OCI Credit can neither be Categorized nor Subcategorized (e.g. it can be applied to a wide variety of usage).

Based on that, there was a robust discussion, particularly on the 7/23 TF1 and 8/8 Member calls, as to where Commitment Discounts belong.  Do they deserve their own Subcategories (e.g. `Commitments (Compute)`, `Commitments (Databases)`) underneath each Category?  Do they also deserve their own Category (e.g. `Commitments` or `Crossfunctional`)?

_Outcome_: given the decision not to change the Category composition, and given the principle of undercategorizing rather than overcategorizing: 

- Commitment Discounts with a natural Category / Subcategory shall be placed therein.
- Commitment Discounts with a natural Category but no Subcategory shall be placed in `Other (<Category>)`.
- Commitment Discounts with no natural Category or Subcategory shall be placed in `Other (Other)`.

#### Shall certain technologies be given their own Categories?

The group discussed the possibility of "graduating" Services to their own net-new categories, such as `Blockchain`, `Containers`, and `Mixed Reality`.  These are technologies for which some or all of the three major cloud service providers have created their own Categories, and there is certainly a use case for being able to easily build reports to show those (and only those) Services.

Given the decision not to change the Category composition on the 8/6 TF1 call, this became a moot discussion.  However, the group did discuss some specific examples, particularly on the 7/23 TF1 call:

- `Blockchain` belongs under `Databases > Ledger`.
- `Containers` belongs under `Compute > Containers`.
- `Mixed Reality` does not yet deserve its own Category.

#### What to call the "unsubcategorized" Subcategory

Each Category carries an "Other" Subcategory to allow the providers to provide a Category without a Subcategory.  A vote issued on 8/13/24 with the following options:

:one: `Uncategorized (<Category Name>)`  
:two: `Other (<Category Name>)`  
:three: `Uncategorized`  
:four: `Other`  

The following considerations were included:

- Brevity, simplicity, and consistency of Subcategory names (e.g. “Uncategorized (Management and Governance)” is pretty long).
- Delineation of Category values from Subcategory values (e.g. use of Subcategory “Other” underneath all Categories “Compute”, “Databases” and “Other” could be confusing).
- Analytical utility of Subcategory without Category context (e.g. uncategorized Compute from uncategorized Databases are automatically separated in a bar chart).

_Outcome_: Option :two: was chosen.






