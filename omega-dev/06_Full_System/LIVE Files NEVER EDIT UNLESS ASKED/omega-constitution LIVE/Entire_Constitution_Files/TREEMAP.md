# 🗺️ TREEMAP — Omega Ecosystem

> **AI agents: Read this file first to understand where everything lives.**
> Updated: 2026-02-26 | Version: 9.9.6

---

## Ecosystem Overview

```
OMEGA ECOSYSTEM
├── omega-constitution    → Governance framework (this repo)
├── omega-claw            → Telegram bot (separate repo)
└── omega-store           → Kits, skills, MCPs (submodule in STORE/)
```

| Repo | GitHub | Purpose |
|------|--------|---------|
| omega-constitution | https://github.com/edsworld27/omega-constitution | The rules. Governs how AI builds things. |
| omega-claw | https://github.com/edsworld27/omega-claw | The hand. Remote Telegram control of the Hive. |
| omega-store | https://github.com/edsworld27/omega-store | The shop. Kits, skills, MCPs to plug in. |

---

## 🏛️ omega-constitution (This Repo)

```
Constution V10/
├── omega.py                    ← ENTRY POINT: Run this to set up a project
├── GO.md                       ← Quick-start prompt (paste into AI)
├── README.md                   ← What this is
├── CHANGELOG.md                ← Version history
│
├── START HERE/                 ← Onboarding for new users
│   ├── START_HERE.md           ← Full training manual
│   ├── RUN.md                  ← How to run omega.py
│   └── OMEGA_LITE.md           ← Lightweight quickstart
│
├── CONSTITUTION/               ← THE RULES (AI reads these)
│   ├── INSTRUCTOR.xml          ← Step-by-step agent behaviour (35KB)
│   ├── FRAMEWORK.xml           ← Core architecture rules
│   ├── SECURITY.xml            ← Security constitution (103KB)
│   ├── PRACTICES.xml           ← Dev practices and standards
│   ├── PROMPTING.xml           ← Prompt engineering rules
│   ├── QUALITY.xml             ← Quality gates and checks
│   ├── SOURCES.xml             ← How to handle external deps
│   ├── STRUCTURE.xml           ← File/folder conventions
│   ├── ONBOARDING.md           ← Agent onboarding flow
│   ├── 00.help.md              ← Help reference
│   │
│   ├── ── Mode Files ──
│   ├── FRESH_BUILD.md          ← New project from scratch
│   ├── IMPORT_PROJECT.md       ← Bring existing project in
│   ├── RESUME_SESSION.md       ← Continue previous work
│   ├── JUST_BUILD.md           ← Skip questions, max autonomy
│   ├── FRONTEND_ONLY.md        ← Frontend-focused build
│   ├── BACKEND_ONLY.md         ← Backend-focused build
│   ├── AUDIT_ONLY.md           ← Security/quality audit only
│   │
│   ├── blueprints/             ← Document templates
│   │   ├── PRD.md              ← Product requirements
│   │   ├── TEST_PLAN.md        ← Test planning
│   │   ├── HANDOFF.md          ← Handoff checklist
│   │   ├── ROLLBACK.md         ← Rollback procedure
│   │   ├── SOP.md              ← Standard operating procedure
│   │   ├── COST_ESTIMATE.md    ← Cost breakdown
│   │   ├── MVP_SCORECARD.md    ← MVP evaluation
│   │   ├── POST_MORTEM.md      ← Incident review
│   │   ├── AGENT_MD.md         ← Agent documentation
│   │   └── AGENT_WORKFLOW.md   ← Multi-agent workflow
│   │
│   ├── python/                 ← Automation scripts
│   │   ├── omega_daemon.py     ← Background daemon (runs security + structure)
│   │   ├── omega_job_watcher.py← Watches telegram_inbox for new jobs
│   │   ├── omega_compiler.py   ← Compiles Constitution docs
│   │   ├── omega_reporter.py   ← Generates compliance reports
│   │   ├── auto_security.py    ← Auto security scanning
│   │   ├── auto_structure.py   ← Auto structure validation
│   │   ├── auto_changelog.py   ← Auto changelog updates
│   │   └── auto_help.py        ← Auto help generation
│   │
│   ├── scenarios/              ← Standard operating procedures
│   │   ├── README.md           ← Scenario index
│   │   └── git-push-all-repos.md ← Multi-repo push procedure
│   │
│   └── tests/
│       └── COMPLIANCE_TESTS.md ← Compliance test cases
│
├── USER SPACE/                 ← YOUR PROJECT (AI writes here)
│   ├── README.md
│   ├── dev-work/               ← Active development
│   │   ├── SESSION_CONTEXT.md  ← Current session state
│   │   ├── TRACKER.md          ← Task tracking
│   │   ├── PICKUP_ALERT.md     ← Job watcher drops alerts here
│   │   ├── seed/               ← Project requirements (AI fills these)
│   │   │   ├── PROJECT.md      ← Core project definition
│   │   │   ├── BRAND.md        ← Brand guidelines
│   │   │   ├── USERS.md        ← User personas
│   │   │   ├── GOALS.md        ← Success metrics
│   │   │   ├── TECH_STACK.md   ← Technology decisions
│   │   │   ├── CONTENT.md      ← Content inventory
│   │   │   ├── MARKET.md       ← Market research
│   │   │   ├── LIMITS.md       ← Constraints
│   │   │   ├── KNOWLEDGE.md    ← Domain knowledge
│   │   │   └── AGENTS.md       ← Agent definitions
│   │   ├── hive/               ← Multi-agent workspace
│   │   │   ├── MASTER_ORCHESTRATOR.md   ← Rule of 3 hierarchy
│   │   │   ├── AGENT_SEED.md            ← Agent onboarding seed
│   │   │   └── telegram_inbox/          ← Omega Claw drops jobs here
│   │   ├── plug-and-play/      ← Drop existing files here
│   │   ├── phases/             ← Phase-based work tracking
│   │   └── docs/               ← Generated documentation
│   ├── project/                ← Clean deliverable output
│   │   ├── src/
│   │   ├── public/
│   │   └── tests/
│   └── logging/
│       └── compliance_report.md ← Auto-generated security report
│
├── STORE/                      ← Link to omega-store
│   └── README.md               ← Points to omega-store repo
│
└── DEV/                        ← Dev tooling & documentation
    ├── README.md
    ├── LINKS.md                ← All repo URLs + versions
    ├── CHANGES_DEV.md          ← Development changelog
    ├── CONTEXT_DEV.md          ← Dev context for agents
    ├── IMPLEMENTATION_DEV.md   ← Implementation notes
    ├── evaluation.md           ← Session evaluation
    └── ideation/               ← Research & prototyping
        ├── CONSTITUTION_BOT.md ← Bot design doc
        └── resource/           ← Gitignored prototypes
```

---

## 🦀 omega-claw (Separate Repo)

```
omega-claw/
├── main.py                     ← ENTRY POINT: python main.py
├── README.md
├── requirements.txt            ← python-telegram-bot + dotenv
├── .env.example                ← Config template (on GitHub)
├── .env                        ← Real keys (gitignored)
├── .gitignore
│
├── agents/                     ← Agent layer
│   ├── __init__.py             ← AgentRegistry + SkillAgent wrapper
│   ├── base_agent.py           ← BaseAgent ABC with capability matrix
│   ├── orchestrator_agent/
│   │   └── __init__.py         ← 4-step onboarding wizard + FOUNDER_JOB
│   └── reporter_agent/
│       └── __init__.py         ← Hive status + job history reporter
│
├── core/                       ← Core engine
│   ├── __init__.py
│   ├── telegram_bot.py         ← Telegram interface (auth + polling)
│   ├── orchestrator.py         ← Message router (intent → agent)
│   ├── intent_agent.py         ← Keyword classifier (no LLM)
│   ├── skill_loader.py         ← Auto-loads skills/ on boot
│   └── logging_setup.py        ← Redacted logging
│
├── db/                         ← Data layer
│   ├── __init__.py
│   └── database.py             ← SQLite (jobs + command_log)
│
├── skills/                     ← Plug-and-play skills (drop folder here)
│   ├── README.md
│   └── _template/              ← Copy this to create a skill
│       ├── skill.json
│       └── handler.py
│
└── mcps/                       ← MCP connections (future)
    └── README.md
```

---

## 🏪 omega-store (Submodule / Separate Repo)

```
omega-store/
├── STORE_GUIDE.md              ← How the store works
├── kits/                       ← Project templates
│   ├── KIT_GUIDE.md
│   ├── KIT_CREATION_GUIDE.md
│   ├── KIT_EXPORT_GUIDE.md
│   ├── _template/              ← Kit template
│   └── website/                ← Website kit (preproduction, production, testing)
├── skills/                     ← Agent skill definitions
│   ├── SKILL_GUIDE.md
│   ├── orchestrator-agent.md
│   ├── analyst-agent.md
│   ├── classifier-agent.md
│   ├── guardian-agent.md
│   └── writer-agent.md
├── mcps/                       ← MCP connection configs
│   └── MCP_CONFIG.md
├── ai-assistants/              ← AI assistant definitions
│   └── AI_ASSISTANTS.md
└── examples/                   ← Reference implementations
    └── example-taskflow/
```

---

## How It All Connects

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ You (Phone)  │────→│  Omega Claw  │────→│ telegram_    │
│ via Telegram │     │  (Bot)       │     │ inbox/       │
└──────────────┘     └──────────────┘     └──────┬───────┘
                                                 │
                          ┌──────────────────────┘
                          ▼
┌──────────────────────────────────────────────────────────┐
│                  OMEGA CONSTITUTION                       │
│                                                          │
│  INSTRUCTOR.xml governs → Agent reads PICKUP_ALERT.md    │
│  → Agent reads FOUNDER_JOB → Spawns Hive (Rule of 3)    │
│  → Builds project in USER SPACE/project/                 │
│                                                          │
│  omega-store provides: kits, skills, MCPs                │
└──────────────────────────────────────────────────────────┘
```

---

*This file is the single source of truth for project structure. Update it when adding new files or directories.*
