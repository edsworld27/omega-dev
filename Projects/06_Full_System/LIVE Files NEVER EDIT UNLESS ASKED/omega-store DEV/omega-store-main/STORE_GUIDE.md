# STORE — Browse & Download

**Version:** 9.0

The store contains optional add-ons for the Omega Constitution Pack. Browse what's here, pick what fits your project, and drop it into `user-input/plug-and-play/`.

---

## How It Works

1. **Browse** the store folders below
2. **Pick** the kits, skills, or MCP configs that match your project
3. **Copy** the folder/file into `user-input/plug-and-play/`
4. The agent reads plug-and-play at CP-0 and auto-activates matching items

```
store/kits/website/          →  copy to  →  user-input/plug-and-play/kits/website/
store/skills/writer-agent.md →  copy to  →  user-input/plug-and-play/skills/writer-agent.md
store/mcps/MCP_CONFIG.md     →  copy to  →  user-input/plug-and-play/mcps/MCP_CONFIG.md
```

---

## What's Available

### Kits (Assembly Lines)

Kits are complete build systems with phases, task files, and trackers.

| Kit | Folder | Best For |
|-----|--------|----------|
| **Website** | `kits/website/` | Marketing sites, landing pages, blogs |
| **SaaS** | `kits/saas/` | Web apps, dashboards, auth + billing |
| **API** | `kits/api/` | REST APIs, backend services, webhooks |
| **Automation** | `kits/automation/` | n8n, Make, Zapier, agentic workflows |

#### Kit Structure (Website Kit as Example)

```
kits/website/
├── WEBSITE_KIT.md              ← Patterns & best practices
├── kit.config.md               ← Auto-activation rules
├── TRACKER.md                  ← Website-specific progress tracker
│
├── preproduction/              ← PLANNING & IMPORTS
│   ├── CHECKLIST.md
│   ├── BRAND_IMPORT.task.md    ← Import brand assets
│   ├── WIREFRAME_IMPORT.task.md← Import wireframes/mockups
│   └── CONTENT_AUDIT.task.md   ← Audit existing content
│
├── production/                 ← BUILD TASKS
│   ├── CHECKLIST.md
│   ├── SEO.task.md
│   ├── PERFORMANCE.task.md
│   └── ACCESSIBILITY.task.md
│
└── testing/                    ← VERIFICATION TASKS
    ├── CHECKLIST.md
    ├── LIGHTHOUSE.task.md
    ├── MOBILE.task.md
    └── BROWSER.task.md
```

#### Task Files

Task files (`.task.md`) are portable instructions any AI can run:

1. Drop the file into your project
2. Tell your AI: "Execute [TASK_NAME].task.md"
3. AI follows the instructions and reports results

Task files work **standalone** — no constitution required. But they respect constitution rules when present.

#### Drop Zone

`user-input/plug-and-play/` is your drop zone. Put existing work here alongside store items:

- Wireframes from Figma
- Code exports from Lovable/v0
- Brand guidelines (PDF, images)
- Existing content

The AI will detect dropped files at CP-0 and ask what they are.

Or tell the AI: "My wireframes are at /path/to/files" — works the same way.

---

### Skills (Agent Capabilities)

#### Official Reference (TIER 1)

| Reference | File | Source |
|-----------|------|--------|
| **Claude Cookbooks** | `CLAUDE_COOKBOOKS_REFERENCE.md` | https://github.com/anthropics/claude-cookbooks |

> **IMPORTANT:** When implementing Claude-specific features, ALWAYS check the Claude Cookbooks reference first. These are Anthropic's official, production-ready patterns.

**Cookbook Capabilities:**
- RAG (Retrieval Augmented Generation)
- Tool Use & Integration (Customer Service, SQL, Calculators)
- Multimodal/Vision (Charts, Forms, PDF Extraction)
- Sub-agents (Haiku as sub-agent with Opus)
- JSON Mode, Prompt Caching, Content Moderation
- Agent Patterns & Orchestration

#### Agent Skills

| Skill | File | Purpose |
|-------|------|---------|
| Classifier | `classifier-agent.md` | Categorise, tag, route data |
| Writer | `writer-agent.md` | Generate structured content |
| Analyst | `analyst-agent.md` | Data analysis and insights |
| Guardian | `guardian-agent.md` | Relationship preservation |
| Orchestrator | `orchestrator-agent.md` | Multi-agent coordination |

---

### AI Assistants (Coming Soon)

Custom AI tools built for specific workflows.

| Folder | Purpose |
|--------|---------|
| `ai-assistants/` | Links to hosted AI assistants |

---

### MCP Configs (Tool Connections)

| Config | File | Examples Included |
|--------|------|-------------------|
| MCP Server Config | `MCP_CONFIG.md` | Filesystem, GitHub, PostgreSQL, Brave Search |

---

### Examples (Reference Projects)

| Example | Folder | Shows |
|---------|--------|-------|
| TaskFlow | `examples/example-taskflow/` | Complete project with all seeds + governance files filled |

---

## Rules

- Store items are **subordinate to the Constitution**. If a kit says "skip testing" — the Constitution wins.
- You can combine kits (SaaS + API = full-stack). See INSTRUCTOR.xml §6 for conflict resolution.
- Creating your own kit? Add it to `user-input/plug-and-play/kits/[your-kit]/` — no need to put it in the store.

---

## Quick Start

1. Pick a kit that matches your project type
2. Copy it to `user-input/plug-and-play/kits/`
3. If you have existing work, drop it in `user-input/plug-and-play/`
4. Fill in `user-input/seed/PROJECT.md`
5. Run the ignition prompt
6. Follow the checklists and task files
