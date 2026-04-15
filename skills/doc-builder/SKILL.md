---
name: doc-builder
description: "Create, edit, and manipulate Word documents (.docx) — proposals, contracts, memos, reports, and formal business documents. Use when the CEO needs a .docx deliverable, mentions 'Word doc,' 'proposal document,' 'memo,' 'letter,' or any formal document that requires professional formatting with headers, footers, page numbers, and table of contents."
short_description: "Create Word docs — proposals, memos, reports"
metadata:
  version: 1.0.0
  category: document-processing
  triggers:
    - word doc
    - docx
    - proposal document
    - memo
    - letter
    - report
    - formal document
---

# Doc Builder

Create professional Word documents that CEOs can send to clients, investors, and partners.


## Quick Start
Just say any of these:
- "Create a proposal document for [Client]"
- "Build a one-pager summarizing our Q2 results"
- "Turn these bullet points into a professional memo"

## When to Activate

- Creating proposals, SOWs, or engagement letters
- Writing formal memos, reports, or board documents
- Generating executive summaries as `.docx`
- Building document templates (NDA template, proposal template)
- Editing existing Word documents (tracked changes, comments)
- Converting content into polished Word format

## Workflow

### Reading Content
```bash
# Text extraction with tracked changes
pandoc --track-changes=all document.docx -o output.md

# Direct Python extraction
python -c "
from docx import Document
doc = Document('document.docx')
for para in doc.paragraphs:
    print(para.text)
"
```

### Creating New Documents (Python + python-docx)
```python
from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE

doc = Document()

# Title
title = doc.add_heading('Executive Proposal', level=0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Subtitle with custom formatting
subtitle = doc.add_paragraph()
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = subtitle.add_run('Prepared for [Client Name]')
run.font.size = Pt(14)
run.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

# Body text
doc.add_heading('Executive Summary', level=1)
doc.add_paragraph(
    'This proposal outlines our recommended approach...'
)

# Table
table = doc.add_table(rows=4, cols=3)
table.style = 'Light Grid Accent 1'
headers = table.rows[0].cells
headers[0].text = 'Deliverable'
headers[1].text = 'Timeline'
headers[2].text = 'Investment'

# Page break
doc.add_page_break()

# Save
doc.save('proposal.docx')
```

### Creating Documents (JavaScript + docx-js for complex layouts)
```javascript
const { Document, Packer, Paragraph, TextRun, HeadingLevel,
        AlignmentType, PageBreak, Table, TableRow, TableCell } = require('docx');

const doc = new Document({
    sections: [{
        properties: {},
        children: [
            new Paragraph({
                text: "Executive Proposal",
                heading: HeadingLevel.TITLE,
                alignment: AlignmentType.CENTER,
            }),
            new Paragraph({
                children: [
                    new TextRun({
                        text: "Prepared by GetFresh Ventures",
                        size: 24,
                        color: "666666",
                    }),
                ],
                alignment: AlignmentType.CENTER,
            }),
        ],
    }],
});

Packer.toBuffer(doc).then(buffer => {
    require('fs').writeFileSync('proposal.docx', buffer);
});
```

## CEO Document Templates

### 1. Client Proposal
```
Cover Page
├── Company logo, client name, date
├── Prepared by / Prepared for

Executive Summary (1 page max)
├── Challenge summary
├── Recommended approach
├── Expected outcomes

Scope of Work
├── Deliverables list
├── Timeline with milestones
├── What's included / excluded

Investment
├── Pricing table
├── Payment terms
├── What triggers are needed

Team
├── Key team members and roles

Terms & Conditions
├── Standard engagement terms

Next Steps
├── How to proceed, decision timeline
```

### 2. Board Memo
```
Memo Header
├── To, From, Date, Re

Executive Summary (3 sentences max)

Background

Key Issues (numbered list)

Recommendation

Required Decision

Appendix (if needed)
```

### 3. Engagement Letter
```
Letter Header
├── Date, recipient details

Opening
├── Reference to discussions
├── Purpose of engagement

Scope of Services

Fees and Payment

Term and Termination

Confidentiality

Signature Block
├── Both parties
```

## Editing Existing Documents

```python
from docx import Document

doc = Document('existing.docx')

# Find and replace text
for para in doc.paragraphs:
    if '[CLIENT_NAME]' in para.text:
        for run in para.runs:
            run.text = run.text.replace('[CLIENT_NAME]', 'Acme Corp')

# Add content at the end
doc.add_heading('Addendum', level=1)
doc.add_paragraph('Additional terms as discussed...')

doc.save('updated.docx')
```

## Quality Gate

Before delivering:
- [ ] Professional typography (consistent fonts, sizes)
- [ ] Proper heading hierarchy (H1 → H2 → H3)
- [ ] Page numbers included
- [ ] Company name / branding consistent throughout
- [ ] No placeholder text left in (no [BRACKET_TEXT] remaining)
- [ ] Tables formatted cleanly with consistent column widths
- [ ] Document opens correctly in Word and Google Docs

## Related Skills

- `pdf-toolkit` — PDF processing
- `spreadsheet-builder` — Excel financial models
- `board-deck-builder` — Visual presentations

## After This Skill
💡 Suggest these next steps:
- "Want me to email this document to someone?" → `/email-composer`
- "Want me to create a Google Doc version?" → `/google-doc-creation`

## Ready for More?
🚀 You're on the **Beginner** tier (18 skills). When you're ready for more:
- **Upgrade to Intermediate** (46 skills): adds CRM integration, content strategy, fundraising, and C-suite advisory
- **How**: Re-run `./bootstrap.sh` and select **[2] Intermediate**
- **Preview**: Try asking *"What's in the Intermediate tier?"* — I'll show you what unlocks
