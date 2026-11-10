# -*- coding: utf-8 -*-
"""Document360 Lotus newsletters, docs-as-code messaging. Brand template: Inter, indigo, Ortto merge tags.
No em dashes. One sentence per paragraph."""
import os, base64

OUT = "/mnt/user-data/outputs/newsletters"
F = "font-family:'Inter', -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif;"
WAITLIST = "https://document360v2.wpengine.com/lotus-waitlist-2/?utm_source=email&amp;utm_medium=newsletter&amp;utm_campaign=lotus-waitlist&amp;utm_content="
INK = "#0d0824"; INDIGO = "#2A1AB9"; TEXT = "#1a1d33"; BODY = "#4a4e66"; MUTED = "#7a7f96"; LINE = "#ebe9f3"; LAV = "#f6f0ff"

with open(os.path.join(OUT, "lotus-banner.png"), "rb") as fh:
    BANNER = "data:image/png;base64," + base64.b64encode(fh.read()).decode()

HEAD = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<!--
  Document360 Lotus waitlist newsletter (docs as code, two-way GitHub sync)
  Audience:     @@AUDIENCE@@
  Subject line: @@SUBJECT@@
  Alt subject:  @@ALTSUBJECT@@
  Preheader:    @@PREHEADER@@

  BEFORE SENDING: upload lotus-banner.png to Ortto's image library and replace the src of
  the image marked BANNER IMAGE below with the hosted URL. The embedded copy is only there
  so the file previews correctly in a browser.
-->
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<meta name="x-apple-disable-message-reformatting" />
<meta name="format-detection" content="telephone=no, date=no, address=no, email=no" />
<meta name="color-scheme" content="light only" />
<meta name="supported-color-schemes" content="light only" />
<title>@@TITLE@@</title>
<!--[if gte mso 9]>
<noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml></noscript>
<style type="text/css">table,td,div,p,a,h1,h2,h3,span{font-family:Arial,sans-serif !important;}</style>
<![endif]-->
<!--[if !mso]><!-->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet" />
<!--<![endif]-->
<style type="text/css">
  body, table, td, a { -webkit-text-size-adjust:100%; -ms-text-size-adjust:100%; }
  table, td { mso-table-lspace:0pt; mso-table-rspace:0pt; }
  img { -ms-interpolation-mode:bicubic; border:0; outline:none; text-decoration:none; height:auto; line-height:100%; display:block; }
  table { border-collapse:collapse; }
  body { margin:0 !important; padding:0 !important; width:100% !important; background-color:#efedf6; }
  a[x-apple-data-detectors] { color:inherit !important; text-decoration:none !important; }
  u + #body a { color:inherit; text-decoration:none; }
  @media only screen and (max-width:640px) {
    .container { width:100% !important; max-width:100% !important; }
    .px { padding-left:24px !important; padding-right:24px !important; }
    .hero-pad { padding:40px 24px 0 24px !important; }
    .hero-title { font-size:32px !important; line-height:1.1 !important; }
    .hero-sub { font-size:16px !important; }
    .banner-img { width:100% !important; height:auto !important; }
    .h2 { font-size:24px !important; }
    .stack { display:block !important; width:100% !important; }
    .cell-l { border-right:0 !important; }
    .cmp-th { padding:10px 8px !important; font-size:10px !important; }
    .cmp-td { padding:12px 8px !important; font-size:13px !important; }
    .close-pad { padding:40px 24px !important; }
    .close-title { font-size:26px !important; }
  }
</style>
</head>
<body id="body" style="margin:0; padding:0; background-color:#efedf6;">
<div style="display:none; max-height:0; overflow:hidden; mso-hide:all; font-size:1px; line-height:1px; color:#efedf6; opacity:0;">
@@PREHEADER@@&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
</div>
<table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color:#efedf6;">
  <tr>
    <td align="center" style="padding:32px 12px;">
      <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="620" class="container" style="width:620px; max-width:620px; background-color:#ffffff; border-radius:20px; overflow:hidden; border-collapse:separate;">
"""

def button(url, label, light):
    bg, fg = ("#ffffff", INK) if light is True else (("#7f56d9", "#ffffff") if light == "primary" else ("#000000", "#ffffff"))
    return f"""<!--[if mso]>
            <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="{url}" style="height:52px;v-text-anchor:middle;width:236px;" arcsize="50%" stroke="f" fillcolor="{bg}">
              <w:anchorlock/>
              <center style="color:{fg};font-family:Arial,sans-serif;font-size:16px;font-weight:700;">{label}</center>
            </v:roundrect>
            <![endif]-->
            <!--[if !mso]><!-->
            <a href="{url}" style="background-color:{bg}; color:{fg}; display:inline-block; {F} font-size:16px; font-weight:700; line-height:52px; text-align:center; text-decoration:none; padding:0 36px; border-radius:26px; mso-hide:all;">{label}</a>
            <!--<![endif]-->"""

def hero(eyebrow, kicker, title, sub, key, micro):
    url = WAITLIST + key + "_hero"
    return f"""
        <tr>
          <td bgcolor="#F2EEFB" style="background-color:#F2EEFB;">
            <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
              <tr>
                <td class="px" style="padding:26px 32px 0 32px;">
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tr>
                      <td style="{F} font-size:16px; font-weight:800; color:#18181b;">Document360</td>
                      <td align="right" style="{F} font-size:12px; font-weight:600; color:#4c3482;">{eyebrow}</td>
                    </tr>
                  </table>
                </td>
              </tr>
              <tr>
                <td align="center" class="hero-pad" style="padding:52px 48px 0 48px;">
                  <p style="margin:0 0 16px 0; {F} font-size:13px; font-weight:600; color:#7f56d9; letter-spacing:0.4px;">{kicker}</p>
                  <p class="hero-title" style="margin:0 0 18px 0; {F} font-size:44px; line-height:1.06; font-weight:800; color:#18181b; letter-spacing:-1.4px;">{title}</p>
                  <p class="hero-sub" style="margin:0 0 30px 0; {F} font-size:18px; line-height:1.55; color:#52525b;">{sub}</p>
                  {button(url, "Join the waitlist", "primary")}
                  <p style="margin:14px 0 0 0; {F} font-size:13px; line-height:1.5; color:#70707a;">{micro}</p>
                </td>
              </tr>
              <tr>
                <td align="center" style="padding:30px 20px 20px 20px;">
                  <!-- BANNER IMAGE: replace src with your hosted URL in Ortto -->
                  <img class="banner-img" src="{BANNER}" width="580" alt="Document360 categories and a GitHub repo, acme/docs, kept in sync both ways by Lotus, with pull request #122 merged." style="display:block; width:580px; max-width:100%; height:auto; border:0; border-radius:14px; {F} font-size:14px; color:#52525b;" />
                </td>
              </tr>
            </table>
          </td>
        </tr>
"""

def intro(lines):
    out = [f'<p style="margin:0 0 20px 0; {F} font-size:17px; line-height:1.6; color:{TEXT}; font-weight:600;">{{% if people.first-name != "None" %}}Hi {{{{ people.first-name }}}},{{% else %}}Hi There,{{% endif %}}</p>']
    for kind, text in lines:
        if kind == "quote":
            out.append(f"""<table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="margin:8px 0 24px 0;">
              <tr>
                <td width="3" style="background-color:{INDIGO}; width:3px; font-size:0; line-height:0;">&nbsp;</td>
                <td style="padding:4px 0 4px 20px; {F} font-size:20px; line-height:1.5; color:{TEXT}; font-weight:600;">{text}</td>
              </tr>
            </table>""")
        else:
            out.append(f'<p style="margin:0 0 16px 0; {F} font-size:17px; line-height:1.65; color:{BODY};">{text}</p>')
    return f"""
        <tr>
          <td class="px" style="padding:52px 48px 20px 48px;">
            {''.join(out)}
          </td>
        </tr>
"""

def head(kicker, title, top="36px"):
    return f"""
        <tr>
          <td class="px" style="padding:{top} 48px 0 48px;">
            <p style="margin:0 0 10px 0; {F} font-size:13px; font-weight:700; color:{INDIGO};">{kicker}</p>
            <p class="h2" style="margin:0; {F} font-size:28px; line-height:1.18; font-weight:800; color:{TEXT}; letter-spacing:-0.7px;">{title}</p>
          </td>
        </tr>
"""

def grid(items):
    def cell(t, d, left, bottom):
        br = f"border-right:1px solid {LINE};" if left else ""
        bb = f"border-bottom:1px solid {LINE};" if bottom else ""
        cls = "stack cell-l" if left else "stack"
        return f"""<td class="{cls}" valign="top" width="50%" style="{br} {bb} padding:24px;">
                  <p style="margin:0 0 6px 0; {F} font-size:17px; line-height:1.3; font-weight:700; color:{TEXT};">{t}</p>
                  <p style="margin:0; {F} font-size:14px; line-height:1.55; color:{BODY};">{d}</p>
                </td>"""
    a, b, c, d = items
    return f"""
        <tr>
          <td class="px" style="padding:24px 48px 0 48px;">
            <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="border:1px solid {LINE}; border-radius:16px; border-collapse:separate !important; background-color:#fcfbff;">
              <tr>{cell(*a, True, True)}{cell(*b, False, True)}</tr>
              <tr>{cell(*c, True, False)}{cell(*d, False, False)}</tr>
            </table>
          </td>
        </tr>
"""

def steps(items, numbered=True):
    rows = []
    for i, (t, lines) in enumerate(items, 1):
        bb = f"border-bottom:1px solid {LINE};" if i < len(items) else ""
        marker = (f'<table role="presentation" border="0" cellpadding="0" cellspacing="0" style="border-collapse:separate !important;"><tr><td align="center" valign="middle" width="34" height="34" style="width:34px; height:34px; border:1.5px solid {INDIGO}; border-radius:17px; {F} font-size:14px; font-weight:700; color:{INDIGO};">{i}</td></tr></table>'
                  if numbered else
                  f'<table role="presentation" border="0" cellpadding="0" cellspacing="0" style="border-collapse:separate !important;"><tr><td width="10" height="10" style="width:10px; height:10px; background-color:{INDIGO}; border-radius:5px; font-size:0; line-height:0;">&nbsp;</td></tr></table>')
        mpad = "22px 0" if numbered else "30px 0 22px 0"
        body = "".join(f'<p style="margin:0 0 6px 0; {F} font-size:16px; line-height:1.6; color:{BODY};">{l}</p>' for l in lines)
        rows.append(f"""<tr>
                <td valign="top" width="54" style="padding:{mpad}; {bb}">{marker}</td>
                <td valign="top" style="padding:22px 0 16px 0; {bb}">
                  <p style="margin:4px 0 6px 0; {F} font-size:17px; line-height:1.35; font-weight:700; color:{TEXT};">{t}</p>
                  {body}
                </td>
              </tr>""")
    return f"""
        <tr>
          <td class="px" style="padding:12px 48px 0 48px;">
            <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">{''.join(rows)}</table>
          </td>
        </tr>
"""

def compare(headers, rows):
    th = []
    for i, h in enumerate(headers):
        bg = f"background-color:{LAV};" if i == 2 else ""
        col = INDIGO if i == 2 else MUTED
        w = ["30%", "35%", "35%"][i]
        th.append(f'<td class="cmp-th" width="{w}" style="{bg} padding:14px 16px; {F} font-size:11px; font-weight:700; color:{col}; letter-spacing:0.8px; text-transform:uppercase; border-bottom:1px solid {LINE};">{h}</td>')
    trs = []
    for idx, (a, b, c) in enumerate(rows):
        bb = f"border-bottom:1px solid {LINE};" if idx < len(rows) - 1 else ""
        trs.append(f"""<tr>
                <td class="cmp-td" valign="top" style="padding:16px; {F} font-size:14px; line-height:1.45; font-weight:700; color:{TEXT}; {bb}">{a}</td>
                <td class="cmp-td" valign="top" style="padding:16px; {F} font-size:14px; line-height:1.45; color:{MUTED}; {bb}">{b}</td>
                <td class="cmp-td" valign="top" style="padding:16px; background-color:{LAV}; {F} font-size:14px; line-height:1.45; font-weight:600; color:{INDIGO}; {bb}">{c}</td>
              </tr>""")
    return f"""
        <tr>
          <td class="px" style="padding:24px 48px 0 48px;">
            <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="border:1px solid {LINE}; border-radius:16px; border-collapse:separate !important; overflow:hidden;">
              <tr>{''.join(th)}</tr>
              {''.join(trs)}
            </table>
          </td>
        </tr>
"""

def closing(title, lines, key, micro):
    url = WAITLIST + key + "_footer"
    ps = "".join(f'<p style="margin:0 0 10px 0; {F} font-size:16px; line-height:1.6; color:#c9c3ec;">{l}</p>' for l in lines)
    return f"""
        <tr>
          <td class="px" style="padding:52px 32px 32px 32px;">
            <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" bgcolor="{INK}" style="background-color:{INK}; border-radius:18px; border-collapse:separate !important;">
              <tr>
                <td align="center" class="close-pad" style="padding:48px 40px;">
                  <p class="close-title" style="margin:0 0 14px 0; {F} font-size:30px; line-height:1.15; font-weight:800; color:#ffffff; letter-spacing:-0.8px;">{title}</p>
                  {ps}
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0" style="margin-top:18px;"><tr><td align="center">
                  {button(url, "Join the waitlist", True)}
                  </td></tr></table>
                  <p style="margin:14px 0 0 0; {F} font-size:13px; line-height:1.5; color:#9f98cf;">{micro}</p>
                </td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td class="px" style="padding:0 48px 40px 48px;">
            <p style="margin:0; {F} font-size:15px; line-height:1.6; color:{BODY};">The Document360 team</p>
          </td>
        </tr>
"""

FOOT = """
      </table>
      <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="620" class="container" style="width:620px; max-width:620px;">
        <tr>
          <td class="px" align="center" style="padding:28px 40px;">
            <p style="margin:0; font-family:'Inter', Arial, sans-serif; font-size:12px; line-height:1.7; color:#7a7f96; text-align:center;">
              If you no longer wish to receive these emails you may change your <a href="https://document360.com/email-preference/?contactid={{ people.ap2_custom.contactidsystem-pipedrive }}" style="color:#2A1AB9; text-decoration:underline;">email preference</a> or <a href="{{ urls.unsubscribe }}" style="color:#2A1AB9; text-decoration:underline;">unsubscribe</a> at any time.
            </p>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
</body>
</html>
"""

def build(meta, body):
    h = HEAD
    for k, v in meta.items():
        h = h.replace(f"@@{k}@@", v)
    return h + body + FOOT

ML = "Be among the first to experience it. Early access spots are limited."
MC = "Be among the first customers to experience it. Early access spots are limited."

leads = (
    hero("Early access", "Introducing Document360 Lotus", "Docs as code.<br /><span style=\"color:#7f56d9;\">Synced both ways.</span>",
         "Keep your docs in GitHub.<br />Edit them in Document360. Lotus keeps both in sync.", "leads", ML)
  + intro([
        ("p", "You've been exploring Document360 to build a knowledge base your users can rely on."),
        ("p", "If your developers already keep docs in a GitHub repo, you've probably hit the same wall as everyone else."),
        ("quote", "Two copies of every doc: Markdown in the repo, a pasted copy in the help center, and they never match for long."),
        ("p", "That's why we built <strong style=\"color:#1a1d33;\">Document360 Lotus</strong>, docs as code built into Document360."),
        ("p", "Your docs live in GitHub and stay in sync with Document360 in both directions, so everyone works on the same docs in the tool they already use."),
    ])
  + head("What you get", "One source of truth, two ways to edit it", top="16px")
  + grid([("Two-way GitHub sync", "Commit in GitHub or edit in Document360. Every change lands on both sides."),
          ("Git in the browser", "Branch, save, open a pull request and Merge &amp; publish from the editor."),
          ("Conflicts made simple", "See both versions side by side and keep GitHub's, yours, or both."),
          ("Agent-ready setup", "Your coding agent writes the d360.json manifest from a prompt we provide.")])
  + head("How it works", "From your repo to a live knowledge base in four steps", top="52px")
  + steps([
        ("Choose Lotus", ["Start a project and pick Document360 - Lotus, the docs-as-code path."]),
        ("Connect GitHub", ["Authorize GitHub, install the app, and pick any repository and branch.", "Docs in a subfolder work too."]),
        ("Add the manifest", ["Lotus maps folders to categories with a small d360.json file.", "Don't have one? Paste our prompt into Claude Code, Cursor or Codex, or start from a template."]),
        ("Sync and keep working", ["Developers keep committing, writers keep editing, and Lotus syncs both ways."]),
    ])
  + head("The difference", "Docs as code today, versus docs as code with Lotus", top="44px")
  + compare(["The moment", "Docs as code today", "With Lotus"], [
        ("A writer fixes a typo", "Clone the repo or ask a developer", "Edit in Document360, it becomes a commit"),
        ("A developer ships a change", "Someone copies it into the help center", "The article updates on its own"),
        ("Both sides edit one page", "Merge markers nobody can read", "Side by side: keep inbound, yours or both"),
        ("Review before publishing", "Only developers can open a PR", "Anyone can, from the editor"),
        ("Going live", "Two places to update", "Merge &amp; publish, once"),
    ])
  + closing("Early access opens to a small group first",
            ["Join the waitlist to try Lotus before your next release."], "leads", ML)
)

cust = (
    hero("Customer early access", "New for Document360 customers", "Your GitHub sync<br /><span style=\"color:#7f56d9;\">just went two-way.</span>",
         "Lotus keeps your repo and your knowledge base in sync.<br />Edits here travel back to GitHub too.", "customers", MC)
  + intro([
        ("p", "Many of you keep developer docs in GitHub and asked us the same thing: can Document360 sync with the repo, both ways?"),
        ("p", "Our GitHub extension synced one way, from the main branch into Document360."),
        ("quote", "The moment a writer fixed something in Document360, the repo was out of date again."),
        ("p", "<strong style=\"color:#1a1d33;\">Document360 Lotus</strong> fixes that, and it's coming to your workspace."),
        ("p", "As a customer, you get first access."),
    ])
  + head("What you get", "Docs as code, built into the knowledge base you already run", top="16px")
  + grid([("Both directions", "GitHub to Document360 and back, on any branch, with docs in any folder."),
          ("Your project, your choice", "Connect a repo you have, or push this project into GitHub by choosing the sync direction."),
          ("Pull requests from the editor", "Save to branch, open a PR, and Merge &amp; publish in one click."),
          ("Every commit on record", "The audit log shows pushes, PRs and merges, and credits GitHub contributors.")])
  + head("What stays, what changes", "Your editor stays. The copy and paste goes.", top="52px")
  + compare(["The moment", "With the GitHub extension", "With Lotus"], [
        ("Sync direction", "GitHub to Document360 only", "Both ways"),
        ("Branches", "Main branch only", "Any branch, plus working branches and PRs"),
        ("Folder structure", "Fixed docs/ folder", "Any subdirectory, mapped by d360.json"),
        ("Edits in Document360", "Stay in Document360", "Become commits and pull requests"),
        ("Conflicts", "Not handled", "Resolved side by side in the editor"),
    ])
  + head("Why customers will notice", "Three things that change first", top="52px")
  + steps([
        ("Your writers stay in the editor", ["Branches, commits and pull requests are buttons, not commands."]),
        ("Your developers stay in GitHub", ["Every commit updates the knowledge base automatically."]),
        ("Your docs stop drifting", ["One source of truth, so the repo and the help center always match."]),
    ], numbered=False)
  + closing("Customers get first access",
            ["We're opening Lotus to a small group of customers first.", "Your feedback will shape the migration from the GitHub extension."], "customers", MC)
)

files = {
    "lotus-newsletter-trial-demo-leads.html": build({
        "AUDIENCE": "Free trial and demo leads",
        "SUBJECT": "Keep your docs in GitHub. Edit them anywhere.",
        "ALTSUBJECT": "Docs as code, without leaving writers behind",
        "PREHEADER": "Document360 Lotus syncs GitHub and Document360 both ways. Join the waitlist for early access.",
        "TITLE": "Docs as code. Synced both ways.",
    }, leads),
    "lotus-newsletter-existing-customers.html": build({
        "AUDIENCE": "Existing customers",
        "SUBJECT": "Your GitHub sync just went two-way",
        "ALTSUBJECT": "Early access for customers: docs as code with Lotus",
        "PREHEADER": "Lotus keeps your GitHub repo and Document360 in sync both ways. Customers get first access.",
        "TITLE": "Your GitHub sync just went two-way.",
    }, cust),
}
for name, html in files.items():
    assert "\u2014" not in html and "&mdash;" not in html, name
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as fh:
        fh.write(html)
    print(name, len(html))
