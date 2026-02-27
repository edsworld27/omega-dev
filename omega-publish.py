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
    "omega-constitution": "https://github.com/edsworld27/omega-constitution.git",
    "omega-store": "https://github.com/edsworld27/omega-store.git",
    "Omega Claw v1": "https://github.com/edsworld27/omega-claw.git",
    "Omega System Public DEV": "https://github.com/edsworld27/Omega-System.git"
}

DEV_ROOT = Path(os.path.dirname(os.path.abspath(__file__)))
SOURCE_DIR = DEV_ROOT / "06_Full_System"
TMP_DIR = DEV_ROOT / ".tmp_publish"

print("\n🚀 INITIATING OMEGA GOD-MODE ECOSYSTEM PUBLISH 🚀\n")

if TMP_DIR.exists():
    shutil.rmtree(TMP_DIR)
os.makedirs(TMP_DIR)

try:
    for local_folder, remote_url in MAPPINGS.items():
        source_path = SOURCE_DIR / local_folder
        if not source_path.exists():
            print(f"⚠️  Skipping {local_folder}: Source directory not found in 06_Full_System.")
            continue
            
        print(f"🔄 Syncing '{local_folder}' to {remote_url}...")
        repo_dir = TMP_DIR / local_folder
        
        # 1. Clone the remote repo
        subprocess.run(["git", "clone", "--quiet", remote_url, str(repo_dir)], check=True)
        
        # 2. Rsync the local master copy over the clone (excluding .git)
        # Using rsync to handle sync perfectly, deleting removed files
        rsync_cmd = [
            "rsync", "-av", "--delete",
            "--exclude=.git",
            f"{str(source_path)}/",
            f"{str(repo_dir)}/"
        ]
        subprocess.run(rsync_cmd, stdout=subprocess.DEVNULL, check=True)
        
        # 3. Commit and push
        subprocess.run(["git", "add", "-A"], cwd=repo_dir, check=True)
        
        # Check if there are changes before committing
        status = subprocess.run(["git", "status", "--porcelain"], cwd=repo_dir, capture_output=True, text=True)
        if not status.stdout.strip():
            print(f"✅ No changes detected for {local_folder}. Skipping commit.\n")
            continue
            
        subprocess.run(["git", "commit", "-m", COMMIT_MESSAGE], cwd=repo_dir, stdout=subprocess.DEVNULL, check=True)
        subprocess.run(["git", "push", "--quiet", "origin", "main"], cwd=repo_dir, check=True)
        print(f"🌐 Successfully published {local_folder} to live ecosystem!\n")

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
