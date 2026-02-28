#!/usr/bin/env python3
"""
HIVE LOCKER - Multi-Agent File Locking System
Omega Constitution V14

Provides distributed file locking for parallel AI agent coordination.
Uses fcntl for OS-level locking + JSON registry for cross-process visibility.

Usage:
    python hive_locker.py lock <filepath> --agent-id ALPHA
    python hive_locker.py unlock <filepath> --agent-id ALPHA
    python hive_locker.py check <filepath> --agent-id ALPHA
    python hive_locker.py status --agent-id ALPHA
    python hive_locker.py heartbeat --agent-id ALPHA
    python hive_locker.py register --agent-id ALPHA [--job-id JOB-001]
    python hive_locker.py deregister --agent-id ALPHA
    python hive_locker.py git-push-lock --agent-id ALPHA
    python hive_locker.py git-push-unlock --agent-id ALPHA
    python hive_locker.py cleanup --agent-id ALPHA
"""

import os
import json
import fcntl
import hashlib
import sys
import argparse
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, Dict, List

# Configuration
HIVE_DIR = os.path.expanduser(
    os.getenv("OMEGA_HIVE_DIR",
              "~/Documents/Omega Constitution Pack/Omega System Public/Constution V13/USER SPACE/dev-work/hive")
)
LOCKS_DIR = os.path.join(HIVE_DIR, "locks")
STATE_DIR = os.path.join(HIVE_DIR, "ai_state")
REGISTRY_FILE = os.path.join(LOCKS_DIR, ".lock_registry.json")
HEARTBEAT_FILE = os.path.join(STATE_DIR, "HEARTBEAT.json")

# Defaults
DEFAULT_LOCK_TIMEOUT = 300  # 5 minutes
GIT_PUSH_TIMEOUT = 60       # 1 minute for git operations
HEARTBEAT_INTERVAL = 60     # 1 minute
STALE_THRESHOLD = 120       # 2 minutes without heartbeat = stale


class HiveLocker:
    """
    Manages distributed file locks for multi-agent coordination.

    Lock file format (JSON):
    {
        "filepath": "/absolute/path/to/file",
        "agent_id": "ALPHA",
        "acquired_at": "2026-02-28T10:30:00Z",
        "expires_at": "2026-02-28T10:35:00Z",
        "heartbeat": "2026-02-28T10:32:00Z",
        "job_id": "FOUNDER_JOB-001-MyProject"
    }
    """

    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self._ensure_dirs()

    def _ensure_dirs(self):
        """Create lock directories if they don't exist."""
        Path(LOCKS_DIR).mkdir(parents=True, exist_ok=True)
        Path(STATE_DIR).mkdir(parents=True, exist_ok=True)

    def _hash_path(self, filepath: str) -> str:
        """Generate a safe filename from filepath hash."""
        abs_path = os.path.abspath(filepath)
        return hashlib.sha256(abs_path.encode()).hexdigest()[:16]

    def _load_registry(self) -> Dict:
        """Load the master lock registry with shared lock."""
        if not os.path.exists(REGISTRY_FILE):
            return {"locks": {}, "last_cleanup": None}

        try:
            with open(REGISTRY_FILE, 'r') as f:
                fcntl.flock(f, fcntl.LOCK_SH)  # Shared lock for reads
                data = json.load(f)
                fcntl.flock(f, fcntl.LOCK_UN)
                return data
        except (json.JSONDecodeError, IOError):
            return {"locks": {}, "last_cleanup": None}

    def _save_registry(self, registry: Dict):
        """Save the master lock registry with exclusive lock."""
        with open(REGISTRY_FILE, 'w') as f:
            fcntl.flock(f, fcntl.LOCK_EX)  # Exclusive lock for writes
            json.dump(registry, f, indent=2)
            f.flush()
            os.fsync(f.fileno())
            fcntl.flock(f, fcntl.LOCK_UN)

    def acquire_lock(self, filepath: str, timeout: int = DEFAULT_LOCK_TIMEOUT,
                     job_id: str = None) -> Dict:
        """
        Attempt to acquire a lock on a file.

        Returns:
            {"success": True/False, "message": str, "lock": dict or None}
        """
        abs_path = os.path.abspath(filepath)
        lock_hash = self._hash_path(abs_path)
        lock_file = os.path.join(LOCKS_DIR, f"{lock_hash}.lock")

        registry = self._load_registry()

        # Check if already locked by another agent
        if lock_hash in registry["locks"]:
            existing = registry["locks"][lock_hash]
            expires = datetime.fromisoformat(existing["expires_at"])

            if datetime.now() < expires and existing["agent_id"] != self.agent_id:
                return {
                    "success": False,
                    "message": f"File locked by {existing['agent_id']} until {existing['expires_at']}",
                    "lock": existing
                }
            # Lock expired or same agent - proceed to re-acquire

        # Create lock entry
        now = datetime.now()
        lock_entry = {
            "filepath": abs_path,
            "agent_id": self.agent_id,
            "acquired_at": now.isoformat(),
            "expires_at": (now + timedelta(seconds=timeout)).isoformat(),
            "heartbeat": now.isoformat(),
            "job_id": job_id
        }

        # Write lock file with fcntl
        try:
            with open(lock_file, 'w') as f:
                fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
                json.dump(lock_entry, f, indent=2)
                fcntl.flock(f, fcntl.LOCK_UN)
        except BlockingIOError:
            return {
                "success": False,
                "message": "Failed to acquire OS-level lock (race condition)",
                "lock": None
            }

        # Update registry
        registry["locks"][lock_hash] = lock_entry
        self._save_registry(registry)

        return {
            "success": True,
            "message": f"Lock acquired on {os.path.basename(abs_path)}",
            "lock": lock_entry
        }

    def release_lock(self, filepath: str, force: bool = False) -> Dict:
        """
        Release a lock on a file.

        Args:
            filepath: Path to the file
            force: If True, release even if owned by another agent
        """
        abs_path = os.path.abspath(filepath)
        lock_hash = self._hash_path(abs_path)
        lock_file = os.path.join(LOCKS_DIR, f"{lock_hash}.lock")

        registry = self._load_registry()

        if lock_hash not in registry["locks"]:
            return {"success": True, "message": "No lock existed"}

        existing = registry["locks"][lock_hash]
        if existing["agent_id"] != self.agent_id and not force:
            return {
                "success": False,
                "message": f"Lock owned by {existing['agent_id']}, not {self.agent_id}. Use --force to override."
            }

        # Remove lock file
        if os.path.exists(lock_file):
            os.remove(lock_file)

        # Update registry
        del registry["locks"][lock_hash]
        self._save_registry(registry)

        return {"success": True, "message": f"Lock released on {os.path.basename(abs_path)}"}

    def check_lock(self, filepath: str) -> Dict:
        """Check if a file is locked and by whom."""
        abs_path = os.path.abspath(filepath)
        lock_hash = self._hash_path(abs_path)

        registry = self._load_registry()

        if lock_hash in registry["locks"]:
            lock = registry["locks"][lock_hash]
            expires = datetime.fromisoformat(lock["expires_at"])

            if datetime.now() < expires:
                return {
                    "locked": True,
                    "agent_id": lock["agent_id"],
                    "owned_by_me": lock["agent_id"] == self.agent_id,
                    "expires_at": lock["expires_at"],
                    "lock": lock
                }

        return {"locked": False, "agent_id": None, "owned_by_me": False}

    def get_status(self) -> Dict:
        """Get all active locks."""
        registry = self._load_registry()
        now = datetime.now()

        active = {}
        expired = []

        for lock_hash, lock in registry["locks"].items():
            expires = datetime.fromisoformat(lock["expires_at"])
            if now < expires:
                active[lock_hash] = lock
            else:
                expired.append(lock_hash)

        return {
            "active_locks": list(active.values()),
            "expired_count": len(expired),
            "my_locks": [l for l in active.values() if l["agent_id"] == self.agent_id],
            "total_agents": len(set(l["agent_id"] for l in active.values()))
        }

    def send_heartbeat(self) -> Dict:
        """Update heartbeat for this agent."""
        # Update all locks owned by this agent
        registry = self._load_registry()
        now = datetime.now()
        updated = 0

        for lock_hash, lock in registry["locks"].items():
            if lock["agent_id"] == self.agent_id:
                lock["heartbeat"] = now.isoformat()
                # Also extend expiry by default timeout
                lock["expires_at"] = (now + timedelta(seconds=DEFAULT_LOCK_TIMEOUT)).isoformat()
                updated += 1

        self._save_registry(registry)

        # Update agent heartbeat file
        heartbeats = {}
        if os.path.exists(HEARTBEAT_FILE):
            try:
                with open(HEARTBEAT_FILE, 'r') as f:
                    heartbeats = json.load(f)
            except:
                pass

        heartbeats[self.agent_id] = {
            "last_seen": now.isoformat(),
            "locks_held": updated
        }

        with open(HEARTBEAT_FILE, 'w') as f:
            json.dump(heartbeats, f, indent=2)

        return {"success": True, "locks_refreshed": updated}

    def cleanup_stale(self) -> Dict:
        """Remove all expired locks."""
        registry = self._load_registry()
        now = datetime.now()
        removed = []

        for lock_hash, lock in list(registry["locks"].items()):
            expires = datetime.fromisoformat(lock["expires_at"])
            if now >= expires:
                # Remove lock file
                lock_file = os.path.join(LOCKS_DIR, f"{lock_hash}.lock")
                if os.path.exists(lock_file):
                    os.remove(lock_file)
                removed.append(lock["filepath"])
                del registry["locks"][lock_hash]

        registry["last_cleanup"] = now.isoformat()
        self._save_registry(registry)

        return {"success": True, "removed": removed, "count": len(removed)}

    def register_agent(self, job_id: str = None) -> Dict:
        """Register this agent as active in the hive."""
        agent_file = os.path.join(STATE_DIR, f"AGENT-{self.agent_id}.md")
        now = datetime.now()

        content = f"""# Agent Registration: {self.agent_id}

**Registered**: {now.isoformat()}
**Status**: ACTIVE
**Current Job**: {job_id or 'None'}
**Last Heartbeat**: {now.isoformat()}

## Session Info
- **Started**: {now.strftime('%Y-%m-%d %H:%M:%S')}
- **Branch**: agent-{self.agent_id.lower()}

## Active Locks
(Updated by heartbeat)

---
*Auto-generated by hive_locker.py*
"""

        with open(agent_file, 'w') as f:
            f.write(content)

        # Also update heartbeat registry
        heartbeats = {}
        if os.path.exists(HEARTBEAT_FILE):
            try:
                with open(HEARTBEAT_FILE, 'r') as f:
                    heartbeats = json.load(f)
            except:
                pass

        heartbeats[self.agent_id] = {
            "last_seen": now.isoformat(),
            "locks_held": 0,
            "job_id": job_id,
            "status": "ACTIVE"
        }

        with open(HEARTBEAT_FILE, 'w') as f:
            json.dump(heartbeats, f, indent=2)

        return {"success": True, "agent_file": agent_file, "message": f"Agent {self.agent_id} registered"}

    def deregister_agent(self) -> Dict:
        """Deregister this agent and release all locks."""
        # Release all locks held by this agent
        registry = self._load_registry()
        released = []

        for lock_hash, lock in list(registry["locks"].items()):
            if lock["agent_id"] == self.agent_id:
                lock_file = os.path.join(LOCKS_DIR, f"{lock_hash}.lock")
                if os.path.exists(lock_file):
                    os.remove(lock_file)
                released.append(lock["filepath"])
                del registry["locks"][lock_hash]

        self._save_registry(registry)

        # Update agent file
        agent_file = os.path.join(STATE_DIR, f"AGENT-{self.agent_id}.md")
        now = datetime.now()

        if os.path.exists(agent_file):
            with open(agent_file, 'a') as f:
                f.write(f"\n**Deregistered**: {now.isoformat()}\n")
                f.write(f"**Status**: INACTIVE\n")
                f.write(f"**Locks Released**: {len(released)}\n")

        # Update heartbeat registry
        heartbeats = {}
        if os.path.exists(HEARTBEAT_FILE):
            try:
                with open(HEARTBEAT_FILE, 'r') as f:
                    heartbeats = json.load(f)
            except:
                pass

        if self.agent_id in heartbeats:
            heartbeats[self.agent_id]["status"] = "INACTIVE"
            heartbeats[self.agent_id]["deregistered"] = now.isoformat()

        with open(HEARTBEAT_FILE, 'w') as f:
            json.dump(heartbeats, f, indent=2)

        return {"success": True, "released": released, "message": f"Agent {self.agent_id} deregistered, {len(released)} locks released"}


class GitPushLock:
    """Special lock for coordinating git push operations."""

    LOCK_FILE = os.path.join(LOCKS_DIR, "GIT_PUSH.lock")

    @classmethod
    def acquire(cls, agent_id: str, timeout: int = GIT_PUSH_TIMEOUT) -> Dict:
        """Acquire the git push lock."""
        Path(LOCKS_DIR).mkdir(parents=True, exist_ok=True)

        if os.path.exists(cls.LOCK_FILE):
            try:
                with open(cls.LOCK_FILE, 'r') as f:
                    existing = json.load(f)
                expires = datetime.fromisoformat(existing["expires_at"])
                if datetime.now() < expires:
                    return {
                        "success": False,
                        "message": f"Git push locked by {existing['agent_id']} until {existing['expires_at']}"
                    }
            except:
                pass  # Corrupted lock file, proceed to overwrite

        now = datetime.now()
        lock_data = {
            "agent_id": agent_id,
            "acquired_at": now.isoformat(),
            "expires_at": (now + timedelta(seconds=timeout)).isoformat()
        }

        try:
            with open(cls.LOCK_FILE, 'w') as f:
                fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
                json.dump(lock_data, f, indent=2)
                fcntl.flock(f, fcntl.LOCK_UN)
        except BlockingIOError:
            return {
                "success": False,
                "message": "Failed to acquire git push lock (race condition)"
            }

        return {"success": True, "message": f"Git push lock acquired by {agent_id}"}

    @classmethod
    def release(cls, agent_id: str) -> Dict:
        """Release the git push lock."""
        if os.path.exists(cls.LOCK_FILE):
            try:
                with open(cls.LOCK_FILE, 'r') as f:
                    existing = json.load(f)
                # Only release if we own it (or it's expired)
                if existing.get("agent_id") != agent_id:
                    expires = datetime.fromisoformat(existing["expires_at"])
                    if datetime.now() < expires:
                        return {
                            "success": False,
                            "message": f"Git push lock owned by {existing['agent_id']}, not {agent_id}"
                        }
            except:
                pass  # Corrupted, safe to remove

            os.remove(cls.LOCK_FILE)

        return {"success": True, "message": "Git push lock released"}

    @classmethod
    def check(cls) -> Dict:
        """Check if git push is locked."""
        if not os.path.exists(cls.LOCK_FILE):
            return {"locked": False, "agent_id": None}

        try:
            with open(cls.LOCK_FILE, 'r') as f:
                existing = json.load(f)
            expires = datetime.fromisoformat(existing["expires_at"])
            if datetime.now() < expires:
                return {
                    "locked": True,
                    "agent_id": existing["agent_id"],
                    "expires_at": existing["expires_at"]
                }
        except:
            pass

        return {"locked": False, "agent_id": None}


def format_output(result: Dict, json_output: bool = False) -> str:
    """Format result for display."""
    if json_output:
        return json.dumps(result, indent=2)

    if "message" in result:
        return result["message"]

    return json.dumps(result, indent=2)


# CLI Interface
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Omega Hive File Locker - Multi-Agent Coordination",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python hive_locker.py register --agent-id ALPHA
  python hive_locker.py lock /path/to/file.py --agent-id ALPHA
  python hive_locker.py check /path/to/file.py --agent-id ALPHA
  python hive_locker.py unlock /path/to/file.py --agent-id ALPHA
  python hive_locker.py status --agent-id ALPHA
  python hive_locker.py deregister --agent-id ALPHA
        """
    )

    parser.add_argument("command", choices=[
        "lock", "unlock", "check", "status", "heartbeat",
        "cleanup", "register", "deregister",
        "git-push-lock", "git-push-unlock", "git-push-check"
    ], help="Command to execute")

    parser.add_argument("filepath", nargs="?", help="File path for lock operations")
    parser.add_argument("--agent-id", required=True, help="Agent identifier (e.g., ALPHA, BRAVO)")
    parser.add_argument("--timeout", type=int, default=DEFAULT_LOCK_TIMEOUT,
                        help=f"Lock timeout in seconds (default: {DEFAULT_LOCK_TIMEOUT})")
    parser.add_argument("--job-id", help="Associated job ID for tracking")
    parser.add_argument("--force", action="store_true", help="Force operation (use with caution)")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")

    args = parser.parse_args()

    # Validate filepath requirement
    if args.command in ["lock", "unlock", "check"] and not args.filepath:
        parser.error(f"Command '{args.command}' requires a filepath")

    locker = HiveLocker(args.agent_id)
    result = {}

    if args.command == "lock":
        result = locker.acquire_lock(args.filepath, args.timeout, args.job_id)
    elif args.command == "unlock":
        result = locker.release_lock(args.filepath, args.force)
    elif args.command == "check":
        result = locker.check_lock(args.filepath)
    elif args.command == "status":
        result = locker.get_status()
    elif args.command == "heartbeat":
        result = locker.send_heartbeat()
    elif args.command == "cleanup":
        result = locker.cleanup_stale()
    elif args.command == "register":
        result = locker.register_agent(args.job_id)
    elif args.command == "deregister":
        result = locker.deregister_agent()
    elif args.command == "git-push-lock":
        result = GitPushLock.acquire(args.agent_id, args.timeout)
    elif args.command == "git-push-unlock":
        result = GitPushLock.release(args.agent_id)
    elif args.command == "git-push-check":
        result = GitPushLock.check()

    print(format_output(result, args.json))

    # Exit code based on success
    if "success" in result:
        sys.exit(0 if result["success"] else 1)
    elif "locked" in result:
        # For check commands, return 0 if not locked, 1 if locked
        sys.exit(0 if not result["locked"] else 1)
    else:
        sys.exit(0)
