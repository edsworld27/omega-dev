# OMEGA SYSTEM IMPLEMENTATION PLAN

**Date:** 2026-02-28
**Status:** IN PROGRESS - USER REPORTED SYSTEM BROKE
**Session:** Claude Opus 4.5

---

## WHAT WE WERE BUILDING

### Core Architecture

```
CONSTITUTION (Core Rules - Local)
       ↓
   Points to
       ↓
STORE (Live Cloud - GitHub)
       ↓
Skills, Kits, Patterns, Cookbooks
       ↓
Instantly available everywhere
```

### Key Insight

- Constitution = Kernel (core rules)
- Store = Cloud/CDN (all dynamic resources)
- ONE skill `/omega` loads constitution
- Constitution fetches from store on demand
- Works in ANY IDE

---

## WHAT WAS CREATED THIS SESSION

### 1. Tree Mapping
- `README_COMPLETE_SYSTEM_MAP.md` - Full system tree (2,065 files)

### 2. Claude Cookbooks Integration
- `SOURCES.xml` - Added to Tier 3 & 4
- `skills/CLAUDE_COOKBOOKS_REFERENCE.md` - In store

### 3. GitHub Publishing
- `GITHUB_PUBLISHING.xml` - Generic protocol
- `python/omega_publish.py` - Generic script
- `python/publish.config.template.json` - Config template
- `blueprints/GITHUB_SETUP.task.md` - Setup task
- `ONBOARDING.md` - Added Step 6 (GitHub) + Step 0 (IDE)

### 4. Claude Code Skills
- `.claude/skills/omega/SKILL.md` - ONE master skill
- `.claude/settings.json` - SessionStart hook
- `CLAUDE.md` - Project rules

### 5. SKILLS.xml (In Progress)
- Was rewriting to point to STORE instead of containing everything
- Store = live cloud, always updated
- Constitution just points to store

---

## FILES CREATED/MODIFIED

| Location | File | Status |
|----------|------|--------|
| Root | README_COMPLETE_SYSTEM_MAP.md | Created |
| Root | CLAUDE.md | Created |
| .claude/ | settings.json | Created |
| .claude/skills/omega/ | SKILL.md | Created |
| Constitution | SOURCES.xml | Modified |
| Constitution | GITHUB_PUBLISHING.xml | Created |
| Constitution | SKILLS.xml | In Progress |
| Constitution | ONBOARDING.md | Modified |
| Constitution | omega-index.md | Modified |
| Constitution/python | omega_publish.py | Created |
| Constitution/python | publish.config.template.json | Created |
| Constitution/python | README.md | Modified |
| Constitution/blueprints | GITHUB_SETUP.task.md | Created |
| Store/skills | CLAUDE_COOKBOOKS_REFERENCE.md | Created |
| Store | STORE_GUIDE.md | Modified |
| Store | TREEMAP.md | Modified |

---

## NEXT STEPS (BEFORE BREAK)

1. Finish SKILLS.xml v2.0 - points to store
2. Consolidate file locations (Projects vs omega-dev issue)
3. Test the system
4. Create fractal shard for v16.34

---

## KNOWN ISSUES

1. **Two locations:** Files in both `/Projects/` and `/omega-dev/`
2. **Constitution files:** Some in wrong location
3. **User reported:** System broke after changes

---

## TO FIX

1. Identify what user changed
2. Consolidate to correct location
3. Ensure omega-publish.py paths are correct
4. Verify constitution structure intact
5. Test skills work

---

## KEY FILES TO CHECK

```
omega-dev/omega-publish.py - Main publisher
omega-dev/06_Full_System/ - Should contain repos
Projects/06_Full_System/ - Also contains repos (?)
03_Context/CONTEXT_DEV.md - Current state
```

---

## STORE ARCHITECTURE (The Goal)

```
omega-store/
├── skills/                    # Agent skills
│   ├── analyst-agent.md
│   ├── classifier-agent.md
│   ├── guardian-agent.md
│   ├── orchestrator-agent.md
│   ├── writer-agent.md
│   └── CLAUDE_COOKBOOKS_REFERENCE.md
├── kits/                      # Project kits
│   ├── marketing_agency/
│   │   └── website/
│   └── make_a_kit/
├── examples/                  # Patterns
└── TREEMAP.md                 # Store map
```

Constitution points to store → fetch on demand → always live

---

*This plan saved so we don't lose context. Ready to help fix the system.*
