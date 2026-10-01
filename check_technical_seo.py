"""Fail-fast technical SEO checks for the generated static site."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import json
import os
import xml.etree.ElementTree as ET


BASE = Path(__file__).parent
ROOT = Path(os.environ.get("AION2_OUTPUT_DIR", BASE / "public"))
DOMAIN = "aion2meta.wiki"


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False
        self.h1_count = 0
        self.meta = {}
        self.canonicals = []
        self.links = []
        self.schemas = []
        self.in_schema = False
        self.schema_text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self.in_title = True
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "meta" and attrs.get("name"):
            self.meta.setdefault(attrs["name"], []).append(attrs.get("content", ""))
        elif tag == "link" and attrs.get("rel") == "canonical":
            self.canonicals.append(attrs.get("href", ""))
        elif tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        elif tag == "script" and attrs.get("type") == "application/ld+json":
            self.in_schema = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "script" and self.in_schema:
            self.in_schema = False
            self.schemas.append("".join(self.schema_text))
            self.schema_text = []

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.in_schema:
            self.schema_text.append(data)


def route_for(path):
    relative = path.relative_to(ROOT).as_posix()
    if relative == "index.html":
        return "/"
    if relative == "404.html":
        return None
    return "/" + relative.removesuffix("index.html")


def target_exists(href):
    path = urlparse(href).path
    if path == "/":
        return (ROOT / "index.html").exists()
    return (ROOT / path.strip("/") / "index.html").exists() or (ROOT / path.strip("/")).is_file()


def main():
    errors = []
    pages = {}
    for path in sorted(ROOT.rglob("*.html")):
        if "ads" in path.relative_to(ROOT).parts:
            continue
        parser = PageParser()
        parser.feed(path.read_text(encoding="utf-8"))
        route = route_for(path)
        pages[route or "/404.html"] = parser
        label = path.relative_to(ROOT).as_posix()
        if not parser.title.strip():
            errors.append(f"{label}: missing title")
        if len(parser.meta.get("description", [])) != 1:
            errors.append(f"{label}: expected one meta description")
        if parser.h1_count != 1:
            errors.append(f"{label}: expected one h1, found {parser.h1_count}")
        if route and parser.canonicals != [f"https://{DOMAIN}{route}"]:
            errors.append(f"{label}: canonical mismatch {parser.canonicals}")
        if not route and parser.canonicals:
            errors.append(f"{label}: error page must not declare a canonical")
        for raw_schema in parser.schemas:
            try:
                json.loads(raw_schema)
            except json.JSONDecodeError as exc:
                errors.append(f"{label}: invalid JSON-LD ({exc})")
        for href in parser.links:
            if href.startswith("/") and not target_exists(href):
                errors.append(f"{label}: broken internal link {href}")

    root = ET.parse(ROOT / "sitemap.xml").getroot()
    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    sitemap_routes = [urlparse(node.text).path for node in root.findall("s:url/s:loc", namespace)]
    if len(sitemap_routes) != len(set(sitemap_routes)):
        errors.append("sitemap.xml: duplicate URLs")
    expected_routes = {route for route in pages if route != "/404.html"}
    if set(sitemap_routes) != expected_routes:
        errors.append(f"sitemap.xml: route mismatch; missing={sorted(expected_routes - set(sitemap_routes))}, extra={sorted(set(sitemap_routes) - expected_routes)}")

    if errors:
        raise SystemExit("Technical SEO checks failed:\n- " + "\n- ".join(errors))
    print(f"Technical SEO checks passed: {len(expected_routes)} indexable pages, no broken internal links.")


if __name__ == "__main__":
    main()
