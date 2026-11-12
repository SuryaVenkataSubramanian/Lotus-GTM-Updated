## Brief

A 3-minute screen walkthrough of the real Lotus flow, from choosing Lotus to merging a pull request and resolving a conflict, with one presenter on voiceover.

| Item | Detail |
| --- | --- |
| Length | 3:00 – 3:30 |
| Where it runs | Product Hunt gallery, Lotus landing page, YouTube, blog embed, customer webinar |
| Audience | Docs teams that work with developers; Document360 customers with developer docs |
| Tone | Calm and practical. Show the product doing the work |
| Presenter | Product lead on voiceover, face-cam bubble optional |
| Demo setup | Sample repo `acme/docs` with `docs/` in a subdirectory; a second browser window with GitHub; one prepared conflicting commit |
| Must show | Choosing Lotus, connecting a repo and branch, the coding-agent prompt for `d360.json`, first sync, the Synced pill, a GitHub commit arriving, save to branch → pull request → Merge & publish, a conflict resolved, the audit log |
| Must not show | Real customer repos; GitLab or Bitbucket (not supported at launch) |

## Script

| # | Time | On screen | Voiceover |
| --- | --- | --- | --- |
| 1 | 0:00–0:15 | Split screen: `quick-start.md` in GitHub says "Download report"; the help center article still says "Export CSV" | "Most teams have two copies of every doc: Markdown in the repo, and a pasted copy in the help center. And they never match for long." |
| 2 | 0:15–0:25 | Lotus mascot animates in. Title: "Document360 Lotus: docs as code, synced both ways" | "This is Document360 Lotus. Your docs live in GitHub, your team works in Document360, and every change lands on both sides." |
| 3 | 0:25–0:40 | Step 1: "How does your team write docs?" Cursor selects **Document360 Lotus** | "Start a project and choose Document360 Lotus. It's the docs-as-code path, built into Document360." |
| 4 | 0:40–1:00 | Connect with GitHub: authorize, install the GitHub App, choose `acme/docs`, branch `main`, toggle "Docs are in a subdirectory" | "Authorize GitHub, install the app, and pick any repository and branch. Docs in a subfolder? Point Lotus at it." |
| 5 | 1:00–1:20 | "Required file missing: d360.json". Click **Copy prompt**, paste into Claude Code, agent commits the file, click **I've added it, re-check** | "Lotus maps your folders to categories with a small manifest called d360.json. Don't have one? Copy this prompt into your coding agent. It builds the file and commits it. Re-check, and you're ready." |
| 6 | 1:20–1:35 | Sync steps tick through, then the editor opens with the **Synced** pill | "The first sync validates every file. Here's the whole repo as a knowledge base, with the Git status right at the top." |
| 7 | 1:35–1:50 | In GitHub, a developer commits a change. In Document360, the pill shows **Updates**, then the article refreshes | "A developer commits in GitHub. Lotus picks it up, and the article updates here. No copy and paste." |
| 8 | 1:50–2:25 | Writer creates a branch, edits, clicks **Save to branch**, **Create pull request**; menu shows "Pull request is ready to merge"; **Merge & publish** with the change list and Eddy AI suggestions | "Now the other direction. A writer branches, edits in the editor, saves, and opens a pull request, all without a terminal. When it's approved, Merge & publish merges the PR and publishes the docs. Eddy AI even suggests improvements before it goes live." |
| 9 | 2:25–2:50 | **Updates** pill, then Review conflicts: side-by-side blocks, click **Keep both**, then **Mark as resolved** | "And when GitHub and Document360 both change the same paragraph? You see both versions side by side. Keep inbound, keep yours, or keep both. No merge markers." |
| 10 | 2:50–3:05 | Audit log: pushes, PR created, merged, with the files changed; My profile with GitHub linked | "Every change is on the record, and once a writer links GitHub, their publishes are committed under their own name." |
| 11 | 3:05–3:15 | Hero visual, end card with CTA URL | "Your docs in GitHub. Your team in Document360. Always in sync. Join the Lotus waitlist." |

## Reference screens

![Scene 3: choose Lotus](img:step1)

![Scene 5: the coding-agent prompt](img:agent)

![Scene 8: pull request ready to merge](img:prmenu)

![Scene 9: review conflicts](img:conflicts)

## Production notes

- Record at 1440 × 900 with 125% browser zoom so the Git status pill and branch menu read on a phone.
- Speed up the agent and sync steps 4× with a small "sped up" label; keep the Merge & publish click in real time.
- Burn in captions: most Product Hunt and LinkedIn views are muted.
- Cut three 15-second clips: scene 5 (agent prompt), scene 8 (PR to publish), scene 9 (conflict resolved).
- YouTube chapters: 0:00 Two copies · 0:25 Choose Lotus · 0:40 Connect · 1:00 d360.json · 1:20 First sync · 1:35 GitHub to Document360 · 1:50 Pull requests · 2:25 Conflicts · 2:50 Audit log.
