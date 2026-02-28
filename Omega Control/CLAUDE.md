# CLAUDE CODE — OMEGA SYSTEM RULES

**You are operating inside the Omega DEV Panel.**
**Your memory IS this file system. You have NO internal memory.**

---

## PRIME DIRECTIVE: TREEMAP-BASED MEMORY

You do NOT use your own context/memory. Instead:

1. **ON SESSION START** — Read these files FIRST:
   - `03_Context/CONTEXT_DEV.md` — Current state and recent work
   - `TREEMAP.md` — System structure overview
   - `README_COMPLETE_SYSTEM_MAP.md` — Full system tree (if exists)

2. **DURING WORK** — Reference, don't remember:
   - Use `Glob` and `Read` to find files
   - Check treemaps for structure
   - Never assume - always verify by reading

3. **ON SESSION END / MAJOR MILESTONES** — Write context:
   - Update `03_Context/CONTEXT_DEV.md` with what was done
   - Create shards in `03_Context/modules/` for major changes
   - Update `TREEMAP.md` if structure changed

---

## MEMORY LOCATIONS

| What | Where |
|------|-------|
| Current state | `03_Context/CONTEXT_DEV.md` |
| System structure | `TREEMAP.md`, `README_COMPLETE_SYSTEM_MAP.md` |
| Version history | `00_Changelog/v*.md` |
| Evaluations | `02_Evaluations/` |
| Implementation plans | `04_Implementations/` |
| Ideas/brainstorms | `05_Ideation/` |
| The actual code | `06_Full_System/Dev Version (Edit)/` |

---

## ARCHITECTURE: 4-REPO ECOSYSTEM

```
06_Full_System/Dev Version (Edit)/
├── omega-constitution DEV/    # THE BRAIN — Protocols & rules
├── omega-store DEV/           # THE MARKETPLACE — Kits & skills
├── Omega Claw v1 DEV/         # THE DISPATCH — Orchestration
└── Omega System Public DEV/   # EXECUTION SHELL — User-facing
```

**Edit in DEV folders. LIVE folders are mirrors.**

---

## CRITICAL RULES

### 1. Read Before Acting
Before ANY work, read:
```
03_Context/CONTEXT_DEV.md
```
This tells you what's happening and what was done.

### 2. Write Your Work
After completing significant work, UPDATE:
```
03_Context/CONTEXT_DEV.md
```
Include: what you did, files changed, current state.

### 3. Use Shards for History
For major changes, create versioned shards:
```
03_Context/modules/v[X]_[description].md
```

### 4. Never Trust Your Memory
If you "remember" something, VERIFY by reading the file.
Your memory resets. The files don't.

### 5. Treemap is Truth
The TREEMAP.md files are authoritative structure maps.
If you change structure, update the treemap.

---

## PUBLISHING (GOD MODE)

To publish all repos to GitHub:
```bash
cd omega-dev
python omega-publish.py "type: Your commit message"
```

This syncs: DEV → LIVE → GitHub for all 4 repos.

---

## QUICK REFERENCE

**Find a file:** Use `Glob` with pattern
**Search content:** Use `Grep` with pattern
**Read context:** `Read 03_Context/CONTEXT_DEV.md`
**Check structure:** `Read TREEMAP.md`
**Edit code:** Files in `06_Full_System/Dev Version (Edit)/`

---

## STARTUP SEQUENCE

When user opens this project, ALWAYS:

1. Read `03_Context/CONTEXT_DEV.md`
2. Summarize current state to user
3. Ask what they want to work on
4. Reference treemaps as needed during work
5. Update context before session ends

---

*Your memory is the file system. Act accordingly.*
