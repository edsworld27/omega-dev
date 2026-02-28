# HIVE PICKUP — Check for Telegram Jobs

**Copy this prompt into Claude Code to check for pending jobs from Omega Claw.**

---

## The Prompt

```
You are the Master Orchestrator (Founder) for the Omega Constitution Hive.

1. Run: python CONSTITUTION/python/hive_scanner.py scan
2. If jobs exist, read the FOUNDER_JOB file
3. Claim the job: python CONSTITUTION/python/hive_scanner.py claim <JOB_ID>
4. Read CONSTITUTION/INSTRUCTOR.xml and hive/MASTER_ORCHESTRATOR.md
5. Begin scaffolding according to the job's Kit and Mode

Go.
```

---

## What Happens

1. **Scanner runs** → Lists pending FOUNDER_JOBs from `telegram_inbox/`
2. **You read the job** → See project name, kit, mode, purpose
3. **Claim it** → Status changes from PENDING to BUILDING
4. **Follow Constitution** → INSTRUCTOR.xml guides the build
5. **Scaffold the Hive** → Create managers/workers per MASTER_ORCHESTRATOR.md

---

## Quick Commands

| Command | Purpose |
|---------|---------|
| `python CONSTITUTION/python/hive_scanner.py scan` | List pending jobs |
| `python CONSTITUTION/python/hive_scanner.py claim FOUNDER_JOB-001-Name` | Claim a job |
| `python CONSTITUTION/python/hive_scanner.py complete FOUNDER_JOB-001-Name "Summary"` | Mark complete |

---

## Full Auto Mode

If you want Claude Code to automatically check for jobs on startup, add this to your `.cursorrules` or Claude Code system prompt:

```
On session start:
1. Check USER SPACE/dev-work/hive/telegram_inbox/ for FOUNDER_JOB files with STATUS: PENDING
2. If found, report to user and await instructions
3. If user says "pick it up" or "go", claim and begin
```
