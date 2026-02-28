# ROLLBACK PLAN — Phase [XX]

**Purpose:** How to safely revert this phase if something goes wrong post-deployment.

---

## 1. What Gets Reverted
| Component | Current Version | Rollback Version | Method |
| :--- | :--- | :--- | :--- |
| | | | (git revert / restore backup / manual) |

## 2. Data Preservation
- **Database changes:** (migrations to reverse / data to preserve)
- **User data:** (what happens to data created since deployment)
- **External integrations:** (webhooks to disable, API keys to rotate)

## 3. Rollback Steps
1. (Step-by-step procedure)
2. (Each step must be reversible itself)

## 4. Verification
- [ ] (How to verify rollback succeeded)
- [ ] (How to verify no data was lost)
- [ ] (How to verify external systems are stable)

## 5. Communication
- (Who to notify)
- (What to tell users)

## 6. Post-Rollback
- (Root cause analysis required)
- (Fix must go through full testing before re-deployment)
