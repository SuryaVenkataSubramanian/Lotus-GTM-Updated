## Where Lotus fits

We are in the same space as **Mintlify and GitBook**, then **ReadMe and Redocly**. Two-way Git sync is common across all of them, so Lotus wins on what surrounds the sync. This comparison is based on each company's own documentation.

| | Document360 Lotus | Mintlify | GitBook | ReadMe | Redocly |
| --- | --- | --- | --- | --- | --- |
| Two-way Git sync | GitHub | GitHub, GitLab | GitHub, GitLab | GitHub, GitLab, Bitbucket | Git-backed editor (GitHub, GitLab, Azure DevOps) |
| Connect an existing repo | Any branch, docs in a subfolder | Root or subfolder | Monorepo folders | Needs a new, empty repo | Yes |
| Editor for non-developers | Full Document360 editor, no GitHub account needed | Visual and Markdown modes | Visual editor | MDX editor in the live hub | Markdown/Markdoc file editor |
| Branches and PRs from the editor | Save to branch, PR, Merge & publish | Branch, PR, approve, Merge & publish | Change requests don't create GitHub PRs | Branches and reviews (Pro/Enterprise) | Branch, commit, PR, visual review |
| Conflict resolution | Side by side, block by block, with article locking | Helped in the editor | Not detailed in its docs | Built into the app | In pull requests |
| AI help | Agent-ready setup and sync-error fixes; Auto Fix before publish | Autopilot agent, AI assistant | GitBook Agent | AI linter, docs audit, agent | Agent reviews PRs (early access) |
| Built for | Knowledge bases and product docs for the whole team | Developer docs | Product and developer docs | API developer hubs | API docs and portals |

**Document360's own gap:** today's GitHub extension syncs one way, GitHub to Document360, from the main branch only. Lotus is the new docs-as-code product type that replaces it for new projects; the extension keeps working for existing ones.

Sources: [ReadMe bi-directional sync](https://docs.readme.com/main/docs/bi-directional-sync), [ReadMe: sync with GitHub](https://docs.readme.com/main/docs/sync-with-github), [Mintlify Git essentials](https://www.mintlify.com/docs/editor/git-essentials), [GitBook Git Sync troubleshooting](https://gitbook.com/docs/docs-as-code/git-sync/troubleshooting), [GitBook monorepos](https://gitbook.com/docs/~gitbook/embed/page/getting-started/git-sync/monorepos), [Redocly Reunite](https://redocly.com/docs/realm/reunite/reunite), [Document360 GitHub extension](https://docs.document360.com/help/docs/github-extension).

## Our five differentiators

1. **Writers need no GitHub account.** Saving, publishing, branches and pull requests follow the Document360 role.
2. **Publish once.** Every pending change is reviewed in one dialog and goes out as one commit; protected branches publish through a pull request.
3. **Conflicts, solved for humans.** Side-by-side, block-level choices and article locking. No merge markers, no terminal.
4. **Agent-ready setup.** Missing `d360.json` or a failed sync? Lotus hands you a prompt for your coding agent, then re-checks.
5. **A knowledge base around your repo.** The Document360 knowledge base site, Eddy AI search and chatbot, multiple workspaces and localization, with the OpenAPI reference generated from the spec in your repo.

## Where competitors are ahead

- **Git providers:** Lotus is GitHub only at launch.
- **Mintlify's editor workflow** (branch, PR, approve, Merge & publish) is the closest to ours, so lead with the knowledge base, no-GitHub-account writers and conflict handling.

## Lines to avoid

- "The only two-way sync": every competitor here has some form of it.
- "Works with GitLab or Bitbucket."
- "Analytics" for Lotus projects: not in the MVP.
- "Convert your existing Document360 project": Lotus is a new project type.
