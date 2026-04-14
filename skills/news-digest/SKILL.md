---
name: news-digest
description: Deeply synthesized, noise-free external market surveillance targeted specifically against the current GTM Pipeline. 
license: MIT
metadata:
  author: GFV Proactive Intelligence
  version: 1.0.0
  category: Infrastructure
---

# /news-digest

**Usage**: Morning intelligence extraction. Instead of a generic RSS feed parser, this skill dynamically cross-references global news explicitly against the CEO's active companies, competitors, and deal markers.

## Paranoia Constraints
1. **Never Parse Raw DOM Without Handlers**: When extracting news articles from external URLs, DO NOT attempt to write raw python regex scrapers. Rely on validated MCP tools like Firecrawl or the Browser Subagent.
2. **Entity Check**: Only push a news result into the digest if it has a >70% contextual match to a known entity in `~/gtm-brain/pipeline.md` or the Hubspot CRM integration connection.

## Execution Rhythms

### 1. The Entity Map
Before fetching news, read the active pipeline and compile an exact dictionary of keywords (e.g., Company Names, Key Contacts, Competitors, Target Industry Acronyms).

### 2. The Extraction
Utilize the allowed web-search tools (Perplexity MCP, Firecrawl, or Web Search APIs) explicitly scoping the queries to the exact entities established in Step 1 and bounded to the last 24-48 hours.

### 3. The C-Suite Synthesis
Do not present raw links with standard meta-descriptions. Output a curated C-Suite Brief formatted as:
`[IMPACT: High/Med/Low] | [ENTITY] | [DEVELOPMENT] | [GTM IMPLICATION]`
*Always provide the "So What?" — tell the CEO how this affects their active pipeline.*
