# -*- coding: utf-8 -*-
"""Document360 Lotus waitlist landing page: docs as code, two-way GitHub sync.
Inline styles only, DDS tokens (Inter, primary #7f56d9). Images are placeholders {{IMG:key}}."""

P = "#7f56d9"; P6 = "#6941c6"; P7 = "#4c3482"; P50 = "#f2eefb"; P100 = "#e5ddf7"; P200 = "#ccbbf0"; P300 = "#b29ae8"
N9 = "#18181b"; N7 = "#3e3e46"; N5 = "#5f5f69"; N3 = "#d1d1d6"; N2 = "#e4e4e7"; N1 = "#f4f4f5"; N05 = "#fafafa"
F = "font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif;"
W = 1440
CTA = "Join the waitlist"
MICRO = "Be among the first to experience it. Early access spots are limited."

D360 = f'<svg width="28" height="27" viewBox="0 0 29 28" fill="{P}" aria-hidden="true"><path d="M23.4 2.3C20.2.4 16.6.6 16.6.6H5.8L2.5 17l5.9 4.1 3.1-14.3h4.3c.8 0 1.5.1 2.1.2.6-2.6 2.8-4.5 5.5-4.6z"></path><path d="M23.7 14.4c-1 0-2-.3-2.9-.7-.1 1.3-.4 2.3-.4 2.3-2 5.4-6.4 5.1-6.4 5.1H8.9L.5 27.2h12.8c8.4-.3 11.7-5.6 11.7-5.6 2.4-3.2 3.1-6.6 3.2-9.2-1.1 1.2-2.7 2-4.5 2z"></path><circle cx="23.7" cy="8.3" r="4"></circle></svg>'
GH = f'<svg width="22" height="22" viewBox="0 0 16 16" fill="{N9}" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>'
PR = '<svg width="22" height="22" viewBox="0 0 16 16" fill="#1d7a46" aria-hidden="true"><path d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v5.256a2.251 2.251 0 101.5 0V5.372zM4.25 12a.75.75 0 100 1.5.75.75 0 000-1.5zm7.5-9.5V4h.75a.75.75 0 01.75.75v6.128a2.251 2.251 0 101.5 0V4.75A2.25 2.25 0 0012.5 2.5h-.75V1L9.5 2.75 11.75 4.5z"></path></svg>'

def check(color=P6):
    return f'<svg width="20" height="20" viewBox="0 0 20 20" fill="none" aria-hidden="true" style="flex-shrink: 0; margin-top: 2px"><circle cx="10" cy="10" r="9" fill="{P50}"></circle><path d="M6 10.3l2.6 2.6L14 7.5" stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"></path></svg>'

def icon(path):
    return f'<span style="display: flex; width: 44px; height: 44px; border-radius: 12px; background: {P50}; align-items: center; justify-content: center; flex-shrink: 0"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="{P6}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{path}</svg></span>'

ICON = {
 "sync": '<path d="M4 9a8 8 0 0 1 14-3l2 2"></path><path d="M20 4v4h-4"></path><path d="M20 15a8 8 0 0 1-14 3l-2-2"></path><path d="M4 20v-4h4"></path>',
 "branch": '<circle cx="6" cy="5" r="2.2"></circle><circle cx="6" cy="19" r="2.2"></circle><circle cx="18" cy="7" r="2.2"></circle><path d="M6 7.2v9.6M18 9.2c0 4-4 4.8-12 7.6"></path>',
 "status": '<circle cx="12" cy="12" r="9"></circle><path d="M8 12.5l2.7 2.7L16 9.8"></path>',
 "spark": '<path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9z"></path><path d="M19 16l.8 2.2L22 19l-2.2.8L19 22l-.8-2.2L16 19l2.2-.8z"></path>',
 "user": '<circle cx="12" cy="8" r="4"></circle><path d="M4 21c0-4 3.6-6.5 8-6.5s8 2.5 8 6.5"></path>',
 "log": '<rect x="4" y="3" width="16" height="18" rx="2"></rect><path d="M8 8h8M8 12h8M8 16h5"></path>',
 "kb": '<path d="M4 5a2 2 0 0 1 2-2h12v16H6a2 2 0 0 0-2 2z"></path><path d="M4 21V5M9 8h6"></path>',
 "code": '<path d="M8 8l-4 4 4 4M16 8l4 4-4 4M14 5l-4 14"></path>',
 "pen": '<path d="M4 20h4L19 9l-4-4L4 16z"></path><path d="M13.5 6.5l4 4"></path>',
 "chart": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"></path>',
 "lock": '<rect x="5" y="11" width="14" height="10" rx="2"></rect><path d="M8 11V8a4 4 0 0 1 8 0v3"></path>',
 "repo": '<path d="M5 4h11l3 3v13H5z"></path><path d="M9 4v5h6"></path><path d="M9 14h6M9 17h4"></path>',
 "shield": '<path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6z"></path><path d="M8.5 12l2.4 2.4L15.5 10"></path>',
 "layers": '<path d="M12 3l9 5-9 5-9-5z"></path><path d="M3 13l9 5 9-5"></path>',
 "verify": '<circle cx="12" cy="12" r="9"></circle><path d="M12 7v6M12 16.5v.5"></path>',
}

def btn(label=CTA, href="#waitlist", size="lg"):
    pad = "0 26px" if size == "lg" else "0 18px"; h = "52px" if size == "lg" else "42px"; fs = "16px" if size == "lg" else "14.5px"
    return f'<a href="{href}" style="display: inline-flex; align-items: center; justify-content: center; height: {h}; padding: {pad}; border-radius: 12px; background: {P6}; color: #ffffff; font-size: {fs}; font-weight: 600; text-decoration: none; white-space: nowrap">{label}</a>'

def form(idsuffix):
    return f'''<form id="waitlist{idsuffix}" action="https://document360v2.wpengine.com/lotus-waitlist-2/" method="get" style="width: 100%; display: flex; flex-direction: column; gap: 12px; align-items: center">
<div style="display: flex; flex-wrap: wrap; gap: 10px; width: 100%; max-width: 560px; box-sizing: border-box; padding: 6px; background: #ffffff; border: 1px solid {N2}; border-radius: 16px; box-shadow: 0 1px 2px rgba(24,24,27,.05), 0 10px 30px rgba(76,52,130,.10)">
<label for="email{idsuffix}" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">Work email</label>
<input id="email{idsuffix}" name="email" type="email" required placeholder="you@company.com" style="flex: 1 1 220px; min-width: 0; height: 50px; border: 0; padding: 0 14px; font-family: inherit; font-size: 16px; color: {N9}; background: transparent; outline-offset: 2px; border-radius: 10px">
<button type="submit" style="height: 50px; padding: 0 24px; border: 0; border-radius: 12px; background: {P6}; color: #ffffff; font-family: inherit; font-size: 16px; font-weight: 600; cursor: pointer; white-space: nowrap">{CTA}</button>
</div>
<p style="margin: 0; font-size: 14px; color: {N5}">{MICRO}</p>
</form>'''

def eyebrow(text):
    return f'<span style="display: inline-flex; align-items: center; gap: 8px; align-self: center; font-size: 14px; font-weight: 600; color: {P7}; background: #ffffff; border: 1px solid {P100}; padding: 6px 14px; border-radius: 999px"><span style="width: 8px; height: 8px; border-radius: 4px; background: {P}"></span>{text}</span>'

def kicker(text, center=False):
    al = "text-align: center; align-self: center;" if center else ""
    return f'<p style="margin: 0; {al} font-size: 14px; font-weight: 600; color: {P6}; letter-spacing: .2px">{text}</p>'

def shead(k, h, l=None, w=820):
    inner = kicker(k, True) + h2(h, True, w) + (lead(l) if l else "")
    return f'<div style="display: flex; flex-direction: column; gap: 16px; align-items: center">{inner}</div>'

def h2(text, center=True, w=760):
    al = "text-align: center; align-self: center;" if center else ""
    return f'<h2 style="margin: 0; {al} max-width: {w}px; font-size: clamp(30px, 4vw, 44px); line-height: 1.12; font-weight: 700; letter-spacing: -1.1px; color: {N9}">{text}</h2>'

def lead(text, center=True, w=720):
    al = "text-align: center; align-self: center;" if center else ""
    return f'<p style="margin: 0; {al} max-width: {w}px; font-size: 18px; line-height: 1.6; color: {N5}">{text}</p>'

def shot(key, alt, h=None, pos="top center"):
    hh = f"height: {h}px; object-fit: cover; object-position: {pos};" if h else "height: auto;"
    return f'<img src="{{{{IMG:{key}}}}}" alt="{alt}" style="display: block; width: 100%; {hh} border-radius: 14px; border: 1px solid {N2}">'

def row(f, text):
    return f'<div style="display: flex; gap: 10px; align-items: center; font-size: 16px; line-height: 34px; color: {N7}; {f}">{text}</div>'

FOLD = f'<span style="width: 18px; height: 14px; border-radius: 3px; background: {P}; flex-shrink: 0"></span>'
FOLDB = '<span style="width: 18px; height: 14px; border-radius: 3px; background: #60a5fa; flex-shrink: 0"></span>'
DOC = f'<span style="width: 14px; height: 17px; border-radius: 2px; border: 1.6px solid #a0a0aa; flex-shrink: 0; background: #ffffff"></span>'
DOCP = f'<span style="width: 14px; height: 17px; border-radius: 2px; border: 1.6px solid {P}; flex-shrink: 0; background: #ffffff"></span>'
ON = f"background: {P50}; color: {P7}; font-weight: 600; border-radius: 8px; margin: 0 -8px; padding-right: 8px;"
CARD = f"position: absolute; background: #ffffff; border: 1px solid {N2}; border-radius: 16px; box-shadow: 0 1px 2px rgba(24,24,27,.05), 0 12px 32px rgba(76,52,130,.10);"

def sync_visual():
    # Document360 <------> Lotus <------> GitHub. One line per side, an arrowhead at both ends.
    lab = f"position: absolute; font-size: 13px; font-weight: 600; color: {N5}; letter-spacing: .2px"
    two = f'<svg width="34" height="10" viewBox="0 0 34 10" fill="none" aria-hidden="true"><path d="M5 5h24M6 1L1 5l5 4M28 1l5 4-5 4" stroke="{P6}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"></path></svg>'
    card = f"position: relative; background: #ffffff; border: 1px solid {N2}; border-radius: 16px; box-shadow: 0 1px 2px rgba(24,24,27,.05), 0 12px 32px rgba(76,52,130,.10);"
    return f'''<div style="width: 100%; overflow-x: auto; display: flex"><div style="position: relative; flex: 0 0 1080px; width: 1080px; height: 440px; margin: 0 auto; border-radius: 28px; background: radial-gradient(40% 55% at 50% 48%, rgba(127,86,217,.14), rgba(127,86,217,0) 70%), rgba(250,250,250,.85); border: 1px solid {N2}; overflow: hidden">
<svg width="1080" height="440" viewBox="0 0 1080 440" fill="none" aria-hidden="true" style="position: absolute; left: 0; top: 0; z-index: 2; pointer-events: none">
<defs><marker id="lpa" viewBox="0 0 12 12" refX="11" refY="6" markerUnits="userSpaceOnUse" markerWidth="16" markerHeight="16" orient="auto-start-reverse"><path d="M1 1L11 6L1 11z" fill="{P6}"></path></marker></defs>
<path d="M352 214 L 458 214" stroke="{P300}" stroke-width="3" stroke-linecap="round" marker-start="url(#lpa)" marker-end="url(#lpa)"></path>
<path d="M622 214 L 728 214" stroke="{P300}" stroke-width="3" stroke-linecap="round" marker-start="url(#lpa)" marker-end="url(#lpa)"></path>
<circle cx="388" cy="214" r="4.5" fill="{P}"></circle><circle cx="422" cy="214" r="4.5" fill="#f472b6"></circle><circle cx="658" cy="214" r="4.5" fill="#f472b6"></circle><circle cx="692" cy="214" r="4.5" fill="{P}"></circle>
</svg>
<span style="{lab}; left: 44px; top: 46px">Document360</span>
<div style="{CARD} left: 40px; top: 70px; width: 304px; padding: 14px 18px">
<div style="display: flex; align-items: center; gap: 10px; font-size: 17px; font-weight: 600; color: {N9}; padding-bottom: 10px; border-bottom: 1px solid {N1}; margin-bottom: 4px">{D360}Categories<span style="margin-left: auto; display: inline-flex; align-items: center; gap: 6px; font-size: 12.5px; font-weight: 600; color: #1d7a46; background: #ecf8f1; border: 1px solid #c6ecd5; border-radius: 999px; padding: 3px 10px"><span style="width: 7px; height: 7px; border-radius: 4px; background: #22a05a"></span>Synced</span></div>
{row(f"font-weight: 600; color: {N9};", FOLD + "Getting started")}
{row("padding-left: 28px;", DOC + "Overview")}
{row(ON + "padding-left: 36px;", DOCP + "Quick start")}
{row(f"font-weight: 600; color: {N9};", FOLD + "API reference")}
{row("padding-left: 28px;", DOC + "Webhooks")}
{row("padding-left: 28px;", DOC + "Rate limits")}
</div>
<span style="{lab}; left: 540px; top: 92px; transform: translateX(-50%); color: {P7}">Lotus</span>
<div style="position: absolute; left: 540px; top: 214px; width: 220px; height: 220px; margin-left: -110px; margin-top: -110px; border-radius: 50%; background: radial-gradient(circle, rgba(204,187,240,.8) 0%, rgba(229,221,247,.45) 45%, rgba(242,238,251,0) 70%); display: flex; align-items: center; justify-content: center"><img src="{{{{IMG:mascot}}}}" alt="Lotus" style="width: 128px; height: 128px; filter: drop-shadow(0 12px 22px rgba(127,86,217,.35))"></div>
<span style="{lab}; left: 740px; top: 46px">GitHub</span>
<div style="position: absolute; left: 736px; top: 70px; width: 312px; display: flex; flex-direction: column; gap: 12px">
<div style="{card} padding: 14px 18px">
<div style="display: flex; align-items: center; gap: 10px; font-size: 17px; font-weight: 600; color: {N9}; padding-bottom: 8px; border-bottom: 1px solid {N1}; margin-bottom: 4px">{GH}acme/docs<span style="margin-left: auto; font-size: 12px; font-weight: 600; color: {N7}; background: {N1}; border: 1px solid {N2}; border-radius: 7px; padding: 2px 8px">main</span></div>
{row(f"font-weight: 600; color: {N9};", FOLDB + "docs")}
{row(ON + "padding-left: 36px;", DOCP + "quick-start.md")}
{row("padding-left: 28px;", DOC + "api-reference.md")}
{row("padding-left: 28px;", DOC + "d360.json")}
</div>
<div style="{card} padding: 12px 18px; display: flex; align-items: center; gap: 12px">{PR}<div style="display: flex; flex-direction: column"><span style="font-size: 16px; font-weight: 600; color: {N9}">#122 Quick start</span><span style="font-size: 13px; color: {N5}">draft-oct-20 → main</span></div><span style="margin-left: auto; font-size: 13px; font-weight: 600; color: #ffffff; background: {P6}; border-radius: 999px; padding: 4px 12px">Merged</span></div>
</div>
<span style="position: absolute; left: 540px; top: 388px; transform: translateX(-50%); display: inline-flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 600; color: {P7}; background: #ffffff; border: 1px solid {P100}; border-radius: 999px; padding: 6px 16px; white-space: nowrap">Document360 {two} Lotus {two} GitHub</span>
</div></div>'''


def section(inner, bg="#ffffff", pad="112px clamp(20px, 8vw, 120px)", gap=48, idattr=""):
    return f'<section {idattr} style="background: {bg}; padding: {pad}; display: flex; flex-direction: column; gap: {gap}px">{inner}</section>'

def build():
    out = []
    # NAV
    out.append(f'''<header style="min-height: 76px; padding: 12px clamp(20px, 8vw, 120px); display: flex; flex-wrap: wrap; align-items: center; gap: 16px 36px; border-bottom: 1px solid {N2}; background: rgba(255,255,255,.9)">
<a href="#" aria-label="Document360 Lotus home" style="display: flex; align-items: center; gap: 12px; text-decoration: none; color: {N9}"><img src="{{{{IMG:wordmark}}}}" alt="Document360" style="display: block; width: 162px; height: 21px"><span style="font-size: 12.5px; font-weight: 600; color: {P7}; background: {P50}; border: 1px solid {P100}; border-radius: 999px; padding: 3px 10px">Lotus</span></a>
<nav aria-label="Page" style="display: flex; flex-wrap: wrap; gap: 8px 28px; font-size: 15px; font-weight: 500"><a href="#how" style="color: {N7}; text-decoration: none">How it works</a><a href="#teams" style="color: {N7}; text-decoration: none">For teams</a><a href="#faq" style="color: {N7}; text-decoration: none">FAQ</a></nav>
<span style="flex-grow: 1"></span>{btn(size="sm")}
</header>''')
    # HERO
    chips = "".join(f'<span style="font-size: 14px; font-weight: 500; color: {N7}; background: #ffffff; border: 1px solid {N2}; border-radius: 999px; padding: 6px 14px">{t}</span>' for t in ["Two-way GitHub sync", "Any branch, any folder", "No GitHub account for writers", "Pull requests in the editor", "Conflicts resolved in the browser"])
    out.append(f'''<section style="position: relative; overflow: hidden; background: #ffffff; padding: 88px clamp(20px, 8vw, 120px) 104px">
<div ref="{{{{ setAsciiHost }}}}" aria-hidden="true" style="position: absolute; left: 0; right: 0; top: 0; height: 760px; overflow: hidden; pointer-events: none"><canvas ref="{{{{ setAsciiCanvas }}}}" aria-hidden="true" style="position: absolute; left: 0; top: 0; display: block; width: 100%; height: 100%"></canvas></div>
<div style="position: relative; z-index: 1; display: flex; flex-direction: column; gap: 28px">
{eyebrow("Document360 Lotus · Beta · Docs as code")}
<h1 style="margin: 0; text-align: center; align-self: center; max-width: 1180px; font-size: clamp(40px, 6vw, 72px); line-height: 1.04; font-weight: 700; letter-spacing: -2.4px; color: {N9}">Docs as code, <span style="color: {P}">synced both ways</span></h1>
<p style="margin: 0; text-align: center; align-self: center; font-size: clamp(19px, 2vw, 24px); line-height: 1.45; font-weight: 500; color: {N7}">Your docs in GitHub. Your team in Document360. Always in sync.</p>
{form("")}
<div style="display: flex; gap: 10px; justify-content: center; flex-wrap: wrap">{chips}</div>
<div style="height: 8px"></div>
{sync_visual()}
</div>
</section>''')
    # PROBLEM
    out.append(section(f'''{shead("The problem", "Most teams keep two copies of every doc", "Developers keep Markdown in the repo. Everyone else keeps a pasted copy in the help center. Every release, the two drift further apart.")}
<div style="display: flex; flex-wrap: wrap; gap: 24px">
<div style="flex: 1 1 320px; background: #ffffff; border: 1px solid {N2}; border-radius: 20px; padding: 32px; box-shadow: 0 1px 2px rgba(24,24,27,.04), 0 18px 40px rgba(76,52,130,.08); display: flex; flex-direction: column; gap: 14px">
<span style="align-self: flex-start; font-size: 13px; font-weight: 700; color: #a12f2f; background: #fdeeee; border-radius: 999px; padding: 4px 12px">Without Lotus</span>
<p style="margin: 0; font-size: 24px; line-height: 1.3; font-weight: 600; color: {N9}">Two sources of truth, and neither is right for long</p>
{"".join(f'<div style="display: flex; gap: 10px; font-size: 16px; line-height: 1.5; color: {N7}"><span style="color: #a12f2f; font-weight: 700">✕</span>{t}</div>' for t in ["Writers can't fix a typo without a developer or a terminal", "Changes in GitHub get copied into the help center by hand", "Edits in the help center never make it back to the repo", "Nobody knows which version is current"])}
</div>
<div style="flex: 1 1 320px; background: linear-gradient(180deg, #ffffff 0%, {P50} 100%); border: 1px solid {P200}; border-radius: 20px; padding: 32px; box-shadow: 0 1px 2px rgba(24,24,27,.04), 0 18px 40px rgba(76,52,130,.12); display: flex; flex-direction: column; gap: 14px">
<span style="align-self: flex-start; font-size: 13px; font-weight: 700; color: #ffffff; background: {P6}; border-radius: 999px; padding: 4px 12px">With Lotus</span>
<p style="margin: 0; font-size: 24px; line-height: 1.3; font-weight: 600; color: {N9}">One source of truth, two ways to edit it</p>
{"".join(f'<div style="display: flex; gap: 10px; font-size: 16px; line-height: 1.5; color: {N7}">{check()}<span>{t}</span></div>' for t in ["Developers commit and review in GitHub, like they already do", "Writers and PMs edit in the Document360 editor", "Every change syncs to the other side automatically", "The repo and the knowledge base always match"])}
</div>
</div>''', bg="radial-gradient(#ddd3f5 1px, rgba(0,0,0,0) 1.4px) 0 0 / 24px 24px, linear-gradient(180deg, #faf8ff 0%, #f1ecfc 100%)"))
    # HOW IT WORKS
    steps = [("01", "Choose Lotus", "Start a new project and pick Document360 Lotus, the docs-as-code project type.", "step1_c", "Step 1: choosing Document360 Lotus"),
             ("02", "Connect GitHub", "Authorize GitHub, install the app, and pick any repository and branch. Docs in a subfolder work too.", "connect_c", "Connect with GitHub, repository and branch selected"),
             ("03", "Sync and keep working", "Commit in GitHub or edit in Document360. The Git status shows Synced the moment both sides match.", "synced_c", "Document360 editor with the Synced status")]
    cards = "".join(f'''<div style="flex: 1 1 300px; display: flex; flex-direction: column; gap: 14px; background: #ffffff; border: 1px solid {N2}; border-radius: 20px; padding: 16px 16px 24px">
{shot(k, alt, h=180)}
<div style="display: flex; flex-direction: column; gap: 8px; padding: 4px 8px 0"><span style="font-size: 13px; font-weight: 700; color: {P6}; font-family: 'IBM Plex Mono', monospace">{n}</span><span style="font-size: 20px; font-weight: 600; color: {N9}">{t}</span><span style="font-size: 15px; line-height: 1.55; color: {N5}">{d}</span></div></div>''' for n, t, d, k, alt in steps)
    node = lambda n: f'<span style="display: flex; flex-shrink: 0; width: 44px; height: 44px; border-radius: 22px; background: {P6}; color: #ffffff; align-items: center; justify-content: center; font-size: 16px; font-weight: 700; box-shadow: 0 0 0 6px {P100}">{n}</span>'
    line = f'<span style="flex: 1 1 0; height: 2px; background: repeating-linear-gradient(90deg, {P300} 0 8px, rgba(0,0,0,0) 8px 14px)"></span>'
    timeline = f'<div aria-hidden="true" style="display: flex; align-items: center; gap: 12px; width: 100%; max-width: 980px; align-self: center; padding: 0 12%; box-sizing: border-box">{node("1")}{line}{node("2")}{line}{node("3")}</div>'
    out.append(section(f'''{shead("How it works", "From your repo to a live knowledge base in three steps")}{timeline}<div style="display: flex; flex-wrap: wrap; gap: 20px">{cards}</div>''', bg="radial-gradient(50% 60% at 50% 0%, rgba(127,86,217,.10), rgba(127,86,217,0) 70%), #ffffff", idattr='id="how"'))
    # ENTERPRISE
    ent = [("lock", "Access by workspace and role", "Content access is set per workspace, and every action follows the person's Document360 role. GitHub permissions never grant access in Document360."),
           ("repo", "Only the repositories you choose", "The Document360 Lotus GitHub App is installed on the repositories you select, and nothing else."),
           ("shield", "Your review rules, respected", "Protected branches publish through a pull request, with optional auto-merge once reviews and checks pass."),
           ("log", "Every Git event on record", "The audit log shows pushes, branches, pull requests, merges and conflicts, filterable by source and workspace, with CSV export."),
           ("layers", "Workspaces at scale", "Each workspace connects to its own repository, branch and docs folder, so many products can share one setup."),
           ("verify", "No half-finished imports", "Every sync checks the whole commit first. If anything fails, nothing is imported, and you get each file, line and reason.")]
    et = "".join(f'<div style="display: flex; flex-direction: column; gap: 14px; background: rgba(255,255,255,.06); border: 1px solid rgba(255,255,255,.14); border-radius: 20px; padding: 28px"><span style="display: flex; width: 44px; height: 44px; border-radius: 12px; background: rgba(255,255,255,.10); align-items: center; justify-content: center"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c4b5fd" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[ic]}</svg></span><span style="font-size: 19px; font-weight: 600; color: #ffffff">{h}</span><span style="font-size: 15.5px; line-height: 1.55; color: #d6d0f5">{d}</span></div>' for ic, h, d in ent)
    out.append(f'''<section id="enterprise" style="position: relative; overflow: hidden; padding: 112px clamp(20px, 8vw, 120px); display: flex; flex-direction: column; gap: 48px; background: radial-gradient(55% 70% at 88% 0%, rgba(236,72,153,.22), rgba(0,0,0,0) 60%), linear-gradient(rgba(255,255,255,.045) 1px, rgba(0,0,0,0) 1px) 0 0 / 40px 40px, linear-gradient(90deg, rgba(255,255,255,.045) 1px, rgba(0,0,0,0) 1px) 0 0 / 40px 40px, linear-gradient(135deg, #0d0824 0%, #1d1170 60%, #2a1ab9 100%)">
<div style="display: flex; flex-direction: column; gap: 16px; align-items: center">
<p style="margin: 0; text-align: center; font-size: 14px; font-weight: 600; color: #c4b5fd; letter-spacing: .2px">Enterprise-ready</p>
<h2 style="margin: 0; text-align: center; max-width: 820px; font-size: clamp(30px, 4vw, 44px); line-height: 1.12; font-weight: 700; letter-spacing: -1.1px; color: #ffffff">Built for teams that run docs at scale</h2>
<p style="margin: 0; text-align: center; max-width: 720px; font-size: 18px; line-height: 1.6; color: #d6d0f5">Governance, access and review controls that engineering, security and docs leaders expect, from the first sync.</p>
</div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 20px">{et}</div>
<div style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center">{"".join(f'<span style="font-size: 14px; font-weight: 600; color: #e9e3ff; background: rgba(255,255,255,.08); border: 1px solid rgba(255,255,255,.18); border-radius: 999px; padding: 6px 14px">{t}</span>' for t in ["GitHub", "Two-way sync", "Pull requests", "Audit log", "Role-based access", "Beta"])}</div>
</section>''')
    # COMPARISON
    rows = [("Sync direction", "GitHub to Document360 only", "Both ways"),
            ("Branches", "Main branch only", "Any branch, plus working branches and pull requests"),
            ("Folder structure", "Fixed docs/ folder", "Any subdirectory, mapped by d360.json"),
            ("Edits in Document360", "Stay in Document360", "Become commits and pull requests"),
            ("Conflicts", "Not handled", "Resolved side by side in the editor")]
    tr = "".join(f'<div style="display: flex; border-top: 1px solid {N2}"><div style="flex: 0 0 28%; padding: 18px 24px; font-size: 16px; font-weight: 600; color: {N9}">{a}</div><div style="flex: 1 1 0; padding: 18px 24px; font-size: 16px; color: {N5}">{b}</div><div style="flex: 1 1 0; padding: 18px 24px; font-size: 16px; font-weight: 600; color: {P7}; background: {P50}">{c}</div></div>' for a, b, c in rows)
    out.append(section(f'''{shead("For Document360 customers", "Already using our GitHub extension?", "Document360 Lotus is the new docs-as-code project type, synced with GitHub in both directions. The one-way extension keeps working for existing projects.")}
<div style="width: 100%; max-width: 1000px; align-self: center; border: 1px solid {N2}; border-radius: 20px; overflow-x: auto; background: #ffffff; box-shadow: 0 1px 2px rgba(24,24,27,.04), 0 24px 48px rgba(76,52,130,.10)"><div style="min-width: 620px">
<div style="display: flex"><div style="flex: 0 0 28%; padding: 16px 24px; font-size: 13px; font-weight: 700; color: {N5}">&nbsp;</div><div style="flex: 1 1 0; padding: 16px 24px; font-size: 13px; font-weight: 700; color: {N5}">GitHub extension</div><div style="flex: 1 1 0; padding: 16px 24px; font-size: 13px; font-weight: 700; color: {P6}; background: {P50}">Document360 Lotus</div></div>
{tr}</div></div>''', bg="radial-gradient(#e2daf6 1px, rgba(0,0,0,0) 1.4px) 0 0 / 24px 24px, linear-gradient(180deg, #f6f3fd 0%, #ffffff 100%)"))
    # TEAMS
    teams = [("code", "Developers", "Keep docs next to the code. Commit Markdown, review in pull requests, and never copy a page into a CMS again."),
             ("pen", "Technical writers", "Edit in a real editor with no GitHub account. Branches and pull requests are buttons, and conflicts are resolved in plain language."),
             ("chart", "Product managers", "One source of truth that ships with every release, with every change reviewed and published in one commit.")]
    t = "".join(f'<div style="flex: 1 1 280px; display: flex; flex-direction: column; gap: 14px; background: linear-gradient(180deg, #ffffff 0%, #faf8ff 100%); border: 1px solid {N2}; border-radius: 20px; padding: 32px; box-shadow: 0 1px 2px rgba(24,24,27,.04), 0 18px 40px rgba(76,52,130,.08)">{icon(ICON[ic])}<span style="font-size: 22px; font-weight: 600; color: {N9}">{n}</span><span style="font-size: 16px; line-height: 1.6; color: {N5}">{d}</span></div>' for ic, n, d in teams)
    out.append(section(f'''{shead("For teams", "Everyone works in the tool they already use")}<div style="display: flex; flex-wrap: wrap; gap: 20px">{t}</div>''', bg="radial-gradient(40% 60% at 0% 100%, rgba(127,86,217,.10), rgba(127,86,217,0) 70%), radial-gradient(40% 60% at 100% 0%, rgba(236,72,153,.08), rgba(236,72,153,0) 70%), #ffffff", idattr='id="teams"'))
    # FAQ
    faqs = [("What is docs as code?", "An approach where documentation lives in a version-controlled repository, is written in plain text such as Markdown, and goes through the same review as code. Lotus brings it to Document360 without locking out non-developers."),
            ("Do writers need to know Git, or have a GitHub account?", "No to both. Branching, saving to a branch, opening a pull request and Merge & publish are buttons in the Document360 editor, and what each person can do follows their Document360 role. Lotus handles the Git."),
            ("What is d360.json?", "A small manifest in your repository that maps folders to categories and Markdown files to articles. Your coding agent can write it from a prompt Lotus gives you, or you can start from a template."),
            ("What happens if GitHub and Document360 change the same article?", "Lotus shows each conflict side by side. Keep the version from GitHub, keep yours, or keep both, then mark the article resolved."),
            ("How does publishing work?", "Publish reviews every pending change in one dialog and writes it to GitHub as one commit. If your main branch is protected, Lotus opens a pull request instead, so your review rules still apply."),
            ("Which Git providers does Lotus support?", "Document360 Lotus launches in Beta with GitHub.")]
    fq = "".join(f'<div style="border-top: 1px solid {N2}; padding: 24px 0; display: flex; flex-direction: column; gap: 10px"><h3 style="margin: 0; font-size: 19px; font-weight: 600; color: {N9}">{q}</h3><p style="margin: 0; font-size: 16px; line-height: 1.6; color: {N5}">{a}</p></div>' for q, a in faqs)
    out.append(section(f'''<div style="display: flex; flex-wrap: wrap; gap: 40px 80px; align-items: flex-start"><div style="flex: 1 1 300px; display: flex; flex-direction: column; gap: 14px">{kicker("FAQ")}<h2 style="margin: 0; font-size: 40px; line-height: 1.12; font-weight: 700; letter-spacing: -1px; color: {N9}">Questions, answered</h2><p style="margin: 0; font-size: 17px; line-height: 1.6; color: {N5}">Want the details before early access opens? Here are the ones we hear most.</p></div><div style="flex: 2 1 420px; border-bottom: 1px solid {N2}">{fq}</div></div>''', bg="linear-gradient(180deg, #fafafa 0%, #f4f0fd 100%)", idattr='id="faq"'))
    # FINAL CTA
    out.append(f'''<section style="position: relative; overflow: hidden; background: #ffffff; padding: 96px clamp(20px, 8vw, 120px) 112px">
<div ref="{{{{ setCtaHost }}}}" aria-hidden="true" style="position: absolute; left: 0; right: 0; top: 0; bottom: 0; overflow: hidden; pointer-events: none"><canvas ref="{{{{ setCtaCanvas }}}}" aria-hidden="true" style="position: absolute; left: 0; top: 0; display: block; width: 100%; height: 100%"></canvas></div>
<div style="position: relative; z-index: 1; max-width: 820px; margin: 0 auto; border-radius: 32px; padding: clamp(40px, 6vw, 72px) clamp(20px, 5vw, 64px); background: rgba(255,255,255,.88); border: 1px solid {P100}; box-shadow: 0 30px 80px rgba(76,52,130,.18); display: flex; flex-direction: column; gap: 22px; align-items: center">
<img src="{{{{IMG:mascot}}}}" alt="The Lotus mascot" style="width: 120px; height: 120px; filter: drop-shadow(0 14px 24px rgba(127,86,217,.35))">
<h2 style="margin: 0; text-align: center; font-size: clamp(32px, 4.4vw, 48px); line-height: 1.1; font-weight: 700; letter-spacing: -1.2px; color: {N9}">Your docs in GitHub.<br><span style="color: {P}">Your team in Document360.</span></h2>
<p style="margin: 0; text-align: center; font-size: 18px; color: {N5}">Join the waitlist and be first to sync your repo both ways.</p>
{form("2")}
</div>
</section>''')
    # FOOTER
    out.append(f'''<footer style="padding: 32px clamp(20px, 8vw, 120px); flex-wrap: wrap; border-top: 1px solid {N2}; display: flex; align-items: center; gap: 12px; font-size: 14px; color: {N5}"><img src="{{{{IMG:wordmark}}}}" alt="Document360" style="display: block; width: 124px; height: 16px"><span>Lotus</span><span style="flex-grow: 1"></span><span>Docs as code, synced both ways</span></footer>''')
    return "".join(out)

BODY = build()
