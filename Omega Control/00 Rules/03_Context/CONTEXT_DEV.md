# Project Context

**Session:** 2026-02-28
**Phase:** System Rebuild Complete
**Version:** V16.35

---

## What Was Fixed This Session

### 1. Cleaned omega-system Structure
- Removed 00_Agents (belongs in omega-claw)
- Removed 05_Ideation, 99 Back Up (not needed)
- Simplified to clean orchestrator

### 2. Fixed Constitution DEV
- Cloned fresh from GitHub to `Projects/Dev Version (Edit)/omega-constitution DEV/`
- Fixed all XML pointers in `Projects/LIVE Files/`

### 3. Fixed ECOSYSTEM_TEMPLATE
- Removed broken symlinks
- Removed outdated agent folders
- Updated all files to clean structure
- Added proper Python scripts

---

## Current Structure

```
omega-system/
├── RUN.py                    # Entry point
├── 00 User/
│   ├── 00_Drop_Zone/         # User input
│   └── 01_Send_Off/          # User output
├── Omega Control/
│   └── 00 Rules/             # Control panel
│       ├── python/           # Scripts
│       │   ├── omega_run.py
│       │   ├── omega_onboard.py
│       │   └── omega_publish.py
│       ├── 03_Context/       # This folder
│       ├── CLAUDE.md
│       └── RULES.md
├── Projects/
│   ├── Dev Version (Edit)/   # Ed's editing area
│   │   ├── omega-constitution DEV/
│   │   ├── omega-store DEV/
│   │   └── Omega Claw v1 DEV/
│   └── LIVE Files/           # XML pointers
└── MASTER_INDEX.md
```

---

## Key Insight

**omega-system = The Orchestrator**
- Users clone this repo
- Constitution/Store/Claw are on GitHub
- AI fetches from GitHub on demand

---

## GitHub Repos

| Repo | Purpose |
|------|---------|
| omega-constitution | Brain - Rules, Protocols |
| omega-store | Marketplace - Kits, Skills |
| omega-claw | Dispatch - Orchestration, Agents |
| Omega-System | Shell - This orchestrator |

---

## Next Steps

1. Publish updated constitution to GitHub
2. Test full flow with fresh clone
3. Verify onboarding works
