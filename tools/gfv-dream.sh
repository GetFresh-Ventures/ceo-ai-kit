#!/usr/bin/env bash

# GFV Dream Mode: Memory Consolidation
# Inspired by openclaude's "autoDream" capability.
# This runs a background "dream" task using Claude or Gemini to review recent session logs
# and consolidate them into durable, well-organized knowledge items in Supabase/SQLite.

set -e

# Discover the Claude project log directory dynamically
# Claude Code stores logs in ~/.claude/projects/-<escaped-cwd>/
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ESCAPED_CWD=$(echo "$REPO_DIR" | sed 's|/|-|g')
MEMORY_DIR="$HOME/.claude/projects/$ESCAPED_CWD/"
# Look for gfv-brain adjacent to this repo, or fall back to ~/gfv-brain
if [ -f "$REPO_DIR/../gfv-brain/scripts/claude_memory.py" ]; then
    PYTHON_CLI="$REPO_DIR/../gfv-brain/scripts/claude_memory.py"
elif [ -f "$HOME/gfv-brain/scripts/claude_memory.py" ]; then
    PYTHON_CLI="$HOME/gfv-brain/scripts/claude_memory.py"
else
    echo "⚠️  claude_memory.py not found. Skipping memory consolidation."
    exit 0
fi

echo "☁️ Starting GFV Dream Mode (Memory Consolidation)..."

# Find the 3 most recent session logs (jsonl files)
RECENT_SESSIONS=$(find "$MEMORY_DIR" -maxdepth 1 -name "*.jsonl" -exec stat -f "%c %N" {} + | sort -rn | head -n 3 | awk '{print $2}')

if [ -z "$RECENT_SESSIONS" ]; then
    echo "No recent sessions found to dream about."
    exit 0
fi

# Build massive prompt combining recent transcripts
PROMPT="DREAM MODE ACTIVE. You are performing a 'dream' — a reflective pass over your memory files. \
Synthesize what you've learned recently into durable, well-organized memories so that future sessions can orient quickly. \
Extract core architectural decisions, client facts (HubSpot/Linear states), and new processes. \
Save them as structured facts using the appropriate tools."

# If claude is installed, run it
if command -v claude &> /dev/null; then
    echo "Running consolidation pass on recent sessions..."
    # We use a subshell to pipe the last transcripts into the prompt block
    for SESSION in $RECENT_SESSIONS; do
        if [ -f "$SESSION" ]; then
            echo "Dreaming about session: $(basename "$SESSION")"
            # Extract last 500 lines to avoid token explosion, grab "text" content heuristically
            grep -o '"text":"[^"]*"' "$SESSION" | tail -n 50 >> /tmp/dream_context.txt
        fi
    done
    if [ -s /tmp/dream_context.txt ]; then
        claude -p "$PROMPT" < /tmp/dream_context.txt
    fi
    rm -f /tmp/dream_context.txt
    echo "✨ Dream Mode complete. Memories consolidated."
else
    echo "❌ Error: Claude CLI not found. Dream Mode requires the 'claude' command line tool."
    exit 1
fi
