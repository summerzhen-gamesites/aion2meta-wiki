from pathlib import Path
from html import escape
import json
import os

BASE = Path(__file__).parent
ROOT = Path(os.environ.get("AION2_OUTPUT_DIR", BASE))
SITE = {
    "name": "AION 2 Meta",
    "domain": "aion2meta.wiki",
    "tagline": "Global server status, build evidence, classes and launch guides for AION 2.",
    "updated": "September 19, 2026",
}
GA_MEASUREMENT_ID = os.environ.get("NEXT_PUBLIC_GA_MEASUREMENT_ID", "").strip()
GOOGLE_SITE_VERIFICATION = os.environ.get("NEXT_PUBLIC_GOOGLE_SITE_VERIFICATION", "").strip()

CLASSES = [
    ("gladiator", "Gladiator", "Melee bruiser", "Durable weapon fighter for players who want direct pressure and forgiving uptime.", "Medium"),
    ("templar", "Templar", "Tank", "Shield-led frontline class for players who want group responsibility and defensive control.", "Medium"),
    ("assassin", "Assassin", "Melee burst", "Fast, positional damage dealer for players who enjoy setup, timing and target selection.", "High"),
    ("ranger", "Ranger", "Ranged physical", "Mobile ranged class for players who want spacing, kiting and steady pressure.", "Medium"),
    ("chanter", "Chanter", "Support hybrid", "Buff-oriented support that can contribute damage while strengthening a group.", "Medium"),
    ("cleric", "Cleric", "Healer", "Primary healing and recovery role for players who want strong group value.", "Medium"),
    ("sorcerer", "Sorcerer", "Ranged magic DPS", "Elemental caster for players who prefer burst windows and ranged control.", "Medium"),
    ("spiritmaster", "Spiritmaster", "Summoner", "Pet and control focused mage for players who like pressure through companions and utility.", "High"),
]

CLASS_DATA = {
    "gladiator": {"archetype": "Warrior", "range": "Melee", "party": "Frontline DPS / bruiser", "beginner": "Good if you want durable melee pressure.", "watch": "Damage uptime, survivability tradeoffs, group demand."},
    "templar": {"archetype": "Warrior", "range": "Melee", "party": "Main tank / protector", "beginner": "Good if you like responsibility and slower, safer play.", "watch": "Tank demand, threat tools, defensive cooldown tuning."},
    "assassin": {"archetype": "Scout", "range": "Melee", "party": "Burst DPS / pick pressure", "beginner": "Harder first pick because timing and positioning matter.", "watch": "Burst windows, stealth value, PvP counterplay."},
    "ranger": {"archetype": "Scout", "range": "Ranged", "party": "Ranged physical DPS", "beginner": "Comfortable if you prefer spacing and kiting.", "watch": "Mobility, trap/control value, sustained damage."},
    "chanter": {"archetype": "Priest", "range": "Melee support", "party": "Buff support / hybrid", "beginner": "Good if you want utility without being a pure healer.", "watch": "Buff strength, off-heal value, group-slot pressure."},
    "cleric": {"archetype": "Priest", "range": "Ranged support", "party": "Primary healer", "beginner": "Good for group-minded players; stressful if you dislike healing responsibility.", "watch": "Healing throughput, dispels, solo comfort."},
    "sorcerer": {"archetype": "Mage", "range": "Ranged magic", "party": "Burst caster DPS", "beginner": "Good if you like clear ranged damage windows.", "watch": "Cast safety, burst tuning, control reliability."},
    "spiritmaster": {"archetype": "Mage", "range": "Ranged / pet", "party": "Summoner / utility mage", "beginner": "More complex because pet control and utility decisions matter.", "watch": "Pet scaling, debuffs, PvE boss reliability."},
}

OFFICIAL_FACTS = [
    ("Launch Scale Test", "The Global Launch Scale Test has ended; the site is now tracking the Advanced Access preparation window."),
    ("LST Level Cap", "The Launch Scale Test is framed around limited test progression up to level 37."),
    ("Test Progress", "Launch Scale Test progress was temporary test data, not launch progression."),
    ("Launch Date", "Steam lists AION 2 as unlocking on October 5, 2026."),
    ("Advance Access", "Founder Pack early access is advertised for September 30, 2026."),
    ("Engine", "Steam describes AION 2 as built on Unreal Engine 5."),
    ("World Scale", "Steam says the world is 36 times larger than the original AION."),
    ("Combat Hook", "Steam positions flight and verticality as central to combat and exploration."),
    ("PvE Scope", "Steam describes over 200 dungeons across solo, 5-player and 10-player formats."),
    ("Other PvE", "Seasonal challenges, competitive rankings and open-world events are named on Steam."),
    ("Customization", "Steam describes over 200 character customization options."),
]

FOUNDER_PACKS = [
    ("Standard", "$24.99", "5-Day Advanced Access, supply chest, title and 30-day Special Quai Membership are the key known value anchors."),
    ("Deluxe", "$49.99", "Includes Standard contents plus extra cosmetic/value items for players who want more than access."),
    ("Ultimate", "$99.99", "Highest listed tier for collectors who want the largest launch bundle."),
]

SYSTEM_REQUIREMENTS = [
    ("OS", "Windows 10 / 11, 64-bit"),
    ("CPU", "AMD Ryzen 5 2600 / Intel Core i5-10500"),
    ("Memory", "8 GB RAM"),
    ("GPU", "NVIDIA GTX 1050 Ti 4GB"),
    ("DirectX", "Version 12"),
    ("Storage", "100 GB available space"),
    ("Network", "Broadband internet connection"),
    ("Note", "SSD recommended; lower graphics preset recommended for FHD on minimum hardware."),
]

NAV = [
    ("/tier-list/class-tier-list/", "Tier Lists"),
    ("/classes/", "Classes"),
    ("/builds/", "Builds"),
    ("/dungeons/", "Dungeons"),
    ("/guides/beginner-guide/", "Guides"),
    ("/meta/global-vs-korea/", "Meta"),
]

META_PAGES = [
    ("/gameplay/", "Gameplay"),
    ("/pve-content/", "PvE Content"),
    ("/flight-combat/", "Flight Combat"),
    ("/character-customization/", "Customization"),
    ("/meta/evidence-policy/", "Evidence Policy"),
    ("/meta/update-log/", "Update Log"),
    ("/meta/launch-verification-checklist/", "Launch Checklist"),
]

PRELAUNCH_PAGES = [
    ("/launch-scale-test/", "Launch Scale Test"),
    ("/advance-access/", "Advance Access"),
    ("/founders-pack/which-edition/", "Which Edition"),
    ("/server-status/", "Server Status"),
    ("/preload-download/", "Preload & Download"),
]

def json_ld(data):
    return json.dumps(data, ensure_ascii=False, separators=(",", ":"))

def analytics_head():
    parts = []
    if GOOGLE_SITE_VERIFICATION:
        parts.append(f'  <meta name="google-site-verification" content="{escape(GOOGLE_SITE_VERIFICATION)}">')
    if GA_MEASUREMENT_ID:
        ga = escape(GA_MEASUREMENT_ID)
        parts.append(f'  <script async src="https://www.googletagmanager.com/gtag/js?id={ga}"></script>')
        parts.append(f"""  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{ga}');
  </script>""")
    return "\n".join(parts)

def table_html(caption, head, rows, class_name=""):
    class_attr = f" class='{escape(class_name)}'" if class_name else ""
    caption_html = f"<caption>{escape(caption)}</caption>"
    return f"<div class='table-wrap'><table{class_attr}>{caption_html}<thead>{head}</thead><tbody>{rows}</tbody></table></div>"

def write(path, body):
    target = ROOT / path.strip("/")
    if path.endswith("/"):
        target = target / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(body, encoding="utf-8", newline="")

def url_for(slug):
    return "/" if slug == "index" else f"/{slug.strip('/')}/"

def card(title, text, href=None, meta=None):
    link = f'<a class="card-link" href="{href}">Open</a>' if href else ""
    meta_html = f'<p class="eyebrow">{escape(meta)}</p>' if meta else ""
    return f'<article class="card">{meta_html}<h3>{escape(title)}</h3><p>{escape(text)}</p>{link}</article>'

def page(title, description, slug, main, extra_class=""):
    main = main.replace("<div class='table-wrap'><table><thead>", f"<div class='table-wrap'><table><caption>{escape(title)} data table</caption><thead>")
    nav = "".join(f'<a href="{href}">{label}</a>' for href, label in NAV)
    canonical = f"https://{SITE['domain']}{url_for(slug)}"
    robots = "  <meta name=\"robots\" content=\"noindex,follow\">\n" if slug == "404" else ""
    analytics = analytics_head()
    analytics = f"\n{analytics}" if analytics else ""
    page_name = f"{title} | {SITE['name']}"
    path_parts = [part for part in url_for(slug).strip("/").split("/") if part]
    breadcrumb_items = [{"@type": "ListItem", "position": 1, "name": SITE["name"], "item": f"https://{SITE['domain']}/"}]
    current_path = ""
    for index, part in enumerate(path_parts, start=2):
        current_path += f"/{part}"
        breadcrumb_items.append({"@type": "ListItem", "position": index, "name": part.replace("-", " ").title(), "item": f"https://{SITE['domain']}{current_path}/"})
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "WebSite", "name": SITE["name"], "url": f"https://{SITE['domain']}/", "description": SITE["tagline"]},
            {"@type": "WebPage", "name": title, "url": canonical, "description": description, "isPartOf": {"@type": "WebSite", "name": SITE["name"], "url": f"https://{SITE['domain']}/"}},
            {"@type": "BreadcrumbList", "itemListElement": breadcrumb_items},
        ],
    }
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(page_name)}</title>
  <meta name="description" content="{escape(description)}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{SITE['name']}">
  <meta property="og:title" content="{escape(page_name)}">
  <meta property="og:description" content="{escape(description)}">
  <meta property="og:url" content="{canonical}">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{escape(page_name)}">
  <meta name="twitter:description" content="{escape(description)}">
{robots.rstrip()}
  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
  <link rel="manifest" href="/site.webmanifest">
  <meta name="theme-color" content="#080a0f">
  <link rel="stylesheet" href="/assets/styles.css">
  <script type="application/ld+json">{json_ld(schema)}</script>
{analytics}
  <script defer src="/assets/site.js"></script>
<style>.top-sticky-ad{{position:sticky;top:0;z-index:45;display:flex;justify-content:center;padding:8px;background:rgba(8,10,15,.92);backdrop-filter:blur(12px);border-bottom:1px solid rgba(255,255,255,.08)}}.top-sticky-ad iframe{{border:0;max-width:calc(100vw - 16px);background:transparent}}</style>
</head>
<body class="{extra_class}">
  <a class="skip" href="#content">Skip to content</a>
  <header class="site-header">
    <a class="brand" href="/"><span class="brand-mark">A2</span><span>{SITE['name']}</span></a>
    <nav aria-label="Primary">{nav}</nav>
  </header>
  <aside class="top-sticky-ad" data-ad-placement="top-sticky" aria-label="Sponsored"><iframe src="/ads/banner-320x50.html" title="Sponsored" width="320" height="50" loading="eager" scrolling="no" sandbox="allow-scripts"></iframe></aside>
  <main id="content">{main}</main>
  <footer class="site-footer">
    <div>
      <strong>{SITE['name']}</strong>
      <p>{SITE['tagline']} Current status: Launch Scale Test ended; Advanced Access preparation. Last updated: {SITE['updated']}.</p>
    </div>
    <p class="small">Unofficial fan resource. AION 2 belongs to its respective publisher and developer. Pages distinguish Official, KR/TW Reference, Global Verified and Unconfirmed information.</p>
  </footer>
</body>
</html>"""

def hero(title, text, eyebrow="Global Meta Tracker"):
    return f"""<section class="hero">
  <div class="hero-copy">
    <p class="eyebrow">{escape(eyebrow)}</p>
    <h1>{escape(title)}</h1>
    <p class="lead">{escape(text)}</p>
    <div class="hero-actions">
      <a class="button primary" href="/tier-list/class-tier-list/">View Tier Matrix</a>
      <a class="button" href="/classes/">Choose a Class</a>
    </div>
  </div>
  <div class="status-panel" aria-label="Global launch status">
    <span class="status-dot"></span>
    <strong>Current Global Status</strong>
    <p>Launch Scale Test ended. No live Global server is available until the next access window; build and class notes remain separate from final launch progression.</p>
    <dl><div><dt>Launch Scale Test</dt><dd>Ended</dd></div><div><dt>Advanced Access</dt><dd>Sep 30, 2026</dd></div><div><dt>Official Launch</dt><dd>Oct 5, 2026</dd></div></dl>
  </div>
</section>"""

def matrix():
    cols = ["Solo", "Dungeon", "Raid", "1v1 PvP", "Small PvP", "Large PvP", "Beginner Complexity"]
    rows = []
    for slug, name, *_ in CLASSES:
        cells = "".join("<td><span class='pill muted'>TBD</span></td>" for _ in cols[:-1])
        complexity = "High" if slug in {"assassin", "spiritmaster"} else "Medium"
        rows.append(f"<tr><th><a href='/classes/{slug}/'>{name}</a></th>{cells}<td>{complexity}</td></tr>")
    head = "".join(f"<th>{c}</th>" for c in ["Class"] + cols)
    return table_html("AION 2 Global class tier matrix with pre-launch TBD rankings and beginner complexity", f"<tr>{head}</tr>", "".join(rows), "tier-matrix")

def content_section(title, body):
    return f"<section class='section'><h2>{escape(title)}</h2>{body}</section>"

def facts_grid():
    return "<div class='grid facts'>" + "".join(f"<div><b>{escape(k)}</b><span>{escape(v)}</span></div>" for k, v in OFFICIAL_FACTS) + "</div>"

def class_compare_table():
    rows = []
    for slug, name, role, _, diff in CLASSES:
        data = CLASS_DATA[slug]
        rows.append(f"<tr><th><a href='/classes/{slug}/'>{name}</a></th><td>{data['archetype']}</td><td>{role}</td><td>{data['range']}</td><td>{diff}</td><td>{data['beginner']}</td></tr>")
    return table_html("AION 2 class comparison by archetype, role, range and beginner fit", "<tr><th>Class</th><th>Archetype</th><th>Role</th><th>Range</th><th>Difficulty</th><th>Beginner Note</th></tr>", "".join(rows))

def source_note():
    return "<p class='source-note'>Source status: Steam / official storefront facts are treated as Official. Class ranking, build strength, economy and PvP dominance remain unverified until Global launch evidence is available.</p>"

def sources_section(extra=""):
    links = "<ul><li><a href='https://store.steampowered.com/app/3393110/AION_2/' target='_blank' rel='noopener noreferrer'>AION 2 on Steam</a> for launch date, gameplay pillars, dungeons, customization and PC requirements.</li><li><a href='https://store.steampowered.com/app/4972180/AION_2_FOUNDERS_PACK/' target='_blank' rel='noopener noreferrer'>AION 2 Founder's Pack on Steam</a> for edition names, prices and advance access framing.</li></ul>"
    if extra:
        links += extra
    return content_section("Sources", links)

home_cards = "".join([
    card("Launch Scale Test", "Ended test details, Steam/PURPLE access notes, level cap and wipe context for the September test.", "/launch-scale-test/", "P0"),
    card("Server Status", "Pre-launch server status, maintenance, queue and connection issue hub for Steam and PURPLE players.", "/server-status/", "P0"),
    card("Current Meta", "Versioned class tier matrix for Global launch, with evidence labels before any rating becomes final.", "/tier-list/class-tier-list/", "P0"),
    card("Choose Your Class", "Eight launch class overviews split by role, difficulty, PvE, PvP and who should play them.", "/classes/", "P0"),
    card("Build Evidence", "Post-LST starter, PvE and PvP build evidence status for all eight Global launch classes.", "/builds/", "P0"),
    card("Founder Pack", "Standard, Deluxe and Ultimate purchase-decision guide for players comparing early access value.", "/founders-pack/", "P1"),
    card("Dungeons", "Global dungeon hub for Launch Scale Test names, party setup, boss mechanics and rewards.", "/dungeons/", "P1"),
    card("Global vs KR/TW", "A clear separation between official Global facts and regional reference data.", "/meta/global-vs-korea/", "Moat"),
])

meta_cards = "".join(card(label, f"Confirmed pre-launch data and update framework for {label.lower()}.", href, "Data") for href, label in META_PAGES)
prelaunch_cards = "".join(card(label, f"Launch preparation page for {label.lower()} search intent.", href, "Pre-launch") for href, label in PRELAUNCH_PAGES)

home = hero("AION 2 Meta", SITE["tagline"]) + content_section("Confirmed Global Facts", facts_grid() + source_note()) + content_section("Start Here", f"<div class='grid cards'>{home_cards}</div>") + content_section("Launch Prep Pages", f"<div class='grid cards'>{prelaunch_cards}</div>") + content_section("Confirmed Data Pages", f"<div class='grid cards'>{meta_cards}</div>") + content_section("Global Class Tier Matrix", matrix()) + content_section("Evidence Rules", "<div class='evidence-row'><span>Official</span><span>Global Verified</span><span>KR/TW Reference</span><span>Unconfirmed</span></div><p>Ratings, builds and patch movement should show the source type, last tested date and reason. Beginner Complexity is not a power ranking; it is a pre-launch estimate of how demanding the class may be for a new player.</p>") + sources_section()
write("index.html", page("AION 2 Meta - Global Builds, Tier Lists & Class Meta", "AION 2 Global meta tracker for class rankings, builds, release date, founder packs and launch guides.", "index", home, "home"))

classes_cards = "".join(card(name, desc, f"/classes/{slug}/", role) for slug, name, role, desc, _ in CLASSES)
class_picker = "<div class='table-wrap'><table><thead><tr><th>I want to...</th><th>Start with</th><th>Why</th></tr></thead><tbody><tr><th>Tank for groups</th><td>Templar</td><td>Clear frontline and defensive responsibility.</td></tr><tr><th>Heal groups</th><td>Cleric</td><td>Primary recovery role with high party value.</td></tr><tr><th>Play support without pure healing</th><td>Chanter</td><td>Hybrid support with buffs and damage contribution.</td></tr><tr><th>Use ranged physical pressure</th><td>Ranger</td><td>Spacing, kiting and steady damage are the role fantasy.</td></tr><tr><th>Use ranged magic burst</th><td>Sorcerer</td><td>Clear caster identity with burst windows.</td></tr><tr><th>Play fast melee burst</th><td>Assassin</td><td>Higher-skill pick focused on timing and target selection.</td></tr><tr><th>Play durable melee</th><td>Gladiator</td><td>Forgiving melee pressure and frontline uptime.</td></tr><tr><th>Manage pets and utility</th><td>Spiritmaster</td><td>More complex summoner/control identity.</td></tr></tbody></table></div>"
write("classes/", page("AION 2 Classes", "Compare all eight AION 2 launch classes by role, playstyle, difficulty and Launch Scale Test fit.", "classes", hero("AION 2 Classes", "Pick a Launch Scale Test class by role, difficulty and intended activity without pretending the final Global meta is solved.", "Class Hub") + content_section("Which AION 2 Class Should You Play?", class_picker) + content_section("Class Comparison", class_compare_table()) + f"<section class='section'><div class='grid cards'>{classes_cards}</div></section>"))

build_cards = "".join(card(f"{name} Build Evidence", f"Starter/PvE/PvP evidence status for {name}: verified fields pending, skills/rotation/stats/gear TBD, test observation needed.", f"/builds/{slug}-build/", "Build") for slug, name, *_ in CLASSES)
lst_builds = "<div class='notice'><b>Launch Scale Test ended:</b> Global build evidence is being verified before any skill, rotation, stats, gear or BIS claim is published. Use this hub to pick the class build page and see which fields remain TBD.</div>"
build_matrix = "<div class='table-wrap'><table><thead><tr><th>Class</th><th>Evidence Status</th><th>Build Page</th></tr></thead><tbody>" + "".join(f"<tr><th>{name}</th><td>{'Tank / group safety' if slug == 'templar' else 'Healer / solo fallback' if slug == 'cleric' else 'Support / group utility' if slug == 'chanter' else 'Ranged physical leveling and PvP' if slug == 'ranger' else 'Melee burst and PvP pressure' if slug == 'assassin' else 'Durable melee leveling' if slug == 'gladiator' else 'Magic burst and AoE' if slug == 'sorcerer' else 'Solo utility and pet control'}; verified fields pending; skills/rotation/stats/gear TBD.</td><td><a href='/builds/{slug}-build/'>Open {name} build</a></td></tr>" for slug, name, *_ in CLASSES) + "</tbody></table></div>"
write("builds/", page("AION 2 Builds - Post-LST PvE & PvP Build Evidence", "AION 2 builds hub for post-LST evidence status, starter build pages, PvE, PvP and all eight Global launch classes.", "builds", hero("AION 2 Builds", "Post-LST build evidence hub for starter, PvE and PvP planning across all eight Global classes while verified data remains pending.", "Build Hub") + content_section("Global Build Evidence", lst_builds + build_matrix) + f"<section class='section'><div class='grid cards'>{build_cards}</div></section>"))

for slug, name, role, desc, diff in CLASSES:
    data = CLASS_DATA[slug]
    body = hero(f"AION 2 {name}", desc, role)
    body += content_section("Quick Verdict", f"<div class='summary'><div><b>Archetype</b><span>{data['archetype']}</span></div><div><b>Role</b><span>{role}</span></div><div><b>Difficulty</b><span>{diff}</span></div><div><b>Global Tier</b><span>TBD until Global evidence is verified</span></div><div><b>Party Job</b><span>{data['party']}</span></div><div><b>Range</b><span>{data['range']}</span></div><div><b>Beginner Note</b><span>{data['beginner']}</span></div><div><b>Build</b><span><a href='/builds/{slug}-build/'>Best {name} Build</a></span></div></div>")
    body += content_section("Who Should Play This Class", f"<p>{name} is a good candidate if the role fantasy fits you. The Global launch meta is not final, so this page separates playstyle confidence from unverified ranking claims.</p><ul><li>Use this class page to understand identity and fit.</li><li>Use the build page for skills, stats, rotation and patch notes.</li><li>Use the tier list for activity-by-activity ranking once Global data exists.</li></ul>")
    body += content_section("PvE, PvP And Solo Outlook", "<p>Pre-launch outlook is intentionally conservative. Activity ratings will move from TBD to a letter-grade rank only when the Global client, patch state and repeatable evidence support the rating.</p>")
    body += content_section("What To Verify At Global Launch", f"<ul><li>{data['watch']}</li><li>Real skill values, cooldowns and animation locks in the Global client.</li><li>Dungeon performance in solo, 5-player and 10-player formats.</li><li>How the class performs in 1v1, small-scale and large-scale PvP separately.</li></ul>")
    write(f"classes/{slug}/", page(f"AION 2 {name} Class Guide", f"AION 2 {name} class overview with role, difficulty, PvE, PvP, solo fit and Global evidence status.", f"classes/{slug}", body))

for slug, name, role, desc, diff in CLASSES:
    data = CLASS_DATA[slug]
    tabs = """<div class="tabs" data-tabs><div role="tablist" aria-label="Build mode"><button class="active" role="tab" aria-selected="true" data-tab="pve">PvE</button><button role="tab" aria-selected="false" data-tab="pvp">PvP</button><button role="tab" aria-selected="false" data-tab="solo">Solo</button></div><section role="tabpanel" data-panel="pve"><h3>PvE Build</h3><p>Core skills, rotation, gear priority and stigma choices stay pending until Global launch data can be tested.</p></section><section role="tabpanel" hidden data-panel="pvp"><h3>PvP Build</h3><p>PvP recommendations will separate 1v1, small-scale and large-scale evidence instead of merging them into one vague rank.</p></section><section role="tabpanel" hidden data-panel="solo"><h3>Solo Build</h3><p>Solo guidance will focus on survivability, uptime and low-friction progression once Global values are known.</p></section></div>"""
    body = hero(f"AION 2 {name} Build", f"Launch Scale Test {name} build page for leveling, PvE and PvP planning around the level 37 test window.", "Build Template")
    body += content_section("Build Status", f"<div class='notice'><b>Launch Scale Test:</b> Treat this as a level 37 starter framework until Global skill values, gear and rotations are verified. No fake endgame BIS claims.</div><div class='summary'><div><b>Role</b><span>{role}</span></div><div><b>Party Job</b><span>{data['party']}</span></div><div><b>Range</b><span>{data['range']}</span></div><div><b>Watch First</b><span>{data['watch']}</span></div></div>")
    body += content_section("Build Modes", tabs)
    body += content_section("What This Page Will Track", "<ol><li>Core skills and skill priority</li><li>Rotation and opener notes</li><li>Gear and stat priority</li><li>Best stigma and alternatives</li><li>Strengths, weaknesses, matchups and patch changes</li></ol>")
    write(f"builds/{slug}-build/", page(f"AION 2 {name} Build", f"AION 2 {name} build for Launch Scale Test leveling, PvE and PvP with Global evidence status.", f"builds/{slug}-build", body))

tier_pages = {
    "class-tier-list": ("AION 2 Class Tier List", "AION 2 class tier list matrix for Global launch, tracking Solo, Dungeon, Raid and PvP rankings with evidence status.", "Full activity matrix", matrix()),
    "pve-tier-list": ("AION 2 PvE Tier List", "AION 2 PvE tier list for dungeon, raid and solo PvE rankings, held as TBD until Global launch testing verifies class performance.", "PvE ranks", matrix()),
    "pvp-tier-list": ("AION 2 PvP Tier List", "AION 2 PvP tier list split by 1v1, small-scale and large-scale play, with Global evidence labels for every future rank.", "PvP ranks", matrix()),
    "beginner-tier-list": ("AION 2 Beginner Tier List", "Best AION 2 beginner classes by difficulty, role clarity and launch progression friendliness, separated from raw power rankings.", "Beginner picks", matrix()),
    "solo-tier-list": ("AION 2 Solo Tier List", "AION 2 solo class tier list for leveling, self-sustain and open-world comfort, updated only after Global verification.", "Solo ranks", matrix()),
}

tier_hub_cards = "".join(card(title.replace("AION 2 ", ""), desc, f"/tier-list/{slug}/", "Tier") for slug, (title, desc, _, _) in tier_pages.items())
body = hero("AION 2 Tier Lists", "All AION 2 tier lists in one place, with every Global rank kept TBD until evidence is strong enough to publish.", "Tier Hub")
body += content_section("Tier List Pages", f"<div class='grid cards'>{tier_hub_cards}</div>")
body += content_section("Current Ranking Policy", "<p>Pre-launch pages use a matrix and evidence labels instead of pretending the Global meta is solved. Activity-specific ranks are tracked separately for class, PvE, PvP, beginner and solo needs.</p>")
write("tier-list/", page("AION 2 Tier Lists", "AION 2 tier list hub for class, PvE, PvP, beginner and solo rankings with Global evidence status.", "tier-list", body))

for slug, (title, desc, label, table) in tier_pages.items():
    body = hero(title, "Every rank is versioned. Pre-launch pages show TBD until Global evidence is strong enough to publish.", label)
    body += content_section("Current Matrix", table)
    body += content_section("How Ratings Become Verified", "<p>A class only receives a rank when the page can state patch, last tested date, evidence type and why the rating changed. KR/TW data may inform hypotheses, but it will be labeled as reference rather than Global proof.</p>")
    write(f"tier-list/{slug}/", page(title, desc, f"tier-list/{slug}", body))

guide_pages = {
    "best-class": ("AION 2 Best Class", "Choose the best AION 2 class for your goal without relying on unverified Global tier claims.", "Match your goal to a role, then revisit the tier matrix after Global testing starts."),
    "beginner-guide": ("AION 2 Beginner Guide", "A practical AION 2 beginner guide for launch preparation, class choice and progression priorities.", "Start with class fit, learn group roles, follow verified patch notes and avoid overcommitting to pre-launch rankings."),
    "leveling-guide": ("AION 2 Leveling Guide", "AION 2 leveling guide framework for launch players, updated as Global progression data is verified.", "Leveling advice is held to known systems and will expand after launch routes, rewards and bottlenecks are confirmed."),
    "gear-progression": ("AION 2 Gear Progression", "AION 2 gear progression guide for Global launch, prepared for verified item sources, upgrade paths and role stat priorities.", "Gear pages will track sources, upgrade priorities and patch evidence once Global itemization is public."),
    "pvp-guide": ("AION 2 PvP Guide", "AION 2 PvP guide for launch players, split by 1v1, small-scale and large-scale play.", "PvP guidance starts with roles and positioning, then adds matchup data after Global testing."),
    "factions": ("AION 2 Factions", "AION 2 faction guide for launch players, covering verified faction restrictions, server planning and PvP implications.", "Faction information will stay limited to verified official details and launch-client checks."),
}

guide_hub_cards = "".join(card(title.replace("AION 2 ", ""), desc, f"/guides/{slug}/", "Guide") for slug, (title, desc, _) in guide_pages.items())
body = hero("AION 2 Guides", "Launch preparation guides for class choice, beginner setup, leveling, gear, PvP and faction verification.", "Guide Hub")
body += content_section("Guide Library", f"<div class='grid cards'>{guide_hub_cards}</div>")
body += content_section("How These Guides Update", "<p>Guides start with official facts and safe launch preparation. After advance access opens, they should be updated from Global Verified evidence, not regional assumptions.</p>")
write("guides/", page("AION 2 Guides", "AION 2 guide hub for beginner, best class, leveling, gear progression, PvP and faction launch preparation.", "guides", body))

for slug, (title, desc, intro) in guide_pages.items():
    body = hero(title, intro, "Guide")
    if slug == "best-class":
        body += content_section("Best Class By Player Goal", "<div class='table-wrap'><table><thead><tr><th>Goal</th><th>Classes To Start With</th><th>Why</th></tr></thead><tbody><tr><th>Safest group role</th><td>Templar, Cleric</td><td>Tank and healer roles usually have clear party value, but exact demand needs Global verification.</td></tr><tr><th>Simple ranged start</th><td>Ranger, Sorcerer</td><td>Both offer a readable ranged role fantasy for players who dislike melee risk.</td></tr><tr><th>Support identity</th><td>Chanter, Cleric</td><td>Pick Chanter for hybrid support interest; pick Cleric if you want primary healing.</td></tr><tr><th>High-skill pressure</th><td>Assassin, Spiritmaster</td><td>Both are marked higher complexity because positioning, timing or pet/utility decisions matter.</td></tr><tr><th>Durable melee</th><td>Gladiator, Templar</td><td>Good candidates if you want to fight near the frontline.</td></tr></tbody></table></div>")
        body += content_section("How To Choose Before Global Meta Exists", "<ol><li>Pick by role first: tank, healer, support, ranged damage, melee pressure or summoner.</li><li>Pick by tolerance for responsibility: Templar and Cleric may carry more group expectations.</li><li>Pick a backup class for advance access because balance and queue demand can change quickly.</li><li>Wait for Global Verified tier updates before treating a class as best for a specific activity.</li></ol>")
    elif slug == "beginner-guide":
        body += content_section("Beginner Launch Checklist", "<ol><li>Check PC requirements and reserve at least 100 GB storage.</li><li>Decide whether five-day advance access matters before buying a Founder Pack.</li><li>Choose two classes: one comfort pick and one group-role pick.</li><li>Bookmark the class tier matrix, but treat every activity rating as TBD until Global evidence appears.</li><li>During launch, record patch, class, level, activity and pain point when comparing advice.</li></ol>")
        body += content_section("Beginner-Friendly Class Framing", class_compare_table())
        body += content_section("Common Mistakes To Avoid", "<ul><li>Do not choose a class only because a pre-launch page predicts dominance.</li><li>Do not assume KR/TW economy, PvP or dungeon tuning is identical to Global.</li><li>Do not split time across too many classes before you understand your preferred role.</li><li>Do not ignore flight and vertical movement; it can affect both combat feel and exploration routing.</li></ul>")
    elif slug == "leveling-guide":
        body += content_section("Pre-Launch Leveling Plan", "<div class='timeline'><div><b>Before Advance Access</b><span>Install early, check storage, pick class pair and read role pages.</span></div><div><b>First Session</b><span>Prioritize main story/tutorial systems and learn your movement, flight and survival tools.</span></div><div><b>Early Group Content</b><span>Test solo and party dungeon comfort before locking a main.</span></div><div><b>After Bottlenecks Appear</b><span>Update routes only from Global client evidence, not regional assumptions.</span></div></div>")
        body += content_section("What This Page Will Track After Launch", "<ul><li>Fastest verified leveling activities.</li><li>Dungeon unlock points and requirements.</li><li>Gear or stat bottlenecks that slow progression.</li><li>Class-specific leveling comfort notes.</li><li>Patch changes that alter route priority.</li></ul>")
    elif slug == "gear-progression":
        body += content_section("Gear Progression Framework", "<div class='table-wrap'><table><thead><tr><th>Stage</th><th>Player Task</th><th>Evidence Needed</th></tr></thead><tbody><tr><th>Early leveling</th><td>Use the highest reliable upgrades without over-optimizing.</td><td>Quest, dungeon and drop sources from Global.</td></tr><tr><th>First dungeon loop</th><td>Identify repeatable upgrades and role priorities.</td><td>Dungeon requirements, reward tables and stat behavior.</td></tr><tr><th>Pre-endgame</th><td>Decide whether crafting, trading or dungeons are the best upgrade path.</td><td>Global economy and material data.</td></tr><tr><th>Meta gearing</th><td>Separate PvE, PvP and solo priorities by class.</td><td>Patch-tested builds and performance evidence.</td></tr></tbody></table></div>")
        body += content_section("What Not To Publish Yet", "<p>Exact stat weights, best-in-slot lists, crafting costs and market values should wait for Global verification. These are exactly the areas where regional data can mislead launch players.</p>")
    elif slug == "pvp-guide":
        body += content_section("PvP Modes To Track Separately", "<div class='summary'><div><b>1v1</b><span>Duel and isolated matchup strength.</span></div><div><b>Small-scale</b><span>Pick pressure, utility and coordinated skirmish value.</span></div><div><b>Large-scale</b><span>Group durability, ranged pressure, healing and area control.</span></div><div><b>Open-world</b><span>Mobility, escape tools, terrain and flight behavior.</span></div></div>")
        body += content_section("Launch PvP Principles", "<ul><li>Track class strength by mode instead of publishing one overall PvP rank.</li><li>Separate mechanical difficulty from power; a hard class can still be strong or weak.</li><li>Watch flight and verticality because they may change ranged uptime and melee access.</li><li>Update matchups only when Global patch and player population evidence support the claim.</li></ul>")
    elif slug == "factions":
        body += content_section("What This Page Can Say Now", "<p>AION as a series is known for faction conflict, but this page stays conservative for AION 2 Global until faction rules, restrictions and launch-client details are confirmed directly.</p>")
        body += content_section("Faction Data To Verify", "<div class='table-wrap'><table><thead><tr><th>Question</th><th>Why It Matters</th></tr></thead><tbody><tr><th>Faction names and restrictions</th><td>Affects character creation and server planning.</td></tr><tr><th>Server or account limits</th><td>Prevents players from locking themselves out of friends or guild plans.</td></tr><tr><th>PvP implications</th><td>Changes open-world risk, grouping and large-scale content.</td></tr><tr><th>Economy boundaries</th><td>Trading and market behavior may differ by faction or server.</td></tr></tbody></table></div>")
    body += content_section("Launch Notes", "<p>This page is designed to answer the player task first, then expand only where evidence exists. Unknown Global values are marked instead of filled with guesses.</p>")
    body += content_section("Related Pages", "<div class='grid cards'>" + card("Class Tier List", "Compare classes by activity.", "/tier-list/class-tier-list/") + card("Classes", "Read launch class overviews.", "/classes/") + card("Evidence Policy", "See how Global claims are verified.", "/meta/evidence-policy/") + "</div>")
    write(f"guides/{slug}/", page(title, desc, f"guides/{slug}", body))

body = hero("AION 2 Release Date", "Steam currently lists AION 2 as available on October 5, 2026, with Founder Pack early access advertised as five days before official launch.", "Release Tracker")
body += content_section("Launch Timeline", "<div class='timeline'><div><b>Sep 30, 2026</b><span>Advance Access for eligible Founder Pack owners.</span></div><div><b>Oct 5, 2026</b><span>Full Global launch date shown on Steam.</span></div></div>")
body += content_section("Confirmed Steam Facts", facts_grid())
body += content_section("What To Prepare", "<ul><li>Pick two candidate classes instead of locking to a fake pre-launch tier.</li><li>Bookmark class, PvE and PvP tier pages for launch-day updates.</li><li>Check Founder Pack value only if early access or cosmetics matter to you.</li></ul>")
write("release-date/", page("AION 2 Release Date", "AION 2 release date, advance access timing and launch preparation checklist.", "release-date", body))

body = hero("AION 2 Launch Scale Test", "Ended Global test hub for Steam and PURPLE access, level cap, progress wipe notes and what to check before Advanced Access.", "Live Test")
body += content_section("Launch Scale Test Schedule", "<div class='table-wrap'><table><thead><tr><th>Window</th><th>PDT</th><th>CEST</th><th>What To Check</th></tr></thead><tbody><tr><th>Day 1</th><td>Sep 17, 6:00 AM-12:00 PM</td><td>Sep 17, 15:00-21:00</td><td>Login, server status, class creation and first build notes.</td></tr><tr><th>Day 2</th><td>Sep 18, 12:00 PM-6:00 PM</td><td>Sep 18, 21:00-Sep 19, 03:00</td><td>Confirm fixes, queues, dungeon access and level 37 build notes.</td></tr></tbody></table></div>")
body += content_section("What Is Included", "<div class='summary'><div><b>Access</b><span>Steam and PURPLE test access.</span></div><div><b>Classes</b><span>All eight Global launch classes are the main test targets.</span></div><div><b>Level Cap</b><span>Plan around level 37 instead of endgame BIS.</span></div><div><b>Progress</b><span>Treat all test progress as temporary.</span></div></div>")
body += content_section("How To Join And Download", "<ul><li>Use the Steam Playtest / AION 2 Steam entry if playing through Steam.</li><li>Use PURPLE if you prefer the NCSOFT launcher path.</li><li>No class rank should be finalized from the first hour of testing.</li><li>After the test, separate Steam Playtest client notes from the full launch client on September 30 and October 5.</li></ul>")
body += content_section("Where To Go Next", "<div class='grid cards'>" + card("Server Status", "Check maintenance, queue and connection status.", "/server-status/") + card("Launch Test Builds", "Open level 37 starter build planning.", "/builds/") + card("Classes", "Choose a class by role and difficulty.", "/classes/") + card("Dungeons", "Track Global dungeon names and requirements.", "/dungeons/") + "</div>")
write("launch-scale-test/", page("AION 2 Launch Scale Test", "AION 2 Launch Scale Test schedule, download, Steam, PURPLE, level cap, progress wipe and server status links.", "launch-scale-test", body))

body = hero("AION 2 Founder's Pack Comparison", "Standard vs Deluxe vs Ultimate, focused on price, five-day advance access, membership and who should actually buy.", "Buyer Guide")
body += content_section("Standard vs Deluxe vs Ultimate", "<div class='table-wrap'><table><thead><tr><th>Feature</th><th>Standard</th><th>Deluxe</th><th>Ultimate</th></tr></thead><tbody><tr><th>US price</th><td>$24.99</td><td>$49.99</td><td>$99.99</td></tr><tr><th>Advance access</th><td>Five-day early access</td><td>Five-day early access</td><td>Five-day early access</td></tr><tr><th>Membership</th><td>30-day membership listed in current pack summaries</td><td>30-day membership listed in current pack summaries</td><td>30-day membership listed in current pack summaries</td></tr><tr><th>Best fit</th><td>Access-first players</td><td>Players who value extra cosmetics/items</td><td>Collectors and committed launch mains</td></tr><tr><th>Risk</th><td>Least sunk cost if you wait after the test</td><td>Only worth it if extras matter to you</td><td>Hardest to justify before final Global meta</td></tr></tbody></table></div>")
body += content_section("Which Founder Pack Should You Buy?", "<p>Pick Standard if five-day advance access is the main reason you are buying. Consider Deluxe or Ultimate only if the extra cosmetics and bundle items matter to you personally. Do not upgrade because a pre-launch class prediction says your class will dominate.</p><div class='grid cards'>" + card("Which Edition?", "Compare Standard, Deluxe and Ultimate by purchase intent.", "/founders-pack/which-edition/") + card("Advance Access", "Check the early access timing and prep list.", "/advance-access/") + card("Launch Scale Test", "Try classes and builds before buying deeper.", "/launch-scale-test/") + "</div>")
body += content_section("Founder Pack FAQ", "<div class='table-wrap'><table><thead><tr><th>Question</th><th>Short Answer</th></tr></thead><tbody><tr><th>Does it include early access?</th><td>Yes, the pack messaging is built around five-day advance access before the October 5 launch.</td></tr><tr><th>Should I buy for a class advantage?</th><td>No. Class strength still needs Global verification.</td></tr><tr><th>Is Standard enough?</th><td>For most access-first players, Standard is the safest comparison baseline.</td></tr></tbody></table></div>")
write("founders-pack/", page("AION 2 Founder's Pack Comparison", "AION 2 Founder's Pack comparison for Standard vs Deluxe vs Ultimate, prices, advance access, membership and purchase recommendations.", "founders-pack", body))

body = hero("AION 2 Advance Access", "Founder Pack early access is advertised for September 30, 2026, five days before the full October 5 launch.", "Early Access")
body += content_section("Known Timing", "<div class='timeline'><div><b>September 30, 2026</b><span>Advertised Founder Pack advance access start.</span></div><div><b>October 5, 2026</b><span>Full Global launch date listed on Steam.</span></div></div>")
body += content_section("Should You Play Advance Access?", "<div class='table-wrap'><table><thead><tr><th>Buy Early If</th><th>Wait If</th></tr></thead><tbody><tr><td>You will actually play during the five-day window.</td><td>You are only buying because of unverified class hype.</td></tr><tr><td>You want to test classes, controls and performance before launch rush.</td><td>You prefer waiting for server stability and first community reports.</td></tr><tr><td>You value founder cosmetics or membership items.</td><td>You only care about long-term meta rankings.</td></tr></tbody></table></div>")
body += content_section("Advance Access Checklist", "<ol><li>Confirm PC storage and requirements.</li><li>Pick a primary and backup class.</li><li>Use the launch verification checklist to record patch, class, skill values and dungeon data.</li><li>Do not convert first-hour impressions into final tier claims.</li></ol>")
write("advance-access/", page("AION 2 Advance Access", "AION 2 advance access date, Founder Pack timing and early access preparation checklist.", "advance-access", body))

body = hero("AION 2 Standard vs Deluxe vs Ultimate", "Compare Founder Pack editions by practical launch value instead of pre-launch class hype.", "Edition Compare")
body += content_section("Edition Comparison", "<div class='table-wrap'><table><thead><tr><th>Edition</th><th>Price</th><th>Best Fit</th><th>Main Reason To Buy</th></tr></thead><tbody><tr><th>Standard</th><td>$24.99</td><td>Players who mainly want the five-day head start.</td><td>Lowest listed entry point for advance access.</td></tr><tr><th>Deluxe</th><td>$49.99</td><td>Players who know they want extra launch cosmetics or bundle value.</td><td>Middle option when Standard feels too bare.</td></tr><tr><th>Ultimate</th><td>$99.99</td><td>Collectors and committed players.</td><td>Highest listed package for the largest bundle.</td></tr></tbody></table></div>")
body += content_section("Simple Recommendation", "<ul><li>Pick Standard if access is the only must-have.</li><li>Pick Deluxe only if the extra items are valuable to you personally.</li><li>Pick Ultimate only if you already expect to main the game at launch.</li><li>Skip upgrading just because a pre-launch tier list claims your class will be dominant.</li></ul>")
write("founders-pack/which-edition/", page("AION 2 Standard vs Deluxe vs Ultimate", "AION 2 Standard vs Deluxe vs Ultimate Founder Pack comparison with prices and purchase recommendations.", "founders-pack/which-edition", body))

body = hero("AION 2 Server Status", "Launch Scale Test ended; this hub tracks pre-launch server status, maintenance, queue and connection issue checks for Steam and PURPLE players.", "Status")
body += content_section("Current Status", "<div class='summary'><div><b>AION 2 Global</b><span>No live Global server; pre-launch window before Advanced Access.</span></div><div><b>Steam</b><span>Uninstall the Steam Playtest App and download the full AION 2 client separately for Advanced Access.</span></div><div><b>PURPLE</b><span>No extra client action reported for PURPLE players; keep the launcher ready.</span></div><div><b>Last Updated</b><span>September 19, 2026</span></div></div><p class='source-note'>Launch Scale Test ended. Advanced Access is listed for September 30, 2026, and Official Launch is listed for October 5, 2026. Use official launcher, Steam and publisher notices for the final live status before deciding whether an error is local.</p>")
body += content_section("AION 2 Server Status After LST", "<div class='table-wrap'><table><thead><tr><th>Status Item</th><th>Current Answer</th><th>Related Page</th></tr></thead><tbody><tr><th>Is AION 2 down?</th><td>No live Global server is available between the ended Launch Scale Test and the next access window.</td><td><a href='/launch-scale-test/'>Launch Scale Test</a></td></tr><tr><th>AION 2 maintenance</th><td>Maintenance reports should be checked against official notices once Advanced Access begins.</td><td><a href='/meta/update-log/'>Update Log</a></td></tr><tr><th>Steam server status</th><td>Steam players should separate Playtest App removal, full-client download and live server availability.</td><td><a href='/preload-download/'>Download</a></td></tr><tr><th>PURPLE server status</th><td>PURPLE players should watch launcher login, region access and any publisher notices.</td><td><a href='/preload-download/'>Download</a></td></tr></tbody></table></div>")
body += content_section("Queue Policy To Watch", "<p>When servers are full, the launch flow can use a priority queue and a general queue. Priority queue access is not a guarantee, so a queue screen during Advanced Access may still be normal server-load behavior rather than a local connection problem.</p>")
body += content_section("Why Can't I Connect To AION 2?", "<ol><li>Confirm whether Advanced Access or Official Launch is currently open for your time zone.</li><li>Steam players should remove the Steam Playtest App and install the full AION 2 client for September 30, 2026 access.</li><li>PURPLE players should keep the launcher ready and check official notices before reinstalling.</li><li>If access is open and only one platform is affected, track Steam and PURPLE issues separately from overall server status.</li></ol>")
body += content_section("Server Status FAQ", "<div class='grid cards'>" + card("Does test progress carry over?", "Treat Launch Scale Test progress as temporary test data, not final launch progression.") + card("Should I reinstall after Steam Playtest?", "Steam players should uninstall the Steam Playtest App and download AION 2 separately before Advanced Access.") + card("Where are builds?", "Use post-LST build evidence pages, not endgame KR/TW assumptions.", "/builds/") + "</div>")
write("server-status/", page("AION 2 Server Status - Is AION 2 Down?", "AION 2 server status for Launch Scale Test, maintenance, queue, Steam, PURPLE and connection issue checks.", "server-status", body))

body = hero("AION 2 Preload & Download", "A cautious launch-prep page for download size, storage and preload status.", "Download")
body += content_section("Known Requirement", "<div class='notice'><b>Storage:</b> Steam currently lists 100 GB available space in the minimum requirements.</div>")
body += content_section("Preload Status", "<p>No preload window is published here until it can be verified from an official source or the Steam client. Treat any unverified preload time as a rumor.</p>")
body += content_section("What The 100 GB Requirement Means", "<p>The listed storage requirement should be treated as the minimum free space to reserve before the client is available. Launch downloads can also need temporary patching room, so players with a nearly full drive should clear additional space rather than stopping at exactly 100 GB. If the Steam client later publishes a preload window, this page should record the date, region and source before calling it confirmed.</p>")
body += content_section("Download Prep Checklist", "<ol><li>Free at least 100 GB before advance access.</li><li>Use an SSD where possible because the storefront recommends it.</li><li>Update GPU drivers and Windows before launch day.</li><li>Check server status before assuming a download or login issue is local.</li></ol>")
body += sources_section()
write("preload-download/", page("AION 2 Preload and Download", "AION 2 preload, download and storage preparation page with 100 GB requirement and launch checklist.", "preload-download", body))

body = hero("AION 2 System Requirements", "PC requirements currently listed for the Global Steam release.", "PC Specs")
body += content_section("Minimum PC Requirements", "<div class='table-wrap'><table><thead><tr><th>Component</th><th>Requirement</th></tr></thead><tbody>" + "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in SYSTEM_REQUIREMENTS) + "</tbody></table></div>")
body += content_section("Launch Prep Notes", "<ul><li>Reserve at least 100 GB before advance access begins.</li><li>Use an SSD where possible because the storefront note recommends it.</li><li>Minimum hardware should start with conservative graphics settings, then raise quality after checking performance in crowded areas.</li></ul>")
body += sources_section()
write("system-requirements/", page("AION 2 System Requirements", "AION 2 PC system requirements for OS, CPU, RAM, GPU, DirectX, storage and launch prep.", "system-requirements", body))

body = hero("AION 2 Gameplay", "A pre-launch overview of the confirmed Global gameplay pillars: class-based combat, flight, PvE, PvP, crafting, trading and large-scale world exploration.", "Gameplay")
body += content_section("Confirmed Gameplay Pillars", "<div class='grid facts'><div><b>Class Combat</b><span>Steam describes class-based combat as a core part of AION 2.</span></div><div><b>Flight</b><span>Flight and verticality are positioned as exploration and combat hooks.</span></div><div><b>PvE</b><span>Dungeon content spans solo, 5-player and 10-player formats.</span></div><div><b>PvP</b><span>PvP exists, but Global activity balance still needs live evidence.</span></div><div><b>Crafting</b><span>Crafting is named as part of the Global feature set.</span></div><div><b>Trading</b><span>Trading is named, but launch economy values are unknown.</span></div><div><b>World</b><span>Steam says the world is 36 times larger than the original AION.</span></div><div><b>Engine</b><span>Unreal Engine 5 is listed as the visual foundation.</span></div></div>")
body += content_section("What Is Still Unknown", "<ul><li>Exact Global skill values, cooldowns and class balance.</li><li>Launch economy, trading restrictions and market behavior.</li><li>Progression speed and bottlenecks after early access begins.</li><li>Which regional assumptions carry over cleanly to Global.</li></ul>")
write("gameplay/", page("AION 2 Gameplay", "AION 2 gameplay overview covering class combat, flight, PvE, PvP, crafting, trading and confirmed Global launch facts.", "gameplay", body))

body = hero("AION 2 PvE Content", "Confirmed PvE scope for Global launch preparation, focused on dungeon formats, seasonal challenges, rankings and open-world events.", "PvE")
body += content_section("Confirmed PvE Formats", "<div class='summary'><div><b>Solo</b><span>Solo dungeon format is named on Steam.</span></div><div><b>5-Player</b><span>Party dungeon format is named on Steam.</span></div><div><b>10-Player</b><span>Larger group dungeon format is named on Steam.</span></div><div><b>200+</b><span>Steam describes over 200 dungeons.</span></div></div>")
body += content_section("Other PvE Systems", "<ul><li>Seasonal challenges are named as recurring PvE content.</li><li>Competitive rankings are named, which makes versioned meta tracking important.</li><li>Open-world events are named, but schedules and reward tables need Global verification.</li></ul>")
body += content_section("Launch Tracking Plan", "<p>After advance access starts, this page should track dungeon names, requirements, boss mechanics, reward types, class performance and patch-specific changes.</p>")
body += sources_section()
write("pve-content/", page("AION 2 PvE Content", "AION 2 PvE content overview for dungeons, solo, 5-player, 10-player, seasonal challenges and open-world events.", "pve-content", body))

body = hero("AION 2 Flight Combat", "Flight and vertical movement are a core Global marketing point, but exact combat advantages still need launch-client testing.", "Combat System")
body += content_section("What Is Confirmed", "<p>Steam positions flight and verticality as central to combat and exploration. That matters for class evaluation because ranged uptime, melee gap-closing, line of sight, terrain and aerial positioning can all change how a class feels.</p>")
body += content_section("What To Test", "<div class='table-wrap'><table><thead><tr><th>Test Area</th><th>Why It Matters</th></tr></thead><tbody><tr><th>Ranged uptime</th><td>Flight can make spacing easier or harder depending on encounter design.</td></tr><tr><th>Melee access</th><td>Gap closing and target stickiness may decide PvP strength.</td></tr><tr><th>Boss arenas</th><td>Vertical mechanics may change dungeon class value.</td></tr><tr><th>Resource limits</th><td>Flight duration or restrictions can change open-world routing.</td></tr></tbody></table></div>")
body += sources_section()
write("flight-combat/", page("AION 2 Flight Combat", "AION 2 flight combat overview and launch testing checklist for verticality, movement, PvE and PvP impact.", "flight-combat", body))

body = hero("AION 2 Character Customization", "Steam describes over 200 customization options for Global launch.", "Customization")
body += content_section("Confirmed Customization Scope", "<div class='notice'><b>Official pre-launch claim:</b> Steam describes over 200 character customization options.</div>")
body += content_section("What The Claim Does And Does Not Prove", "<p>The storefront claim is useful for launch preparation, but it does not yet tell players how those options are distributed across face, body, hair, voice, color, presets or post-creation editing. It also does not prove whether every option is available to every account, whether some cosmetics are founder bonuses, or whether appearance changes can be edited freely after character creation.</p>")
body += content_section("What To Track At Launch", "<ul><li>Body, face, hair and color option categories.</li><li>Whether any appearance options are tied to Founder Pack items or shop purchases.</li><li>Character creation limits such as name rules and slot count.</li><li>Cosmetic availability by edition and region.</li><li>Whether saved presets, randomization and post-creation edits exist in the Global client.</li></ul>")
body += sources_section()
write("character-customization/", page("AION 2 Character Customization", "AION 2 character customization overview with confirmed 200+ customization option claim and launch tracking checklist.", "character-customization", body))

body = hero("AION 2 Global vs KR/TW Meta", "The core editorial difference: reference regional data without presenting it as verified Global truth.", "Meta Method")
body += content_section("Comparison", "<div class='table-wrap'><table><thead><tr><th>Topic</th><th>KR/TW</th><th>Global</th></tr></thead><tbody><tr><th>Classes</th><td>Existing live environment.</td><td>Launch roster tracked separately.</td></tr><tr><th>Balance</th><td>Regional live patches.</td><td>Global build must be verified.</td></tr><tr><th>Tier Lists</th><td>Useful reference.</td><td>TBD until tested.</td></tr><tr><th>Economy</th><td>Mature market.</td><td>Unknown launch market.</td></tr><tr><th>PvP Meta</th><td>Established assumptions.</td><td>Needs Global population and ruleset evidence.</td></tr><tr><th>Dungeons</th><td>May reveal mechanics and content patterns.</td><td>Names, rewards and tuning must be confirmed on Global.</td></tr></tbody></table></div>")
body += content_section("Why Regional Data Can Mislead", "<p>Regional versions can be useful for deciding what to test first, but they can mislead Global players when patch timing, monetization, economy maturity, server population or launch roster differs. A build that is stable in an older live environment may be wrong for a fresh Global economy, and a PvP matchup that depends on experienced players may not describe launch-week behavior.</p>")
body += content_section("How This Site Uses KR/TW Reference", "<ol><li>Use regional data to form test hypotheses.</li><li>Label it as KR/TW Reference, never Global Verified.</li><li>Retest in the Global client before updating ranks or build recommendations.</li><li>Log every rank change with patch, date and reason.</li></ol>")
body += sources_section()
write("meta/global-vs-korea/", page("AION 2 Global vs Korea Meta", "AION 2 Global vs KR/TW meta comparison for class balance, economy, PvP and dungeon assumptions, with evidence policy labels.", "meta/global-vs-korea", body))

meta_hub_cards = card("Global vs KR/TW", "Separate regional reference from Global proof.", "/meta/global-vs-korea/", "Meta")
meta_hub_cards += "".join(card(label, f"Meta operations and evidence framework for {label.lower()}.", href, "Meta") for href, label in META_PAGES if href.startswith("/meta/"))
body = hero("AION 2 Meta Hub", "Evidence policy, update log, Global-vs-regional comparison and launch verification workflow.", "Meta Hub")
body += content_section("Meta Operations", f"<div class='grid cards'>{meta_hub_cards}</div>")
body += content_section("Why This Exists", "<p>AION2Meta.wiki is built around versioned evidence. The Meta section explains when a claim is official, when it is Global Verified, and when it is only a KR/TW reference or an unconfirmed report.</p>")
write("meta/", page("AION 2 Meta Hub", "AION 2 Meta hub for evidence policy, update log, Global vs KR/TW comparison and launch verification workflow.", "meta", body))

body = hero("AION 2 Evidence Policy", "How AION2Meta.wiki decides whether a rank, build or guide claim is ready to publish.", "Editorial Policy")
body += content_section("Evidence Labels", "<div class='table-wrap'><table><thead><tr><th>Label</th><th>Meaning</th><th>Allowed Use</th></tr></thead><tbody><tr><th>Official</th><td>Publisher, official site or storefront information.</td><td>Dates, platform facts, feature claims and requirements.</td></tr><tr><th>Global Verified</th><td>Tested in the Global client or confirmed from repeatable Global evidence.</td><td>Tier ranks, build recommendations, dungeon mechanics and progression advice.</td></tr><tr><th>KR/TW Reference</th><td>Information from existing regional versions.</td><td>Hypotheses and comparison notes, not final Global claims.</td></tr><tr><th>Unconfirmed</th><td>Community reports or expected behavior without enough proof.</td><td>Tracking queues, never final recommendations.</td></tr></tbody></table></div>")
body += content_section("Ranking Rules", "<ol><li>No class receives a final rank without patch, date, evidence type and reason.</li><li>PvE, solo, 1v1, small-scale PvP and large-scale PvP are tracked separately.</li><li>KR/TW information can influence what to test, but cannot be presented as Global proof.</li><li>Every changed rating should create an update-log entry.</li></ol>")
write("meta/evidence-policy/", page("AION 2 Evidence Policy", "AION 2 Meta evidence policy for Official, Global Verified, KR/TW Reference and Unconfirmed information.", "meta/evidence-policy", body))

body = hero("AION 2 Meta Update Log", "A public changelog for class rankings, build changes and confirmed launch facts.", "Update Log")
body += content_section("Current Entries", "<div class='timeline'><div><b>September 13, 2026</b><span>Pre-launch site skeleton created with official Steam facts, class structure, Founder Pack prices, system requirements and TBD tier matrix.</span></div><div><b>September 30, 2026</b><span>Planned: advance access verification pass for class data, dungeon names, build values and early meta movement.</span></div><div><b>October 5, 2026</b><span>Planned: full launch verification pass and first Global Verified tier updates where evidence is sufficient.</span></div></div>")
body += content_section("What Gets Logged", "<ul><li>Tier movement with reason and patch context.</li><li>Build page updates after skill, stat or gear verification.</li><li>Dungeon requirement, boss mechanic and reward confirmations.</li><li>Corrections when a pre-launch assumption proves wrong.</li></ul>")
write("meta/update-log/", page("AION 2 Meta Update Log", "AION 2 Meta update log for class rankings, builds, dungeon data and launch verification changes.", "meta/update-log", body))

body = hero("AION 2 Launch Verification Checklist", "A working checklist for turning pre-launch TBD pages into Global Verified class, build and dungeon pages after access opens.", "Operations")
body += content_section("First 24 Hours", "<div class='table-wrap'><table><thead><tr><th>Task</th><th>Pages Affected</th><th>Evidence Required</th></tr></thead><tbody><tr><th>Confirm client patch and server region</th><td>All tier and build pages</td><td>Patch label, date and screenshot or official note.</td></tr><tr><th>Record launch class roster</th><td>Classes, best class, tier matrix</td><td>Global client roster check.</td></tr><tr><th>Capture skill values</th><td>8 build pages</td><td>Skill names, cooldowns, effects and any unlocked variants.</td></tr><tr><th>Test solo comfort</th><td>Solo tier, beginner tier, class pages</td><td>Repeatable leveling or solo dungeon observations.</td></tr><tr><th>List first dungeon names</th><td>Dungeons, PvE content</td><td>Requirements, format, bosses and reward screenshots.</td></tr></tbody></table></div>")
body += content_section("Do Not Update A Rank Until", "<ol><li>The activity is clear: Solo, Dungeon, Raid, 1v1 PvP, Small PvP, Large PvP or Beginner.</li><li>The page can state the Global patch and last tested date.</li><li>The claim has repeatable evidence or a clearly labeled official source.</li><li>The update log records what changed and why.</li></ol>")
body += content_section("Update Order", "<div class='timeline'><div><b>1. Release Date / Status</b><span>Confirm access, server status and any launch delay.</span></div><div><b>2. Classes</b><span>Confirm roster, role labels and class page basics.</span></div><div><b>3. Builds</b><span>Fill skill values and early stat priorities only after client checks.</span></div><div><b>4. Tier Lists</b><span>Move TBD to ranks only where activity-specific evidence exists.</span></div><div><b>5. Dungeons</b><span>Create individual dungeon pages only after name, mechanics and rewards are verified.</span></div></div>")
write("meta/launch-verification-checklist/", page("AION 2 Launch Verification Checklist", "AION 2 launch verification checklist for updating class rankings, builds, dungeon data and Global evidence labels.", "meta/launch-verification-checklist", body))

body = hero("AION 2 Dungeons", "Launch Scale Test dungeon hub for Global dungeon names, level requirements, party setup, boss mechanics and rewards.", "Dungeon Hub")
body += content_section("Launch Scale Test Dungeon Tracking", "<div class='summary'><div><b>Total Scope</b><span>Over 200 dungeons described on Steam.</span></div><div><b>Solo</b><span>Track solo challenge availability.</span></div><div><b>Party</b><span>Track 5-player requirements and roles.</span></div><div><b>Group</b><span>Track 10-player requirements when visible.</span></div></div>")
body += content_section("What Players Need First", "<div class='table-wrap'><table><thead><tr><th>Need</th><th>What This Page Will Record</th></tr></thead><tbody><tr><th>Dungeon level requirements</th><td>Unlock level, entry rules and whether it fits the level 37 test cap.</td></tr><tr><th>Recommended party setup</th><td>Tank, healer, support and DPS needs without turning one run into a tier claim.</td></tr><tr><th>Boss mechanics</th><td>Named boss patterns, avoidable damage and wipe points.</td></tr><tr><th>Dungeon rewards</th><td>Gear, materials and progression relevance once verified.</td></tr></tbody></table></div>")
body += content_section("Why This Hub Exists Now", "<p>GSC already shows early dungeon demand, but individual dungeon pages should wait for verified Global names and mechanics. This hub captures the demand without inventing dozens of thin URLs before the test produces real data.</p>")
body += content_section("Launch Verification Priorities", "<ul><li>Record the first dungeon names exactly as they appear in the Global client.</li><li>Separate solo, 5-player and 10-player content instead of merging them into one list.</li><li>Capture requirements, boss names, mechanics and reward screenshots before publishing an individual dungeon page.</li><li>Track which classes feel valuable by activity, but avoid turning one dungeon impression into a site-wide tier claim.</li></ul>")
body += sources_section()
write("dungeons/", page("AION 2 Dungeons", "AION 2 dungeon hub for Launch Scale Test level requirements, party setup, boss mechanics and rewards.", "dungeons", body))

body = hero("Page Not Found", "This AION 2 Meta page does not exist yet, or it may be waiting for Global verification.", "404")
body += content_section("Find The Right Page", "<div class='grid cards'>" + card("Classes", "Compare the launch class roster.", "/classes/") + card("Tier Lists", "Open the Global tier matrix.", "/tier-list/") + card("Guides", "Read launch preparation guides.", "/guides/") + card("Update Log", "Check what changed recently.", "/meta/update-log/") + "</div>")
write("404.html", page("Page Not Found", "AION 2 Meta 404 page with links to classes, tier lists, guides and update log.", "404", body))

styles = r"""
:root{color-scheme:dark;--bg:#080a0f;--panel:#111722;--panel2:#171f2d;--text:#edf4ff;--muted:#a9b6c8;--line:#293448;--gold:#f2c36b;--blue:#76d5ff;--red:#ff7e79;--green:#86e3b2;--shadow:0 24px 80px rgba(0,0,0,.35)}*{box-sizing:border-box}body{margin:0;background:radial-gradient(circle at 20% 0%,rgba(118,213,255,.18),transparent 34rem),radial-gradient(circle at 90% 12%,rgba(242,195,107,.14),transparent 28rem),var(--bg);color:var(--text);font-family:Inter,ui-sans-serif,system-ui,-apple-system,Segoe UI,Arial,sans-serif;line-height:1.6}a{color:inherit}.skip{position:absolute;left:-999px}.skip:focus{left:1rem;top:1rem;z-index:99;background:#fff;color:#000;padding:.5rem 1rem}.site-header{position:sticky;top:0;z-index:10;display:flex;align-items:center;justify-content:space-between;gap:1rem;padding:1rem clamp(1rem,4vw,4rem);border-bottom:1px solid rgba(255,255,255,.1);background:rgba(8,10,15,.82);backdrop-filter:blur(14px)}.brand{display:flex;align-items:center;gap:.7rem;text-decoration:none;font-weight:800}.brand-mark{display:grid;place-items:center;width:2.35rem;height:2.35rem;border:1px solid rgba(242,195,107,.5);background:linear-gradient(145deg,#1b2534,#0c1017);color:var(--gold);font-size:.85rem}.site-header nav{display:flex;gap:.35rem;flex-wrap:wrap}.site-header nav a{padding:.55rem .75rem;border-radius:.35rem;color:var(--muted);text-decoration:none;font-size:.92rem}.site-header nav a:hover,.site-header nav a:focus{background:rgba(255,255,255,.08);color:var(--text)}.hero{min-height:clamp(520px,70vh,760px);display:grid;grid-template-columns:minmax(0,1.15fr) minmax(280px,.65fr);gap:2rem;align-items:center;padding:clamp(3rem,7vw,7rem) clamp(1rem,4vw,4rem);border-bottom:1px solid rgba(255,255,255,.1)}.hero h1{font-size:clamp(2.8rem,7vw,6.8rem);line-height:.9;letter-spacing:0;margin:.4rem 0 1.3rem;max-width:11ch}.lead{font-size:clamp(1.1rem,2.2vw,1.45rem);color:#d8e4f5;max-width:43rem}.eyebrow{margin:0;color:var(--gold);font-weight:800;text-transform:uppercase;font-size:.78rem;letter-spacing:.12em}.hero-actions{display:flex;gap:.8rem;flex-wrap:wrap;margin-top:1.7rem}.button,.card-link{display:inline-flex;align-items:center;justify-content:center;min-height:44px;padding:.72rem 1rem;border:1px solid rgba(255,255,255,.16);border-radius:.35rem;text-decoration:none;font-weight:800;background:rgba(255,255,255,.06)}.button.primary{background:var(--gold);color:#12100a;border-color:var(--gold)}.status-panel,.card,.notice{background:linear-gradient(180deg,rgba(23,31,45,.92),rgba(12,16,23,.92));border:1px solid rgba(255,255,255,.12);box-shadow:var(--shadow);padding:1.25rem}.status-panel{align-self:stretch;display:flex;flex-direction:column;justify-content:end;min-height:24rem}.status-dot{width:.8rem;height:.8rem;border-radius:99px;background:var(--red);box-shadow:0 0 0 .45rem rgba(255,126,121,.12);margin-bottom:1rem}.status-panel dl{display:grid;gap:.7rem;margin:1rem 0 0}.status-panel dl div,.summary div,.timeline div{display:flex;justify-content:space-between;gap:1rem;border-top:1px solid rgba(255,255,255,.1);padding-top:.75rem}.status-panel dt,.summary b{color:var(--muted)}.status-panel dd{margin:0;font-weight:800}.section{padding:clamp(2.5rem,5vw,5rem) clamp(1rem,4vw,4rem);max-width:1320px;margin:0 auto}.section h2{font-size:clamp(1.8rem,3vw,3rem);line-height:1.05;margin:0 0 1.2rem}.grid{display:grid;gap:1rem}.cards{grid-template-columns:repeat(3,minmax(0,1fr))}.facts{grid-template-columns:repeat(4,minmax(0,1fr))}.facts div{border:1px solid rgba(255,255,255,.12);background:rgba(255,255,255,.055);padding:1rem}.facts b{display:block;color:var(--gold);margin-bottom:.35rem}.facts span{color:#d8e4f5}.source-note{color:var(--muted);max-width:62rem}.card{min-height:14rem;display:flex;flex-direction:column}.card h3{font-size:1.35rem;margin:.3rem 0 .5rem}.card p{color:var(--muted);margin:0 0 1rem}.card-link{margin-top:auto;width:max-content}.table-wrap{overflow:auto;border:1px solid rgba(255,255,255,.13);background:rgba(17,23,34,.72)}table{width:100%;border-collapse:collapse;min-width:760px}caption{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}th,td{text-align:left;padding:1rem;border-bottom:1px solid rgba(255,255,255,.1);vertical-align:top}thead th{color:var(--gold);font-size:.78rem;text-transform:uppercase;letter-spacing:.08em}tbody th{white-space:nowrap}.pill{display:inline-flex;min-width:3rem;justify-content:center;padding:.25rem .55rem;border-radius:99px;background:rgba(255,255,255,.08);font-weight:800;font-size:.78rem}.pill.muted{color:var(--muted)}.summary{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:1rem}.summary div{display:block;background:rgba(255,255,255,.05);padding:1rem;border:1px solid rgba(255,255,255,.1)}.summary span{display:block;margin-top:.35rem}.evidence-row{display:flex;flex-wrap:wrap;gap:.7rem}.evidence-row span{padding:.55rem .75rem;border:1px solid rgba(255,255,255,.13);background:rgba(255,255,255,.06);font-weight:800}.tabs{border:1px solid rgba(255,255,255,.13);background:rgba(17,23,34,.72);padding:1rem}.tabs [role=tablist]{display:flex;gap:.5rem;flex-wrap:wrap;border-bottom:1px solid rgba(255,255,255,.12);padding-bottom:.8rem}.tabs button{min-height:44px;padding:.6rem 1rem;border:1px solid rgba(255,255,255,.18);background:transparent;color:var(--text);font-weight:800;border-radius:.3rem}.tabs button.active{background:var(--blue);color:#061018;border-color:var(--blue)}.timeline{display:grid;gap:1rem;max-width:760px}.timeline div{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);padding:1rem}.site-footer{display:grid;grid-template-columns:1fr 1fr;gap:2rem;margin-top:3rem;padding:2rem clamp(1rem,4vw,4rem);border-top:1px solid rgba(255,255,255,.1);color:var(--muted)}.site-footer strong{color:var(--text);font-size:1.25rem}.small{font-size:.86rem}@media (max-width:1040px){.facts{grid-template-columns:repeat(2,minmax(0,1fr))}}@media (max-width:880px){.site-header{align-items:flex-start;flex-direction:column}.hero{grid-template-columns:1fr;min-height:auto}.hero h1{max-width:12ch}.cards{grid-template-columns:1fr}.summary{grid-template-columns:1fr 1fr}.site-footer{grid-template-columns:1fr}}@media (max-width:520px){.facts,.summary{grid-template-columns:1fr}.hero{padding-top:2rem}.site-header nav a{padding:.45rem .5rem}.status-panel{min-height:auto}.section{padding-block:2rem}}
"""
write("assets/styles.css", styles)

favicon = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="AION 2 Meta">
  <rect width="64" height="64" rx="10" fill="#080a0f"/>
  <path d="M12 48 29 14h6l17 34h-8l-3.4-7.4H23.4L20 48h-8Zm14.4-14h11.2L32 21.7 26.4 34Z" fill="#f2c36b"/>
  <path d="M42 16h10v6H42v-6Zm0 10h10v6H42v-6Z" fill="#76d5ff"/>
</svg>
"""
write("assets/favicon.svg", favicon)

manifest = {
    "name": SITE["name"],
    "short_name": "AION2Meta",
    "description": SITE["tagline"],
    "start_url": "/",
    "display": "standalone",
    "background_color": "#080a0f",
    "theme_color": "#080a0f",
    "icons": [{"src": "/assets/favicon.svg", "sizes": "any", "type": "image/svg+xml"}],
}
write("site.webmanifest", json.dumps(manifest, ensure_ascii=False, indent=2))

script = r"""
document.querySelectorAll('[data-tabs]').forEach((tabs) => {
  const buttons = tabs.querySelectorAll('[data-tab]');
  const panels = tabs.querySelectorAll('[data-panel]');
  buttons.forEach((button) => {
    button.addEventListener('click', () => {
      buttons.forEach((item) => {
        const selected = item === button;
        item.classList.toggle('active', selected);
        item.setAttribute('aria-selected', String(selected));
      });
      panels.forEach((panel) => panel.hidden = panel.dataset.panel !== button.dataset.tab);
    });
  });
});
"""
write("assets/site.js", script)

all_urls = ["/", "/classes/", "/builds/", "/tier-list/", "/guides/", "/meta/", "/release-date/", "/founders-pack/", "/system-requirements/", "/dungeons/", "/meta/global-vs-korea/"]
all_urls += [href for href, _ in PRELAUNCH_PAGES]
all_urls += [href for href, _ in META_PAGES]
all_urls += [f"/classes/{slug}/" for slug, *_ in CLASSES]
all_urls += [f"/builds/{slug}-build/" for slug, *_ in CLASSES]
all_urls += [f"/tier-list/{slug}/" for slug in tier_pages]
all_urls += [f"/guides/{slug}/" for slug in guide_pages]
sitemap = "\n".join(f"https://{SITE['domain']}{u}" for u in all_urls)
write("sitemap.txt", sitemap)
xml_sitemap = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n" + "\n".join(
    f"  <url><loc>https://{SITE['domain']}{u}</loc><lastmod>2026-09-19</lastmod><changefreq>{'daily' if u in ['/', '/meta/update-log/', '/tier-list/class-tier-list/', '/server-status/', '/launch-scale-test/', '/builds/'] else 'weekly'}</changefreq><priority>{'1.0' if u == '/' else '0.8'}</priority></url>"
    for u in all_urls
) + "\n</urlset>\n"
write("sitemap.xml", xml_sitemap)
write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: https://{SITE['domain']}/sitemap.xml\n")
write("CNAME", f"{SITE['domain']}\n")

print(f"Generated {len(all_urls)} pages in {ROOT}")
