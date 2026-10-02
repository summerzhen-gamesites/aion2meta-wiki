from pathlib import Path
from html import escape
import json
import os

BASE = Path(__file__).parent
ROOT = Path(os.environ.get("AION2_OUTPUT_DIR", BASE))
SITE = {
    "name": "AION 2 Meta",
    "domain": "aion2meta.wiki",
    "tagline": "Global builds, tier lists and class guides for the latest AION 2 patch.",
    "updated": "October 1, 2026",
    "updated_iso": "2026-10-01",
    "phase": "Advanced Access live",
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

CLASS_GUIDES = {
    "gladiator": {"fit": "Choose Gladiator if you want to stay in the fight, pressure nearby targets and trade burst precision for a forgiving frontline rhythm.", "strengths": "Durable melee presence; readable engage-and-pressure plan; suited to players who value uptime.", "tradeoffs": "Must manage damage while staying close; loses value when mechanics deny melee uptime.", "pve": "Stay on target, preserve mobility for mechanics and align heavy attacks with safe damage windows.", "pvp": "Apply frontline pressure without chasing through control; save mobility or defense for the counter-engage.", "solo": "Pull deliberately, group only what you can control and keep one recovery option available.", "loop": "Approach safely → establish pressure → spend the damage window → defend through retaliation → re-engage.", "stats": "Confirm weapon scaling and offensive breakpoints first; compare damage gain with the survival needed to maintain melee uptime."},
    "templar": {"fit": "Choose Templar if you enjoy leading pulls, protecting teammates and controlling where enemies face and move.", "strengths": "Clear tank identity; defensive control; strong group purpose for players comfortable with responsibility.", "tradeoffs": "Success may depend on positioning and cooldown timing; solo kills may feel slower than dedicated damage classes.", "pve": "Establish threat, turn attacks away from the party and rotate mitigation around boss patterns.", "pvp": "Protect vulnerable allies, disrupt enemy setups and use control to create space.", "solo": "Favor reliable damage and low downtime while keeping a defensive reserve for elites or adds.", "loop": "Start the pull → secure attention and position → answer the dangerous mechanic → refresh threat/control → preserve an emergency defense.", "stats": "Verify threat and mitigation rules before committing to a defensive stack; add offense only when survival and aggro are stable."},
    "assassin": {"fit": "Choose Assassin if you enjoy target selection, positional play and short commitment windows where timing matters most.", "strengths": "Focused melee burst identity; rewards planning, movement and recognizing exposed targets.", "tradeoffs": "Punishing when an engage is mistimed; vulnerable to control and forced downtime.", "pve": "Maintain positional access, prepare resources before burst and avoid losing a full sequence to mechanics.", "pvp": "Find an exposed target, force a defensive response and leave before counter-control arrives.", "solo": "Control pull size and prioritize clean kills; mobility is part of survival, not only damage uptime.", "loop": "Prepare resources → approach safely → apply setup/control → commit burst → disengage or reset.", "stats": "Validate accuracy and positional or critical interactions before chasing burst stats; compare peak damage with consistency."},
    "ranger": {"fit": "Choose Ranger if you want physical ranged pressure, active spacing and safe attack opportunities while moving.", "strengths": "Ranged access; kiting identity; flexible target switching and clear mechanic visibility.", "tradeoffs": "Poor spacing erases the range advantage; control and movement must be planned.", "pve": "Use range to keep uptime, pre-position for the next safe lane and stay within group support.", "pvp": "Create distance before committing damage, deny approaches and switch targets when a chase breaks position.", "solo": "Open from range, slow the approach and move toward cleared ground; save an escape for failed control.", "loop": "Open at range → establish spacing/control → pressure while moving → disengage from contact → reopen.", "stats": "Confirm accuracy, attack-speed and movement constraints; prioritize consistent ranged uptime before theoretical burst."},
    "chanter": {"fit": "Choose Chanter if you want to improve a party through buffs and utility while still contributing direct damage.", "strengths": "Hybrid support identity; adapts between contribution and recovery; rewards group awareness.", "tradeoffs": "Value is wasted when buffs or recovery are mistimed; personal output misses support contribution.", "pve": "Maintain valuable group effects, deal damage during stable periods and reserve utility for predictable pressure.", "pvp": "Stay close enough to support allies without becoming an easy focus; extend engages or blunt burst.", "solo": "Balance damage with sustain to reduce downtime; do not copy a group setup that cannot finish solo fights.", "loop": "Establish buffs → contribute damage → watch allies and enemy setup → respond with utility/recovery → refresh effects.", "stats": "Verify buff scaling, support effect rules and healing coefficients; judge gear by party contribution and uptime."},
    "cleric": {"fit": "Choose Cleric if you want primary responsibility for recovery, cleansing and keeping a group stable.", "strengths": "Direct healer identity; clear party value; rewards encounter knowledge and calm triage.", "tradeoffs": "High awareness burden; inefficient timing creates resource pressure; may be focused early in PvP.", "pve": "Use efficient healing for routine damage, reserve strong recovery for spikes and cleanse only worthwhile effects.", "pvp": "Position behind cover or allies, anticipate burst and protect your escape.", "solo": "Use a damage-forward setup while retaining self-recovery; avoid costly overhealing.", "loop": "Pre-position → maintain efficient recovery → identify the next spike → heal/cleanse appropriately → reposition.", "stats": "Confirm healing coefficients, resource regeneration and cast constraints; prioritize reliable throughput and uptime."},
    "sorcerer": {"fit": "Choose Sorcerer if you want ranged magical burst, deliberate cast windows and planned control.", "strengths": "Clear burst-caster identity; ranged visibility; control can protect a planned damage window.", "tradeoffs": "Interrupted or unsafe casts reduce output sharply; poor positioning leaves few answers at close range.", "pve": "Plan casts around movement, hold burst for stable windows and move early rather than cancel late.", "pvp": "Create space, wait out interrupts and commit burst only when the target cannot deny the sequence.", "solo": "Open with control or range, finish priority enemies first and save repositioning for failed control.", "loop": "Pre-position → setup/control → cast burst → use low-commitment pressure while recovering → relocate.", "stats": "Validate cast-speed, accuracy and critical interactions; compare reliable casts with theoretical burst under movement."},
    "spiritmaster": {"fit": "Choose Spiritmaster if you enjoy managing a companion, sustained pressure and situational utility.", "strengths": "Pet-and-utility identity; layered pressure; flexible answers for players willing to manage more systems.", "tradeoffs": "Pet behavior and target access affect consistency; more effects and timers increase decision load.", "pve": "Keep the pet on a valid target, maintain valuable effects without waste and reserve utility for mechanics.", "pvp": "Pressure through multiple sources, limit enemy options and protect the pet and your position during resets.", "solo": "Let the pet control contact, pull deliberately and use sustained effects to keep moving.", "loop": "Set pet target → establish sustained effects → apply utility/control → refresh expiring effects → redirect or reset.", "stats": "Verify pet inheritance, debuff rules and duration first; measure pet and player scaling separately."},
}

OFFICIAL_FACTS = [
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
    ("/server-status/", "Server Status"),
    ("/codes/", "Codes"),
    ("/tier-list/class-tier-list/", "Tier Lists"),
    ("/classes/", "Classes"),
    ("/builds/", "Builds"),
    ("/dungeons/", "Dungeons"),
    ("/guides/", "Guides"),
]

BREADCRUMB_LABELS = {
    "builds": "Builds",
    "classes": "Classes",
    "codes": "Codes",
    "dungeons": "Dungeons",
    "guides": "Guides",
    "meta": "Meta",
    "pve-content": "PvE Content",
    "pvp-guide": "PvP Guide",
    "server-status": "Server Status",
    "system-requirements": "System Requirements",
    "tier-list": "Tier Lists",
}

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
    ("/advance-access/", "Advance Access"),
    ("/founders-pack/which-edition/", "Which Edition"),
    ("/preload-download/", "Preload & Download"),
]

LIVE_PAGES = [
    ("/server-status/", "Server Status"),
    ("/codes/", "Redeem Codes"),
    ("/servers/", "Server Guide"),
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

def breadcrumb_label(part):
    return BREADCRUMB_LABELS.get(part, part.replace("-", " ").title())

def card(title, text, href=None, meta=None):
    link = f'<a class="card-link" href="{href}">Open</a>' if href else ""
    meta_html = f'<p class="eyebrow">{escape(meta)}</p>' if meta else ""
    return f'<article class="card">{meta_html}<h3>{escape(title)}</h3><p>{escape(text)}</p>{link}</article>'

def page(title, description, slug, main, extra_class=""):
    main = main.replace("<div class='table-wrap'><table><thead>", f"<div class='table-wrap'><table><caption>{escape(title)} data table</caption><thead>")
    nav = "".join(f'<a href="{href}">{label}</a>' for href, label in NAV)
    canonical = f"https://{SITE['domain']}{url_for(slug)}"
    analytics = analytics_head()
    analytics = f"\n{analytics}" if analytics else ""
    page_name = title if slug == "index" else f"{title} | {SITE['name']}"
    path_parts = [part for part in url_for(slug).strip("/").split("/") if part]
    breadcrumb_items = [{"@type": "ListItem", "position": 1, "name": SITE["name"], "item": f"https://{SITE['domain']}/"}]
    current_path = ""
    for index, part in enumerate(path_parts, start=2):
        current_path += f"/{part}"
        breadcrumb_items.append({"@type": "ListItem", "position": index, "name": breadcrumb_label(part), "item": f"https://{SITE['domain']}{current_path}/"})
    website_id = f"https://{SITE['domain']}/#website"
    page_id = f"{canonical}#webpage"
    page_type = "CollectionPage" if slug in {"index", "classes", "builds", "tier-list", "guides", "meta", "dungeons"} else "WebPage"
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "WebSite", "@id": website_id, "name": SITE["name"], "url": f"https://{SITE['domain']}/", "description": SITE["tagline"], "inLanguage": "en"},
            {"@type": page_type, "@id": page_id, "name": title, "url": canonical, "description": description, "inLanguage": "en", "dateModified": SITE["updated_iso"], "isPartOf": {"@id": website_id}, "about": {"@type": "VideoGame", "name": "AION 2", "url": "https://store.steampowered.com/app/3393110/AION_2/"}},
            {"@type": "BreadcrumbList", "@id": f"{canonical}#breadcrumb", "itemListElement": breadcrumb_items},
        ],
    }
    robots = "noindex,follow" if slug == "404" else "index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1"
    if slug == "404":
        canonical_link = "<!-- no canonical for this non-indexable page -->"
    else:
        canonical_link = f'<link rel="canonical" href="{canonical}">'  # indexed page
    breadcrumb_nav = ""
    if path_parts:
        visible_crumbs = ['<a href="/">Home</a>']
        current_path = ""
        for index, part in enumerate(path_parts):
            current_path += f"/{part}"
            label = escape(breadcrumb_label(part))
            visible_crumbs.append(f'<span aria-hidden="true">/</span><span aria-current="page">{label}</span>' if index == len(path_parts) - 1 else f'<span aria-hidden="true">/</span><a href="{current_path}/">{label}</a>')
        breadcrumb_nav = f'<nav class="breadcrumbs" aria-label="Breadcrumb">{"".join(visible_crumbs)}</nav>'
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(page_name)}</title>
  <meta name="description" content="{escape(description)}">
  <meta name="robots" content="{robots}">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  {canonical_link}
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{SITE['name']}">
  <meta property="og:title" content="{escape(page_name)}">
  <meta property="og:description" content="{escape(description)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:locale" content="en_US">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{escape(page_name)}">
  <meta name="twitter:description" content="{escape(description)}">
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
  <main id="content">{breadcrumb_nav}{main}</main>
  <footer class="site-footer">
    <div>
      <strong>{SITE['name']}</strong>
      <p>{SITE['tagline']} Current status: {SITE['phase']}. Last updated: {SITE['updated']}.</p>
    </div>
    <div><p class="small">Unofficial fan resource. AION 2 belongs to its respective publisher and developer. Pages distinguish Official, KR/TW Reference, Global Verified and Unconfirmed information.</p><nav class="footer-links" aria-label="Footer"><a href="/release-date/">Release Date</a><a href="/system-requirements/">System Requirements</a><a href="/meta/evidence-policy/">Evidence Policy</a><a href="/meta/update-log/">Update Log</a></nav></div>
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
      <a class="button primary" href="/server-status/">Check Server Status</a>
      <a class="button" href="/codes/">View Active Codes</a>
    </div>
  </div>
  <div class="status-panel" aria-label="Global service status">
    <span class="status-dot" style="background:var(--green);box-shadow:0 0 0 .45rem rgba(134,227,178,.12)"></span>
    <strong>Current Global Status</strong>
    <p><b>Advanced Access: Live.</b> The latest official update says all servers returned online after October 1 maintenance. Official Global Launch: Oct 5, 2026.</p>
    <dl><div><dt>Service</dt><dd>Online</dd></div><div><dt>Last official update</dt><dd>Oct 1, 2026</dd></div><div><dt>Official Global Launch</dt><dd>Oct 5, 2026</dd></div></dl>
  </div>
</section>"""

def matrix():
    cols = ["Solo", "Dungeon", "Raid", "1v1 PvP", "Small PvP", "Large PvP", "Beginner Complexity"]
    rows = []
    for slug, name, *_ in CLASSES:
        cells = "".join("<td><span class='pill muted'>Unranked</span></td>" for _ in cols[:-1])
        complexity = "High" if slug in {"assassin", "spiritmaster"} else "Medium"
        rows.append(f"<tr><th><a href='/classes/{slug}/'>{name}</a></th>{cells}<td>{complexity}</td></tr>")
    head = "".join(f"<th>{c}</th>" for c in ["Class"] + cols)
    return table_html("AION 2 Global class tier matrix with currently unranked results and beginner complexity", f"<tr>{head}</tr>", "".join(rows), "tier-matrix")

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
    return "<p class='source-note'>Source status: Steam and publisher notices are treated as Official. Advanced Access observations are labeled separately; class ranking, build strength, economy and PvP dominance remain unverified until repeatable Global evidence exists.</p>"

def sources_section(extra=""):
    links = "<ul><li><a href='https://store.steampowered.com/app/3393110/AION_2/' target='_blank' rel='noopener noreferrer'>AION 2 on Steam</a> for launch date, gameplay pillars, dungeons, customization and PC requirements.</li><li><a href='https://store.steampowered.com/app/4972180/AION_2_FOUNDERS_PACK/' target='_blank' rel='noopener noreferrer'>AION 2 Founder's Pack on Steam</a> for edition names, prices and advance access framing.</li></ul>"
    if extra:
        links += extra
    return content_section("Sources", links)

home_cards = "".join([
    card("Live Server Status", "Latest official availability, maintenance and incident updates for Global service.", "/server-status/", "Live"),
    card("Active Codes", "Current AION 2 redeem codes, rewards, region deadlines and redemption steps.", "/codes/", "Updated Oct 1"),
    card("Current Meta", "Versioned class tier matrix for Global launch, with evidence labels before any rating becomes final.", "/tier-list/class-tier-list/", "P0"),
    card("Choose Your Class", "Eight launch class overviews split by role, difficulty, PvE, PvP and who should play them.", "/classes/", "P0"),
    card("Latest Builds", "One build page per class with PvE, PvP and Solo tabs ready for Global patch notes.", "/builds/", "P1"),
    card("Leveling Guide", "A verified-first progression guide for the road to level 45 and the next steps after it.", "/guides/leveling-guide/", "Progression"),
    card("Global vs KR/TW", "A clear separation between official Global facts and regional reference data.", "/meta/global-vs-korea/", "Moat"),
    card("Dungeons", "Global dungeon formats, current official activity and a verified-data roadmap.", "/dungeons/", "Live"),
])

meta_cards = "".join(card(label, f"Confirmed Global facts and evidence status for {label.lower()}.", href, "Data") for href, label in META_PAGES)
prelaunch_cards = "".join(card(label, f"Launch and account preparation for {label.lower()}.", href, "Launch Prep") for href, label in PRELAUNCH_PAGES)
live_cards = "".join(card(label, f"Current Global information for {label.lower()}.", href, "Live") for href, label in LIVE_PAGES)

home = hero("AION 2 Meta", "Live Global service updates, redeem codes and evidence-labeled guides for Advanced Access and launch.") + content_section("Live Now", f"<div class='grid cards'>{live_cards}</div>") + content_section("Start Here", f"<div class='grid cards'>{home_cards}</div>") + content_section("Confirmed Global Facts", facts_grid() + source_note()) + content_section("Launch Prep Pages", f"<div class='grid cards'>{prelaunch_cards}</div>") + content_section("Evidence Rules", "<div class='evidence-row'><span>Official</span><span>Global Verified</span><span>KR/TW Reference</span><span>Unconfirmed</span></div><p>Ratings, builds and patch movement show the source type, last tested date and reason. Beginner Complexity describes learning demands, not class power.</p>") + sources_section()
write("index.html", page("AION 2 Meta - Global Builds, Tier Lists & Class Meta", "AION 2 Global meta tracker for class rankings, builds, release date, founder packs and launch guides.", "index", home, "home"))

classes_cards = "".join(card(name, f"{desc} Best fit: {CLASS_GUIDES[slug]['fit']}", f"/classes/{slug}/", role) for slug, name, role, desc, _ in CLASSES)
classes_body = hero("AION 2 Classes", "Compare all eight classes by combat identity, party job, learning demands and activity fit. Rankings stay separate from role guidance.", "Class Hub")
classes_body += content_section("Choose By Role", class_compare_table())
classes_body += content_section("Fast Recommendations", "<div class='grid cards'>" + card("Lead groups", "Templar covers tank responsibility; Cleric covers primary healing.", "/classes/templar/", "Group roles") + card("Ranged damage", "Compare Ranger spacing, Sorcerer cast windows and Spiritmaster pet-and-utility workload.", "/classes/ranger/", "Ranged") + card("Melee pressure", "Gladiator favors durable uptime; Assassin favors timing and selective burst.", "/classes/gladiator/", "Melee") + card("Hybrid support", "Chanter mixes group utility with direct participation instead of pure healing.", "/classes/chanter/", "Support") + "</div>")
classes_body += content_section("All Class Guides", f"<div class='grid cards'>{classes_cards}</div>")
classes_body += content_section("How To Use These Guides", "<p>Role and playstyle descriptions are guidance, not a hidden tier list. Open a class guide for its activity plan, then use the linked build page as a safe starting framework. Exact skill names, coefficients, stat breakpoints and activity rankings require repeatable Global-client evidence.</p>")
write("classes/", page("AION 2 Classes", "Compare all eight AION 2 classes by role, range, difficulty, PvE, PvP and solo playstyle.", "classes", classes_body))

build_cards = "".join(card(f"{name} Build", f"Quick-start combat loop plus PvE, PvP and solo variations for the {role.lower()} role.", f"/builds/{slug}-build/", "Advanced Access framework") for slug, name, role, *_ in CLASSES)
builds_body = hero("AION 2 Builds", "Start with a role-correct combat loop now, then replace verification checkpoints with tested Global skill and stat data.", "Build Hub")
builds_body += content_section("Pick A Build", f"<div class='grid cards'>{build_cards}</div>")
builds_body += content_section("Global build evidence", "<div class='notice'><b>Advanced Access: Live.</b> These builds are post-launch verification frameworks. Use the role plan now, but keep exact skill, stigma, stat and gear claims pending until repeatable Global-client evidence supports them.</div>")
builds_body += content_section("What Is Usable Now", "<ul><li><b>Quick Start:</b> positioning, resource and cooldown decisions matching the class role.</li><li><b>Activity variations:</b> what to emphasize in PvE, PvP and solo play without inventing a universal loadout.</li><li><b>Verification order:</b> client facts to check before publishing skill, stigma, stat or gear claims.</li><li><b>Version safety:</b> no untested numbers or copied KR/TW build is labeled Global best.</li></ul>")
builds_body += content_section("Before You Copy A Build", "<p>Confirm tested date, region, patch and activity. A raid setup can be poor for solo progression; a 1v1 setup can sacrifice the support or area pressure a large fight needs. Treat each build as a starting decision system until its exact loadout receives a Global Verified label.</p>")
write("builds/", page("AION 2 Builds", "AION 2 builds for all eight classes with quick-start rotations, PvE, PvP and solo variations plus Global verification notes.", "builds", builds_body))

for slug, name, role, desc, diff in CLASSES:
    data = CLASS_DATA[slug]
    guide = CLASS_GUIDES[slug]
    body = hero(f"AION 2 {name}", desc, role)
    body += content_section("Quick Verdict", f"<div class='summary'><div><b>Archetype</b><span>{data['archetype']}</span></div><div><b>Primary Role</b><span>{role}</span></div><div><b>Learning Demand</b><span>{diff}</span></div><div><b>Evidence Status</b><span>Advanced Access live; post-launch evidence pending</span></div><div><b>Party Job</b><span>{data['party']}</span></div><div><b>Range</b><span>{data['range']}</span></div><div><b>Beginner Note</b><span>{data['beginner']}</span></div><div><b>Quick Start</b><span><a href='/builds/{slug}-build/'>Best {name} Build</a></span></div></div>")
    body += content_section("Who Should Play This Class", f"<p>{guide['fit']}</p><h3>Likely strengths</h3><p>{guide['strengths']}</p><h3>Tradeoffs to accept</h3><p>{guide['tradeoffs']}</p>")
    body += content_section("How To Play It", f"<div class='grid cards'>{card('PvE', guide['pve'], None, 'Dungeon / group')}{card('PvP', guide['pvp'], None, 'Matchup framework')}{card('Solo', guide['solo'], None, 'Progression')}</div><h3>Core decision loop</h3><p>{guide['loop']}</p>")
    body += content_section("First Session Checklist", f"<ol><li>Learn the range and movement needed for the class job: {data['party']}.</li><li>Identify one pressure sequence, one defensive response and one escape or reposition option.</li><li>Test the loop on ordinary enemies before judging dungeon or PvP performance.</li><li>Open the <a href='/builds/{slug}-build/'>{name} build</a> and choose the correct activity variation.</li><li>Record Global patch and tested activity before treating performance as evidence.</li></ol>")
    body += content_section("Evidence And Open Questions", f"<div class='notice'><b>Verified scope:</b> class identity and role framing. Exact power ranking remains unranked until repeatable Global evidence exists.</div><ul><li>{data['watch']}</li><li>Exact skill names, values, cooldowns, costs and animation locks.</li><li>{guide['stats']}</li><li>Separate results for solo, 5-player, 10-player, 1v1, small-scale and large-scale play.</li></ul>")
    write(f"classes/{slug}/", page(f"AION 2 {name} Class Guide", f"AION 2 {name} class overview with role, difficulty, PvE, PvP, solo fit and Global evidence status.", f"classes/{slug}", body))

for slug, name, role, desc, diff in CLASSES:
    data = CLASS_DATA[slug]
    guide = CLASS_GUIDES[slug]
    tabs = f"""<div class="tabs" data-tabs><div role="tablist" aria-label="Build mode"><button class="active" data-tab="pve">PvE</button><button data-tab="pvp">PvP</button><button data-tab="solo">Solo</button></div><section data-panel="pve"><h3>PvE variation</h3><p>{guide['pve']}</p><ul><li>Favor reliable uptime and encounter tools.</li><li>Keep one answer for movement, control or incoming damage.</li><li>Measure party contribution in the content format being tested.</li></ul></section><section hidden data-panel="pvp"><h3>PvP variation</h3><p>{guide['pvp']}</p><ul><li>Build for a named format: 1v1, small-scale or large-scale.</li><li>Complete engage, survival and disengage plans before adding damage.</li><li>Test several matchups before calling a result solved.</li></ul></section><section hidden data-panel="solo"><h3>Solo variation</h3><p>{guide['solo']}</p><ul><li>Reduce downtime and keep a recovery plan for mistakes or adds.</li><li>Prefer a repeatable sequence over a perfect party burst window.</li><li>Reassess defense when moving from ordinary enemies to elites.</li></ul></section></div>"""
    body = hero(f"AION 2 {name} Build", f"A practical {name} quick-start for PvE, PvP and solo play, with unverified skill or stat claims kept explicit.", "Advanced Access Build")
    body += content_section("Build Snapshot", f"<div class='notice'><b>Evidence status:</b> usable role and decision framework; exact skills, stigma names, stat breakpoints and gear pieces require Global-client verification.</div><div class='summary'><div><b>Role</b><span>{role}</span></div><div><b>Party Job</b><span>{data['party']}</span></div><div><b>Range</b><span>{data['range']}</span></div><div><b>Learning Demand</b><span>{diff}</span></div><div><b>Core Loop</b><span>{guide['loop']}</span></div><div><b>Test First</b><span>{data['watch']}</span></div></div>")
    body += content_section("Quick Start", f"<ol><li><b>Position:</b> begin where the {data['range'].lower()} role can perform without spending its escape.</li><li><b>Setup:</b> establish the resource, control, buff, debuff or target condition the class needs.</li><li><b>Commit:</b> use the main pressure window while the target and encounter allow it.</li><li><b>Recover:</b> switch to safe repeatable actions while key tools return.</li><li><b>Reset:</b> reposition before starting the next sequence.</li></ol><p><b>{name} decision loop:</b> {guide['loop']}</p>")
    body += content_section("Build Modes", tabs)
    body += content_section("Skill And Rotation Framework", "<div class='table-wrap'><table><thead><tr><th>Slot</th><th>What belongs here</th><th>How to verify it</th></tr></thead><tbody><tr><th>Core action</th><td>The reliable action advancing the class's main job.</td><td>Confirm tooltip, cost, cooldown and Global behavior.</td></tr><tr><th>Setup</th><td>A buff, debuff, control or resource step enabling pressure.</td><td>Compare the sequence with and without setup.</td></tr><tr><th>Spend / burst</th><td>The high-value commitment used when the target is available.</td><td>Record window time, misses, interruptions and cost.</td></tr><tr><th>Defense / utility</th><td>The answer preventing a failed mechanic, death or lost teammate.</td><td>Test the effect and interruption rules.</td></tr><tr><th>Mobility / reset</th><td>The tool preserving range, avoiding danger or restarting.</td><td>Check range, cooldown and combat restrictions.</td></tr></tbody></table></div>")
    body += content_section("Stats, Gear And Stigma", f"<p><b>Priority method:</b> {guide['stats']}</p><ol><li>Meet confirmed accuracy, survival or resource requirements.</li><li>Compare one stat change at a time on the same target and sequence.</li><li>Prefer repeatable uptime over a larger tooltip that rarely lands.</li><li>Choose modifiers to solve the actual problem: damage, control, sustain, mobility or party utility.</li><li>Save patch, item level, target and sample size with every recommendation.</li></ol>")
    body += content_section("Global Verification Checklist", f"<ul><li>Capture exact Global names and tooltips for each recommended skill and modifier.</li><li>Verify {data['watch'].lower()}</li><li>Measure cooldown, cost, cast or animation time and positional conditions.</li><li>Test PvE on the same encounter and PvP in the same format before comparison.</li><li>Use Global Verified only when another tester can repeat the result.</li></ul><p>Need the overview first? Read the <a href='/classes/{slug}/'>AION 2 {name} class guide</a>.</p>")
    write(f"builds/{slug}-build/", page(f"Best AION 2 {name} Build", f"Best AION 2 {name} build for PvE, PvP and Solo with Global patch evidence status.", f"builds/{slug}-build", body))

tier_pages = {
    "class-tier-list": ("AION 2 Class Tier List", "AION 2 class tier list matrix for Global launch, tracking Solo, Dungeon, Raid and PvP rankings with evidence status.", "Full activity matrix", matrix()),
    "pve-tier-list": ("AION 2 PvE Tier List", "AION 2 PvE tier list framework separating dungeon, raid and solo evidence for the current Global build.", "PvE ranks", matrix()),
    "pvp-tier-list": ("AION 2 PvP Tier List", "AION 2 PvP tier list split by 1v1, small-scale and large-scale Global PvP evidence.", "PvP ranks", matrix()),
    "beginner-tier-list": ("AION 2 Beginner Tier List", "Best AION 2 beginner classes by difficulty, role clarity and early progression friendliness.", "Beginner picks", matrix()),
    "solo-tier-list": ("AION 2 Solo Tier List", "AION 2 solo class tier list for leveling, self-sustain and open-world comfort after Global verification.", "Solo ranks", matrix()),
}

tier_hub_cards = "".join(card(title.replace("AION 2 ", ""), desc, f"/tier-list/{slug}/", "Tier") for slug, (title, desc, _, _) in tier_pages.items())
body = hero("AION 2 Tier Lists", "Activity-specific class comparisons for the current Global build, with unranked cells where evidence is still incomplete.", "Tier Hub")
body += content_section("Tier List Pages", f"<div class='grid cards'>{tier_hub_cards}</div>")
body += content_section("Current Ranking Policy", "<p>Advanced Access evidence is still developing. Activity-specific ranks are tracked separately for class, PvE, PvP, beginner and solo needs, and cells remain unranked until the page can state the patch, activity and reason.</p>")
write("tier-list/", page("AION 2 Tier Lists", "AION 2 tier list hub for class, PvE, PvP, beginner and solo rankings with Global evidence status.", "tier-list", body))

for slug, (title, desc, label, table) in tier_pages.items():
    body = hero(title, "Every rank is versioned by Global patch, activity, evidence type and last review date.", label)
    body += content_section("Current Matrix", table)
    body += content_section("How Ratings Become Verified", "<p>A class only receives a rank when the page can state patch, last tested date, evidence type and why the rating changed. KR/TW data may inform hypotheses, but it will be labeled as reference rather than Global proof.</p>")
    write(f"tier-list/{slug}/", page(title, desc, f"tier-list/{slug}", body))

guide_pages = {
    "best-class": ("AION 2 Best Class", "Choose the best AION 2 class for solo play, groups, PvP or a first character without relying on an unverified overall tier list.", "There is no single best class for every activity. Start with the role and combat style you want, then use activity-specific evidence as the Global meta develops."),
    "beginner-guide": ("AION 2 Beginner Guide", "A practical AION 2 beginner guide for Advanced Access: class choice, first-session priorities, gear decisions and account safety.", "Use this start-to-play path to make the first sessions productive without turning unverified launch-week observations into permanent rules."),
    "leveling-guide": ("AION 2 Leveling Guide", "AION 2 leveling guide for moving through the story, unlocking systems and preparing for group content during Global Advanced Access.", "Follow a low-risk progression loop: advance the main path, clear required unlocks, learn your class, and use repeatable content only when it solves a real progression block."),
    "gear-progression": ("AION 2 Gear Progression", "AION 2 gear progression guide for leveling upgrades, early dungeon preparation and resource-safe gearing decisions.", "Equip meaningful upgrades, preserve scarce resources until their value is clear, and separate PvE, PvP and solo gear goals instead of chasing an unsupported best-in-slot list."),
    "pvp-guide": ("AION 2 PvP Guide", "AION 2 PvP guide covering preparation, positioning, target selection and the differences between duels, skirmishes and large battles.", "Build sound PvP habits first. Exact matchups and class rankings remain activity- and patch-specific, but preparation, awareness and team discipline matter in every mode."),
    "factions": ("AION 2 Factions", "AION 2 Elyos and Asmodian faction guide for choosing with friends and avoiding server-planning mistakes.", "Elyos and Asmodian areas are named in official Global notices. Choose with your group before investing heavily, and verify current creation and transfer restrictions in the client."),
}

guide_hub_cards = "".join(card(title.replace("AION 2 ", ""), desc, f"/guides/{slug}/", "Guide") for slug, (title, desc, _) in guide_pages.items())
body = hero("AION 2 Guides", "Task-first Global guides for choosing a class, starting well, leveling, gearing, PvP and coordinating your faction during Advanced Access.", "Guide Hub")
body += content_section("Guide Library", f"<div class='grid cards'>{guide_hub_cards}</div>")
body += content_section("Pick The Guide For Your Next Task", "<div class='table-wrap'><table><thead><tr><th>If You Need To…</th><th>Start Here</th></tr></thead><tbody><tr><td>Choose a first character</td><td><a href='/guides/best-class/'>Best Class by player goal</a></td></tr><tr><td>Get through the first sessions cleanly</td><td><a href='/guides/beginner-guide/'>Beginner Guide</a></td></tr><tr><td>Keep progression moving</td><td><a href='/guides/leveling-guide/'>Leveling Guide</a></td></tr><tr><td>Decide what gear is worth resources</td><td><a href='/guides/gear-progression/'>Gear Progression</a></td></tr><tr><td>Prepare for player combat</td><td><a href='/guides/pvp-guide/'>PvP Guide</a></td></tr><tr><td>Coordinate faction and server choices</td><td><a href='/guides/factions/'>Factions Guide</a></td></tr></tbody></table></div>")
body += content_section("Evidence Standard", "<p>Official notices establish service and feature facts. Recommendations are deliberately limited to durable player decisions; exact drop rates, stat weights, matchups and economy values stay unranked until repeatable Global evidence supports them.</p>")
write("guides/", page("AION 2 Guides", "AION 2 guide hub for beginner priorities, best class selection, leveling, gear progression, PvP and factions during Global Advanced Access.", "guides", body))

for slug, (title, desc, intro) in guide_pages.items():
    body = hero(title, intro, "Guide")
    if slug == "best-class":
        body += content_section("Best Class By Player Goal", "<div class='table-wrap'><table><thead><tr><th>Goal</th><th>Classes To Compare</th><th>Decision</th></tr></thead><tbody><tr><th>Clear party responsibility</th><td>Templar, Cleric</td><td>Start here if you actively want tanking or primary healing rather than only faster group finding.</td></tr><tr><th>Ranged damage</th><td>Ranger, Sorcerer</td><td>Compare mobile physical pressure with spell-focused ranged play; neither is labeled the stronger Global pick yet.</td></tr><tr><th>Support play</th><td>Chanter, Cleric</td><td>Choose hybrid support interest or primary healing responsibility.</td></tr><tr><th>High-input specialist</th><td>Assassin, Spiritmaster</td><td>Consider these when timing, positioning, utility or companion management is part of the appeal.</td></tr><tr><th>Frontline melee</th><td>Gladiator, Templar</td><td>Choose damage-oriented frontline play or a tank identity.</td></tr></tbody></table></div>")
        body += content_section("Four-Step Class Decision", "<ol><li><b>Choose range:</b> decide whether you want to stay at range or commit near the frontline.</li><li><b>Choose responsibility:</b> tanking and healing are role choices, not merely shortcuts to party demand.</li><li><b>Choose complexity:</b> use the class pages' Beginner Complexity label as a learning-cost guide, not a power rank.</li><li><b>Test before investing:</b> confirm the movement, targeting and core loop feel right before committing scarce resources.</li></ol>")
        body += content_section("What This Guide Does Not Claim", "<p>Launch-week popularity, queue composition and regional rankings do not prove a class is best. Use the <a href='/tier-list/'>activity-specific tier pages</a> only when their entries show a Global patch, test date and evidence.</p>")
    elif slug == "beginner-guide":
        body += content_section("First-Session Checklist", "<ol><li>Check <a href='/server-status/'>server status</a> before troubleshooting a login problem locally.</li><li>Choose the same region, server and faction as friends before investing in a character.</li><li>Complete the opening path and tutorials instead of skipping systems you have not learned.</li><li>Put frequently used combat, movement, healing and interaction actions on comfortable keys.</li><li>Equip clear upgrades, but keep scarce currencies and materials until their purpose is understood.</li><li>Try the class's normal combat loop before deciding it is weak or spending heavily on it.</li></ol>")
        body += content_section("Beginner-Friendly Class Framing", class_compare_table())
        body += content_section("A Safe Progression Loop", "<div class='timeline'><div><b>Advance</b><span>Follow the main path until a system, area or activity opens.</span></div><div><b>Learn</b><span>Read the unlock prompt and practice the new action before moving on.</span></div><div><b>Upgrade</b><span>Use obvious equipment improvements; delay irreversible or expensive optimization.</span></div><div><b>Group</b><span>Enter party content after understanding your role and basic survival tools.</span></div></div>")
        body += content_section("Common Mistakes To Avoid", "<ul><li>Do not choose a class only because a launch-week page predicts dominance.</li><li>Do not assume KR/TW economy, PvP or dungeon tuning is identical to Global.</li><li>Do not spread limited resources across many characters before choosing a main.</li><li>Do not ignore flight and vertical movement; learn where it changes navigation or combat positioning.</li><li>Do not use unofficial account-linking workarounds while the official issue remains under investigation.</li></ul>")
    elif slug == "leveling-guide":
        body += content_section("Leveling Priority", "<div class='timeline'><div><b>1. Main Path</b><span>Use the main story and required objectives as the default route because they introduce progression systems and access.</span></div><div><b>2. Nearby Unlocks</b><span>Complete tutorials and required side objectives that open travel, combat or account systems.</span></div><div><b>3. Power Check</b><span>If progress slows, review equipment, skill use and survival before grinding unrelated activities.</span></div><div><b>4. Group Content</b><span>Use available dungeons or party activities when they provide a relevant objective, upgrade opportunity or practice.</span></div></div>")
        body += content_section("When Progress Stalls", "<ol><li>Confirm the current objective and map marker rather than assuming more experience is required.</li><li>Equip upgrades already earned and repair or replenish ordinary supplies if the client requires it.</li><li>Review whether a tutorial, prerequisite or interaction was missed.</li><li>Check <a href='/server-status/'>known issues</a> when an object or quest step does not respond.</li><li>Only add repeatable content after identifying whether the blocker is level, gear, access or execution.</li></ol>")
        body += content_section("Route Accuracy", "<p>This guide does not publish an exact hour-by-hour route without a repeatable Global test. Quest rewards, dungeon unlock points and efficient detours should be versioned before they are presented as fastest.</p>")
    elif slug == "gear-progression":
        body += content_section("Gear Decision Path", "<div class='table-wrap'><table><thead><tr><th>Stage</th><th>Do Now</th><th>Avoid</th></tr></thead><tbody><tr><th>Early leveling</th><td>Equip clear upgrades that support your current role and keep the story moving.</td><td>Spending rare materials to perfect gear that will soon be replaced.</td></tr><tr><th>First party content</th><td>Meet entry requirements, cover basic survival and learn which rewards are relevant to your role.</td><td>Assuming every higher-rarity item is automatically correct for every activity.</td></tr><tr><th>Repeated dungeons</th><td>Target a documented upgrade source and stop when the expected gain no longer justifies the time.</td><td>Copying a regional best-in-slot list without matching the Global item and patch.</td></tr><tr><th>Specialization</th><td>Maintain separate goals for PvE, PvP and solo play when their needs differ.</td><td>Using one universal stat priority without class- and activity-specific evidence.</td></tr></tbody></table></div>")
        body += content_section("Before Spending A Scarce Resource", "<ol><li>Identify whether the item is temporary or part of a longer progression path.</li><li>Confirm the upgrade applies to the activity and role you actually play.</li><li>Check whether enhancement, transfer or replacement behavior is documented in the Global client.</li><li>Keep a reserve until the cost of the next progression step is known.</li></ol>")
        body += content_section("Evidence Limits", "<p>Exact stat weights, best-in-slot lists, enhancement breakpoints, crafting costs and market prices are intentionally omitted until Global data is reproducible. Use the <a href='/builds/'>class build pages</a> for versioned recommendations as they are verified.</p>")
    elif slug == "pvp-guide":
        body += content_section("PvP Modes To Track Separately", "<div class='summary'><div><b>1v1</b><span>Duel and isolated matchup strength.</span></div><div><b>Small-scale</b><span>Pick pressure, utility and coordinated skirmish value.</span></div><div><b>Large-scale</b><span>Group durability, ranged pressure, healing and area control.</span></div><div><b>Open-world</b><span>Mobility, escape tools, terrain and flight behavior.</span></div></div>")
        body += content_section("Before Entering PvP", "<ol><li>Put escape, defensive, control-break and recovery actions where they can be reached immediately.</li><li>Know which teammate provides frontline pressure, healing, support or ranged damage.</li><li>Choose a retreat direction before committing; flight and terrain can change pursuit and line of sight.</li><li>Enter with an activity-specific setup once the relevant build is Global Verified.</li></ol>")
        body += content_section("Fight Priorities", "<ul><li><b>Survive the opening:</b> do not spend every defensive tool on the first threat.</li><li><b>Track control:</b> distinguish a safe damage window from a target that can immediately counter or escape.</li><li><b>Focus with the group:</b> coordinated pressure is more useful than isolated damage in team modes.</li><li><b>Protect the objective:</b> a kill that abandons positioning or support can lose the larger fight.</li><li><b>Review by mode:</b> a duel result does not establish small- or large-scale class strength.</li></ul>")
        body += content_section("How PvP Claims Are Ranked", "<p>The <a href='/tier-list/pvp-tier-list/'>PvP tier list</a> separates 1v1, small-scale and large-scale evidence. A matchup is not promoted to a Global recommendation without a patch, date, mode and repeatable reason.</p>")
    elif slug == "factions":
        body += content_section("Confirmed Global Faction Context", "<p>Official Global maintenance notices name both <b>Elyos</b> and <b>Asmodian</b> areas. Current server and character-creation restrictions can change with population, so the client and official notices remain the source of truth for what can be created now.</p>")
        body += content_section("Choose Without Regret", "<ol><li>Agree on region, server and faction with friends or guildmates before character investment.</li><li>Check the client for current creation or recommendation labels at the moment you create.</li><li>Do not assume characters on different factions can group, trade or transfer together unless the Global client explicitly permits it.</li><li>Review the <a href='/servers/'>server guide</a> before relying on a planned transfer; the announced October 14 system has restrictions and is not yet live.</li></ol>")
        body += content_section("What Can Change", "<div class='table-wrap'><table><thead><tr><th>Check</th><th>Why It Matters</th></tr></thead><tbody><tr><th>Character creation</th><td>Population controls may affect where a new character can be made.</td></tr><tr><th>Friend and guild plans</th><td>Faction choice may determine whether players can participate together.</td></tr><tr><th>PvP context</th><td>Faction conflict can affect objectives, targets and open-world risk.</td></tr><tr><th>Transfers</th><td>Officially announced rules limit transfers by faction and server access type.</td></tr></tbody></table></div>")
    body += content_section("Verification Note", "<p>This page answers the player task with durable decisions and official facts. Unknown Global values are left unranked rather than filled with regional assumptions or launch-week guesses.</p>")
    body += content_section("Related Pages", "<div class='grid cards'>" + card("Class Tier List", "Compare classes by activity.", "/tier-list/class-tier-list/") + card("Classes", "Read launch class overviews.", "/classes/") + card("Evidence Policy", "See how Global claims are verified.", "/meta/evidence-policy/") + "</div>")
    write(f"guides/{slug}/", page(title, desc, f"guides/{slug}", body))

body = hero("AION 2 Release Date", "Advanced Access is live now. Full Global launch is scheduled for October 5, 2026 at 13:00 UTC after planned maintenance.", "Release Tracker")
body += content_section("Launch Timeline", "<div class='timeline'><div><b>Sep 30, 13:30 UTC</b><span>Advanced Access opened after a 30-minute delay.</span></div><div><b>Oct 5, 05:00–13:00 UTC</b><span>Planned pre-launch maintenance window.</span></div><div><b>Oct 5, 13:00 UTC</b><span>Scheduled full Global launch.</span></div></div>")
body += content_section("Confirmed Steam Facts", facts_grid())
body += content_section("What To Prepare", "<ul><li>Pick two candidate classes instead of locking to a fake pre-launch tier.</li><li>Bookmark class, PvE and PvP tier pages for launch-day updates.</li><li>Check Founder Pack value only if early access or cosmetics matter to you.</li></ul>")
write("release-date/", page("AION 2 Release Date", "AION 2 release date, advance access timing and launch preparation checklist.", "release-date", body))

body = hero("AION 2 Founder's Pack", "Compare Standard, Deluxe and Ultimate with a focus on early access and launch value.", "Buyer Guide")
body += content_section("Known Purchase Decision", "<div class='table-wrap'><table><thead><tr><th>Edition</th><th>Steam Price</th><th>Best For</th><th>Known Anchor</th></tr></thead><tbody>" + "".join(f"<tr><th>{name}</th><td>{price}</td><td>{'Players who mainly want early access.' if name == 'Standard' else 'Players who want extra launch cosmetics and bundle value.' if name == 'Deluxe' else 'Collectors who want the largest launch bundle.'}</td><td>{anchor}</td></tr>" for name, price, anchor in FOUNDER_PACKS) + "</tbody></table></div>")
body += content_section("Recommendation", "<p>Buy for early access or cosmetics, not because a pre-launch meta page says one class will dominate. The strongest value depends on whether you will actually play during the five-day head start.</p><div class='grid cards'>" + card("Which Edition?", "Compare Standard, Deluxe and Ultimate by purchase intent.", "/founders-pack/which-edition/") + card("Advance Access", "Check the early access timing and prep list.", "/advance-access/") + "</div>")
write("founders-pack/", page("AION 2 Founder's Pack", "AION 2 Founder Pack guide comparing Standard, Deluxe and Ultimate purchase intent.", "founders-pack", body))

body = hero("AION 2 Advanced Access", "Advanced Access is live for eligible Founder Pack accounts until the October 5 Global launch.", "Advanced Access Live")
body += content_section("Current Timing", "<div class='timeline'><div><b>September 30, 13:30 UTC</b><span>Advanced Access opened after the official 30-minute delay.</span></div><div><b>October 5, 05:00 UTC</b><span>Advanced Access ends and planned maintenance begins.</span></div><div><b>October 5, 13:00 UTC</b><span>Scheduled Global launch.</span></div></div>")
body += content_section("Should You Play Advance Access?", "<div class='table-wrap'><table><thead><tr><th>Buy Early If</th><th>Wait If</th></tr></thead><tbody><tr><td>You will actually play during the five-day window.</td><td>You are only buying because of unverified class hype.</td></tr><tr><td>You want to test classes, controls and performance before launch rush.</td><td>You prefer waiting for server stability and first community reports.</td></tr><tr><td>You value founder cosmetics or membership items.</td><td>You only care about long-term meta rankings.</td></tr></tbody></table></div>")
body += content_section("Advance Access Checklist", "<ol><li>Confirm PC storage and requirements.</li><li>Pick a primary and backup class.</li><li>Use the launch verification checklist to record patch, class, skill values and dungeon data.</li><li>Do not convert first-hour impressions into final tier claims.</li></ol>")
write("advance-access/", page("AION 2 Advance Access", "AION 2 advance access date, Founder Pack timing and early access preparation checklist.", "advance-access", body))

body = hero("AION 2 Standard vs Deluxe vs Ultimate", "Compare Founder Pack editions by practical launch value instead of pre-launch class hype.", "Edition Compare")
body += content_section("Edition Comparison", "<div class='table-wrap'><table><thead><tr><th>Edition</th><th>Price</th><th>Best Fit</th><th>Main Reason To Buy</th></tr></thead><tbody><tr><th>Standard</th><td>$24.99</td><td>Players who mainly want the five-day head start.</td><td>Lowest listed entry point for advance access.</td></tr><tr><th>Deluxe</th><td>$49.99</td><td>Players who know they want extra launch cosmetics or bundle value.</td><td>Middle option when Standard feels too bare.</td></tr><tr><th>Ultimate</th><td>$99.99</td><td>Collectors and committed players.</td><td>Highest listed package for the largest bundle.</td></tr></tbody></table></div>")
body += content_section("Simple Recommendation", "<ul><li>Pick Standard if access is the only must-have.</li><li>Pick Deluxe only if the extra items are valuable to you personally.</li><li>Pick Ultimate only if you already expect to main the game at launch.</li><li>Skip upgrading just because a pre-launch tier list claims your class will be dominant.</li></ul>")
write("founders-pack/which-edition/", page("AION 2 Standard vs Deluxe vs Ultimate", "AION 2 Standard vs Deluxe vs Ultimate Founder Pack comparison with prices and purchase recommendations.", "founders-pack/which-edition", body))

body = hero("AION 2 Server Status", "Latest official Global availability, maintenance and known-issue updates. This is an official-notice tracker, not an automated uptime monitor.", "Official Status Tracker")
body += content_section("Current Global Status", "<div class='notice status-online'><b>Advanced Access: Live.</b> Latest official notice: all servers returned online after the October 1 maintenance. Local queues or new incidents may occur after that notice.</div><div class='summary'><div><b>Access phase</b><span>Advanced Access live</span></div><div><b>Official service state</b><span>All servers back online</span></div><div><b>Last checked</b><span>Oct 1, 2026</span></div><div><b>Official Global Launch</b><span>Oct 5, 2026</span></div></div>")
body += content_section("Latest Maintenance", "<div class='table-wrap'><table><thead><tr><th>Window</th><th>Scope</th><th>Reason</th><th>Resolution</th></tr></thead><tbody><tr><td>Oct 1, 08:00 CEST / Sep 30, 23:00 PDT</td><td>All services</td><td>Quest object-interaction bottlenecks affecting named Elyos and Asmodian areas.</td><td>Official notice says maintenance ended and all servers returned online.</td></tr></tbody></table></div>")
body += content_section("Known Issues", "<div class='table-wrap'><table><thead><tr><th>Issue</th><th>Official state</th><th>Player action</th></tr></thead><tbody><tr><th>Account linking</th><td>Investigation ongoing.</td><td>Follow official notices; do not unlink or relink accounts based on unofficial workarounds.</td></tr><tr><th>Advanced Access recognition</th><td>Officially marked fixed.</td><td>Restart the client to receive the no-downtime update.</td></tr><tr><th>In-game purchases</th><td>Officially marked fixed.</td><td>Restart the client before retrying.</td></tr></tbody></table></div>")
body += content_section("Regions And Queues", "<p>The official service covers Europe, NA East, NA West and Latin America in current Advanced Access notices. Queue conditions can change quickly, so an official all-servers-online notice does not prove every realm is queue-free.</p><div class='grid cards'>" + card("Server List & Transfers", "See official region names, newly added servers and the planned October 14 transfer rules.", "/servers/", "Official") + card("Active Redeem Code", "Claim the October thank-you gift before the NA or EU deadline.", "/codes/", "Oct 1") + "</div>")
body += content_section("Official Sources", "<ul><li><a href='https://steamcommunity.com/app/3393110/allnews/?l=english'>AION 2 Steam News</a> — maintenance, service restoration, known issues and launch notices.</li><li><a href='https://aion2.plaync.com/en-us/board/notice/list?redirect=false'>AION 2 official announcements</a>.</li></ul>")
write("server-status/", page("AION 2 Server Status – Maintenance, Queue & Known Issues", "Latest official AION 2 server status, maintenance, queue context and known issues for Global Advanced Access.", "server-status", body))

body = hero("AION 2 Codes", "Active Global redeem codes, rewards, region deadlines and verified redemption steps.", "Updated October 1")
body += content_section("Active Codes", "<div class='table-wrap'><table><thead><tr><th>Code</th><th>Rewards</th><th>Expires</th><th>Limits</th></tr></thead><tbody><tr><th><code>TAKEFLIGHTAION2</code></th><td>Odyle Energy (Bound) ×4; Resurrection Spiritstone (Bound) ×5; Battle Enhance Scroll (Bound) ×10</td><td>NA: Oct 13, 11:00 PM PDT<br>EU: Oct 14, 08:00 CEST</td><td>All servers; one redemption per account; rewards are bound.</td></tr></tbody></table></div>")
body += content_section("How To Redeem", "<ol><li>Open AION 2 and go to <b>Settings</b>.</li><li>Select <b>Miscellaneous</b>, then <b>Account</b>.</li><li>Choose <b>Enter Coupon</b>.</li><li>Enter <code>TAKEFLIGHTAION2</code> and confirm.</li></ol><div class='notice'><b>Region note:</b> The official notice publishes separate NA and EU deadlines. Do not assume the later EU deadline applies to every region.</div>")
body += content_section("Official Source", "<p><a href='https://steamcommunity.com/app/3393110/allnews/?l=english'>A Thank You Gift to all Daevas — official AION 2 Steam News</a>. Last checked October 1, 2026.</p>")
write("codes/", page("AION 2 Codes October 2026", "Active AION 2 codes for October 2026 with verified rewards, NA and EU expiration times, and redemption instructions.", "codes", body))

body = hero("AION 2 Servers", "Official region, new-server, queue and transfer information for Global Advanced Access.", "Server Guide")
body += content_section("Global Regions", "<div class='summary'><div><b>Europe</b><span>Advanced Access region</span></div><div><b>NA East</b><span>Advanced Access region</span></div><div><b>NA West</b><span>Advanced Access region</span></div><div><b>Latin America</b><span>Advanced Access region</span></div></div>")
body += content_section("Recently Added Servers", "<div class='table-wrap'><table><thead><tr><th>Region</th><th>Officially announced additions</th></tr></thead><tbody><tr><th>Europe</th><td>Yustiel / Marchutan; Ariel / Azphel; Fregion / Ereshkigal; Meslamtaeda / Beritra</td></tr><tr><th>NA East</th><td>Vaizel / Triniel</td></tr><tr><th>NA West</th><td>Nezekan / Zikel</td></tr></tbody></table></div><p class='source-note'>This records the additions named in the September 30 official notice; it is not presented as a complete permanent server list.</p>")
body += content_section("Queues And Recommended Servers", "<p>Official notices advise players facing long queues to consider a recommended server. New-server and recommendation labels can change, so check the client before creating a character.</p>")
body += content_section("Server Transfers", "<div class='notice'><b>Planned for October 14:</b> transfers are scheduled to begin within the same faction and are expected to be free initially. Advanced Access characters may transfer only to other Advanced Access servers, not commercial-launch servers. This feature is not live yet and the rules may change.</div><p>Instanced content, including dungeons, supports cross-server play according to the official notice.</p>")
body += content_section("Official Source", "<p><a href='https://steamcommunity.com/app/3393110/allnews/?l=english'>AION 2 Steam News</a> — queue, new-server and transfer announcements. Last checked October 1, 2026.</p>")
write("servers/", page("AION 2 Server List, Regions & Transfers", "AION 2 Global server regions, newly added servers, queue guidance and planned server-transfer rules.", "servers", body))

body = hero("AION 2 Download", "Pre-download is available on Steam and PURPLE for the Windows PC client.", "Download")
body += content_section("Known Requirement", "<div class='notice'><b>Storage:</b> Steam currently lists 100 GB available space in the minimum requirements.</div>")
body += content_section("Download Status", "<div class='notice'><b>Available now:</b> the official notice confirms pre-download through Steam and PURPLE. Downloaded files are encrypted and decrypt when access opens; decryption time depends on the PC.</div>")
body += content_section("What The 100 GB Requirement Means", "<p>The listed storage requirement should be treated as the minimum free space to reserve before the client is available. Launch downloads can also need temporary patching room, so players with a nearly full drive should clear additional space rather than stopping at exactly 100 GB. If the Steam client later publishes a preload window, this page should record the date, region and source before calling it confirmed.</p>")
body += content_section("Download Prep Checklist", "<ol><li>Free at least 100 GB before advance access.</li><li>Use an SSD where possible because the storefront recommends it.</li><li>Update GPU drivers and Windows before launch day.</li><li>Check server status before assuming a download or login issue is local.</li></ol>")
body += sources_section()
write("preload-download/", page("AION 2 Preload and Download", "AION 2 preload, download and storage preparation page with 100 GB requirement and launch checklist.", "preload-download", body))

body = hero("AION 2 System Requirements", "PC requirements currently listed for the Global Steam release.", "PC Specs")
body += content_section("Minimum PC Requirements", "<div class='table-wrap'><table><thead><tr><th>Component</th><th>Requirement</th></tr></thead><tbody>" + "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in SYSTEM_REQUIREMENTS) + "</tbody></table></div>")
body += content_section("Launch Prep Notes", "<ul><li>Reserve at least 100 GB before advance access begins.</li><li>Use an SSD where possible because the storefront note recommends it.</li><li>Minimum hardware should start with conservative graphics settings, then raise quality after checking performance in crowded areas.</li></ul>")
body += sources_section()
write("system-requirements/", page("AION 2 System Requirements", "AION 2 PC system requirements for OS, CPU, RAM, GPU, DirectX, storage and launch prep.", "system-requirements", body))

body = hero("AION 2 Gameplay", "A task-focused overview of the confirmed Global gameplay pillars: class combat, flight, PvE, PvP, crafting, trading and large-scale exploration.", "Gameplay")
body += content_section("Confirmed Gameplay Pillars", "<div class='grid facts'><div><b>Class Combat</b><span>Steam describes class-based combat as a core part of AION 2.</span></div><div><b>Flight</b><span>Flight and verticality are positioned as exploration and combat hooks.</span></div><div><b>PvE</b><span>Dungeon content spans solo, 5-player and 10-player formats.</span></div><div><b>PvP</b><span>PvP exists, but Global activity balance still needs live evidence.</span></div><div><b>Crafting</b><span>Crafting is named as part of the Global feature set.</span></div><div><b>Trading</b><span>Trading is named, but launch economy values are unknown.</span></div><div><b>World</b><span>Steam says the world is 36 times larger than the original AION.</span></div><div><b>Engine</b><span>Unreal Engine 5 is listed as the visual foundation.</span></div></div>")
body += content_section("Choose Your Next Activity", "<div class='grid cards'>" + card("Learn A Class", "Compare roles and open the matching build path.", "/classes/") + card("Enter PvE", "See confirmed formats and the dungeon hub.", "/pve-content/") + card("Prepare For PvP", "Set up controls, positioning and mode-specific goals.", "/guides/pvp-guide/") + card("Keep Progressing", "Use the leveling and gear decision paths.", "/guides/leveling-guide/") + "</div>")
body += content_section("What Still Needs Global Evidence", "<ul><li>Exact skill values, cooldowns and class balance for the current Global patch.</li><li>Economy prices, trading restrictions and stable market behavior.</li><li>Repeatable progression bottlenecks and route comparisons.</li><li>Which KR/TW strategies remain valid under the Global client and population.</li></ul>")
write("gameplay/", page("AION 2 Gameplay", "AION 2 gameplay overview covering class combat, flight, PvE, PvP, crafting, trading and confirmed Global launch facts.", "gameplay", body))

body = hero("AION 2 PvE Content", "Confirmed Global PvE formats and a practical path from solo learning to party and larger-group dungeon content.", "PvE")
body += content_section("Confirmed PvE Formats", "<div class='summary'><div><b>Solo</b><span>Solo dungeon format is named on Steam.</span></div><div><b>5-Player</b><span>Party dungeon format is named on Steam.</span></div><div><b>10-Player</b><span>Larger group dungeon format is named on Steam.</span></div><div><b>200+</b><span>Steam describes over 200 dungeons.</span></div></div>")
body += content_section("PvE Progression Path", "<div class='timeline'><div><b>Solo Learning</b><span>Practice movement, survival and the class's repeatable combat loop before taking group responsibility.</span></div><div><b>5-Player Parties</b><span>Learn role execution, boss telegraphs and recovery without treating one clear as proof of a meta.</span></div><div><b>10-Player Content</b><span>Prioritize coordination, mechanic assignments and group survival over personal damage claims.</span></div><div><b>Repeatable Goals</b><span>Target documented upgrades, event objectives or rankings with the current patch and reset schedule recorded.</span></div></div>")
body += content_section("Before Joining A Dungeon", "<ol><li>Confirm the activity's current entry requirement and whether your role is needed.</li><li>Equip sensible upgrades and place survival or support tools on accessible keys.</li><li>Read verified mechanics on the <a href='/dungeons/'>dungeon hub</a>; do not rely on an unlabeled regional guide.</li><li>After a run, identify whether the blocker was mechanics, coordination, survival or damage before changing the build.</li></ol>")
body += content_section("Other PvE Systems", "<ul><li>Seasonal challenges and competitive rankings are part of the announced PvE scope.</li><li>Open-world events are named, but schedules and reward tables require current Global verification.</li><li>Dungeon names, requirements, mechanics and rewards should carry a source and last-verified date before becoming recommendations.</li></ul>")
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
body += content_section("Comparison", "<div class='table-wrap'><table><thead><tr><th>Topic</th><th>KR/TW</th><th>Global</th></tr></thead><tbody><tr><th>Classes</th><td>Existing live environment.</td><td>Launch roster tracked separately.</td></tr><tr><th>Balance</th><td>Regional live patches.</td><td>Global build must be verified.</td></tr><tr><th>Tier Lists</th><td>Useful reference.</td><td>Unranked until activity-specific Global evidence is sufficient.</td></tr><tr><th>Economy</th><td>Mature market.</td><td>Fresh Advanced Access market.</td></tr><tr><th>PvP Meta</th><td>Established assumptions.</td><td>Needs Global population and ruleset evidence.</td></tr><tr><th>Dungeons</th><td>May reveal mechanics and content patterns.</td><td>Names, rewards and tuning must be confirmed on Global.</td></tr></tbody></table></div>")
body += content_section("Why Regional Data Can Mislead", "<p>Regional versions can be useful for deciding what to test first, but they can mislead Global players when patch timing, monetization, economy maturity, server population or launch roster differs. A build that is stable in an older live environment may be wrong for a fresh Global economy, and a PvP matchup that depends on experienced players may not describe launch-week behavior.</p>")
body += content_section("How This Site Uses KR/TW Reference", "<ol><li>Use regional data to form test hypotheses.</li><li>Label it as KR/TW Reference, never Global Verified.</li><li>Retest in the Global client before updating ranks or build recommendations.</li><li>Log every rank change with patch, date and reason.</li></ol>")
body += sources_section()
write("meta/global-vs-korea/", page("AION 2 Global vs Korea Meta", "AION 2 Global vs KR/TW meta comparison and evidence policy.", "meta/global-vs-korea", body))

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
body += content_section("Current Entries", "<div class='timeline'><div><b>September 13, 2026</b><span>Initial evidence-labeled site structure published with official storefront facts.</span></div><div><b>October 1, 2026</b><span>Advanced Access migration: live official server tracker, current maintenance and known issues, active code, server guide, dungeon event, player-task guides and expanded class/build pages.</span></div><div><b>October 5, 2026</b><span>Scheduled: verify the full-launch patch and update activity-specific rankings only where repeatable evidence is available.</span></div></div>")
body += content_section("What Gets Logged", "<ul><li>Tier movement with reason and patch context.</li><li>Build page updates after skill, stat or gear verification.</li><li>Dungeon requirement, boss mechanic and reward confirmations.</li><li>Corrections when a pre-launch assumption proves wrong.</li></ul>")
write("meta/update-log/", page("AION 2 Meta Update Log", "AION 2 Meta update log for class rankings, builds, dungeon data and launch verification changes.", "meta/update-log", body))

body = hero("AION 2 Launch Verification Checklist", "A working checklist for turning Advanced Access observations into Global Verified class, build and dungeon guidance.", "Operations")
body += content_section("First 24 Hours", "<div class='table-wrap'><table><thead><tr><th>Task</th><th>Pages Affected</th><th>Evidence Required</th></tr></thead><tbody><tr><th>Confirm client patch and server region</th><td>All tier and build pages</td><td>Patch label, date and screenshot or official note.</td></tr><tr><th>Record launch class roster</th><td>Classes, best class, tier matrix</td><td>Global client roster check.</td></tr><tr><th>Capture skill values</th><td>8 build pages</td><td>Skill names, cooldowns, effects and any unlocked variants.</td></tr><tr><th>Test solo comfort</th><td>Solo tier, beginner tier, class pages</td><td>Repeatable leveling or solo dungeon observations.</td></tr><tr><th>List first dungeon names</th><td>Dungeons, PvE content</td><td>Requirements, format, bosses and reward screenshots.</td></tr></tbody></table></div>")
body += content_section("Do Not Update A Rank Until", "<ol><li>The activity is clear: Solo, Dungeon, Raid, 1v1 PvP, Small PvP, Large PvP or Beginner.</li><li>The page can state the Global patch and last tested date.</li><li>The claim has repeatable evidence or a clearly labeled official source.</li><li>The update log records what changed and why.</li></ol>")
body += content_section("Update Order", "<div class='timeline'><div><b>1. Release Date / Status</b><span>Confirm access, server status and any launch delay.</span></div><div><b>2. Classes</b><span>Confirm roster, role labels and class page basics.</span></div><div><b>3. Builds</b><span>Fill skill values and early stat priorities only after client checks.</span></div><div><b>4. Tier Lists</b><span>Move Unranked cells to ranks only where activity-specific evidence exists.</span></div><div><b>5. Dungeons</b><span>Create individual dungeon pages only after name, mechanics and rewards are verified.</span></div></div>")
write("meta/launch-verification-checklist/", page("AION 2 Launch Verification Checklist", "AION 2 launch verification checklist for updating class rankings, builds, dungeon data and Global evidence labels.", "meta/launch-verification-checklist", body))

body = hero("AION 2 Dungeons", "Global dungeon formats, current official activities and evidence-labeled details for Advanced Access.", "Dungeon Hub")
body += content_section("Confirmed Dungeon Scope", "<div class='summary'><div><b>Total Scope</b><span>Over 200 dungeons described on Steam.</span></div><div><b>Solo</b><span>Solo challenge format named.</span></div><div><b>Party</b><span>5-player party content named.</span></div><div><b>Group</b><span>10-player group dungeons named.</span></div></div>")
body += content_section("Transcendence Dungeon Leaderboard", "<div class='notice'><b>Advanced Access event live:</b> the official leaderboard runs through November 2 for Advanced Access servers.</div><div class='table-wrap'><table><thead><tr><th>Dungeon</th><th>Ranking</th><th>Where To Check</th><th>Results</th></tr></thead><tbody><tr><th>Deus Research Base</th><td>Per server and per class</td><td>ESC → Transcendence → Rank → Class</td><td>Top rankers announced Nov 9</td></tr><tr><th>Shattered Arkanis</th><td>Per server and per class</td><td>ESC → Transcendence → Rank → Class</td><td>Rewards mailed by Nov 16</td></tr></tbody></table></div><p class='source-note'>The event notice confirms these leaderboard dungeons, not the complete Global dungeon catalog or their full mechanics.</p>")
body += content_section("Dungeon Data Standard", "<ol><li>Publish the exact Global dungeon name and format.</li><li>Verify level, entry requirements and reset rules in the Global client.</li><li>Document bosses and mechanics with repeatable evidence.</li><li>Record rewards without importing unverified KR/TW tables.</li><li>Create an individual URL only when the page can answer those player questions.</li></ol>")
body += content_section("Launch Verification Priorities", "<ul><li>Record the first dungeon names exactly as they appear in the Global client.</li><li>Separate solo, 5-player and 10-player content instead of merging them into one list.</li><li>Capture requirements, boss names, mechanics and reward screenshots before publishing an individual dungeon page.</li><li>Track which classes feel valuable by activity, but avoid turning one dungeon impression into a site-wide tier claim.</li></ul>")
body += sources_section("<ul><li><a href='https://steamcommunity.com/app/3393110/allnews/?l=english'>Official Community Launch Events</a> for the Transcendence Dungeon Leaderboard.</li></ul>")
write("dungeons/", page("AION 2 Dungeons – Requirements, Bosses & Rewards", "AION 2 Global dungeon hub with formats, current Transcendence activity and a verified-data standard for requirements, bosses and rewards.", "dungeons", body))

body = hero("Page Not Found", "This AION 2 Meta page does not exist yet, or it may be waiting for Global verification.", "404")
body += content_section("Find The Right Page", "<div class='grid cards'>" + card("Classes", "Compare the launch class roster.", "/classes/") + card("Tier Lists", "Open the Global tier matrix.", "/tier-list/") + card("Guides", "Read launch preparation guides.", "/guides/") + card("Update Log", "Check what changed recently.", "/meta/update-log/") + "</div>")
write("404.html", page("Page Not Found", "AION 2 Meta 404 page with links to classes, tier lists, guides and update log.", "404", body))

styles = r"""
:root{color-scheme:dark;--bg:#080a0f;--panel:#111722;--panel2:#171f2d;--text:#edf4ff;--muted:#a9b6c8;--line:#293448;--gold:#f2c36b;--blue:#76d5ff;--red:#ff7e79;--green:#86e3b2;--shadow:0 24px 80px rgba(0,0,0,.35)}*{box-sizing:border-box}body{margin:0;background:radial-gradient(circle at 20% 0%,rgba(118,213,255,.18),transparent 34rem),radial-gradient(circle at 90% 12%,rgba(242,195,107,.14),transparent 28rem),var(--bg);color:var(--text);font-family:Inter,ui-sans-serif,system-ui,-apple-system,Segoe UI,Arial,sans-serif;line-height:1.6}a{color:inherit}.skip{position:absolute;left:-999px}.skip:focus{left:1rem;top:1rem;z-index:99;background:#fff;color:#000;padding:.5rem 1rem}.site-header{position:sticky;top:0;z-index:10;display:flex;align-items:center;justify-content:space-between;gap:1rem;padding:1rem clamp(1rem,4vw,4rem);border-bottom:1px solid rgba(255,255,255,.1);background:rgba(8,10,15,.82);backdrop-filter:blur(14px)}.brand{display:flex;align-items:center;gap:.7rem;text-decoration:none;font-weight:800}.brand-mark{display:grid;place-items:center;width:2.35rem;height:2.35rem;border:1px solid rgba(242,195,107,.5);background:linear-gradient(145deg,#1b2534,#0c1017);color:var(--gold);font-size:.85rem}.site-header nav{display:flex;gap:.35rem;flex-wrap:wrap}.site-header nav a{padding:.55rem .75rem;border-radius:.35rem;color:var(--muted);text-decoration:none;font-size:.92rem}.site-header nav a:hover,.site-header nav a:focus{background:rgba(255,255,255,.08);color:var(--text)}.hero{min-height:clamp(520px,70vh,760px);display:grid;grid-template-columns:minmax(0,1.15fr) minmax(280px,.65fr);gap:2rem;align-items:center;padding:clamp(3rem,7vw,7rem) clamp(1rem,4vw,4rem);border-bottom:1px solid rgba(255,255,255,.1)}.hero h1{font-size:clamp(2.8rem,7vw,6.8rem);line-height:.9;letter-spacing:0;margin:.4rem 0 1.3rem;max-width:11ch}.lead{font-size:clamp(1.1rem,2.2vw,1.45rem);color:#d8e4f5;max-width:43rem}.eyebrow{margin:0;color:var(--gold);font-weight:800;text-transform:uppercase;font-size:.78rem;letter-spacing:.12em}.hero-actions{display:flex;gap:.8rem;flex-wrap:wrap;margin-top:1.7rem}.button,.card-link{display:inline-flex;align-items:center;justify-content:center;min-height:44px;padding:.72rem 1rem;border:1px solid rgba(255,255,255,.16);border-radius:.35rem;text-decoration:none;font-weight:800;background:rgba(255,255,255,.06)}.button.primary{background:var(--gold);color:#12100a;border-color:var(--gold)}.status-panel,.card,.notice{background:linear-gradient(180deg,rgba(23,31,45,.92),rgba(12,16,23,.92));border:1px solid rgba(255,255,255,.12);box-shadow:var(--shadow);padding:1.25rem}.status-panel{align-self:stretch;display:flex;flex-direction:column;justify-content:end;min-height:24rem}.status-dot{width:.8rem;height:.8rem;border-radius:99px;background:var(--red);box-shadow:0 0 0 .45rem rgba(255,126,121,.12);margin-bottom:1rem}.status-panel dl{display:grid;gap:.7rem;margin:1rem 0 0}.status-panel dl div,.summary div,.timeline div{display:flex;justify-content:space-between;gap:1rem;border-top:1px solid rgba(255,255,255,.1);padding-top:.75rem}.status-panel dt,.summary b{color:var(--muted)}.status-panel dd{margin:0;font-weight:800}.section{padding:clamp(2.5rem,5vw,5rem) clamp(1rem,4vw,4rem);max-width:1320px;margin:0 auto}.section h2{font-size:clamp(1.8rem,3vw,3rem);line-height:1.05;margin:0 0 1.2rem}.grid{display:grid;gap:1rem}.cards{grid-template-columns:repeat(3,minmax(0,1fr))}.facts{grid-template-columns:repeat(4,minmax(0,1fr))}.facts div{border:1px solid rgba(255,255,255,.12);background:rgba(255,255,255,.055);padding:1rem}.facts b{display:block;color:var(--gold);margin-bottom:.35rem}.facts span{color:#d8e4f5}.source-note{color:var(--muted);max-width:62rem}.card{min-height:14rem;display:flex;flex-direction:column}.card h3{font-size:1.35rem;margin:.3rem 0 .5rem}.card p{color:var(--muted);margin:0 0 1rem}.card-link{margin-top:auto;width:max-content}.table-wrap{overflow:auto;border:1px solid rgba(255,255,255,.13);background:rgba(17,23,34,.72)}table{width:100%;border-collapse:collapse;min-width:760px}caption{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}th,td{text-align:left;padding:1rem;border-bottom:1px solid rgba(255,255,255,.1);vertical-align:top}thead th{color:var(--gold);font-size:.78rem;text-transform:uppercase;letter-spacing:.08em}tbody th{white-space:nowrap}.pill{display:inline-flex;min-width:3rem;justify-content:center;padding:.25rem .55rem;border-radius:99px;background:rgba(255,255,255,.08);font-weight:800;font-size:.78rem}.pill.muted{color:var(--muted)}.summary{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:1rem}.summary div{display:block;background:rgba(255,255,255,.05);padding:1rem;border:1px solid rgba(255,255,255,.1)}.summary span{display:block;margin-top:.35rem}.evidence-row{display:flex;flex-wrap:wrap;gap:.7rem}.evidence-row span{padding:.55rem .75rem;border:1px solid rgba(255,255,255,.13);background:rgba(255,255,255,.06);font-weight:800}.tabs{border:1px solid rgba(255,255,255,.13);background:rgba(17,23,34,.72);padding:1rem}.tabs [role=tablist]{display:flex;gap:.5rem;flex-wrap:wrap;border-bottom:1px solid rgba(255,255,255,.12);padding-bottom:.8rem}.tabs button{min-height:44px;padding:.6rem 1rem;border:1px solid rgba(255,255,255,.18);background:transparent;color:var(--text);font-weight:800;border-radius:.3rem}.tabs button.active{background:var(--blue);color:#061018;border-color:var(--blue)}.timeline{display:grid;gap:1rem;max-width:760px}.timeline div{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);padding:1rem}.site-footer{display:grid;grid-template-columns:1fr 1fr;gap:2rem;margin-top:3rem;padding:2rem clamp(1rem,4vw,4rem);border-top:1px solid rgba(255,255,255,.1);color:var(--muted)}.site-footer strong{color:var(--text);font-size:1.25rem}.small{font-size:.86rem}@media (max-width:1040px){.facts{grid-template-columns:repeat(2,minmax(0,1fr))}}@media (max-width:880px){.site-header{align-items:flex-start;flex-direction:column}.hero{grid-template-columns:1fr;min-height:auto}.hero h1{max-width:12ch}.cards{grid-template-columns:1fr}.summary{grid-template-columns:1fr 1fr}.site-footer{grid-template-columns:1fr}}@media (max-width:520px){.facts,.summary{grid-template-columns:1fr}.hero{padding-top:2rem}.site-header nav a{padding:.45rem .5rem}.status-panel{min-height:auto}.section{padding-block:2rem}}
"""
styles += r"""
.breadcrumbs{display:flex;align-items:center;gap:.55rem;max-width:1320px;margin:0 auto;padding:1rem clamp(1rem,4vw,4rem) 0;color:var(--muted);font-size:.88rem}.breadcrumbs a:hover,.breadcrumbs a:focus,.footer-links a:hover,.footer-links a:focus{color:var(--text)}.footer-links{display:flex;flex-wrap:wrap;gap:.55rem 1rem;margin-top:1rem}.footer-links a{color:var(--muted)}
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
all_urls += [href for href, _ in LIVE_PAGES]
all_urls += [href for href, _ in META_PAGES]
all_urls += [f"/classes/{slug}/" for slug, *_ in CLASSES]
all_urls += [f"/builds/{slug}-build/" for slug, *_ in CLASSES]
all_urls += [f"/tier-list/{slug}/" for slug in tier_pages]
all_urls += [f"/guides/{slug}/" for slug in guide_pages]
if len(all_urls) != len(set(all_urls)):
    duplicates = sorted({url for url in all_urls if all_urls.count(url) > 1})
    raise ValueError(f"Duplicate sitemap URLs: {duplicates}")
sitemap = "\n".join(f"https://{SITE['domain']}{u}" for u in all_urls)
write("sitemap.txt", sitemap)
xml_sitemap = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n" + "\n".join(
    f"  <url><loc>https://{SITE['domain']}{u}</loc><lastmod>{SITE['updated_iso']}</lastmod><changefreq>{'daily' if u in ['/', '/server-status/', '/codes/', '/meta/update-log/'] else 'weekly'}</changefreq><priority>{'1.0' if u == '/' else '0.9' if u == '/server-status/' else '0.8'}</priority></url>"
    for u in all_urls
) + "\n</urlset>\n"
write("sitemap.xml", xml_sitemap)
write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: https://{SITE['domain']}/sitemap.xml\n")
write("CNAME", f"{SITE['domain']}\n")

print(f"Generated {len(all_urls)} pages in {ROOT}")
