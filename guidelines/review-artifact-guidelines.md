# FOCUS Review Artifact Guidelines

## Overview

A review artifact is a PDF of content that is not part of a FOCUS release. It is built from a branch of the FOCUS Specification and shared when a release comes out, so people can give feedback on it. It is not a version of the FOCUS Specification. It has no requirements model, and it is not for implementation.

Data generators are asked what it would take to generate the data it describes. Practitioners are asked what it would take to use that data. Their answers help settle the open questions that keep the content out of a release.

A review artifact is a snapshot. It is built once, from the source branch as it stood at a single point in time, and it is not revised.

## Releasing a Review Artifact

* FOCUS Members approve releasing a review artifact. The approval follows the same steps as a pull request: two presentation cycles at the Members meeting, as the [Development Processes](contributors/development-processes.md#pull-request-approval-and-conflict-resolution) describe.
* The approval covers the source branch as it stands when approved, plus `working_draft` changes merged into it. It also covers the questions on the tracking issue.
* From the approval until the tag is in place, the source branch takes in only `working_draft` changes.
* Every review artifact has a tracking issue that lists the questions the review needs to answer.
* A review artifact is built from its source branch as it stood at a single point in time, marked by one commit.
* That commit holds only the approved source branch content and `working_draft` changes merged into it.
* Before that commit is chosen, the source branch should take in the release's consistency review changes from `working_draft`.
* The Admins put a Git tag on that commit that names the review artifact. The tracking issue records the tag and the commit.
* A review artifact completes an Intellectual Property Rights (IPR) review. That review runs in the same period as the IPR review of the release it goes out with.
* The source branch is not merged into the release that the review artifact goes out with.
* Only the PDF is released as the review artifact. The build also makes HTML and requirements model files. Those files are not part of the review artifact and are not shared for review.

## Labeling a Review Artifact

* The Admins build the PDF from the tagged commit. They add the label below when they build it. The label is not committed to the source branch.
* Every page shows a "Review Artifact" watermark.
* The version line names the content under review and says that the document has no version number (e.g., "SKU Price Dataset Review Artifact (Unversioned)").
* The first page replaces the working draft status text. It says that the document is not a FOCUS release and is not for implementation, names the sections under review, and links to the tracking issue.

## Distributing a Review Artifact

* After the IPR review completes, the Admins attach the PDF to the tracking issue.
* A review artifact is not published on the FOCUS or FinOps Foundation websites.
* A review artifact is not announced as part of a release.
* Anything that announces or shares a review artifact says that its content and sample data are out for review.
* FinOps Foundation staff should collect feedback in community calls, in talks with practitioners, and by reaching out to data generators. Staff then sum up that feedback on the tracking issue.

## Developing Content Under Review

* After the tag is in place, work on the content under review can continue on the source branch. The source branch should take in changes merged into `working_draft`. The tag keeps the reviewed commit intact.
* Until the review artifact is retired, changes to the content should not be proposed for a release.
* Feedback on changes made after the snapshot goes through the normal development process. A review artifact is not reissued to cover them.

## Retiring a Review Artifact

* The Maintainers and the working group review the progress of each review artifact at least once per release. Each review ends with either retirement or a decision to continue, and the tracking issue records that decision and the date of the next review.
* A review artifact has no time limit. Time passing is not, by itself, a reason to retire it.
* A review artifact is retired when the Maintainers and the working group agree on one of the following:
  * The tracking issue's questions are answered.
  * The content should move toward a release while a question is still open.
  * The content should be closed.
  * The review artifact is no longer useful.
* The Maintainers record the retirement and its reason in a comment on the tracking issue. They also add the same record as a note at the top of the tracking issue's description.
* Once a review artifact is retired, the project stops sharing it. The PDF stays attached to the tracking issue as a record of what was reviewed.
* After retirement, the content under review is either closed or moves toward a future release. When it moves forward, it goes through the normal development process. A future release can include it only through a pull request that FOCUS Members approve.
