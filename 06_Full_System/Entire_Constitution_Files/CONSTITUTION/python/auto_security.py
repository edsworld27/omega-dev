import os
import time

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
USER_SPACE = os.path.join(ROOT_DIR, "USER SPACE")

FORBIDDEN_EXTENSIONS = {'.pem', '.key'}
FORBIDDEN_FILES = {'id_rsa', 'id_dsa', '.env'}

def scan_file(filepath):
    filename = os.path.basename(filepath)
    _, ext = os.path.splitext(filename)
    
    if filename in FORBIDDEN_FILES or ext in FORBIDDEN_EXTENSIONS:
        return True
    
    # Try reading content for raw keys
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            if "BEGIN RSA PRIVATE KEY" in content or "AWS_ACCESS_KEY_ID=" in content:
                return True
    except Exception:
        pass
        
    return False

def run_watcher():
    print("🛡️ Starting Security Watcher...")
    while True:
        time.sleep(5)

        if not os.path.exists(PROJECT_DIR):
            continue

        for root, _, files in os.walk(PROJECT_DIR):
            for f in files:
                filepath = os.path.join(root, f)
                if scan_file(filepath):
                    print(f"\n🚨 [SECURITY ALERT] Sensitive data found in: {filepath}")
                    print("🚨 Renaming file to prevent accidental commit.")
                    os.rename(filepath, filepath + ".SECURE_LOCKED")

if __name__ == "__main__":
    run_watcher()
