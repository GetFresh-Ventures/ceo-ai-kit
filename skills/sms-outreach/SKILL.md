---
name: sms-outreach
description: Send SMS and WhatsApp messages for CEO outbound communications. Multi-channel reach beyond email.
license: MIT
metadata:
  author: GFV Proactive Intelligence
  version: 1.0.0
  category: Revenue Enablement
---

# /sms-outreach

**Usage**: When email isn't getting responses, escalate to SMS or WhatsApp. For deal follow-ups, meeting confirmations, and time-sensitive communications.

## When to Use SMS vs. Email

| Scenario | Channel | Why |
|----------|---------|-----|
| Deal follow-up after 2+ unanswered emails | SMS | Higher open rate (98% vs 20%) |
| Meeting confirmation same-day | SMS | Immediate visibility |
| Sharing a doc/link with context | WhatsApp | Rich media + threading |
| Cold outreach | ❌ NEVER SMS | Compliance risk (TCPA) |

## Execution Flow

### 1. Message Drafting
- Draft the message using the CEO's voice model.
- SMS: Max 160 chars for single segment. Keep it under 2 segments.
- WhatsApp: Richer formatting allowed, but keep under 500 chars.
- Always include a clear CTA and identify yourself.

### 2. Compliance Gate
Before sending ANY SMS:
- Verify the recipient has given prior consent (check CRM contact record).
- Include opt-out language if required by jurisdiction.
- NEVER send bulk SMS without explicit compliance review.
- Log every outbound SMS in CRM for audit trail.

### 3. Delivery & Tracking
- Use Twilio API or similar verified provider for delivery.
- Track delivery status and read receipts (WhatsApp).
- Log response in CRM contact timeline.

## Hard Rules
> [!CAUTION]
> - NEVER send cold SMS. TCPA violations carry $500-$1,500 per message penalties.
> - NEVER send after 9pm or before 8am recipient's local time.
> - ALL messages require CEO "send it" approval before dispatch.
