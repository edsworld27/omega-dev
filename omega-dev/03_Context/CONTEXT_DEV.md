# Omega DEV Panel: Context & Current State

**Ecosystem Iteration:** V16.34 (Publishing & Cookbooks Integration)
**Core Engine:** INSTRUCTOR.xml v8.2
**Last Updated:** 2026-02-28
**Session Agent:** Claude Opus 4.5

---

## Current Development State / Phase

We are in **Infrastructure & Tooling Enhancement Phase**.

### This Session's Work (2026-02-28)

#### 1. Complete System Tree Mapping
- Created `README_COMPLETE_SYSTEM_MAP.md` - comprehensive tree of entire 2,065 file system
- Mapped all 4 repositories: Constitution, Claw, Store, System Public

#### 2. Claude Cookbooks Integration (Anthropic Official)
- **SOURCES.xml** - Added to Tier 3 & Tier 4
- **CLAUDE_COOKBOOKS_REFERENCE.md** - Created in omega-store/skills/
- Source: https://github.com/anthropics/claude-cookbooks

#### 3. GitHub Publishing Protocol (NEW)
- **GITHUB_PUBLISHING.xml** - Generic, user-configurable publishing protocol
- **python/omega_publish.py** - Generic publishing script for user projects
- **python/publish.config.template.json** - Configuration template
- **ONBOARDING.md** - Added Step 6: GitHub Setup
- **blueprints/GITHUB_SETUP.task.md** - Standalone setup task

---

## Key Concept: Two Publishing Systems

### 1. User Projects (Generic)
Uses `python/omega_publish.py` with `publish.config.json`:
```bash
python python/omega_publish.py "feat: Add feature"
```

### 2. Omega Ecosystem (God Mode)
Uses `omega-dev/omega-publish.py` for multi-repo sync:
```bash
python omega-publish.py "sync: Update ecosystem"
```

**God Mode Flow:**
```
DEV folders → LIVE folders → GitHub remotes
     ↓              ↓              ↓
   Edit here    Mirror copy    Public repos
```

---

## Files Created/Modified

| Location | File | Status |
|----------|------|--------|
| Constitution | SOURCES.xml | Modified |
| Constitution | GITHUB_PUBLISHING.xml | NEW |
| Constitution | python/omega_publish.py | NEW |
| Constitution | python/publish.config.template.json | NEW |
| Constitution | python/README.md | Modified |
| Constitution | ONBOARDING.md | Modified |
| Constitution | blueprints/GITHUB_SETUP.task.md | NEW |
| Constitution | omega-index.md | Modified |
| Store | skills/CLAUDE_COOKBOOKS_REFERENCE.md | NEW |
| Store | STORE_GUIDE.md | Modified |
| Store | TREEMAP.md | Modified |
| DEV MODE root | README_COMPLETE_SYSTEM_MAP.md | NEW |

---

## Current Issue

User reports code "went sideways" - needs investigation.

---

## Quick Reference: Publishing

**For User Projects:**
```bash
# Setup
cp python/publish.config.template.json publish.config.json
# Edit with your repo URL

# Publish
python python/omega_publish.py "feat: Message"
```

**For Omega Ecosystem:**
```bash
cd omega-dev
python omega-publish.py "sync: Message"
```
