## Where Lotus fits

Two-way Git sync is no longer rare: GitBook and Mintlify both offer it. Lotus wins on what surrounds the sync, and on closing Document360's own gap.

| Platform | Git sync | Editing for non-developers | Conflicts | What to say |
| --- | --- | --- | --- | --- |
| **Document360 today (GitHub extension)** | One-way, GitHub → Document360, main branch only, fixed `docs/` folder | Can't edit synced content back to Git | n/a | Lotus replaces this: two-way, any branch, any folder |
| **Document360 Lotus** | Two-way, any branch, subdirectory, choose initial direction | Full Document360 editor, branches and pull requests in the UI | Resolved in the browser, block by block, with locking | Docs as code that doesn't leave writers behind |
| **GitBook** | Bi-directional with GitHub and GitLab | Visual editor, change requests | Handled through the Git layer | Lotus adds agent-ready setup, sync-error fixing, Eddy AI and the Document360 knowledge base platform |
| **Mintlify** | Git-native; web editor commits, branches and opens PRs | Web editor for page content | Three-way merge in the editor | Lotus serves knowledge bases and support content, not only developer docs, with localization, workspaces and analytics built in |
| **ReadMe** | Bi-directional via CLI and GitHub Action | Asks contributors to learn MDX | Through Git | Lotus needs no CLI: connect in the browser |
| **Fern** | Docs as code | No web editor that writes back to Git | Through Git | Lotus gives writers and PMs a real editor |

Sources: [Document360 GitHub extension docs](https://docs.document360.com/help/docs/github-extension), [GitBook comparison](https://www.gitbook.com/blog/best-documentation-collaboration-tools), [GitBook API docs comparison](https://www.gitbook.com/blog/api-docs-git-integration), [Mintlify web editor](https://www.mintlify.com/docs/editor), [GitBook Git Sync](https://gitbook.com/docs/docs-as-code/git-sync). The GitBook articles are a competitor's own comparisons; treat their claims about others with care.

## Our five differentiators

1. **Conflicts, solved for humans.** Side-by-side, block-level choices (Keep inbound, Keep both, Keep yours) and article locking. No merge markers, no terminal.
2. **Agent-ready setup.** Missing or broken `d360.json`, or files that fail validation? Lotus hands you a prompt for your coding agent, then re-checks.
3. **Start from where you are.** Connect a repo, start from a template, or push an existing Document360 project into GitHub by choosing the sync direction.
4. **Publish with a safety net.** A full change list before every publish, with Eddy AI suggestions for GEO/SEO, tags and related articles.
5. **A complete knowledge base around your repo.** Knowledge base site, Eddy AI search and chatbot, workspaces, localization, analytics and an audit log that records every commit.

## Lines to avoid

- "The only two-way sync": GitBook and Mintlify both have it.
- "Works with GitLab or Bitbucket": the design covers GitHub only.
- "No review needed": Lotus is built on review, through pull requests and the publish confirmation.
