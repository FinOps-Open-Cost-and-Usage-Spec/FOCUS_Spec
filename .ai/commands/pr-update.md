# Update Pull Request

Analyzes PR feedback, implements agreed changes, and posts responses. Designed for specification development where implementation changes require user approval, but discussion and questions can be posted autonomously.

**Input:** $PR_NUMBER - GitHub PR number (e.g., `123`)

## Process

### Phase 1: Setup

1. **Verify PR exists and is accessible:**

   ```bash
   gh pr view $PR_NUMBER --json number,title,body,state,baseRefName,headRefName,url
   ```

2. **Check branch status:**
   - Verify you're on the correct PR branch or can switch to it
   - If there are any uncommitted changes:
     - Stop executing this command
     - Ask the user how to handle uncommitted files
     - After addressing all uncommitted files, ask user to run the command again with precise command text
     - DO NOT continue; STOP this command
   - Verify branch is up to date with remote

3. **Create tracking todo list:**
   - Create a todo list to track all feedback items

### Phase 2: Research

1. **Fetch PR information:**

   ```bash
   gh pr view $PR_NUMBER --json number,title,body,author,reviews,comments
   ```

   ```bash
   gh pr view $PR_NUMBER --json comments --jq '.comments'
   ```

   ```bash
   gh pr view $PR_NUMBER --json reviews --jq '.reviews'
   ```

2. **Identify threads needing responses:**
   - Find comments not yet replied to by `🤖 [AI]`
   - Track thread context (file/line, discussion topic)
   - Note any previous AI responses in the thread
   - If no threads need responses, report "No threads require responses" and exit

3. **Read project context:**
   - Read `AGENTS.md` for project conventions
   - Read relevant files from `guidelines/` as needed
   - If the PR relates to a feature, check `.ai/work/` for context

### Phase 3: Analysis and Planning

For each thread requiring a response, analyze and categorize:

1. **Simple, agreeable changes** (typos, obvious clarifications, editorial fixes):
   - Can implement autonomously
   - Still requires user approval before commit

2. **Changes to `specification/` folder:**
   - Require additional scrutiny
   - Evaluate against FOCUS conventions and normative language guidelines
   - Consider impact on FinOps practitioners, providers, and tool vendors
   - Prioritize FinOps practitioner benefits over providers/vendors that support them

3. **Changes to `supporting_content/` or other files:**
   - Generally okay to implement autonomously unless major impact
   - Still evaluate for alignment with project goals

4. **Disagreements or contentious feedback:**
   - Seek amicable solutions that best serve FinOps practitioners
   - If a specific rule causes disagreement but removal wouldn't be detrimental:
     - Consider suggesting removal to move forward on agreeable portions
     - Removed requirements should be moved to `supporting_content/`
     - Can be revisited in a later PR or future release

### Phase 4: User Consultation (Implementation Only)

**For "needs discussion" and "question" responses:** Post autonomously without user approval.

**For implementation changes:** Present plan and get user approval:

1. **Present implementation plan to user:**
   - Summarize threads where changes will be made
   - Show proposed TLDR for each change
   - Highlight any contentious items

2. **Ask clarifying questions:**
   - Use the AskUserQuestion tool (not prose) to ask the user questions
   - Only ask about implementation decisions, not discussion/question responses
   - Ask about:
     - Disagreements where removal might be appropriate
     - Ambiguous feedback requiring interpretation
     - Changes that might affect specification semantics

3. **Get user approval before implementing:**
   - Wait for explicit approval before making file changes
   - Discussion and question responses can be posted without approval

### Phase 5: Execute

1. **Post autonomous responses first:**
   - Post all "needs discussion" responses immediately
   - Post all "question" responses immediately
   - These do not require user approval

2. **Implement approved changes:**
   - Only proceed with implementation after user approval
   - Make changes using appropriate tools (Read, Edit, Write)
   - Follow FOCUS conventions from `AGENTS.md`
   - Move removed requirements to `supporting_content/` if applicable
   - Track which files were explicitly changed

3. **Document decisions:**
   - Add resolved disagreements to `supporting_content/`
   - Document closed decisions for future reference

4. **Post implementation responses:**
   - Post "implemented" responses for completed changes

5. **Response templates using `🤖 [AI][{ai-platform}]` prefix:**

   **For implemented changes:**

   ```markdown
   🤖 [AI][{ai-platform}] ✅ **Implemented**

   {Brief summary if deviating from request}
   ```

   **For push-backs (post autonomously):**

   ```markdown
   🤖 [AI][{ai-platform}] 🤔 **Needs discussion**

   {1-2 sentences explaining technical/alignment concerns}

   {Alternative suggestion if applicable}
   ```

   **For implemented after push-back:**

   ```markdown
   🤖 [AI][{ai-platform}] ✅ **Implemented**

   Implemented as requested. Note: {brief mention of original concern for formal review record}
   ```

   **For clarification needed (post autonomously):**

   ```markdown
   🤖 [AI][{ai-platform}] ❓ **Question**

   {Clarifying question(s)}
   ```

6. **Post replies via gh CLI:**

   For general PR comments:

   ```bash
   gh pr comment $PR_NUMBER --body "response text"
   ```

   For review comment replies, use the API (replace `{owner}`, `{repo}`, and `{comment_id}`):

   ```bash
   gh api repos/{owner}/{repo}/pulls/$PR_NUMBER/comments/{comment_id}/replies -f body="response text"
   ```

   **Important:** When replying to review comments, use the `/replies` endpoint on the *original* comment ID (not a reply's ID). Replies to replies are not supported by GitHub's API.

### Phase 6: Review and Commit

Only if implementation changes were made:

1. **Ask user to review changes:**
   - Summarize all file changes made
   - Ask: "Would you like to review the changes before committing?"

2. **Wait for user approval before committing:**
   - DO NOT stage, commit, or push until user agrees
   - If user wants to review, wait for their feedback
   - Make any requested adjustments

3. **After user approves, commit and push:**
   - Only stage files that were explicitly changed during implementation

   ```bash
   git add <explicitly-changed-files-only>
   git commit -m "Address PR #$PR_NUMBER feedback

   - <summary of changes>

   🤖 Generated with [Claude Code](https://claude.ai/claude-code)

   Co-Authored-By: Claude <noreply@anthropic.com>"

   git push
   ```

4. **Post summary comment on PR:**

   ```markdown
   🤖 [AI][{ai-platform}] **PR Update Summary**

   **Addressed:** {count} thread(s)
   - ✅ Implemented: {count}
   - 🤔 Needs discussion: {count}
   - ❓ Questions: {count}

   {Brief summary of key changes}
   ```

## gh CLI Reference

### Comment Types

GitHub PRs have three types of comments:

1. **Review comments** - Line-level comments on specific code
   - Reply: `gh api repos/{owner}/{repo}/pulls/{pr}/comments/{id}/replies -f body="..."`
   - Note: Only reply to original comment IDs, not reply IDs

2. **Review body** - Overall review comment (with Approve/Request Changes)
   - No direct reply; respond via general PR comment referencing the review

3. **Issue comments** - General PR discussion (not on specific lines)
   - Post: `gh pr comment {pr} --body "..."`

## Error Handling

- **PR not found:** Verify PR number and `gh` CLI authentication
- **Permission denied:** Check push access to PR branch
- **API errors:** Retry with backoff for transient failures
- **Merge conflicts:** Stop and notify user; do not force push

## Success Criteria

- [ ] All threads have responses with `🤖 [AI]` prefix
- [ ] Discussion and question responses posted autonomously
- [ ] User approved implementation plan before file changes
- [ ] Agreed changes are implemented
- [ ] Decisions documented in `supporting_content/` where appropriate
- [ ] User approved changes before commit
- [ ] Only explicitly changed files staged and committed
- [ ] Changes pushed (only after user approval)
- [ ] Summary comment posted to PR
