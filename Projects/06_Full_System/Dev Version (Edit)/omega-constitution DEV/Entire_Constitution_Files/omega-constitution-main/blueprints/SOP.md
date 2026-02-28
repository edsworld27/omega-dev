# SOP TEMPLATE — STANDARD OPERATING PROCEDURE

**Usage:** Generated during Pre-Production (CP-4) and updated during Production. Every piece of logic must exist as an SOP in `02_architecture/` BEFORE it exists as code.

---

# SOP: [Component Name]
**Phase:** [Phase XX]
**Status:** DRAFT / APPROVED
**Location:** `02_architecture/[filename].md`

## 1. Purpose
(What does this component do? One paragraph.)

## 2. Inputs
| Input | Source | Type | Validation |
| :--- | :--- | :--- | :--- |
| (e.g., User email) | (Frontend form) | (String) | (Email format, max 255 chars) |

## 3. Outputs
| Output | Destination | Type | Format |
| :--- | :--- | :--- | :--- |
| (e.g., JWT token) | (HTTP response) | (String) | (Bearer token in header) |

## 4. Logic Flow
(Step-by-step logic in plain English. This becomes the blueprint for code.)

1. Receive [input]
2. Validate [conditions]
3. Process [action]
4. If [condition]: [path A]
5. Else: [path B]
6. Return [output]

## 5. Error Handling
| Error Condition | Response | HTTP Code | User Message |
| :--- | :--- | :--- | :--- |
| (e.g., Invalid email) | (Reject) | (400) | ("Please enter a valid email") |

## 6. Security Constraints
(From SECURITY.xml — what security rules apply to this component?)
- [ ] Input validation (all inputs malicious until proven otherwise)
- [ ] Auth required (who can access this?)
- [ ] Rate limiting (what limits apply?)
- [ ] Logging (what gets logged?)

## 7. Dependencies
(What packages/services does this component use? Must be in deps.md.)

| Package | Version | Purpose |
| :--- | :--- | :--- |

## 8. Interface Contract
(If this exposes an API endpoint, define it here. Must match INTERFACES.md.)

```
[METHOD] /api/v1/[endpoint]
Request: { field: type }
Response: { field: type }
Auth: [Required/Public]
```

## 9. Test Criteria
(How do you prove this SOP is correctly implemented?)
- [ ] Happy path test
- [ ] Edge case test
- [ ] Error handling test
- [ ] Security test
