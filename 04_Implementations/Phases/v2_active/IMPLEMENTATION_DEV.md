# IMPLEMENTATION_DEV — Roadmap & Ideas

**Purpose:** Track what we're building next and ideas for the future.

---

## In Progress

### Website Kit Completion
**Status:** Partially complete
**Files:**
- [x] kit.config.md
- [x] PROMPTER.md
- [ ] STRUCTURE.md (exists but needs review)
- [ ] WEBSITE_KIT.md (patterns and checklists)

---

## Next Up

### 1. Test Full Workflow
Run through a complete project using the new structure:
- Start with FRESH_BUILD.md prompt
- Fill seeds
- Let kit activate
- Build in project/
- Export with omega_compiler.py

### 2. Future Kits
Located in: `DEV/future-kits/`
- saas/ - SaaS application patterns
- api/ - API-first patterns
- automation/ - n8n/workflow patterns

### 3. Skills System
- Skill templates for specialized agents
- Skill auto-discovery like kits
- Located in omega-store/skills/

---

## Ideas Parking Lot

| Idea | Notes |
|------|-------|
| Kit marketplace | Community-contributed kits rated/reviewed |
| AI kit generator | Prompt that generates new kit from description |
| Kit validator | Script to check kit completeness |
| Cross-AI testing | Test prompts work in Claude, GPT, Cursor |
| MCP integration | Deep integration with Model Context Protocol |
| Version migration | Tool to upgrade projects between versions |

---

## Architecture Decisions

### Why dev-work + project split?
**Problem:** Users had to run compiler to separate framework files from deliverable
**Solution:** Separation is built-in. project/ is always clean.

### Why separate omega-store repo?
**Problem:** Constitution updates shouldn't require re-downloading kits
**Solution:** Two repos, two concerns. Users can star/watch what they need.

### Why kit.config.md for activation?
**Problem:** Detecting project type was implicit/guessing
**Solution:** Explicit activation rules. Kit declares when it should be used.

---

## Notes

- All constitution development uses this DEV/ folder
- We're using the framework to build the framework (meta!)
- This is NOT committed to omega-store, only omega-constitution

---

*This is our roadmap for evolving Omega itself.*
