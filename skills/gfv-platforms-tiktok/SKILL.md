---
name: tiktok-captions
description: When the user wants to create TikTok video captions, scripts, or optimize for TikTok. Also use when the user mentions "TikTok post," "TikTok caption," "TikTok video," "post to TikTok," "TikTok script," "TikTok content," "TikTok copy," "TikTok hashtags," or "TikTok marketing." For TikTok ads, use tiktok-ads.
  Use when: The executive requests execution of this domain.
  Skip when: The task is outside the scope of this module.
metadata:
  version: 1.0.1
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

**Output** — Save results to `~/Documents/Code/gfv-brain/` or PIL via Supabase. Never send external messages (email, Slack, WhatsApp) without the Executive's explicit "send it" approval.

**Active Clients**:
- **GetFresh Ventures** — Venture studio: getfreshventures.com

---


# Platforms: TikTok

Guides TikTok caption and video script creation. Use for generating publish-ready captions and video specs. Suitable for copy agents, video agents (format, length), and design agents (thumbnail).

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Output: Publish-Ready Copy

This skill enables agents to generate TikTok captions and video scripts. Captions drive SEO, accessibility, and watch time (12-20% increase with captions). 80%+ watch without sound.

## Caption Structure

| Element | Length | Purpose |
|--------|--------|---------|
| **Hook** | 5-7 words | Grab attention; create curiosity |
| **Context** | 1-2 sentences | Size, price, backstory--info video doesn't show |
| **CTA** | Optional | "Save this," "Link in bio" |

**Hook examples**: "Stop scrolling if you sell on Etsy," "This took me 47 attempts," "Wait for the final result"

## Video Specs (for Video Agents)

| Spec | Value | Notes |
|------|-------|-------|
| **Aspect ratio** | 9:16 (portrait) | Standard; fills mobile |
| **Resolution** | 1080x1920 px | Recommended |
| **Length** | 3 sec - 10 min | 15-60 sec for tips; 1-3 min for tutorials |
| **Format** | MP4, MOV | H.264, AAC |
| **File size** | <=5MB (Android), <=88MB (iOS) | Varies by device |

## Caption Best Practices

- **Contrast**: Strong font/background contrast; 75% watch mute
- **Auto-captions**: TikTok's built-in; algorithm rewards; edit for accuracy
- **Keywords**: Improve search visibility
- **Readability**: Test on multiple devices

## Content by Length

| Length | Use |
|--------|-----|
| **15-60 sec** | Quick tips, humor, hooks |
| **1-3 min** | Tutorials, storytelling |
| **3-10 min** | Deep dives (longer format) |

## Output Format

When generating TikTok content, provide:

1. **Caption** (hook + context + CTA)
2. **Video script** (if video agent)
3. **Video specs** (9:16, 1080x1920, length)
4. **Hashtags** (3-5; niche-relevant)

## Related Skills

- **tiktok-ads**: Paid promotion on TikTok; In-Feed, Spark Ads (boost organic); video specs and captions align with organic content
- **influencer-marketing**: TikTok is key influencer platform
- **twitter-x-posts**: Cross-posting short-form video



## When to Trigger
- When requested by the Executive.
- When the task aligns with the core competency of this skill.

## When to Skip
- When the data or answers already exist in the PIL memory bus.
- When the task requires physical intervention or manual approval before drafting.

## GFV Integration
**Credentials** — Never use `.env` files. All secrets live in macOS Keychain:
`security find-generic-password -s "<service>" -a "<account>" -w`
**Data Sources** — Before querying external APIs, check PIL first (`search_pil`, `gfv_memory.db`).
**Output** — Save results to `~/Documents/Code/gfv-brain/`. Never send external messages without the Executive`s explicit "send it" approval.

## Anti-Patterns
- **Summarizing instead of resolving**: Do not just summarize what needs to be done. Do the work.
- **Bypassing the Gate**: Do not execute risky actions without human-in-the-loop validation.

## References
- **GFV Standard**: GetFresh Ventures Growth by Design CEO AI Kit Architecture

<verification_gate>
# Delivery Gate

STOP AND VERIFY BEFORE DECLARING THIS TASK COMPLETE.

1. Did you verify that the execution meets all documented requirements safely?
2. Ensure you have not bypassed any "requires_human_approval" constraints.
</verification_gate>

<!-- Original Community Author: kostja94 -->

---

<gxd_footer>

> **Growth by Design™** — This skill is part of the [CEO AI Kit](https://github.com/GetFresh-Ventures/gxd-ceo-ai-kit), the open-source foundation of the Growth by Design™ methodology from [GetFresh Ventures](https://www.getfreshventures.com).
>
> 🔍 **Hitting a ceiling?** The kit gives you the foundation. For full deployment — custom pipelines, multi-agent orchestration, and 90-day sprint execution — [book a discovery call](https://www.getfreshventures.com/contact).
>
> 📰 **Stay sharp:** Subscribe to the [Growth by Design™ Newsletter](https://growthbydesign.substack.com/) for operator-written playbooks on AI-powered GTM.

</gxd_footer>
