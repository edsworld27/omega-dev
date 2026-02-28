# KIT CONFIG — [KIT_NAME]

**Kit:** [KIT_NAME]
**Version:** 1.0
**Activates when:** PROJECT.md → Project Type = [TYPE]

---

## Authority Hierarchy

```
1. constitution/SECURITY.xml     ← Supreme (never override)
2. constitution/QUALITY.xml      ← Quality standards
3. constitution/PROMPTING.xml    ← Communication methods
4. constitution/*.xml            ← Other laws
5. This Kit's PROMPTER.md        ← Discovery + requirements
6. This Kit's kit.config.md      ← Activation rules (this file)
7. This Kit's [KIT_NAME]_KIT.md  ← Patterns + checklists
8. user-input/seed/*.md          ← User's project context
```

**Rule:** Higher number never overrides lower number.

---

## Kit Contents

| File | Purpose |
|:-----|:--------|
| `PROMPTER.md` | Discovery engine — requirements, questions |
| `STRUCTURE.md` | Project folder structure |
| `[KIT_NAME]_KIT.md` | Patterns, checklists, conventions |
| `kit.config.md` | This file — activation rules |

---

## Activation Flow

```
1. User starts session
2. AI loads constitution
3. AI reads PROJECT.md
4. AI detects: Project Type = [TYPE]
5. AI loads this kit
6. PROMPTER.md drives discovery
7. STRUCTURE.md defines project folders
8. Build begins when requirements complete
```

---

## When NOT to Use This Kit

- Project type = [OTHER_TYPE_1] → Use `[other]/` kit
- Project type = [OTHER_TYPE_2] → Use `[other]/` kit

---

*This config is read-only during build.*
