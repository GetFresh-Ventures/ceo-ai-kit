---
name: voice-synth
description: AI voice synthesis for content production. Generate realistic speech, clone CEO voice (with consent), and produce audio content.
license: MIT
metadata:
  author: GFV Proactive Intelligence
  version: 1.0.0
  category: Growth Engine
---

# /voice-synth

**Usage**: Convert text content into high-quality audio. Produce podcast intros, video voiceovers, audio newsletters, and voice messages at scale.

## Use Cases

### 1. Content Narration
- Convert blog posts into audio articles (podcast-style).
- Generate voiceovers for `ugc-video` productions.
- Create audio versions of `weekly-ceo-brief` outputs.

### 2. CEO Voice Cloning (Opt-In)
- With explicit CEO consent, clone their voice for consistent brand audio.
- Requires a 3-5 minute voice sample for initial training.
- All cloned audio must be labeled as "AI-generated" in distribution.

### 3. Multilingual Content
- Generate same content in multiple languages via voice synthesis.
- Useful for international outreach and global team communications.

## Implementation
- Primary API: ElevenLabs (highest quality).
- Fallback: OpenAI TTS, Google Cloud TTS.
- Output formats: MP3, WAV, OGG.

## Hard Constraints
> [!CAUTION]
> - Voice cloning ONLY with explicit written CEO consent on file.
> - ALL synthesized audio must include AI disclosure metadata.
> - NEVER impersonate another person's voice without their consent.
> - Audio files are not stored beyond the active session unless CEO explicitly requests archiving.
