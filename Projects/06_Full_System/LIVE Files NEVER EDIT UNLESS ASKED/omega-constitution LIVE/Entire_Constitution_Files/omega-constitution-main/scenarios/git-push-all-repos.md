# Scenario: Git Push — All Repos

## Trigger
When the user says any of:
- "push to git"
- "upload to git"
- "commit and push"
- "sync everything"

## Context
The Omega ecosystem spans **multiple Git repositories**. A single "push to git" means **push ALL repos that have changes**, not just the one you're currently working in.

## Repos to Check

| Repo | Local Path | GitHub |
|------|-----------|--------|
| omega-constitution | `~/Documents/Omega Constitution Pack` | https://github.com/edsworld27/omega-constitution |
| omega-claw | `~/Documents/omega-claw` | https://github.com/edsworld27/omega-claw |
| omega-store | https://github.com/edsworld27/omega-store | https://github.com/edsworld27/omega-store |

> [!IMPORTANT]
> Always check `DEV/LINKS.md` for the latest repo list — new repos may be added.

## Procedure

```bash
# 1. Check each repo for changes
cd ~/Documents/Omega\ Constitution\ Pack && git status -s
cd ~/Documents/omega-claw && git status -s

# 2. For each repo WITH changes:
git add -A
git commit -m "descriptive message"
git push

# 3. Report which repos were pushed
```

## Rules
1. **Never skip a repo** — if it has changes, push it
2. **Separate commits** — each repo gets its own commit message
3. **Report back** — tell the user which repos were pushed and which were clean
4. **.env files are gitignored** — never force-add them
