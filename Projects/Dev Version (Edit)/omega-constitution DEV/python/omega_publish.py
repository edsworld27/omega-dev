#!/usr/bin/env python3
"""
OMEGA PUBLISH - Git Publishing Automation
==========================================
Part of the Omega Constitution framework.

This script automates Git publishing workflows including:
- Single repo publishing
- Multi-repo sync (for monorepo or decoupled architectures)
- Pre-publish validation
- Commit standardization

USAGE:
    python omega_publish.py "Your commit message"
    python omega_publish.py --config publish.config.json "Message"
    python omega_publish.py --dry-run "Test message"
    python omega_publish.py --validate-only

CONFIGURATION:
    Create a publish.config.json in your project root:
    {
        "repositories": [
            {
                "name": "my-project",
                "local_path": "./src",
                "remote_url": "https://github.com/user/repo.git",
                "branch": "main"
            }
        ],
        "pre_publish_checks": true,
        "auto_tag": false
    }

    Or run without config for single-repo mode (uses current directory).
"""

import os
import sys
import json
import shutil
import subprocess
import argparse
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict


# =============================================================================
# CONFIGURATION
# =============================================================================

DEFAULT_CONFIG = {
    "repositories": [],
    "pre_publish_checks": True,
    "auto_tag": False,
    "commit_types": [
        "feat", "fix", "docs", "style", "refactor",
        "test", "chore", "security", "perf"
    ],
    "forbidden_patterns": [
        "API_KEY", "SECRET", "PASSWORD", "TOKEN",
        "PRIVATE_KEY", "aws_access_key"
    ]
}


# =============================================================================
# VALIDATION
# =============================================================================

def validate_commit_message(message: str, commit_types: List[str]) -> tuple[bool, str]:
    """Validate commit message format."""
    if not message or len(message.strip()) < 3:
        return False, "Commit message is too short"

    # Check for type prefix
    has_type = any(message.lower().startswith(f"{t}:") for t in commit_types)
    if not has_type:
        valid_types = ", ".join(commit_types)
        return False, f"Commit message should start with a type prefix: {valid_types}"

    # Check first line length
    first_line = message.split("\n")[0]
    if len(first_line) > 72:
        return False, f"First line is {len(first_line)} chars (max 72)"

    return True, "Valid"


def check_for_secrets(path: Path, patterns: List[str]) -> List[str]:
    """Scan files for potential secrets."""
    findings = []

    # File extensions to check
    check_extensions = {'.py', '.js', '.ts', '.json', '.yml', '.yaml', '.env', '.md', '.txt'}

    for file_path in path.rglob('*'):
        if not file_path.is_file():
            continue
        if file_path.suffix not in check_extensions:
            continue
        if '.git' in str(file_path):
            continue

        try:
            content = file_path.read_text(errors='ignore')
            for pattern in patterns:
                if pattern.lower() in content.lower():
                    # Skip if it's just documentation about the pattern
                    if f"# {pattern}" in content or f"// {pattern}" in content:
                        continue
                    findings.append(f"{file_path}: Potential secret pattern '{pattern}'")
        except Exception:
            pass

    return findings


def check_staged_files() -> List[str]:
    """Get list of staged files."""
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        capture_output=True, text=True
    )
    return [f for f in result.stdout.strip().split("\n") if f]


def run_pre_publish_checks(config: Dict, verbose: bool = True) -> tuple[bool, List[str]]:
    """Run pre-publish validation checks."""
    issues = []

    if verbose:
        print("\n🔍 Running pre-publish checks...")

    # Check for secrets in staged files
    if verbose:
        print("   Checking for secrets...")

    cwd = Path.cwd()
    secret_findings = check_for_secrets(cwd, config.get("forbidden_patterns", []))
    if secret_findings:
        issues.extend(secret_findings)

    # Check .gitignore exists
    if not (cwd / ".gitignore").exists():
        issues.append("Warning: No .gitignore file found")

    # Check for common mistakes in staged files
    staged = check_staged_files()
    for file in staged:
        if file == ".env" or file.endswith(".env.local"):
            issues.append(f"CRITICAL: Environment file staged: {file}")
        if file == "credentials.json" or "secret" in file.lower():
            issues.append(f"CRITICAL: Potentially sensitive file staged: {file}")
        if file.endswith(".pem") or file.endswith(".key"):
            issues.append(f"CRITICAL: Key file staged: {file}")

    if verbose:
        if issues:
            print(f"   ⚠️  Found {len(issues)} issue(s)")
            for issue in issues:
                print(f"      - {issue}")
        else:
            print("   ✅ All checks passed")

    # CRITICAL issues block publishing
    has_critical = any("CRITICAL" in issue for issue in issues)
    return not has_critical, issues


# =============================================================================
# GIT OPERATIONS
# =============================================================================

def git_status() -> str:
    """Get git status."""
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        capture_output=True, text=True
    )
    return result.stdout.strip()


def git_add_all():
    """Stage all changes."""
    subprocess.run(["git", "add", "-A"], check=True)


def git_commit(message: str) -> bool:
    """Create a commit."""
    result = subprocess.run(
        ["git", "commit", "-m", message],
        capture_output=True, text=True
    )
    return result.returncode == 0


def git_push(branch: str = "main", remote: str = "origin") -> bool:
    """Push to remote."""
    result = subprocess.run(
        ["git", "push", remote, branch],
        capture_output=True, text=True
    )
    return result.returncode == 0


def git_tag(version: str, message: Optional[str] = None):
    """Create a git tag."""
    if message:
        subprocess.run(["git", "tag", "-a", version, "-m", message], check=True)
    else:
        subprocess.run(["git", "tag", version], check=True)


# =============================================================================
# MULTI-REPO SYNC
# =============================================================================

def sync_repositories(config: Dict, commit_message: str, dry_run: bool = False) -> bool:
    """Sync multiple repositories from config."""
    repos = config.get("repositories", [])

    if not repos:
        print("No repositories configured. Running in single-repo mode.")
        return publish_single_repo(commit_message, config, dry_run)

    print(f"\n🚀 OMEGA MULTI-REPO PUBLISH")
    print(f"   Syncing {len(repos)} repository(ies)...\n")

    success_count = 0

    for repo in repos:
        name = repo.get("name", "unnamed")
        local_path = Path(repo.get("local_path", "."))
        branch = repo.get("branch", "main")

        print(f"📦 Processing: {name}")

        if not local_path.exists():
            print(f"   ⚠️  Path not found: {local_path}")
            continue

        if dry_run:
            print(f"   [DRY RUN] Would publish {local_path} to {branch}")
            success_count += 1
            continue

        # Change to repo directory
        original_dir = os.getcwd()
        os.chdir(local_path)

        try:
            # Stage, commit, push
            git_add_all()

            status = git_status()
            if not status:
                print(f"   ✅ No changes to commit")
                success_count += 1
                continue

            if git_commit(commit_message):
                if git_push(branch):
                    print(f"   ✅ Published successfully")
                    success_count += 1
                else:
                    print(f"   ❌ Push failed")
            else:
                print(f"   ❌ Commit failed")
        finally:
            os.chdir(original_dir)

    print(f"\n{'='*50}")
    print(f"✅ Successfully published: {success_count}/{len(repos)}")

    return success_count == len(repos)


def publish_single_repo(commit_message: str, config: Dict, dry_run: bool = False) -> bool:
    """Publish current directory as single repo."""
    print("\n🚀 OMEGA SINGLE-REPO PUBLISH\n")

    # Run checks
    if config.get("pre_publish_checks", True):
        passed, issues = run_pre_publish_checks(config)
        if not passed:
            print("\n❌ Pre-publish checks failed. Aborting.")
            return False

    if dry_run:
        print("[DRY RUN] Would stage, commit, and push changes")
        return True

    # Stage all changes
    print("📦 Staging changes...")
    git_add_all()

    # Check for changes
    status = git_status()
    if not status:
        print("✅ No changes to commit")
        return True

    # Commit
    print(f"💾 Committing: {commit_message}")
    if not git_commit(commit_message):
        print("❌ Commit failed")
        return False

    # Push
    print("🌐 Pushing to remote...")
    if not git_push():
        print("❌ Push failed")
        return False

    print("\n✅ Published successfully!")
    return True


# =============================================================================
# MAIN
# =============================================================================

def load_config(config_path: Optional[str] = None) -> Dict:
    """Load configuration from file or use defaults."""
    config = DEFAULT_CONFIG.copy()

    # Try to load from specified path or default locations
    paths_to_try = []
    if config_path:
        paths_to_try.append(Path(config_path))
    paths_to_try.extend([
        Path("publish.config.json"),
        Path(".omega/publish.config.json"),
        Path.home() / ".omega" / "publish.config.json"
    ])

    for path in paths_to_try:
        if path.exists():
            try:
                with open(path) as f:
                    user_config = json.load(f)
                    config.update(user_config)
                    print(f"📄 Loaded config from: {path}")
                    break
            except Exception as e:
                print(f"⚠️  Error loading {path}: {e}")

    return config


def main():
    parser = argparse.ArgumentParser(
        description="Omega Publish - Git publishing automation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("message", nargs="?", default="", help="Commit message")
    parser.add_argument("--config", "-c", help="Path to config file")
    parser.add_argument("--dry-run", "-n", action="store_true", help="Show what would be done")
    parser.add_argument("--validate-only", "-v", action="store_true", help="Only run validation")
    parser.add_argument("--skip-checks", action="store_true", help="Skip pre-publish checks")

    args = parser.parse_args()

    # Load config
    config = load_config(args.config)

    if args.skip_checks:
        config["pre_publish_checks"] = False

    # Validate only mode
    if args.validate_only:
        passed, issues = run_pre_publish_checks(config, verbose=True)
        sys.exit(0 if passed else 1)

    # Need commit message for actual publish
    if not args.message:
        print("❌ Error: Commit message required")
        print("Usage: python omega_publish.py \"Your commit message\"")
        sys.exit(1)

    # Validate commit message
    valid, error = validate_commit_message(args.message, config.get("commit_types", []))
    if not valid:
        print(f"❌ Invalid commit message: {error}")
        print("Example: feat: Add new user authentication")
        sys.exit(1)

    # Run publish
    if config.get("repositories"):
        success = sync_repositories(config, args.message, args.dry_run)
    else:
        success = publish_single_repo(args.message, config, args.dry_run)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
