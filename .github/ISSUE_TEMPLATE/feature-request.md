---
name: Feature Request
about: Propose a new feature or enhancement to the FOCUS specification
labels: feature, needs triage
assignees: matt-cowsert
---

# Feature Request

> **For Requesters:** Complete only the "Requester Information" section below (estimated time: 10-15 minutes). The "Maintainer Assessment" section will be completed by FOCUS Maintainers during triage.
>
> Brief, clear responses are fine. Maintainers will follow up if more detail is needed.
>
> **Required fields:** Problem Statement, Use Case / User Story, Success Criteria, Type of Request, Organizations Requesting This Feature
>
> **Optional but helpful:** Data Generator Support, Supporting Documentation, Proposed Solution / Approach, Additional Context

---

## Requester Information

### Problem Statement
Describe the problem, issue, or opportunity this feature addresses. What is FOCUS unable to do today that creates this problem? Include practitioner quotes or real-world examples if available.

```
Write your problem statement here.
```

---

### Use Case / User Story
Provide a clear, specific use case that defines what is being provided to the practitioner or persona:

**As a** [specific role - e.g., FinOps Practitioner, Data Engineer, Procurement/Finance, Tooling Vendor]
**I need to** [specific capability in FOCUS data]
**So that** [measurable outcome or decision I can make]

**Example:**
> As a FinOps practitioner, I need to group costs by resource groupings within my Sub Account, so that I can align cost reporting with my organization's structure without post-processing.

```
Write your use case here.
```

---

### Success Criteria
What needs to be true when we deliver this capability for it to be meaningful? Describe 2-4 specific criteria. Focus on what you need to be able to DO with the data, not implementation details.

**Example** *(describe what you can DO, not structural changes like "add column X"):*
- I can perform cost allocation using this data without additional processing
- The data is consistently available across all data generators that support this concept
- Missing or unavailable data is handled in a clear, standardized way

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3
- [ ] Criterion 4

---

### Type of Request
**Select the option that best describes this request.** Maintainers may reclassify during triage.

- [ ] **Standardization** - Data already exists across data generators but is not yet normalized in FOCUS
- [ ] **Enhancement** - Refinement or extension of an existing FOCUS column, metric, or capability
- [ ] **Net New** - A concept not yet represented in FOCUS or widely available from data generators
- [ ] **Enablement/Supporting Content** - Non-normative items like appendix explanations, examples, or supporting documentation
- [ ] **Tech Debt** - Addressing technical debt or maintenance items *(Note: For Tech Debt items, feel free to liberally delete sections of this template that aren't relevant)*

---

### Organizations Requesting This Feature
List one or more organizations who have requested or explicitly supported this request. For each organization, indicate whether this feature blocks their adoption of FOCUS or is a nice-to-have enhancement.

**Format:**
- **[Organization Name]** - [Adoption Blocker / Nice to Have] - [Brief explanation]

**Example:**
- **Acme Corp** - Adoption Blocker - Cannot implement FOCUS without multi-cloud tagging support
- **BigCloud Inc** - Nice to Have - Would streamline our reporting process

```
List organizations here.
```

---

### Data Generator Support (Optional)
Do data generators already support this concept in their native billing data? It's OK to select "Unknown." Maintainers will validate during triage.

- [ ] **Yes** - Widely available across data generators
- [ ] **Partially** - Some data generators support this, others don't
- [ ] **No** - Would require new data collection/exposure
- [ ] **Unknown** - Not sure about data generator support

**If yes or partially, please provide links to documentation:**

```
Links to data generator documentation.
```

---

### Supporting Documentation (Optional)
Include links to data samples, relevant PRs, GitHub discussions, or implementation references.

> **Reminder:** Please ensure any linked documents are accessible to maintainers and collaborators. If access is restricted, your request may be delayed.

```
Paste links here.
```

---

### Proposed Solution / Approach (Optional)
Share initial ideas, constraints, and feasibility considerations if you have them. Solutions are welcome but not required. Maintainers may explore alternative approaches during discovery.

```
Your proposal goes here.
```

---

### Additional Context (Optional)
Add any other context that might be helpful:

**Current Workaround:**
```
What do you do today without this feature? Is this a heavy workaround or a slight inconvenience?
```

**Urgency/Timeline:**
```
Is there a specific timeframe when your organization needs this?
```

**Related Requests:**
```
Links to similar or related feature requests or scopes of work.
```

---

> **STOP:** The sections below are for FOCUS Maintainers only. Requesters do not need to fill these out. **Scroll to the bottom and click "Create" to submit your request.**

---

## Maintainer Assessment
*This section will be completed by FOCUS Maintainers during triage.*

### Adoption Impact
Which category best describes this feature's impact on FOCUS adoption?

- [ ] **Adoption Blocker** - Organizations cannot adopt FOCUS without this feature
- [ ] **Adoption Accelerator** - This feature would help organizations start using FOCUS
- [ ] **Practitioner Enhancement** - Improves experience for existing FOCUS users
- [ ] **Technical Improvement** - Internal specification refinement

**Justification:**

```
FOCUS Maintainers complete during triage.
```

---

### Supported Features Alignment
Which [FOCUS Supported Features](https://focus.finops.org/#supported-features) does this request enable or enhance? If you know which supported feature this relates to, please specify. If this enables a new supported feature, describe it below.

**Feature Description:**

```
FOCUS Maintainers describe how this request advances FinOps capabilities or defines new supported features.
```

---

### Implementation Scope
*Note: This section should not block the creation of the feature request. If the scope isn't clear yet, it can be filled in during the discovery/development phase.*

**Phasing/Sequencing:**
What is the minimum we can deliver (MVP) vs. the long-term state?

**MVP Definition:**

```
FOCUS Maintainers define minimum implementation that provides value.
```

**North Star Vision:**

```
FOCUS Maintainers describe ideal complete solution.
```

**Phasing Strategy:**

```
FOCUS Maintainers determine if/how this should be implemented in phases.
```

---

### Specification Impact

**Impacted Parties:**
- [ ] FinOps Practitioner - end users who analyze or act on the data
- [ ] FOCUS Data Generator - data generators producing output aligned to the spec
- [ ] Vendor Supporting FOCUS - vendors or tools ingesting the spec or using the spec language in their UI
- [ ] Other: [specify]

**Level of Ambiguity:**
*Note: This is for maintainers to assess, not for requesters to estimate.*

Rate from 1 to 5:
- 1 = very well-defined, low complexity
- 3 = moderately scoped, some ambiguity
- 5 = vague, high complexity or conceptual

```
Rating and reasoning.
```

---

### FinOps Scope Alignment
Does this request align with one or more of the following [FinOps Scopes](https://www.finops.org/framework/scopes/)?

- [ ] Public Cloud - e.g., AWS, Azure, GCP, OCI
- [ ] Software-as-a-Service (SaaS) - e.g., Salesforce, Snowflake
- [ ] Data Center - on-prem compute and infrastructure
- [ ] Licensing - subscription or usage-based licensing models *(under development)*
- [ ] AI - cost and usage for AI models and platforms *(under development)*
- [ ] Custom - internal tooling, specialized infra *(under development)*

## Community Support
If your organization supports this request or has a similar use case:

- Add a **comment** below including:
  - Your **organization**
  - A **brief explanation** of why this is important to you (e.g., use case, urgency)
- FOCUS Staff & Maintainers will aggregate supporting orgs over time.
