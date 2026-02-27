# ONBOARDING — Structured Interview Flow

**This is the MANDATORY first interaction when a user starts.**

The AI MUST follow this exact sequence. No skipping. No deviation.

---

## STEP 1: Intent Detection (ALWAYS FIRST)

```
═══════════════════════════════════════════════════════════
  OMEGA CONSTRUCTOR — WHAT DO YOU NEED?
═══════════════════════════════════════════════════════════

  1. BUILD SOMETHING — I want to create a project
  2. LEARN FIRST — I want to understand how this works
  3. GET HELP — I have a question about the system

  Reply with: 1, 2, or 3
═══════════════════════════════════════════════════════════
```

**If LEARN FIRST (2):** Jump to LEARNING PATH below.
**If GET HELP (3):** Jump to HELP PATH below.
**If BUILD (1):** Continue to Step 2.

---

## STEP 2: Mode Selection (If building)

```
═══════════════════════════════════════════════════════════
  HOW WOULD YOU LIKE TO WORK?
═══════════════════════════════════════════════════════════

  1. FULL DISCOVERY — Guide me through everything
     (Best for: new projects, exploring ideas)

  2. QUICK START — I already filled the seed files
     (Best for: pre-planned projects)

  3. LITE MODE — Minimal questions, simple build
     (Best for: small models, quick prototypes)

  4. JUST BUILD — Skip to code, I know what I want
     (Best for: experienced users, clear specs)

  Reply with: 1, 2, 3, or 4
═══════════════════════════════════════════════════════════
```

**WAIT for answer before proceeding.**

---

## STEP 3: Project Type (Triggers kit activation)

```
═══════════════════════════════════════════════════════════
  WHAT ARE YOU BUILDING?
═══════════════════════════════════════════════════════════

  A. WEBSITE — Marketing site, landing page, portfolio
  B. WEB APP — SaaS, dashboard, user accounts
  C. API — Backend service, REST/GraphQL
  D. AUTOMATION — Workflows, integrations, scripts
  E. OTHER — Tell me what

  Reply with: A, B, C, D, or E
═══════════════════════════════════════════════════════════
```

**Kit activation:** A=website, B=saas, C=api, D=automation

**WAIT for answer before proceeding.**

---

## STEP 4: Existing Work Detection (Critical)

```
═══════════════════════════════════════════════════════════
  DO YOU HAVE EXISTING WORK?
═══════════════════════════════════════════════════════════

  1. STARTING FRESH — Nothing built yet

  2. HAVE FRONTEND — UI/designs exist, need backend

  3. HAVE BACKEND — API exists, need frontend

  4. HAVE BOTH — Existing project, need help continuing

  5. HAVE DESIGNS — Wireframes/mockups, no code yet

  Reply with: 1, 2, 3, 4, or 5
═══════════════════════════════════════════════════════════
```

**IMPORTANT: Based on answer, guide them appropriately:**

### If STARTING FRESH (1):
```
═══════════════════════════════════════════════════════════
  PERFECT — LET'S BUILD FROM SCRATCH
═══════════════════════════════════════════════════════════

  I'll help you create everything. First, a few quick questions:

  1. What's your project called? (working name is fine)

  2. Who is this for? (e.g., "small business owners", "developers")

  3. What's the ONE main thing it needs to do?

  Answer these and I'll set up your project structure.
═══════════════════════════════════════════════════════════
```

**After they answer, read the activated kit's STRUCTURE.md to scaffold:**
```
═══════════════════════════════════════════════════════════
  SETTING UP YOUR PROJECT
═══════════════════════════════════════════════════════════

  Based on your project type ([kit name]), I'll create:

  📁 USER SPACE/project/
  [Structure from kit's STRUCTURE.md]

  Example structures by kit:

  WEBSITE KIT:
  ├── pages/          ← Page components
  ├── components/     ← Reusable UI
  ├── assets/         ← Images, fonts
  ├── styles/         ← CSS/styling
  └── public/         ← Static files

  SAAS KIT:
  ├── src/app/        ← App routes
  ├── src/api/        ← API routes
  ├── src/components/ ← UI components
  ├── src/lib/        ← Utilities
  └── prisma/         ← Database schema

  API KIT:
  ├── routes/         ← API endpoints
  ├── controllers/    ← Business logic
  ├── models/         ← Data models
  ├── middleware/     ← Auth, validation
  └── tests/          ← API tests

  AUTOMATION KIT:
  ├── workflows/      ← Workflow definitions
  ├── triggers/       ← Event triggers
  ├── actions/        ← Action handlers
  └── config/         ← Configuration

  I'll also fill in your seeds:
  📝 dev-work/seed/PROJECT.md — Your project brief
  📝 dev-work/seed/TECH_STACK.md — Technology choices

  Ready to scaffold? (yes/no)
═══════════════════════════════════════════════════════════
```

**IMPORTANT:** Always read the activated kit's STRUCTURE.md for the actual folder layout.
The kit determines the project structure, not this generic example.

**Then proceed to kit PROMPTER for domain-specific questions.**

### If HAVE FRONTEND (2):
```
═══════════════════════════════════════════════════════════
  GOT IT — YOU HAVE FRONTEND CODE
═══════════════════════════════════════════════════════════

  Please put your frontend files here:

  📁 USER SPACE/dev-work/plug-and-play/frontend/

  Drop your entire frontend folder there, or tell me:
  "My frontend is at /path/to/folder"

  What framework is your frontend? (React, Vue, etc.)
═══════════════════════════════════════════════════════════
```

### If HAVE BACKEND (3):
```
═══════════════════════════════════════════════════════════
  GOT IT — YOU HAVE BACKEND/API
═══════════════════════════════════════════════════════════

  Please put your backend files here:

  📁 USER SPACE/dev-work/plug-and-play/backend/

  Drop your backend folder there, or tell me:
  "My backend is at /path/to/folder"

  Do you have API documentation or an INTERFACES.md?
═══════════════════════════════════════════════════════════
```

### If HAVE BOTH (4):
```
═══════════════════════════════════════════════════════════
  GOT IT — YOU HAVE AN EXISTING PROJECT
═══════════════════════════════════════════════════════════

  Please put your project files here:

  📁 USER SPACE/dev-work/plug-and-play/existing/

  Drop your project folder there, or tell me:
  "My project is at /path/to/folder"

  What do you need help with?
  - Bug fixes
  - New features
  - Refactoring
  - Testing
  - Something else
═══════════════════════════════════════════════════════════
```

### If HAVE DESIGNS (5):
```
═══════════════════════════════════════════════════════════
  GOT IT — YOU HAVE DESIGNS
═══════════════════════════════════════════════════════════

  Please put your design files here:

  📁 USER SPACE/dev-work/plug-and-play/designs/

  Accepted formats:
  - Figma links (paste the URL)
  - Images (PNG, JPG, PDF)
  - Wireframe sketches

  Drop them there and let me know when ready.
═══════════════════════════════════════════════════════════
```

---

## STEP 5: Quick Context

```
═══════════════════════════════════════════════════════════
  QUICK CONTEXT
═══════════════════════════════════════════════════════════

  In 1-2 sentences, what's the core purpose?

  Example: "A landing page for my SaaS that captures emails"
  Example: "An API that processes payments for my app"
  Example: "A dashboard where users manage their projects"

═══════════════════════════════════════════════════════════
```

---

## STEP 6: Confirm & Handoff

```
═══════════════════════════════════════════════════════════
  HERE'S WHAT I KNOW
═══════════════════════════════════════════════════════════

  Mode: [Full Discovery / Quick Start / Lite / Just Build]
  Type: [Website / Web App / API / Automation / Other]
  Starting Point: [Fresh / Have Frontend / Have Backend / etc.]
  Existing Files: [Location if provided]
  Purpose: [Their 1-2 sentence description]

  Kit Activated: [website / saas / api / automation / none]

  Is this correct? (yes/no)
═══════════════════════════════════════════════════════════
```

Then proceed to kit's PROMPTER.md questions.

---

## LEARNING PATH (If they chose "Learn First")

```
═══════════════════════════════════════════════════════════
  OMEGA CONSTITUTION — LEARNING MODE
═══════════════════════════════════════════════════════════

  What would you like to understand?

  1. HOW IT WORKS — The overall system and flow
  2. THE STRUCTURE — Folders and what goes where
  3. KITS — What they are and how they help
  4. MODES — Full/Quick/Lite/Just Build explained
  5. SECURITY — How the system keeps things safe
  6. EVERYTHING — Give me the full tour

  Reply with: 1, 2, 3, 4, 5, or 6
═══════════════════════════════════════════════════════════
```

**Based on answer, explain that topic clearly, then ask:**
"Ready to build something, or want to learn more?"

---

## HELP PATH (If they chose "Get Help")

```
═══════════════════════════════════════════════════════════
  OMEGA CONSTRUCTOR — HELP MODE
═══════════════════════════════════════════════════════════

  What do you need help with?

  Just ask your question and I'll answer it.

  Common questions:
  - "Where do I put my files?"
  - "How do I start a new project?"
  - "What's a kit?"
  - "How do I resume a previous session?"
  - "What if I have existing code?"

═══════════════════════════════════════════════════════════
```

**Answer their question, then ask:**
"Anything else, or ready to build?"

---

## Rules

1. **Always start with Step 1** — Intent detection (Build/Learn/Help)
2. **Never skip Step 4** — Existing work detection + file locations
3. **Tell them WHERE to put files** — Be specific with paths
4. **Confirm understanding** — Show summary before proceeding
5. **One question at a time** — Don't overwhelm
6. **Support learning** — Not everyone wants to build immediately

---

## File Location Quick Reference

| They Have | Put It Here |
|:----------|:------------|
| Frontend code | `USER SPACE/dev-work/plug-and-play/frontend/` |
| Backend code | `USER SPACE/dev-work/plug-and-play/backend/` |
| Full project | `USER SPACE/dev-work/plug-and-play/existing/` |
| Designs | `USER SPACE/dev-work/plug-and-play/designs/` |
| Kits | `USER SPACE/dev-work/plug-and-play/kits/` |
| Other assets | `USER SPACE/dev-work/plug-and-play/` |

---

## Anti-Patterns

- ❌ Asking multiple questions at once
- ❌ Assuming they want to build immediately
- ❌ Not telling them where to put files
- ❌ Skipping the existing work check
- ❌ Ignoring help/learning requests
- ❌ Being vague about file locations

---

*Every user gets the right experience from the first message.*
