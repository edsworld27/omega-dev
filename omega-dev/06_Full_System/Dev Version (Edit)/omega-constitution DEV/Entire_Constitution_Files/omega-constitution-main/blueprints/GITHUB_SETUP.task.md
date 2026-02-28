# GITHUB SETUP TASK

**Task ID:** GITHUB_SETUP
**Phase:** Preproduction
**Duration:** 5-10 minutes
**Dependencies:** None

---

## Objective

Configure Git version control and GitHub publishing for this project.

---

## Prerequisites

- [ ] GitHub account exists
- [ ] Repository created (or will create)
- [ ] Git installed locally

---

## Steps

### Step 1: Gather Information

Ask the user:

```
═══════════════════════════════════════════════════════════
  GITHUB REPOSITORY SETUP
═══════════════════════════════════════════════════════════

  Please provide your repository details:

  1. Repository URL:
     Example: https://github.com/username/my-project.git

  2. Default branch (usually "main"):

  3. Is this a new repo or existing?
     - NEW: I'll help you initialize
     - EXISTING: Already has commits
═══════════════════════════════════════════════════════════
```

### Step 2: Create Configuration

Create `publish.config.json` in project root:

```json
{
  "repositories": [
    {
      "name": "PROJECT_NAME",
      "local_path": "./",
      "remote_url": "REPO_URL",
      "branch": "BRANCH_NAME"
    }
  ],
  "pre_publish_checks": true,
  "auto_tag": false,
  "commit_types": [
    "feat", "fix", "docs", "style", "refactor",
    "test", "chore", "security", "perf"
  ],
  "forbidden_patterns": [
    "API_KEY", "SECRET", "PASSWORD", "TOKEN",
    "PRIVATE_KEY", "aws_access_key"
  ]
}
```

### Step 3: Create .gitignore

Create `.gitignore` with standard entries:

```gitignore
# Dependencies
node_modules/
vendor/
.venv/
__pycache__/
*.pyc

# Build outputs
dist/
build/
*.egg-info/

# Environment & Secrets
.env
.env.local
.env.*.local
*.pem
*.key
credentials.json

# IDE & Editor
.idea/
.vscode/
*.swp
*~

# OS Files
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Testing
coverage/
.coverage
.pytest_cache/

# Temporary
tmp/
temp/
*.tmp
```

### Step 4: Initialize Git (If New Repo)

If this is a new repository:

```bash
git init
git add .
git commit -m "chore: Initial project setup"
git branch -M main
git remote add origin REPO_URL
git push -u origin main
```

### Step 5: Verify Setup

Run validation:

```bash
python python/omega_publish.py --validate-only
```

Expected output:
```
📄 Loaded config from: publish.config.json
🔍 Running pre-publish checks...
   Checking for secrets...
   ✅ All checks passed
```

---

## Output Artifacts

| File | Purpose |
|------|---------|
| `publish.config.json` | Publishing configuration |
| `.gitignore` | Files to exclude from Git |

---

## Usage Instructions

After setup, publish with:

```bash
# Standard publish
python python/omega_publish.py "feat: Add new feature"

# Dry run (preview)
python python/omega_publish.py --dry-run "test: Preview"

# Validate only
python python/omega_publish.py --validate-only
```

### Commit Types

| Type | Use For |
|------|---------|
| `feat:` | New features |
| `fix:` | Bug fixes |
| `docs:` | Documentation |
| `style:` | Formatting |
| `refactor:` | Code restructuring |
| `test:` | Adding tests |
| `chore:` | Maintenance |
| `security:` | Security fixes |
| `perf:` | Performance |

---

## Troubleshooting

### "Permission denied"
- Check SSH keys or use HTTPS with token
- Run: `git remote set-url origin https://github.com/USER/REPO.git`

### "Repository not found"
- Verify the URL is correct
- Check if repo is private and you have access

### "Pre-publish checks failed"
- Review the warnings
- Fix any CRITICAL issues before publishing
- Use `--skip-checks` only if you're certain

---

## Multi-Repo Setup (Advanced)

For projects with multiple repositories:

```json
{
  "repositories": [
    {
      "name": "frontend",
      "local_path": "./frontend",
      "remote_url": "https://github.com/user/frontend.git",
      "branch": "main"
    },
    {
      "name": "backend",
      "local_path": "./backend",
      "remote_url": "https://github.com/user/backend.git",
      "branch": "main"
    }
  ]
}
```

---

## Completion Checklist

- [ ] Repository URL provided
- [ ] publish.config.json created
- [ ] .gitignore created
- [ ] Git initialized (if new)
- [ ] Remote origin configured
- [ ] Validation passed
- [ ] Test publish successful (optional)

---

*Task complete when all checklist items are done.*
