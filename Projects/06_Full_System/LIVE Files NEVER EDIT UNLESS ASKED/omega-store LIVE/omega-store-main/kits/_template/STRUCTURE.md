# [KIT_NAME] KIT — Project Structure

**When this kit activates, create this folder structure in USER SPACE.**

---

## Folder Structure

```
[project-name]/
│
├── 00_governance/                 ← Rules, state, tracking (MANDATORY)
│   ├── rules.md                      Constitution reference
│   ├── STATE.md                      Current status
│   ├── deps.md                       Dependencies
│   ├── decisions.md                  Decision log
│   └── TRACKER.md                    Progress tracking
│
├── 01_discovery/                  ← Seeds and context
│   ├── PROJECT.md                    Project definition
│   ├── [SEED_1].md                   [Purpose]
│   ├── [SEED_2].md                   [Purpose]
│   └── CONSTRAINTS.md                Budget, timeline, limits
│
├── 02_docs/                       ← Generated documentation
│   ├── PRD.md                        Product requirements
│   ├── SOP.md                        Standard operating procedures
│   └── [DOC_1].md                    [Purpose]
│
├── 03_[PHASE_NAME]/               ← [Description]
│   ├── [folder]/                     [Purpose]
│   └── [folder]/                     [Purpose]
│
├── 04_src/                        ← Source code
│   ├── [folder]/                     [Purpose]
│   ├── [folder]/                     [Purpose]
│   └── [folder]/                     [Purpose]
│
├── 05_tests/                      ← Test files
│   ├── [test_type]/                  [Purpose]
│   └── [test_type]/                  [Purpose]
│
└── 06_deploy/                     ← Deployment config
    ├── .env.example                  Environment template
    └── [CONFIG_FILE]                 [Purpose]
```

---

## Folder Purposes

| Folder | Purpose | When Created |
|:-------|:--------|:-------------|
| `00_governance/` | Project rules and state | CP-0 (Init) |
| `01_discovery/` | Requirements and context | CP-1 (Discovery) |
| `02_docs/` | Generated specifications | CP-2 (Planning) |
| `03_[phase]/` | [Purpose] | CP-[X] |
| `04_src/` | Actual code | CP-3 (Build) |
| `05_tests/` | Test results and reports | CP-4 (Testing) |
| `06_deploy/` | Deployment configuration | CP-5 (Launch) |

---

## Required Files at Init

When project starts, create these minimum files:

```
[project-name]/
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
**Kit:** [KIT_NAME]
**Version:** 1.0

## Authority Hierarchy
1. Constitution (SECURITY.xml supreme)
2. This project's governance files
3. Kit patterns ([KIT_NAME]_KIT.md)
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
| [Requirement] | [ ] | |
| [Requirement] | [ ] | |
| [Requirement] | [ ] | |
| Deadline | [ ] | |

## Build Progress
| [Unit] | [Phase1] | [Phase2] | [Phase3] | Status |
|:-------|:---------|:---------|:---------|:-------|
| [Item] | [ ] | [ ] | [ ] | Not started |
| [Item] | [ ] | [ ] | [ ] | Not started |
| [Item] | [ ] | [ ] | [ ] | Not started |

## Quality Gates
| Check | Target | Actual | Pass |
|:------|:-------|:-------|:-----|
| [Metric 1] | [Target] | - | [ ] |
| [Metric 2] | [Target] | - | [ ] |
| Security Review | Pass | - | [ ] |
```

---

## When to Create Folders

| Checkpoint | Create |
|:-----------|:-------|
| CP-0 | `00_governance/`, `01_discovery/` |
| CP-2 | `02_docs/` |
| CP-3 | `03_[phase]/`, `04_src/` |
| CP-4 | `05_tests/` |
| CP-5 | `06_deploy/` |

**Rule:** Only create folders when needed. Don't pre-create empty structure.

---

*This structure is created by the AI when the [KIT_NAME] Kit activates.*
