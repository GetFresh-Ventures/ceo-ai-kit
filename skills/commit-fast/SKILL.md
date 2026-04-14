---
name: commit-fast
description: Automates git commit process by reviewing staged files, generating structured semantic commits, and executing without manual copy-pasting.
---

# Commit Fast Skill

When the user runs `/commit-fast`, your job is to analyze the current Git diff, generate a clean, semantic commit message, and execute the commit. 

## Execution Sequence

1. **Check Git Status:**
   Run `git status` to see what is staged vs unstaged.
   - If nothing is staged, offer to stage all modified tracked files or ask the user which to stage.

2. **Generate Commit Message:**
   Use the `git diff --cached` command to see what is about to be committed.
   Generate a commit message conforming to Conventional Commits:
   `<type>[optional scope]: <description>`
   
   Types:
   - `feat:` A new feature
   - `fix:` A bug fix
   - `docs:` Documentation only changes
   - `style:` Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
   - `refactor:` A code change that neither fixes a bug nor adds a feature
   - `perf:` A code change that improves performance
   - `test:` Adding missing tests or correcting existing tests
   - `chore:` Changes to the build process or auxiliary tools and libraries such as documentation generation

3. **Execute:**
   Propose the command `git commit -m "your message here"`. Once approved (or if Dippy/auto-approve is configured), execute the commit.

**WARNING:** Always generate a concise message (under 50 chars for the subject line). Do not add a body unless there are significant breaking changes.
