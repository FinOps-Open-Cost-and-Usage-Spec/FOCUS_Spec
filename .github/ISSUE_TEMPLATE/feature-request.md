---
name: Feature Request
about: Propose a new feature or enhancement to the FOCUS specification
---

# Feature Request

## Requester Information

### 🧠 Problem Statement
Describe the problem, issue, or opportunity this feature addresses. Include practitioner quotes or real-world examples if available.

[Write your problem statement here.]

---

### 📖 User Story
Provide a clear, specific user story or set of user stories:

**As a** [specific role - e.g., FinOps Practitioner, Data Engineer, Procurement/Finance, Tooling Vendor]
**I need to** [specific capability in FOCUS data]
**So that** [measurable outcome or decision I can make]

**Example:**
> As a FinOps practitioner, I need to group costs by resource groupings within my Sub Account, so that I can align cost reporting with my organization's structure without post-processing.

[Write your user story here.]

---

### ✅ What Success Looks Like
Describe 2-4 specific criteria that would indicate this feature is working correctly. Focus on what you need to be able to DO with the data, not implementation details.

**Example:**
- I can perform cost allocation using this data without additional processing
- The data is consistently available across all data generators that support this concept
- Missing or unavailable data is handled in a clear, standardized way

- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]
- [ ] [Criterion 4]

---

### 📨 Type of Request
**Select the option that best describes this request:**

- [ ] **Standardization** - Data generators already support this; FOCUS needs to standardize how it's represented
- [ ] **Enhancement** - Refining or extending existing FOCUS columns, attributes, metadata, or supported features
- [ ] **New Capability** - Introduces something data generators don't currently expose or FOCUS doesn't currently address
- [ ] **Supporting Content** - Examples, appendices, or explanatory material (not normative spec changes)

---

### 🏛️ Organizations Requesting This Feature
List one or more organizations who have requested or explicitly supported this request (including your own, if applicable).

[e.g., BigCloud Inc, Acme Corp]

---

### 🏗️ Data Generator Support (Optional)
Do data generators already support this concept in their native billing data?

- [ ] **Yes** - Widely available across data generators
- [ ] **Partially** - Some data generators support this, others don't
- [ ] **No** - Would require new data collection/exposure
- [ ] **Unknown** - Not sure about data generator support

**If yes or partially, please provide links to documentation:**

[Links to data generator documentation]

---

### 📂 Supporting Documentation (Optional)
Include links to data samples, relevant PRs, GitHub discussions, or implementation references.

> 🔐 **Reminder:** Please ensure any linked documents are accessible to maintainers and collaborators. If access is restricted, your request may be delayed.

[Paste links here.]

---

### 🛠️ Proposed Solution / Approach (Optional)
Share initial ideas, constraints, and feasibility considerations if you have them.

[Your proposal goes here.]

---

### 💭 Additional Context (Optional)
Add any other context that might be helpful:

**Current Workaround:** [What do you do today without this feature?]
**Urgency/Timeline:** [Is there a specific timeframe when your organization needs this?]
**Related Requests:** [Links to similar or related feature requests]

[Additional context here.]

---

## FOCUS Staff Assessment
*This section will be completed by FOCUS Staff during triage.*

### 🚀 Adoption Impact
Which category best describes this feature's impact on FOCUS adoption?

- [ ] **Adoption Blocker** – Organizations cannot adopt FOCUS without this feature
- [ ] **Adoption Accelerator** – This feature would help organizations start using FOCUS
- [ ] **Practitioner Enhancement** – Improves experience for existing FOCUS users
- [ ] **Technical Improvement** – Internal specification refinement

**Justification:**

[FOCUS Staff completes during triage]

---

### 🔧 Supported Features Alignment
Which existing or new [FOCUS Supported Features](https://focus.finops.org/#supported-features) does this request enable or enhance?

**Existing Features Enhanced:**
- [ ] Cost and Usage Attribution
- [ ] Charge Categorization
- [ ] Effective Cost
- [ ] [Other - specify]

**New Features Enabled:**
- [ ] [Describe new supported feature this would enable]

**Feature Description:**

[FOCUS Team describes how this request advances FinOps capabilities]

---

### 🎯 Implementation Scope
**MVP Definition:**

[FOCUS Team defines minimum implementation that provides value]

**North Star Vision:**

[FOCUS Team describes ideal complete solution]

**Phasing Strategy:**

[FOCUS Team determines if/how this should be implemented in phases]

---

### 📊 Specification Impact

**Impacted Parties:**
- [ ] FinOps Practitioner – end users who analyze or act on the data
- [ ] FOCUS Data Generator – data generators producing output aligned to the spec
- [ ] Vendor Supporting FOCUS – vendors or tools ingesting the spec or using the spec language in their UI
- [ ] Other: [specify]

**Level of Ambiguity:**
Rate from 1 to 5:
- 1 = very well-defined, low complexity
- 3 = moderately scoped, some ambiguity
- 5 = vague, high complexity or conceptual


[Rating and reasoning]

---

### 🌐 FinOps Scope Alignment
Does this request align with one or more of the following [FinOps Scopes](https://www.finops.org/framework/scopes/)?

- [ ] Public Cloud – e.g., AWS, Azure, GCP, OCI
- [ ] Software-as-a-Service (SaaS) – e.g., Salesforce, Snowflake
- [ ] Data Center – on-prem compute and infrastructure
- [ ] Licensing – subscription or usage-based licensing models *(under development)*
- [ ] AI – cost and usage for AI models and platforms *(under development)*
- [ ] Custom – internal tooling, specialized infra *(under development)*

---

## Community Support
If your organization supports this request or has a similar use case:

- Add a **comment** below including:
  - Your **organization**
  - A **brief explanation** of why this is important to you (e.g., use case, urgency)
- FOCUS Staff & Maintainers will aggregate supporting orgs over time.
