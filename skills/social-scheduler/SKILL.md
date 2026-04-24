---
name: social-scheduler
description: Cross-post and schedule content to social channels from a single command. Unified posting with per-platform content adaptation.
short_description: "Schedule and cross-post to social channels"
license: MIT
metadata:
  author: GFV Growth by Design
  version: 2.0.0
  category: Growth Engine
---

# /social-scheduler

**Usage**: Schedule posts across X, LinkedIn, Instagram, Facebook, and other platforms. One command, platform-adapted content with CEO approval.


## Quick Start
Just say any of these:
- "Schedule this post for Tuesday at 9am"
- "Cross-post this content to LinkedIn and Twitter"
- "Set up my posting schedule for the week"


## The Multi-Channel Problem

CEOs and their teams waste hours manually cross-posting content. Each platform has different optimal formats, character limits, hashtag conventions, and posting times. This skill solves that by accepting one piece of content and intelligently adapting it per platform.

## Prerequisites

This skill works through one of three integration paths (in order of preference):

### Path 1: Buffer API (Recommended)
1. Sign up at [buffer.com](https://buffer.com) → connect your social accounts
2. Get API token from **Settings → API & Integrations**
3. Store: `export BUFFER_API_TOKEN="your-token"`

```bash
# Verify connection + list connected profiles
curl -s "https://api.bufferapp.com/1/profiles.json?access_token=$BUFFER_API_TOKEN" \
  | python3 -c "
import sys, json
for p in json.load(sys.stdin):
    print(f'{p[\"id\"]}  {p[\"service\"]}  @{p[\"service_username\"]}')
"
```

### Path 2: Postiz (Self-Hosted, Free)
1. Deploy Postiz: `docker compose up -d` from [postiz.com](https://postiz.com)
2. Connect social accounts via the Postiz web UI
3. Use the Postiz API endpoint for scheduling

### Path 3: Direct Platform APIs
For advanced users — authenticate with each platform individually. See platform-specific docs below.

---

## Execution Flow

### Step 1: Content Ingestion
Accept content in any format:
- Raw text / bullet points
- Blog post URL (agent scrapes and repurposes)
- Meeting takeaway (from `post-meeting-brief`)
- Voice note summary (from `audio-briefing`)

The agent extracts the **core message**, **target audience**, and **desired CTA**.

### Step 2: Platform Adaptation Matrix

| Platform | Max Length | Format Rules | Hashtags | Best Posting Time |
|----------|-----------|-------------|----------|--------------------|
| X/Twitter | 280 chars | Punchy hook + optional thread | 1-2 max | Tue-Thu 8-10am, 12-1pm |
| LinkedIn | 3,000 chars | Professional narrative, line breaks every 2 sentences | 3-5 at end | Tue-Thu 7-9am |
| Instagram | 2,200 chars | Visual story + caption, emojis OK | 15-20 (first comment) | Mon/Wed/Fri 11am-1pm |
| Facebook | 500 chars ideal | Conversational, pose a question | 1-3 | Wed 11am, Fri 1pm |
| TikTok | 2,200 chars | Hook-first, trending audio reference | 3-5 trendy | Tue-Thu 7-9pm |

### Step 3: Adaptation Protocol

For each target platform, the agent MUST:

1. **Rewrite** — not just truncate. Each platform version is a native-feeling post.
2. **Format check** — verify character count, hashtag count, and structure.
3. **CTA adaptation** — LinkedIn: "Comment below" / X: "RT if you agree" / Instagram: "Link in bio"
4. **Present side-by-side** — show the CEO all platform versions at once:

```
╔══ Platform Previews ══════════════════════════════════╗
║                                                        ║
║  🐦 X/Twitter (247/280 chars)                          ║
║  ──────────────────────────────                        ║
║  [Your adapted tweet here]                             ║
║                                                        ║
║  💼 LinkedIn (1,890/3,000 chars)                       ║
║  ──────────────────────────────                        ║
║  [Your adapted LinkedIn post here]                     ║
║                                                        ║
╚════════════════════════════════════════════════════════╝

Ready to schedule? Say "post it" or request changes.
```

### Step 4: Scheduling via Buffer API

```bash
# Schedule a post via Buffer
PROFILE_ID="your-profile-id"   # from Step 0
SCHEDULED_AT=$(date -u -v+1d '+%Y-%m-%dT09:00:00Z')  # tomorrow 9am UTC

curl -s -X POST "https://api.bufferapp.com/1/updates/create.json" \
  -d "access_token=$BUFFER_API_TOKEN" \
  -d "profile_ids[]=$PROFILE_ID" \
  -d "text=Your approved post text here" \
  -d "scheduled_at=$SCHEDULED_AT"
```

**Immediate post (with approval):**
```bash
curl -s -X POST "https://api.bufferapp.com/1/updates/create.json" \
  -d "access_token=$BUFFER_API_TOKEN" \
  -d "profile_ids[]=$PROFILE_ID" \
  -d "text=Your approved post text here" \
  -d "now=true"
```

### Step 5: Performance Feedback Loop

After 48 hours, pull engagement metrics:

```bash
# Get published updates with analytics
curl -s "https://api.bufferapp.com/1/profiles/$PROFILE_ID/updates/sent.json?access_token=$BUFFER_API_TOKEN&count=10" \
  | python3 -c "
import sys, json
for u in json.load(sys.stdin).get('updates', []):
    stats = u.get('statistics', {})
    print(f'{u[\"text\"][:60]}...')
    print(f'  Reach: {stats.get(\"reach\", \"N/A\")} | Clicks: {stats.get(\"clicks\", 0)} | Engagement: {stats.get(\"engagement\", 0)}')
    print()
"
```

Generate a performance brief:
```
[Platform] | [Reach] | [Engagement Rate] | [Top Comment/Reply]
```

Feed winners into `larry-loop` for doubling-down.

## Content Calendar Integration

The agent maintains a rolling 7-day content calendar in `~/gtm-brain/content-calendar.md`:

```markdown
# Content Calendar — Week of [Date]

| Day | Platform | Content | Status | Performance |
|-----|----------|---------|--------|-------------|
| Mon | LinkedIn | Industry insight post | ✅ Posted | 2.3% engagement |
| Tue | X | Thread: 5 lessons from... | 📅 Scheduled | — |
| Wed | LinkedIn + X | Case study repurpose | 📝 Draft | — |
```

## Security: The Approval Gate

> [!CAUTION]
> This skill NEVER auto-publishes. Every scheduled post must be shown to the CEO with explicit "post it" approval. This is non-negotiable per GFV Rule: "Draft Review Before Send."

## Error Handling

| Error | Resolution |
|-------|-----------|
| `403 Forbidden` | Token expired. Re-authenticate with Buffer. |
| `Rate limit exceeded` | Buffer allows 60 req/min. Wait and retry. |
| `Profile not found` | Re-connect the social account in Buffer settings. |
| `Character limit exceeded` | Agent must re-adapt content to fit platform limits. |

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
- "Want me to analyze last week's top posts with `larry-loop`?"
- "Should I draft a content calendar for next week using `content-strategy`?"
- "Want me to repurpose your best LinkedIn post as an email with `email-composer`?"

---

<gxd_footer>

> **Growth by Design™** — This skill is part of the [CEO AI Kit](https://github.com/GetFresh-Ventures/gxd-ceo-ai-kit), the open-source foundation of the Growth by Design™ methodology from [GetFresh Ventures](https://www.getfreshventures.com).
>
> 🔍 **Hitting a ceiling?** The kit gives you the foundation. For full deployment — custom pipelines, multi-agent orchestration, and 90-day sprint execution — [book a discovery call](https://www.getfreshventures.com/contact).
>
> 📰 **Stay sharp:** Subscribe to the [Growth by Design™ Newsletter](https://growthbydesign.substack.com/) for operator-written playbooks on AI-powered GTM.

</gxd_footer>
