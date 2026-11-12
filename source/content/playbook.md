## Comment reply bank

Starting points only; rewrite each in your own words before posting.

| Likely question | Reply direction |
| --- | --- |
| How is this different from GitBook or Mintlify? | They're good tools and both sync with Git. Lotus adds writers who need no GitHub account, one-commit publishing, conflict resolution writers can use, agent-ready setup, and the full Document360 knowledge base around it. |
| How is this different from your old GitHub extension? | The extension syncs one way, from the main branch into Document360, and keeps working for existing projects. Lotus is a new project type that syncs both ways, on any branch, with pull requests and conflicts handled in the editor. |
| Do writers need to know Git? | No. Branch, save, pull request and Merge & publish are buttons in the editor. |
| What's d360.json? | A small manifest that maps folders to categories and files to articles. Your coding agent can write it from a prompt we provide, or start from a template. |
| What happens on a merge conflict? | Lotus shows each conflict side by side. Keep GitHub's, keep yours, or keep both, then mark the article resolved. Articles being resolved are locked for others. |
| Do writers need a GitHub account? | No. Saving, publishing, branches and pull requests follow the Document360 role. Linking GitHub is optional and only changes who the commit is credited to. |
| Is it generally available? | Lotus launches in Beta. [Confirm plans and Beta terms.] |
| What if a sync fails? | Nothing is imported until the repository is fixed. You see each file with the line and the reason, plus a prompt your coding agent can use to fix it. Then re-check. |
| GitLab or Bitbucket? | Lotus launches with GitHub only. [Add the roadmap answer once confirmed.] |
| Does it work with monorepos? | Yes, point Lotus at the subdirectory that holds your docs and `d360.json`. |
| Who gets credit for commits? | Link your GitHub account and your commits are credited to you in the audit log and as a contributor on the knowledge base site. |
| Pricing? | [Confirm pricing.] |
| Is my code safe? | [Security team to confirm: GitHub App permissions, what's stored, SOC 2 status.] |

## Outreach templates

Every message asks for feedback, not votes.

**Email to customers and the notify list (launch morning)**

> Subject: Lotus is live on Product Hunt: two-way GitHub sync
>
> Hi [First name],
>
> Today we launched Document360 Lotus on Product Hunt: docs as code, built into Document360. Your docs live in a GitHub repo and stay in sync with Document360 in both directions, with pull requests and conflict resolution right in the editor.
>
> We'd love your honest take. Check out the launch and tell us what you think: [PH link]
>
> [Name], Document360

**Personal DM (GitHub extension users, beta users, partners)**

> Hey [Name], you were one of the first to ask for two-way GitHub sync, and it's live on Product Hunt today. Your take on how it compares to the old extension would help a lot of teams deciding: [PH link]

**Developer community post (only where self-promotion is allowed)**

> We built two-way sync between a GitHub docs repo and a hosted knowledge base. Commits update articles; edits in the browser become commits and PRs; conflicts are resolved side by side. Setup uses a manifest your coding agent can write. It's on Product Hunt today, and blunt feedback from docs-as-code folks is very welcome: [PH link]

**In-app banner (launch day)**

> New: Lotus brings two-way GitHub sync to Document360. We're live on Product Hunt today, come say hi →

## Post-launch follow-through

- Day after: thank-you post with final ranks; reply to late comments
- Day after: Product Hunt badge on the Lotus landing page, homepage banner and email signatures
- Two days after: "What we learned from launch-day comments" post, including the GitLab and migration answers
- Week after: migration guide for GitHub extension users, sent to every extension account
- Week after: retarget Product Hunt visitors with the commercial and the waitlist
- Ten days after: launch report: ranks, traffic, signups, repositories connected, top objections
