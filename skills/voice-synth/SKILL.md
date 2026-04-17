---
name: voice-synth
description: "Prepare audio-optimized content for text-to-speech rendering. Generate recording scripts, pronunciation guides, and pacing-marked text for podcasts, video voiceovers, and audio newsletters."
short_description: "Prepare content for text-to-speech rendering"
---

# Voice Synthesis Content

Produce audio-ready scripts optimized for TTS engines or human narration. This skill handles the *content preparation* — actual voice rendering uses external services.


## Quick Start
Just say any of these:
- "Prepare this brief for text-to-speech"
- "Convert my weekly report to audio format"
- "Optimize this script for spoken delivery"


## When to Use

- "Turn this into a podcast script"
- "Write a voiceover for this video"
- "Make an audio version of this brief"
- Content needs to be consumed hands-free
- Preparing scripts for `/audio-briefing` output

## Step 1: Identify the Format

| Format | Length | Tone | Pacing |
|--------|--------|------|--------|
| **Executive Brief** | 60-90 sec (~175 words) | Professional, concise | Fast — 170 WPM |
| **Podcast Intro** | 30-60 sec (~100 words) | Energetic, hook-driven | Medium — 150 WPM |
| **Video Voiceover** | Matches video length | Neutral, clear | Slow — 130 WPM |
| **Audio Newsletter** | 3-5 min (~500 words) | Conversational | Medium — 150 WPM |
| **Phone/IVR Script** | 15-30 sec (~50 words) | Calm, clear | Very slow — 120 WPM |

## Step 2: Write for the Ear

**Rules for spoken-word content:**

| Written | Spoken Equivalent |
|---------|------------------|
| $1,200 | twelve hundred dollars |
| 15% | fifteen percent |
| Q2 2026 | second quarter twenty twenty-six |
| CPA | cost per acquisition |
| e.g. | for example |
| etc. | and so on |
| vs. | versus |
| Dr. Smith | Doctor Smith |
| URLs | (omit entirely — can't click audio) |

**Structure rules:**
- One idea per sentence
- Max 15 words per sentence
- Use contractions (it's, we're, that's) — sounds natural
- Front-load the important word in each sentence
- Use transition phrases: "Now...", "Here's the key thing...", "Moving on..."

## Step 3: Add Pacing Markers

Use these inline markers for TTS engines and narrators:

```
[PAUSE 0.5]  — half-second pause (comma equivalent)
[PAUSE 1.0]  — one-second pause (period/section break)
[PAUSE 2.0]  — two-second pause (major section transition)
[EMPHASIS]   — stress the next word
[SLOW]       — reduce speed for complex content
[NORMAL]     — return to normal speed
```

**Example:**
```
Good morning. [PAUSE 1.0]

Here's what matters today. [PAUSE 0.5]

You have [EMPHASIS] three meetings on your calendar.
The first is at ten AM with the engineering team. [PAUSE 0.5]
They'll want a decision on the migration timeline. [PAUSE 1.0]

Moving on to pipeline. [PAUSE 0.5]
```

## Step 4: Pronunciation Guide

For proper nouns, technical terms, or ambiguous words, include a pronunciation block:

```
## Pronunciation Guide
- Asana: ah-SAH-nah
- Supabase: SOO-pah-bayse
- Vercel: vur-SELL
- Cron: KRON (rhymes with "on")
- OAuth: oh-AUTH
- GIF: JIF (or GIF — match CEO preference)
```

## Step 5: TTS Rendering Options

**macOS built-in:**
```bash
# List available voices
say -v '?'

# Render to file
say -v "Samantha" -r 170 -o output.aiff "$(cat script.txt)"

# Convert to MP3
afconvert output.aiff output.mp3 -f mp4f -d aac
```

**ElevenLabs (highest quality):**
```bash
curl -X POST "https://api.elevenlabs.io/v1/text-to-speech/VOICE_ID" \
  -H "xi-api-key: $ELEVENLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "...", "model_id": "eleven_turbo_v2", "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}}' \
  --output output.mp3
```

**OpenAI TTS:**
```python
from openai import OpenAI
client = OpenAI()
# Voices: alloy, echo, fable, onyx, nova, shimmer
response = client.audio.speech.create(
    model="tts-1-hd",  # or tts-1 for faster/cheaper
    voice="onyx",
    speed=1.0,
    input=open("script.txt").read()
)
response.stream_to_file("output.mp3")
```

If no TTS service is configured, output the marked-up script only — it's still valuable for human narration.

## Output

Always deliver:
1. **The script** with pacing markers
2. **Pronunciation guide** (if proper nouns are present)
3. **Word count + estimated duration** at target WPM
4. **Audio file** (if TTS was used, with file path)

## Integration

- Called by `/audio-briefing` for morning brief narration
- Called by `/content-strategy` for audio content production
- Scripts saved to `~/ceo-brain/audio-scripts/` for reuse

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
- "Try `audio-briefing` — Generate audio-ready executive briefing scripts"
- "Try `voice-model` — Build your personal writing voice model"
- "Try `weekly-ceo-brief` — Synthesize your week into a CEO summary"
