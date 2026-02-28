#!/usr/bin/env python3
import os
import sys
import shutil
import subprocess
from pathlib import Path

# --- THE OMEGA ECOSYSTEM MASTER PUBLISHER ---
# This script ensures true "God-Mode" single-source-of-truth syncing.
# It takes the code from `06_Full_System` inside this Dev Panel, 
# clones the live GitHub repos to a temporary folder, overwrites
# them with your local master copies, and force pushes the updates.

COMMIT_MESSAGE = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Auto-Sync: God-Mode Master Architecture Update"

MAPPINGS = {
    "omega-constitution": ("omega-constitution DEV/Entire_Constitution_Files", "omega-constitution LIVE/Entire_Constitution_Files", "https://github.com/edsworld27/omega-constitution.git"),
    "omega-store": ("omega-store DEV/omega-store-main", "omega-store LIVE/omega-store-main", "https://github.com/edsworld27/omega-store.git"),
    "Omega Claw v1": ("Omega Claw v1 DEV/omega-claw-main", "Omega Claw v1 LIVE/omega-claw-main", "https://github.com/edsworld27/omega-claw.git"),
    "Omega System Public": ("Omega System Public DEV/Omega-System-main", "Omega System Public LIVE/Omega-System-main", "https://github.com/edsworld27/Omega-System.git")
}

DEV_ROOT = Path(os.path.dirname(os.path.abspath(__file__)))
SOURCE_DIR = DEV_ROOT / "06_Full_System"
TMP_DIR = DEV_ROOT / ".tmp_publish"

print("\n🚀 INITIATING OMEGA GOD-MODE ECOSYSTEM PUBLISH 🚀\n")

if TMP_DIR.exists():
    shutil.rmtree(TMP_DIR)
os.makedirs(TMP_DIR)

try:
    for name, (dev_path, live_path, remote_url) in MAPPINGS.items():
        dev_full_path = SOURCE_DIR / "Dev Version (Edit)" / dev_path
        live_full_path = SOURCE_DIR / "LIVE Files NEVER EDIT UNLESS ASKED" / live_path
        
        if not dev_full_path.exists():
            print(f"⚠️  Skipping {name}: Dev directory not found at {dev_full_path}.")
            continue
            
        print(f"🔄 Syncing DEV files to LIVE files for '{name}'...")
        # 0. Sync Dev to Live locally
        if not live_full_path.exists():
            os.makedirs(live_full_path)
            
        rsync_local_cmd = [
            "rsync", "-a", "--delete",
            "--exclude=.git", "--exclude=.DS_Store",
            f"{str(dev_full_path)}/",
            f"{str(live_full_path)}/"
        ]
        subprocess.run(rsync_local_cmd, stdout=subprocess.DEVNULL, check=True)
            
        print(f"🌐 Syncing '{name}' LIVE files to GitHub Remote: {remote_url}...")
        repo_dir = TMP_DIR / name
        
        # 1. Clone the remote repo
        subprocess.run(["git", "clone", "--quiet", remote_url, str(repo_dir)], check=True)
        
        # 2. Rsync the live master copy over the clone (excluding .git)
        # Using rsync to handle sync perfectly, deleting removed files
        rsync_cmd = [
            "rsync", "-a", "--delete",
            "--exclude=.git", "--exclude=.DS_Store",
            f"{str(live_full_path)}/",
            f"{str(repo_dir)}/"
        ]
        subprocess.run(rsync_cmd, stdout=subprocess.DEVNULL, check=True)
        
        # 3. Commit and push
        subprocess.run(["git", "add", "-A"], cwd=repo_dir, check=True)
        
        # Check if there are changes before committing
        status = subprocess.run(["git", "status", "--porcelain"], cwd=repo_dir, capture_output=True, text=True)
        if not status.stdout.strip():
            print(f"✅ No changes detected for {name}. Skipping commit.\n")
            continue
            
        subprocess.run(["git", "commit", "-m", COMMIT_MESSAGE], cwd=repo_dir, stdout=subprocess.DEVNULL, check=True)
        subprocess.run(["git", "push", "--quiet", "origin", "main"], cwd=repo_dir, check=True)
        print(f"🌐 Successfully published {name} to live ecosystem!\n")

    # 4. Finally, push the Dev Panel itself
    print("🧠 Syncing Omega DEV Panel Master Repository...")
    subprocess.run(["git", "add", "-A"], cwd=DEV_ROOT, check=True)
    status = subprocess.run(["git", "status", "--porcelain"], cwd=DEV_ROOT, capture_output=True, text=True)
    if status.stdout.strip():
        subprocess.run(["git", "commit", "-m", COMMIT_MESSAGE], cwd=DEV_ROOT, stdout=subprocess.DEVNULL, check=True)
        subprocess.run(["git", "push", "--quiet", "origin", "main"], cwd=DEV_ROOT, check=True)
        print("🌐 Successfully backed up Omega DEV Panel.")
    else:
        print("✅ DEV Panel is already up to date.")

except Exception as e:
    print(f"\n❌ CRITICAL FAILURE DURING PUBLISH: {e}")
finally:
    # Cleanup temp directory
    if TMP_DIR.exists():
        shutil.rmtree(TMP_DIR)

print("\n🎉 GOD-MODE SYNC COMPLETE. Ecosystem is mathematically aligned. 🎉\n")
