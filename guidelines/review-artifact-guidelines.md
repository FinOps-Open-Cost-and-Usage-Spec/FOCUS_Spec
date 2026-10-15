# FOCUS Review Artifact Guidelines

## Overview

A review artifact is a PDF build of the FOCUS Specification that includes content held back from a release, so people can give feedback on it. Only the sections named on its first page are under review, and the rest matches the release it goes out with. It is not a FOCUS release, it is not for production use or conformance claims, and it has no requirements model (the machine-readable form of the specification's rules).

Data generators, which produce FOCUS data, and practitioners, who use it, are asked what it would take to generate or use the data it describes. Trying the content out is welcome. What they learn helps settle the open questions that keep the content out of a release.

A review artifact is built once, from its content as it stood at a single point in time, marked by one tagged commit, and never changed. Its Markdown source stays in GitHub. Its tracking issue, a GitHub issue, records its open questions and every decision, and holds the checklist for building and sharing it.

### Roles

* **Working group:** the FOCUS Working Group, the contributors who develop the specification. Everyone in the working group is encouraged to attend the weekly Members meeting, where pull requests are approved.
* **Maintainers:** working group contributors who lead the project, listed in [MAINTAINERS.md](../MAINTAINERS.md).
* **Pull request authors:** the contributors who opened the pull requests that hold the content under review.
* **Admins:** the GitHub group that merges pull requests.
* **FinOps Foundation staff:** the FinOps Foundation team that supports FOCUS.

### Lifecycle

| Stage | Who | What happens |
| --- | --- | --- |
| 1. Approve | Working group, at the Members meeting | Approve the content and its open questions |
| 2. Build | Pull request authors, Admins | Combine the content into one pull request, tag one commit, and build the labeled PDF |
| 3. Share and review | Admins, FinOps Foundation staff | Share the PDF after its Intellectual Property Rights (IPR) review, and collect feedback |
| 4. Retire | Maintainers and the working group, at the Members meeting | Check progress each release, and retire the review artifact when done |

## Stage 1: Approve

The working group approves a review artifact at the Members meeting after two presentation cycles, as for a pull request (see [Development Processes](contributors/development-processes.md#pull-request-approval-and-conflict-resolution)). Its pull requests need no GitHub approvals, since they are not merged. Supported features, the parts of the specification that show how FOCUS data meets common FinOps needs, are part of the content under review.

A review artifact MUST adhere to the following requirements:

* A review artifact MUST be approved at the Members meeting before it is built.
* When the content under review has supported features, a review artifact MUST include them.
* A review artifact MUST have a tracking issue.

## Stage 2: Build

The content is brought into one pull request, which takes in `working_draft`, the branch where the next release is written. The Admins tag one commit and build the PDF from it. When the approved content has to change before the tag (e.g., to resolve a merge conflict), it is approved again. The label is the text the build adds: a watermark, a version line, and first-page statements, in place of the usual working draft wording.

A review artifact MUST adhere to the following requirements:

* A review artifact MUST be built from its content as it stood at a single point in time, marked by one tagged commit.
* A review artifact MUST NOT be revised after it is built.
* The content under review in a review artifact MUST match the approved content.
* The sections under review MUST include every section that the content under review adds or changes.
* The sections of a review artifact that are not under review MUST match the release it goes out with, as that release enters its IPR review.
* A review artifact MUST be a PDF.
* Links in a review artifact to files in the repository MUST resolve to its tagged commit.
* Every page of a review artifact MUST show a "Review Artifact" watermark.
* The version line of a review artifact MUST include the following:
  * The name of the content under review (e.g., "SKU Price Dataset Review Artifact").
  * A statement that the document has no version number (e.g., "(Unversioned)").
* The first page of a review artifact MUST NOT call the document a working draft.
* The first page of a review artifact MUST include the following:
  * A statement that the document is not a FOCUS release.
  * A statement that the document is not for production use or conformance claims.
  * A statement that trying the content out is welcome.
  * The names of the sections under review.
  * A link to the tracking issue.

## Stage 3: Share and Review

A review artifact goes through an IPR review, a patent review period, at the same time as its release, and is shared only after that review completes. Sharing means sending the PDF, or a link to it, to people for feedback. FinOps Foundation staff collect the feedback. Work on the content continues through the normal development process.

A review artifact MUST adhere to the following requirements:

* A review artifact MUST complete an IPR review before it is shared.
* A review artifact's IPR review MUST run at the same time as the IPR review of the release it goes out with.
* Files from a review artifact build other than the PDF (e.g., `spec.html` or `spec.md`) MUST NOT be shared.
* A review artifact MUST NOT be published on the FOCUS website.
* A review artifact MUST NOT be published on the FinOps Foundation website.
* A review artifact MUST NOT be announced as part of a release.
* Any announcement or message that shares a review artifact MUST state that its content, including any sample data, is out for review.
* The content under review MUST NOT be part of the release that the review artifact goes out with.
* The content under review SHOULD NOT be proposed for a release until the review artifact is retired.

## Stage 4: Retire

A review artifact has no time limit, since content can need more than one release to mature. After retirement, the content is closed, continues under a new review artifact, or moves toward a release through a pull request approved at the Members meeting.

A review artifact MUST adhere to the following requirements:

* A review artifact MUST have its progress checked at least once per release.
* Each progress check of a review artifact MUST take place at the Members meeting.
* A review artifact MUST be either retired or continued at each progress check.
* A review artifact MUST NOT be retired when the passage of time is the only reason for retirement.
* A review artifact MUST NOT be retired unless the Maintainers and the working group agree on one of the following:
  * The tracking issue's questions are answered.
  * The content should move toward a release while a question is still open.
  * The content should be closed.
  * A new review artifact for the content is shared.
  * The review artifact is no longer useful.
* A retired review artifact MUST NOT be shared.

## Tracking Issue

The Maintainers record each progress check decision on the tracking issue, including the retirement.

A review artifact MUST adhere to the following requirements:

* The tracking issue of a review artifact MUST list the following, as approved at the Members meeting:
  * The questions the review needs to answer.
  * The pull requests that hold the content under review.
  * The sections under review.
* The tracking issue of a review artifact MUST record the following for the build:
  * The Git tag.
  * The commit that the review artifact is built from.
* A review artifact MUST be attached to its tracking issue, including after it is retired.
* The tracking issue of a review artifact SHOULD summarize the feedback on it.
* The tracking issue of a review artifact MUST record the following:
  * The decision from each progress check.
  * The date of the next progress check, unless the review artifact is retired.
* When a review artifact is retired, its tracking issue MUST record the retirement and its reason in the following places:
  * A comment.
  * A note at the top of the description.
