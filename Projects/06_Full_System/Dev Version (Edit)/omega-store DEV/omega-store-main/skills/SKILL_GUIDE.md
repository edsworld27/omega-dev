# SKILLS — AGENT CAPABILITY EXTENSIONS
**Version:** 4.0

**Purpose:** Drop-in instruction files that teach the agent specific capabilities. Skills are additive — they extend what the agent can do but NEVER override the Constitution.

---

## How Skills Work

1. Create a `.md` file in this folder (e.g., `email-drafting.md`)
2. Reference it in `CONTEXT.md` under "Active Seed Files" or in `AGENTS.md` under agent software access
3. The agent reads it during CP-0 and activates it

## Skill File Structure

Every skill file should contain:
- **Purpose** — What capability this skill provides
- **Instructions** — Step-by-step how the agent should use it
- **Examples** — Input/output pairs showing quality expectations
- **Constraints** — Guardrails specific to this skill
- **Quality Criteria** — How to judge if the skill was applied correctly

## Hierarchy

Skills sit below every Constitution file in the precedence chain:
```
SECURITY.xml > OMEGA_CONSTITUTION > BUILD_PROMPT_TEMPLATE > OMEGA_PROMPTER >
BEST_PRACTICES > AUDIT_PROTOCOL > ERROR_TAXONOMY > MULTI_SESSION_PROTOCOL >
SOURCES > DEPENDENCY_POLICY > Kits > Skills
```

If a skill says "install package X" but it's not in `deps.md`, the Install Gate wins.
If a skill says "skip testing" — the Constitution wins. Always.

## Sub-Agent Skills

For agentic projects, skills can be scoped to specific agents:
- Name the file `agent-[X]-[skill-name].md`
- Reference it in that agent's definition in `AGENTS.md`
- The skill only activates for that agent

## Available Skills

| Skill | File | Purpose |
| :--- | :--- | :--- |
| Classifier | `classifier-agent.md` | Categorise, tag, route, or filter data |
| Writer | `writer-agent.md` | Generate structured content |
| Analyst | `analyst-agent.md` | Data analysis and insights |
| Guardian | `guardian-agent.md` | Relationship preservation and compliance |
| Orchestrator | `orchestrator-agent.md` | Multi-agent coordination |
| Claude Code | `claude-agent.md` | Bootstraps Anthropic's CLI to obey Omega System rulings |
| Archivist | `archivist-agent.md` | The AGI hippocampus. Extracts local memory and new workflows, pushing them entirely to private repos/local context to protect the immutable Constitution. |
