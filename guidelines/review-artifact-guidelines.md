# FOCUS Review Artifact Guidelines

## Overview

A review artifact is a PDF of content that is not part of a FOCUS release. It is shared when a release comes out, so people can give feedback on the content. It is not a version of the FOCUS Specification, and it is not for implementation. It has no requirements model, the machine-readable form of the specification's rules.

Data generators, the organizations that produce FOCUS data, are asked what it would take to generate the data it describes. Practitioners, the people who use FOCUS data, are asked what it would take to use that data. Their answers help settle the open questions that keep the content out of a release.

A review artifact is a snapshot. It is built once from the pull request that holds its content, as that content stood at a single point in time. Each review artifact has a tracking issue, the GitHub issue that lists its open questions and records each decision about it.

### Roles

* **Working group:** the FOCUS Working Group, the contributors who develop the specification. Everyone in the working group is encouraged to attend the weekly Members meeting, where pull requests are approved.
* **Maintainers:** working group contributors who lead the project, listed in [MAINTAINERS.md](../MAINTAINERS.md).
* **Admins:** the GitHub group that merges pull requests.
* **FinOps Foundation staff:** the FinOps Foundation team that supports FOCUS.

### Lifecycle

| Stage | Who | What happens | On the tracking issue |
| --- | --- | --- | --- |
| 1. Approve | Working group, at the Members meeting | Approve the content and its open questions | The questions, as approved |
| 2. Build | Pull request author, Admins | Freeze the pull request, tag one commit, and build a labeled PDF from it | The Git tag and the commit |
| 3. Share and review | Admins, FinOps Foundation staff | Attach the PDF after the Intellectual Property Rights (IPR) review, then collect feedback while work on the content continues | The PDF and a summary of the feedback |
| 4. Retire | Maintainers and the working group | Check progress at least once per release, and retire the review artifact when they agree it is done | Each decision, the date of the next check, and the retirement and its reason |

The sections below set the requirements for each stage. The [Steps for Each Review Artifact](#steps-for-each-review-artifact) at the end say how to carry out the Build and Share stages.

## Stage 1: Approve

A review artifact is approved at the Members meeting, the same way as a pull request. That means two presentation cycles, as the [Development Processes](contributors/development-processes.md#pull-request-approval-and-conflict-resolution) describe. The approval covers the content in the pull request and the questions on the tracking issue. Approving a review artifact does not merge the pull request.

A review artifact MUST adhere to the following requirements:

* A review artifact MUST be approved at the Members meeting before it is built.
* A review artifact MUST have a tracking issue.
* The tracking issue of a review artifact MUST list the questions the review needs to answer, as approved at the Members meeting.

## Stage 2: Build

The pull request takes in changes from `working_draft`, the branch where the next FOCUS release is written. One of those changes is the release's consistency review, the last set of edits made across a release before it ships. The label is text added during the build that marks the PDF as a review artifact. A normal build starts with a version line and a statement that calls the document a working draft, and the label changes both.

A review artifact MUST adhere to the following requirements:

* A review artifact MUST be built from its pull request as it stood at a single point in time, marked by one commit.
* The commit a review artifact is built from MUST hold only the approved content and changes merged from `working_draft`.
* The commit a review artifact is built from SHOULD include the release's consistency review changes.
* A review artifact MUST consist of the PDF only.
* A review artifact MUST NOT be revised after it is built.
* Every page of a review artifact MUST show a "Review Artifact" watermark.
* The version line of a review artifact MUST include the following:
  * The name of the content under review (e.g., "SKU Price Dataset Review Artifact").
  * A statement that the document has no version number (e.g., "(Unversioned)").
* The first page of a review artifact MUST NOT call the document a working draft.
* The first page of a review artifact MUST include the following:
  * A statement that the document is not a FOCUS release.
  * A statement that the document is not for implementation.
  * The names of the sections under review.
  * A link to the tracking issue.
* The review artifact label MUST NOT be committed to the pull request.
* The tracking issue of a review artifact MUST record the Git tag and the commit that the review artifact is built from.

## Stage 3: Share and Review

Sharing starts after the IPR review, the patent review period that every FOCUS release also goes through. FinOps Foundation staff then collect feedback in community calls, in talks with practitioners, and by reaching out to data generators. Work on the content continues during the review. Feedback on those later changes goes through the normal development process, not through the review artifact.

A review artifact MUST adhere to the following requirements:

* A review artifact MUST complete an IPR review before it is shared.
* A review artifact's IPR review MUST run in the same period as the IPR review of the release it goes out with.
* A review artifact MUST be attached to its tracking issue.
* The HTML and requirements model files from a review artifact build MUST NOT be shared.
* A review artifact MUST NOT be published on the FOCUS or FinOps Foundation websites.
* A review artifact MUST NOT be announced as part of a release.
* Any announcement or message that shares a review artifact MUST state that its content, including any sample data, is out for review.
* The content under review MUST NOT be part of the release that the review artifact goes out with.
* The content under review SHOULD NOT be proposed for a release until the review artifact is retired.
* The tracking issue of a review artifact SHOULD summarize the feedback on it.

## Stage 4: Retire

A review artifact has no time limit, since content can need more than one release to mature.

A review artifact MUST adhere to the following requirements:

* A review artifact MUST have its progress checked by the Maintainers and the working group at least once per release.
* A review artifact MUST be either retired or continued at each progress check.
* A review artifact MUST NOT be retired only because time has passed.
* A review artifact MUST NOT be retired unless the Maintainers and the working group agree on one of the following:
  * The tracking issue's questions are answered.
  * The content should move toward a release while a question is still open.
  * The content should be closed.
  * The review artifact is no longer useful.
* A retired review artifact MUST NOT be shared.
* A retired review artifact MUST stay attached to its tracking issue as a record of what was reviewed.
* The tracking issue of a review artifact MUST record the following:
  * The decision from each progress check.
  * The date of the next progress check.
* When a review artifact is retired, its tracking issue MUST record the retirement and its reason in the following places:
  * A comment.
  * A note at the top of the description.

After retirement, the content is either closed or moves toward a future release. A future release can include it only through a pull request approved at the Members meeting, like any other content.

## Steps for Each Review Artifact

1. **Freeze the pull request** (pull request author). From the approval at the Members meeting until the tag in step 2, merge only `working_draft` changes into it. Before the tag, merge the release's consistency review changes when they are in `working_draft`.
2. **Tag the commit** (Admins). Add a Git tag that names the review artifact to the latest commit in the pull request. Record the tag and the commit on the tracking issue. The tag keeps the reviewed commit intact, so work on the content can continue as usual.
3. **Build the PDF** (Admins). Build the PDF from the tagged commit, and add the label during the build.
4. **Attach the PDF** (Admins). After the IPR review completes, attach the PDF to the tracking issue.
