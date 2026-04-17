---
name: ugc-video
description: Script-to-video production pipeline. AI talking heads, B-roll, voiceover, and subtitles for social media content.
short_description: "Script-to-video production pipeline"
license: MIT
metadata:
  author: GFV Proactive Intelligence
  version: 1.0.0
  category: Growth Engine
---

# /ugc-video

**Usage**: Transform a script, blog post, or talking points into a finished UGC-style video with AI-generated talking head, B-roll, voiceover, and subtitles.


## Quick Start
Just say any of these:
- "Script a 60-second product demo video"
- "Create a talking-head video script for [topic]"
- "Plan a video content series"


## The UGC Content Machine

User-Generated Content style videos drive 4x higher engagement than polished brand content. This skill automates the production pipeline so the CEO can produce daily video content without a video team.

## Pipeline

### 1. Script Generation
- Accept input: raw topic, blog post URL, meeting notes, or bullet points.
- Generate a 30-60 second script optimized for the target platform.
- Structure: Hook (3s) → Problem (10s) → Solution (15s) → CTA (5s).

### 2. Visual Production
- **AI Talking Head**: Generate using HeyGen, Synthesia, or D-ID APIs.
- **B-Roll**: Source from Pexels/Pixabay APIs (royalty-free) matched to script keywords.
- **Text Overlays**: Auto-generate caption cards for key stats or quotes.
- **Subtitles**: Burn-in captions (95% of social video is watched on mute).

### 3. Platform Optimization
| Platform | Aspect Ratio | Max Duration | Format |
|----------|-------------|-------------|--------|
| TikTok | 9:16 | 60s optimal | MP4 |
| Instagram Reels | 9:16 | 90s max | MP4 |
| LinkedIn | 1:1 or 16:9 | 2 min optimal | MP4 |
| YouTube Shorts | 9:16 | 60s | MP4 |

### 4. Review & Approval
- Present video preview + script side-by-side.
- CEO approves or requests revision.
- Route approved videos to `social-scheduler` for distribution.

## Constraints
- All AI-generated faces must be clearly disclosed as AI in the video description.
- Never use real people's likenesses without consent.
- Voice cloning requires explicit CEO opt-in and disclosure.

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
💡 Suggest these next:
- "Try `social-engine` — Create platform-native social media content"
- "Try `copy-master` — Write world-class marketing copy"
- "Try `launch-strategy` — Plan product launches and release strategies"
