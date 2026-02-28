# 00_RULES.md — PROJECT MANDATES (TaskFlow)

**Generated at:** CP-1 (Initialisation)  
**Status:** LAW (subordinate to SECURITY.xml and Constitution only)

---

## Project Identity
- **Name:** TaskFlow
- **Type:** Web Application (SaaS)
- **Kit:** SaaS Kit activated
- **Version:** 0.1.0 (pre-MVP)

## Non-Negotiable Rules
1. **Free tier only.** No paid services until post-launch revenue.
2. **2-week deadline.** MVP must be deployable in 14 days.
3. **No feature creep.** Only tasks in scope: create, edit, complete, delete, assign.
4. **GDPR compliance.** Cookie consent, data export, account deletion.
5. **Mobile-responsive.** Every page must work at 375px width.

## Build Order (IRONCORE)
1. **Function:** Supabase schema → auth → CRUD API → task logic
2. **UX:** Dashboard layout → task interactions → empty states → error states
3. **Form:** Brand colours → typography → animations → final polish

## Checkpoint Approvals Required
- CP-3: PRD must include acceptance criteria for all 5 core features
- CP-5: deps.md must justify every dependency (target: <5 runtime deps)
- CP-7: Lighthouse scores ≥90 on Performance and Accessibility
- CP-10: Manual test of signup → create task → complete task → logout flow
