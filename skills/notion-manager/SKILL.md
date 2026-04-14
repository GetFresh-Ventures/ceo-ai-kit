---
name: notion-manager
description: Safely connect to and manage Notion workspaces through verified MCP endpoints strictly governing read/write boundaries.
license: MIT
metadata:
  author: GFV Proactive Intelligence
  version: 1.0.0
  category: Day-to-Day Execution
---

# /notion-manager

**Usage**: Utilize this skill when the CEO wants to query, update, or orchestrate across their Notion workspace wikis and databases.

## ⚠️ Security Protocol: The Database Boundary

Unlike typical Notion AI integrations that scrape entire workspaces uncontrollably, this skill operates under a "Verification First" boundary constraints.

1. **Explicit Targeting**: The orchestration agent must NEVER search globally across all Notion. The CEO must explicitly provide the Database ID, Page ID, or the exact name of the table to query.
2. **Schema Verification**: Prior to performing any `WRITE` actions (adding rows, creating to-dos, mutating documentation), the agent MUST first pull the `Schema/Properties` of the database to ensure no column types mismatch resulting in database corruption.
3. **Delete Prohibition**: AI agents executing this skill are strictly forbidden from archiving or deleting Notion pages. Only `CREATE`, `READ`, or `APPEND` actions are permitted.

## Phase 1: Query Execution
When asked to summarize a tracker (e.g., "What are my priorities today?"):
- Use the connected Notion MCP tool to query the specific database.
- Parse the structured JSON into readable, C-Suite markdown.
- Never summarize without listing the exact properties (e.g. Status: `Not Started`).

## Phase 2: Page Generation Strategy
When generating Meeting Notes, PRDs, or Strategies in Notion:
- First, extract the structural map of the destination.
- Generate blocks recursively using the Notion Block architecture.
- Always include an overarching "AI Summary Box" at the top of long documents.
