# STATE.md — PROJECT STATE (TaskFlow)

**Last updated:** CP-3 checkpoint  
**Current phase:** Phase A — Pre-Production  
**Current checkpoint:** CP-3 (PRD Review — awaiting Pilot approval)

---

## What Has Been Done
- [x] CP-0: Seed scan — all seeds validated
- [x] CP-1: Project initialised — 00_rules.md generated, folder structure created
- [x] CP-2: Environment — Supabase project created, Vercel connected, .env configured
- [/] CP-3: PRD written — awaiting Pilot review

## What's Next
- [ ] CP-4: Write SOPs for all core components
- [ ] CP-5: Submit deps.md for approval
- [ ] Phase B: Begin building

## Active Decisions
| Decision | Choice | Reason | Reversible? |
| :--- | :--- | :--- | :--- |
| Database | Supabase (Postgres) | Free tier, built-in auth, realtime | Yes (migration effort: medium) |
| Hosting | Vercel | Free, Next.js native | Yes (low effort) |
| Styling | Tailwind CSS | Fast iteration, good with Next.js | Yes (medium effort) |
| Drag-and-drop | Deferred to v2 | Reduces v1 scope by ~3 days | Yes |

## Blockers
- None currently. Waiting for PRD approval at CP-3.

## Session Count
- Session 1: Seed setup + CP-0 through CP-2
- Session 2 (current): PRD generation + CP-3
