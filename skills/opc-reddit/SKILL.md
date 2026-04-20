---
name: reddit
description: Search and retrieve content from Reddit. Get posts, comments, subreddit info, and user profiles via the public JSON API. Use when user mentions Reddit, a subreddit, or r/ links.
---


> [!IMPORTANT]
> **GFV-Adapted Skill** — This skill runs within the GetFresh Ventures infrastructure. Follow these conventions.

### GFV Infrastructure Integration

**Credentials** — Never use `.env` files. All secrets live in macOS Keychain:
```bash
security find-generic-password -s "<service>" -a "<account>" -w
```
Check `~/Documents/Code/gfv-brain/scripts/pil_config.py` for service mappings.

**Data Sources** — Before querying external APIs, check PIL first:
- `search_pil` / `smart_search` / `vector_search` MCP tools (491K+ embeddings, 81K entities)
- Supabase tables: `entity_embeddings`, `ont_entities`, `ont_facts`
- Local SQLite: WhatsApp (59K msgs), Slack (2.5K msgs), `gfv_memory.db`

**Output** — Save results to `~/Documents/Code/gfv-brain/` or PIL via Supabase. Never send external messages (email, Slack, WhatsApp) without Diraj's explicit "send it" approval.

**Active Clients**:
- **Golden Rule PHC** — HVAC/plumbing/roofing: goldenrulephc.com, rivercityac.com, cornerstoneroofingexteriors.com
- **Aprio Board Portal** — SaaS governance: aprioboardportal.com
- **GetFresh Ventures** — Venture studio: getfreshventures.com

---


# Reddit Skill

Get posts, comments, subreddit info, and user profiles from Reddit via the public JSON API.

## Prerequisites

**No API key required!** Reddit's public JSON API works without authentication.

**Quick Check**:
```bash
cd <skill_directory>
python3 scripts/get_posts.py python --limit 3
```

## Commands

All commands run from the skill directory.

### Subreddit Posts
```bash
python3 scripts/get_posts.py python --limit 20           # Hot posts (default)
python3 scripts/get_posts.py python --sort new --limit 20
python3 scripts/get_posts.py python --sort top --time week
python3 scripts/get_posts.py python --sort top --time all --limit 10
```

### Search Posts
```bash
python3 scripts/search_posts.py "AI agent" --limit 20
python3 scripts/search_posts.py "MCP server" --subreddit ClaudeAI --limit 10
python3 scripts/search_posts.py "async python" --sort top --time year
```

### Subreddit Info
```bash
python3 scripts/get_subreddit.py python
python3 scripts/get_subreddit.py ClaudeAI
```

### Post & Comments
```bash
python3 scripts/get_post.py abc123                       # Get post by ID
python3 scripts/get_post.py abc123 --comments 50         # With more comments
```

### User Profile
```bash
python3 scripts/get_user.py spez
python3 scripts/get_user.py spez --posts 10              # Include recent posts
```

## Sort Options

| Sort | Description | Time Options |
|------|-------------|--------------|
| `hot` | Trending posts (default) | - |
| `new` | Latest posts | - |
| `top` | Highest voted | hour, day, week, month, year, all |
| `rising` | Gaining traction | - |
| `controversial` | Mixed votes | hour, day, week, month, year, all |

## API Info
- **Method**: Public JSON API (no auth needed)
- **Trick**: Append `.json` to any Reddit URL
- **Rate Limit**: 100 requests/minute
- **Docs**: https://www.reddit.com/dev/api
