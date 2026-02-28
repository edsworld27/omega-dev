# AGENTS — AGENT DEFINITIONS & CAPABILITY MATRICES

**Purpose:** For multi-agent and agentic workflow projects. Defines every agent's role, boundaries, and security constraints. Each agent gets a capability matrix that the system enforces.

**Required for:** Agentic Workflow projects. Optional for all others.
**If blank:** The system operates as a single-agent build (the Omega Constructor).

---

## System Architecture

**How many agents?** (e.g., 6)
**Orchestration:** (e.g., n8n + Antigravity / LangChain / Custom)
**Communication:** (e.g., Webhook / Queue / Direct handoff)

---

## Agent Definitions

*Copy this block for each agent in your system.*

### Agent [NUMBER] — [NAME]

**Role:** (Single sentence: what is this agent's sole purpose?)
**Codename:** (e.g., The Analyst, The Writer, The Guardian)
**Personality:** (How does it reason and communicate?)

#### Capability Matrix (MANDATORY — from SECURITY.xml §3.3)

| Field | Definition |
| :--- | :--- |
| **Permitted Inputs** | (Exact list of data sources this agent may read) |
| **Permitted Outputs** | (Exact list of actions this agent may take) |
| **Permitted APIs** | (Exact list of APIs/tools with scoped credentials) |
| **Forbidden Actions** | (What this agent must NEVER do) |
| **Credentials** | (Scoped credentials unique to this agent — NOT shared) |
| **Human Checkpoint** | (Conditions that trigger halt and escalation) |
| **Max Blast Radius** | (Maximum damage if this agent is fully compromised) |

#### Workflow Position
- **Receives from:** (Which agent or trigger sends data to this one?)
- **Hands off to:** (Which agent receives this one's output?)
- **Handoff condition:** (What must be true for the handoff to happen?)

#### Software Access
| Tool | Access Level | Credential Location |
| :--- | :--- | :--- |
| (e.g., Google Sheets) | (Read/Write) | (.env — SHEETS_API_KEY) |

---

## Compartmentalisation Rules
(From SECURITY.xml §3.3 — enforced automatically)

1. No two agents share the same API key or credential
2. Compromise of one agent must not cascade to others
3. Agent-to-agent communication is authenticated
4. Permissions are the minimum required for the defined function

## Parallel Execution Rules
(For agents that can operate simultaneously)

- Independent operations MAY run in parallel
- Dependent operations MUST be sequential
- Parallel agents must NOT share mutable state
- Results from parallel agents must be validated before merge
