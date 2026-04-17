---
name: sms-outreach
description: Compliant SMS/WhatsApp outreach with opt-in verification, Twilio integration, CRM logging, and TCPA safeguards.
short_description: "Compliant SMS/WhatsApp outreach campaigns"
license: MIT
metadata:
  author: GFV Proactive Intelligence
  version: 2.0.0
  category: Growth Engine
---

# /sms-outreach

**Usage**: Send compliant SMS or WhatsApp messages to warm leads with proper opt-in verification, CRM integration, and delivery tracking.

> [!WARNING]
> SMS marketing carries serious legal risk. TCPA violations are **$500-$1,500 per unsolicited message**. This skill enforces strict compliance gates.


## Quick Start
Just say any of these:
- "Set up a compliant SMS campaign"
- "Build a text follow-up sequence"
- "Design opt-in flows for SMS outreach"


## Prerequisites

### Twilio Setup (5 minutes)
1. Create account at [twilio.com](https://www.twilio.com)
2. Buy a phone number with SMS capability ($1/month)
3. Get credentials from the [Twilio Console](https://console.twilio.com):
   - **Account SID**: `ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
   - **Auth Token**: `your-auth-token`
   - **Phone Number**: `+1234567890`

```bash
# Store credentials securely
# macOS
security add-generic-password -s "TWILIO_SID" -a "ceo-kit" -w "ACxxxx..."
security add-generic-password -s "TWILIO_TOKEN" -a "ceo-kit" -w "your-auth-token"

# Or environment variables
export TWILIO_ACCOUNT_SID="ACxxxx..."
export TWILIO_AUTH_TOKEN="your-auth-token"
export TWILIO_PHONE="+1234567890"
```

### Verification
```bash
curl -s -u "$TWILIO_ACCOUNT_SID:$TWILIO_AUTH_TOKEN" \
  "https://api.twilio.com/2010-04-01/Accounts/$TWILIO_ACCOUNT_SID.json" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'✅ Account: {d[\"friendly_name\"]} | Status: {d[\"status\"]}')"
```

---

## The 3-Gate Compliance Protocol

Every SMS sent through this skill passes through 3 mandatory gates:

### Gate 1: Opt-In Verification
Before ANY message is sent, the agent MUST verify opt-in:
- **Existing customer** with prior text consent? → Check CRM for `sms_opt_in: true`
- **New lead from web form** with SMS checkbox? → Verify form submission record
- **No documented opt-in?** → ❌ **BLOCK. Do not send.**

```python
# Example opt-in check against CRM
def verify_opt_in(contact_id):
    """Check HubSpot for SMS consent."""
    # Query HubSpot contact properties
    # Look for: sms_opt_in == True AND sms_opt_in_date is set
    # BLOCK if either is missing
    pass
```

### Gate 2: Content Compliance
Every message must:
- Include business name identification
- Include opt-out instructions: "Reply STOP to unsubscribe"
- Be under 160 characters for SMS (or clearly segmented)
- Contain NO misleading claims or urgency language banned by TCPA

### Gate 3: CEO Approval
> [!CAUTION]
> **NEVER auto-send.** Every SMS requires CEO "send it" approval. Show the full message, recipient, and opt-in status before sending.

---

## Sending Messages

### Send a Single SMS
```bash
curl -s -X POST \
  "https://api.twilio.com/2010-04-01/Accounts/$TWILIO_ACCOUNT_SID/Messages.json" \
  -u "$TWILIO_ACCOUNT_SID:$TWILIO_AUTH_TOKEN" \
  -d "From=$TWILIO_PHONE" \
  -d "To=+1RECIPIENTPHONE" \
  -d "Body=Hi [Name], this is [Company]. Your appointment is confirmed for Thursday at 2pm. Reply STOP to opt out." \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'SID: {d.get(\"sid\",\"ERROR\")} | Status: {d.get(\"status\",d.get(\"message\",\"unknown\"))}')"
```

### Send via WhatsApp (if Twilio WhatsApp enabled)
```bash
curl -s -X POST \
  "https://api.twilio.com/2010-04-01/Accounts/$TWILIO_ACCOUNT_SID/Messages.json" \
  -u "$TWILIO_ACCOUNT_SID:$TWILIO_AUTH_TOKEN" \
  -d "From=whatsapp:$TWILIO_PHONE" \
  -d "To=whatsapp:+1RECIPIENTPHONE" \
  -d "Body=Your message here"
```

### Check Delivery Status
```bash
MESSAGE_SID="SMxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
curl -s -u "$TWILIO_ACCOUNT_SID:$TWILIO_AUTH_TOKEN" \
  "https://api.twilio.com/2010-04-01/Accounts/$TWILIO_ACCOUNT_SID/Messages/$MESSAGE_SID.json" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'To: {d[\"to\"]} | Status: {d[\"status\"]} | Error: {d.get(\"error_message\",\"none\")}')"
```

---

## Use Case Templates

### 1. Appointment Confirmation
```
Hi [Name], this is [Company]. Your [Service] appointment is confirmed for [Day] at [Time]. Reply Y to confirm or call us at [Phone]. Reply STOP to opt out.
```
**When**: After CRM creates a booked appointment.

### 2. Follow-Up After Service
```
Hi [Name], thank you for choosing [Company]! We'd love your feedback — could you leave us a quick review? [Review Link]. Reply STOP to opt out.
```
**When**: 24-48 hours after service completion. Check CRM for job status = completed.

### 3. Warm Lead Re-Engagement
```
Hi [Name], this is [CEO Name] from [Company]. We spoke last [timeframe] about [topic]. I have a quick update that might help — got 5 minutes this week? Reply STOP to opt out.
```
**When**: Lead in CRM hasn't responded in 14+ days. REQUIRES prior relationship + opt-in.

### 4. Event/Webinar Reminder
```
Reminder: [Event Name] starts tomorrow at [Time]. Join here: [Link]. Looking forward to seeing you! - [Company]. Reply STOP to opt out.
```
**When**: 24 hours before registered event.

---

## CRM Integration

After every message:
1. Log the SMS in the contact's CRM timeline (HubSpot engagement API)
2. Record: message text, timestamp, delivery status, direction (outbound)
3. If recipient replies STOP → immediately set `sms_opt_in: false` in CRM

```bash
# Log SMS to HubSpot (example)
curl -s -X POST "https://api.hubapi.com/crm/v3/objects/notes" \
  -H "Authorization: Bearer $HUBSPOT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "properties": {
      "hs_note_body": "SMS sent: [message text] | Status: delivered",
      "hs_timestamp": "'$(date -u +%s)000'"
    },
    "associations": [{"to": {"id": "CONTACT_ID"}, "types": [{"associationCategory": "HUBSPOT_DEFINED", "associationTypeId": 202}]}]
  }'
```

## Hard Rules

> [!CAUTION]
> - **NEVER** send cold SMS. TCPA violations carry $500-$1,500 per message penalties.
> - **NEVER** send after 9pm or before 8am in the recipient's local time zone.
> - **ALL** messages require CEO "send it" approval before dispatch.
> - **ALWAYS** include opt-out language ("Reply STOP to unsubscribe").
> - **NEVER** send to numbers on the National Do Not Call Registry without prior business relationship.

## Error Handling

| Error Code | Meaning | Resolution |
|------------|---------|-----------|
| 21211 | Invalid phone number | Verify number format (+1XXXXXXXXXX) |
| 21608 | Unverified number (trial) | Verify recipient in Twilio console or upgrade account |
| 21610 | Recipient opted out | STOP. Respect opt-out. Update CRM. |
| 30003 | Unreachable | Phone off or disconnected. Try again in 24hrs. |
| 30006 | Landline | Cannot SMS a landline. Remove from SMS list. |

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
- "Want me to set up an automated appointment confirmation flow?"
- "Should I check the CRM for leads missing opt-in status with `pipeline-pulse`?"
- "Want me to draft a review request sequence for completed jobs?"
