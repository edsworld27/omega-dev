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

import xml.etree.ElementTree as ET

DEV_PANEL = Path(os.path.dirname(os.path.abspath(__file__)))
DEV_ROOT = DEV_PANEL.parent
SOURCE_DIR = DEV_ROOT / "Projects" / "06_Full_System" / "LIVE Files NEVER EDIT UNLESS ASKED"
TMP_DIR = DEV_PANEL / ".tmp_publish"

print("\n🚀 INITIATING OMEGA GOD-MODE ECOSYSTEM PUBLISH 🚀\n")

if TMP_DIR.exists():
    shutil.rmtree(TMP_DIR)
os.makedirs(TMP_DIR)

try:
    # Discover XML project pointers
    xml_files = [f for f in os.listdir(SOURCE_DIR) if f.endswith(".xml")]
    if not xml_files:
        print(f"⚠️  No XML project pointers found in {SOURCE_DIR}")
    
    for xml_file in xml_files:
        xml_path = SOURCE_DIR / xml_file
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        project_name = root.get("name") or xml_file.replace(".xml", "")
        remote_url = root.find("repository").get("url")
        source_rel_path = root.find("source_path").text
        
        # Calculate absolute source path
        if source_rel_path == ".":
            source_path = DEV_ROOT
        else:
            source_path = DEV_ROOT / source_rel_path
            
        if not source_path.exists():
            print(f"⚠️  Skipping {project_name}: Source path {source_path} not found.")
            continue
            
        print(f"🔄 Syncing '{project_name}' to {remote_url}...")
        repo_dir = TMP_DIR / project_name
        
        # 1. Clone the remote repo
        subprocess.run(["git", "clone", "--quiet", remote_url, str(repo_dir)], check=True)
        
        # 2. Rsync the local master copy over the clone (excluding .git)
        rsync_cmd = [
            "rsync", "-av", "--delete",
            "--exclude=.git",
            "--exclude=node_modules",
            "--exclude=.tmp_publish",
            f"{str(source_path)}/",
            f"{str(repo_dir)}/"
        ]
        subprocess.run(rsync_cmd, stdout=subprocess.DEVNULL, check=True)
        
        # 3. Commit and push
        subprocess.run(["git", "add", "-A"], cwd=repo_dir, check=True)
        
        # Check if there are changes before committing
        status = subprocess.run(["git", "status", "--porcelain"], cwd=repo_dir, capture_output=True, text=True)
        if not status.stdout.strip():
            print(f"✅ No changes detected for {project_name}. Skipping commit.\n")
            continue
            
        subprocess.run(["git", "commit", "-m", COMMIT_MESSAGE], cwd=repo_dir, stdout=subprocess.DEVNULL, check=True)
        subprocess.run(["git", "push", "--quiet", "origin", "main"], cwd=repo_dir, check=True)
        print(f"🌐 Successfully published {project_name} to live ecosystem!\n")

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
