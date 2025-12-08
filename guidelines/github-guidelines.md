# GitHub Guidelines

Guidelines, recommendations, and instructions for how to work with FOCUS on GitHub, using tools like a web browser, GitHub Desktop, and VSCode.

## Table of Contents

1. [FOCUS Repository Structure Overview](#focus-repository-structure-overview)
2. [Logging into GitHub](#logging-into-github)
3. [Configuring Notifications](#configuring-notifications)
4. [Installing GitHub Desktop](#installing-github-desktop)
5. [Installing Visual Studio Code](#installing-visual-studio-code)
6. [Configuring Local Spec Build](#configuring-local-spec-build)
7. [Interacting with (e.g., review, comment, participate in) an Issue via Web Browser](#how-to-interact-review-comment-participate-in-etc-with-an-issue-via-web-browser)
8. [Cloning a Repository with GitHub Desktop](#cloning-a-repository-with-github-desktop)
9. [Submitting a Pull Request (PR) using GitHub Desktop and VSCode](#how-to-submit-a-pull-request-pr-using-github-desktop-and-vscode)
10. [Submitting changes to an existing PR using GitHub desktop and VS Code](#how-to-submit-changes-to-an-existing-pr-using-github-desktop-and-vscode)
11. [Interacting with (e.g., review, comment, participate in) a PR via Web Browser](#how-to-interact-review-comment-participate-in-etc-with-a-pull-request-via-web-browser)
12. [Tips for Success](#tips-for-success)

---

## FOCUS Repository Structure Overview

## General Overview of FOCUS_Spec Repository

The [FOCUS_Spec repository](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec) contains the FinOps Open Cost and Usage Specification (FOCUS), which is a community-driven effort to develop a standard schema for cloud, SaaS, and other billing data. The primary goal of the FOCUS specification is to make it easier to understand, report on, and manage cloud costs.

## Repository Purpose

FOCUS is designed to address the complexity that FinOps practitioners face when dealing with disparate billing data formats from different cloud, software, and other service providers. Without a standard, each provider generates unique billing data files with their terminology, forcing practitioners to develop custom normalization schemes for each provider.

## Main Folders and Their Contents

### 1. `.github` folder

This is a standard GitHub directory that contains GitHub-specific configuration files and templates. Typically found at .github/workflows/ for GitHub Actions, .github/linters/ for linter configuration files.

A typical FOCUS contributor will not spend much time interacting with this folder, and thus it can be safely ignored.

### 2. `custom_linter_rules` folder

This directory contains custom linting rules specific to the FOCUS specification project. Linting rules help maintain code quality, ensure consistency in documentation, and establish coding best practices.

A typical FOCUS contributor will not spend much time interacting with this folder, and thus it can be safely ignored.

### 3. `guidelines` folder

This folder contains various guidelines on development, editorial, normative requirements, specification change, and specification design.

### 4. `specification` folder

The core folder containing the specification documentation:

- **`overview.md`** - Contains the main specification overview, principles, and requirements
- **`glossary.md`** - Comprehensive glossary of terms and definitions used throughout the specification
- **`columns` subfolder** - Contains detailed documentation for individual FOCUS columns like `servicesubcategory.md`

### 5. `supporting_content` folder

The repository provides supporting content that includes example mappings between well-known service provider datasets and what's defined in the FOCUS specification. This likely includes mappings for major cloud providers like:

- AWS (Amazon Web Services)
- GCP (Google Cloud Platform)
- Azure (Microsoft)
- Oracle Cloud

### 6. `vendored` folder

This directory contains third-party dependencies or external libraries that are directly included in the repository rather than being downloaded at build time.

A typical FOCUS contributor will not spend much time interacting with this folder, and thus it can be safely ignored.

### 7. Documentation Structure

The repository follows standard documentation patterns with:

- **`README.md`** - Main repository documentation
- **`CHANGELOG.md`** - Version changes and updates
- **`CONTRIBUTING.md`** - Overviews development environment for FOCUS specification.
- **`RELEASE-PLANNING.md`** - Outlines release planning and schedule information for FOCUS.
- Various markdown files for specification details

## Repository Organization Principles

The repository is organized around several key principles:

### FinOps Scenario-Driven Development

- Columns are defined to answer use cases rather than looking for use cases to fit existing columns
- Each column must have a clear use case
- Work backward from essential FinOps capabilities to prioritize dimensions, metrics, and attributes

### Incremental Development

- Incremental iterations are released regularly to provide higher value to practitioners
- Allow feedback as the specification develops
- The specification is expected to evolve over time

### Provider Neutrality

- Contributors must ensure the specification examines how each decision relates to each of the major cloud, SaaS, and other service providers
- Does not favor any single data generator's implementation
- Prioritizes enabling FinOps capabilities and alignment with the FinOps Framework

## Target Audience

The specification is designed to be used by three major groups:

1. **Billing Data Generators** - Cloud, SaaS, and other infrastructure and service providers that bill based on consumption.
2. **FinOps Practitioners** - Professionals who analyze and manage cloud costs.
3. **FinOps Tool Vendors** - Companies that provide tools and platforms for cloud cost management.

## Repository Status

The repository is actively maintained and represents a collaborative effort between:

- FinOps practitioners
- Cloud and SaaS service providers
- FinOps vendors
- The FinOps Foundation (supporting organization)
- Linux Foundation (hosting the specification project)

The repository is well-structured for both specification development and practical implementation, supporting the goal of creating a vendor-neutral standard for cloud billing data that can be adopted across different cloud service providers and FinOps tools.

---

## Logging into GitHub

### Create a GitHub Account

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

GitHub Desktop is a user-friendly application that makes it easy to work with Git and GitHub repositories without using the command line.  Further, GitHub desktop allows you to work with the repository (clone, branch, etc.) and push changes to the repository via pull requests.

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

Visual Studio Code (VS Code) is a free, powerful code editor that integrates seamlessly with Git and GitHub. It's highly recommended for editing code and managing repositories.

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
2. You may see a welcome screen with helpful getting-started information
3. VSCode will automatically detect your system settings and apply appropriate defaults

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

This is also elaborated upon within the [Cloning a Repository with GitHub Desktop](#cloning-a-repository-with-github-desktop) section.

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

**Viewing Git History:**

1. Install the **GitLens** extension
2. You'll see Git blame information inline with your code
3. Click on any line to see commit details
4. Use the **GitLens** panel to explore repository history

### Working with GitHub Features in VSCode

**Pull Requests:**

See [Working with Pull Requests](#working-with-pull-requests) for more details.

1. With the **GitHub Pull Requests and Issues** extension installed
2. Click the **GitHub** icon in the sidebar
3. View and manage pull requests directly from VSCode
4. Review code, leave comments, and merge pull requests

**Issues:**

See [How to Interact (review, comment, participate in, etc.) with an Issue via Web Browser](#how-to-interact-review-comment-participate-in-etc-with-an-issue-via-web-browser) for more details.

1. Access GitHub issues from the same GitHub panel
2. Create new issues or work on existing ones
3. Link commits to issues using keywords like "fixes #123"

**Code Reviews:**

See [Reviewing and Commenting on GitHub Issues](#reviewing-and-commenting-on-github-issues) for more details.

1. Open a pull request in the GitHub panel
2. Review changes with inline comments
3. Suggest changes directly in the editor
4. Approve or request changes

---

## How to Configure Local Spec Build

### FOCUS Specification Development Environment

The Specification is built in markdown, HTML, and PDF formats via a set of Python scripts.  This build pipeline automatically runs as a GitHub docker job in GitHub after every commit.  However, it can also be run locally to test changes as they are performed.  This functionality is therefore only needed by FinOps Foundation staff and core contributors, but any contributor can benefit from its use.

Currently, the only tested/supported environment is MacOS; however, the build pipeline in GitHub uses Ubuntu, so use of a Linux environment is theoretically possible.

The following setup steps are a rough guideline.  Your specific environment may require more and/or different specific steps, based on previous/legacy configurations.

### Setup Steps

1. Install homebrew (as per: https://brew.sh)
2. Setup cask

	`brew install cask`

3. Install python

	`brew install python`

4. Add packages for python

	`pip3 install -r requirements.txt`

5. Install pandoc

	`brew install pandoc`

6. Install HTML to PDF helper tool

	~~`brew install --cask wkhtmltopdf`~~

   UPDATE: WKHTMLTOPDF has been disabled in Homebrew as of late 2024.  The following commands can be run instead (or alternatively, it can be downloaded and installed from the [wkhtmltopdf website](https://wkhtmltopdf.org/downloads.html)):

   `curl -L https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-2/wkhtmltox-0.12.6-2.macos-cocoa.pkg -O`

   `installer -pkg wkhtmltox-0.12.6-2.macos-cocoa.pkg -target ~`

7. If your machine does not have git/make etc, you might run the following: Install developer command line tools for MacOS

	`xcode-select --install`

### Assembling the specification locally

1. Move into the `specification` folder
2. Use `make clean` to strike the output artifacts
3. Use `make` to generate the spec, which generates `spec.md`, `spec.html`, and `spec.pdf` in the `specification` folder

---

## How to Interact (review, comment, participate in, etc.) with an Issue via Web Browser

## Reviewing and Commenting on GitHub Issues

GitHub Issues are a powerful way to track bugs, feature requests, tasks, and other project-related discussions. Learning how to effectively review and comment on issues is essential for contributing to open standard projects and collaborating with teams.

### Understanding GitHub Issues

**What are Issues?**

- Issues are discussion threads related to specific topics in a repository
- They can be bug reports, feature requests, questions, or general discussions
- Each issue has a unique number and can be referenced across the repository
- Issues can be assigned to people, labeled, and organized into milestones

**Types of Issues**

- Action Item - This is a task within a Work Item issue
- FOCUS Feature Request - Propose a new attribute, refinement, or data structure for the FOCUS specification.
- General Feedback - Suggest minor corrections, clarity improvements, or inconsistencies in the FOCUS Specification.
- Maintenance Task - Create tasks related to work on the GitHub Repository or GitHub Actions.
- Work Item - Template for creating new Work Items (these are linked to a Feature Request)
- Blank issue - try not to use this, please

### Finding and Accessing Issues

**Viewing Repository Issues:**

1. Navigate to the [FOCUS repository](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec)
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
   - `is:issue state:open` - Open issues
   - `is:issue state:open type:Feature` - All open features
   - `is:issue state:open label:1.3` - Issues for version 1.3
   - `author:username` - Issues created by specific user
   - `assignee:username` - Issues assigned to specific user

### How to Submit an Issue

Issues are tickets in GitHub and are used to organize various request within FOCUS.

1. Go to https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues
2. Click `New Issue` (upper right)
3. Select the type of Issue that best describes your goal
  - Action Item - This is a task within a Work Item issue
  - FOCUS Feature Request - Propose a new attribute, refinement, or data structure for the FOCUS specification.
  - General Feedback - Suggest minor corrections, clarity improvements, or inconsistencies in the FOCUS Specification.
  - Maintenance Task - Create tasks related to work on the GitHub Repository or GitHub Actions.
  - Work Item - Template for creating new Work Items (these are linked to a Feature Request)
  - Blank issue - try not to use this, please
4. Fill out the details of the template, and please be straightforward and thorough.
5. Click the `Create` button

### Reading and Analyzing Issues

**Before Commenting:**

1. **Read the entire issue**, including the original description and all comments
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
- **Be demanding or impatient** - Open Standards are collaborative, not customer service
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

- If you've provided the requested information
- If you've found a solution or workaround
- If the issue status has changed (bug confirmed, feature approved, etc.)
- If you've tested a proposed fix

**How to Follow Up:**

```markdown
**Update:** I've reviewed the proposed solution and can confirm it works.

**Testing Environment:**
- Read details from PR #789
- Confirmed compatibility
- No concerns

The fix resolves the original issue. Thanks for the quick response!
```

### Advanced Issue Management

You can type comments and link issues to each other; entering a hashtag (#) will cause a pop-up to select the linked item (type or scroll to select the item).

**Creating Links Between Issues:**

```markdown
This issue is related to #123
This closes #456
Duplicate of #789
```

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
   - **GitHub.com:** Your repositories and those you have access to
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

Here's a comprehensive guide for submitting a Pull Request using GitHub Desktop and VSCode:

## Step-by-Step Instructions

### 1. Create a New Branch (GitHub Desktop)

1. Open GitHub Desktop
2. Select your repository from the dropdown
3. Click "Current branch" at the top
4. Click "New branch"
5. Name your branch descriptively (e.g., Start with your name (e.g. `flanakin/skuterm`);  Start with the Work Item number (e.g. `636-clarify-guidance-around-refunds`)
6. Click "Create branch"

### 2. Make Your Changes (VSCode)

1. Open VSCode
2. Open your project folder (File → Open Folder)
3. Make your code changes, add new files, or modify existing ones
4. Save your changes (Ctrl+S / Cmd+S)

### 3. Review and Commit Changes (GitHub Desktop)

1. Switch back to GitHub Desktop
2. You'll see your changes listed in the left panel
3. Review the diff in the main panel to ensure changes are correct
4. Add a descriptive commit message in the bottom left:
   - **Summary**: Brief description (e.g., "Add user authentication form")
   - **Description** (optional): More detailed explanation
5. Click "Commit to [your-branch-name]"

### 4. Push Your Branch

1. After committing, you'll see "Publish branch" or "Push origin"
2. Click this button to upload your branch to GitHub

### 5. Create the Pull Request

1. GitHub Desktop will show a "Create Pull Request" button - click it
2. This opens GitHub in your browser, or you can go to your repository on GitHub manually
3. You'll see a banner suggesting to create a PR for your recently pushed branch
4. Click "Compare & pull request"
5. Fill out the PR form:
   - **Title**: Clear, descriptive title
   - **Description**: Explain what changes you made and why
   - **Reviewers**: Add team members if needed
   - **Labels/Projects**: Add relevant tags if your repo uses them
6. Click "Create pull request"

## Alternative: Creating PR from GitHub Desktop

GitHub Desktop also offers a direct "Create Pull Request" option:

1. After pushing your branch, go to Branch → Create Pull Request
2. This opens your browser with the PR creation page pre-filled

## Best Practices

- **Atomic commits**: Make commits that represent single, logical changes
- **Clear commit messages**: Write messages that explain what and why, not just what
- **Test before submitting**: Ensure your code works and doesn't break existing functionality
- **Link issues**: Reference any related GitHub issues in your PR description using `#issue-number`

---

## How to Submit Changes to an Existing PR using GitHub Desktop and VSCode

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

1. In GitHub Desktop, verify that the current branch name matches the pull request branch
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

## How to Interact (review, comment, participate in, etc.) with a Pull Request via Web Browser

### Finding the Pull Request

1. Navigate to the [FOCUS repository](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pulls) on GitHub
2. Click the "Pull requests" tab
3. Click on the specific PR you want to comment on

### Making General Comments

**To add a general comment:**

1. Scroll to the bottom of the PR conversation page
2. In the "Write" tab of the comment box, type your comment
3. Use the "Preview" tab to see how your comment will look
4. Click "Comment" to submit

**Comment formatting options:**

- Use Markdown for formatting (bold, italic, code blocks, etc.)
- Add emoji reactions using `:emoji_name:` syntax
- Tag people using `@username`
- Reference issues with `#issue_number`

### Making Line-Specific Comments

**To comment on specific code lines:**

1. Click the "Files changed" tab
2. Hover over the line number you want to comment on
3. Click the blue "+" icon that appears
4. Type your comment in the text box
5. Choose between:
   - **"Add single comment"**: Posts immediately
   - **"Start a review"**: Saves comment for a formal review

**For multi-line comments:**

1. Click and drag from the starting line number to the ending line number
2. Click the [+] sign next to the last line number in the series.  This will select multiple lines for your comment
3. Add your comment and submit

### Making Code Suggestions

**To suggest specific code changes:**

1. Make a line-specific comment as above
2. Click the suggestion icon in the comment toolbar (the document icon with a + and -)
3. GitHub will pre-populate with the existing code
4. Edit the code to show your suggested changes
5. Add explanation text above or below the suggestion block
6. Submit the comment

**Example suggestion format:**

```suggestion
// Your improved code here
const userName = user.name || 'Anonymous';
```

### Conducting a Formal Review

**To start a comprehensive review:**

1. Go to "Files changed" tab
2. Add line-specific comments as needed, choosing "Start a review"
3. When finished reviewing all files, click "Review changes" (top right)
4. Choose your review type:
   - **Comment**: General feedback without approval status
   - **Approve**: Approve the changes for merging
   - **Request changes**: Block merging until issues are addressed
5. Add an overall review summary
6. Click "Submit review"

### Comment Features and Options

#### Reactions

- Click the emoji icon on any comment to add reactions
- Possible reactions: 👍 👎 😄 🎉 😕 ❤️ 🚀 👀

#### Editing Comments

- Click the "..." menu on your own comments
- Select "Edit" to modify
- Comments show "edited" indicator after changes

#### Resolving Conversations

- Click "Resolve conversation" on comment threads once issues are addressed
  - Typically, the resolution is a partnership between the PR author and the comment author.  The conversation should be resolved by the comment author upon review.  However, the PR author has the license to close the conversation without resolution if they provide sufficient context and/or the comment author does not promptly provide review.
- Helps track which feedback has been handled

### Notifications

- Use `@username` to notify specific people
- Use `@team/teamname` to notify entire teams

### Best Practices for PR Comments

#### Be Constructive

- Focus on the code, not the person
- Explain the "why" behind your suggestions
- Offer solutions, not just problems

#### Be Specific

- Quote the exact code you're referencing
- Provide examples of better approaches
- Link to documentation or standards when relevant

#### Use Appropriate Comment Types

- **Nitpicks**: Minor style/formatting issues
- **Suggestions**: Improvement ideas
- **Questions**: Ask for clarification
- **Blockers**: Serious issues that prevent merging

#### Sample Comment Templates

**For suggestions:**
```
Consider using a more descriptive variable name here. Instead of `data`, 
maybe `userProfile` would be clearer?
```

**For questions:**
```
Could you explain why we're using this approach instead of the built-in 
method? I want to make sure I understand the reasoning.
```

**For approval:**
```
Great work! The error handling looks solid and the tests cover the edge cases well. 
Ready to merge! ✅
```

---

## Tips for Success

Read the [development practices](development-processes.md) file.

Ask questions in the [working-group](https://f2-focus.slack.com/archives/C06MJPRAPCH) slack channel.

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
