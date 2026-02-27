# 🚨 06_Full_System: THE "GOD-MODE" SANDBOX
**Confidentiality:** MAXIMUM  
**Role:** The Architect's Nexus

This directory is the absolute nerve center of the Omega Framework. 

Do not treat this as a standard project folder. This is a **live orchestration environment** containing active Git clones of every single repository in the ecosystem.

## 🏗️ The Contents

You will find the complete 4-Repo Triad nested within this directory:

1. `omega-constitution/` (The Rules Data Lake)
2. `omega-store/` (The Starter Kits)
3. `omega-claw/` (The Python Automation)
4. `Omega System Public DEV/` (The isolated Execution Shell used for testing)

---

## 🔄 The CI/CD "God-Mode" Workflow

Because all 4 constituent repositories exist locally within this single context window, you (or your AI agent) have unprecedented visibility over the entire ecosystem.

**How to Execute Global Updates:**

1. **Context Loading:** Open Claude Desktop or Cursor IDE and set the root workspace to `06_Full_System/`. The AI now has absolute knowledge of the Constitution rules, the executable Python scripts, and the downstream Store templates. 
2. **Cross-Repo Mutating:** Instruct your AI to make a change.
   > *"Update the Website Kit in the `omega-store` folder to include Stripe billing, and then update the `SECURITY.xml` in the `omega-constitution` folder to include new payment rules."*
3. **Validation:** The AI edits the local files. You review the diffs.
4. **The Deployment Phase:**
   Because each nested folder (`omega-store`, `omega-constitution`, etc.) retains its original `.git` bindings to its respective upstream repository, you simply deploy the changes individually:
   ```bash
   cd omega-constitution
   git add . && git commit -m "Update SECURITY.xml for Stripe billing"
   git push

   cd ../omega-store
   git add . && git commit -m "Add Stripe billing to Website Kit"
   git push
   ```
5. **Instant Live Propagation:** The absolute millisecond those pushes succeed on GitHub, every public execution shell dynamically inherits the updates the next time a user runs `omega.py` or the `server-github` MCP prompt.

**You have just updated an entire ecosystem's logic framework and asset library globally, zero LLM hallucination, zero manual package downloads.**

---

## 🛑 Critical Warnings

*   **NEVER** run a blanket `git add .` from the root of `06_Full_System` if you intend to push changes to the public system. You *must* `cd` into the specific repository you are modifying.
*   The `06_Full_System` folder itself is tracked individually by the parent `omega-dev` repository to preserve its existence, but the nested repos are tracked by their respective upstreams.
