# SESSION CONTEXT — AI Working Memory

**Purpose:** This file is the AI's working memory. All agents read this first.

**Maintained by:** AI (auto-generated and updated)
**Human editable:** Yes, but AI will overwrite during sessions

---

## Project Summary

| Field | Value |
|:------|:------|
| **Project Name** | Omega Constitution Framework |
| **Project Type** | AI Governance Framework + Agentic Orchestration |
| **North Star** | Text your phone → AI agents build your project |
| **Target User** | Solo founders who want AI-first development |
| **Active Kit** | N/A (framework-level work) |
| **Current Phase** | Infrastructure — Omega Claw + Hive integration |
| **Last Updated** | 2026-02-26T17:59:00Z |

---

## Ecosystem Repos

| Repo | URL | Purpose |
|:-----|:----|:--------|
| **omega-constitution** | https://github.com/edsworld27/omega-constitution | The law — governs all agent behavior |
| **omega-claw** | https://github.com/edsworld27/omega-claw | Remote control — Telegram → Hive → Agents |
| **omega-store** | https://github.com/edsworld27/omega-store | Marketplace — kits, skills, MCPs |

---

## Key Decisions (Locked)

1. **Rule of 3** — 3 Workers → 1 Manager → 3 Managers → 1 Mega-Manager (infinite recursion)
2. **LLM-Free Omega Claw** — No API costs. Keyword matching + structured wizards.
3. **File-drop job system** — Telegram → FOUNDER_JOB.md → PICKUP_ALERT.md → Claude Code
4. **3-repo ecosystem** — Constitution (law), Claw (control), Store (marketplace)

---

## Architecture Status

| Component | Status | Notes |
|:----------|:-------|:------|
| Constitution v9 | ✅ LIVE | INSTRUCTOR.xml, SECURITY.xml, QUALITY.xml |
| omega.py wizard | ✅ LIVE | Scaffolds USER SPACE, kits, seeds |
| Daemon (6 watchers) | ✅ LIVE | auto_changelog, auto_security, auto_structure, auto_help, omega_reporter, omega_job_watcher |
| Omega Claw (bot) | ✅ BUILT | 20 files, 2 agents (Orchestrator + Reporter), SQLite, IntentAgent |
| Skills system | 🏗️ SCAFFOLDED | `skills/_template/` ready, auto-loader not yet wired |
| MCPs system | 🏗️ SCAFFOLDED | `mcps/` directory ready, loader not yet wired |
| Telegram live | ⏳ NEEDS TOKEN | Requires @BotFather token in `.env` |

---

## Session Log

| Time | Action | Result |
|:-----|:-------|:------|
| 15:00 | Constitution Bot integration (v9.6) | ConstitutionAgent built + wired |
| 15:30 | Rule of 3 hierarchy (v9.7) | MASTER_ORCHESTRATOR.md updated |
| 16:00 | Omega Bot MVP (v9.8) | 9-file bot stripped from mac-commander |
| 16:30 | Job watcher daemon | omega_job_watcher.py wired into daemon |
| 17:00 | Architecture planning | Omega Claw ecosystem designed |
| 17:30 | Omega Claw standalone (v9.9) | 20-file standalone repo built |
| 17:59 | GitHub push | https://github.com/edsworld27/omega-claw LIVE |

---

*This file is auto-maintained by the AI. Manual edits are allowed but may be overwritten.*
