---
name: ralph-loop-agent
description: Continuous autonomy and iterative evaluation loops for AI coding agents ("Ralph is a Bash loop"). Use when tasks require autonomous multi-step execution, persistent retry until verified complete, self-correcting test/build loops, or continuous background tasks.
---

# Ralph Loop Agent (Continuous Autonomy)

Implements the Ralph Wiggum technique from Vercel Labs: persistent, multi-iteration execution loops where an AI agent executes tools, evaluates output against completion criteria, and iterates with error feedback until the task is genuinely verified.

## Core Concepts

1. **Outer Verification Loop**:
   - `while (!taskCompleted)`: Run agent turn -> Execute tools -> Run verification checks -> Evaluate results.
2. **Deterministic Stop Conditions**:
   - Stop only when automated tests pass, compiler checks succeed, and deliverables exist.
   - Max iteration limit (safety breaker) with clear failure reporting.
3. **Context Management**:
   - Keep previous attempt failures and error logs in working memory to prevent repeating the same mistake.

## Workflow

1. Define unambiguous verification test (e.g. `npm test`, `pytest`, `cargo check`).
2. Execute code modifications.
3. Run verification test and capture exact error output.
4. If failures occur: inject error trace as direct feedback and re-run.
5. Once all checks pass: conclude with final verification summary.
