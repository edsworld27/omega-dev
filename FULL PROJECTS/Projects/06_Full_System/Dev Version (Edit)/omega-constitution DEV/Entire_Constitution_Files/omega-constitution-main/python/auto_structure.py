import os
import time

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

REQUIRED_FOLDERS = [
    "START HERE",
    "CONSTITUTION",
    "USER SPACE",
    "STORE"
]

def run_watcher():
    print("🏛️ Starting Structural Integrity Watcher...")
    while True:
        time.sleep(10)
        
        for folder in REQUIRED_FOLDERS:
            folder_path = os.path.join(ROOT_DIR, folder)
            if not os.path.exists(folder_path):
                print(f"⚠️ [STRUCTURE ALERT] Critical folder '{folder}' is missing. Recreating...")
                os.makedirs(folder_path, exist_ok=True)
                
                # Check if it was STORE and add the README back
                if folder == "STORE":
                    readme_path = os.path.join(folder_path, "README.md")
                    with open(readme_path, 'w', encoding='utf-8') as f:
                        f.write("# 🏪 Omega Store\n\nThe actual store is in the separate `omega-store` repo.")

if __name__ == "__main__":
    run_watcher()
