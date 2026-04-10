#!/usr/bin/env python3
# ccflare-lite.py
# A local CLI dashboard to track Claude token usage and cost burn rate.
# Reads the local ~/.claude/projects/ directory to aggregate jsonl session logs.
import os
import json
import glob
from collections import defaultdict
from datetime import datetime

# Pricing (Claude 3.5 Sonnet / Haiku as of late 2024 / 2026 expected)
# Assume average of Sonnet for estimation if model is undefined
COST_PER_1M_INPUT = 3.00
COST_PER_1M_OUTPUT = 15.00
COST_PER_1M_CACHE_CREATE = 3.75
COST_PER_1M_CACHE_READ = 0.30

def parse_logs():
    home = os.path.expanduser("~")
    # In some setups, project logs are stored in ~/.claude/projects/*/*.jsonl
    log_files = glob.glob(f"{home}/.claude/projects/*/*.jsonl")
    
    if not log_files:
        # Fallback to local .claude if running globally
        local_dir = os.path.join(os.getcwd(), '.system_generated/logs')
        log_files = glob.glob(f"{local_dir}/*.jsonl")

    # If we are in Antigravity or standard Claude code, try catching standard json or jsonl
    antigravity_logs = glob.glob(f"{home}/.gemini/antigravity/brain/*/.system_generated/logs/*.json")
    
    all_files = log_files + antigravity_logs

    if not all_files:
        print("📭 No Claude session logs found to analyze.")
        return

    total_input = 0
    total_output = 0
    total_cache_create = 0
    total_cache_read = 0
    sessions = 0
    
    print(f"📊 Analyzing {len(all_files)} session logs...\n")
    
    for file in all_files:
        sessions += 1
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    data = json.loads(line.strip())
                    # Anthropic/Claude Code style telemetry format
                    message = data.get("message", {})
                    usage = message.get("usage", {})
                    if not usage:
                        usage = data.get("usage", {})
                    total_input += usage.get("input_tokens", 0)
                    total_output += usage.get("output_tokens", 0)
                    total_cache_create += usage.get("cache_creation_input_tokens", 0)
                    total_cache_read += usage.get("cache_read_input_tokens", 0)
                except json.JSONDecodeError:
                    continue

    calc_dashboard(sessions, total_input, total_output, total_cache_create, total_cache_read)

def calc_dashboard(sessions, total_input, total_output, total_cache_create, total_cache_read):
    input_cost = (total_input / 1_000_000) * COST_PER_1M_INPUT
    output_cost = (total_output / 1_000_000) * COST_PER_1M_OUTPUT
    cache_create_cost = (total_cache_create / 1_000_000) * COST_PER_1M_CACHE_CREATE
    cache_read_cost = (total_cache_read / 1_000_000) * COST_PER_1M_CACHE_READ
    total_cost = input_cost + output_cost + cache_create_cost + cache_read_cost

    print("========================================")
    print("🔥 GFV Executive Token Burn Dashboard 🔥")
    print("========================================\n")
    print(f"Total Sessions Analyzed:  {sessions}")
    print(f"Total Input Tokens:       {total_input:,}")
    print(f"Total Output Tokens:      {total_output:,}")
    print(f"Total Cache Create:       {total_cache_create:,}")
    print(f"Total Cache Read:         {total_cache_read:,}")
    print("-" * 40)
    print(f"Estimated Input Cost:     ${input_cost:.2f}")
    print(f"Estimated Output Cost:    ${output_cost:.2f}")
    print(f"Estimated Caching Cost:   ${(cache_create_cost + cache_read_cost):.2f}")
    print(f"Estimated Total Spend:    ${total_cost:.2f}")
    print("========================================")
    if total_cost > 50:
         print("⚠️ WARNING: High burn rate detected. Consider agentRouting to lighter models for exploration tasks.")

if __name__ == "__main__":
    parse_logs()
