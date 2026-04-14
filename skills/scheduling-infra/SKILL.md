---
name: scheduling-infra
description: Open-source scheduling infrastructure. Create booking pages, manage availability, and handle calendar logistics without SaaS vendor lock-in.
license: MIT
metadata:
  author: GFV Proactive Intelligence
  version: 1.0.0
  category: Day-to-Day Operations
---

# /scheduling-infra

**Usage**: Set up and manage meeting scheduling infrastructure. Create bookable event types, check availability, and automate meeting logistics.

## Capabilities

### 1. Availability Management
- Query Google Calendar or Outlook for real-time availability.
- Define scheduling windows (e.g., "Only book meetings Tue-Thu 10am-4pm").
- Buffer time between meetings (default: 15 minutes).
- Block focus time and prevent back-to-back stacking.

### 2. Event Type Templates
Pre-configured meeting types for common CEO interactions:

| Type | Duration | Buffer | Notes |
|------|----------|--------|-------|
| Discovery Call | 30 min | 15 min | Includes pre-call `meeting-prep` trigger |
| Board Meeting | 90 min | 30 min | Auto-generates `board-deck-builder` prompt |
| 1:1 with Direct Report | 25 min | 5 min | Pulls recent Linear activity for context |
| Investor Update | 45 min | 15 min | Triggers `fundraise` prep sequence |

### 3. Booking Flow
- Generate shareable booking links (via Cal.com or native calendar API).
- Auto-send confirmation with calendar invite.
- Pre-populate `meeting-prep` dossier when booking is confirmed.
- Send reminder 1 hour before with key context.

### 4. Post-Meeting Automation
- After meeting end time, prompt for `post-meeting-brief`.
- Auto-create follow-up task in Linear if action items exist.
- Route follow-up email draft through `email-composer`.

## Integration Points
- Google Calendar API (primary)
- Cal.com API (optional, for public booking pages)
- Linear MCP (for task creation)
- Email composer (for follow-ups)
