# Omega Automation Library

This directory contains the automation Python scripts that keep your Omega project intact, secure, and properly published.

> [!IMPORTANT]
> **NO EDITS OR DELETIONS:** This folder is designed to only be added to. Do not mutate or delete existing `.py` files here unless absolutely necessary.

---

## Core Scripts

| Script | Purpose |
|:-------|:--------|
| `omega_daemon.py` | Master script — runs all watchers in background |
| `omega_compiler.py` | Exports clean project to Desktop (strips framework) |
| `omega_reporter.py` | Generates status reports |
| `hive_scanner.py` | Scans hive system for jobs |
| `omega_job_watcher.py` | Monitors job queue |

## Auto-Healing Scripts

| Script | Purpose |
|:-------|:--------|
| `auto_changelog.py` | Auto-generates CHANGELOG.md on file changes |
| `auto_security.py` | Scans for secrets (.env, .pem, keys) and locks them |
| `auto_structure.py` | Ensures core structure exists, recreates if missing |
| `auto_help.py` | Generates 00.help.md project map |

---

## Git Publishing Tools

### omega_publish.py

Automated Git publishing with validation, commit standards, and multi-repo support.

**Usage:**
```bash
# Single repo publish
python omega_publish.py "feat: Add new feature"

# With custom config
python omega_publish.py --config publish.config.json "fix: Bug fix"

# Dry run (see what would happen)
python omega_publish.py --dry-run "test: Test message"

# Validate only (no publish)
python omega_publish.py --validate-only
```

**Commit Types:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation
- `refactor:` - Code restructuring
- `test:` - Tests
- `chore:` - Maintenance
- `security:` - Security fixes
- `perf:` - Performance

### Configuration

Copy `publish.config.template.json` to `publish.config.json` and customize:

```json
{
  "repositories": [
    {
      "name": "my-project",
      "local_path": "./",
      "remote_url": "https://github.com/USER/REPO.git",
      "branch": "main"
    }
  ],
  "pre_publish_checks": true
}
```

**Multi-Repo Example:**
```json
{
  "repositories": [
    {"name": "frontend", "local_path": "./frontend", "remote_url": "..."},
    {"name": "backend", "local_path": "./backend", "remote_url": "..."},
    {"name": "docs", "local_path": "./docs", "remote_url": "..."}
  ]
}
```

---

## How to Run Everything

1. Copy scripts to your project
2. Configure `publish.config.json` with your repos
3. Run scripts as needed:
   - `python omega_daemon.py` - Background monitoring
   - `python omega_publish.py "message"` - Publish to GitHub

---

## Protocol Reference

See `GITHUB_PUBLISHING.xml` for full publishing protocol including:
- Commit standards
- Pre-publish checklist
- Branch management
- Release workflows
- Emergency procedures
