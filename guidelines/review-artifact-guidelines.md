# FOCUS Review Artifact Guidelines

## Overview

A review artifact is a PDF of content that is not part of a FOCUS release. It is shared when a release comes out, so people can give feedback on the content. It is not a version of the FOCUS Specification, and it is not for implementation: it is not for production use or for conformance claims. It has no requirements model, the machine-readable form of the specification's rules.

Data generators, the organizations that produce FOCUS data, are asked what it would take to generate the data it describes. Practitioners, the people who use FOCUS data, are asked what it would take to use that data. Trying the content out, such as generating or using sample data, is welcome. Their answers and findings help settle the open questions that keep the content out of a release.

A review artifact is a snapshot. It is built once from the pull request that holds its content, as that content stood at a single point in time. The Markdown files it is built from stay in GitHub, where anyone can read them. Each review artifact has a tracking issue, the GitHub issue that lists its open questions and records each decision about it.

### Roles

* **Working group:** the FOCUS Working Group, the contributors who develop the specification. Everyone in the working group is encouraged to attend the weekly Members meeting, where pull requests are approved.
* **Maintainers:** working group contributors who lead the project, listed in [MAINTAINERS.md](../MAINTAINERS.md).
* **Admins:** the GitHub group that merges pull requests.
* **FinOps Foundation staff:** the FinOps Foundation team that supports FOCUS.

### Lifecycle

| Stage | Who | What happens | On the tracking issue |
| --- | --- | --- | --- |
| 1. Approve | Working group, at the Members meeting | Approve the content and its open questions | The questions, as approved, and the pull requests that hold the content |
| 2. Build | Pull request authors, Admins | Freeze the pull requests, combine them into one, tag one commit, and build a labeled PDF from it | The Git tag, the commit, and the `working_draft` commit the build option came from |
| 3. Share and review | Admins, FinOps Foundation staff | Send the PDF to an Intellectual Property Rights (IPR) review, attach it when the review completes, then collect feedback while work on the content continues | The PDF and a summary of the feedback |
| 4. Retire | Maintainers and the working group, at the Members meeting | Check progress at least once per release, and retire the review artifact when they agree it is done | Each decision, the date of the next check, and the retirement and its reason |

The sections below set the requirements for each stage. The [Steps for Each Review Artifact](#steps-for-each-review-artifact) at the end say how to carry out the Build and Share stages.

## Stage 1: Approve

A review artifact is approved at the Members meeting, the same way as a pull request. That means two presentation cycles, as the [Development Processes](contributors/development-processes.md#pull-request-approval-and-conflict-resolution) describe. The approval covers the content under review and the questions on the tracking issue. Approving a review artifact does not merge any of its pull requests.

Supported features are the parts of the specification that show how FOCUS data meets common FinOps needs. The content under review includes its supported features. The tracking issue lists the pull requests that hold the content. When there is more than one, the review artifact is built from the first one listed. The others are merged into it before the tag.

A review artifact MUST adhere to the following requirements:

* A review artifact MUST be approved at the Members meeting before it is built.
* When the content under review has supported features, a review artifact MUST include them.
* The tracking issue of a review artifact MUST list the pull requests that hold the content under review.
* A review artifact MUST have a tracking issue.
* The tracking issue of a review artifact MUST list the questions the review needs to answer, as approved at the Members meeting.

## Stage 2: Build

The pull request takes in changes from `working_draft`, the branch where the next FOCUS release is written. Each review artifact goes out with one FOCUS release. Its IPR review, a patent review period, runs in the same period as that release's IPR review. Near the end of a release, `working_draft` goes through a Final Consistency Review, the last planned round of edits across the release. The release's IPR review then starts from one `working_draft` commit. Before the tag, the pull request takes in `working_draft` up to that commit.

Sometimes a merge before the tag needs a change to the approved content (e.g., to resolve a merge conflict or a lint error). When it does, the review artifact goes back to the Members meeting for approval, the same way as in Stage 1. When that approval comes too late for the release's IPR review, the freeze ends. The review artifact then goes out with a later release, after it is approved again.

The label is the text the build adds to mark the PDF as a review artifact: the watermark, the version line, and the first-page statements. A normal build starts with a version line and a statement that calls the document a working draft, and the label changes both. A review artifact build option adds the label. The Admins take that option from `working_draft` at build time, so the tagged commit does not need to have it. The label values (the content name, the sections under review, and the tracking issue link) are given to the build, so they are not committed anywhere.

A review artifact MUST adhere to the following requirements:

* A review artifact MUST be built from its pull request as it stood at a single point in time, marked by one commit.
* The commit a review artifact is built from MUST hold all of the content under review.
* The commit a review artifact is built from MUST include the `working_draft` commit that the release's IPR review starts from.
* The commit a review artifact is built from MUST NOT include changes unless they are part of the approved content under review or the `working_draft` commit that the release's IPR review starts from.
* When a merge before the tag needs a change to the approved content, a review artifact MUST be approved again before it is built.
* A review artifact MUST be a PDF.
* A review artifact MUST NOT be revised after it is built.
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
* The label values of a review artifact MUST NOT be committed to the pull request.
* The tracking issue of a review artifact MUST record the following for the build:
  * The Git tag.
  * The commit that the review artifact is built from.
  * The `working_draft` commit that the build option came from.

## Stage 3: Share and Review

The PDF's IPR review runs in the same period as the release's, and sharing starts after it completes. FinOps Foundation staff then collect feedback in community calls, in talks with practitioners, and by reaching out to data generators. Work on the content continues during the review. Feedback on those later changes goes through the normal development process, not through the review artifact.

A review artifact MUST adhere to the following requirements:

* A review artifact MUST complete an IPR review before it is shared.
* A review artifact's IPR review MUST run in the same period as the IPR review of the release it goes out with.
* A review artifact MUST be attached to its tracking issue.
* A file that a review artifact build produces MUST NOT be shared unless it is the PDF (e.g., `spec.html`, `spec.md`, and the requirements model file).
* A review artifact MUST NOT be published on the FOCUS website.
* A review artifact MUST NOT be published on the FinOps Foundation website.
* A review artifact MUST NOT be announced as part of a release.
* Any announcement or message that shares a review artifact MUST state that its content, including any sample data, is out for review.
* The content under review MUST NOT be part of the release that the review artifact goes out with.
* The content under review SHOULD NOT be proposed for a release until the review artifact is retired.
* The tracking issue of a review artifact SHOULD summarize the feedback on it.

## Stage 4: Retire

A review artifact has no time limit, since content can need more than one release to mature. The Maintainers record each progress check decision on the tracking issue, including the retirement.

A progress check can also decide to build a new review artifact from the updated content. The new review artifact goes through every stage again, starting with approval. The earlier one is retired when the new one is shared.

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
* A retired review artifact MUST stay attached to its tracking issue as a record of what was reviewed.
* The tracking issue of a review artifact MUST record the following:
  * The decision from each progress check.
  * The date of the next progress check.
* When a review artifact is retired, its tracking issue MUST record the retirement and its reason in the following places:
  * A comment.
  * A note at the top of the description.

After retirement, the content is closed, continues under a new review artifact, or moves toward a future release. A future release can include it only through a pull request approved at the Members meeting, like any other content.

## Steps for Each Review Artifact

1. **Freeze the pull requests** (pull request authors). From the approval at the Members meeting until the tag in step 2, change the pull requests listed on the tracking issue only by merging `working_draft` into them or merging them together. Before the tag, if more than one pull request is listed, merge the other listed pull requests into the first one. Then merge `working_draft` into the first pull request, up to the commit that the release's IPR review starts from. When a merge needs a change to the approved content, take the review artifact back to the Members meeting before the tag.
2. **Tag the commit** (Admins). Add a Git tag that names the review artifact to the latest commit in the pull request. Record the tag and the commit on the tracking issue. The tag keeps the reviewed commit intact, so work on the content can continue as usual.
3. **Build the PDF** (Admins). Check out the tagged commit, add only the build option's files from `working_draft` to that checkout, and build the PDF with the label. Record the `working_draft` commit the build option came from on the tracking issue.
4. **Send the PDF to IPR review** (Admins). Start the PDF's IPR review in the same period as the release's IPR review.
5. **Attach the PDF** (Admins). After the IPR review completes, attach the PDF to the tracking issue.
