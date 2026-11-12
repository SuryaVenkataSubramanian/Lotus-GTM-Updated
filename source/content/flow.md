## How Lotus works, screen by screen

This tour follows the Lotus design end to end. Every screenshot is taken from the design, and every claim in the launch assets traces back to one of these screens.

### 1. Choose how your team writes docs

New projects start with one question: the editor-first Document360 product, or **Document360 Lotus** (Beta), the docs-as-code product type. Lotus keeps docs in a GitHub repo, synced with Document360: write and review with pull requests, or edit in Document360, and changes flow both ways.

![Step 1: How does your team write docs?](img:step1)

### 2. Connect a repository or start from a template

Name the project, then choose **Connect with GitHub** to sync an existing repository, or **Start with a template** to begin from a ready-made docs structure that Lotus commits to your repo.

![Basic details: Connect with GitHub or Start with a template](img:basic)

### 3. Authorize, install the GitHub App, pick a repo and branch

Sign in with GitHub, install the Document360 GitHub App so it can push updates, then choose the repository and **any branch**. Docs can live in a subdirectory. Lotus checks for the `d360.json` manifest and confirms you're ready to sync.

![Connect with GitHub: repository and branch selected, d360.json found](img:connect)

### 4. No d360.json? Your coding agent writes it

If the manifest is missing, Lotus offers two paths: copy a ready-made prompt into your coding agent (Claude Code, Cursor, Codex) to generate and commit `d360.json`, then re-check; or use a template project. An invalid manifest gets the same fix-it prompt.

![d360.json missing: copy the prompt into your coding agent](img:agent)

### 5. First sync, validated step by step

Lotus fetches the repository, validates syntax, checks soft limits and wraps up. Starting from a template, it seeds articles and `d360.json`, pushes them to the repo and publishes.

![Template project syncing: seeding articles, pushing to repo, publishing](img:tplsync)

### 6. When a sync fails, you see exactly why

Failures list every file with the line and the reason ("front matter isn't closed with ---"), plus a prompt your coding agent can use to fix them. Retry when you're done.

![Sync failed: files with errors and a fix prompt](img:syncfail)

### 7. Work in the editor, with Git status always visible

The top bar shows the branch and a Git status: **Synced**, **Syncing**, **Updates** (new changes from GitHub) or **Sync failed**. Articles, categories and navigation come straight from the repo.

![Editor after sync, showing the Synced status](img:synced)

### 8. Branches, commits and pull requests without leaving Document360

Create a working branch, **Save to branch** (a commit), **Create pull request**, then watch it move from conflicts to ready to merge. **Merge & publish** merges the PR and publishes in one step. If a branch is deleted in GitHub, Lotus keeps your unsaved changes and offers to copy them to a new branch.

![Branch menu: pull request ready to merge](img:prmenu)

### 9. Publish with a full change list and AI suggestions

Before anything goes live, the confirmation lists every changed article, snippet, glossary term and variable. **Auto Fix** suggests SEO descriptions, tags and related articles for changed articles; it fills empty fields only, and you review before publishing. Everything goes out in **one commit**.

![Merge and publish confirmation with suggested improvements](img:merge)

### 10. Resolve conflicts in the browser, block by block

When GitHub and Document360 both change the same article, Lotus shows each conflict side by side: **Keep inbound** (GitHub), **Keep both** or **Keep yours** (Document360). Mark the article resolved and move on. While someone resolves an article, it's locked for others.

![Review conflicts: Keep inbound, Keep both, Keep yours](img:conflicts)

### 11. Publish safely to a protected main branch

If the tracked branch is protected in GitHub, publishing opens a pull request instead of committing directly, and later publishes add to the same pull request. Teams can choose to publish every change through a pull request, and to merge it automatically once reviews and checks pass. Writers need no GitHub account for any of this: what they can do follows their Document360 role.

![Connect with GitHub: repository, branch and d360.json check](img:connect)

### 12. Every commit is credited and audited

Link your GitHub account in My profile, and changes you make in GitHub are credited to you in the audit log and as a contributor on the knowledge base site. When a linked writer publishes, the commit is authored by their own GitHub account; otherwise by Document360 Bot. The audit log records Git events (pushes, branches, saves, pull requests and merges) with the files each one changed.

![Audit log with Git events](img:audit)

![My profile: GitHub account linked](img:profile)

## What this means for messaging

| Capability in the design | Message |
| --- | --- |
| Two-way sync, any branch, subdirectory | Your docs in GitHub and Document360, always in sync |
| Save to branch, pull requests, Merge & publish | Git workflows for everyone, without the command line |
| Review conflicts, block by block | Conflicts resolved in the browser, not in merge markers |
| Coding-agent prompts for d360.json and sync errors | Agent-ready from the first minute |
| Protected branches publish through a pull request | Your review rules are respected |
| Writers need no GitHub account | Anyone on the team can edit and publish |
| One Publish, one commit, with Auto Fix | Every change reviewed, every page improved |
| Commits authored by the writer, audit log | Every commit credited, every change on record |
