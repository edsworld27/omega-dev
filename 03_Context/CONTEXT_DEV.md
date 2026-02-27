# CONTEXT_DEV — Constitution Development Context

**Purpose:** Working memory for developing the Omega Constitution itself. Meta-level: using the framework to build the framework.

---

## Current State

**Version:** v9
**Last Updated:** 2026-02-26
**Status:** Active development

---

## Recent Session Summary

### Session: 2026-02-26

**What we did:**
- Restructured USER SPACE into `dev-work/` + `project/` split
- Updated all path references across constitution files (13 files)
- Created omega-store repository for kits/skills/mcps
- Built kit creation framework with `_template/` folder
- Added KIT_EXPORT_GUIDE.md for AI-to-kit conversion
- Moved incomplete kits (saas, api, automation) to DEV/future-kits/

**Architecture decisions:**
- dev-work/ = framework files (don't share)
- project/ = clean deliverable (share this)
- omega-store = separate repo for community contributions

---

## Active Priorities

1. [ ] Complete website kit as reference implementation
2. [ ] Test full workflow with new structure
3. [ ] Document any gaps found during testing

---

## Known Issues / Debt

| Issue | Priority | Notes |
|-------|----------|-------|
| future-kits need completion | Low | saas, api, automation in DEV/future-kits/ |
| Python scripts need testing | Medium | omega_compiler.py, auto_security.py |

---

## Vision

Make Omega fully open-source and AI-tool agnostic:
- Cursor, VS Code, Antigravity can all understand it
- AI can turn projects into reusable kits
- Community can contribute kits to omega-store

---

*This file is our SESSION_CONTEXT.md for constitution development.*
