# GitHub Guidelines

Guidelines, recommendations, and instructions for how to work with FOCUS on GitHub.

## Table of Contents

1. [Logging into GitHub](#logging-into-GitHub)
2. [Configuring Notifications](#configuring-notifications)
3. [Installing GitHub Desktop](#installing-GitHub-desktop)
4. [Describe Specification Layout](#describe-specification-layout)
5. [How to Submit an Issue](#how-to-submit-an-issue)
6. [How to Interact (review, comment, participate in, etc.) with an Issue](#how-to-interact-review-comment-participate-in-etc-with-an-issue)
7. [Cloning a Repository with GitHub Desktop](#cloning-a-repository-with-GitHub-desktop)
8. [How to submit a Pull Request (PR) using GitHub Desktop and VSCode](#how-to-submit-a-pr-using-GitHub-desktop-and-vscode)
9. [How to submit changes to an an existing PR using GitHub desktop and vscode](#how-to-submit-changes-to-an-an-existing-pr-using-GitHub-desktop-and-vscode)
10. [Data Exercise to learn FOCUS columns](#data-exercise-to-learn-focus-columns)
11. [Tips for Success](#tips-for-success)

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

### Download and Installation

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

## Describe Specification Layout

---

## How to Submit an Issue

---

## How to Interact (review, comment, participate in, etc.) with an Issue

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

## How to Submit a Pull Request (PR) using GitHub Desktop and VSCode

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

## How to Submit Changes to an an Existing PR using GitHub Desktop and VSCode

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


