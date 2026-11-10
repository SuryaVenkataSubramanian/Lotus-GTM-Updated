# -*- coding: utf-8 -*-
import base64, json, html, os, re

HERE = "/home/claude/cc"
MD = os.path.join(HERE, "md")
IMG = os.path.join(HERE, "img")
OUT = "/mnt/user-data/outputs/lotus-gtm-dashboard.html"

def uri(path, mime):
    with open(path, "rb") as fh:
        return f"data:{mime};base64," + base64.b64encode(fh.read()).decode()

IMAGES = {}
for f in sorted(os.listdir(IMG)):
    if f.endswith(".jpg"):
        IMAGES[f[:-4]] = uri(os.path.join(IMG, f), "image/jpeg")
IMAGES["mascot"] = uri(os.path.join(HERE, "mascot_256.png"), "image/png")
MASCOT_BIG = uri(os.path.join(HERE, "mascot_512.png"), "image/png")

WAITLIST = "https://document360v2.wpengine.com/lotus-waitlist-2/"
D360PH = "https://www.producthunt.com/products/document360"

# id, title, cat, phase, channel, audience, summary, md, link, link label, preview image (full), thumb
A = [
 ("overview", "GTM plan at a glance", "strategy", "plan", "Internal", "Marketing team",
  "What changed in Lotus, the five phases, go/no-go, KPIs, risks and open questions.", "overview.md", None, None, None, "hero"),
 ("flow", "Product tour: how Lotus works", "product", "plan", "Internal, sales, video", "Everyone on the launch",
  "Twelve steps through the Lotus design, from choosing Lotus to resolving conflicts, with the message each one proves.", "flow.md", None, None, None, "flow_thumb"),
 ("competitive", "Competitive landscape", "strategy", "plan", "Internal, sales", "Marketing and sales",
  "Lotus against GitBook, Mintlify, ReadMe, Fern and the current GitHub extension, with five differentiators.", "competitive.md", None, None, None, "conflicts_c"),
 ("strategy", "Positioning and message house", "strategy", "plan", "Internal", "Marketing team",
  "Positioning statement, message house, audiences in order and the four strategic moves.", "strategy.md", None, None, None, "strategy_thumb"),
 ("landing", "Waitlist landing page", "content", "base", "Website", "All audiences",
  "The new docs-as-code landing page: hero, how it works, features, extension comparison and FAQ.", "landing.md", "/waitlist-landing-page", "Open the landing page design", None, "landing_thumb"),
 ("blog", "SEO blog: docs as code", "content", "base", "Blog, search", "Docs teams, developers, PMs",
  "SEO brief and the full ~1,600-word article with screenshots, checklist and FAQ.", "blog.md", None, None, None, "herobare"),
 ("widgets", "Blog sidebar widgets", "content", "base", "document360.com/blog", "Blog readers",
  "Five 330 px widgets with the Lotus mascot, each with its own tracked waitlist link.", "widgets.md", None, None, None, "widgets_thumb"),
 ("nl-customers", "Newsletter: existing customers", "email", "base", "Email (Ortto)", "Customers",
  "\u201cYour GitHub sync just went two-way.\u201d Premium HTML email with the new banner.", "nl-customers.md", None, None, "nlcust", "nlcust_thumb"),
 ("community", "Community post", "social", "base", "community.document360.com", "Customers",
  "Two-way GitHub sync announcement that asks members where their docs live today.", "community.md", None, None, None, "gitsync_c"),
 ("ph-prelaunch", "Product Hunt pre-launch plan", "ph", "base", "Product Hunt", "Followers, supporters",
  "Refresh the Document360 page, grow 19 followers to 1,000+, line up 500 supporters.", "ph-prelaunch.md", D360PH, "Open Document360 on Product Hunt", None, "hero"),
 ("portal", "In-portal notifications", "product", "warm", "Portal (Appcues)", "Customers and leads",
  "Five messaging directions shown on the portal, plus the winners for customers and for leads.", "portal.md", None, None, None, "synced"),
 ("nl-leads", "Newsletter: trial and demo leads", "email", "warm", "Email (Ortto)", "Trial and demo leads",
  "\u201cDocs as code. Synced both ways.\u201d Four steps and a side-by-side comparison.", "nl-leads.md", None, None, "nlleads", "nlleads_thumb"),
 ("walkthrough", "Walkthrough video script", "video", "warm", "YouTube, landing page", "Docs teams, customers",
  "Eleven scenes through the real flow: connect, agent prompt, sync, pull request, conflict, audit log.", "walkthrough.md", None, None, None, "agent_c"),
 ("commercial", "45-second commercial", "video", "warm", "Paid video, Product Hunt", "Everyone",
  "\u201cTwo copies? Not anymore.\u201d Nine shots, plus 15-second and 6-second cutdowns.", "commercial.md", None, None, None, "herobare"),
 ("brandvideo", "Brand video: repo to article", "video", "warm", "Social, Product Hunt", "Everyone",
  "A Markdown file and manifest, the article they become, and the edit that travels back as a PR.", "brandvideo.md", None, None, None, "hero"),
 ("paid", "Paid social: 20 ads", "social", "warm", "LinkedIn, Facebook, X", "Docs teams and builders",
  "Twenty descriptions with twenty matching banners, and which to test where.", "paid.md", None, None, None, "herobare"),
 ("influencers", "Influencer program (25 creators)", "influencers", "warm", "Creators\u2019 channels", "Their audiences",
  "Four creator groups including DevRel voices, three waves, the brief, starter posts and tracking.", "influencers.md", None, None, None, "prmenu_c"),
 ("ph-launch", "Product Hunt launch page and maker comment", "ph", "launch", "Product Hunt", "Product Hunt community",
  "Listing, eight-slot gallery, Saravana\u2019s maker comment and the first team replies.", "ph-launch.md", None, None, None, "hero"),
 ("saravana", "Saravana\u2019s launch-day posts", "social", "launch", "LinkedIn, X", "Saravana\u2019s network",
  "A LinkedIn post and a four-part X thread for the hour the launch goes live.", "saravana.md", None, None, None, "merge_c"),
 ("board", "Board members\u2019 LinkedIn posts", "social", "launch", "LinkedIn", "Board networks",
  "Four angles: founder story, customer demand, docs as code for everyone, the agent era.", "board.md", None, None, None, "audit_c"),
 ("runofshow", "Launch-day run of show", "ph", "launch", "Product Hunt, all channels", "Whole team",
  "Hour-by-hour plan in PST and IST, with owners and war-room rules.", "runofshow.md", None, None, None, "syncing_c"),
 ("playbook", "Launch playbook: replies, outreach, follow-up", "ph", "after", "Product Hunt, email, social", "Whole team",
  "Comment reply bank, outreach templates and post-launch steps, including the extension migration.", "playbook.md", None, None, None, "profile_c"),
]

CATS = [("all", "All assets"), ("strategy", "Strategy"), ("product", "Product and in-app"), ("ph", "Product Hunt"),
        ("content", "Content and SEO"), ("email", "Email"), ("video", "Video"), ("social", "Social and paid"),
        ("influencers", "Influencers")]
CAT_LABEL = dict(CATS)
PHASES = [("plan", "Plan"), ("base", "Build the base"), ("warm", "Warm the crowd"), ("launch", "Launch day"), ("after", "Follow-through")]
PHASE_LABEL = dict(PHASES)

ICONS = {
 "strategy": '<path d="M4 19V9M10 19V5M16 19v-7M22 19H2" />',
 "product": '<rect x="3" y="4" width="18" height="16" rx="2" /><path d="M3 9h18M8 14h5" />',
 "ph": '<path d="M12 3l2.6 5.6 6.1.7-4.5 4.2 1.2 6L12 16.6 6.6 19.5l1.2-6L3.3 9.3l6.1-.7z" />',
 "content": '<path d="M5 4h10l4 4v12H5z" /><path d="M14 4v5h5M8 13h8M8 17h6" />',
 "email": '<rect x="3" y="5" width="18" height="14" rx="2" /><path d="M3 7l9 6 9-6" />',
 "video": '<rect x="3" y="5" width="14" height="14" rx="2" /><path d="M17 10l4-2v8l-4-2z" />',
 "social": '<path d="M4 5h16v10H9l-5 4z" />',
 "influencers": '<circle cx="9" cy="8" r="3.2" /><path d="M3 20c0-3.3 2.7-5.6 6-5.6s6 2.3 6 5.6" /><circle cx="17.5" cy="9" r="2.4" /><path d="M16 14.6c2.8.1 5 2 5 4.9" />',
}
def icon(cat, size=18):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[cat]}</svg>'
esc = lambda s: html.escape(s, quote=True)

md_blocks, meta, cards = [], [], []
for a in A:
    aid, title, cat, phase, channel, aud, summ, mdf, link, ll, prev, thumb = a
    text = open(os.path.join(MD, mdf), encoding="utf-8").read()
    assert "</script" not in text.lower()
    for k in re.findall(r'img:([a-z0-9_]+)', text):
        assert k in IMAGES, (mdf, k)
    md_blocks.append(f'<script type="text/plain" id="md-{aid}">{text}</script>')
    meta.append({"id": aid, "title": title, "cat": cat, "catLabel": CAT_LABEL[cat], "phase": phase,
                 "phaseLabel": PHASE_LABEL[phase], "channel": channel, "audience": aud, "summary": summ,
                 "link": link, "linkLabel": ll, "img": prev})
    cards.append(f'''<article class="card" data-cat="{cat}" data-phase="{phase}" data-search="{esc((title+' '+summ+' '+channel+' '+aud+' '+CAT_LABEL[cat]).lower())}">
  <button class="thumb" type="button" data-open="{aid}" aria-label="View full resource: {esc(title)}"><img data-img="{thumb}" alt="" loading="lazy"><span class="cat cat-on-img">{icon(cat, 15)}<span>{esc(CAT_LABEL[cat])}</span></span></button>
  <div class="card-body">
    <span class="phase-tag">{esc(PHASE_LABEL[phase])}</span>
    <h3>{esc(title)}</h3>
    <p class="sum">{esc(summ)}</p>
    <dl class="facts"><div><dt>Channel</dt><dd>{esc(channel)}</dd></div><div><dt>Audience</dt><dd>{esc(aud)}</dd></div></dl>
    <button class="open" type="button" data-open="{aid}" aria-label="View full resource: {esc(title)}">View full resource<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button>
  </div>
</article>''')

counts = {p: sum(1 for a in A if a[3] == p) for p, _ in PHASES}
rail = "".join(f'<button class="phase" type="button" data-phase-filter="{p}" aria-pressed="false"><span class="ph-num">{i:02d}</span><span class="ph-name">{esc(l)}</span><span class="ph-count">{counts[p]} asset{"s" if counts[p]!=1 else ""}</span></button>' for i, (p, l) in enumerate(PHASES, 1))
chips = "".join(f'<button class="chip" type="button" data-cat-filter="{c}" aria-pressed="{"true" if c=="all" else "false"}">{esc(l)}<span>{len(A) if c=="all" else sum(1 for a in A if a[2]==c)}</span></button>' for c, l in CATS)

PILLARS = [
 ("Two-way sync", "Commit in GitHub or edit in Document360. Any branch, any folder.", "connect_c"),
 ("Git in the browser", "Save to branch, open a pull request, Merge & publish.", "prmenu_c"),
 ("Conflicts made human", "Keep inbound, keep yours, or keep both, side by side.", "conflicts_c"),
 ("Agent-ready setup", "Your coding agent writes d360.json from a prompt.", "agent_c"),
]
pillars = "".join(f'<button class="pillar" type="button" data-open="flow"><img data-img="{k}" alt="" loading="lazy"><b>{esc(t)}</b><span>{esc(d)}</span></button>' for t, d, k in PILLARS)

MARKED = open(os.path.join(HERE, "package", "marked.min.js"), encoding="utf-8").read()

CSS = r"""
:root{color-scheme:light;--bg:#f7f6fb;--surface:#fff;--surface-2:#f2eefb;--border:#e4e4e7;--text:#18181b;--muted:#52525b;--accent:#6941c6;--hero-bg:radial-gradient(45% 70% at 80% 45%,rgba(127,86,217,.20),transparent 70%),linear-gradient(180deg,#f2eefb 0%,#fbfaff 100%);--hero-text:#18181b;--hero-muted:#52525b;--hero-line:#e5ddf7;--hero-em:#7f56d9;--hero-grid:#d1d1d6;--accent-ink:#fff;--accent-soft:#ece5ff;--glow:rgba(90,49,214,.12);--code-bg:#efeaf9;--shadow:0 1px 2px rgba(22,19,42,.05),0 8px 24px rgba(22,19,42,.06);box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){color-scheme:dark;--hero-bg:radial-gradient(55% 80% at 82% 40%,rgba(236,72,153,.32),transparent 62%),linear-gradient(135deg,#0d0824,#1d1170 55%,#2a1ab9);--hero-text:#fff;--hero-muted:#d6d0ff;--hero-line:rgba(255,255,255,.14);--hero-em:#c4b5fd;--hero-grid:rgba(255,255,255,.12);--bg:#0b0820;--surface:#141031;--surface-2:#1c1742;--border:#2b2556;--text:#f1eefc;--muted:#aaa3d1;--accent:#a78bfa;--accent-ink:#140c35;--accent-soft:#2a2163;--glow:rgba(167,139,250,.16);--code-bg:#1f1a49;--shadow:0 1px 2px rgba(0,0,0,.3),0 10px 30px rgba(0,0,0,.35)}}
:root[data-theme="dark"]{color-scheme:dark;--hero-bg:radial-gradient(55% 80% at 82% 40%,rgba(236,72,153,.32),transparent 62%),linear-gradient(135deg,#0d0824,#1d1170 55%,#2a1ab9);--hero-text:#fff;--hero-muted:#d6d0ff;--hero-line:rgba(255,255,255,.14);--hero-em:#c4b5fd;--hero-grid:rgba(255,255,255,.12);--bg:#0b0820;--surface:#141031;--surface-2:#1c1742;--border:#2b2556;--text:#f1eefc;--muted:#aaa3d1;--accent:#a78bfa;--accent-ink:#140c35;--accent-soft:#2a2163;--glow:rgba(167,139,250,.16);--code-bg:#1f1a49;--shadow:0 1px 2px rgba(0,0,0,.3),0 10px 30px rgba(0,0,0,.35)}
html{scroll-padding-top:calc(env(safe-area-inset-top,0px) + 84px)}
*,*::before,*::after{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font-family:'Plus Jakarta Sans',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;font-size:16px;line-height:1.55;-webkit-font-smoothing:antialiased}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:30;background:var(--bg)}
a{color:var(--accent)} button{font-family:inherit}
.wrap{max-width:1240px;margin:0 auto;padding:0 24px}
.top{position:sticky;top:env(safe-area-inset-top,0px);z-index:20;background:color-mix(in srgb,var(--bg) 88%,transparent);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1px solid var(--border)}
.top .wrap{display:flex;align-items:center;gap:16px;min-height:68px;flex-wrap:wrap;padding-top:10px;padding-bottom:10px}
.brand{display:flex;align-items:center;gap:12px;margin-right:auto}
.brand img{width:40px;height:40px}
.brand b{display:block;font-size:16px;font-weight:800;letter-spacing:-.2px}
.brand small{display:block;font-size:12.5px;color:var(--muted);font-weight:600}
.search{position:relative;flex:0 1 320px}
.search input{width:100%;height:44px;border-radius:12px;border:1px solid var(--border);background:var(--surface);color:var(--text);padding:0 14px 0 40px;font:inherit;font-size:14.5px}
.search input:focus{outline:2px solid var(--accent);outline-offset:1px}
.search svg{position:absolute;left:13px;top:50%;transform:translateY(-50%);color:var(--muted)}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
.hero{margin:28px 0 0;border-radius:28px;padding:44px 44px 0;color:var(--hero-text);position:relative;overflow:hidden;background:var(--hero-bg);border:1px solid var(--hero-line)}
.hero::after{content:"";position:absolute;inset:0;background-image:radial-gradient(var(--hero-grid) 1px,transparent 1.2px);background-size:22px 22px;opacity:.6;-webkit-mask-image:radial-gradient(70% 80% at 75% 45%,#000 10%,transparent 75%);mask-image:radial-gradient(70% 80% at 75% 45%,#000 10%,transparent 75%);pointer-events:none}
.hero-grid{display:grid;grid-template-columns:1.25fr .75fr;gap:24px;align-items:center;position:relative;z-index:1}
.eyebrow{display:inline-flex;gap:8px;align-items:center;font-size:13px;font-weight:700;color:var(--accent);background:var(--surface);border:1px solid var(--border);padding:6px 12px;border-radius:999px}
.eyebrow i{width:8px;height:8px;border-radius:4px;background:#7f56d9;box-shadow:0 0 0 4px rgba(127,86,217,.2)}
.hero h1{margin:16px 0 12px;font-size:clamp(32px,4.6vw,54px);line-height:1.03;letter-spacing:-1.6px;font-weight:800}
.hero h1 em{font-style:normal;color:var(--hero-em)}
.hero p.lead{margin:0 0 24px;font-size:18px;color:var(--hero-muted);max-width:600px}
.hero-actions{display:flex;gap:12px;flex-wrap:wrap}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:46px;padding:0 20px;border-radius:12px;font-weight:700;font-size:15px;text-decoration:none;cursor:pointer;border:0}
.btn-light{background:var(--accent);color:var(--accent-ink)}.btn-light:hover{filter:brightness(1.08)}
.btn-ghost{background:var(--surface);color:var(--text);border:1px solid var(--border)}.btn-ghost:hover{border-color:var(--accent);color:var(--accent)}
.mascot-wrap{position:relative;display:flex;justify-content:center}
.mascot-wrap img{width:min(300px,100%);height:auto;filter:drop-shadow(0 24px 40px rgba(127,86,217,.35));animation:bob 5s ease-in-out infinite}
@keyframes bob{0%,100%{transform:translateY(0) rotate(-2deg)}50%{transform:translateY(-10px) rotate(2deg)}}
.kpis{position:relative;z-index:1;display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:34px 0 0;padding:20px 0 30px;border-top:1px solid var(--hero-line)}
.kpi b{display:block;font-size:28px;line-height:1.1;font-weight:800;letter-spacing:-.6px}
.kpi span{font-size:13px;color:var(--hero-muted);font-weight:600}
.changed{margin:24px 0 0;display:grid;grid-template-columns:1.1fr .9fr;gap:20px;background:var(--surface);border:1px solid var(--border);border-radius:24px;padding:22px;box-shadow:var(--shadow);align-items:center}
.changed img.hv{width:100%;height:auto;display:block;border-radius:16px}
.changed h2{margin:6px 0 8px;font-size:23px;letter-spacing:-.4px;line-height:1.2}
.changed p{margin:0 0 14px;color:var(--muted);font-size:15px}
.tag{display:inline-block;font-size:12px;font-weight:800;color:var(--accent);background:var(--accent-soft);padding:4px 10px;border-radius:999px}
.vs{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:0 0 14px}
.vs div{border:1px solid var(--border);border-radius:14px;padding:12px 14px;font-size:13.5px;background:var(--surface-2)}
.vs b{display:block;font-size:12px;color:var(--muted);margin-bottom:4px}
.vs .new{border-color:var(--accent);background:var(--accent-soft)}
.vs .new b{color:var(--accent)}
.section-head{display:flex;align-items:baseline;justify-content:space-between;gap:12px;margin:40px 0 14px;flex-wrap:wrap}
.section-head h2{margin:0;font-size:21px;letter-spacing:-.3px}
.section-head p{margin:0;color:var(--muted);font-size:14px}
.pillars{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.pillar{text-align:left;background:var(--surface);border:1px solid var(--border);border-radius:18px;padding:0 0 16px;overflow:hidden;cursor:pointer;color:var(--text);display:flex;flex-direction:column;gap:4px;box-shadow:var(--shadow);transition:transform .18s ease,border-color .18s ease}
.pillar:hover{transform:translateY(-3px);border-color:var(--accent)}
.pillar img{width:100%;aspect-ratio:16/9;object-fit:cover;object-position:top center;display:block;border-bottom:1px solid var(--border);margin-bottom:10px;background:var(--surface-2)}
.pillar b{padding:0 16px;font-size:15.5px}
.pillar span{padding:0 16px;font-size:13.5px;color:var(--muted)}
.rail{display:grid;grid-template-columns:repeat(5,1fr);gap:10px}
.phase{text-align:left;background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:16px;cursor:pointer;color:var(--text);display:flex;flex-direction:column;gap:4px;min-height:96px;position:relative;box-shadow:var(--shadow);transition:transform .15s ease,border-color .15s ease}
.phase:hover{transform:translateY(-2px);border-color:var(--accent)}
.phase[aria-pressed="true"]{border-color:var(--accent);background:var(--accent-soft)}
.ph-num{font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--accent)}
.ph-name{font-weight:800;font-size:15.5px}
.ph-count{font-size:13px;color:var(--muted);font-weight:600}
.phase:not(:last-child)::after{content:"";position:absolute;right:-11px;top:50%;width:12px;height:2px;background:var(--border)}
.chips{display:flex;gap:8px;flex-wrap:wrap;margin:22px 0 18px}
.chip{display:inline-flex;align-items:center;gap:8px;min-height:40px;padding:0 14px;border-radius:999px;border:1px solid var(--border);background:var(--surface);color:var(--text);font-weight:700;font-size:13.5px;cursor:pointer}
.chip span{font-size:12px;color:var(--muted);background:var(--surface-2);border-radius:999px;padding:1px 8px}
.chip[aria-pressed="true"]{background:var(--text);color:var(--bg);border-color:var(--text)}
.chip[aria-pressed="true"] span{background:color-mix(in srgb,var(--bg) 18%,transparent);color:var(--bg)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:18px}
.card{background:var(--surface);border:1px solid var(--border);border-radius:20px;overflow:hidden;display:flex;flex-direction:column;box-shadow:var(--shadow);transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
.card:hover{transform:translateY(-3px);border-color:color-mix(in srgb,var(--accent) 55%,var(--border));box-shadow:0 16px 36px var(--glow)}
.card[hidden]{display:none}
.thumb{position:relative;display:block;padding:0;border:0;background:var(--surface-2);cursor:pointer;aspect-ratio:16/9;overflow:hidden}
.thumb img{width:100%;height:100%;object-fit:cover;object-position:top center;display:block;transition:transform .4s ease}
.card:hover .thumb img{transform:scale(1.04)}
.cat{display:inline-flex;align-items:center;gap:7px;font-size:12.5px;font-weight:700;color:var(--accent);background:var(--accent-soft);padding:5px 10px 5px 8px;border-radius:999px}
.cat-on-img{position:absolute;left:12px;top:12px;background:rgba(255,255,255,.94);color:#3d1aa0;box-shadow:0 2px 8px rgba(0,0,0,.15)}
.card-body{padding:16px 18px 18px;display:flex;flex-direction:column;gap:8px;flex:1}
.phase-tag{font-size:12px;font-weight:700;color:var(--muted)}
.card h3{margin:0;font-size:18px;line-height:1.3;letter-spacing:-.2px}
.sum{margin:0;color:var(--muted);font-size:14.5px}
.facts{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:4px 0 0;padding-top:12px;border-top:1px solid var(--border)}
.facts dt{font-size:11.5px;font-weight:700;color:var(--muted)}
.facts dd{margin:0;font-size:13.5px;font-weight:600}
.open{margin-top:auto;display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:44px;border-radius:12px;border:1px solid var(--border);background:var(--surface-2);color:var(--text);font-weight:700;font-size:14.5px;cursor:pointer}
.open:hover{background:var(--accent);color:var(--accent-ink);border-color:var(--accent)}
.empty{padding:40px;text-align:center;color:var(--muted);border:1px dashed var(--border);border-radius:18px}
footer{margin:48px 0 40px;color:var(--muted);font-size:13px;display:flex;gap:12px;align-items:center}
footer img{width:28px;height:28px}
dialog{width:min(1020px,calc(100vw - 24px));max-height:calc(100dvh - 24px - env(safe-area-inset-top,0px) - env(safe-area-inset-bottom,0px));padding:0;border:1px solid var(--border);border-radius:22px;background:var(--surface);color:var(--text);box-shadow:0 30px 80px rgba(0,0,0,.35)}
dialog::backdrop{background:rgba(10,7,30,.62);backdrop-filter:blur(4px)}
.dlg{display:flex;flex-direction:column;max-height:inherit}
.dlg-head{padding:20px 24px;border-bottom:1px solid var(--border);display:flex;gap:16px;align-items:flex-start}
.dlg-head .t{flex:1;min-width:0}
.dlg-head h2{margin:8px 0 4px;font-size:24px;line-height:1.2;letter-spacing:-.4px}
.dlg-head p{margin:0;color:var(--muted);font-size:14.5px}
.dlg-actions{display:flex;gap:8px;flex-wrap:wrap;padding:12px 24px;border-bottom:1px solid var(--border);background:var(--surface-2)}
.act{display:inline-flex;align-items:center;gap:8px;min-height:40px;padding:0 14px;border-radius:10px;border:1px solid var(--border);background:var(--surface);color:var(--text);font-weight:700;font-size:13.5px;text-decoration:none;cursor:pointer}
.act:hover{border-color:var(--accent);color:var(--accent)}
.act[hidden]{display:none}
.x{width:44px;height:44px;border-radius:12px;border:1px solid var(--border);background:var(--surface);color:var(--text);display:flex;align-items:center;justify-content:center;cursor:pointer;flex-shrink:0}
.dlg-body{overflow:auto;padding:8px 28px 32px}
.md{font-size:15.5px;line-height:1.65}
.md h1{font-size:26px;letter-spacing:-.4px;margin:28px 0 10px}
.md h2{font-size:20px;letter-spacing:-.3px;margin:28px 0 10px}
.md h3{font-size:16.5px;margin:22px 0 8px}
.md p{margin:0 0 12px}
.md ul,.md ol{margin:0 0 14px;padding-left:22px}
.md li{margin:4px 0}
.md hr{border:0;border-top:1px solid var(--border);margin:24px 0}
.md blockquote{margin:12px 0 18px;padding:16px 20px;background:var(--surface-2);border:1px solid var(--border);border-radius:14px}
.md blockquote p:last-child{margin-bottom:0}
.md code{font-family:'JetBrains Mono',monospace;font-size:.88em;background:var(--code-bg);padding:1px 6px;border-radius:6px}
.md pre{background:#120f2a;color:#e6e3f7;padding:16px 18px;border-radius:14px;overflow-x:auto}
.md pre code{background:none;padding:0;color:inherit;font-size:13px}
.md img{display:block;max-width:100%;height:auto;border-radius:14px;border:1px solid var(--border);margin:8px auto 4px}
.md p:has(> img){margin:16px 0 18px}
.md .cap{display:block;text-align:center;font-size:12.5px;color:var(--muted);margin-top:6px}
.table-wrap{overflow-x:auto;margin:8px 0 18px;border:1px solid var(--border);border-radius:14px}
.md table{border-collapse:collapse;width:100%;font-size:14px;min-width:560px}
.md th{text-align:left;font-size:12px;font-weight:800;color:var(--muted);background:var(--surface-2);padding:10px 12px;border-bottom:1px solid var(--border)}
.md td{padding:10px 12px;border-bottom:1px solid var(--border);vertical-align:top}
.md tr:last-child td{border-bottom:0}
.preview{margin:18px 0 6px}
.preview p{font-size:13px;color:var(--muted);margin:0 0 10px}
.preview img{display:block;width:100%;max-width:620px;height:auto;margin:0 auto;border-radius:14px;border:1px solid var(--border)}
/* widget mockups (brand colours, theme independent) */
.wdg-row{display:flex;gap:18px;overflow-x:auto;padding:6px 2px 14px;margin:10px 0 16px;align-items:flex-start}
.wdg{flex:0 0 280px;border-radius:20px;padding:24px 22px;display:flex;flex-direction:column;gap:12px;font-family:'Plus Jakarta Sans',sans-serif;min-height:280px}
.wdg h4{margin:0;font-size:21px;line-height:1.2;letter-spacing:-.3px;font-weight:800}
.wdg p{margin:0;font-size:13.5px;line-height:1.5}
.wdg small{font-size:12px;opacity:.85;text-align:center}
.wdg-grad{color:#fff;align-items:center;text-align:center;background:radial-gradient(120% 90% at 100% 55%,#D8248C 0%,rgba(216,36,140,0) 55%),radial-gradient(110% 90% at 0% 20%,#3B1FD8 0%,rgba(59,31,216,0) 60%),#170F4A}
.wdg-ink{color:#fff;background:#1B1740}
.wdg-light{color:#16132a;background:#F4F1FC;border:1px solid #E2DCF6}
.wdg.tall{min-height:440px}.wdg.compact{min-height:0}
.wdg .wdg-m{width:84px;height:84px;border:0;margin:0 auto;filter:drop-shadow(0 10px 20px rgba(217,70,239,.45))}
.wdg .wdg-m.sm{width:60px;height:60px;margin:0}
.md .wdg img,.md .pmk img{border:0;border-radius:0;margin:0;display:inline-block}
.wdg-eb{display:flex;align-items:center;gap:8px;font-size:13px;font-weight:700;color:#D9D2FF}
.wdg-eb.dark{color:#4B27C9}
.wdg-btn{display:inline-block;padding:11px 20px;border-radius:999px;background:#4B27C9;color:#fff;font-weight:700;font-size:14px;text-align:center;align-self:stretch}
.wdg-btn.light{background:#fff;color:#3A1FA3}
.wdg-grad .wdg-btn{align-self:center}
.wdg-sync{display:flex;align-items:center;gap:8px}
.wdg-repo,.wdg-ed{flex:1;border-radius:10px;padding:10px;font-size:11.5px;display:flex;flex-direction:column;gap:3px}
.wdg-repo{background:#0f1117;border:1px solid #2a2e3a;color:#c9cdd8;font-family:'JetBrains Mono',monospace}
.wdg-repo b{color:#fff}
.wdg-ed{background:#fff;color:#16132a}
.wdg-ed em{font-style:normal;color:#1d7a46;font-weight:700}
.wdg-arrows{font-size:22px;color:#f9a8d4}
.wdg-ba{display:flex;flex-direction:column;gap:8px}
.wdg-ba div{background:#fff;border:1px solid #E2DCF6;border-radius:10px;padding:10px 12px;font-size:12.5px;line-height:1.45}
.wdg-ba em{display:block;font-style:normal;font-weight:800;font-size:11px;margin-bottom:2px}
.wdg-ba .bad{color:#A12F2F}.wdg-ba .good{color:#1F7A4D}
.wdg-role{background:#fff;border:1px solid #E2DCF6;border-radius:10px;padding:10px 12px;font-size:12.5px;display:flex;flex-direction:column}
.wdg-role b{font-size:13.5px}
/* portal mockups */
.pmk{position:relative;height:420px;border-radius:16px;overflow:hidden;border:1px solid var(--border);margin:14px 0 18px;background:#f4f4f6 center top/cover no-repeat;font-family:Inter,'Plus Jakarta Sans',sans-serif;color:#18181b}
.pmk-dim{position:absolute;inset:0;background:rgba(22,18,48,.5)}
.pmk-card{position:absolute;background:#fff;border-radius:16px;box-shadow:0 20px 50px rgba(27,23,64,.3);padding:20px;display:flex;flex-direction:column;gap:10px}
.pmk-card h4{margin:0;font-size:19px;line-height:1.25;font-weight:800;color:#18181b}
.pmk-card p{margin:0;font-size:13.5px;line-height:1.5;color:#3f3a60}
.pmk-card ul{margin:0;padding-left:18px;font-size:13px;color:#2a2650}
.pmk-card small{font-size:11.5px;color:#5e5a7a}
.pmk-card.modal{left:50%;top:50%;transform:translate(-50%,-50%);width:420px}
.pmk-card.slide{right:18px;bottom:18px;width:330px}
.pmk-card.slide.big{width:380px}
.pmk-card.tip{left:42%;top:64px;width:300px}
.pmk-card.hot{right:90px;top:70px;width:300px}
.pmk-eb{display:flex;align-items:center;gap:8px;font-size:12.5px;font-weight:700;color:#5a31d6}
.pmk-btns{display:flex;gap:8px;align-items:center}
.pmk-btns .wdg-btn{align-self:auto;padding:9px 16px;font-size:13px;border-radius:10px;background:#5a31d6}
.pmk-btns .wdg-btn.full{flex:1}
.pmk-ghost{font-size:13px;font-weight:600;color:#3f3a60;padding:9px 10px}
.pmk-shot{width:100%;height:auto;border-radius:10px !important;border:1px solid #eee !important}
.pmk-ring{position:absolute;left:calc(42% + 160px);top:18px;width:84px;height:30px;border-radius:9px;box-shadow:0 0 0 3px rgba(224,66,138,.7),0 0 0 9px rgba(224,66,138,.2)}
.pmk-dot{position:absolute;right:100px;top:40px;width:18px;height:18px;border-radius:9px;background:#E0428A;box-shadow:0 0 0 7px rgba(224,66,138,.25)}
.pmk-banner{position:absolute;left:0;right:0;top:0;display:flex;align-items:center;gap:12px;padding:12px 16px;background:#1B1740;color:#fff}
.pmk-banner p{margin:0;flex:1;font-size:13.5px;color:#D6D1F5}.pmk-banner b{color:#fff}
.pmk-banner .wdg-btn{align-self:auto;padding:9px 14px;font-size:13px;white-space:nowrap}
.pmk-tag{position:absolute;left:12px;bottom:12px;font-size:12px;font-weight:800;background:rgba(17,12,48,.82);color:#fff;padding:5px 10px;border-radius:999px}
.pmk-tag.win{background:#1d7a46}
@media (max-width:980px){.hero-grid,.changed{grid-template-columns:1fr}.mascot-wrap{display:none}.pillars{grid-template-columns:repeat(2,1fr)}.rail{grid-template-columns:repeat(2,1fr)}.phase::after{display:none}.kpis{grid-template-columns:repeat(2,1fr)}}
@media (max-width:600px){.wrap{padding:0 16px}.hero{padding:30px 22px 0;border-radius:22px}.pillars,.rail{grid-template-columns:1fr}.search{flex:1 1 100%}.dlg-body{padding:4px 18px 24px}.dlg-head{padding:16px 18px}.dlg-actions{padding:10px 18px}.vs{grid-template-columns:1fr}.pmk{height:auto;min-height:440px}.pmk-card.modal,.pmk-card.slide,.pmk-card.tip,.pmk-card.hot{left:12px;right:12px;width:auto;transform:none;top:auto;bottom:44px}.pmk-ring,.pmk-dot{display:none}}
@media (prefers-reduced-motion:reduce){*{transition:none !important;animation:none !important}}
"""

JS = r"""
(function(){
  var ASSETS = __META__;
  var IMGS = __IMGS__;
  var ICONS = __ICONS__;
  var byId = {}; ASSETS.forEach(function(a,i){ a.index=i; byId[a.id]=a; });
  function fillImgs(root){
    root.querySelectorAll('img[data-img]').forEach(function(im){ var k=im.getAttribute('data-img'); if(IMGS[k]) im.src=IMGS[k]; });
    root.querySelectorAll('img').forEach(function(im){ var s=im.getAttribute('src')||''; if(s.indexOf('img:')===0 && IMGS[s.slice(4)]) im.src=IMGS[s.slice(4)]; });
    root.querySelectorAll('[data-bg]').forEach(function(el){ var k=el.getAttribute('data-bg'); if(IMGS[k]) el.style.backgroundImage='url("'+IMGS[k]+'")'; });
  }
  fillImgs(document);
  var state={cat:'all',phase:null,q:''};
  var cards=[].slice.call(document.querySelectorAll('.card'));
  var countEl=document.getElementById('count'), emptyEl=document.getElementById('empty');
  function apply(){
    var shown=0;
    cards.forEach(function(c){
      var ok=(state.cat==='all'||c.dataset.cat===state.cat)&&(!state.phase||c.dataset.phase===state.phase)&&(!state.q||c.dataset.search.indexOf(state.q)!==-1);
      c.hidden=!ok; if(ok) shown++;
    });
    countEl.textContent=shown+' of '+cards.length+' shown'; emptyEl.hidden=shown!==0;
  }
  document.querySelectorAll('[data-cat-filter]').forEach(function(b){ b.addEventListener('click',function(){ state.cat=b.dataset.catFilter; document.querySelectorAll('[data-cat-filter]').forEach(function(x){ x.setAttribute('aria-pressed', x===b?'true':'false'); }); apply(); }); });
  document.querySelectorAll('[data-phase-filter]').forEach(function(b){ b.addEventListener('click',function(){ var p=b.dataset.phaseFilter; state.phase=state.phase===p?null:p; document.querySelectorAll('[data-phase-filter]').forEach(function(x){ x.setAttribute('aria-pressed', x.dataset.phaseFilter===state.phase?'true':'false'); }); apply(); document.getElementById('assets').scrollIntoView({behavior:'smooth',block:'start'}); }); });
  document.getElementById('q').addEventListener('input',function(e){ state.q=e.target.value.trim().toLowerCase(); apply(); });

  var dlg=document.getElementById('dlg'), current=null;
  function mdText(id){ var el=document.getElementById('md-'+id); return el?el.textContent:''; }
  function render(text){
    var out=null;
    try{ out=window.marked?window.marked.parse(text,{smartypants:true,mangle:false,headerIds:false}):null; }catch(e){ out=null; }
    if(!out){ var pre=document.createElement('pre'); pre.textContent=text; return pre.outerHTML; }
    return out;
  }
  function post(root){
    root.querySelectorAll('table').forEach(function(t){ if(t.parentNode.classList.contains('table-wrap')) return; var w=document.createElement('div'); w.className='table-wrap'; t.parentNode.insertBefore(w,t); w.appendChild(t); });
    root.querySelectorAll('a[href^="http"],a[href^="/"]').forEach(function(a){ a.target='_blank'; a.rel='noopener'; });
    root.querySelectorAll('p > img[alt]').forEach(function(im){ if(im.closest('.wdg,.pmk')) return; var c=document.createElement('span'); c.className='cap'; c.textContent=im.alt; im.after(c); im.loading='lazy'; });
    fillImgs(root);
  }
  function openAsset(id, fromHash){
    var a=byId[id]; if(!a) return; current=a;
    var cat=document.getElementById('dlg-cat'); cat.innerHTML=ICONS[a.cat]+'<span></span>'; cat.lastChild.textContent=a.catLabel+' \u00b7 '+a.phaseLabel;
    document.getElementById('dlg-title').textContent=a.title;
    document.getElementById('dlg-sum').textContent=a.summary+' Channel: '+a.channel+'. Audience: '+a.audience+'.';
    var body=document.getElementById('dlg-body'); body.innerHTML=render(mdText(a.id));
    if(a.img && IMGS[a.img]){ var f=document.createElement('div'); f.className='preview'; var c=document.createElement('p'); c.textContent='Full email preview (desktop). The HTML file is ready to import into Ortto.'; var im=document.createElement('img'); im.src=IMGS[a.img]; im.alt='Full preview of the '+a.title.toLowerCase(); f.appendChild(c); f.appendChild(im); body.appendChild(f); }
    post(body);
    var link=document.getElementById('dlg-link');
    if(a.link){ link.hidden=false; link.href=a.link; document.getElementById('dlg-link-label').textContent=a.linkLabel; } else link.hidden=true;
    document.getElementById('dlg-copy').lastChild.textContent='Copy text';
    if(!dlg.open) dlg.showModal();
    dlg.querySelector('.dlg-body').scrollTop=0;
    if(!fromHash && location.hash!=='#'+a.id){ try{ location.hash=a.id; }catch(e){} }
  }
  function closeDlg(){ if(dlg.open) dlg.close(); }
  dlg.addEventListener('close',function(){ current=null; if(location.hash){ try{ history.replaceState(null,'',location.pathname+location.search); }catch(e){} } });
  dlg.addEventListener('click',function(e){ if(e.target===dlg) closeDlg(); });
  document.getElementById('dlg-close').addEventListener('click',closeDlg);
  document.getElementById('dlg-prev').addEventListener('click',function(){ if(current) openAsset(ASSETS[(current.index-1+ASSETS.length)%ASSETS.length].id); });
  document.getElementById('dlg-next').addEventListener('click',function(){ if(current) openAsset(ASSETS[(current.index+1)%ASSETS.length].id); });
  document.getElementById('dlg-copy').addEventListener('click',function(){
    if(!current) return; var label=this.lastChild;
    var text=mdText(current.id).replace(/<div[\s\S]*?<\/div>\n?/g,'').replace(/!\[[^\]]*\]\(img:[^)]+\)\n?/g,'');
    function done(ok){ label.textContent=ok?'Copied':'Copy failed, select the text instead'; setTimeout(function(){ label.textContent='Copy text'; },1800); }
    try{ if(navigator.clipboard&&navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(function(){done(true);},function(){done(false);}); else done(false); }catch(e){ done(false); }
  });
  document.addEventListener('click',function(e){ var t=e.target.closest?e.target.closest('[data-open]'):null; if(!t) return; var id=t.getAttribute('data-open'), a=byId[id]; if(a && a.link && a.link.charAt(0)==='/' && !t.closest('dialog')){ window.open(a.link,'_blank','noopener'); return; } openAsset(id); });
  function fromHash(){ var id=(location.hash||'').replace('#',''); if(id&&byId[id]) openAsset(id,true); else if(!id) closeDlg(); }
  window.addEventListener('hashchange',fromHash);
  apply(); fromHash();
})();
"""
JS = JS.replace("__META__", json.dumps(meta)).replace("__IMGS__", json.dumps(IMAGES)).replace("__ICONS__", json.dumps({k: icon(k, 16) for k in ICONS}))

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Document360 Lotus · GTM command center</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&family=Inter:wght@400;600;700;800&display=swap">
<script>{MARKED}</script>
<style>{CSS}</style>
</head>
<body>
<header class="top"><div class="wrap">
  <div class="brand"><img src="{IMAGES['mascot']}" alt="Lotus mascot"><div><b>Lotus GTM command center</b><small>Document360 · docs as code launch</small></div></div>
  <div class="search"><label class="sr" for="q">Search assets</label>
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
    <input id="q" type="search" placeholder="Search assets, channels, audiences" autocomplete="off"></div>
</div></header>

<main class="wrap">
  <section class="hero" aria-labelledby="hero-title">
    <div class="hero-grid">
      <div>
        <span class="eyebrow"><i></i>Document360 - Lotus · docs as code</span>
        <h1 id="hero-title">Docs as code, <em>synced both ways.</em></h1>
        <p class="lead">Lotus keeps your docs in a GitHub repo and in Document360, in sync in both directions. Every launch asset below tells that story, with visuals built from the Lotus design.</p>
        <div class="hero-actions">
          <button class="btn btn-light" type="button" data-open="flow">Take the product tour</button>
          <button class="btn btn-ghost" type="button" data-open="overview">Open the plan at a glance</button>
        </div>
      </div>
      <div class="mascot-wrap"><img src="{MASCOT_BIG}" alt="The Lotus mascot"></div>
    </div>
    <div class="kpis" aria-label="Plan in numbers">
      <div class="kpi"><b>{len(A)}</b><span>launch assets, all updated</span></div>
      <div class="kpi"><b>#1</b><span>goal in Knowledge base software</span></div>
      <div class="kpi"><b>25</b><span>creators in the influencer program</span></div>
      <div class="kpi"><b>100+</b><span>repositories connected in launch month</span></div>
    </div>
  </section>

  <section class="changed" aria-labelledby="changed-title">
    <img class="hv" data-img="herobare" alt="A GitHub repository and a Document360 article kept in sync both ways by Lotus">
    <div>
      <span class="tag">What changed</span>
      <h2 id="changed-title">Lotus is now docs as code</h2>
      <div class="vs"><div><b>Before</b>Lotus drafted docs from code, for review</div><div class="new"><b>Now</b>Lotus syncs a GitHub repo and Document360, both ways</div></div>
      <p>Developers commit Markdown and review in pull requests. Writers and PMs edit in Document360. Branches, Merge &amp; publish and conflict resolution all work in the editor.</p>
      <button class="btn btn-light" type="button" data-open="competitive">See the competitive landscape</button>
    </div>
  </section>

  <div class="section-head"><h2>The four pillars</h2><p>Each one is proved by a screen in the Lotus design.</p></div>
  <div class="pillars">{pillars}</div>

  <div class="section-head"><h2>The five phases</h2><p>Select a phase to see what goes out in it.</p></div>
  <nav class="rail" aria-label="Phases">{rail}</nav>

  <div class="section-head" id="assets"><h2>Assets</h2><p id="count" aria-live="polite"></p></div>
  <div class="chips" role="group" aria-label="Filter by type">{chips}</div>
  <section class="grid" id="grid">{''.join(cards)}</section>
  <p class="empty" id="empty" hidden>No assets match. Clear the search or pick another filter.</p>

  <footer><img src="{IMAGES['mascot']}" alt="">Screenshots come from the Lotus docs-as-code design. Newsletter HTML files and the new banner image are shared separately in chat.</footer>
</main>

<dialog id="dlg" aria-labelledby="dlg-title"><div class="dlg">
  <div class="dlg-head"><div class="t"><span class="cat" id="dlg-cat"></span><h2 id="dlg-title"></h2><p id="dlg-sum"></p></div>
    <button class="x" type="button" id="dlg-close" aria-label="Close"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div>
  <div class="dlg-actions">
    <button class="act" type="button" id="dlg-copy"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/></svg><span>Copy text</span></button>
    <a class="act" id="dlg-link" href="#" target="_blank" rel="noopener" hidden><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 4h6v6M20 4l-9 9M19 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h5"/></svg><span id="dlg-link-label"></span></a>
    <button class="act" type="button" id="dlg-prev">Previous</button>
    <button class="act" type="button" id="dlg-next">Next</button>
  </div>
  <div class="dlg-body"><div class="md" id="dlg-body"></div></div>
</div></dialog>

{''.join(md_blocks)}
<script>{JS}</script>
</body>
</html>
'''
with open(OUT, "w", encoding="utf-8") as fh:
    fh.write(page)
print(OUT, len(page)//1024, "KB")
