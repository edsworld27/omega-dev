# PRD TEMPLATE — PRODUCT REQUIREMENTS DOCUMENT

**Usage:** The agent uses this template when generating PRDs during Pre-Production (CP-3). The Prompter's 4-D Methodology is applied: Deconstruct the user's inputs → Diagnose gaps → Develop the requirements → Deliver for approval.

---

# Phase [XX] PRD — [Phase Name]
**Status:** DRAFT (Must be approved by Pilot)
**Generated from:** CONTEXT.md, PRD_INPUTS (if provided), Phase definition (if provided)

## 1. Objective
(One sentence: What does this phase achieve? Grounded in the North Star from CONTEXT.md.)

## 2. Paradigm
- [ ] Path A: Application (Logic First)
- [ ] Path B: Website (Content First)

## 3. MVP Definition
What is "done" for this phase? Each item must be testable.

- [ ] (Specific deliverable with binary pass/fail)
- [ ] (Specific deliverable with binary pass/fail)
- [ ] (Specific deliverable with binary pass/fail)

## 4. Acceptance Criteria
How do you PROVE each MVP item works? (From CONTEXT.md success criteria + Prompter quality standards)

| # | Criterion | Test Method | Evidence Required |
| :--- | :--- | :--- | :--- |
| 1 | | (Unit test / Manual / Screenshot) | (Log / Screenshot / Response code) |

## 5. Time Appetite
- **Estimate:** (Effort box — not a deadline)
- **Hard Deadline:** (If any)

## 6. Dependencies
(What must exist before this phase can start?)

## 7. Non-Goals for This Phase
(What is explicitly OUT of scope?)

## 8. Risks & Edge Cases
(What could go wrong? What's the fallback?)

| Risk | Likelihood | Impact | Mitigation |
| :--- | :--- | :--- | :--- |
| | (High/Med/Low) | (High/Med/Low) | |

## 9. IRONCORE Build Order
For this phase, Function means:
- **Function:** (What backend/logic/content must be built and tested first?)
- **Motion (UX):** (What UX optimisations after Function passes?)
- **Look (Form):** (What visual/styling after UX?)

## 10. SOPs Required
(List the SOPs that must be written in 02_architecture/ before code)
- [ ] (e.g., backend.md — API contract and schema)
- [ ] (e.g., auth.md — Authentication flow)
