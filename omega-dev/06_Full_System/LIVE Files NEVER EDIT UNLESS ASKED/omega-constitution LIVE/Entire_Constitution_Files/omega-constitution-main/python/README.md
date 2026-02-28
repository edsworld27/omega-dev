# 🐍 Omega Automation Library

This directory contains the self-healing and continuous-monitoring Python scripts that keep the Omega project intact and secure.

> [!IMPORTANT]
> **NO EDITS OR DELETIONS:** This folder is designed to only be added to. Do not mutate or delete existing `.py` files here unless absolutely necessary.

## The Scripts

| Script | Purpose |
|:-------|:--------|
| `omega_daemon.py` | Master script — runs all watchers in background |
| `omega_compiler.py` | Exports clean project to Desktop (strips framework) |
| `auto_changelog.py` | Auto-generates CHANGELOG.md on file changes |
| `auto_security.py` | Scans for secrets (.env, .pem, keys) and locks them |
| `auto_structure.py` | Ensures 4 pillars exist, recreates if missing |
| `auto_help.py` | Generates 00.help.md project map |

## How to Run Everything

1. Open your terminal in the root `Constution V10` folder.
2. Run `python3 CONSTITUTION/python/omega_daemon.py`
3. Enjoy your self-healing, automated, highly-secure workspace.
