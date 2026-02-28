# TASK: FINAL SECURITY AUDIT (THE GUARDIAN GATE)

This is the ultimate verification step performed before the project is considered "Complete". It audits the entire site against the constitutional `SECURITY.xml` laws.

## Objectives
- [ ] **Data Leak Audit:** Scan for exposed environment variables, API keys, or SSR-leaked sensitive data.
- [ ] **Input Sanitization:** Verify all forms and user inputs are sanitized against XSS and injection.
- [ ] **CSP Review:** Verify Content Security Policy headers (if applicable).
- [ ] **Dependency Audit:** Run `npm audit` or equivalent to check for known vulnerabilities in the production stack.
- [ ] **Law Compliance:** Verify the build follows ALL mandates in `00_Constitution/SECURITY.xml`.

## Audit Loops
- If a security flaw is found, AI MUST immediately:
  1. Fix the vulnerability.
  2. Document the fix in `findings.md`.
  3. Re-run this audit until it passes with 0 critical issues.

## Evidence Required
- [ ] `SECURITY_EVIDENCE.md` summary of the audit findings.
- [ ] Pass/Fail report for each `SECURITY.xml` mandate.
