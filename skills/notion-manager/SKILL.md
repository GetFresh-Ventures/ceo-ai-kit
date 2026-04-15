---
name: notion-manager
description: "Query, create, and update pages and databases in Notion. Use when the user wants to manage their Notion workspace, sync data to Notion, or pull information from Notion databases."
short_description: "Query and manage Notion pages and databases"
---

# Notion Manager

Interact with Notion workspaces through the API. Always verify database schemas before writing — blind writes corrupt data.


## Quick Start
Just say any of these:
- "Create a project tracker in Notion"
- "Query my Notion database for [criteria]"
- "Organize my Notion workspace"


## When to Use

- "Check my Notion for [topic]"
- "Add [item] to my Notion database"
- "Update the [name] page in Notion"
- "Sync [data] to Notion"
- Any Notion workspace management

## Prerequisites

### Authentication
```python
import os
NOTION_TOKEN = os.environ.get("NOTION_API_KEY")
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}
```

**Token source:** Integration token from https://www.notion.so/my-integrations. Must be shared with target pages/databases.

### MCP Alternative
If Notion MCP server is configured, use MCP tools instead of raw API calls:
- `notion_search` — Find pages and databases
- `notion_read_page` — Read page content
- `notion_update_page` — Update page properties

## Common Operations

### 1. Search for a Database

```python
import requests

response = requests.post(
    "https://api.notion.com/v1/search",
    headers=HEADERS,
    json={
        "query": "Tasks",
        "filter": {"property": "object", "value": "database"}
    }
)
databases = response.json()["results"]
for db in databases:
    print(f"{db['id']}: {db['title'][0]['plain_text']}")
```

### 2. Read Database Schema (MANDATORY before writing)

```python
def get_schema(database_id):
    """Always read schema before creating/updating rows."""
    response = requests.get(
        f"https://api.notion.com/v1/databases/{database_id}",
        headers=HEADERS
    )
    db = response.json()
    schema = {}
    for prop_name, prop_config in db["properties"].items():
        schema[prop_name] = {
            "type": prop_config["type"],
            "id": prop_config["id"]
        }
    return schema

# ALWAYS run this first
schema = get_schema("YOUR_DATABASE_ID")
print(schema)  # Verify property names and types before writing
```

### 3. Query Database Rows

```python
response = requests.post(
    f"https://api.notion.com/v1/databases/{database_id}/query",
    headers=HEADERS,
    json={
        "filter": {
            "property": "Status",
            "select": {"equals": "In Progress"}
        },
        "sorts": [
            {"property": "Priority", "direction": "ascending"}
        ],
        "page_size": 20
    }
)
rows = response.json()["results"]
```

### 4. Create a Page (Row)

```python
def create_row(database_id, properties):
    """Create a new row in a Notion database."""
    response = requests.post(
        "https://api.notion.com/v1/pages",
        headers=HEADERS,
        json={
            "parent": {"database_id": database_id},
            "properties": properties
        }
    )
    return response.json()

# Example: Create a task
create_row("DB_ID", {
    "Name": {"title": [{"text": {"content": "Review Q2 financials"}}]},
    "Status": {"select": {"name": "To Do"}},
    "Priority": {"select": {"name": "High"}},
    "Due Date": {"date": {"start": "2026-04-20"}}
})
```

### 5. Update a Page

```python
def update_row(page_id, properties):
    """Update properties on an existing Notion page."""
    response = requests.patch(
        f"https://api.notion.com/v1/pages/{page_id}",
        headers=HEADERS,
        json={"properties": properties}
    )
    return response.json()

# Example: Mark task complete
update_row("PAGE_ID", {
    "Status": {"select": {"name": "Done"}}
})
```

## Property Type Reference

| Notion Type | JSON Structure |
|------------|---------------|
| `title` | `{"title": [{"text": {"content": "value"}}]}` |
| `rich_text` | `{"rich_text": [{"text": {"content": "value"}}]}` |
| `number` | `{"number": 42}` |
| `select` | `{"select": {"name": "Option"}}` |
| `multi_select` | `{"multi_select": [{"name": "Tag1"}, {"name": "Tag2"}]}` |
| `date` | `{"date": {"start": "2026-04-14"}}` |
| `checkbox` | `{"checkbox": true}` |
| `url` | `{"url": "https://example.com"}` |
| `email` | `{"email": "user@example.com"}` |

## Safety Rules

1. **Never search globally** — always target a specific database ID or page ID
2. **Read schema before ANY write** — property name mismatches silently fail
3. **Verify access** — the integration must be shared with the target page/database
4. **Pagination** — results are capped at 100. Check `has_more` and use `start_cursor`
5. **Rate limits** — 3 requests/second. Add `time.sleep(0.35)` between batch operations

## Integration

- Used by `/weekly-ceo-brief` to pull status from Notion databases
- Used by `/chief-of-staff` for task management
- Syncs with Linear via manual export (no native integration)

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Database views are slow | Limit the number of relations and rollups — they compound query time |
| Team not using Notion | Create a dashboard as their 'home' page — one click to everything |



## After This Skill
💡 Suggest these next:
- "Try `doc-builder` — Create Word docs — proposals, memos, reports"
- "Try `spreadsheet-builder` — Build and analyze Excel spreadsheets"
- "Try `chief-of-staff` — Your always-on executive AI assistant"
