# CONTEXT — THE ROOT SEED

**Purpose:** Everything grows from this file.

---

## 1. Project Name
TaskFlow

## 2. Project Type
- [x] **Web Application** (SaaS, Dashboard, Portal) → Requires: TECH_STACK.md

## 3. The North Star
Enable individuals and small teams to organise their tasks in under 60 seconds, with zero learning curve.

## 4. Who Is This For?
Freelancers, solo founders, and small teams (2–5 people) who need task management without the complexity of Jira or Asana.

## 5. What Problem Does It Solve?
Existing task managers are either too simple (notes apps) or too complex (enterprise PM tools). TaskFlow sits in the middle — structured enough to be useful, simple enough to not need a tutorial.

## 6. Non-Goals
1. We will NOT build Gantt charts or timeline views
2. We will NOT support teams larger than 10 people
3. We will NOT integrate with Slack, Teams, or other messaging platforms in v1
4. We will NOT build a mobile app (responsive web only)

## 7. Core Constraints
- **Budget:** £0 (free tier services only)
- **Timeline:** 2 weeks to MVP
- **Tech Stack:** Next.js + Supabase (see TECH_STACK.md)
- **Compliance:** GDPR (UK-based users)
- **Hosting:** Vercel (free tier)

## 8. Existing Assets
- None. Fresh build.

## 9. Key Decisions Already Made
- Supabase for auth + database (not Firebase — better Postgres access)
- Vercel for hosting (integrates with Next.js)
- No paid services in v1

## 10. Open Questions
- Should we support drag-and-drop reordering in v1 or defer to v2?
- Email notifications — include in MVP or post-launch?

## 11. Active Seed Files
Check which additional seed files you've filled in:
- [x] `BRAND.md` — Brand identity
- [x] `TECH_STACK.md` — Technology decisions
- [ ] `KNOWLEDGE.md` — Domain knowledge base
- [ ] `AGENTS.md` — Agent definitions (agentic projects only)
- [x] `PERSONAS.md` — User personas
- [x] `COMPETITORS.md` — Market analysis
- [x] `CONTENT.md` — Content strategy (websites)
- [x] `CONSTRAINTS.md` — Hard limits (budget, timeline, performance)
- [x] `METRICS.md` — Success KPIs
