# FOCUS Development Process

## Overview

This document is aimed at outlining how the FOCUS Working Group develops the specification.  It defines the workflows, processes, and collaboration expectations for all development activities, including Issue management, Pull Request handling, approval workflows, and communication guidelines.\
\
Nothing in this document overrides any requirements of the FOCUS Working Group as outlined in the [FOCUS Foundation repository,](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation) including the [workflows](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/workflow-procedures.md) required to maintain our [intellectual property review](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/working_draft/ipr.md) (IPR) protections. All members are required to follow the FOCUS project’s [code of conduct](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/code_of_conduct.md).


## Git Issues

All work in the FOCUS Project must be tracked via a GitHub Issue. This ensures visibility into what is happening and why changes are being made to the specification. Updates to an Issue's attributes (such as, the due date changing, descriptions, definition of done, assignees) in GitHub should always be accompanied by a comment adding context as to why the change was required. As the group aims to operate more asynchronously these comments are essential.


### Naming and Descriptions

Naming for all Issues should aim to be short, but remain clear and descriptive. Issue names that are too generic are hard to find, and long descriptions as the names of Issues makes it harder to list Issues. Descriptions should be detailed enough that with only the Issue itself a FOCUS member is able to understand the purpose of the Issue. 


### Issue Types

Issues should be created via the use of issue templates that adhere to Issue Types. The Working Group uses four Issue Types: Feedback, Work Items, Action Items, and Maintenance Tasks.


#### Feedback

All minor corrections (typos, syntax, editorial changes) should be introduced to the FOCUS project via GitHub Issues of the type Feedback. The template for these Issues will ensure the needed information is gathered and available for prioritisation processes. Anyone can submit Feedback Issues within the GitHub repository. The description for feedback items should aim to be clear what the desired outcome should be, however for non-FOCUS members a solution should not be included (e.g. Column names, types of data to include, normative text suggestions). 

Feedback Issues will have the Type: Feedback and Label: feedback, and be associated with the FOCUS WG project.

Everyone is welcome to add comments to further define the feedback item, add concerns and/or considerations you would like to see taken into account when developing a solution for the feedback. Support for a feedback item can also be shown in the form of reactions on the Issue ticket.

Feedback Issues will have a title that starts with \`\[Feedback]\`.


#### Feature Request

All suggestions and feature requests should be introduced to the FOCUS project via GitHub Issues of the type Feature Request. The template for these Issues will ensure the needed information is gathered and available for prioritisation processes. Anyone can submit Feedback Issues within the GitHub repository. The description for feature request items should aim to be clear what the desired outcome should be, however for non-FOCUS members a solution should not be included (e.g. Column names, types of data to include, normative text suggestions). 

Feedback Issues will have the Type: Feature Request and Label: feature request, and be associated with the FOCUS WG project.

Everyone is welcome to add comments to further define the feature request item, add concerns and/or considerations you would like to see taken into account when developing a solution for the feature request. Support for a feature request item can also be shown in the form of reactions on the Issue ticket.

Feature Request Issues will have a title that starts with \`\[FR]\`.


#### Work Items

Once a Feedback Issue has been accepted into scope for a release, a Work Item (WI) Issue will be created to describe the work, define the scope, and set the definition of done.

Work Items are parent issues that describe a larger piece of work for the FOCUS specification development and should be associated with many children Action Item Issues which outline individual pieces of work needed to conclude work on the Work Item.

The Assignee(s) of a Work Item Issue is ultimately the FOCUS member(s) leading the development of that particular piece of work. If you would like to contribute to an open Work Item, the best first step would be to reach out to the Assignee(s) for guidance.

Work Item Issues will have a title that starts with \`\[WI]\`.


#### Action Items

Action Item (AI) Issues are used to track the concrete steps necessary for developing a Work Item.  An AI should be granular: ideally a single action with a simple definition of done. This makes Action Items easier to understand and for asynchronous work to be performed on them.

If it is determined that an AI is too large or contains multiple items, it should be split into multiple AI Issues to assist in keeping them as atomic as possible.

The Assignee(s) of an AI Issue is ultimately the FOCUS member(s) leading the development of that particular piece of work. If you would like to contribute to an open AI the best first step would be to reach out to the assignee(s) for guidance.

Action Item Issues will have a title that starts with \`\[AI]\`.


#### Maintenance Tasks

This Issue type is reserved for work that does not affect the contents of the Specification itself but the processes around the working of the repository, such as, adding Issue Templates, updating GitHub Actions Workflows, changing settings on the repository configuration, etc.

### Project

The working group oversees the scope of the next release via a GitHub project.

#### Status

Each issue carries one of the following Status values, which represent the overall working group workflow from ideation to completion.

- Submitted: newly filed, awaiting triage
- Needs More Info: triaged; needs more clarification or detail before prioritization can begin
- Under Consideration: being actively evaluated for upcoming spec work
- Accepted in Scope: will be developed in next release
- Ready for Dev: not started
- In Discussion: in progress
- PR Needed: TF requires a concrete proposal to move forward
- PR In Draft: PR being authored
- PR TF Review: PR issued and in review with Task Force
- PR Member Review: TF approved, in review with Members
- PR Ready for Approval: all threads resolved, ready for approval
- PR Approved: PR approved by Members
- Implemented: done and dusted
- Blocked: cannot move forward
- Closed: out of scope, not feasible, or duplicative

Some notes about the use of Status values:

- Each issue is assigned a Status of `Submitted` upon creation.
- Each issue moves through these Status values as they are developed.
- An issue that is postponed during the development phase is moved back to `Under Consideration` for the next release.
- Each issue is assigned a Status of `Closed` upon being closed.
- An issue that is assigned a Status of `Implemented` will automatically be closed.
- Not every value is applicable to every issue type.

#### AI Status

Action Items carry a separate custom field called `AI Status` that carries a smaller set of values:

- Open
- In Progress
- Blocked
- On Hold
- Closed
- Completed
- Postponed

Each Action Item is assigned an AI Status of `Open` upon creation.

## Content Creation

This section details best practices for the creation of content that is added to the specification.  This section will be augmented over time.

### Table Conversion for Markdown

Working group content is often created and socialized in Google Workspace, especially via Google Sheets.  Often, content in those spreadsheets needs conversion into markdown for inclusion in the spec or supporting content.  Here a couple of tools to use for converting to markdown:

- [Clipboard-To-Markdown](https://euangoddard.github.io/clipboard2markdown/) is useful for converting content other than the tables within your content.
- [Tables Generator](https://www.tablesgenerator.com/markdown_tables) is useful for converting tables in your content.

## Git Branches

### Branch Pipeline

Our branch promotion process takes the following path:

- _<\<dev\_branch>>:_ The feature branch in which a FOCUS Working Group member creates changes.  Such feature branches are ephemeral and are automatically deleted once their content is merged into the working draft.
- _working\_draft:_ The branch in which all approved changes are collected during development.
- _candidate\_recommendation_: The branch in which all approved changes are collected at the end of development for a release. Content in this branch is held for 30 days to enable the [Intellectual Property Rights (IPR) review process](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/working_draft/ipr.md).
- _main_: The branch in which all approved changes are published after Steering Committee ratification of the latest release.

The process by which the Working Group promotes changes across these branches is described below.


### Protected Branches

As per the overarching [procedures](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/workflow-procedures.md)/[workflow](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/w3c_mode_workflow.md) documented in the [FOCUS Foundation repository](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation), the following branches are protected in GitHub:

- _working\_draft_
- _candidate\_recommendation_
- _main_

Merges into the _candidate\_recommendation_ and _main_ branches are only to be performed by the \`Admins\` group in the GitHub Organization as part of the formal approval process with the FOCUS Members and FOCUS Steering Committee respectively.

Development work contributing a change to the FOCUS specification is performed via merging a pull request into the _working\_draft_ branch. Only the \`Admins\` group in GitHub are able to merge content into the _working\_draft_ branch after the formal review and approval process has been completed.


### Feature Branches

Each Task Force (TF) group in the FOCUS Working Group is able to have a Maintainer open a feature branch on behalf of the Task Force either for a single Work Item or a group of related items. This will be the recommended method of organizing work in progress on Work Items over individuals creating working branches themselves and pushing them into the project.


### Branch Management

Members of the FOCUS project need to be aware that all branches in the [FOCUS\_Spec](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec) repository are owned by the project and that frequent cleanups of stale branches will be performed by the \`Admins\`. This means that any scratch/WIP/ideation work which is not part of any open Action Items/Work Items should be moved out to a [fork of the repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) in the individual members own GitHub repository. 

When Pull Requests are merged the option to delete the working branch should always be used, with a preference for a new branch to be created for further work.


### Branch Naming

As members of FOCUS you are able to open branches in the GitHub repository. The naming convention of branches must follow one of the following patterns:

1. Start with your name (e.g. flanakin/skuterm)
2. Start with the Work Item number (e.g. 636-clarify-guidance-around-refunds)

Branches not following this naming convention may be closed without notice.

### Merging

We prefer using merge commits, as they provide traceability and context on the features being merged. For feature branches (used for creating Pull Requests) a clean-up rebase before sharing for review is encouraged. Merge commits are absolutely preferred on the protected branches. Squash merges should be avoided due to the nature of how the original commits are not recorded in the commit graph of the target branch. For more information on how merges work in Git see: ([Different Merge Types in Git](https://lukemerrett.com/different-merge-types-in-git/))


## Pull Requests

Pull Requests (PRs) are used to promote development work through our branch pipeline, with the overarching [contributing guidelines](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/contributing.md) being followed. 


### Naming and Descriptions

The _name_ of a Pull Request should be short but also clearly describe what the pull request is doing. The name should start with a verb in order to describe the action that has taken place (e.g., “Reorganize metadata appendix”, “Correct typos in Section 1.2”).  The reference to the parent issue should be included in the title also (e.g. #628) as often lists of Pull Request titles are made and this helps keep the reference to the related issue (see: Related to Issues).

- Pull requests related directly to Work Items should have a title starting with \`WI #\<number of the WI ticket>:\` followed by a short description
- Pull requests related directly to Action Items should have a title starting with \`AI #\<number of the AI ticket>:\` followed by a short description

The _description_ of a Pull Request should be as detailed as possible to help other members better understand the PRs content. Descriptions should consider the following:

- Any assumed knowledge (Preference a short education, links to relevant docs, etc)
- Example data to demonstrate the outcome of the content being merged
- Any decisions made in the development that are likely to become recurring suggestions (e.g. Decisions on naming, Lists of Values, etc). 

As much as possible, descriptions should provide the most amount of information that enables those with less context of the change being proposed to review the content asynchronously and add valuable feedback.


### Related to Issues

All Pull Requests must be linked to a parent Issue which tracks the work and the reason the pull request was raised. This linking is performed via the “Development” section in the right-hand nav of GitHub.  The definition of done of the parent Issue should be referenced when reviewing the Pull Request to ensure the desired outcomes are being reached.


### Drafting

When a pull request is first opened and still being edited and contributed to by Task Force members, it should be configured to [draft mode](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/changing-the-stage-of-a-pull-request), as this signals to other members of the project that the PR is not ready for full review and should be treated as a work in progress. As a PR becomes ready for review, it should be marked as such in GitHub. If after further review and comments it becomes clear that more work is needed, the Pull Request should be moved back to draft mode, enabling the open PRs to be sorted and reviewed.

Draft status signals that the author is still working on the pull request and would prefer direct conversations on your feedback vs asynchronous review/comments. Adding comments to a draft pull request can be disruptive as the author is forced to stop and respond to your comment vs work on getting the PR completed. It would be best to talk directly with the author and especially important that you involve the author if you are having conversations about the pull request with others. Once a PR comes out of draft status, there will be plenty of time for async feedback.


### Reviewing

It is important for members to review all PRs especially when they are open and in status of ‘PR Member Review’ to ensure you have an opportunity to give feedback on all changes to the Specification. Positive feedback is just as important as feedback looking for further changes, without a 👍 or “Looks good to me” comment your support for a PR is not clearly documented.


### Reviewers Comments and Suggestions

The aim for all comments and suggestions on Issues/PRs should be constructive feedback, this means that comments must clearly:

- Describe the item which is being supported or challenged 
- Aim to provide a suggestion of a solution, or at least suggest some items to consider
- Remain positive and avoid being confrontational or antagonistic

All FOCUS members are encouraged to review and make comments and suggestions. With the aim for all changes to the specification to be by consensus. 

### Reviewing Contributions on GitHub

When submitting review comments using the **“Review Changes”** feature in GitHub, reviewers should select from the three available options based on the nature of their feedback:

#### 1. **Comment**
Use this option to provide *non-blocking feedback*, such as suggestions, requests for clarification, or minor edits.  
- All comments **MUST** be reviewed and considered by the Working Group.  
- Comments **MAY** be dismissed if they are determined to be non-impactful, already resolved, or out of scope.

#### 2. **Approve**
Select this option to indicate **formal approval** of the proposed contribution.  
- At least **three (3)** Working Group members must submit an “Approve” review for the pull request (PR) to be eligible for merging.

#### 3. **Request Changes**
Use this option when **significant revisions** are needed.  
- If the request is made as an **OBJECTION**, it **MUST** be resolved before the contribution can proceed to merge.

### Resolving Comments and Suggestions

As the assignee of a Pull Request you are responsible for timely responses to the comments and suggestions made by reviewers. If a comment or suggestion is unclear it is essential that you ask for clarification as leaving unclear comments will only delay the completion of work. 


### Pull Request Approval and Conflict Resolution

In the FOCUS Members Working Group, contributions are first developed and discussed within the Task Forces, where consensus is gradually built. During this phase, it is considered good practice to provide regular progress updates during the Members meetings to keep the broader group informed.

Once a contribution reaches a sufficient level of maturity and preliminary consensus has been established, it should proceed through **two presentation cycles** at the Members meeting:

1. **First Cycle** – The contribution is presented for **review and feedback** from the broader group.  
2. **Second Cycle** – In a subsequent meeting (typically a different week), the contribution is presented for **formal approval** by the Working Group.

All Pull Requests **must go through a formal review and approval process before being merged into the `working_draft` branch**. This two-step review cycle helps ensure that contributions are visible, well-understood, and aligned with group expectations before final acceptance.

#### Approvals Required

- All reviewers assigned to the Pull Request must approve before the Pull Request is eligible for merging.
- If a reviewer becomes inactive or unresponsive, Maintainers may reassign review to an alternate reviewer.
- At least **one Maintainer** must approve the Pull Request.
- It is not required to have approvals from _all_ FOCUS members, but all active reviewers must approve.


#### Approval Criteria

A Pull Request is eligible for approval when:

- All reviewer comments and suggestions have been resolved or otherwise addressed.
- The Pull Request fully meets the linked Issue's Definition of Done (DoD).
- The Pull Request description is complete, including rationale, data examples, links to supporting information, and explanation of key decisions.
- No unresolved objections remain from reviewers.


#### Conflict Resolution

If reviewers cannot reach consensus or if blocking objections are raised:

- Follow the conflict resolution process outlined in the [FOCUS Foundation repository](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/workflow-procedures.md).
- Escalate to the Maintainers group for mediation if needed.


#### Meeting Approval

Having met all approval criteria, a Pull Request can be scheduled for final review and approval during the weekly FOCUS All Members Meeting.

- Pull Requests in good standing (meeting all above criteria) may be formally approved at the meeting and merged thereafter by Maintainers or Admins as appropriate.


## Git Notifications

GitHub platform has a [notifications inbox](https://github.com/notifications) which members should regularly check on, in order to keep tabs of updates, mentions, and open assigned work that should be reviewed and responded to. Responding to notifications is important as this enables the group to know that you are aware of and have acknowledged the notification. If you are unable to immediately perform the work needed by the notification responding that you have scheduled some time and when to expect an update helps the project keep track of work that is happening.


## Slack

The FOCUS project has its own Slack workspace for members to communicate. As the FOCUS Slack is limited to only members of the Project all decisions, summaries of conversations, and updates about the development of the Specification should always be echoed back into the relevant Pull Request, Work Item, and Action Item tickets in GitHub for the general public to see and the Project to track. All decisions must be documented in the related GitHub Issue or PR within 48 hours.


### Channels

The Slack workspace works on a less is more motto for channels, the desire is to have fewer more active channels than many sparse channels. 


#### #announcements

Used by the FOCUS Staff to provide the whole group updates on major events, milestones, or activities


#### #working-group

Main channel for members to communicate and share information. Remember to update GitHub where relevant.


#### #task-force-\#

Sub group specific channels for targeted conversations about work items/action items. Remember to update GitHub where relevant.

##### #tf-<name>
Further subgroups are created for larger items like SaaS, sku properties, etc.


#### #maintainers

Channel for maintainers to communicate and update each other about activities.


## Glossary

- CLA = Contributor License Agreement
- WG = Working Group
- TF = Task Force
- DoD = Definition of Done
- PR = Pull Request
- FR = Feature Request
- WI = Work Item
- AI = Action Item
- FOCUS member = Individuals contributing after their Organization signs the [CLA](https://github.com/FinOps-Open-Cost-and-Usage-Spec/EasyCLA).

