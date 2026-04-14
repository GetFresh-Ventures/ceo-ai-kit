---
name: hubspot-architect
description: Comprehensive HubSpot architecture logic for syncing, integrating, and creating data pipelines using the official Python SDK, OpenAPI spec layer, and the MCP connector.
license: MIT
metadata:
  author: GFV Proactive Intelligence
  version: 1.0.0
  category: core-architecture
---

# /hubspot-architect

**Usage**: Utilize this skill anytime the user requests to build an integration, webhook, CRM sync, or custom Python script leveraging HubSpot.

## 1. Ground Truth First
Before writing ANY integration code, you MUST consult the local reference libraries cloned inside standard GTM architecture:
- **API Spec Layer**: Open and review schemas in `gfv_growth_by_design/references/hubspot/HubSpot-public-api-spec-collection`. Do not guess property names or API structures.
- **Python SDK Layer**: Cross-verify calls using `gfv_growth_by_design/references/hubspot/hubspot-api-python`. Ensure you are using the v3 Python client conventions.

## 2. Syncing & Deduplication
If tasked with syncing external databases (e.g., Supabase / PIL) to HubSpot, leverage the patterns from the official `crm-object-sync` reference implementation:
1. Use an immutable unique identifier (like Email for Contacts, Domain for Companies) to avoid duplicates.
2. Employ an upsert strategy: Check if the object exists. If yes, patch (merge) the data. If no, create it.
3. Write back the generated `hs_object_id` instantly to the external DB to establish a bidirectional mapping.

## 3. Real-time Capabilities vs Scripting
- **Immediate Lookups**: If the user asks "What's in my pipeline?", do NOT write a script. Use the built-in MCP server (`mcp-hubspot`). Query tools like `hubspot_search_data` or `hubspot_get_recent_conversations`.
- **Structural Cleanup**: If the user asks to clean the database or run audits, suggest running the native `hubspot-admin-skills` slash commands (e.g., `/hubspot-audit` or `/hubspot-implementation-plan`).
- **Custom Scripts**: ONLY write custom scripts if the task falls outside MCP coverage and standard admin coverage.

## 4. Execution Sandbox
Any scripts built should be placed in `gfv-brain/scripts/` unless instructed otherwise. Ensure they pull `HUBSPOT_ACCESS_TOKEN` cleanly from the OS environment (`os.getenv`), never hardcode secrets.
