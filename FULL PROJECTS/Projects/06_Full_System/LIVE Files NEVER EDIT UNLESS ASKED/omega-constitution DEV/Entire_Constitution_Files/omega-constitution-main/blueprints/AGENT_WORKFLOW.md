# AGENT WORKFLOW — Agent [X]: [Name]

**Purpose:** Visual and logical map of how this agent operates. Sits alongside the Agent MD file.

---

## Workflow Diagram
```
[TRIGGER] ──► [RECEIVE INPUT] ──► [VALIDATE]
                                      │
                              ┌───────┴───────┐
                              │               │
                          [VALID]         [INVALID]
                              │               │
                        [PROCESS]        [REJECT + LOG]
                              │
                        [GENERATE OUTPUT]
                              │
                   ┌──────────┴──────────┐
                   │                     │
            [HUMAN CHECK?]          [AUTO PASS]
                   │                     │
            [AWAIT APPROVAL]        [HANDOFF]
                   │                     │
            [APPROVED] ──────────► [HAND OFF TO AGENT X]
```

## Decision Points
| Point | Condition | Path A | Path B |
| :--- | :--- | :--- | :--- |
| Validation | Input matches schema | Process | Reject |
| Human check | (when required) | Wait for approval | Auto-pass |

## Data Flow
| From | Data | Format | To |
| :--- | :--- | :--- | :--- |

## Trigger Conditions
- (What starts this agent?)
- (Webhook / Schedule / Manual / Agent handoff)

## Error Handling
| Error | Action | Escalation |
| :--- | :--- | :--- |
