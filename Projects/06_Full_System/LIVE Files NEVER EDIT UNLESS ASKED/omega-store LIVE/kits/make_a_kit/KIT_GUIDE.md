# KIT GUIDE — HOW KITS WORK

**Version:** 5.0

**What:** Kits are complete project assembly systems. They include patterns, checklists, and a PROMPTER that ensures nothing gets missed during discovery and build.

**Where:** `store/kits/[kit-name]/`

**Rule:** Kits are subordinate to the Constitution. Kit patterns never override `SECURITY.xml` or any constitution law.

---

## How Kits Work

```
1. Constitution loads first (always)
2. AI reads your seeds in user-input/seed/
3. AI detects project type → activates matching kit
4. Kit PROMPTER.md takes over discovery
5. PROMPTER ensures every requirement is filled
6. Build only begins when requirements table is complete
```

---

## Available Kits

| Kit | Folder | Use When |
|:----|:-------|:---------|
| **Website** | `website/` | Marketing sites, landing pages, blogs, portfolios |
| **SaaS** | `saas/` | Web apps, dashboards, auth + billing |
| **API** | `api/` | REST/GraphQL APIs, backend services, webhooks |
| **Automation** | `automation/` | n8n, Make, Zapier, agentic workflows |

---

## Kit Contents

Each kit folder contains:

| File | Purpose |
|:-----|:--------|
| `PROMPTER.md` | Discovery engine — requirements table, question batches, evaluation matrix |
| `[KIT]_KIT.md` | Patterns, checklists, and conventions for that project type |
| `kit.config.md` | Activation rules, authority hierarchy, override logic |
| `TRACKER.md` | Progress tracking specific to that kit |
| `preproduction/` | Tasks before build (imports, audits, planning) |
| `production/` | Tasks during build (implementation checklists) |
| `testing/` | Tasks before launch (validation, lighthouse, etc.) |

---

## The PROMPTER System

The PROMPTER is the brain of each kit. It ensures nothing gets missed.

### What PROMPTER.md Does

1. **Activation Gate** — Verifies constitution is loaded before proceeding
2. **Requirements Table** — Every row must be filled before build begins
3. **Discovery Batches** — Questions in groups of 2-4 (never overwhelming)
4. **Evaluation Matrix** — Scores project against kit requirements
5. **Build Handoff** — Generates sitemap, component list, PRD

### Requirements Table Example (Website Kit)

| Requirement | Source | Status | Notes |
|:------------|:-------|:-------|:------|
| Project name | PROJECT.md | [ ] | |
| North star | PROJECT.md | [ ] | |
| Site type | PROJECT.md | [ ] | Marketing/Blog/E-commerce/Portfolio |
| Page count | CONTENT.md or ask | [ ] | |
| Content ready? | Ask or plug-and-play/ | [ ] | Yes/No/Partial |
| Brand guidelines? | BRAND.md or plug-and-play/ | [ ] | |
| Tech stack | TECH_STACK.md or ask | [ ] | |
| Launch deadline | CONSTRAINTS.md or ask | [ ] | |

**Rule:** If a cell is blank, the AI asks. Never assumes.

---

## Flexible Discovery Options

You don't have to go through the full discovery with this framework. Multiple paths to get requirements filled:

### Option 1: Full In-Framework Discovery
```
Use RUN.md → AI asks questions → fills seeds → evaluates kit requirements → builds
```
Best for: Starting from scratch, want full guidance

### Option 2: External AI Discovery
```
Use ChatGPT/Claude web to plan → export your decisions → paste into seed files → upload
```
Best for: Saving credits, prefer conversation outside framework

### Option 3: Custom AI Discovery
```
Use your own fine-tuned AI or GPT → generate requirements → import into seeds
```
Best for: Organisations with their own AI systems

### Option 4: Self-Placeholder
```
Fill seed files yourself → mark [PLACEHOLDER] where unsure → AI asks about placeholders only
```
Best for: Experienced users who know what they want

### Option 5: Hybrid
```
Fill what you know → drop existing docs in plug-and-play/ → AI fills gaps
```
Best for: Projects with existing work

**All paths converge:** The kit PROMPTER still validates that requirements are complete before build begins.

---

## Authority Hierarchy

When instructions conflict, higher number wins:

```
1. constitution/SECURITY.xml     ← Supreme (never override)
2. constitution/QUALITY.xml      ← Quality standards
3. constitution/PROMPTING.xml    ← Communication methods
4. constitution/*.xml            ← Other laws
5. Kit PROMPTER.md               ← Discovery + requirements
6. kit.config.md                 ← Activation rules
7. [KIT]_KIT.md                  ← Patterns + checklists
8. user-input/seed/*.md          ← User's project context
```

**Rule:** A lower-number file always beats a higher-number file.

---

## How To Use

### If you want full guidance:
1. Run `RUN.md`
2. Answer the AI's questions
3. Kit activates automatically based on your project type
4. PROMPTER drives the conversation
5. Build begins when ready

### If you want to skip ahead:
1. Fill `user-input/seed/PROJECT.md` with your project type
2. Fill other seeds with what you know
3. Drop any existing files in `user-input/plug-and-play/`
4. Copy the kit you need into `plug-and-play/kits/`
5. Run the AI — it will validate and fill remaining gaps

---

## Combining Kits

Some projects need multiple kits:

| Combined | Example |
|:---------|:--------|
| SaaS + API | Full-stack app with public API |
| Website + Automation | Marketing site with lead capture workflows |
| API + Automation | Backend service with scheduled jobs |

**Rule:** When kits combine, their requirements stack. Both PROMPTERs must be satisfied.

---

## Creating Your Own Kit

1. Create folder: `store/kits/[your-kit]/`
2. Copy structure from an existing kit
3. Create your `PROMPTER.md` with:
   - Activation gate
   - Requirements table (specific to your project type)
   - Discovery batches
   - Evaluation matrix
4. Create `kit.config.md` with:
   - Authority hierarchy
   - Activation trigger
   - Override rules
5. Create `[YOUR_KIT]_KIT.md` with patterns and checklists

---

## Summary

**Kits = Complete project systems**
- PROMPTER ensures nothing is missed
- Patterns give you proven structures
- Checklists keep you on track
- Trackers show progress

**Nothing gets left behind.**
