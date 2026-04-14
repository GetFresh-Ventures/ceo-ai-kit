---
name: slack-connector
description: Read, post, and manage Slack team communications. Channel monitoring, thread replies, and workflow notifications.
license: MIT
metadata:
  author: GFV Proactive Intelligence
  version: 1.0.0
  category: Day-to-Day Operations
---

# /slack-connector

**Usage**: Integrate Slack workspace communications into the CEO operating system. Monitor channels, post updates, search history, and route critical messages.

## Capabilities

### 1. Read & Summarize
- Pull unread messages from specified channels.
- Summarize threads into executive-level briefs: who said what, decisions made, action items.
- Flag messages mentioning the CEO by name or containing keywords like "urgent", "blocker", "deadline."

### 2. Post & Notify
- Draft messages in the CEO's voice (via `voice-model`).
- Post to channels or threads with CEO approval.
- Send DMs to specific team members.
- Enforce "Draft Review Before Send" — never auto-post.

### 3. Search & Recall
- Search message history by keyword, person, date range, or channel.
- Extract decisions and commitments from past conversations.
- Cross-reference with `decision-logger` to verify execution.

### 4. Workflow Integration
- Route `support-triage` high-severity alerts to a #alerts channel.
- Post `weekly-ceo-brief` summaries to #leadership.
- Pipe `news-digest` outputs to #market-intel.

## Security Constraints
- Requires Slack Bot Token with scoped permissions (channels:read, chat:write, search:read).
- NEVER read DMs without explicit CEO permission for that specific conversation.
- All outbound messages require approval per GFV "Draft Review Before Send" rule.
