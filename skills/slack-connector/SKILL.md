---
name: slack-connector
description: Read, post, and manage Slack team communications. Channel monitoring, thread replies, and workflow notifications.
short_description: "Read, post, and manage Slack messages"
license: MIT
metadata:
  author: GFV Proactive Intelligence
  version: 2.0.0
  category: Day-to-Day Operations
---

# /slack-connector

**Usage**: Integrate Slack workspace communications into the CEO operating system. Monitor channels, post updates, search history, and route critical messages.


## Quick Start
Just say any of these:
- "Post this update to #general"
- "What did the team discuss today?"
- "Set up a daily standup reminder"


## Prerequisites

Before using this skill, the CEO (or their technical admin) must set up a Slack App:

### Setup Steps
1. Go to [api.slack.com/apps](https://api.slack.com/apps) → **Create New App** → **From Scratch**
2. Name it "CEO Intelligence" (or similar), select the workspace
3. Under **OAuth & Permissions**, add these Bot Token Scopes:
   - `channels:history` — Read public channel messages
   - `channels:read` — List channels
   - `chat:write` — Post messages
   - `search:read` — Search workspace messages
   - `users:read` — Resolve user names
   - `im:history` — Read DM history (only if CEO explicitly enables)
4. **Install to Workspace** → Copy the **Bot User OAuth Token** (`xoxb-...`)
5. Store the token:
   ```bash
   # macOS
   security add-generic-password -s "SLACK_BOT_TOKEN" -a "ceo-kit" -w "xoxb-your-token"
   # Or set as environment variable
   export SLACK_BOT_TOKEN="xoxb-your-token"
   ```

### Verification
```bash
curl -s -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
  https://slack.com/api/auth.test | python3 -m json.tool
```
Expected: `"ok": true` with your bot name.

---

## Capabilities

### 1. Read & Summarize Channels

**List channels:**
```bash
curl -s -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
  "https://slack.com/api/conversations.list?types=public_channel&limit=100" \
  | python3 -c "import sys,json; [print(f'{c[\"id\"]}  #{c[\"name\"]}') for c in json.load(sys.stdin)['channels']]"
```

**Pull recent messages from a channel:**
```bash
CHANNEL_ID="C0123456789"  # from list above
curl -s -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
  "https://slack.com/api/conversations.history?channel=$CHANNEL_ID&limit=20" \
  | python3 -c "
import sys, json
data = json.load(sys.stdin)
for msg in data.get('messages', []):
    user = msg.get('user', 'bot')
    text = msg.get('text', '')[:120]
    print(f'[{user}] {text}')
"
```

**Summarization protocol:**
After pulling messages, the agent summarizes into:
- **Decisions Made**: Any explicit commitments or agreements
- **Action Items**: Tasks assigned with owner names
- **Flags**: Messages containing "urgent", "blocker", "deadline", or CEO @-mentions
- **Sentiment**: Overall team energy (positive/neutral/concerned)

### 2. Post Messages (With Approval Gate)

> [!CAUTION]
> **NEVER auto-post.** Every outbound Slack message requires CEO "send it" approval.

**Draft → Review → Post workflow:**
1. Agent drafts message using `voice-model` for tone
2. Presents to CEO: "Here's the draft for #leadership:"
3. CEO says "send it" → agent posts:

```bash
curl -s -X POST -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"channel": "C0123456789", "text": "Your approved message here"}' \
  https://slack.com/api/chat.postMessage
```

**Reply to a thread:**
```bash
curl -s -X POST -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"channel": "C0123456789", "text": "Reply text", "thread_ts": "1234567890.123456"}' \
  https://slack.com/api/chat.postMessage
```

### 3. Search Workspace History

```bash
QUERY="budget Q2"
curl -s -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
  "https://slack.com/api/search.messages?query=$(python3 -c "import urllib.parse; print(urllib.parse.quote('$QUERY'))")&count=10" \
  | python3 -c "
import sys, json
data = json.load(sys.stdin)
for match in data.get('messages', {}).get('matches', []):
    channel = match.get('channel', {}).get('name', '?')
    user = match.get('username', '?')
    text = match.get('text', '')[:100]
    print(f'#{channel} [{user}]: {text}')
"
```

### 4. Workflow Integrations

This skill pipes into other skills automatically:

| Event | Routing |
|-------|---------|
| `support-triage` escalation | Post to #alerts channel |
| `weekly-ceo-brief` generated | Post summary to #leadership |
| `news-digest` output | Post to #market-intel |
| `deal-review` flags stale deal | DM account owner |
| `post-meeting-brief` captures action items | Post to relevant project channel |

### 5. Channel Health Monitor

Weekly automated check (requires CEO opt-in):
- Which channels had zero activity in 14 days → suggest archiving
- Which channels are highest volume → suggest summarization schedule
- Which team members haven't posted in 7 days → surface to CEO (not to them)

## Error Handling

| Error | Resolution |
|-------|-----------|
| `not_authed` | Token expired or invalid. Re-create bot token. |
| `channel_not_found` | Bot not invited to channel. Have CEO invite the bot. |
| `missing_scope` | Add the required scope in Slack app settings, reinstall. |
| `ratelimited` | Wait `Retry-After` seconds. Slack rate limits: ~1 req/sec. |

## Security Constraints
- Requires Slack Bot Token with scoped permissions — never use user tokens.
- NEVER read DMs without explicit CEO permission for that specific conversation.
- All outbound messages require "send it" approval per GFV Draft Review Before Send rule.
- Never store Slack message content beyond the active session.
- Bot token stored in system keychain, never in plaintext files.

## Live Integration Hooks

| System | What It Provides | How to Access |
|--------|-----------------|---------------|
| PIL | Cross-session intelligence | `pil-memory-bus` / `gfv-brain-search.py` |
| HubSpot / CRM | Real-time pipeline state | `hubspot-api` |

> **GFV Rule:** Check PIL and live systems to verify claims before submitting answers.

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
- 🟡 **Medium** — Deduced from PIL/memory or recent but not validated real-time data.
- 🔴 **Assumed** — No source available, utilizing best-judgment baseline.

## <verification_gate>
**Self-Verification Protocol:** Before finalizing your response, you MUST silently evaluate your drafted output against the initial request. Have you provided concrete Action Items with ownership? Did you use the Bottom Line First formatting? Have you applied Confidence Tags to your claims? If not, rewrite the response before submitting.

## After This Skill
💡 Suggest these next steps:
- "Want me to set up daily channel summaries with `weekly-ceo-brief`?"
- "Should I monitor #sales for deal mentions and cross-reference with `pipeline-pulse`?"
- "Want me to draft a team update for #leadership?"

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Token expired or invalid | Re-authenticate: revoke old token in Slack admin, create new one |
| Missing channels | Bot must be manually invited to private channels |

