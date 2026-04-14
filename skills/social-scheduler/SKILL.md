---
name: social-scheduler
description: Cross-post and schedule content to 28+ social channels from a single command. Unified posting with per-platform content adaptation.
license: MIT
metadata:
  author: GFV Proactive Intelligence
  version: 1.0.0
  category: Growth Engine
---

# /social-scheduler

**Usage**: Schedule posts across X, LinkedIn, Instagram, Facebook, TikTok, YouTube, and 20+ other platforms. One command, platform-adapted content.

## The Multi-Channel Problem

CEOs and their teams waste hours manually cross-posting content. Each platform has different optimal formats, character limits, hashtag conventions, and posting times. This skill solves that by accepting one piece of content and intelligently adapting it per platform.

## Execution Flow

### 1. Content Ingestion
Accept content in any format: raw text, a blog URL, a voice note summary, or a meeting takeaway. The agent adapts the core message.

### 2. Platform Adaptation Matrix

| Platform | Max Length | Format | Hashtags | Best Time |
|----------|-----------|--------|----------|-----------|
| X/Twitter | 280 chars | Punchy hook + thread option | 1-2 max | 8-10am, 12-1pm |
| LinkedIn | 3,000 chars | Professional narrative + line breaks | 3-5 | Tue-Thu 7-9am |
| Instagram | 2,200 chars | Visual story + caption | 15-20 (comment) | Mon/Wed/Fri 11am |
| Facebook | 63,206 chars | Conversational + question | 1-3 | Wed 11am, Fri 1pm |
| TikTok | 2,200 chars | Hook-first + trending audio ref | 3-5 | Tue-Thu 7pm |

### 3. Scheduling Engine
- Use connected MCP tools (Postiz, Buffer, or native APIs) to push scheduled posts.
- Present the CEO with a preview table before any post goes live.
- Enforce the GFV "Draft Review Before Send" rule — NO automated posting without explicit approval.

### 4. Performance Feedback Loop
- After 48 hours, pull engagement metrics per platform.
- Auto-generate a brief: `[Platform] | [Reach] | [Engagement Rate] | [Top Comment]`
- Feed winners into the `larry-loop` doubling-down engine.

## Security: The Approval Gate
> [!CAUTION]
> This skill NEVER auto-publishes. Every scheduled post must be shown to the CEO with explicit "post it" approval. This is non-negotiable per GFV Rule: "Draft Review Before Send."
