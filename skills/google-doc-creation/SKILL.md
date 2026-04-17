---
name: google-doc-creation
description: Create professional, executive-ready Google Docs with branded styling. Use this whenever the user asks to create a Google Doc, report, strategy document, or any document in Google Drive. ALL agents must use this skill — never create raw/unstyled docs.
short_description: "Create professional Google Docs in Drive"
---

# Google Doc Creation — Professional Documents


## Quick Start
Just say any of these:
- "Create a Google Doc: [title]"
- "Write a strategy document for [initiative] and put it in Drive"
- "Turn these notes into a professional Google Doc"

## When to Use This Skill

Use this skill **any time** a Google Doc needs to be created, including:
- Strategy reports, audit reports, growth plans
- Client-facing documents (proposals, analyses, recommendations)
- Internal reports (status updates, retrospectives)
- Any document requested to be placed in Google Drive

**NEVER create a plain, unstyled Google Doc.** Every doc must have professional styling applied automatically.

## The Script

**Location:** `~/ceo-brain/scripts/create_google_doc.py`

### Quick Usage

```python
# From Python
import sys
sys.path.insert(0, os.path.expanduser("~/ceo-brain/scripts"))
from create_google_doc import create_formatted_doc

url = create_formatted_doc(
    markdown_content,
    title="My Professional Document",
    folder_id="GOOGLE_DRIVE_FOLDER_ID"
)
```

```bash
# From the terminal
python3 ~/ceo-brain/scripts/create_google_doc.py \
    --input content.md \
    --title "My Document" \
    --folder FOLDER_ID
```

### Auth

- **Preferred:** Service Account at `~/.config/gfv/gfv_service_account.json` with domain-wide delegation (impersonates `{{CEO_EMAIL}}`)
- **Fallback:** `gws` command-line tool for content insertion, service account for styling pass

### What It Does Automatically

The script handles two phases:

1. **Content Insertion** — Parses markdown → inserts headings, paragraphs, tables, lists, horizontal rules via Docs API `batchUpdate`
2. **Professional Styling Pass** — Reads the doc back and applies all visual design rules (see below)

## ⚠️ HARD DESIGN RULES — NEVER SKIP

Every Google Doc created by any agent MUST comply with ALL of these rules. They are enforced automatically by `create_google_doc.py`.

### Typography

| Element | Size | Weight | Color |
|---------|------|--------|-------|
| H1 (Title/Part headers) | 20pt | Bold | Navy `#1B2A4A` |
| H2 (Section headers) | 16pt | Bold | Navy `#1B2A4A` |
| H3 (Sub-section headers) | 13pt | Bold | Dark Navy `#141F38` |
| Body text | 11pt | Regular | Black |
| Table header text | 10pt | Bold | White `#FFFFFF` |

### Heading Rules

- All headings use `keepWithNext: true` so they never orphan at page bottoms
- H1 has **28pt above, 10pt below** spacing (major section break)
- H2 has **22pt above, 8pt below** spacing (sub-section break)
- H3 has **16pt above, 6pt below** spacing (minor sub-section)
- Line spacing: headings at 100%, body at 115%

### Table Design — MANDATORY

| Element | Style |
|---------|-------|
| **Header row background** | Navy `#1B2A4A` |
| **Header row text** | White, Bold, 10pt |
| **Odd body rows** | White background (default) |
| **Even body rows** | Light Gray `#F5F5F5` |
| **Cell padding** | Header: 4pt top/bottom, 6pt left/right. Body: 3pt top/bottom, 6pt left/right |
| **Column widths** | Auto-fitted proportional to max content length per column |

### Column Width Auto-Fit Algorithm

Column widths are calculated as:
1. Measure the max text length in each column (all rows including header)
2. Calculate proportional width: `width_pt = max(60, page_width * col_length / total_length)`
3. Page width is 468pt (6.5 inches at 72pt/in)
4. Minimum column width is 60pt to prevent collapse

### Callout / Blocker Text

Lines containing these keywords are automatically styled **bold red** (`#CC1919`):
- "WordPress access is the critical-path blocker"
- "WordPress access is the single gating dependency"
- "CRITICAL"
- "⚠️"

### Horizontal Rules

- Rendered as a paragraph with `borderBottom` (solid, 1pt, gray `#B3B3B3`)
- 6pt padding below the border
- Do NOT use on the title paragraph — only between major sections

### Title / Cover Page — MANDATORY

Every professional report MUST include a branded title page. Pass `cover_page` dict to `create_formatted_doc()`.

**Layout (top → bottom, all centered, NO blank lines):**

| Element | Style |
|---------|-------|
| **Main title** | 36pt, bold, Navy `#1B2A4A`, centered, **200pt `spaceAbove`** (pushes ~40% down page) |
| **Subtitle** | 24pt, regular, Gray `#666666`, centered, 30pt below |
| **Domain** | 13pt, italic, Navy, centered, 1.5pt navy `borderBottom` divider, 8pt padding |
| **Prepared by** | 12pt, Gray, centered, 24pt above |
| **Date** | 12pt, Gray, centered, 30pt below |
| **CONFIDENTIAL** | 9pt, Light Gray `#999999`, centered, 20pt above |
| **Page break** | Separates title page from body content |

> [!IMPORTANT]
> **NEVER use blank `\n` lines for vertical spacing.** They inherit the default 11pt paragraph height and will push content to page 2. Always use `spaceAbove`/`spaceBelow` on paragraph styles. The 200pt `spaceAbove` on the title paragraph is the canonical way to push content down the page.

**Usage:**

```python
url = create_formatted_doc(
    markdown_content,
    title="Client — Report Title",
    folder_id="DRIVE_FOLDER_ID",
    cover_page={
        "title": "SEO Growth Strategy",
        "subtitle": "Your Company Name",
        "domain": "example.com",
        "prepared_by": "GetFresh Ventures",
        "date": "April 2026",
        "confidential": True,
    }
)
```

## Writing Content for the Doc

### Markdown Format

Write content as standard markdown. The parser supports:
- `# H1`, `## H2`, `### H3` headings
- `**bold**`, `*italic*`, `***bold italic***`
- Bullet lists (`- item`)
- Numbered lists (`1. item`)
- Pipe tables (`| col1 | col2 |`)
- Horizontal rules (`---`)

### Table Cell Content Rules

- Keep table cell text **concise** — long text causes wrapping and poor readability
- For short values (grades, scores, dates), use minimal text
- For descriptions, keep to ~40 characters max per cell

### Title Rules

- The H1 title should be a single line — keep it under 50 characters
- If a title would wrap at 20pt, shorten it or break into title + subtitle
- Use an em dash (—) as separator in compound titles: "Client — Report Type"

## Shared Drive Locations

| Client | Drive ID | Notes |
|--------|----------|-------|
| Client A | `YOUR_SHARED_DRIVE_ID` | Client shared drive |
| Internal | `YOUR_INTERNAL_FOLDER_ID` | Internal working folder |

## Common Workflow

```python
import os, sys
sys.path.insert(0, os.path.expanduser("~/ceo-brain/scripts"))

# 1. Write the markdown content
md_content = """
# Client A — SEO Growth Strategy

Domain: example.com · Date: April 2026

---

## Executive Summary

The key findings are...

| Pillar | Grade | Score | Key Finding |
|--------|-------|-------|-------------|
| Content | B+ | 82/100 | Good depth |
| Keywords | C | 55/100 | 57% uncovered |

---

## Next Steps

- Fix performance issues
- Create competitor pages
"""

# 2. Create the doc (styling applied automatically)
from create_google_doc import create_formatted_doc
url = create_formatted_doc(
    md_content,
    title="Client A — SEO Growth Strategy",
    folder_id="YOUR_SHARED_DRIVE_ID"
)
print(f"Doc ready: {url}")
```

## For Shared Drives (Important)

When placing docs in Shared Drives, you may need the SA direct approach instead of `gws`:

```python
from google.oauth2 import service_account
from googleapiclient.discovery import build

SA_KEY = os.path.expanduser("~/.config/gfv/gfv_service_account.json")
creds = service_account.Credentials.from_service_account_file(
    SA_KEY,
    scopes=["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/documents"],
    subject="{{CEO_EMAIL}}"  # Replace with your Google Workspace email
)
drive = build("drive", "v3", credentials=creds, cache_discovery=False)
docs_svc = build("docs", "v1", credentials=creds, cache_discovery=False)

# Create doc in shared drive
doc_file = drive.files().create(
    body={
        "name": "Document Title",
        "mimeType": "application/vnd.google-apps.document",
        "parents": [DRIVE_ID]
    },
    supportsAllDrives=True,
    fields="id,name,webViewLink"
).execute()

# Then parse + insert content using create_google_doc functions
from create_google_doc import parse_markdown, build_requests, apply_professional_styling
elements = parse_markdown(md_content)
reqs = build_requests(elements)

# Send style defaults + content in one batch each
docs_svc.documents().batchUpdate(documentId=doc_file["id"], body={"requests": reqs}).execute()

# Apply professional styling
apply_professional_styling(doc_file["id"], docs_svc)
```

## Known Limitations

1. **No chunk splitting** — All batchUpdate requests must be sent in a single call. Splitting corrupts tables due to reverse-order cell inserts with forward index tracking.
2. **No `updateNamedStyle`** — Despite docs showing it, `updateNamedStyle` is NOT a valid batchUpdate request type in the Docs API v1. All heading styling (color, size, spacing) is applied per-element via `updateTextStyle` + `updateParagraphStyle` in the post-insertion styling pass.
3. **Images** — Not supported. Use an image-generation tool or dedicated report skill for image-based reports.
4. **Links** — Inline markdown links are not yet parsed. Add links manually after creation.
5. **Nested lists** — Only single-level bullets/numbers supported.
6. **Page breaks** — Google Docs auto-paginates. Tables may split across pages. Use `keepWithNext` on headings to prevent orphans.

## Post-Creation Validation — MANDATORY

After every doc creation, the agent MUST visually validate the output. Open the doc URL in the browser and verify:

| Check | What to Look For |
|-------|------------------|
| **Title page fits one page** | All elements (title, subtitle, domain, attribution, date, CONFIDENTIAL) are visible on page 1 with no overflow to page 2 |
| **Page break is clean** | Content body starts on the page after the title page |
| **Headings are navy** | H1, H2, H3 should all be Navy `#1B2A4A`, not black |
| **Table headers are navy** | First row of each table should have navy background with white bold text |
| **Table columns are readable** | Auto-fitted column widths, no crushed/garbled cells |
| **Alternating row shading** | Even rows should have `#F5F5F5` background |
| **Red callouts** | Lines containing ❌, ⚠️, BLOCKED, etc. should be bold red |
| **No orphan headings** | Headings should not appear alone at the bottom of a page |

If ANY check fails, fix the issue before returning the URL to the user.

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| Title page splits across 2 pages | Blank lines used for spacing | Remove blank lines, use `spaceAbove: 200pt` on title paragraph |
| Tables after first one garbled | Chunk splitting | Never chunk — send all requests in one batch |
| No styling applied | SA auth missing | Ensure `~/.config/gfv/gfv_service_account.json` exists |
| "index out of range" error | Doc doesn't start at index 1 | Create a blank doc first, don't reuse existing |
| Tables have wrong data | Forward index tracking drift | Use SA direct approach with group-by-table batching |

## Live Integration Hooks

| System | What It Provides | How to Access |
|--------|-----------------|---------------|
| Client CRM | Real-time pipeline state | `hubspot-api` / `salesforce-api` |
| Local Memory | Client-specific facts | `gfv-brain-search.py` |

> **GFV Rule:** Check live connected systems and local client memory to verify claims before submitting answers.

## Proactive Triggers

Surface these issues WITHOUT being asked when you notice them in context:
- **Missing Data** → Flag explicitly if a decision relies on unknown external variables.
- **Scope Creep** → Alert if the requested operation spans beyond immediate context goals.
- **Executive Bottlenecks** → Warn if the action plan relies entirely on unassigned human approval gates.
- **Financial Risk** → Call out actions that may trigger unexpected OPEX burn (e.g. infinite LLM agent loops).

## Output Artifacts

| When you ask for... | You get... |
|---------------------|------------|
| Process Map | A mermaid.js chronological diagram |
| Executive Decision | BOTTOM LINE FIRST layout with options + trade-offs |
| Data Audit | A structured table grouping issues by severity |
| Code Execution | Isolated, copy-ready code blocks + terminal commands |

## Confidence Tagging

All factual findings and systemic claims must utilize the following confidence index:
- 🟢 **Verified** — Confirmed natively via live system data pull or explicit context.
- 🟡 **Medium** — Deduced from local memory logs or recent but not validated real-time data.
- 🔴 **Assumed** — No source available, utilizing best-judgment baseline.

## <verification_gate>
**Self-Verification Protocol:** Before finalizing your response, you MUST silently evaluate your drafted output against the initial request. Have you provided concrete Action Items with ownership? Did you use the Bottom Line First formatting? Have you applied Confidence Tags to your claims? If not, rewrite the response before submitting.

## After This Skill
💡 Suggest these next steps:
- "Want me to share this doc with your team via Google Drive?"
- "Should I create a complementary spreadsheet with `spreadsheet-builder`?"
- "Want me to draft an email sending this report with `email-composer`?"

## Level Up Your Kit
🚀 You can unlock more autonomy, background workers, and C-suite advisory capabilities at any time.
- **Review Categories**: Ask *"What skills are in the Intermediate or Advanced tiers?"*
- **How to Upgrade**: Run `./bootstrap.sh` in the repository root and select your new tier.
