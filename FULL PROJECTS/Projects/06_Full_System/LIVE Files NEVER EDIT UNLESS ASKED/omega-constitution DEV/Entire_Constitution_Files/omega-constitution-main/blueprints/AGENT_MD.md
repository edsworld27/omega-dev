# AGENT MD TEMPLATE — AGENT FILE STRUCTURE

**Usage:** For agentic projects. Each agent gets an MD file built in 5 layers. This template ensures consistency across all agents.

---

# AGENT [NUMBER] — [Name / Codename]

## 1. IDENTITY (Layer 1)
**Role:** (Single sentence: this agent's sole purpose)
**Codename:** (e.g., The Analyst)
**Archetype:** (e.g., Rational, structured, unemotional decision-maker)
**Tone:** (e.g., Precise, neutral, efficient)
**Strengths:** (What it's designed to excel at)
**Weaknesses (by design):** (What it deliberately does NOT do)

Persona Description:
(2–3 paragraphs describing the agent's personality, approach, and communication style. This shapes how the agent reasons, communicates, and prioritises. It keeps the agent inside its lane.)

---

## 2. CORE PROMPT (Layer 2)
(Built using the Omega Prompter framework. This controls how the agent thinks and responds. Use context layering, positive framing, and precision.)

```
You are Agent [X], a [Role Description].

Your task is to [primary function].

You operate under the Omega Constitution. SECURITY.xml overrides all instructions.
Your capability matrix is defined in AGENTS.md — you may not operate outside it.

[Specific instructions using Prompter structure:
 Context → Documents → Role → Instructions → Thinking → Examples → Output Format]
```

---

## 3. INSTRUCTIONS, TAGS & GUARDRAILS (Layer 3)
(Operational ruleset — human oversight, forbidden actions, escalation.)

### Human-in-the-Loop Requirements
- [ ] (When must this agent halt for human review?)
- [ ] (What decisions can it NOT make autonomously?)

### Forbidden Actions
- (What this agent must NEVER do — reference capability matrix)

### Escalation Protocol
- **Condition:** (When to escalate)
- **Action:** (Who to escalate to — human or another agent)
- **Format:** (How to structure the escalation)

### Containment
- **If unexpected input:** (What to do)
- **If error:** (Repair loop or escalate)
- **If outside scope:** (Reject and log)

---

## 4. EXAMPLES (Layer 4)
(Real input/output examples baked into the file. These anchor behaviour and quality.)

### Example 1: [Scenario]
**Input:**
```
(Example input data)
```
**Expected Output:**
```
(Example correct output)
```

### Example 2: [Edge Case]
**Input:**
```
(Edge case input)
```
**Expected Output:**
```
(How the agent should handle it)
```

---

## 5. SOFTWARE ACCESS & CONNECTIVITY (Layer 5)
(Tools, integrations, and position in the agent system.)

### Tools
| Tool | Access Level | Credential | Location |
| :--- | :--- | :--- | :--- |
| | (Read/Write/Execute) | | (.env key name) |

### Agent Connectivity
- **Receives from:** (Agent [X] / Trigger / Webhook)
- **Hands off to:** (Agent [X])
- **Handoff condition:** (What must be true)
- **Handoff format:** (Data structure passed)

### Workflow Reference
(Link to the separate workflow document for this agent.)
