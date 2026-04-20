---
name: twitter
description: Search and retrieve content from Twitter/X. Get user info, tweets, replies, followers, communities, spaces, and trends via twitterapi.io. Use when user mentions Twitter, X, or tweets.
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


# Twitter/X Skill

Get user profiles, tweets, replies, followers/following, communities, spaces, and trends from Twitter/X via twitterapi.io.

## Prerequisites

Set API key in `~/.zshrc`:
```bash
export TWITTERAPI_API_KEY="your_api_key"
```

**Quick Check**:
```bash
cd <skill_directory>
python3 scripts/get_user_info.py elonmusk
```

## Commands

All commands run from the skill directory.

### User Endpoints
```bash
python3 scripts/get_user_info.py USERNAME
python3 scripts/get_user_about.py USERNAME
python3 scripts/batch_get_users.py USER_ID1,USER_ID2
python3 scripts/get_user_tweets.py USERNAME --limit 20
python3 scripts/get_user_mentions.py USERNAME --limit 20
python3 scripts/get_followers.py USERNAME --limit 100
python3 scripts/get_following.py USERNAME --limit 100
python3 scripts/get_verified_followers.py USERNAME --limit 20
python3 scripts/check_relationship.py USER1 USER2
python3 scripts/search_users.py "query" --limit 20
```

### Tweet Endpoints
```bash
python3 scripts/get_tweet.py TWEET_ID [TWEET_ID2...]
python3 scripts/search_tweets.py "query" --type Latest --limit 20
python3 scripts/get_tweet_replies.py TWEET_ID --limit 20
python3 scripts/get_tweet_quotes.py TWEET_ID --limit 20
python3 scripts/get_tweet_retweeters.py TWEET_ID --limit 50
python3 scripts/get_tweet_thread.py TWEET_ID
python3 scripts/get_article.py TWEET_ID
```

### List Endpoints
```bash
python3 scripts/get_list_followers.py LIST_ID --limit 20
python3 scripts/get_list_members.py LIST_ID --limit 20
```

### Community Endpoints
```bash
python3 scripts/get_community.py COMMUNITY_ID
python3 scripts/get_community_members.py COMMUNITY_ID --limit 20
python3 scripts/get_community_moderators.py COMMUNITY_ID
python3 scripts/get_community_tweets.py COMMUNITY_ID --limit 20
python3 scripts/search_community_tweets.py "query" --limit 20
```

### Other Endpoints
```bash
python3 scripts/get_space.py SPACE_ID
python3 scripts/get_trends.py --woeid 1  # Worldwide
```

## Search Query Syntax

```bash
# Basic search
python3 scripts/search_tweets.py "AI agent"

# From specific user
python3 scripts/search_tweets.py "from:elonmusk"

# Date range
python3 scripts/search_tweets.py "AI since:2024-01-01 until:2024-12-31"

# Exclude retweets
python3 scripts/search_tweets.py "AI -filter:retweets"

# With media
python3 scripts/search_tweets.py "AI filter:media"

# Minimum engagement
python3 scripts/search_tweets.py "AI min_faves:1000"
```

## API: twitterapi.io
- Base URL: https://api.twitterapi.io/twitter
- Auth: X-API-Key header
- Pricing: ~$0.15-0.18/1k requests
- Docs: https://docs.twitterapi.io/
