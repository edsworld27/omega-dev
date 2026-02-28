# OMEGA SYSTEM - COMPLETE SYSTEM MAP

> **Generated:** 2026-02-28
> **Total Files:** 2,065
> **Total Size:** ~13MB
> **Architecture:** Decoupled 5-Repository Ecosystem

---

## TABLE OF CONTENTS

1. [System Overview](#system-overview)
2. [Architecture Diagram](#architecture-diagram)
3. [Complete System Tree](#complete-system-tree)
4. [Omega Constitution (The Brain)](#omega-constitution-the-brain)
5. [Omega Claw (The Dispatch)](#omega-claw-the-dispatch)
6. [Omega Store (The Marketplace)](#omega-store-the-marketplace)
7. [Omega System Public (Execution Shell)](#omega-system-public-execution-shell)
8. [Documentation Structure](#documentation-structure)
9. [File Statistics](#file-statistics)

---

## SYSTEM OVERVIEW

The Omega System is a decoupled AI-powered development ecosystem consisting of four main repositories:

| Repository | Codename | Purpose |
|------------|----------|---------|
| **omega-constitution** | The Brain | Protocols, standards, and AI behavior rules |
| **omega-claw** | The Dispatch | Orchestration, automation, and agent management |
| **omega-store** | The Marketplace | SaaS kits, skills, and reusable components |
| **omega-system** | Execution Shell | User-facing entry points and execution layer |

---

## ARCHITECTURE DIAGRAM

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            OMEGA ECOSYSTEM                                  │
│                     "AI-Powered Development Framework"                      │
└─────────────────────────────────────────────────────────────────────────────┘
                                     │
         ┌───────────────────────────┼───────────────────────────┐
         │                           │                           │
         ▼                           ▼                           ▼
┌─────────────────────┐   ┌─────────────────────┐   ┌─────────────────────┐
│  omega-constitution │   │    Omega System     │   │     omega-store     │
│    "THE BRAIN"      │   │  "EXECUTION SHELL"  │   │  "THE MARKETPLACE"  │
│                     │   │                     │   │                     │
│  • Protocols (XML)  │──▶│  • User Space       │◀──│  • SaaS Kits        │
│  • Standards        │   │  • Entry Points     │   │  • Skills Library   │
│  • AI Rules         │   │  • Dev Work         │   │  • Templates        │
│  • Blueprints       │   │  • Hive System      │   │  • Examples         │
└─────────────────────┘   └─────────────────────┘   └─────────────────────┘
         │                           │                           │
         └───────────────────────────┼───────────────────────────┘
                                     │
                                     ▼
                       ┌─────────────────────────┐
                       │      omega-claw         │
                       │    "THE DISPATCH"       │
                       │                         │
                       │  • Orchestrator Agent   │
                       │  • Phantom Agent        │
                       │  • Terminal Agent       │
                       │  • Reporter Agent       │
                       │  • Autonomous Runner    │
                       └─────────────────────────┘
```

---

## COMPLETE SYSTEM TREE

```
/Volumes/Internal/Projects/Omega System/
│
├── Omega System DEV MODE/                              # PRIMARY WORKSPACE
│   │
│   ├── .git/                                           # Git repository
│   ├── .cursorrules
│   ├── .gitignore
│   ├── META_DEV_MODE.xml
│   ├── README.md
│   ├── TREEMAP.md
│   ├── MASTER_PRD.md
│   ├── LINKS.md
│   ├── READ ME.md
│   ├── omega-publish.py                                # God-Mode multi-repo syncer
│   │
│   ├── 00_Changelog/                                   # VERSION HISTORIES
│   │   ├── v16.15-v16.22_Omni_Maestro_Evolution.md
│   │   ├── v16.23-v16.25_Omni_Router_Evolution.md
│   │   ├── v16.26_Standalone_Architecture.md
│   │   ├── v16.27_Maintenance_Phase.md
│   │   ├── v16.28_Demo_Mode.md
│   │   ├── v16.30_Nested_Kit_Architecture.md
│   │   ├── v16.31_Kit_Creation_Architecture.md
│   │   └── v16.33_System_Router_Links.md
│   │
│   ├── 02_Evaluations/                                 # AUDITS & SWOTs
│   │   ├── EVALUATION_INDEX.md
│   │   ├── SYSTEM_WIDE_EVALUATION_V16.29.md
│   │   ├── WEBSITE_KIT_EVALUATION_V16.28.md
│   │   ├── v1_shards/
│   │   │   ├── v9.9.0_McKinsey_V9_Audit.md
│   │   │   ├── v9.9.12_V10_Ecosystem_Evaluation.md
│   │   │   └── v9.9.5_SECURITY_Audit.md
│   │   ├── v2_shards/
│   │   │   ├── v13.0_Full_Ecosystem_Evaluation.md
│   │   │   ├── v14.4_Full_Ecosystem_Evaluation.md
│   │   │   └── v15.0_Comprehensive_Evaluation.md
│   │   ├── v3_shards/
│   │   │   ├── v15.0_Public_Release_Audit.md
│   │   │   ├── v15.1_McKinsey_SWOT_Decoupling_Audit.md
│   │   │   └── v16.0_Horizon_and_Stability_Evaluation.md
│   │   └── v4_active/
│   │       └── evaluation.md
│   │
│   ├── 03_Context/                                     # SESSION CONTINUITY
│   │   ├── CONTEXT_DEV.md
│   │   ├── CONTEXT_MAP.md
│   │   └── modules/v1_changes/
│   │       └── CONTEXT_DEV.md
│   │
│   ├── 04_Implementations/                             # TACTICAL ROADMAPS
│   │   ├── TREE_MAP.md
│   │   ├── v1_shards/
│   │   │   ├── v14.1_Omega_Claw_MVP.md
│   │   │   └── v16.0_Deep_CLI_Integration.md
│   │   ├── Phases/
│   │   │   ├── TREE_MAP.md
│   │   │   ├── v1_shards/
│   │   │   │   ├── TREE_MAP.md
│   │   │   │   ├── v14.0_Orchestration_and_Install_Plan.md
│   │   │   │   ├── v15.1_God_Mode_Architecture_Implementation.md
│   │   │   │   └── v9.9.12_V10_Security_and_Structure_Plan.md
│   │   │   └── v2_active/
│   │   │       └── IMPLEMENTATION_DEV.md
│   │   └── Testing_Archive/
│   │       └── v14.0_Feature_Test_Report.md
│   │
│   ├── 05_Ideation/                                    # BRAINSTORMS & VISION
│   │   ├── TREE_MAP.md
│   │   ├── v1_active/
│   │   │   └── CONSTITUTION_BOT.md
│   │   └── Changelog_Archive/
│   │       ├── TREE_MAP.md
│   │       ├── v1_shards/
│   │       │   ├── v14.1_Omega_Claw_MVP_Ready.md
│   │       │   ├── v14.2_Hive_Backend_Complete.md
│   │       │   └── v9.9.12_V10_Final_Restructure.md
│   │       ├── v2_shards/
│   │       │   ├── v14.3_Autonomous_Mode.md
│   │       │   ├── v14.4_Multi_Agent_Locks.md
│   │       │   └── v14.5_Quality_and_DX_Refinements.md
│   │       └── v3_active/
│   │           └── CHANGES_DEV.md
│   │
│   ├── 99 Back Up/                                     # FULL BACKUP
│   │   └── Omega System DEV MODE copy/
│   │       ├── [Mirror of all documentation folders]
│   │       └── omega-dev/
│   │           └── 06_Full_System/
│   │               ├── Dev Version (Edit)/
│   │               └── LIVE Files NEVER EDIT UNLESS ASKED/
│   │
│   └── omega-dev/                                      # ACTIVE DEV WORKSPACE
│       ├── .dev_backups/
│       │   └── omega_snapshot_2026-02-28_13-46-25_Initial_State.zip
│       ├── .cursorrules
│       ├── .gitignore
│       ├── META_DEV_MODE.xml
│       ├── README.md
│       ├── TREEMAP.md
│       ├── MASTER_PRD.md
│       ├── omega-publish.py
│       ├── omega-backup.py
│       │
│       ├── 00_Changelog/
│       ├── 02_Evaluations/
│       ├── 03_Context/
│       ├── 04_Implementations/
│       ├── 05_Ideation/
│       │
│       └── 06_Full_System/                             # MASTER SANDBOX
│           ├── README_GOD_MODE.md
│           │
│           ├── Dev Version (Edit)/                     # EDITABLE REPOS
│           │   ├── Omega Claw v1 DEV/
│           │   ├── Omega System Public DEV/
│           │   ├── omega-constitution DEV/
│           │   └── omega-store DEV/
│           │
│           └── LIVE Files NEVER EDIT UNLESS ASKED/     # READ-ONLY COPIES
│               ├── Omega Claw v1 LIVE/
│               ├── Omega System Public LIVE/
│               ├── omega-constitution LIVE/
│               └── omega-store LIVE/
```

---

## OMEGA CONSTITUTION (The Brain)

The Constitution is the core protocol layer that governs all AI behavior, standards, and execution rules.

```
omega-constitution/
│
└── Entire_Constitution_Files/
    ├── .cursorrules
    ├── .gitignore
    ├── GO.md
    ├── README.md
    ├── README_ECOSYSTEM.md
    ├── CHANGELOG.md
    ├── TREEMAP.md
    ├── omega.py
    │
    ├── .github/
    │   └── workflows/
    │       └── omega-ci.yml
    │
    ├── START HERE/
    │   ├── START_HERE.md
    │   ├── RUN.md
    │   └── OMEGA_LITE.md
    │
    ├── STORE/
    │   └── README.md
    │
    ├── USER SPACE/
    │   ├── README.md
    │   │
    │   ├── dev-work/
    │   │   ├── README.md
    │   │   ├── PICKUP_ALERT.md
    │   │   ├── SESSION_CONTEXT.md
    │   │   ├── TRACKER.md
    │   │   │
    │   │   ├── hive/                              # JOB ORCHESTRATION
    │   │   │   ├── README.md
    │   │   │   ├── AGENT_SEED.md
    │   │   │   ├── MASTER_ORCHESTRATOR.md
    │   │   │   ├── master-job-board.md
    │   │   │   │
    │   │   │   ├── ai_inbox/
    │   │   │   │   └── .gitkeep
    │   │   │   │
    │   │   │   ├── ai_outbox/
    │   │   │   │   └── .gitkeep
    │   │   │   │
    │   │   │   ├── ai_state/
    │   │   │   │   ├── .gitkeep
    │   │   │   │   └── AGENT_STATUS.md
    │   │   │   │
    │   │   │   ├── blockers/
    │   │   │   │   └── .gitkeep
    │   │   │   │
    │   │   │   ├── progress/
    │   │   │   │   └── .gitkeep
    │   │   │   │
    │   │   │   └── telegram_inbox/
    │   │   │       ├── .processed.json
    │   │   │       └── FOUNDER_JOB-001-TestApp.md
    │   │   │
    │   │   ├── seed/                              # PROJECT DNA
    │   │   │   ├── AGENTS.md
    │   │   │   ├── BRAND.md
    │   │   │   ├── CONTENT.md
    │   │   │   ├── GOALS.md
    │   │   │   ├── KNOWLEDGE.md
    │   │   │   ├── LIMITS.md
    │   │   │   ├── MARKET.md
    │   │   │   ├── PROJECT.md
    │   │   │   ├── TECH_STACK.md
    │   │   │   └── USERS.md
    │   │   │
    │   │   ├── phases/
    │   │   │   └── PHASE_TEMPLATE.md
    │   │   │
    │   │   └── plug-and-play/
    │   │       └── README.md
    │   │
    │   ├── logging/
    │   │   └── compliance_report.md
    │   │
    │   └── project/
    │       └── README.md
    │
    └── omega-constitution-main/                   # THE CORE BRAIN
        │
        ├── README.md
        ├── omega-index.md
        ├── 00.help.md
        │
        ├── ─────────────────────────────────────
        │   ENTRY POINT GUIDES
        ├── ─────────────────────────────────────
        ├── ONBOARDING.md
        ├── RESUME_SESSION.md
        ├── FRESH_BUILD.md
        ├── JUST_BUILD.md
        ├── IMPORT_PROJECT.md
        ├── HIVE_PICKUP.md
        ├── AUDIT_ONLY.md
        ├── BACKEND_ONLY.md
        ├── FRONTEND_ONLY.md
        │
        ├── ─────────────────────────────────────
        │   CORE XML PROTOCOLS
        ├── ─────────────────────────────────────
        ├── SECURITY.xml              # 103 KB - Security rules
        ├── PROMPTING.xml             # 62 KB  - Prompting standards
        ├── INSTRUCTOR.xml            # 44 KB  - Teaching protocols
        ├── PRACTICES.xml             # 22 KB  - Best practices
        ├── FRAMEWORK.xml             # 16 KB  - Framework rules
        ├── QUALITY.xml               # 14 KB  - Quality standards
        ├── SOURCES.xml               # 8 KB   - Source handling + Claude Cookbooks
        ├── GITHUB_PUBLISHING.xml     # NEW    - Multi-repo sync & release management
        ├── AI_PROTOCOL.xml           # 7 KB   - AI behavior
        ├── STRUCTURE.xml             # 6 KB   - Structure rules
        ├── RUN_DEV_MODE.xml          # 1.5 KB - Dev mode config
        │
        ├── CONSTITUTION/                         # SUB-PROTOCOLS
        │   ├── CONTEXT_PROTOCOL.xml
        │   ├── EVALUATION_PROTOCOL.xml
        │   ├── FRACTAL_PROTOCOL.xml
        │   └── GLOBAL_STANDARDS.xml
        │
        ├── blueprints/                           # TEMPLATES
        │   ├── AGENT_MD.md
        │   ├── AGENT_WORKFLOW.md
        │   ├── BEST_PRACTICES_BLUEPRINT.xml
        │   ├── COST_ESTIMATE.md
        │   ├── HANDOFF.md
        │   ├── MVP_SCORECARD.md
        │   ├── POST_MORTEM.md
        │   ├── PRD.md
        │   ├── ROLLBACK.md
        │   ├── SOP.md
        │   └── TEST_PLAN.md
        │
        ├── python/                               # UTILITIES
        │   ├── README.md
        │   ├── auto_changelog.py
        │   ├── auto_help.py
        │   ├── auto_security.py
        │   ├── auto_structure.py
        │   ├── hive_scanner.py
        │   ├── omega_compiler.py
        │   ├── omega_daemon.py
        │   ├── omega_job_watcher.py
        │   └── omega_reporter.py
        │
        ├── scenarios/                            # USE CASES
        │   ├── README.md
        │   └── git-push-all-repos.md
        │
        └── tests/                                # TESTING
            └── COMPLIANCE_TESTS.md
```

### Constitution Protocol Sizes

| Protocol | Size | Purpose |
|----------|------|---------|
| SECURITY.xml | 103 KB | Security rules & validation |
| PROMPTING.xml | 62 KB | Prompting standards |
| INSTRUCTOR.xml | 44 KB | Teaching & guidance protocols |
| PRACTICES.xml | 22 KB | Best practices |
| FRAMEWORK.xml | 16 KB | Framework rules |
| QUALITY.xml | 14 KB | Quality standards |
| SOURCES.xml | 8 KB | Source handling |
| AI_PROTOCOL.xml | 7 KB | AI behavior rules |
| STRUCTURE.xml | 6 KB | Structure conventions |
| RUN_DEV_MODE.xml | 1.5 KB | Dev mode config |

### Seed Files (Project DNA)

```
seed/
├── PROJECT.md       # Core project definition
├── GOALS.md         # Project objectives
├── USERS.md         # Target users
├── MARKET.md        # Market positioning
├── BRAND.md         # Brand identity
├── CONTENT.md       # Content strategy
├── TECH_STACK.md    # Technology choices
├── KNOWLEDGE.md     # Domain knowledge
├── LIMITS.md        # Constraints & boundaries
└── AGENTS.md        # Agent configurations
```

### Hive System (Job Orchestration)

```
hive/
├── AGENT_SEED.md              # Agent initialization
├── MASTER_ORCHESTRATOR.md     # Main controller
├── master-job-board.md        # Job queue
│
├── ai_inbox/                  # Incoming jobs
├── ai_outbox/                 # Completed jobs
├── ai_state/                  # Current state
│   └── AGENT_STATUS.md
├── blockers/                  # Blocked items
├── progress/                  # In-progress work
└── telegram_inbox/            # External inputs
```

---

## OMEGA CLAW (The Dispatch)

The Claw is the orchestration and automation layer that manages agents and executes tasks.

```
omega-claw-main/
├── main.py                          # Entry point
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
├── agents/                          # AGENT CLASSES
│   ├── __init__.py
│   ├── base_agent.py                # Base agent class
│   │
│   ├── orchestrator_agent/          # Main orchestration
│   │   └── __init__.py
│   │
│   ├── phantom_agent/               # Background automation
│   │   ├── __init__.py
│   │   └── landmarks.json           # Navigation data
│   │
│   ├── reporter_agent/              # Status reporting
│   │   └── __init__.py
│   │
│   └── terminal_agent/              # CLI interactions
│       └── __init__.py
│
├── core/                            # CORE MODULES
│   ├── __init__.py
│   ├── autonomous_runner.py         # Autonomous execution
│   ├── dual_vector.py               # Vector operations
│   ├── intent_agent.py              # Intent parsing
│   ├── interactive_invoker.py       # User interactions
│   ├── logging_setup.py             # Logging config
│   ├── mcp_wizard.py                # MCP management
│   ├── orchestrator.py              # Main orchestrator
│   ├── script_invoker.py            # Script execution
│   ├── skill_loader.py              # Skill loading
│   ├── telegram_bot.py              # Telegram integration
│   └── terminal_bridge.py           # Terminal bridging
│
├── db/                              # DATABASE
│   ├── __init__.py
│   └── database.py
│
├── install/                         # INSTALLATION
│   ├── AI_PROTOCOL.xml
│   └── install_ai_layer.py
│
├── mcps/                            # MCP SERVERS
│   └── README.md
│
└── skills/                          # SKILLS
    ├── README.md
    └── _template/
        ├── handler.py
        └── skill.json
```

### Claw Agent Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      OMEGA CLAW                             │
│                   "THE DISPATCH"                            │
└─────────────────────────────────────────────────────────────┘
                           │
     ┌─────────────────────┼─────────────────────┐
     │                     │                     │
     ▼                     ▼                     ▼
┌──────────┐        ┌──────────┐        ┌──────────┐
│ AGENTS   │        │   CORE   │        │    DB    │
├──────────┤        ├──────────┤        ├──────────┤
│ • Base   │        │ • Runner │        │ • SQLite │
│ • Orch.  │◀──────▶│ • Orch.  │◀──────▶│ • State  │
│ • Phantom│        │ • Intent │        │          │
│ • Report │        │ • Skills │        │          │
│ • Term.  │        │ • MCP    │        │          │
└──────────┘        └──────────┘        └──────────┘
```

---

## OMEGA STORE (The Marketplace)

The Store contains reusable SaaS kits, skills, and templates.

```
omega-store-main/
│
├── TREEMAP.md
├── README.md
│
├── kits/                            # SAAS KITS
│   │
│   ├── _template/                   # Kit template
│   │   └── README.md
│   │
│   ├── marketing_agency/            # Agency Meta-Kit
│   │   ├── TREEMAP.md
│   │   ├── website/
│   │   │   ├── TREEMAP.md
│   │   │   ├── README.md
│   │   │   └── skills/
│   │   │       ├── contact-form/
│   │   │       │   ├── handler.py
│   │   │       │   └── skill.json
│   │   │       ├── faq-section/
│   │   │       │   ├── handler.py
│   │   │       │   └── skill.json
│   │   │       ├── hero-section/
│   │   │       │   ├── handler.py
│   │   │       │   └── skill.json
│   │   │       └── [Additional skills...]
│   │   │
│   │   └── [Other agency components...]
│   │
│   └── [Additional kits...]
│
├── skills/                          # STANDALONE SKILLS
│   └── [Independent skill modules]
│
└── examples/                        # EXAMPLES
    └── example-taskflow/
        └── README.md
```

### Kit Structure Pattern

```
kit/
├── SKILL_MANIFEST.json      # Kit metadata & dependencies
├── TREEMAP.md               # Kit structure map
├── README.md                # Documentation
│
└── skills/                  # Kit skills
    └── skill-name/
        ├── skill.json       # Skill definition
        └── handler.py       # Skill logic
```

---

## OMEGA SYSTEM PUBLIC (Execution Shell)

The public-facing execution layer and user workspace.

```
Omega-System-main/
│
├── 00 Rules/                        # PROTOCOL LAYER
│   ├── README.md
│   ├── OMEGA_RULES/
│   │   └── [Protocol XMLs]
│   ├── SKILL_KITS/
│   │   └── [Bundled kits]
│   └── Constution V13/
│       ├── TREEMAP.md
│       └── [Legacy protocols]
│
└── 01 User Space/                   # USER WORKSPACE
    ├── README.md
    │
    ├── dev-work/
    │   ├── README.md
    │   │
    │   ├── hive/                    # Job orchestration
    │   │   └── README.md
    │   │
    │   ├── plug-and-play/           # Reusable components
    │   │   └── README.md
    │   │
    │   └── [Working files]
    │
    └── project/
        └── README.md
```

---

## DOCUMENTATION STRUCTURE

```
Documentation Folders/
│
├── 00_Changelog/                    # Version histories
│   └── v16.XX_*.md                  # Evolution documents
│
├── 02_Evaluations/                  # Audits & analysis
│   ├── v1_shards/                   # v9.x evaluations
│   ├── v2_shards/                   # v13-v15 evaluations
│   ├── v3_shards/                   # v15-v16 evaluations
│   └── v4_active/                   # Current evaluation
│
├── 03_Context/                      # Session state
│   ├── CONTEXT_DEV.md               # Current goals
│   └── CONTEXT_MAP.md               # Fractal links
│
├── 04_Implementations/              # Execution plans
│   ├── Phases/                      # Phase-based plans
│   └── Testing_Archive/             # Test reports
│
└── 05_Ideation/                     # Vision & brainstorms
    └── Changelog_Archive/           # Legacy changelogs
```

---

## FILE STATISTICS

### By File Type

| File Type | Count | Purpose |
|-----------|-------|---------|
| **Markdown (.md)** | 895 | Documentation, changelogs, evaluations, plans |
| **Python (.py)** | 143 | Core application code |
| **XML (.xml)** | 76 | Protocol definitions, configurations |
| **JSON (.json)** | 19 | Data structures, configs |
| **YAML (.yml)** | 10 | Configuration files |
| **Other** | 922 | Git objects, system files, misc |

### By Repository

| Repository | Files | Primary Content |
|------------|-------|-----------------|
| omega-constitution | ~75 | Protocols, blueprints, utilities |
| omega-claw | ~45 | Agents, core modules, skills |
| omega-store | ~150 | Kits, skills, examples |
| omega-system | ~50 | Rules, user space |
| Documentation | ~200 | Changelogs, evaluations, plans |

### Key Totals

- **Total Files:** 2,065
- **Total Size:** ~13MB
- **Git Commits:** 500+
- **Core Protocols:** 14 XMLs
- **Python Modules:** 143
- **Blueprint Templates:** 11

---

## AUTOMATION SCRIPTS

| Script | Location | Purpose |
|--------|----------|---------|
| `omega-publish.py` | DEV MODE root | God-Mode multi-repo syncer |
| `omega-backup.py` | omega-dev | Automated backup system |
| `omega_compiler.py` | constitution/python | Constitution compiler |
| `omega_daemon.py` | constitution/python | Background service |
| `omega_job_watcher.py` | constitution/python | Job queue monitor |
| `omega_reporter.py` | constitution/python | Status reporting |
| `hive_scanner.py` | constitution/python | Hive system scanner |

---

## VERSION STRUCTURE

The system uses a semantic versioning approach tracked in `00_Changelog/`:

```
v16.33 ─── Current (System Router Links)
   │
v16.30-32 ─ Kit Architecture Evolution
   │
v16.26-29 ─ Standalone Architecture & Evaluations
   │
v16.23-25 ─ Omni Router Evolution
   │
v16.15-22 ─ Omni Maestro Evolution
   │
v15.x ──── Public Release & Decoupling
   │
v14.x ──── Omega Claw MVP & Hive Backend
   │
v13.x ──── Full Ecosystem Evaluation
   │
v9.x ───── Original V10 Security & Structure
```

---

## QUICK REFERENCE

### Entry Points
- **Fresh Start:** `omega-constitution/FRESH_BUILD.md`
- **Resume Work:** `omega-constitution/RESUME_SESSION.md`
- **Import Project:** `omega-constitution/IMPORT_PROJECT.md`
- **Hive Pickup:** `omega-constitution/HIVE_PICKUP.md`

### Key Files
- **Master PRD:** `MASTER_PRD.md`
- **God Mode Guide:** `06_Full_System/README_GOD_MODE.md`
- **Current Context:** `03_Context/CONTEXT_DEV.md`
- **Main Entry:** `omega-claw-main/main.py`

### Development Workflow
1. Edit files in `Dev Version (Edit)/`
2. Test changes locally
3. Run `omega-publish.py` to sync
4. Changes propagate to `LIVE Files/`

---

*Last Updated: 2026-02-28*
