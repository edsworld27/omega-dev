# Jarvis (Open Claw Runtime Environment)

This directory is the dedicated execution engine for the Omega System's persistent AGI. It separates the **Active Intelligence** (Jarvis / Open Claw) from the immutable rules (`omega-constitution`) and the global toolkit (`omega-store`).

## Core Architecture

- **The Rules:** Jarvis is structurally bound to ingest the global `00_Constitution` framework, ensuring it never hallucinates operational protocols or bypasses security guardrails.
- **The Engine:** This folder houses the Open Claw application (or customized Claude/Cursor instances) that actually executes tasks.
- **The Memory:** Using the `archivist-agent` skill, Jarvis writes exclusively to its local `OMEGA_MEMORY_BANK.md`. This gives the AI permanent, localized context without ever contaminating the global systems.
- **The Personal Ecosystem:** When Jarvis learns a new complex workflow, it builds a template (Kit) and pushes it to your *Personal* Kit Repository for infinite scaling.

## Directory Structure

- `OMEGA_MEMORY_BANK.md` - The AI's local "hippocampus" holding all accumulated learnings, preferences, and workflows. 
- *(Add Open Claw runtime files and mcps/ configurations here)*
