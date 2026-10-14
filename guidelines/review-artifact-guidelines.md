# FOCUS Review Artifact Guidelines

## Overview

A review artifact is a PDF of content that is not part of a FOCUS release. It is shared when a release comes out, so people can give feedback on the content. It is not a version of the FOCUS Specification, and it is not for implementation. It has no requirements model, the machine-readable form of the specification's rules.

Data generators, the organizations that produce FOCUS data, are asked what it would take to generate the data it describes. Practitioners, the people who use FOCUS data, are asked what it would take to use that data. Their answers help settle the open questions that keep the content out of a release.

A review artifact is a snapshot of its source branch, the GitHub branch that holds the content under review. It is built once, from that branch as it stood at a single point in time.

Each review artifact has a tracking issue, the GitHub issue that lists the questions the review needs to answer. The tracking issue also records each decision about the review artifact.

A review artifact goes through four stages:

1. **Approve and build:** FOCUS Members approve the content and its questions. Then the Admins, the GitHub group that merges pull requests, build and label the PDF.
2. **Share:** The PDF is shared after an Intellectual Property Rights (IPR) review. This is the patent review period that every FOCUS release also goes through.
3. **Review and develop:** People give feedback while work on the content continues.
4. **Retire:** The Maintainers and the working group agree that the review is done. The Maintainers are the project leads listed in [MAINTAINERS.md](../MAINTAINERS.md).

The sections below set the requirements for each stage. The Git and build steps are in the [Admin Checklist](#admin-checklist).

## Approving and Building a Review Artifact

FOCUS Members approve a review artifact the same way they approve a pull request. That means two presentation cycles at the Members meeting, as the [Development Processes](contributors/development-processes.md#pull-request-approval-and-conflict-resolution) describe. The approval covers the content on the source branch and the questions on the tracking issue.

The source branch takes in changes from `working_draft`, the branch where the next FOCUS release is written. One of those changes is the release's consistency review, the last set of edits made across a release before it ships.

A review artifact MUST adhere to the following requirements:

* A review artifact MUST be approved by FOCUS Members before it is built.
* A review artifact MUST have a tracking issue.
* A review artifact MUST be built from its source branch as it stood at a single point in time, marked by one commit.
* The commit a review artifact is built from MUST hold only the content Members approved and changes merged from `working_draft`.
* The commit a review artifact is built from SHOULD include the release's consistency review changes.
* A review artifact MUST consist of the PDF only.
* The HTML and requirements model files from a review artifact build MUST NOT be shared.
* A review artifact MUST NOT be revised after it is built.

## Labeling a Review Artifact

The label marks the PDF as a review artifact. The Admins add it when they build the PDF. A normal build starts with a version line and a statement that calls the document a working draft. The label changes both.

A review artifact MUST adhere to the following requirements:

* Every page of a review artifact MUST show a "Review Artifact" watermark.
* The version line of a review artifact MUST name the content under review.
* The version line of a review artifact MUST state that the document has no version number (e.g., "SKU Price Dataset Review Artifact (Unversioned)").
* The first page of a review artifact MUST NOT call the document a working draft.
* The first page of a review artifact MUST state that the document is not a FOCUS release and is not for implementation.
* The first page of a review artifact MUST name the sections under review.
* The first page of a review artifact MUST link to its tracking issue.
* A review artifact label MUST NOT be committed to the source branch.

## Sharing a Review Artifact

FinOps Foundation staff collect feedback on a review artifact in community calls, in talks with practitioners, and by reaching out to data generators.

A review artifact MUST adhere to the following requirements:

* A review artifact MUST complete an IPR review before it is shared.
* A review artifact's IPR review MUST run in the same period as the IPR review of the release it goes out with.
* The content of a review artifact MUST NOT be part of the release it goes out with.
* A review artifact MUST be attached to its tracking issue.
* A review artifact MUST NOT be published on the FOCUS or FinOps Foundation websites.
* A review artifact MUST NOT be announced as part of a release.
* Any announcement or message that shares a review artifact MUST state that its content and sample data are out for review.

## Developing Content Under Review

Work on the content can continue while the review artifact is out for review. Changes made after the snapshot get feedback through the normal development process, not through the review artifact.

Content under review MUST adhere to the following requirements:

* Content under review MUST NOT change on its source branch from Member approval until the review artifact's commit is tagged, except when the change is merged from `working_draft`.
* Content under review MAY change on its source branch after the review artifact's commit is tagged.
* The source branch SHOULD take in changes merged into `working_draft` while the review artifact is out for review.
* Content under review SHOULD NOT be proposed for a release until its review artifact is retired.

## Retiring a Review Artifact

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

After retirement, the content is either closed or moves toward a future release. A future release can include it only through a pull request that FOCUS Members approve, like any other content.

## Tracking Issue

A review artifact tracking issue MUST adhere to the following requirements:

* The tracking issue MUST list the questions the review needs to answer, as FOCUS Members approved them.
* The tracking issue MUST record the Git tag and the commit that the review artifact is built from.
* The tracking issue SHOULD summarize the feedback on the review artifact.
* The tracking issue MUST record the decision from each progress check.
* The tracking issue MUST record the date of the next progress check.
* The tracking issue MUST record the retirement and its reason in a comment.
* The tracking issue description MUST start with a note that records the retirement and its reason when the review artifact is retired.

## Admin Checklist

The Admins follow these steps for each review artifact after FOCUS Members approve it:

1. **Hold the source branch.** Until the tag in step 3 is in place, the source branch takes in only `working_draft` changes.
2. **Take in the consistency review.** Merge the release's consistency review changes from `working_draft` into the source branch.
3. **Tag the commit.** Add a Git tag that names the review artifact to the latest commit on the source branch. Record the tag and the commit on the tracking issue. Work on the content can resume on the source branch after this step. The tag keeps the reviewed commit intact.
4. **Build the PDF.** Build the PDF from the tagged commit, and add the label during the build. Do not commit the label to the source branch.
5. **Attach the PDF.** After the IPR review completes, attach the PDF to the tracking issue. Do not attach the HTML or requirements model files from the build.
