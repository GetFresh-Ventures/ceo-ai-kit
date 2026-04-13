---
name: agent-orchestrator
description: Coordinate multi-agent pipeline tasks using DAG and Debate orchestration modes.
---

# Agent Orchestrator

The Agent Orchestrator allows you to execute operations across multiple agent personas simultaneously and merge their intelligence outputs, instead of executing requests chronologically yourself. It is powered by the `hooks/task_manager.py` bridge.

## Core Capabilities

1. **Linear Hand-off**: Sequential execution of steps ensuring previous steps provide inputs to the next.
2. **DAG (Directed Acyclic Graph)**: Parallelizing decoupled workflows, ensuring blocked actions pause whilst non-blocked actions proceed.
3. **Debate Mode**: Defining multiple personas with unique rulesets (e.g., CFO vs VP Sales), having them cross-examine findings, and synthesizing the final resolution.

## 1. Debate Workflow Execution

If the CEO requests you to execute a multi-perspective analysis or "debate" on a topic (e.g., forecasting, deal rescue, risk assessment), follow these mechanics:

1. **Initialize the Debate**:
   Execute `python3 hooks/task_manager.py init [topic-slug] --mode debate -g "[Objective]"`
2. **Spin Up Debaters**:
   Add specific executive personas related to the topic.
   ```bash
   python3 hooks/task_manager.py add-debater [topic-slug] cfo-agent --role "Chief Financial Officer focused on cost reduction and risk"
   python3 hooks/task_manager.py add-debater [topic-slug] cro-agent --role "Chief Revenue Officer focused on speed to close and top-line growth"
   ```
3. **Begin the Round**:
   `python3 hooks/task_manager.py round [topic-slug] start`
4. **Generate & Collect Positions**:
   Act as each persona separately, taking into account their role, and input their findings:
   `python3 hooks/task_manager.py round [topic-slug] collect cfo-agent "My analysis highlights..."`
5. **Cross-Review and Synthesize**:
   `python3 hooks/task_manager.py round [topic-slug] cross-review`
   Collect the reviews, then synthesize the final recommendation:
   `python3 hooks/task_manager.py round [topic-slug] synthesize`

## 2. DAG Parallel Tasks

If you have to retrieve multiple APIs or read different files to build an analysis, structure them in a DAG.
1. `python3 hooks/task_manager.py init [project-slug] -m dag -g "[Objective]"`
2. Add tasks:
   `python3 hooks/task_manager.py add [project-slug] fetch-hs -a hubspot-agent --desc "Fetch CRM deals"`
   `python3 hooks/task_manager.py add [project-slug] fetch-qb -a quickbooks-agent --desc "Fetch accounting metrics"`
   `python3 hooks/task_manager.py add [project-slug] synthesize -a synthesis-agent -d "fetch-hs,fetch-qb" --desc "Merge CRM and Financial Data"`
3. Determine Ready tasks with `python3 hooks/task_manager.py ready [project-slug]`

**Constraint:** The state is persisted locally. Use this for highly complex executive analysis where a single LLM stream-of-consciousness is prone to bias.
