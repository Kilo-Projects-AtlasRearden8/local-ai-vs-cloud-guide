# STATUS

## What was built

A beginner manual for running AI locally versus in the cloud, published by
Asdale Dynamics, LLC. The project contains:

- `LICENSE` — MIT License, copyright line exactly
  `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` — project overview, credits Asdale Dynamics, LLC, includes the
  copyright line
- `docs/` — the full manual in Markdown (9 files):
  - `00-read-me-first.md` — welcome, audience, how to use
  - `01-choosing-models.md` — model sizes, quantization, where to find models
  - `02-ram-vram-basics.md` — RAM vs. VRAM, how to check memory, sizing guide
  - `03-ollama-setup.md` — install Ollama, run first model, everyday commands
  - `04-lm-studio-setup.md` — install LM Studio, download a model, chat
  - `05-privacy-benefits.md` — why local AI keeps data private, limits
  - `06-cost-comparison.md` — local vs. cloud costs with real-world examples
  - `07-when-to-use-each.md` — decision flowchart, starter routine
  - `08-glossary.md` — plain-English definitions
- `site/` — the same manual as a static HTML site (10 HTML files + style.css +
  app.js). No build step, no server; open any page in a browser.
- `verify.py` — verification script (link integrity, credits, copyright,
  secret scan)

## How to run it

- Markdown: open any file in `docs/` (start with `00-read-me-first.md`) in a
  text editor or Markdown reader.
- HTML: open `site/index.html` in any web browser and click through the
  navigation. Nothing to install, build, or serve.

No API key, no account, and no credit card are required for the local AI
path (Ollama / LM Studio).

## Verification results

`python3 verify.py` — all checks passed:

- Required files present (LICENSE, README.md, docs, site/index.html)
- LICENSE contains the exact copyright line
  `Copyright (c) 2026 Asdale Dynamics, LLC`
- README.md credits Asdale Dynamics, LLC and includes the copyright line
- Every docs/ and site/ page credits Asdale Dynamics, LLC
- All 10 HTML files validated; all internal links resolve (no broken links)
- CSS (style.css) and JS (app.js) referenced and present
- Required section keywords present in each docs page
- No API keys, secrets, or personal data in any file
- No `.github/workflows` files present

## Known gaps

- The manual covers the local-AI path in depth; cloud setup (creating
  accounts, obtaining API keys) is intentionally out of scope ("no API key or
  account needed"), so cloud-specific click-by-click steps are not included.
- No automated test suite beyond `verify.py`; verification is link/credit/
  copyright integrity rather than rendered-output testing.
- The HTML site is a single folder of static files; no search, dark mode, or
  multi-language support.
- Ollama/LM Studio installation steps describe downloading from vendor sites;
  actual installation was not performed in this environment (no GUI/network
  software installation in scope).

## Style notes

Plain English, step by step, never condescending; local-first; tested via
verify.py; no secrets or personal data. Credit: Asdale Dynamics, LLC
(Indiana, formed October 2026), founded by Dylan Asdale.
