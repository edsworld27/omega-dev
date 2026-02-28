# Kit Template

**Copy this folder to create a new kit.**

---

## Quick Start

```bash
# 1. Copy the template
cp -r _template/ my-new-kit/

# 2. Rename files
mv my-new-kit/KIT_NAME_KIT.md my-new-kit/MY_NEW_KIT.md

# 3. Find and replace placeholders
# Replace all [PLACEHOLDERS] in each file

# 4. Done — kit auto-activates when dropped in store/kits/
```

---

## Files to Edit

| File | What to Change |
|:-----|:---------------|
| `kit.config.md` | Kit name, activation trigger, excluded types |
| `PROMPTER.md` | Requirements table, discovery batches, evaluation matrix |
| `STRUCTURE.md` | Project folder structure, file templates |
| `KIT_NAME_KIT.md` | Patterns, checklists, quality standards |

---

## Placeholders to Replace

| Placeholder | Replace With |
|:------------|:-------------|
| `[KIT_NAME]` | Your kit name (e.g., `MOBILE`, `CLI`, `GAME`) |
| `[TYPE]` | Project type trigger (e.g., `Mobile App`, `CLI Tool`) |
| `[REQUIREMENT_X]` | Specific requirements for this project type |
| `[CATEGORY_X]` | Discovery/evaluation categories |
| `[QUESTION_X]` | Discovery questions |
| `[RULE_X]` | Kit-specific prompting rules |
| `[SOURCE]` | Where to find requirement (seed file or "ask") |
| `[OPTIONS]` | Valid values for the requirement |

---

## Checklist Before Publishing

- [ ] All `[PLACEHOLDERS]` replaced
- [ ] kit.config.md has correct activation trigger
- [ ] PROMPTER.md has 8-15 requirements
- [ ] PROMPTER.md has 3-4 discovery batches
- [ ] STRUCTURE.md defines project folders
- [ ] STRUCTURE.md has 00_governance/ (mandatory)
- [ ] KIT_NAME_KIT.md renamed correctly
- [ ] Patterns are specific to this project type
- [ ] Tested with fresh session

---

## Test Your Kit

```
1. Start fresh AI session
2. Load constitution
3. Say: "I want to build a [TYPE]"
4. Verify: Kit auto-activates
5. Verify: PROMPTER asks questions in batches
6. Verify: All requirements get covered
```

---

*See KIT_CREATION_GUIDE.md for full documentation.*
