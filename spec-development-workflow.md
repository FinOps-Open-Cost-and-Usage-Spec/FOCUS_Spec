# FOCUS specification formatting + submission process


## Finalizing content in the google doc

Start with the google doc worksheet that has been created based on discussions in the working sessions. Once the working session(s) related to the task complete, the content may require cleanup and/or enhancement to capture the discussions and decisions that were made during the working sessions. 

Follow the following steps:

1. Take a first stab at finalizing content
   * Make sure naming / descriptions are clear and agreed upon within the working group
   * Make sure example mappings and scenarios are populated
   * Make sure formatting and writing is consistent with previous tasks
2. Reach out to the squad working on the task for final edits/comments. Incorporate any changes based on comments
3. If naming changes, update document name, github issue and related fields, agenda and other places where the task may be referenced.

### Converting spec content to Markdown

The content in the worksheets will be broken into two documents in the FOCUS_Spec repository. First section is the 'Spec content' and will go into the specification folder within the folder. The second section will go under the supporting_content folder.

Tools to use for converting to markdown:
- [Clipboard-To-Markdown](https://euangoddard.github.io/clipboard2markdown/) is useful for converting content other than the tables within your content.
- [Tables Generator](https://www.tablesgenerator.com/markdown_tables#) is useful for converting tables in your content.

As you convert, be aware of the following conversion errors:
- Content that has special characters e.g. phrase '<not specified>' or placeholders in content like '//container.googleapis.com/projects/<project_id>/locations/\<location>/clusters/\<cluster>' may not convert correctly without escaping. Find these inconsistencies after conversion and escape the special characters when necessary. 
- Multi-line content within table cells also don't convert correctly. You'll have to put `<br>` tags to ensure the multi-line content renders correctly in markdown.
- Ensure HTML or anchor links are set up correctly after the conversion

Markdown linter will catch some issues that might happen during conversion. Common issues are:

- New lines may not get added at the end of documents (and at times before and after headings). These are needed for the linter to pass
- Trailing spaces in your content will fail the build.

VSCode and other IDEs may highlight these. If not, it's a good idea to run the build process locally before you push the changes to git. 

### Local make process

Steps for setting up and building locally are listed here: <https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec#focus-specification-development-environment> 

Git workflow
------------

This is one way to the git workflow. You may have other preferred approaches. Unless specified below as being required, each contributor has the chance to follow their own process.

1.  Go to the github issue you're working on and assign it to yourself under the Assignees section
2.  Create a topic branch by clicking on the 'Create a branch' link under the Development section
3. Name your branch - by default, it's selecting the issue title. It doesn’t need to be as long as the title (e.g. 10-create-a-service-name-dimension -> 10-service-name-dimension)
4. Checkout to your preferred workspace and make the edits.
5. Build the specification locally to ensure there are no issues highlighted by the linter
6. When ready to commit, please include your issue number in the branch name and commit message (commit message may need to be prefixed with FOCUS so the issue number e.g. #10 doesn’t look like a comment)
7. Create a new pull request from your changes. Set the correct values on the right side of the PR to ensure its correctly accounted for:
8. If you have many smaller commits, squash your changes prior to merge and rebase in order to avoid messy git logs (and to simplify selecting a single task for rollback or cherry-pick)
