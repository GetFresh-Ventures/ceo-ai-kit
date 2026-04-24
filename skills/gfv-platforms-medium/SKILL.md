---
name: medium-posts
description: When the user wants to write, publish, republish, or optimize posts on Medium.com (canonical tags, distribution, Medium SEO). Also use when the user mentions "Medium," "Medium article," "Medium story," "Medium publishing," "canonical Medium," or "publish on Medium." Not for general parasite SEO when Medium is not the target platform—use parasite-seo. For AI search visibility strategy, use generative-engine-optimization.
  Use when: The executive requests execution of this domain.
  Skip when: The task is outside the scope of this module.
metadata:
  version: 1.1.0
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


# Platforms: Medium

Guides Medium publishing for parasite SEO and content distribution. Medium's domain authority helps content rank faster than on new sites; articles can reach page 1 within days. Use this skill when planning Medium content or republishing from your site.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read Sections 6 (Keywords), 11 (Content Strategy).

Identify:
1. **Content**: Original or republish
2. **Canonical**: If republish, set canonical to original URL
3. **Goal**: Traffic, backlinks, AI citations

## Why Medium for Parasite SEO

| Benefit | Detail |
|---------|--------|
| **Fast rankings** | Page 1 within days vs months on own domain |
| **Authority** | Leverages Medium's domain authority |
| **AI-friendly** | Frequently cited in AI search results |
| **Backlinks** | Traffic-generating articles attract links |

## Canonical Links

When republishing: Set canonical to your original URL in Medium settings. Prevents duplicate content penalties; signals original source.

## Content Best Practices

- **Match intent**: Keyword-focused; solve problem or answer question
- **Quality**: Same quality as on your site
- **CTA**: Link to relevant site pages; don't over-promote

## Output Format

- **Title** (keyword-optimized)
- **Structure** (for original) or **canonical** setup (for republish)
- **Internal links** to site
- **CTA** placement

## Related Skills

- **parasite-seo**: Parasite SEO strategy; Medium as platform
- **article-page-generator**: Article structure for republish
- **link-building**: Medium as backlink source
- **grokipedia-recommendations**: GEO; AI search visibility



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
