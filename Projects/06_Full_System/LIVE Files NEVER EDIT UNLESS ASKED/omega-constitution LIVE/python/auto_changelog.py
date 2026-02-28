import os
import time
from datetime import datetime

# Path definition
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CHANGELOG_FILE = os.path.join(ROOT_DIR, "CHANGELOG.md")

IGNORE_DIRS = {'.git', '.claude', '__pycache__', 'node_modules', '.venv', 'venv'}

def get_file_registry():
    """Returns a dictionary mapping file paths to their last modification time."""
    registry = {}
    for root, dirs, files in os.walk(ROOT_DIR):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith('.')]
        for f in files:
            if f == 'CHANGELOG.md' or f == '00.help.md' or f.startswith('.'):
                continue
            filepath = os.path.join(root, f)
            try:
                registry[filepath] = os.path.getmtime(filepath)
            except Exception:
                pass
    return registry

def append_to_changelog(message):
    """Appends a timestamped message to the CHANGELOG.md file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"- **[{timestamp}]** {message}\n"
    
    if not os.path.exists(CHANGELOG_FILE):
        with open(CHANGELOG_FILE, 'w', encoding='utf-8') as f:
            f.write("# 📜 Project Changelog\n\n> This changelog is automatically maintained by `CONSTITUTION/python/auto_changelog.py`.\n\n")
            
    with open(CHANGELOG_FILE, 'a', encoding='utf-8') as f:
        f.write(entry)

def run_watcher():
    print("⏳ Starting Changelog Watcher...")
    current_registry = get_file_registry()
    
    while True:
        time.sleep(3)
        new_registry = get_file_registry()
        
        # Check for additions and modifications
        for filepath, mtime in new_registry.items():
            if filepath not in current_registry:
                rel_path = os.path.relpath(filepath, ROOT_DIR)
                append_to_changelog(f"Added new file: `{rel_path}`")
            elif mtime > current_registry[filepath]:
                rel_path = os.path.relpath(filepath, ROOT_DIR)
                append_to_changelog(f"Modified file: `{rel_path}`")
                
        # Check for deletions
        for filepath in current_registry.keys():
            if filepath not in new_registry:
                rel_path = os.path.relpath(filepath, ROOT_DIR)
                append_to_changelog(f"Deleted file: `{rel_path}`")
                
        current_registry = new_registry

if __name__ == "__main__":
    run_watcher()
