# KIT CREATION GUIDE

**For developers who want to build custom kits for the Omega Constitution.**

---

## Quick Start (Use the Template)

```bash
# 1. Copy the template folder
cp -r _template/ my-new-kit/

# 2. Rename the kit pattern file
mv my-new-kit/KIT_NAME_KIT.md my-new-kit/MY_NEW_KIT.md

# 3. Edit the 4 files — replace all [PLACEHOLDERS]

# 4. Done — kit auto-activates when project type matches
```

**See `_template/README.md` for placeholder reference.**

---

## Plug-and-Play Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   1. Create your kit folder                                 │
│   2. Add required files (PROMPTER, config, patterns)        │
│   3. Drop into store/kits/                                  │
│   4. Done. It auto-activates when project type matches.     │
│                                                             │
│   NO registration. NO index file. NO manual config.         │
│   The folder structure IS the registry.                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## What is a Kit?

A kit is a specialized module that teaches the AI how to build a specific type of project.

```
┌─────────────────────────────────────────────────────────┐
│                      CONSTITUTION                       │
│              (Security, Quality, Prompting)             │
│                    [Foundation]                         │
└───────────────────────────┬─────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│                         KIT                             │
│                   [Your Module]                         │
│                                                         │
│   PROMPTER.md      "What to ask"                        │
│   kit.config.md    "When to activate"                   │
│   [TYPE]_KIT.md    "Patterns and checklists"            │
│   phases/          "Tasks by stage"                     │
│                                                         │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│                     USER PROJECT                        │
│              (Seeds, Content, Constraints)              │
└─────────────────────────────────────────────────────────┘
```

**Kits contain:**
- **Requirements** — What must be gathered before building
- **Patterns** — Templates, checklists, best practices
- **Tasks** — Phase-by-phase work items
- **Rules** — Kit-specific constraints

---

## Kit Structure

```
store/kits/your-kit/
├── PROMPTER.md           # REQUIRED — Discovery engine
├── kit.config.md         # REQUIRED — Activation rules
├── STRUCTURE.md          # REQUIRED — Project folder structure
├── YOUR_KIT.md           # REQUIRED — Patterns and checklists
├── preproduction/        # Optional — Pre-build tasks
├── production/           # Optional — Build tasks
├── testing/              # Optional — QA tasks
├── TRACKER.md            # Optional — Progress tracking
└── README.md             # Optional — Quick reference
```

**STRUCTURE.md** defines what folders the AI creates when starting a project with this kit.

---

## Step 1: Create kit.config.md

This file tells the AI when to activate your kit.

### Template

```markdown
# KIT CONFIG — [Your Kit Name]

**Kit:** [Name]
**Version:** 1.0
**Activates when:** PROJECT.md → Project Type = [Type] (or similar)

---

## Authority Hierarchy

```
1. constitution/SECURITY.xml     ← Supreme (never override)
2. constitution/QUALITY.xml      ← Quality standards
3. constitution/PROMPTING.xml    ← Communication methods
4. constitution/*.xml            ← Other laws
5. This Kit's PROMPTER.md        ← Discovery + requirements
6. This Kit's kit.config.md      ← Activation rules (this file)
7. This Kit's [NAME]_KIT.md      ← Patterns + checklists
8. user-input/seed/*.md          ← User's project context
```

**Rule:** Higher number never overrides lower number.

---

## Kit Contents

| File | Purpose |
|:-----|:--------|
| `PROMPTER.md` | How to discover requirements |
| `[NAME]_KIT.md` | Patterns, templates, checklists |
| `kit.config.md` | This file |

---

## Activation Flow

```
1. User starts session
2. AI loads constitution
3. AI reads PROJECT.md
4. AI detects: Project Type = [Your Type]
5. AI loads this kit
6. PROMPTER.md drives discovery
7. Build begins when requirements complete
```

---

## When NOT to Use This Kit

- [List other project types that should use different kits]

---

*This config is read-only during build.*
```

---

## Step 2: Create PROMPTER.md

This is the discovery engine. It ensures nothing gets missed.

### Template

```markdown
# [YOUR KIT] — PROMPTER

**Purpose:** Gather all requirements before building a [type] project.

**Authority:** Constitution > This Prompter > kit.config.md > [NAME]_KIT.md patterns

---

## 1. ACTIVATION GATE

Before using this kit, verify:
- [ ] Constitution loaded (SECURITY.xml, QUALITY.xml, PROMPTING.xml)
- [ ] PROJECT.md read
- [ ] Project type = [Your Type] confirmed
- [ ] plug-and-play/ scanned for existing assets

If any constitution file is missing → HALT.

---

## 2. REQUIREMENTS TABLE

**Every row must have a value before build begins.**

| Requirement | Source | Status | Notes |
|:------------|:-------|:-------|:------|
| [Requirement 1] | [Where to find it] | [ ] | |
| [Requirement 2] | [Where to find it] | [ ] | |
| [Requirement 3] | [Where to find it] | [ ] | |
| ... | | | |

---

## 3. DISCOVERY SEQUENCE

Ask in batches of 2-4 questions max.

### Batch 1: [Category Name]
```
[2-4 questions about this category]
```

### Batch 2: [Category Name]
```
[2-4 questions about this category]
```

### Batch 3: [Category Name]
```
[2-4 questions about this category]
```

---

## 4. EVALUATION MATRIX

| Category | Required Items | Status |
|:---------|:---------------|:-------|
| [Category 1] | [What must be defined] | [ ] |
| [Category 2] | [What must be defined] | [ ] |
| ... | | |

---

## 5. BUILD HANDOFF

Once requirements table is complete:
1. [First output to generate]
2. [Second output to generate]
3. Begin phase tasks

---

## 6. NOTHING LEFT BEHIND

Before ANY code is written:
- Every seed gap is filled
- Every kit requirement is evaluated
- Every constitution rule is respected

**If unclear → ASK. Never assume.**

---

## 7. KIT-SPECIFIC PROMPTING RULES

[List 3-5 rules specific to this project type]

---

*This prompter auto-activates when kit.config.md conditions are met.*
```

---

## Step 3: Create STRUCTURE.md

This file defines the project folder structure the AI creates.

### Template

```markdown
# [YOUR KIT] — Project Structure

**When this kit activates, create this folder structure for the project.**

---

## Folder Structure

```
my-project/
│
├── 00_governance/                 ← Rules, state, tracking
│   ├── rules.md                      Constitution reference
│   ├── STATE.md                      Current status
│   └── TRACKER.md                    Progress tracking
│
├── 01_discovery/                  ← Seeds and requirements
│   ├── PROJECT.md                    Project definition
│   └── [other seeds...]              As needed
│
├── 02_docs/                       ← Generated documentation
│   ├── PRD.md                        Requirements
│   └── SOP.md                        Procedures
│
├── 03_[phase]/                    ← Kit-specific folders
│   └── ...
│
└── ...
```

---

## Folder Purposes

| Folder | Purpose | When Created |
|:-------|:--------|:-------------|
| `00_governance/` | Project rules and state | CP-0 (Init) |
| `01_discovery/` | Requirements and context | CP-1 (Discovery) |
| ... | | |

---

## When to Create Folders

| Checkpoint | Create |
|:-----------|:-------|
| CP-0 | `00_governance/`, `01_discovery/` |
| CP-2 | `02_docs/` |
| ... | |

**Rule:** Only create folders when needed.
```

### Key Principles

1. **00_governance/ is mandatory** — Every project needs rules and state
2. **01_discovery/ holds seeds** — User requirements go here
3. **Number prefixes** — Keep folders ordered (00_, 01_, 02_...)
4. **Create just-in-time** — Don't pre-create empty folders
5. **Kit-specific folders** — Add folders relevant to your project type

---

## Step 4: Create [NAME]_KIT.md

This file contains patterns, checklists, and templates.

### Template

```markdown
# [YOUR KIT NAME] KIT

**Purpose:** Patterns and checklists for building [type] projects.

---

## Overview

[2-3 sentences describing what this kit helps build]

---

## Checklist

### [Category 1]
- [ ] [Item]
- [ ] [Item]
- [ ] [Item]

### [Category 2]
- [ ] [Item]
- [ ] [Item]

---

## Patterns

### [Pattern 1 Name]

**When:** [When to use this pattern]

**Structure:**
```
[Template or code structure]
```

### [Pattern 2 Name]

**When:** [When to use this pattern]

**Structure:**
```
[Template or code structure]
```

---

## Common Integrations

| Integration | Recommended Tool | Notes |
|:------------|:-----------------|:------|
| [Integration 1] | [Tool] | |
| [Integration 2] | [Tool] | |

---

## Quality Standards

| Metric | Target | Measure With |
|:-------|:-------|:-------------|
| [Metric 1] | [Value] | [Tool/Method] |
| [Metric 2] | [Value] | [Tool/Method] |

---

## Anti-Patterns

| Don't Do This | Do This Instead |
|:--------------|:----------------|
| [Bad practice] | [Good practice] |
| [Bad practice] | [Good practice] |

---

*Use with PROMPTER.md for complete coverage.*
```

---

## Step 5: Design Your Requirements Table

The requirements table is the heart of your PROMPTER. Every row must be filled before building begins.

### Guidelines

| Column | Purpose | Example |
|:-------|:--------|:--------|
| **Requirement** | What must be defined | "Authentication method" |
| **Source** | Where to look first | "TECH_STACK.md or ask" |
| **Status** | Checkbox for tracking | [ ] or [x] |
| **Notes** | Valid values or context | "JWT / Session / OAuth" |

### Good Requirements

```
✓ Specific: "Payment provider" not "Handle money"
✓ Verifiable: Can check if it's been answered
✓ Actionable: Leads to a build decision
✓ Sourced: Points to where answer might exist
```

### Bad Requirements

```
✗ Vague: "Make it good"
✗ Compound: "Auth and billing and dashboard"
✗ Opinion: "Should look nice"
✗ Unsourced: No idea where to find the answer
```

---

## Step 6: Write Discovery Batches

Discovery batches are scripted question sets. Keep them:

- **Small:** 2-4 questions per batch
- **Focused:** One category per batch
- **Progressive:** Start broad, get specific
- **Actionable:** Each answer fills a requirement row

### Example Flow

```
Batch 1: Core Identity (What is this?)
    ↓
Batch 2: Users/Audience (Who is it for?)
    ↓
Batch 3: Technical (How will it work?)
    ↓
Batch 4: Constraints (What are the limits?)
```

### Question Format

Good:
```
1. **Authentication method:**
   - Email/password
   - Social login (Google, GitHub)
   - Magic link
   - SSO/Enterprise
```

Bad:
```
1. How do you want to handle authentication? There are many options
   like email/password, social login, magic links, SSO, or you could
   use a third-party service, or build custom, what do you think?
```

---

## Step 7: Define Evaluation Matrix

The evaluation matrix maps kit checklist items to verification status.

### Template

| Category | Required Items | Status |
|:---------|:---------------|:-------|
| **Security** | Auth, input validation, HTTPS | [ ] |
| **Core Features** | [List minimum viable features] | [ ] |
| **Performance** | [Metrics with targets] | [ ] |
| **Compliance** | [Legal/regulatory items] | [ ] |

---

## Step 8: Drop It In

**No registration needed.** Just place your kit folder in `store/kits/`.

```
store/kits/
├── website/           ← Existing kit
├── saas/              ← Existing kit
├── api/               ← Existing kit
└── your-new-kit/      ← Drop yours here. Done.
```

**How auto-discovery works:**
1. AI scans `store/kits/` at session start
2. Any folder with `kit.config.md` is a valid kit
3. AI reads activation trigger from `kit.config.md`
4. When project type matches, kit auto-loads

**That's it.** The folder structure is the registry.

---

## Testing Your Kit

Before publishing, verify:

### 1. Activation Test
- Start fresh session
- Load constitution
- State your project type
- Kit should auto-activate

### 2. Discovery Test
- Every requirement should get asked
- Questions should come in batches (2-4)
- No question should be skipped

### 3. Completion Test
- Fill all requirements
- Kit should generate PRD or build plan
- All evaluation matrix items should be checkable

### 4. Override Test
- Try conflicting values
- Higher authority should win
- Security should never be overridden

---

## Kit Quality Checklist

Before publishing your kit:

- [ ] kit.config.md has authority hierarchy
- [ ] kit.config.md lists when NOT to use
- [ ] PROMPTER.md has activation gate
- [ ] Requirements table covers all must-haves
- [ ] Discovery batches are 2-4 questions each
- [ ] Evaluation matrix maps to kit checklist
- [ ] STRUCTURE.md defines project folders
- [ ] STRUCTURE.md has 00_governance/ (mandatory)
- [ ] [NAME]_KIT.md has patterns and checklists
- [ ] Tested activation, discovery, completion
- [ ] Respects constitution authority

---

## Example Kits

Study these for reference:

| Kit | Strength | Learn From |
|:----|:---------|:-----------|
| `website/` | Complete PROMPTER | Discovery batches, evaluation matrix |
| `saas/` | (Template) | Basic structure |
| `api/` | (Template) | Basic structure |

---

## Common Mistakes

| Mistake | Problem | Fix |
|:--------|:--------|:----|
| Too many requirements | Overwhelms user | Focus on must-haves only |
| No discovery batches | AI asks all at once | Script the question flow |
| Missing activation gate | Kit loads without constitution | Always check constitution first |
| Overriding security | Dangerous | Security.xml is supreme, always |
| No evaluation matrix | Can't verify completeness | Map requirements to verification |

---

## Publishing Your Kit

### For Personal Use
```
1. Create kit folder with required files
2. Drop into store/kits/
3. Test with fresh session
4. Done — it works immediately
```

### For Community Contribution
```
1. Create kit folder with required files
2. Test thoroughly (all 4 test types)
3. Add README.md with usage examples
4. Submit PR to main repo
5. Community reviews and merges
```

### Sharing Your Kit

Kits are portable. To share:
```
1. Zip your kit folder
2. Send to recipient
3. They unzip into their store/kits/
4. It works. No config needed.
```

---

## Architecture Summary

```
┌─────────────────────────────────────────────────────────────┐
│                       FOUNDATION                            │
│                    (Omega provides)                         │
├─────────────────────────────────────────────────────────────┤
│   constitution/     Laws, security, quality                 │
│   user-input/       Seeds, working memory                   │
│   store/kits/       ← KITS PLUG IN HERE                     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      YOUR KIT                               │
│                   (You provide)                             │
├─────────────────────────────────────────────────────────────┤
│   PROMPTER.md      Discovery engine                         │
│   kit.config.md    Activation trigger                       │
│   [NAME]_KIT.md    Patterns + checklists                    │
│   phases/          Optional task folders                    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    AUTO-ACTIVATION                          │
├─────────────────────────────────────────────────────────────┤
│   User says "I'm building a [type]"                         │
│   AI scans store/kits/ for matching kit.config.md           │
│   Kit loads automatically                                   │
│   PROMPTER takes over discovery                             │
│   Build begins when requirements complete                   │
└─────────────────────────────────────────────────────────────┘
```

---

*Kits extend the constitution. They don't replace it. Build once, share everywhere.*
