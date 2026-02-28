---
name: omega-constitution
description: Load and reference Omega Constitution protocols and rules
user-invocable: true
allowed-tools: Read, Glob, Grep
---

# Omega Constitution Reference

You are loading the Omega Constitution - the "Brain" of the system.

## Constitution Location

```
Omega System DEV MODE/omega-dev/06_Full_System/Dev Version (Edit)/omega-constitution DEV/Entire_Constitution_Files/omega-constitution-main/
```

## Core Protocol Files

| File | Purpose | Priority |
|------|---------|----------|
| SECURITY.xml | Security rules (103KB) | HIGHEST |
| PROMPTING.xml | Prompting standards (62KB) | HIGH |
| INSTRUCTOR.xml | Teaching protocols (44KB) | HIGH |
| PRACTICES.xml | Best practices (22KB) | MEDIUM |
| FRAMEWORK.xml | Framework rules (16KB) | MEDIUM |
| QUALITY.xml | Quality standards (14KB) | MEDIUM |
| SOURCES.xml | Valid sources + Claude Cookbooks | MEDIUM |
| GITHUB_PUBLISHING.xml | Publishing protocol | MEDIUM |
| AI_PROTOCOL.xml | AI behavior rules | MEDIUM |
| STRUCTURE.xml | Structure conventions | LOW |

## Sub-Protocols (CONSTITUTION folder)

- CONTEXT_PROTOCOL.xml
- EVALUATION_PROTOCOL.xml
- FRACTAL_PROTOCOL.xml
- GLOBAL_STANDARDS.xml

## Blueprints

Templates in `blueprints/`:
- PRD.md, SOP.md, TEST_PLAN.md
- AGENT_MD.md, AGENT_WORKFLOW.md
- HANDOFF.md, ROLLBACK.md
- GITHUB_SETUP.task.md

## Usage

If user asks about a specific topic, read the relevant XML:
```
Read: [path]/SECURITY.xml
Read: [path]/SOURCES.xml
```

Then explain the rules in plain language.

## Arguments

User may specify what they want to know: $ARGUMENTS

Examples:
- `/omega-constitution security` → Read SECURITY.xml
- `/omega-constitution sources` → Read SOURCES.xml
- `/omega-constitution publishing` → Read GITHUB_PUBLISHING.xml
