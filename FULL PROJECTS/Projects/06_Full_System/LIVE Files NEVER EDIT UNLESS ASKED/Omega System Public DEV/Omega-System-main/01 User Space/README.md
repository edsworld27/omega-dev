# 🏠 User Space

**Your project lives here.**

---

## Structure

```
USER SPACE/
│
├── dev-work/          ← Framework files (don't share)
│   ├── seed/             Project requirements
│   ├── phases/           Phase planning
│   ├── plug-and-play/    Dropped assets
│   ├── docs/             Generated PRD, specs
│   ├── SESSION_CONTEXT.md
│   └── TRACKER.md
│
└── project/           ← Clean deliverable (share this)
    ├── src/              Your code
    ├── tests/            Your tests
    └── README.md         Your readme
```

---

## The Split

| Folder | Purpose | Share? |
|:-------|:--------|:-------|
| `dev-work/` | Omega framework, planning, AI context | ❌ No |
| `project/` | Clean code, ready to deploy | ✅ Yes |

---

## Workflow

```
1. Discovery    → Fill dev-work/seed/ files
2. Planning     → AI generates dev-work/docs/
3. Building     → Code goes in project/
4. Testing      → Tests go in project/tests/
5. Handoff      → Zip project/ and send
```

---

## Why This Split?

**Before:** Everything mixed together, need compiler to separate.

**Now:** Already separated. Just grab `project/` when done.

---

*Omegaly simple.*
