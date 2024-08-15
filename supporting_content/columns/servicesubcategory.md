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


### Discussions

A series of open questions were discussed over the course of July and August 2024, both in the [draft spreadsheet](https://docs.google.com/spreadsheets/d/1aYq79sWp8TK4zbcSKUb-gRIBei3fERVwAgDJ5ezZf1w/edit?usp=sharing) and in Task Force (TF) and Member calls.  This section attempts to capture the largest of those discussions.

#### Shall the Category composition from FOCUS 1.0?

With Subcategories now in scope for FOCUS 1.1, it unlocks the potential of rolling existing Categories together.  For example: 

- `Identity` could become a child Subcategory of `Security`.
- `Web` and `Mobile` could be grouped together into a net-new category (proposed `Front-end` or `Application Tools`).
- Activity that is truly cross-categorical could be placed in a net-new category (proposed `Crossfunctional`).

After much discussion, particularly on the 8/6 TF1 call, it became clear that the "burden of proof" for changing existing Categories is higher, given that some of the group feels this to constitute a "breaking change".  Some of the group felt that Service Categories and Subcategories should be considered more of a "living document" that is revisited from one FOCUS release to another, in order to stay more tightly aligned with the slowly-changing nature of Service categorizations; others felt that would be disruptive for FOCUS consumers who have constructed various downstream artifacts that depend on a certain Category and Subcategory composition.

Outcome: leave the Category composition in place for FOCUS 1.1 and narrow scope of this release to only add Subcategories underneath them, leaving the door open to alter the Category composition in a future major release.

#### Shall Blockchain become its own Category, or shall it be a Subcategory of Compute?

This was discussed on the 7/23/24 Task Force (TF) 1 call.

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

Outcome: Option :two: was chosen.






