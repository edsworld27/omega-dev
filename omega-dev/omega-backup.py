#!/usr/bin/env python3
import os
import sys
import shutil
import zipfile
import datetime
from pathlib import Path

# --- THE OMEGA ECOSYSTEM LOCAL BACKUP & UNDO TOOL ---
# This tool provides an "Undo Button" for the Dev Panel.
# It packages the entire local `omega-dev` folder into a zipped snapshot
# (ignoring .git and previous backups) and allows you to instantly
# restore to a previous state if an AI agent or human deletes files.

DEV_ROOT = Path(os.path.dirname(os.path.abspath(__file__)))
BACKUP_DIR = DEV_ROOT / ".dev_backups"
IGNORE_DIRS = {".git", ".dev_backups", "__pycache__", "node_modules", ".tmp_publish"}

def ensure_backup_dir():
    if not BACKUP_DIR.exists():
        os.makedirs(BACKUP_DIR)

def get_ignore_paths(base_path):
    """Returns absolute paths we should never compress or delete."""
    return {str(DEV_ROOT / d) for d in IGNORE_DIRS}

def create_backup(message):
    ensure_backup_dir()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    safe_message = message.replace(' ', '_').replace('/', '-').replace('\\', '-')
    filename = f"omega_snapshot_{timestamp}_{safe_message}.zip"
    zip_path = BACKUP_DIR / filename
    
    print(f"\n📦 Creating Fractal Snapshot: {filename} ...")
    
    ignore_paths = get_ignore_paths(DEV_ROOT)
    
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(DEV_ROOT):
                # We need to filter dirs in-place to prevent os.walk from entering them:
                dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

                for file in files:
                    # Ignore .zip files matching our backup format specifically
                    if file.startswith("omega_snapshot_") and file.endswith(".zip"):
                        continue
                        
                    file_path = Path(root) / file
                    
                    # Safety check for broken symlinks or files that disappeared
                    if not file_path.exists():
                        continue
                        
                    arcname = file_path.relative_to(DEV_ROOT)
                    zipf.write(file_path, arcname)
                    
        print(f"✅ Backup created successfully at: {zip_path.relative_to(DEV_ROOT)}\n")
    except Exception as e:
        print(f"\n❌ Failed to create backup: {e}\n")
        if zip_path.exists():
            os.remove(zip_path)

def list_backups():
    ensure_backup_dir()
    backups = sorted(BACKUP_DIR.glob("*.zip"), key=os.path.getmtime, reverse=True)
    
    if not backups:
        print("\n📭 No backups found. Use 'python3 omega-backup.py save [message]' to create one.\n")
        return []
        
    print("\n🕰️ AVAILABLE OMEGA SNAPSHOTS (Newest First):\n")
    for i, backup in enumerate(backups):
        size_mb = os.path.getsize(backup) / (1024 * 1024)
        print(f"  [{i}] {backup.name} ({size_mb:.2f} MB)")
    print("")
    return backups

def restore_backup(backup_path):
    print(f"\n⚠️ WARNING: This will WIPE the current working directory (excluding .git) and restore from:\n  {backup_path.name}")
    confirm = input("Are you absolutely sure you want to UNDO and OVERWRITE current files? (yes/no): ")
    
    if confirm.lower() not in {"y", "yes"}:
        print("Restoration cancelled.")
        return
        
    ignore_paths = get_ignore_paths(DEV_ROOT)
    
    print("\n🧹 1. Cleaning current directory...")
    for item in os.listdir(DEV_ROOT):
        item_path = DEV_ROOT / item
        if str(item_path) in ignore_paths:
            continue
            
        try:
            if item_path.is_file() or item_path.is_symlink():
                item_path.unlink()
            elif item_path.is_dir():
                shutil.rmtree(item_path)
        except Exception as e:
            print(f"❌ Error deleting {item}: {e}")
            return
            
    print("📦 2. Restoring from snapshot...")
    try:
        with zipfile.ZipFile(backup_path, 'r') as zipf:
            zipf.extractall(DEV_ROOT)
        print(f"✅ System successfully restored to state defined in {backup_path.name}!\n")
    except Exception as e:
        print(f"\n❌ CRITICAL: Failed to extract backup: {e}\n")

def main():
    if len(sys.argv) < 2:
        print("\nUsage:")
        print("  python3 omega-backup.py save [optional_message]   - Creates a new local snapshot")
        print("  python3 omega-backup.py list                      - Lists all local snapshots")
        print("  python3 omega-backup.py undo                      - Interactively restore a past snapshot")
        print("  python3 omega-backup.py undo [index]              - Directly restore snapshot by index\n")
        sys.exit(1)
        
    command = sys.argv[1].lower()
    
    if command == "save":
        message = "Manual_Snapshot"
        if len(sys.argv) > 2:
            message = "_".join(sys.argv[2:])
        create_backup(message)
        
    elif command == "list":
        list_backups()
        
    elif command == "undo":
        backups = list_backups()
        if not backups:
            return
            
        index = -1
        if len(sys.argv) > 2:
            try:
                index = int(sys.argv[2])
            except ValueError:
                print("❌ Invalid index. Please provide a number.")
                return
        else:
            try:
                choice = input("Enter the number of the snapshot to restore (or 'q' to quit): ")
                if choice.lower() == 'q':
                    return
                index = int(choice)
            except ValueError:
                print("❌ Invalid input.")
                return
                
        if 0 <= index < len(backups):
            restore_backup(backups[index])
        else:
            print(f"❌ Index {index} is out of range.")
            
    else:
        print(f"❌ Unknown command: {command}")
        
if __name__ == "__main__":
    main()
