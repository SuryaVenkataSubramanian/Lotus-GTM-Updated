# Document360 Lotus (Beta): GTM command center

**Docs as code, synced both ways.** Your docs in GitHub. Your team in Document360. Always in sync.

This repository is the complete go-to-market kit for Document360 Lotus, the docs-as-code product type of Document360 with two-way GitHub sync. All content follows PRD v0.3.17. It includes the GTM command center, the waitlist landing page, both newsletters, the brand assets and every written resource. It is a static site with no build step and deploys on Vercel as is.

## Pages

| URL | What it is |
| --- | --- |
| `/` | GTM command center: 22 launch assets, filters by type and phase, search, and the full resource in a pop-up |
| `/landing` | Waitlist landing page with the GradientASCII hero animation and the Document360 ⟷ Lotus ⟷ GitHub visual |
| `/waitlist`, `/lotus` | Short links to the waitlist landing page (`/landing`); the old `/waitlist-landing-page` link redirects there too |
| `/newsletters/lotus-newsletter-existing-customers` | Customer newsletter (HTML for Ortto) |
| `/newsletters/lotus-newsletter-trial-demo-leads` | Trial and demo leads newsletter (HTML for Ortto) |

## Folders

| Folder | Contents |
| --- | --- |
| `assets/` | Images used by the landing page; `brand/` (Lotus mascot, Document360 logo in purple and white); `ads/` (20 paid social banners, 1200 × 628) |
| `newsletters/` | Both HTML emails, `lotus-banner.png` and `document360-logo.png` (upload both to Ortto and swap the image `src` values marked in each email before sending) |
| `lotus-hero/` | `LotusHero.jsx` for the live site; add the component with `npx shadcn@latest add @react-bits/GradientASCII-JS-CSS` |
| `source/content/` | Every command center resource as Markdown (strategy, product tour, competitive, blog, scripts, Product Hunt, influencers, paid social and more) |
| `source/images/` | Screenshots from the Lotus design, hero visuals and thumbnails used by the command center |
| `source/build/` | The Python builders that generated the command center, landing page and emails |

## Theme

Inter and Plus Jakarta Sans; Document360 primary `#7f56d9` (buttons `#6941c6`), neutrals `#18181b` / `#52525b` / `#e4e4e7`, lavender `#f2eefb`. The command center supports light and dark mode.

## Related links

- Command center (Claude artifact): https://claude.ai/artifact/LAGDttmSaxFsVGTDw9hw2C
- Landing page design canvas: https://claude.ai/artifact/C4mmh1oitDopuMyE27WWme

## Messaging rules (PRD v0.3.17)

- Name: **Document360 Lotus**, Beta at launch. GitHub is the only Git provider.
- Don't claim Analytics, custom pages, article templates, public API, integrations, Find & Replace, recycle bin, archive, scheduled publish or unpublishing for Lotus.
- Lotus is a new project type: don't promise to convert existing Document360 projects.
- Auto Fix suggests SEO descriptions, tags and related articles (empty fields only).
