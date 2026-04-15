---
name: audio-briefing
description: "Generate a concise, audio-ready executive briefing script from data across your systems. Use when the user wants a morning brief, situation update, or a summary they can listen to on the go."
---

# Audio Briefing

Produce a structured, spoken-word briefing script the CEO can consume hands-free. This skill generates the *script* — actual text-to-speech rendering is handled by external TTS services (ElevenLabs, OpenAI TTS, macOS `say`, etc.).


## Quick Start
Just say any of these:
- "Create an audio briefing for my commute"
- "Turn my weekly brief into a 5-minute audio script"
- "Prepare a voice briefing covering pipeline and meetings"

## When to Use

- "Give me my morning brief"
- "What do I need to know today?"
- "Summarize everything for my commute"
- Start of day when `/chief-of-staff` detects pending items

## Step 1: Gather Intelligence

Pull from available sources (skip any that aren't connected):

```
1. Calendar  → Next 3 meetings (title, time, attendee count)
2. Linear    → P0/P1 issues updated in last 24h
3. Pipeline  → ~/gtm-brain/pipeline.md (deals with activity)
4. Email     → Unread count + any flagged/urgent
5. News      → /news-digest output if available
```

**Time budget:** Spend no more than 30 seconds per source. If a source is slow or unavailable, skip it and note the gap.

## Step 2: Write the Script

**Format rules for spoken delivery:**

| Rule | Why |
|------|-----|
| Short sentences (under 15 words) | Easier to process aurally |
| No bullet points or tables | They don't translate to speech |
| Numbers spoken naturally | "about twelve hundred" not "1,200" |
| Spell out acronyms on first use | "P-zero" not "P0", "cost per acquisition" not "CPA" |
| Use transition phrases | "Moving on...", "Next up...", "One thing to flag..." |
| Total length: 60-90 seconds | ~150-225 words at speaking pace |

**Script structure:**

```markdown
## Executive Briefing — [Day, Month Date]

Good morning. Here's what matters today.

### Schedule
You have [N] meetings today. First up is [meeting] at [time]
with [key attendee]. [One sentence on what it's about or what to prepare.]

### Pipeline
[1-2 sentences on the most important pipeline movement.
Focus on what changed, not the full state.]

### Operations
[1-2 sentences on urgent tickets, blockers, or team items.
Only mention things that need action today.]

### One Thing to Watch
[The single most important non-urgent item the CEO should be
aware of. A risk, an opportunity, or a trend.]

That's your brief. Have a good one.
```

## Step 3: Render (Optional)

If the user wants actual audio output:

**macOS (built-in, no API key):**
```bash
say -v Samantha -r 170 -o ~/ceo-brain/briefing-$(date +%Y%m%d).aiff "$(cat briefing.txt)"
```

**ElevenLabs API (if configured):**
```bash
curl -X POST "https://api.elevenlabs.io/v1/text-to-speech/VOICE_ID" \
  -H "xi-api-key: $ELEVENLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"text\": \"$(cat briefing.txt)\", \"model_id\": \"eleven_turbo_v2\"}" \
  --output ~/ceo-brain/briefing-$(date +%Y%m%d).mp3
```

**OpenAI TTS:**
```python
from openai import OpenAI
client = OpenAI()
response = client.audio.speech.create(
    model="tts-1",
    voice="onyx",
    input=open("briefing.txt").read()
)
response.stream_to_file("briefing.mp3")
```

If no TTS is configured, just output the script — it's still valuable as text.

## Output

Always produce:
1. **The script** (in the format above)
2. **Audio file path** (if TTS was used)
3. **Sources used** (which systems contributed data)
4. **Gaps** (which systems were unavailable)

## Integration

- Triggered by `/chief-of-staff` during morning sweep
- Feeds from `/news-digest` for the market section
- Feeds from `/pipeline-pulse` for deal updates
- Script saved to `~/ceo-brain/briefings/` for history

## After This Skill
💡 Suggest these next steps:
- "Want a detailed written version?" → `/weekly-ceo-brief`
- "Want me to prep for the meetings mentioned?" → `/meeting-prep`
