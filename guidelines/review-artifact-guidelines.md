# FOCUS Review Artifact Guidelines

## Overview

A review artifact is a PDF built from a branch of the FOCUS Specification and released alongside a FOCUS release to collect feedback on content that is not part of that release. It is not a version of the FOCUS Specification, it has no requirements model, and it is not for implementation. Data generators are asked what it would take to generate the data it describes, and practitioners are asked what it would take to use that data. Their answers address the open questions that hold the content back from a release.

A review artifact is a snapshot. It is built once, from one commit, and it is not revised.

## Releasing a Review Artifact

* FOCUS Members MUST approve releasing a review artifact through the same two presentation cycles at the Members meeting that a pull request follows under the [Development Processes](contributors/development-processes.md#pull-request-approval-and-conflict-resolution). The approval covers the source branch as it stands when approved, plus `working_draft` changes merged into it, and the tracking issue's questions.
* A review artifact MUST have a tracking issue that lists the open questions the review is meant to answer.
* A review artifact MUST be built from a single commit of its source branch.
* That commit MUST contain only the approved source branch content and `working_draft` changes merged into it.
* That commit MUST be preserved with a Git tag that names the review artifact, created by the Admins, and the tracking issue MUST record the tag and the commit.
* The source branch SHOULD include the consistency review changes made to `working_draft` for the accompanying release before that commit is chosen.
* A review artifact MUST complete an Intellectual Property Rights (IPR) review that runs in the same period as the IPR review of the release it accompanies.
* The source branch MUST NOT be merged into the release that the review artifact accompanies.
* Only the PDF is released as the review artifact. The HTML and requirements model output that the build also produces are not part of it and MUST NOT be shared as review material.

## Labeling a Review Artifact

* Every page MUST carry a "Review Artifact" watermark.
* The version line MUST name the content under review and state that the document is unversioned (e.g., "SKU Price Dataset Review Artifact (Unversioned)").
* The first page MUST state that the document is not a FOCUS release and is not for implementation, and MUST link to the tracking issue.

## Distributing a Review Artifact

* The PDF MUST be attached to the tracking issue.
* A review artifact MUST NOT be published on the FOCUS or FinOps Foundation websites.
* A review artifact MUST NOT be announced as part of a release.
* Communication about a review artifact MUST describe it as out for review of its content and its sample data.
* FinOps Foundation staff SHOULD collect feedback through community calls, conversations with practitioners, and outreach to data generators, and summarize that feedback on the tracking issue.

## Developing Content Under Review

* Development of the content under review MAY continue on the source branch, and the source branch SHOULD take in changes merged into `working_draft`. The tag keeps the reviewed commit intact.
* Changes to the content under review SHOULD NOT be proposed for a release until the review artifact is retired.
* Feedback on changes made after the snapshot goes through the normal development process. A review artifact is not reissued to cover them.

## Retiring a Review Artifact

* A review artifact is retired when one of the following happens:
  * The Maintainers and the working group agree that the tracking issue's questions are answered.
  * The Maintainers and the working group agree to move the content toward a release with a question still open.
  * The Maintainers and the working group agree to close the content, or agree that the review artifact no longer serves its purpose.
* The Maintainers MUST record the retirement and its reason in a comment on the tracking issue and in a note at the top of its description.
* Once a review artifact is retired, the project MUST stop sharing it. The PDF stays attached to the tracking issue as a record of what was reviewed.
* After retirement, the content under review either continues through the normal development process toward a future release or is closed. A future release includes it only through a pull request that FOCUS Members approve.
