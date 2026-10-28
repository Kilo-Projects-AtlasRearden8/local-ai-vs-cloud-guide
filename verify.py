#!/usr/bin/env python3
"""Verification script for the local-ai-vs-cloud-guide project."""
import os
import re
import sys
from html.parser import HTMLParser

ROOT = "/workspace/kilo-lab/local-ai-vs-cloud-guide"
errors = []
warnings = []


def check(condition, message):
    if not condition:
        errors.append(message)
    else:
        print("OK: " + message)


# 1. Required files exist
for f in ["LICENSE", "README.md", "docs/00-read-me-first.md", "site/index.html"]:
    check(os.path.isfile(os.path.join(ROOT, f)), "required file exists: " + f)

# 2. LICENSE copyright line exactly
with open(os.path.join(ROOT, "LICENSE")) as fh:
    license_text = fh.read()
check(
    "Copyright (c) 2026 Asdale Dynamics, LLC" in license_text,
    "LICENSE contains exact copyright line",
)
check(license_text.startswith("MIT License"), "LICENSE starts with MIT License")

# 3. README credits Asdale Dynamics, LLC
with open(os.path.join(ROOT, "README.md")) as fh:
    readme = fh.read()
check("Asdale Dynamics, LLC" in readme, "README credits Asdale Dynamics, LLC")
check("Copyright (c) 2026 Asdale Dynamics, LLC" in readme, "README includes copyright line")

# 4. All docs and site pages credit Asdale Dynamics, LLC
for dirpath, _, files in os.walk(ROOT):
    for fn in files:
        if fn.endswith((".md", ".html")):
            path = os.path.join(dirpath, fn)
            with open(path) as fh:
                content = fh.read()
            rel = os.path.relpath(path, ROOT)
            check(
                "Asdale Dynamics, LLC" in content,
                f"{rel} credits Asdale Dynamics, LLC",
            )
            # LICENSE/READMEs require the exact literal line; HTML uses &copy; entity.
            if fn in ("LICENSE", "README.md") or rel.startswith("docs/"):
                check(
                    "Copyright (c) 2026 Asdale Dynamics, LLC" in content,
                    f"{rel} includes exact copyright line",
                )
            else:
                check(
                    ("Copyright (c) 2026 Asdale Dynamics, LLC" in content)
                    or ("&copy;" in content and "2026" in content),
                    f"{rel} includes copyright mark/year",
                )

# 5. No actual secrets (API keys, sk- tokens, passwords as values)
secret_patterns = [r"sk-[A-Za-z0-9]{20,}", r"API[_-]?KEY\s*=\s*['\"][^'\"]+",
                   r"SECRET\s*=\s*['\"][^'\"]+", r"password\s*=\s*['\"][^'\"]+"]
for dirpath, _, files in os.walk(ROOT):
    for fn in files:
        if fn.endswith((".md", ".html", ".css", ".js")) or fn == "LICENSE":
            path = os.path.join(dirpath, fn)
            with open(path) as fh:
                content = fh.read()
            rel = os.path.relpath(path, ROOT)
            for pat in secret_patterns:
                if re.search(pat, content, re.IGNORECASE):
                    errors.append(f"possible secret in {rel}: pattern {pat}")

# 6. HTML internal links resolve
class LinkChecker(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.links = []
    def handle_starttag(self, tag, attrs):
        if tag in ("a", "link"):
            for k, v in attrs:
                if k == "href" and v and not v.startswith(("http://", "https://", "mailto:", "#")):
                    self.links.append(v)
        if tag == "script":
            for k, v in attrs:
                if k == "src" and v and not v.startswith(("http://", "https://")):
                    self.links.append(v)
        if tag == "img":
            for k, v in attrs:
                if k == "src" and v:
                    self.links.append(v)

site_dir = os.path.join(ROOT, "site")
html_files = [f for f in os.listdir(site_dir) if f.endswith(".html")]
for html_file in html_files:
    path = os.path.join(site_dir, html_file)
    with open(path) as fh:
        content = fh.read()
    parser = LinkChecker(path)
    parser.feed(content)
    for link in parser.links:
        # strip fragment/query
        target = link.split("#")[0].split("?")[0]
        # resolve relative to site dir
        target_path = os.path.normpath(os.path.join(site_dir, os.path.dirname(html_file), target))
        if not os.path.isfile(target_path):
            errors.append(f"broken link in {html_file}: -> {link} (resolved {target_path})")

# 7. CSS/JS referenced exist
for html_file in html_files:
    path = os.path.join(site_dir, html_file)
    with open(path) as fh:
        content = fh.read()
    for ref in ["style.css", "app.js"]:
        if ref in content and not os.path.isfile(os.path.join(site_dir, ref)):
            errors.append(f"{html_file} references missing {ref}")

# 8. Required sections present in docs
required_sections = {
    "docs/01-choosing-models.md": ["choosing models", "quantization", "ollama"],
    "docs/02-ram-vram-basics.md": ["ram", "vram"],
    "docs/03-ollama-setup.md": ["ollama", "ollama run"],
    "docs/04-lm-studio-setup.md": ["lm studio"],
    "docs/05-privacy-benefits.md": ["privacy"],
    "docs/06-cost-comparison.md": ["cost", "comparison"],
    "docs/07-when-to-use-each.md": ["when to use"],
}
for doc, keywords in required_sections.items():
    path = os.path.join(ROOT, doc)
    with open(path) as fh:
        content = fh.read().lower()
    for kw in keywords:
        check(kw in content, f"{doc} covers '{kw}'")

print("\n" + "=" * 60)
if errors:
    print("FAILURES:")
    for e in errors:
        print("  - " + e)
    sys.exit(1)
else:
    print(f"All checks passed ({len(html_files)} HTML files validated).")
    if warnings:
        print("Warnings:")
        for w in warnings:
            print("  - " + w)
