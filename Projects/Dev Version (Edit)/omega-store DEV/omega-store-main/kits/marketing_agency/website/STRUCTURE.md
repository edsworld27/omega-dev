# WEBSITE KIT — Project Structure

**When this kit activates, create this folder structure for the project.**

---

## Folder Structure

```
my-website-project/
│
├── 00_governance/                 ← Rules, state, tracking
│   ├── rules.md                      Constitution reference
│   ├── STATE.md                      Current status
│   ├── deps.md                       Dependencies
│   ├── decisions.md                  Decision log
│   └── TRACKER.md                    Progress tracking
│
├── 01_discovery/                  ← Seeds and context
│   ├── PROJECT.md                    Project definition
│   ├── BRAND.md                      Brand guidelines
│   ├── CONTENT.md                    Content inventory
│   ├── PERSONAS.md                   Target users
│   ├── COMPETITORS.md                Competitor analysis
│   └── CONSTRAINTS.md                Budget, timeline, limits
│
├── 02_docs/                       ← Generated documentation
│   ├── PRD.md                        Product requirements
│   ├── SOP.md                        Standard operating procedures
│   ├── SITEMAP.md                    Page structure
│   └── TECH_SPEC.md                  Technical specification
│
├── 03_design/                     ← Design assets
│   ├── wireframes/                   Low-fidelity layouts
│   ├── mockups/                      High-fidelity designs
│   └── assets/                       Logos, images, icons
│
├── 04_src/                        ← Source code
│   ├── components/                   Reusable UI components
│   ├── pages/                        Page templates
│   ├── styles/                       CSS/Tailwind
│   ├── lib/                          Utilities and helpers
│   └── public/                       Static assets
│
├── 05_tests/                      ← Test files
│   ├── lighthouse/                   Performance reports
│   ├── accessibility/                A11y audits
│   └── browser/                      Cross-browser tests
│
└── 06_deploy/                     ← Deployment config
    ├── .env.example                  Environment template
    ├── vercel.json                   (or netlify.toml)
    └── LAUNCH_CHECKLIST.md           Pre-launch tasks
```

---

## Folder Purposes

| Folder | Purpose | When Created |
|:-------|:--------|:-------------|
| `00_governance/` | Project rules and state | CP-0 (Init) |
| `01_discovery/` | Requirements and context | CP-1 (Discovery) |
| `02_docs/` | Generated specifications | CP-2 (Planning) |
| `03_design/` | Visual assets | CP-2 or when provided |
| `04_src/` | Actual code | CP-3 (Build) |
| `05_tests/` | Test results and reports | CP-4 (Testing) |
| `06_deploy/` | Deployment configuration | CP-5 (Launch) |

---

## Required Files at Init

When project starts, create these minimum files:

```
my-website-project/
├── 00_governance/
│   ├── rules.md              → Link to constitution
│   ├── STATE.md              → "Phase: Discovery"
│   └── TRACKER.md            → Empty tracker table
└── 01_discovery/
    └── PROJECT.md            → Template for user to fill
```

---

## File Templates

### 00_governance/rules.md
```markdown
# Project Rules

This project follows the Omega Constitution.

**Constitution Location:** [path to Constution V10]
**Kit:** Website
**Version:** 1.0

## Authority Hierarchy
1. Constitution (SECURITY.xml supreme)
2. This project's governance files
3. Kit patterns (WEBSITE_KIT.md)
4. User decisions
```

### 00_governance/STATE.md
```markdown
# Project State

**Project:** [Name]
**Phase:** Discovery
**Checkpoint:** CP-0
**Last Updated:** [Date]

## Current Focus
- Gathering requirements

## Blockers
- None

## Next Action
- Complete PROMPTER requirements table
```

### 00_governance/TRACKER.md
```markdown
# Progress Tracker

## Discovery
| Requirement | Status | Source |
|:------------|:-------|:-------|
| Project name | [ ] | |
| Site type | [ ] | |
| Pages | [ ] | |
| Tech stack | [ ] | |
| Brand | [ ] | |
| Content | [ ] | |
| Deadline | [ ] | |

## Build Progress
| Page | Design | Code | Test | Status |
|:-----|:-------|:-----|:-----|:-------|
| Home | [ ] | [ ] | [ ] | Not started |
| About | [ ] | [ ] | [ ] | Not started |
| Contact | [ ] | [ ] | [ ] | Not started |

## Quality Gates
| Check | Target | Actual | Pass |
|:------|:-------|:-------|:-----|
| Lighthouse Performance | ≥90 | - | [ ] |
| Lighthouse Accessibility | ≥90 | - | [ ] |
| Mobile Responsive | Yes | - | [ ] |
| SSL Active | Yes | - | [ ] |
```

---

## When to Create Folders

| Checkpoint | Create |
|:-----------|:-------|
| CP-0 | `00_governance/`, `01_discovery/` |
| CP-2 | `02_docs/` |
| CP-3 | `03_design/`, `04_src/` |
| CP-4 | `05_tests/` |
| CP-5 | `06_deploy/` |

**Rule:** Only create folders when needed. Don't pre-create empty structure.

---

*This structure is created by the AI when the Website Kit activates.*
