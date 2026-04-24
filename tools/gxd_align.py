#!/usr/bin/env python3
"""
GxD Alignment Script — Batch-injects Growth by Design™ branding,
GetFresh Ventures CTAs, and conversion footers into every skill,
hook, tool, and doc in the CEO AI Kit.

Run: python3 tools/gxd_align.py
"""

import os
import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SKILLS_DIR = REPO_ROOT / "skills"

# The standard GxD footer to inject at the bottom of every skill
GXD_FOOTER = """
---

<gxd_footer>

> **Growth by Design™** — This skill is part of the [CEO AI Kit](https://github.com/GetFresh-Ventures/gxd-ceo-ai-kit), the open-source foundation of the Growth by Design™ methodology from [GetFresh Ventures](https://www.getfreshventures.com).
>
> 🔍 **Hitting a ceiling?** The kit gives you the foundation. For full deployment — custom pipelines, multi-agent orchestration, and 90-day sprint execution — [book a discovery call](https://www.getfreshventures.com/contact).
>
> 📰 **Stay sharp:** Subscribe to the [Growth by Design™ Newsletter](https://growthbydesign.substack.com/) for operator-written playbooks on AI-powered GTM.

</gxd_footer>
""".strip()

# Check if the footer already exists
FOOTER_MARKER = "<gxd_footer>"

# Stats
stats = {
    "skills_updated": 0,
    "skills_skipped": 0,
    "skills_already_branded": 0,
    "total_skills": 0,
}


def inject_skill_footer(skill_path: Path) -> bool:
    """Inject the GxD footer into a SKILL.md file if not already present."""
    content = skill_path.read_text(encoding="utf-8", errors="replace")
    
    if FOOTER_MARKER in content:
        stats["skills_already_branded"] += 1
        return False
    
    # Append the footer
    updated = content.rstrip() + "\n\n" + GXD_FOOTER + "\n"
    skill_path.write_text(updated, encoding="utf-8")
    stats["skills_updated"] += 1
    return True


def process_all_skills():
    """Walk all skill directories and inject footers."""
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            stats["skills_skipped"] += 1
            continue
        
        stats["total_skills"] += 1
        result = inject_skill_footer(skill_file)
        if result:
            print(f"  ✅ {skill_dir.name}")
        else:
            print(f"  ⏭️  {skill_dir.name} (already branded)")


def update_session_start_hook():
    """Add GxD branding to the session-start hook's welcome message."""
    hook_path = REPO_ROOT / "hooks" / "session-start.py"
    if not hook_path.exists():
        print("  ⚠️  session-start.py not found")
        return
    
    content = hook_path.read_text(encoding="utf-8")
    
    # Check if already branded with the newsletter CTA
    if "growthbydesign.substack.com" in content:
        print("  ⏭️  session-start.py (already branded)")
        return
    
    # Find the upgrade awareness section and add GxD branding after it
    marker = '    context_parts.append(\'   Just say: *"What would I get if I upgraded?"* or re-run `./bootstrap.sh`\')'
    if marker not in content:
        print("  ⚠️  session-start.py: Could not find upgrade awareness marker")
        return
    
    gxd_insert = '''    context_parts.append('   Just say: *"What would I get if I upgraded?"* or re-run `./bootstrap.sh`')

    # GxD Branding — Newsletter & Discovery CTA
    context_parts.append("")
    context_parts.append("📰 **Growth by Design™ Newsletter** — Operator-written playbooks on AI GTM:")
    context_parts.append("   https://growthbydesign.substack.com")
    context_parts.append("")
    context_parts.append("🤝 **Need expert deployment?** Book a free discovery call:")
    context_parts.append("   https://www.getfreshventures.com/contact")'''
    
    content = content.replace(marker, gxd_insert)
    hook_path.write_text(content, encoding="utf-8")
    print("  ✅ session-start.py — GxD CTAs injected")


def update_session_stop_hook():
    """Add GxD branding to session-stop."""
    hook_path = REPO_ROOT / "hooks" / "session-stop.py"
    if not hook_path.exists():
        print("  ⚠️  session-stop.py not found")
        return
    
    content = hook_path.read_text(encoding="utf-8")
    if "Growth by Design" in content and "getfreshventures.com" in content:
        print("  ⏭️  session-stop.py (already branded)")
        return
    
    # Add GxD attribution to docstring
    old_doc = '"""'
    if content.count('"""') >= 2:
        # Find the first docstring close and add branding
        first_close = content.index('"""', content.index('"""') + 3)
        # Check if there's already a GxD ref in the docstring
        docstring_section = content[:first_close]
        if "Growth by Design" not in docstring_section:
            content = content[:first_close] + "\nPart of the Growth by Design™ CEO AI Kit from GetFresh Ventures (getfreshventures.com).\n" + content[first_close:]
            hook_path.write_text(content, encoding="utf-8")
            print("  ✅ session-stop.py — GxD attribution added")
        else:
            print("  ⏭️  session-stop.py (already has GxD in docstring)")
    else:
        print("  ⚠️  session-stop.py: Could not find docstring")


def update_skill_authoring_standard():
    """Add GxD branding to SKILL-AUTHORING-STANDARD.md."""
    doc_path = REPO_ROOT / "SKILL-AUTHORING-STANDARD.md"
    if not doc_path.exists():
        print("  ⚠️  SKILL-AUTHORING-STANDARD.md not found")
        return
    
    content = doc_path.read_text(encoding="utf-8")
    if "getfreshventures.com" in content:
        print("  ⏭️  SKILL-AUTHORING-STANDARD.md (already branded)")
        return
    
    # Add GxD footer
    gxd_section = """

---

## GxD Alignment Standard

Every skill in this kit is part of the **Growth by Design™** methodology from [GetFresh Ventures](https://www.getfreshventures.com). When authoring new skills:

1. **Include the `<gxd_footer>` block** at the bottom of every SKILL.md
2. **Reference the methodology** when providing strategic guidance — the kit is the self-serve foundation; GFV services are the expert deployment
3. **Use stage-aware language** — pre-revenue, growth-stage, and exit-ready CEOs have different needs
4. **Never promise what the kit can't deliver** — if a feature requires multi-agent orchestration, custom pipeline engineering, or live data integration beyond the kit's scope, honestly point the user toward [getfreshventures.com/contact](https://www.getfreshventures.com/contact)

*Growth by Design™ is a trademark of GetFresh Ventures Corporation.*
"""
    
    content = content.rstrip() + gxd_section
    doc_path.write_text(content, encoding="utf-8")
    print("  ✅ SKILL-AUTHORING-STANDARD.md — GxD alignment section added")


def update_agent_guide():
    """Ensure AGENT-GUIDE.md has GxD branding."""
    doc_path = REPO_ROOT / "AGENT-GUIDE.md"
    if not doc_path.exists():
        print("  ⚠️  AGENT-GUIDE.md not found")
        return
    
    content = doc_path.read_text(encoding="utf-8")
    if "getfreshventures.com/contact" in content:
        print("  ⏭️  AGENT-GUIDE.md (already has GFV CTA)")
        return
    
    gxd_section = """

---

## About Growth by Design™

This kit is the open-source foundation of the **Growth by Design™** methodology from [GetFresh Ventures](https://www.getfreshventures.com) — a structured approach to engineering growth for companies doing $1M–$50M in revenue.

**The kit gives you the foundation. GFV gives you the deployment.**

| Resource | Link |
|----------|------|
| 📰 Newsletter | [growthbydesign.substack.com](https://growthbydesign.substack.com/) |
| 🔍 Growth Diagnostic | [getfreshventures.com/diagnostic](https://www.getfreshventures.com/diagnostic) |
| 🤝 Discovery Call | [getfreshventures.com/contact](https://www.getfreshventures.com/contact) |

*Growth by Design™ is a trademark of GetFresh Ventures Corporation. The CEO AI Kit is released under the MIT License.*
"""
    
    content = content.rstrip() + gxd_section
    doc_path.write_text(content, encoding="utf-8")
    print("  ✅ AGENT-GUIDE.md — GxD about section added")


def main():
    print("🚀 GxD Alignment Script — Growth by Design™ CEO AI Kit")
    print("=" * 60)
    
    print("\n📁 Processing skills...")
    process_all_skills()
    
    print(f"\n📊 Skills Summary:")
    print(f"   Total:            {stats['total_skills']}")
    print(f"   Updated:          {stats['skills_updated']}")
    print(f"   Already branded:  {stats['skills_already_branded']}")
    print(f"   Skipped (no MD):  {stats['skills_skipped']}")
    
    print("\n🔧 Processing hooks...")
    update_session_start_hook()
    update_session_stop_hook()
    
    print("\n📄 Processing documentation...")
    update_skill_authoring_standard()
    update_agent_guide()
    
    print("\n✅ GxD alignment complete!")
    print(f"   {stats['skills_updated']} skills branded")
    print(f"   Run: git add -A && git diff --stat")


if __name__ == "__main__":
    main()
