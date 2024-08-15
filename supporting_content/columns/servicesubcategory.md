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






