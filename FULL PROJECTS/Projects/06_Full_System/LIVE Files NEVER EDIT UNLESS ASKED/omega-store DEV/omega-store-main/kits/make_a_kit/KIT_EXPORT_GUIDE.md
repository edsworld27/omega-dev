# KIT EXPORT GUIDE

**For AI agents that want to turn a completed project into a reusable kit.**

---

## The Concept

After building a project, the AI can "export" what it learned into a kit that others can reuse.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   1. AI builds a project (website, SaaS, API, etc.)         │
│   2. AI tracks: questions asked, folders created, patterns  │
│   3. AI generates kit files from this knowledge             │
│   4. Kit dropped into omega-store/kits/                     │
│   5. Anyone can now build similar projects faster           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## When to Export

Export a kit when:
- You've built a complete project of a specific type
- The patterns would be reusable for similar projects
- The discovery questions were valuable and shouldn't be forgotten
- The folder structure worked well

---

## Export Process

### Step 1: Gather What You Learned

Review the completed project and extract:

| What | Where to Find It | Goes Into |
|:-----|:-----------------|:----------|
| Questions you asked | Conversation history, SESSION_CONTEXT.md | PROMPTER.md |
| Folder structure | The project itself | STRUCTURE.md |
| Patterns used | Code patterns, architecture decisions | [NAME]_KIT.md |
| Activation trigger | Project type | kit.config.md |

---

### Step 2: Generate PROMPTER.md

**Extract the discovery flow:**

```markdown
## What questions did you ask?

Review conversation and list:
1. Core identity questions (what is this, who is it for)
2. Technical questions (stack, hosting, integrations)
3. Business questions (pricing, users, constraints)
4. Launch questions (timeline, MVP scope)

## Group into batches of 2-4

Batch 1: [Category] → Questions 1-3
Batch 2: [Category] → Questions 4-6
...

## Create requirements table

Every question = one requirement row
| Requirement | Source | Status | Notes |
```

**Template prompt for AI:**
```
Based on the project I just built, generate a PROMPTER.md that captures:
1. All the questions I asked during discovery
2. Grouped into batches of 2-4 questions
3. A requirements table with every decision point
4. An evaluation matrix for quality checks

Use omega-store/kits/_template/PROMPTER.md as the format.
```

---

### Step 3: Generate STRUCTURE.md

**Extract the folder structure:**

```markdown
## What folders were created?

List every folder in the project:
- 00_governance/ (if used)
- 01_discovery/
- 02_docs/
- 03_[custom]/
- 04_src/
- 05_tests/
- 06_deploy/

## When was each folder created?

Map to checkpoints:
- CP-0: governance, discovery
- CP-2: docs
- CP-3: src, design
- CP-4: tests
- CP-5: deploy

## What files are essential at init?

Minimum files needed to start a new project of this type.
```

**Template prompt for AI:**
```
Based on the project structure I created, generate a STRUCTURE.md that:
1. Shows the complete folder tree
2. Explains each folder's purpose
3. Maps folders to checkpoints
4. Lists minimum files needed at init
5. Includes file templates for governance files

Use omega-store/kits/_template/STRUCTURE.md as the format.
```

---

### Step 4: Generate [NAME]_KIT.md

**Extract patterns and checklists:**

```markdown
## What patterns did you use?

List reusable patterns:
- Code architecture patterns
- File naming conventions
- Component structures
- API patterns
- Data flow patterns

## What was on your checklist?

Categories to check before launch:
- Security items
- Performance targets
- Quality metrics
- Compliance requirements

## What integrations were common?

| Integration | Tool Used | Why |
```

**Template prompt for AI:**
```
Based on the patterns I used in this project, generate a [NAME]_KIT.md that:
1. Lists all reusable patterns with examples
2. Creates category checklists
3. Documents quality standards with targets
4. Lists common integrations
5. Documents anti-patterns to avoid

Use omega-store/kits/_template/KIT_NAME_KIT.md as the format.
```

---

### Step 5: Generate kit.config.md

**Define activation:**

```markdown
## When should this kit activate?

Project type trigger: "[TYPE]"
Example: "E-commerce Site", "Chrome Extension", "Discord Bot"

## What other kits should NOT be used?

List exclusive types.

## Authority hierarchy

Copy from template, update kit name.
```

**Template prompt for AI:**
```
Generate a kit.config.md that:
1. Sets activation trigger to "[PROJECT_TYPE]"
2. Lists when NOT to use this kit
3. Includes the standard authority hierarchy

Use omega-store/kits/_template/kit.config.md as the format.
```

---

## One-Shot Export Prompt

Copy this prompt after completing a project:

```
I've just finished building a [PROJECT_TYPE] project. I want to export this as a reusable kit for the Omega Constitution framework.

Based on:
1. The questions I asked during discovery
2. The folder structure I created
3. The patterns and decisions I made
4. The quality checks I performed

Generate a complete kit with these 4 files:

1. **kit.config.md** — Activation trigger: [PROJECT_TYPE]
2. **PROMPTER.md** — All discovery questions grouped into batches, requirements table
3. **STRUCTURE.md** — Project folder structure with checkpoint mapping
4. **[PROJECT_TYPE]_KIT.md** — Patterns, checklists, quality standards

Use the templates from omega-store/kits/_template/ as the format.

Output each file in full, ready to save.
```

---

## Validation Checklist

Before dropping your exported kit into omega-store/kits/:

- [ ] kit.config.md has correct activation trigger
- [ ] PROMPTER.md has 8-15 requirements
- [ ] PROMPTER.md has 3-4 discovery batches (2-4 questions each)
- [ ] STRUCTURE.md has 00_governance/ (mandatory)
- [ ] STRUCTURE.md maps folders to checkpoints
- [ ] [NAME]_KIT.md has real patterns (not placeholders)
- [ ] [NAME]_KIT.md has measurable quality standards
- [ ] All files use correct naming convention

---

## Example: Exporting a Chrome Extension Kit

After building a Chrome extension, the AI might generate:

**kit.config.md:**
```markdown
**Kit:** Chrome Extension
**Activates when:** PROJECT.md → Project Type = Chrome Extension / Browser Extension
```

**PROMPTER.md requirements table:**
```markdown
| Requirement | Source | Status | Notes |
|:------------|:-------|:-------|:------|
| Extension name | PROJECT.md | [ ] | |
| Manifest version | Ask | [ ] | V2 (legacy) / V3 |
| Permissions needed | Ask | [ ] | tabs, storage, etc. |
| Content scripts? | Ask | [ ] | Yes / No |
| Background service? | Ask | [ ] | Yes / No |
| Popup UI? | Ask | [ ] | Yes / No |
| Options page? | Ask | [ ] | Yes / No |
| Browser targets | Ask | [ ] | Chrome / Firefox / Both |
```

**STRUCTURE.md:**
```markdown
my-extension/
├── 00_governance/
├── 01_discovery/
├── 02_docs/
├── 04_src/
│   ├── manifest.json
│   ├── background/
│   ├── content/
│   ├── popup/
│   └── options/
├── 05_tests/
└── 06_deploy/
    └── store-assets/
```

---

## Contributing Exported Kits

To share your kit with the community:

1. Export kit using this guide
2. Test with fresh session
3. Create folder in omega-store/kits/
4. Submit PR to omega-store repo
5. Include README.md with:
   - What this kit builds
   - Example use case
   - Any special requirements

---

## The Feedback Loop

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   Build Project → Export Kit → Share Kit → Others Use It    │
│         ↑                                           │       │
│         └───────────── Improve ←────────────────────┘       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

Every project makes the ecosystem smarter.

---

*The more kits exist, the faster everyone builds.*
