# Contributing to the FOCUS Working Group

> This repository represents the written spec, not working code.  As such, most people will not need any development environment; most of the work around the spec happens in regularly scheduled discussions and issues here in Github.

Thank you for your interest in contributing to the **FinOps Open Cost and Usage Specification (FOCUS)**.  
This repository contains the technical specification and supporting documentation for the FOCUS project under the **FinOps Foundation**.

Before contributing, please review the following guidelines carefully to ensure consistency and efficiency across all contributions.

---

## 1. Before You Start

1. **Join the FOCUS Project**
   - If you’re not already a participant, visit the [FOCUS Enrolment](https://enrollment.lfx.linuxfoundation.org/?project=finopsopenbillingspec) for instructions on how **your company** can join the FOCUS Open Standards Project. In addition, you must be approved by your company as a contributor to this project. You are required to complete the steps indicated in the [README of the EasyCLA](https://github.com/FinOps-Open-Cost-and-Usage-Spec/EasyCLA/blob/main/README.md) repository.
   - Only authorized contributors can submit or review Pull Requests.

2. **Get Familiar with the Project**
   - Review the [FOCUS Specification Overview](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/working_draft/README.md#overview) and the latest release.
   - Join the **FOCUS Slack working-group** for discussions and meeting updates. _(you will be invited once you have completed the [README CLA](https://github.com/FinOps-Open-Cost-and-Usage-Spec/EasyCLA/blob/main/README.md) steps)_
   - Familiarize yourself with the [Roles & Tasks](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/operating_procedures.md#22-organization-roles) and [Review & Approval Process](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/operating_procedures.md#52-review--approval).

---

## 2. Types of Contributions

You can contribute to this repository in several ways:

- **Action Items** – Updates or follow-up tasks resulting from meetings.

- **Feature Requests** – Proposals for new functionality, attributes, or examples.

- **Feedback** – Comments or recommendations on existing content.

- **Maintenance** – Fixes or updates for typos, structure, or metadata.

- **Work Items** – Specific contributions tracked as GitHub issues.

If you are not sure where your contribution fits, open a **Blank Issue** first and request feedback before submitting a Pull Request (PR).

---

## 3. Contribution Process

1. **Fork this repository** and create a branch for your work:
```bash
git checkout -b feature/your-change-description
```

> For further details on how to work with Git and GitHub, refer to the [GitHub Guidelines](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/working_draft/guidelines/github-guidelines.md).

2. **Reference existing issues** or create a new one to track your change. Include the issue number in your PR title or description (e.g., Fixes #845).

3. **Follow FOCUS content conventions:**

- Use BCP-14 keywords (**MUST**, **SHOULD**, **MAY**, etc.) correctly.  
- Do not remove normative content without prior discussion.

> See [Typographic Conventions](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/working_draft/specification/overview.md#typographic-conventions), (e.g., “for how to use BCP-14 keywords”).

4. **Submit your PR**

- Include a clear summary of the change.  
- Use one PR per logical change.  
- Assign appropriate labels (e.g., `normative-change`, `editorial`, `discussion`).

> For details about labels and stages, see [Git Issues - Project - Content Creation](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/working_draft/guidelines/development-processes.md#focus-development-process)

5. **Participate in the review**

- Your PR will go through the following review sequence:

    - **Maintainers / Task Force(s) → Members (for review and approval)**

    - Be responsive to reviewer comments and requested edits.

---

6. **Writing Style and Format**

- Use the provided Markdown Editorial Guidelines for all specification text.  
- Follow the structure of existing sections (Introduction → Requirements → Examples → Notes).  
- Use **RFC 2119** language for normative statements.

> Visit [Editorial Guidelines](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/working_draft/guidelines/editorial-guidelines.md) for further information.


7. **Normative vs Supporting Content**

- **Normative content** defines required behavior using **MUST**, **SHALL**, or **SHOULD**.  
- **Supporting content** explains context or provides examples.  
- If your contribution changes a normative rule, it will require review by the **Task Force** and **Members** before approval.

---

8. **Review and Approval Flow**

| Stage | Responsible Group     | Description                                           |
|:------:|----------------------|-------------------------------------------------------|
| 1 | Maintainers | Broad alignment and quality assurance |
| 2 | Task Force | Technical review and discussion of proposed change |
| 3 | Members Working Group | Broad review and approval |

Status changes and approvals are tracked in GitHub **Issues** and **Pull Requests**.

---

9. **Resources and References**

- [FOCUS Specification Website](https://focus.finops.org/focus-specification/)  
- [FOCUS Governance Repository](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation)  
- [FOCUS Membership Enrollment](https://enrollment.lfx.linuxfoundation.org/?project=finopsopenbillingspec) _Company joining instructions_ 
- [FOCUS CLA Contribution](https://github.com/FinOps-Open-Cost-and-Usage-Spec/EasyCLA) _Contributors approved by own company_
- [FinOps Foundation](https://www.finops.org)  

10. **License and Intellectual Property**

All contributions are made under the terms of the **[FOCUS Member Agreement](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/FOCUS_-_Membership_Agreement_Package_for_use.pdf)**, as stated in the [LICENSE](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/working_draft/license.md) file.  
By submitting a contribution, you agree that:

- Your work complies with the project’s **[IPR and CLA](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/FOCUS_-_Membership_Agreement_Package_for_use.pdf)** requirements.  
- You have the rights to submit the content.  
- Contributions become part of the open **FinOps FOCUS Specification**.

