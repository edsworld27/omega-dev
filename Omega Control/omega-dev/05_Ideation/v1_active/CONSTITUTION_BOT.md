# Constitution Bot — Ideation

**Status**: MVP Complete
**Priority**: Active
**Resource**: [omega-bot](resource/omega-bot/)

---

## Vision

Control Omega Constitution projects from your phone via Telegram.

```
You (Phone) → Telegram → Constitution Bot → Claude Code (Mac) → Build
                 ↑                                    │
                 └────────── Progress Updates ────────┘
```

---

## How It Works

### The Flow

1. **You message Telegram**: "Build me a task management app"
2. **Bot asks constitution questions**: Kit? Mode? Constraints?
3. **Bot creates structured job**: Seeds filled, kit activated
4. **Claude Code picks up job**: Follows constitution, builds
5. **Progress updates to Telegram**: Checkpoints, blockers, completions
6. **You approve/redirect from phone**: Stay in loop or go autonomous

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   CONSTITUTION BOT                       │
│           (Telegram interface to Omega)                  │
└─────────────────────────┬───────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                    ORCHESTRATOR                          │
│    • Routes messages to agents                           │
│    • Handles risk assessment                             │
│    • Passkey protection for DANGER commands              │
└─────────────────────────┬───────────────────────────────┘
                          │
     ┌────────────────────┼─────────────────────┐
     ▼                    ▼                     ▼
┌──────────┐      ┌─────────────┐       ┌────────────┐
│ SYSTEM   │      │CONSTITUTION │       │ MONITORING │
│ AGENT    │      │ AGENT       │       │ AGENT      │
│          │      │             │       │            │
│ • status │      │ • onboard   │       │ • alerts   │
│ • docker │      │ • build     │       │ • audit    │
│ • git    │      │ • status    │       │ • security │
└──────────┘      └─────────────┘       └────────────┘
```

---

## Constitution Agent

New agent that bridges Telegram to Omega:

```
agents/constitution_agent/
├── __init__.py           # ConstitutionAgent class
├── onboarding.py         # Structured questions (mirrors ONBOARDING.md)
├── job_creator.py        # Creates job files with seeds
└── templates/            # Job templates per kit
    ├── website.md
    ├── saas.md
    ├── api.md
    └── automation.md
```

### Key Methods

| Method | Description |
|--------|-------------|
| `onboard()` | Run structured interview (mode, kit, existing work) |
| `create_job()` | Generate job file with filled seeds |
| `check_status()` | Read job status, return progress |
| `list_jobs()` | Show all active/completed jobs |

---

## Job File Format

```markdown
# JOB-007: SaaS-Task-Manager

**STATUS**: PENDING
**CREATED**: 2024-01-15T10:30:00
**KIT**: saas
**MODE**: Full Discovery

---

## Constitution Context

- **Kit**: saas (activated)
- **Mode**: Full Discovery
- **Checkpoint**: CP-0 (Seed Scan)

## Seeds (Filled)

### PROJECT.md
- Name: TaskFlow
- Audience: Freelancers
- Purpose: Simple task tracking

### TECH_STACK.md
- Frontend: Next.js
- Backend: Supabase
- Hosting: Vercel

---

## Task

Build user authentication with Supabase

---

## Deliverables

- [ ] Implementation complete
- [ ] Tests passing
- [ ] Documentation written
- [ ] Checkpoint advanced

---

## Progress Log

### 2024-01-15 10:30
- Job created via Telegram
- Status: PENDING
- Awaiting Claude Code pickup
```

---

## Reporter Integration

The existing ReporterAgent can be enhanced to:

1. **Watch job files** for status changes
2. **Send Telegram notifications** on:
   - Checkpoint completion
   - Build success/failure
   - Blockers requiring input
3. **Respond to queries** like "what's the status?"

---

## Setup Requirements

### 1. Telegram Bot
- Create via @BotFather
- Get token
- Set allowed user IDs

### 2. Environment Variables
```
TELEGRAM_BOT_TOKEN=your_token
TELEGRAM_ALLOWED_USER_IDS=your_id
DANGER_ACTION_PASSKEY=your_passkey
CONSTITUTION_PATH=~/Constution V10
JOBS_DIR=~/Constution V10/USER SPACE/dev-work/jobs
```

### 3. Claude Code Integration
- Point Claude Code at jobs directory
- Add hook to check for new jobs on startup
- Configure constitution path

---

## Use Cases

### 1. Start New Project (Phone)
```
You: "New project"
Bot: "What are you building?"
     1. Website
     2. Web App (SaaS)
     3. API
     4. Automation
You: "2"
Bot: "Project name?"
You: "TaskFlow"
Bot: "Who is it for?"
You: "Freelancers who need simple task tracking"
Bot: "Mode?"
     1. Full Discovery
     2. Quick Start
     3. Lite
You: "2"
Bot: "✅ JOB-007 Created
     Kit: saas (activated)
     Mode: Quick Start

     Claude Code will pick this up.
     I'll notify you on progress."
```

### 2. Check Progress (Phone)
```
You: "Status"
Bot: "📊 JOB-007: TaskFlow

     Status: IN PROGRESS (45%)
     Current: Building auth with Supabase
     Checkpoint: CP-1 (Seed Complete)

     No blockers. ETA ~2 hours."
```

### 3. Redirect (Phone)
```
You: "Add social login"
Bot: "Added to JOB-007:
     - Google OAuth
     - GitHub OAuth

     Claude Code will incorporate this."
```

### 4. Go Autonomous
```
You: "Go autonomous"
Bot: "🤖 Autonomous mode enabled.

     I'll continue building and only
     notify you on:
     - Completion
     - Blockers
     - Security decisions

     Say 'pause' to stop."
```

---

## Security

- **Allowed User IDs**: Only authorized users can interact
- **Passkey Gate**: Dangerous commands require passkey
- **Audit Trail**: All actions logged by MonitoringAgent
- **Confirmation Flow**: Risky actions need explicit approval

---

## Future Enhancements

1. **Voice Commands**: Speech-to-text for hands-free control
2. **Multi-Project**: Track multiple active jobs
3. **Team Mode**: Multiple users, role-based permissions
4. **Webhooks**: GitHub/Vercel integration for CI/CD updates
5. **Cost Tracking**: Token usage, API costs per project

---

## Resource

The omega-bot codebase in [resource/omega-bot/](resource/omega-bot/) contains:

- Lean Telegram bot with authorization
- 3-agent MVP: IntentAgent, ConstitutionAgent, ReporterAgent
- Omega Hive integration (FOUNDER_JOB drops)
- Zero legacy bloat — stripped from the old mac-commander
