# KNOWLEDGE — PROJECT KNOWLEDGE BASE

**Purpose:** Domain-specific knowledge the agent needs. Industry rules, reference data, business logic, regulatory requirements. This is the project's "brain" — distinct from the constitution's "spine."

**If blank:** The agent works from CONTEXT.md and general knowledge only.

---

## 1. Domain Rules
(Business rules the agent must follow. Be explicit — these become law within the project.)

| Rule | Source | Priority |
| :--- | :--- | :--- |
| (e.g., "Orders over £500 require manual approval") | (Business requirement) | (Must-Have) |

## 2. Reference Data
(Links or references to existing documentation, APIs, specs, or standards.)

| Document | Type | Location |
| :--- | :--- | :--- |
| (e.g., "API Specification") | (OpenAPI / PDF / Link) | (URL or file path) |

## 3. Industry / Regulatory Context
(What compliance or industry standards apply?)
- (e.g., GDPR — EU data protection)
- (e.g., PCI DSS — payment card security)
- (e.g., WCAG 2.1 AA — accessibility)

## 4. Terminology
(Project-specific terms the agent must use correctly.)

| Term | Definition | Context |
| :--- | :--- | :--- |
| (e.g., "Lead") | (A potential customer who has expressed interest) | (Used in Agent 1 classification) |

## 5. Existing Patterns
(Patterns or conventions that already exist in the project or organisation.)
- (e.g., "All API responses use snake_case")
- (e.g., "Error codes follow HTTP standards")

## 6. External Knowledge Sources
(Approved external sources the agent may reference — feeds into SOURCES.md Tier 3.)

| Source | URL | Trust Level |
| :--- | :--- | :--- |
| (e.g., "Next.js Docs") | (https://nextjs.org/docs) | (Tier 4 — Official) |
