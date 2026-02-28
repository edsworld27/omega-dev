# AntiGravity + NotebookLM Integrations

**Purpose:** A master playbook for pairing NotebookLM's deep research and synthesis capabilities with AntiGravity's execution and building powers across multiple domains (Business, Education, Personal Productivity, Content).

## Setup & Diagnostics
Before executing these workflows, ensure the NotebookLM MCP server is installed and authenticated via `notebooklm-mcp-auth`. Verify connections by listing available notebooks.

## Key Workflows

### 1. The 30-Minute Course Creator (Education)
- **NotebookLM:** Executes deep research on a topic, extracts key modules, and generates intro video/audio scripts and quiz flashcards.
- **AntiGravity:** Takes these raw assets, builds the course platform/UI, and handles the payment logic.

### 2. Client Onboarding on Autopilot (Agency)
- **NotebookLM:** Researches the client's industry, generating Video Overviews, Infographics, Data Tables, and Slide Decks.
- **AntiGravity:** Assembles these assets into a custom client portal within minutes.

### 3. The Content Repurposing Engine (Media)
- **NotebookLM:** Conducts deep research on one core topic and splits it into 12 formats (Blog, YouTube Script, Podcast audio, Tweets, Newsletters, etc.).
- **AntiGravity:** Orchestrates the publishing or packaging of these assets into automated channels.

### 4. Meeting Intelligence System (Advanced Automation)
- **NotebookLM:** Parses meeting recordings to extract key decisions, action items, and follow-up questions, turning them into briefing docs and data tables.
- **AntiGravity:** Creates the tasks in project management tools, sends summary emails, and schedules follow-ups.

## Constraints
- **Token Efficiency:** Always use `source_get_content` to extract specific data before querying to save 10x the processing cost.
- **Drive Sync:** Use `source_sync_drive` to keep notebooks updated dynamically.

## Quality Criteria
- NotebookLM is strictly utilized as "The Brain" (analysis/research).
- AntiGravity is strictly utilized as "The Builder" (execution/automation).
- The transition between research and execution must be seamless and fully automated where defined.
