#!/usr/bin/env python3
import os
import sys
import json
import tempfile
import subprocess
from pathlib import Path

def get_claude_logs_dir():
    repo_dir = str(Path(__file__).parent.parent.absolute())
    escaped_cwd = repo_dir.replace("/", "-")
    return Path(os.environ.get("GFV_CEO_BRAIN", Path.home() / "ceo-brain")) / ".core" / "projects" / escaped_cwd

def main():
    repo_dir = Path(__file__).parent.parent.absolute()
    
    # Check for legacy pipeline (bypassed for agnostic kit)
    # The script now processes logs independently.

    print("☁️ Starting GFV Dream Mode (Memory Consolidation)...")

    logs_dir = get_claude_logs_dir()
    if not logs_dir.exists() or not logs_dir.is_dir():
        print("No recent sessions found to dream about.")
        sys.exit(0)

    logs = sorted(logs_dir.glob("*.jsonl"), key=os.path.getmtime, reverse=True)[:3]
    if not logs:
        print("No recent sessions found to dream about.")
        sys.exit(0)

    prompt = (
        "DREAM MODE ACTIVE. You are performing a 'dream' — a reflective pass over your memory files. "
        "Synthesize what you've learned recently into durable, well-organized memories so that future sessions can orient quickly. "
        "Extract core architectural decisions, client facts (HubSpot/Linear states), and new processes. "
        "Save them as structured facts using the appropriate tools."
    )

    try:
        subprocess.run(["claude", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except FileNotFoundError:
        print("❌ Error: Claude CLI not found. Dream Mode requires the 'claude' command line tool.")
        sys.exit(1)

    print("Running consolidation pass on recent sessions...")
    extracted_text = []

    for logfile in logs:
        print(f"Dreaming about session: {logfile.name}")
        session_text = []
        try:
            with open(logfile, "r", encoding="utf-8") as f:
                for line in f:
                    if not line.strip(): continue
                    try:
                        record = json.loads(line)
                        msg = record.get("message", {})
                        content = msg.get("content", [])
                        if isinstance(content, list):
                            for item in content:
                                if item.get("type") == "text" and "text" in item:
                                    session_text.append(item["text"])
                    except Exception:
                        pass
            # tail n 50
            extracted_text.extend(session_text[-50:])
        except Exception:
            pass

    if extracted_text:
        with tempfile.NamedTemporaryFile(mode="w+", encoding="utf-8", delete=False) as tmp:
            tmp.write("\n".join(extracted_text))
            tmp_path = tmp.name

        try:
            with open(tmp_path, "r") as tmp_in:
                subprocess.run(["claude", "-p", prompt], stdin=tmp_in)
            print("✨ Dream Mode complete. Memories consolidated.")
        except Exception as e:
            print(f"Error running claude execution: {e}")
        finally:
            os.remove(tmp_path)
    else:
        print("No text found heavily in transcripts.")

if __name__ == "__main__":
    main()
