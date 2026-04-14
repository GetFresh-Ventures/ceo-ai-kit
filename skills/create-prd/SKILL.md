---
name: create-prd
description: Converts a rough idea, meeting transcript, or shorthand notes into a highly structured 6-part Product Requirements Document (PRD).
---

# Create PRD Skill

When the user runs this skill by typing `/create-prd`, ask them for their unstructured notes or idea if they haven't provided it. Then, transform the input into a highly structured Product Requirements Document (PRD) ready for export to Linear or Notion.

## Rules for PRD Generation
1. **Be Concise.** CEOs hate fluff. Use bullet points and stark, declarative language.
2. **Focus on Outcomes.** What business metric does this move?
3. **Assume Nothing.** Highlight areas where the user's initial notes lack clarity or technical feasibility.

## PRD Structure

Always generate the exact structure below:

### 1. Problem Statement
(1-2 sentences on what is broken or missing and why it hurts the business.)

### 2. Target Audience
(Who is this for? e.g. "Internal Sales Reps", "B2B Marketing Managers".)

### 3. Business Objectives & Metrics
- Primary Metric (e.g. increase lead conversion rate by 15%)
- Secondary Metric 

### 4. Core User Journeys
List the exact step-by-step path the user takes to achieve the goal using this feature.
- Step 1: User does X
- Step 2: System does Y

### 5. Technical Constraints & Out-of-Scope
- List what WE ARE NOT doing in this version (MVP constraints).
- Mention any known integration hurdles (e.g. "Requires HubSpot API key rotation").

### 6. Suggested Linear Epics/Issues
Break the PRD down into actionable tickets (Front-End, Back-End, Design).
