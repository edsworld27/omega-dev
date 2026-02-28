# [KIT_NAME] KIT — PROMPTER

**Purpose:** Gather all requirements before building a [TYPE] project.

**Authority:** Constitution > This Prompter > kit.config.md > [KIT_NAME]_KIT.md patterns

---

## 1. ACTIVATION GATE

Before using this kit, verify:
- [ ] Constitution loaded (SECURITY.xml, FRAMEWORK.xml, INSTRUCTOR.xml)
- [ ] PROJECT.md read (USER SPACE/seed/)
- [ ] Project type = [TYPE] confirmed
- [ ] plug-and-play/ scanned for existing assets

If any constitution file is missing → HALT. Load constitution first.

---

## 2. REQUIREMENTS TABLE

**Every row must have a value before build begins. If blank, AI must ask.**

| Requirement | Source | Status | Notes |
|:------------|:-------|:-------|:------|
| Project name | PROJECT.md | [ ] | |
| North star (singular goal) | PROJECT.md | [ ] | |
| Target audience | PROJECT.md or PERSONAS.md | [ ] | |
| [REQUIREMENT_4] | [SOURCE] or ask | [ ] | [OPTIONS] |
| [REQUIREMENT_5] | [SOURCE] or ask | [ ] | [OPTIONS] |
| [REQUIREMENT_6] | [SOURCE] or ask | [ ] | [OPTIONS] |
| [REQUIREMENT_7] | [SOURCE] or ask | [ ] | [OPTIONS] |
| [REQUIREMENT_8] | [SOURCE] or ask | [ ] | [OPTIONS] |
| Tech stack | TECH_STACK.md or ask | [ ] | |
| Launch deadline | CONSTRAINTS.md or ask | [ ] | |
| Budget tier | CONSTRAINTS.md or ask | [ ] | £0 / £500 / £5k+ |

---

## 3. DISCOVERY SEQUENCE

Use constitution PROMPTING.xml methods. Ask in batches of 2-4 questions max.

### Batch 1: Core Identity
```
I've loaded your project seeds. Let me confirm a few things:

1. **[QUESTION_1]:**
   - [Option A]
   - [Option B]
   - [Option C]
   - Other (describe)

2. **[QUESTION_2]:**
   - [Option A]
   - [Option B]
   - [Option C]
```

### Batch 2: [CATEGORY_2]
```
About [TOPIC]:

1. **[QUESTION_3]:**
   - [Option A]
   - [Option B]
   - [Option C]

2. **[QUESTION_4]:**
   - [Option A]
   - [Option B]
```

### Batch 3: Technical Preferences
```
Technical setup:

1. **Framework/platform preference?**
   - [Recommended option]
   - [Alternative 1]
   - [Alternative 2]
   - Other: ___

2. **Hosting?**
   - [Recommended option]
   - [Alternative 1]
   - [Alternative 2]
   - No preference
```

### Batch 4: Launch Context
```
Final context:

1. **Launch deadline?** (date or "no rush")

2. **Any specific integrations needed?**
   - [Common integration 1]
   - [Common integration 2]
   - [Common integration 3]
```

---

## 4. EVALUATION MATRIX

After discovery, score the project against [KIT_NAME]_KIT.md requirements:

| Category | Required Items | Status |
|:---------|:---------------|:-------|
| **[CATEGORY_1]** | [Item, Item, Item] | [ ] |
| **[CATEGORY_2]** | [Item, Item, Item] | [ ] |
| **[CATEGORY_3]** | [Item, Item, Item] | [ ] |
| **Security** | Auth, validation, HTTPS | [ ] |
| **Performance** | [Metric targets] | [ ] |
| **Testing** | [Test requirements] | [ ] |

---

## 5. BUILD HANDOFF

Once requirements table is complete:

1. **Generate [OUTPUT_1]** (e.g., architecture diagram, sitemap)
2. **Create [OUTPUT_2]** (e.g., component list, API contract)
3. **Output PRD** using constitution/blueprints/PRD.md
4. **Begin phase tasks** from STRUCTURE.md checkpoints

---

## 6. NOTHING LEFT BEHIND

Before ANY code is written, this prompter ensures:
- Every seed gap is filled by asking
- Every kit requirement is evaluated
- Every constitution rule is respected
- Every deliverable is tracked

**If a requirement is unclear → ASK. Never assume.**

---

## 7. KIT-SPECIFIC PROMPTING RULES

From constitution PROMPTING.xml, apply to [TYPE] context:

1. **[RULE_1]:** [Description]
2. **[RULE_2]:** [Description]
3. **[RULE_3]:** [Description]
4. **Chunked delivery:** Build [unit]-by-[unit], not all at once
5. **Checkpoint after each [unit]:** "[Unit] complete. Review before I continue?"

---

*This prompter auto-activates when kit.config.md conditions are met.*
