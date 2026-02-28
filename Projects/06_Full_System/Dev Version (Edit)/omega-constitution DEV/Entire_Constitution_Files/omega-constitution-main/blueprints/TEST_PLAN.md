# TEST PLAN TEMPLATE

**Usage:** Generated during Testing phase (CP-8). Defines what to test, how, and what evidence is required.

---

# Test Plan: Phase [XX] — [Name]
**Status:** DRAFT / APPROVED
**Evidence Location:** `04_tests/results/YYYY-MM-DD_phase_xx/`

## 1. Scope
(What is being tested in this cycle?)

## 2. Function Tests (IRONCORE Priority 1)
| # | Function | Test | Input | Expected Output | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| F-01 | | Happy path | | | Log / Screenshot |
| F-02 | | Edge case | | | Log / Screenshot |
| F-03 | | Error handling | | | Log / Screenshot |
| F-04 | | Security | | | Log / Screenshot |
| F-05 | | Performance | | | Log / Timing |

## 3. UX Tests (IRONCORE Priority 2)
| # | Flow | Test | Expected Behaviour | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| U-01 | | Navigation works | | Screenshot |
| U-02 | | Error states display correctly | | Screenshot |
| U-03 | | Responsive on mobile | | Screenshot |
| U-04 | | Accessibility (WCAG) | | Audit report |

## 4. Integration Tests
| # | System A | System B | Test | Expected | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| I-01 | | | Handshake | | Log |
| I-02 | | | Data flow | | Log |

## 5. Agent Tests (Agentic Projects Only)
| # | Agent | Test Type | Test | Expected | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| A-01 | | Capability boundary | Attempt forbidden action | Rejection | Log |
| A-02 | | Hallucination | Request unlisted library | Refusal | Log |
| A-03 | | Prompt injection | Inject override instruction | Rejection | Log |
| A-04 | | Handoff integrity | Send data to next agent | Correct receipt | Log |
| A-05 | | Parallel execution | Run independent ops | No interference | Log |

## 6. Regression Tests
(Verify previous phase deliverables still work after this phase's changes.)

| # | Previous Feature | Test | Expected | Evidence |
| :--- | :--- | :--- | :--- | :--- |

## 7. Pass / Fail Criteria
- **Pass:** ALL function tests pass AND all critical UX tests pass AND no security failures
- **Fail:** ANY function test fails OR ANY security test fails
- **Conditional:** UX/integration failures that don't block functionality

## 8. Actionable Insights
(After testing, the agent generates these for the Pilot.)
- What works well and why
- What failed and the root cause
- Recommendations for the next phase
- Performance metrics vs budget
- Security posture assessment
