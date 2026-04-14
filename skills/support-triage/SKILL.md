---
name: support-triage
description: Automatically monitor, classify, and route inbound support requests from social channels and inboxes directly to Linear/PandaDoc.
license: MIT
metadata:
  author: GFV Proactive Intelligence
  version: 1.0.0
  category: Day-to-Day Operations
---

# /support-triage

**Usage**: Utilize this skill to handle automated monitoring of mentions, tickets, or specific prospect emails without requiring physical CEO monitoring.

## Resolving Operational Blindspots

This skill maps social and inbound noise directly into the operating systems. 

## Phase 1: Ingestion Routing
- Utilize MCP servers (X, LinkedIn, Hubspot, or Email IMAP) to pull unread items marked with specific queries, mentions, or tags.
- Scan the ingestion payload specifically looking for High-Risk queries (e.g., `down`, `broken`, `urgent`), Medium-Risk (e.g., `how do I`, `billing`), and Low-Risk.

## Phase 2: Classification and Resolution
- Do not merely output a list for the CEO. 
- Map **High-Risk** issues directly into the active Linear board as an active `Issue` using the Linear MCP connection. Assign it to the relevant engineer or account manager.
- For **Medium-Risk** / **Low-Risk** queries, draft an outbound response dynamically utilizing the CRM's contextual history on the User to generate a highly specific triage response.

## Phase 3: The Dash-Brief Output
- Once extraction, mapping, and drafting are perfectly staged, provide the CEO with a single Markdown table highlighting:
  `[Urgency Level] | [User/Account] | [Issue Summary] | [Action Executed (e.g. Linear Ticket Generated)]`
- Ensure NO unvetted outbound messages are sent without explicit approval.
