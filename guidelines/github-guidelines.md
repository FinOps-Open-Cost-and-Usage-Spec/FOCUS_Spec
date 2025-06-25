# GitHub Guidelines

Guidelines, recommendations, and instructions for how to work with FOCUS on GitHub.

## Table of Contents

1. [FOCUS Repository Structure Overview](#focus-repository-structure-overview)
2. [Logging into GitHub](#logging-into-github)
3. [Configuring Notifications](#configuring-notifications)
4. [Installing GitHub Desktop](#installing-github-desktop)
5. [Installing Visual Studio Code](#installing-visual-studio-code)
6. [How to Submit an Issue](#how-to-submit-an-issue)
7. [How to Interact (review, comment, participate in, etc.) with an Issue](#how-to-interact-review-comment-participate-in-etc-with-an-issue)
8. [Cloning a Repository with GitHub Desktop](#cloning-a-repository-with-github-desktop)
9. [How to submit a Pull Request (PR) using GitHub Desktop and VSCode](#how-to-submit-a-pull-request-pr-using-github-desktop-and-vscode)
10. [How to submit changes to an an existing PR using GitHub desktop and vscode](#how-to-submit-changes-to-an-an-existing-pr-using-github-desktop-and-vscode)
11. [Data Exercise to learn FOCUS columns](#data-exercise-to-learn-focus-columns)
12. [Tips for Success](#tips-for-success)

---

## FOCUS Repository Structure Overview

## General Overview of FOCUS_Spec Repository

The FOCUS_Spec repository contains the FinOps Open Cost and Usage Specification (FOCUS), which is a community-driven effort to develop a standard schema for cloud, SaaS, and other billing data. The primary goal of the FOCUS specification is to make it easier to understand, report on, and manage cloud costs.

## Repository Purpose

FOCUS is designed to address the complexity that FinOps practitioners face when dealing with disparate billing data formats from different cloud providers. Without a standard, each provider generates unique billing data files with their own terminology, forcing practitioners to develop custom normalization schemes for each provider.

## Main Folders and Their Contents

### 1. `specification/` folder

The core folder containing the specification documentation:

- **`overview.md`** - Contains the main specification overview, principles, and requirements
- **`glossary.md`** - Comprehensive glossary of terms and definitions used throughout the specification
- **`columns/` subfolder** - Contains detailed documentation for individual FOCUS columns like `servicesubcategory.md`

### 2. `supporting_content` folder

The repository provides supporting content that includes example mappings between well-known provider datasets and what's defined in the FOCUS specification. This likely includes mappings for major cloud providers like:

- AWS (Amazon Web Services)
- GCP (Google Cloud Platform)
- Azure (Microsoft)
- Oracle Cloud

### 3. `guidelines` folder

This folder contains various guidelines on development, editorial, normative requirements, spec change, and spec design.

### 4. Documentation Structure

The repository follows standard documentation patterns with:

- **`README.md`** - Main repository documentation
- **`CHANGELOG.md`** - Version changes and updates
- Various markdown files for specification details

## Key Content Areas

### Specification Details

- Column definitions (dimensions and metrics), column-specific requirements, and attributes (spec-wide requirements)
- Data dimensions, metrics, a set of attributes about billing data, and a common lexicon for describing billing data
- Requirements using standard terminology (MUST, SHOULD, MAY, etc.) following BCP 14 standards

### Provider Integration

- Support for major cloud providers including Microsoft Azure, Oracle Cloud, AWS, and Google Cloud Platform
- Example mappings showing how provider-specific billing data maps to FOCUS standard format
- Conversion guidelines and best practices

### Use Cases and Examples

- Library of FinOps capabilities that can be solved by FOCUS data
- Cost reporting use cases
- Chargeback scenarios enabled by net cost and amortized cost metrics

## Repository Organization Principles

The repository is organized around several key principles:

### FinOps Scenario-Driven Development

- Columns are defined to answer scenario questions rather than looking for scenarios to fit existing columns
- Each column must have a clear use case
- Work backward from essential FinOps capabilities to prioritize dimensions, metrics, and attributes

### Incremental Development

- Incremental iterations released regularly to provide higher value to practitioners
- Allow feedback as the specification develops
- Goal is not to create a complete, finished specification in one pass

### Provider Neutrality

- Contributors must ensure the specification examines how each decision relates to each of the major cloud providers
- Does not favor any single provider's implementation
- Prioritizes enabling FinOps capabilities and alignment with the FinOps Framework

## Specification Features

### Version Information

- Current focus on version 1.2 which introduces foundational support for Software as a Service (SaaS) platforms
- Includes normative columns for pricing currencies, effective cost, and contracted pricing in non-monetary units such as credits or tokens
- Versioned based on Semantic Versioning 2.0

### Extensibility

- Supports extensibility through structured naming conventions (e.g., x_ custom columns)
- Conditional requirements
- Version-aware schema approach

### Future Considerations

Future versions of FOCUS will consider including additional FinOps capabilities such as:

- Forecasting
- Exchange rate modeling
- Anomaly detection
- Support for broader range of billing and cost datasets including internal infrastructure platforms and marketplace offerings

## Target Audience

The specification is designed to be used by three major groups:

1. **Billing Data Generators** - Infrastructure and services providers that bill based on consumption
2. **FinOps Practitioners** - Professionals who analyze and manage cloud costs
3. **FinOps Tool Vendors** - Companies that provide tools and platforms for cloud cost management

## Repository Status

The repository is actively maintained and represents a collaborative effort between:

- FinOps practitioners
- Cloud and SaaS providers
- FinOps vendors
- The FinOps Foundation (supporting organization)
- Linux Foundation (hosting the specification project)

The repository appears to be well-structured for both specification development and practical implementation, supporting the goal of creating a vendor-neutral standard for cloud billing data that can be adopted across different cloud providers and FinOps tools.

---

## Logging into GitHub

### Creating a GitHub Account

If you don't have a GitHub account yet:

1. Go to [GitHub.com](https://GitHub.com)
2. Click the **Sign up** button in the top right corner
3. Enter your email address, create a password, and choose a username
4. Complete the verification process
5. Select your preferences and click **Create account**

### Logging In

1. Navigate to [GitHub.com](https://GitHub.com)
2. Click **Sign in** in the top right corner
3. Enter your username/email and password
4. If you have two-factor authentication enabled, enter your authentication code
5. Click **Sign in**

### Two-Factor Authentication (Recommended)

For enhanced security:

1. Go to **Settings** (click your profile picture → Settings)
2. Click **Password and authentication** in the left sidebar
3. Click **Enable two-factor authentication**
4. Choose your preferred method (authenticator app or SMS)
5. Follow the setup instructions

---

## Configuring Notifications

GitHub notifications help you stay updated on repository activity, issues, pull requests, and mentions.

### Accessing Notification Settings

1. Click your profile picture in the top right corner
2. Select **Settings** from the dropdown menu
3. Click **Notifications** in the left sidebar

### Email Notification Settings

Configure what you want to receive via email:

**Participating notifications:**

- Comments on issues and pull requests you're involved in
- Direct mentions of your username
- Check the box to receive these via email

**Watching notifications:**

- Activity on repositories you're watching
- Choose your preference: all activity, releases only, or ignore

**Custom routing:**

- Set up different email addresses for different organizations
- Useful for separating work and personal notifications

### Web and Mobile Notifications

- **Web notifications:** Enable browser notifications for real-time updates
- **Mobile notifications:** Install the GitHub mobile app and configure push notifications

### Repository-Specific Notifications

For individual repositories:

1. Go to the repository page
2. Click the **Watch** button (eye icon) near the top right
3. Choose your notification level:
   - **Not watching:** Only receive notifications when participating or mentioned
   - **Releases only:** Only get notified about new releases
   - **Watching:** Get notified about all conversations
   - **Ignoring:** Never get notifications

### Managing Notification Frequency

- **Automatically watch repositories:** Enable this to watch repositories you have push access to
- **Automatically watch teams:** Get notifications when you're added to a team
- **Dependency graph:** Get notifications about security vulnerabilities in your dependencies

---

## Installing GitHub Desktop

GitHub Desktop is a user-friendly application that makes it easy to work with Git and GitHub repositories without using the command line.

### Download and Installation GitHub Desktop

**For Windows:**

1. Go to [desktop.GitHub.com](https://desktop.GitHub.com)
2. Click **Download for Windows**
3. Run the downloaded installer
4. Follow the installation wizard

**For Mac:**

1. Go to [desktop.GitHub.com](https://desktop.GitHub.com)
2. Click **Download for macOS**
3. Open the downloaded .zip file
4. Drag GitHub Desktop to your Applications folder

### Initial Setup

1. Launch GitHub Desktop
2. Click **Sign in to GitHub.com**
3. Enter your GitHub credentials
4. Configure Git with your name and email address
5. Choose whether to submit usage statistics (optional)

---

## Installing Visual Studio Code

Visual Studio Code (VSCode) is a free, powerful code editor that integrates excellently with Git and GitHub. It's highly recommended for editing code and managing repositories.

### Download and Installation VSCode

**For Windows:**

1. Go to [code.visualstudio.com](https://code.visualstudio.com)
2. Click **Download for Windows**
3. Run the downloaded installer (`VSCodeUserSetup-{version}.exe`)
4. Follow the installation wizard:
   - Accept the license agreement
   - Choose installation location (default is usually fine)
   - Select additional tasks (recommended options):
     - ✅ Add "Open with Code" action to Windows Explorer file context menu
     - ✅ Add "Open with Code" action to Windows Explorer directory context menu
     - ✅ Register Code as an editor for supported file types
     - ✅ Add to PATH (important for command line usage)
5. Click **Install** and wait for completion
6. Launch VSCode when installation finishes

**For Mac:**

1. Go to [code.visualstudio.com](https://code.visualstudio.com)
2. Click **Download for Mac**
3. Open the downloaded `.zip` file
4. Drag **Visual Studio Code.app** to your **Applications** folder
5. Launch VSCode from Applications or Spotlight search

**For Linux (Ubuntu/Debian):**

1. Download the `.deb` package from [code.visualstudio.com](https://code.visualstudio.com)
2. Install via command line: `sudo dpkg -i code_*.deb`
3. Or use the repository method:
   ```bash
   wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
   sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
   echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" | sudo tee /etc/apt/sources.list.d/vscode.list
   sudo apt update
   sudo apt install code
   ```

### Initial Setup and Configuration

**First Launch:**

1. Open VSCode
2. You may see a welcome screen with helpful getting started information
3. VSCode will automatically detect your system settings and apply appropriate defaults

**Essential Extensions for GitHub Development:**

1. Click the **Extensions** icon in the sidebar (or press `Ctrl+Shift+X`)
2. Install these recommended extensions:
   - **GitHub Pull Requests and Issues** - Manage pull requests and issues directly from VSCode
   - **GitLens** - Supercharge Git capabilities with blame annotations, code lens, and more
   - **GitHub Copilot** (optional, requires subscription) - AI-powered code completion
   - **Bracket Pair Colorizer** - Makes matching brackets easier to identify

### Integrating VSCode with GitHub

**GitHub Authentication:**

1. Open VSCode
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) to open the command palette
3. Type "GitHub: Sign in" and select it
4. Choose "Allow" to open GitHub in your browser
5. Sign in to your GitHub account
6. Authorize VSCode to access your GitHub account
7. Return to VSCode - you should now be signed in

### Opening Repository Files in VSCode

**Method 1: From GitHub Desktop**

1. In GitHub Desktop, select your repository
2. Click **Repository** → **Open in Visual Studio Code**
3. Or click the **Open in Visual Studio Code** button in the toolbar

**Method 2: From File Explorer**

1. Navigate to your cloned repository folder
2. Right-click in the folder
3. Select **Open with Code** (if you enabled this during installation)

**Method 3: From VSCode**

1. Open VSCode
2. Click **File** → **Open Folder**
3. Navigate to and select your repository folder
4. Click **Select Folder**

**Method 4: From Command Line**

1. Open terminal/command prompt
2. Navigate to your repository folder: `cd path/to/your/repository`
3. Type: `code .` (the dot means "current directory")

### Using VSCode with Git and GitHub

**Source Control Panel:**

1. Click the **Source Control** icon in the sidebar (or press `Ctrl+Shift+G`)
2. This panel shows:
   - Changed files
   - Staged changes
   - Commit message box
   - Sync status with remote repository

**Making Commits:**

1. Make changes to your files
2. Changed files will appear in the Source Control panel
3. Click the **+** icon next to files to stage them
4. Enter a commit message in the text box
5. Click the **✓** (checkmark) button to commit
6. Click **Sync Changes** to push to GitHub

**Viewing Git History:**

1. Install the **GitLens** extension
2. You'll see Git blame information inline with your code
3. Click on any line to see commit details
4. Use the **GitLens** panel to explore repository history

**Managing Branches:**

1. Click the branch name in the bottom-left status bar
2. Select **Create new branch** or choose an existing branch
3. VSCode will switch to the selected branch
4. Make changes and commit as usual

### Working with GitHub Features in VSCode

**Pull Requests:**

1. With the **GitHub Pull Requests and Issues** extension installed
2. Click the **GitHub** icon in the sidebar
3. View and manage pull requests directly from VSCode
4. Review code, leave comments, and merge pull requests

**Issues:**

1. Access GitHub issues from the same GitHub panel
2. Create new issues or work on existing ones
3. Link commits to issues using keywords like "fixes #123"

**Code Reviews:**

1. Open a pull request in the GitHub panel
2. Review changes with inline comments
3. Suggest changes directly in the editor
4. Approve or request changes

### Useful VSCode Shortcuts for Git

- **Ctrl+Shift+G**: Open Source Cont# GitHub Tutorial: Getting Started Guide

---

## How to Submit an Issue

1. Go to https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues
2. Click `New Issue` (upper right)
3. Select the type of Issue that best describes your goal
  a. Action Item - This is a task within a Work Item issue
  b. FOCUS Feature Request - Propose a new attribute, refinement, or data structure for the FOCUS specification.
  c. General Feedback - Suggest minor corrections, clarity improvements, or inconsistencies in the FOCUS Specification.
  d. Maintenance Task - Create tasks related to work on the GitHub Repository or GitHub Actions.
  e. Work Item - Template for creating new Work Items (these are linked to a Feature Request)
  f. Blank issue - try not to use this, please
4. Fill out the details of the template, please be straight forward and thorough.
5. Click the `Create` button

---

## How to Interact (review, comment, participate in, etc.) with an Issue

## Reviewing and Commenting on GitHub Issues

GitHub Issues are a powerful way to track bugs, feature requests, tasks, and other project-related discussions. Learning how to effectively review and comment on issues is essential for contributing to open source projects and collaborating with teams.

### Understanding GitHub Issues

**What are Issues?**

- Issues are discussion threads related to specific topics in a repository
- They can be bug reports, feature requests, questions, or general discussions
- Each issue has a unique number and can be referenced across the repository
- Issues can be assigned to people, labeled, and organized into milestones

**Issue Components:**

- **Title:** Brief description of the issue
- **Description:** Detailed explanation with context, steps to reproduce, etc.
- **Labels:** Categories like "bug," "enhancement," "documentation"
- **Assignees:** People responsible for working on the issue
- **Milestone:** Project phase or version the issue belongs to
- **Comments:** Discussion thread where collaboration happens

### Finding and Accessing Issues

**Viewing Repository Issues:**

1. Navigate to any GitHub repository
2. Click the **Issues** tab near the top of the repository page
3. You'll see a list of open issues by default

**Filtering Issues:**

- **Open/Closed:** Toggle between open and closed issues
- **Labels:** Filter by specific labels (bug, enhancement, etc.)
- **Assignee:** Filter by who's assigned to work on issues
- **Milestone:** Filter by project milestone
- **Author:** Filter by who created the issue
- **Sort:** By newest, oldest, most commented, recently updated, etc.

**Search Issues:**

1. Use the search bar at the top of the issues list
2. Search by keywords, labels, or advanced queries
3. Example searches:
   - `is:open label:bug` - Open bug reports
   - `author:username` - Issues created by specific user
   - `assignee:username` - Issues assigned to specific user

### Reading and Analyzing Issues

**Before Commenting:**

1. **Read the entire issue** including the original description and all comments
2. **Check for duplicates** - search if similar issues already exist
3. **Review linked pull requests** - see if someone is already working on it
4. **Check issue status** - ensure it's still relevant and open
5. **Understand the context** - read related documentation or code if needed

**Key Information to Look For:**

- **Steps to reproduce** (for bugs)
- **Expected vs. actual behavior**
- **Environment details** (OS, browser, version numbers)
- **Screenshots or code examples**
- **Previous attempts at solutions**
- **Project maintainer responses**

### Writing Effective Comments

**Comment Structure:**

1. **Quote relevant parts** of previous comments if responding to specific points
2. **Provide context** for your comment
3. **Be specific and actionable**
4. **Use formatting** to make your comment readable


### Best Practices for Issue Comments

**Do:**

- **Be respectful and professional** in all interactions
- **Stay on topic** and relevant to the issue
- **Provide concrete examples** with code, screenshots, or logs
- **Update your comments** if you find additional information
- **Thank contributors** for their time and effort
- **Test suggestions** before recommending them
- **Link to relevant resources** like documentation or related issues

**Don't:**

- **Spam with "+1" comments** - use the thumbs up reaction instead
- **Ask "when will this be fixed?"** - maintainers work on volunteer time
- **Hijack issues** with unrelated problems - create a new issue instead
- **Be demanding or impatient** - open source is collaborative, not customer service
- **Post duplicate information** that's already been shared
- **Make assumptions** about others' skill levels or intentions

### Using Reactions and Interactions

**Emoji Reactions:**

- Use 👍 (thumbs up) to show support for an issue or comment
- Use 👎 (thumbs down) to disagree (but explain why in a comment)
- Use ❤️ (heart) to show appreciation
- Use 🎉 (celebration) when issues are resolved
- Use 👀 (eyes) to indicate you're watching/interested

**Other Interactions:**

- **Subscribe** to issues you want to follow
- **Reference issues** in commits and pull requests using #issue-number
- **Mention users** with @username to get their attention
- **Cross-reference** related issues and pull requests

### Following Up on Issues

**When to Follow Up:**

- If you've provided requested information
- If you've found a solution or workaround
- If the issue status has changed (bug confirmed, feature approved, etc.)
- If you've tested a proposed fix

**How to Follow Up:**

```markdown
**Update:** I've tested the proposed solution and can confirm it works.

**Testing Environment:**
- Applied the patch from PR #789
- Tested with sample data set
- No errors encountered

The fix resolves the original issue. Thanks for the quick response!
```

### Working with Issue Templates

**Understanding Templates:**

- Many repositories use issue templates to guide bug reports and feature requests
- Templates help ensure all necessary information is provided
- Follow the template structure when creating or commenting on issues

**Responding to Template Questions:**

- Answer all sections of the template
- Don't delete template sections - mark them as N/A if not applicable
- Provide requested information like version numbers, environment details, etc.

### Issue Etiquette for Different Project Types

**Open Source Projects:**

- Be extra patient and respectful - maintainers are often volunteers
- Read contributing guidelines before commenting
- Check if the project is actively maintained
- Consider sponsoring or contributing if you benefit from the project

**Work/Team Projects:**

- Follow your team's established workflows and conventions
- Use agreed-upon labels and assignment practices
- Be more direct in communication since you're working with colleagues
- Include relevant stakeholders in discussions

### Advanced Issue Management

**Creating Links Between Issues:**

```markdown
This issue is related to #123
This closes #456
Duplicate of #789
```

**Using Keywords for Automation:**

```markdown
// In commit messages or pull requests
fixes #123
closes #456
resolves #789
```

**Organizing with Projects:**

- Issues can be added to GitHub Projects for better organization
- Use project boards to track progress
- Move issues through different status columns

### Troubleshooting Common Issues

**Can't Comment on Issues:**

- Ensure you're signed in to GitHub
- Check if the repository allows comments from external contributors
- Verify the issue isn't locked or closed to new comments

**Comments Not Formatting Properly:**

- Preview your comment before posting using the "Preview" tab
- Check your Markdown syntax
- Use the formatting toolbar for basic formatting

**Not Receiving Notifications:**

- Check your notification settings in GitHub
- Ensure you're subscribed to the issue
- Verify your email notifications are working

---

## Cloning a Repository with GitHub Desktop

Cloning creates a local copy of a repository on your computer, allowing you to work on it offline and then sync changes in the future.

### Method 1: Clone from GitHub.com

1. Go to the repository you want to clone on GitHub.com (`https://GitHub.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec`)
2. Click the **Code** button (toward the upper right part of the screen)
3. Select **Open with GitHub Desktop**
4. GitHub Desktop will open automatically
5. Choose where to save the repository on your computer
6. Click **Clone**

### Method 2: Clone from GitHub Desktop

1. Open GitHub Desktop
2. Click **File** → **Clone repository** (or use Ctrl/Cmd + Shift + O)
3. You'll see three tabs:
   - **GitHub.com:** Your repositories and ones you have access to
   - **GitHub Enterprise:** If you have an enterprise account
   - **URL:** For repositories not listed or from other Git hosts

**Using GitHub.com tab:**

1. Select the repository you want to clone (`FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec`)
2. Choose the local path where you want to save it
3. Click **Clone**

**Using URL tab:**

1. Enter the repository URL (e.g., `(https://GitHub.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec)`)
2. Choose the local path
3. Click **Clone**

### After Cloning

Once cloned, you can:

- **View files:** Browse the repository files in your file explorer
- **Make changes:** Edit files using your preferred text editor or IDE (recommend [VSCode](https://code.visualstudio.com/))
- **Commit changes:** Save your changes with a descriptive message
- **Push to GitHub:** Upload your changes back to the online repository
- **Pull updates:** Download changes made by others

### Working with Your Cloned Repository

1. **Making changes:** Edit files in your preferred editor (recommend [VSCode](https://code.visualstudio.com/))
2. **Reviewing changes:** GitHub Desktop shows all modified files in the left panel
3. **Committing changes:**
   - You will need to submit a Pull Request to make changes to the FOCUS repository.  See [Working with Pull Requests](#working-with-pull-requests) and [How to Submit a Pull Request (PR) using GitHub Desktop and VSCode](#how-to-submit-a-pull-request-pr-using-GitHub-desktop-and-vscode)

---

## Working with Pull Requests

Pull requests are a way to propose changes to a repository. Sometimes you'll need to work on an existing pull request to make modifications or add features. Here's how to clone a pull request, make changes, and push them back.

### Understanding Pull Request Branches

When someone creates a pull request, they're proposing to merge changes from one branch (usually called a "feature branch") into another branch (usually "main" or "master"). To work on a pull request, you need to check out the feature branch.

---

## How to Submit a Pull Request (PR) using GitHub Desktop and VSCode

//TODO
TODO

---

## How to Submit Changes to an an Existing PR using GitHub Desktop and VSCode

### Method 1: Checking Out a Pull Request from GitHub Desktop

**Step 1: Clone the Repository**

1. First, clone the repository using the methods described in the previous section
2. Make sure you have the repository open in GitHub Desktop

**Step 2: Fetch All Branches**

1. In GitHub Desktop, click **Repository** → **Pull** to ensure you have the latest changes
2. Click **Branch** → **New Branch** to see available branches
3. GitHub Desktop automatically fetches remote branches

**Step 3: Check Out the Pull Request Branch**

1. Look for the branch associated with the pull request (you can find the branch name on the GitHub pull request page)
2. In GitHub Desktop, click **Current Branch** dropdown at the top
3. Look for the branch under **Remote branches**
4. Click on the branch name to check it out locally
5. GitHub Desktop will create a local copy of the remote branch

### Method 2: Using GitHub's Pull Request Interface

**Step 1: Find the Pull Request Branch Name**

1. Go to the pull request on GitHub.com (https://GitHub.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pulls)
2. For this example, we'll use [PR 1088](https://GitHub.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/1088)
3. Look for the branch information near the top (e.g., "ljadvey wants to merge 3 commits into working_draft from 1016/GitHub-guidelines")
4. Note the source branch name (in this example, "1016/GitHub-guidelines")

**Step 2: Clone and Check Out**

1. Clone the repository if you haven't already (see [Cloning a Repository with GitHub Desktop](#cloning-a-repository-with-GitHub-desktop))
2. In GitHub Desktop, use the branch dropdown to find and check out the pull request branch (`1016/GitHub-guidelines`) by clicking on the branch which will automatically load the file changes from the repository.

### Making Modifications to the Pull Request

**Step 1: Ensure You're on the Correct Branch**

1. In GitHub Desktop, verify the current branch name matches the pull request branch
2. The branch name is displayed at the top of the GitHub Desktop interface

**Step 2: Make Your Changes**

1. Open the repository files in your preferred text editor or IDE (recommend [VSCode](https://code.visualstudio.com/))
2. Make the necessary modifications to the code
3. Save your changes

**Step 3: Review Your Changes**

1. Return to GitHub Desktop
2. You'll see your modified files listed in the left panel under "Changes"
3. Click on each file to review the specific changes (additions in green, deletions in red)

### Committing and Pushing Changes

**Step 1: Stage and Commit Changes**

1. In GitHub Desktop, review all the changes you want to include
2. Write a clear commit message describing your modifications (in the bottom left part of the GitHub Desktop window)
3. Optionally, add a longer description explaining the reasoning behind your changes
4. Click **Commit # file to [branch-name]**

**Step 2: Push Changes to the Pull Request**

1. After committing, click **Push origin** in GitHub Desktop
2. This uploads your changes to the remote branch
3. Your changes will automatically appear in the existing pull request

### Verifying Your Changes

**Step 1: Check the Pull Request Page**

1. Go back to the pull request page on GitHub.com
2. You should see your new commits listed in the conversation
3. The "Files changed" tab will show your modifications

**Step 2: Update Pull Request Description (if needed)**

1. If your changes significantly alter the pull request's purpose, update the description
2. Add comments explaining your modifications
3. Tag relevant reviewers if necessary

### Collaborative Pull Request Workflow

**Working with Others:**

1. **Communication:** Leave comments on the pull request explaining your changes
2. **Conflict Resolution:** If others have pushed changes, you may need to pull their updates first
3. **Review Process:** Your changes will go through the same review process as the original pull request

**Handling Conflicts:**

1. If there are merge conflicts, GitHub Desktop will show them clearly
2. Use GitHub Desktop's built-in merge editor to resolve conflicts
3. Commit the resolved conflicts and push to update the pull request
4. If you run into issues, seek help on the [#working-group](https://f2-focus.slack.com/archives/C06MJPRAPCH) slack channel

### Best Practices for Pull Request Modifications

**Before Making Changes:**

- Read through the existing pull request description and comments
- Understand the original intent and scope
- Communicate with the original author if making significant changes

**When Making Changes:**

- Keep modifications focused and related to the pull request's purpose
- Write clear commit messages that explain what and why
- Test your changes thoroughly before pushing

**Communication:**

- Leave clear comments about what you changed and why
- Tag the original pull request author
- Update the pull request description if your changes expand the scope

### Troubleshooting Common Issues

**Branch Not Found:**

- Make sure you've fetched the latest changes from the remote repository
- Verify the branch name matches exactly what's shown in the pull request

**Permission Issues:**

- Ensure you have write access to the repository
- For forks, you may need to push to your own fork and create a new pull request

**Merge Conflicts:**

- Pull the latest changes from the target branch (usually main)
- Resolve conflicts using GitHub Desktop's merge editor
- Commit the resolution and push

**Changes Not Appearing:**

- Verify you're on the correct branch before making changes
- Ensure you've committed and pushed your changes
- Check that you're looking at the right pull request

---

## Data Exercise to learn FOCUS columns

---

## Tips for Success

### Best Practices

- **Commit frequently** with clear, descriptive messages
- **Pull before pushing** to avoid conflicts
- **Use branches** for new features or experiments
- **Write good commit messages** that explain what and why, not just what

### Common Issues and Solutions

- **Repository not showing:** Make sure you're signed in to the correct GitHub account
- **Clone fails:** Check your internet connection and repository permissions
- **Can't push changes:** Ensure you have write access to the repository
- **Merge conflicts:** Use GitHub Desktop's built-in merge conflict resolver

### Getting Help

- **GitHub Desktop documentation:** [docs.GitHub.com/desktop](https://docs.GitHub.com/desktop)
- **GitHub Support:** [support.GitHub.com](https://support.GitHub.com)
- **Community Forum:** [GitHub.community](https://GitHub.community)
