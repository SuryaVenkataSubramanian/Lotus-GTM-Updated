## The frame

GitHub on the left, the Lotus mascot in the middle, Document360 on the right. The arrows run both ways: a commit in GitHub becomes an article, and an edit in Document360 becomes a commit and a pull request.

![Brand video key frame](img:hero)

## Code (left): `docs/analytics/exporting-reports.md`

```md
---
title: "Exporting reports"
category: "Analytics"
tags: [analytics, export]
---

# Exporting reports

Open **Analytics → Reports** and select **Download report**.
Choose **CSV** or **PDF**. Exports include up to **24 months** of data.

> Admins can schedule exports **daily**, **weekly** or **monthly**.
```

And the manifest that maps folders to categories (illustrative; confirm the real schema with product):

```json
{
  "categories": [
    {
      "title": "Analytics",
      "path": "docs/analytics",
      "articles": [
        { "title": "Exporting reports", "file": "exporting-reports.md" }
      ]
    }
  ]
}
```

## Documentation (right)

> **Analytics › Exporting reports** · ● Synced · main
>
> **Exporting reports**
> Tags: analytics, export
>
> Open **Analytics → Reports** and select **Download report**. Choose **CSV** or **PDF**. Exports include up to **24 months** of data.
>
> ℹ️ Admins can schedule exports **daily**, **weekly** or **monthly**.
>
> *Last change: commit a91c3e7 by markjamesdev*

## Frame B: the other direction

A writer changes "24 months" to "36 months" in Document360, clicks **Save to branch**, then **Create pull request**. The GitHub side shows the diff (`- 24 months` / `+ 36 months`) on PR #122, then **Merged**, and the article shows **Published**.

## How each line becomes the article

| In the repo | Becomes in Document360 |
| --- | --- |
| `title: "Exporting reports"` | Article title |
| `category: "Analytics"` and the `d360.json` entry | The article's place in the category tree |
| `tags: [analytics, export]` | Article tags |
| `**Download report**`, `**CSV**`, `**PDF**` | Bold UI labels in the article |
| `> Admins can schedule…` | A callout |
| The commit itself | An audit log entry, and contributor credit for the GitHub author |

Every line on the right traces back to a line on the left, and every edit on the right travels back as a commit. That's the "synced both ways" message, shown on screen instead of stated.
