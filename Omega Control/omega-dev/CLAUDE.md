# CLAUDE CODE — OMEGA DEV WORKSPACE

**Your memory IS this file system. Read treemaps, write context.**

---

## ON EVERY SESSION START

```
MUST READ FIRST:
1. 03_Context/CONTEXT_DEV.md   — What's happening, what was done
2. TREEMAP.md                  — Structure overview
```

Then summarize to user and ask what they need.

---

## ON EVERY SESSION END

```
MUST UPDATE:
1. 03_Context/CONTEXT_DEV.md   — What you did this session
```

---

## DIRECTORY STRUCTURE

```
omega-dev/
├── 00_Changelog/          # Version history
├── 02_Evaluations/        # Audits & analysis
├── 03_Context/            # ← YOUR MEMORY LIVES HERE
│   ├── CONTEXT_DEV.md     # Current state (READ/WRITE THIS)
│   └── modules/           # Shards for major changes
├── 04_Implementations/    # Plans & roadmaps
├── 05_Ideation/           # Ideas & brainstorms
└── 06_Full_System/        # THE CODE
    ├── Dev Version (Edit)/         # ← EDIT HERE
    │   ├── omega-constitution DEV/ # Brain
    │   ├── omega-store DEV/        # Marketplace
    │   ├── Omega Claw v1 DEV/      # Dispatch
    │   └── Omega System Public DEV/# Shell
    └── LIVE Files.../              # Mirrors (don't edit)
```

---

## CORE RULES

1. **Read 03_Context first** — Know the current state
2. **Edit DEV folders only** — Never edit LIVE
3. **Write context after work** — Persist your progress
4. **Never trust memory** — Always read files to verify
5. **Update treemaps** — If you change structure

---

## PUBLISHING

```bash
python omega-publish.py "type: Message"
```
Syncs all 4 repos: DEV → LIVE → GitHub

Commit types: `feat`, `fix`, `docs`, `refactor`, `sync`, `protocol`

---

## KEY FILES

| Purpose | File |
|---------|------|
| Current context | `03_Context/CONTEXT_DEV.md` |
| System map | `../README_COMPLETE_SYSTEM_MAP.md` |
| Structure | `TREEMAP.md` |
| Publisher | `omega-publish.py` |
| Backup | `omega-backup.py` |

---

## CONSTITUTION REFERENCE

When building features, check:
- `omega-constitution DEV/.../SOURCES.xml` — Valid sources
- `omega-constitution DEV/.../GITHUB_PUBLISHING.xml` — Publish rules
- `omega-store DEV/.../CLAUDE_COOKBOOKS_REFERENCE.md` — Claude patterns

---

*File system = memory. No exceptions.*
