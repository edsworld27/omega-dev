import subprocess
import os
import sys
import time

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PYTHON_LIB_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT = os.path.dirname(ROOT_DIR)

# List of scripts to run continuously
WATCHERS = [
    os.path.join(PYTHON_LIB_DIR, "auto_changelog.py"),
    os.path.join(PYTHON_LIB_DIR, "auto_security.py"),
    os.path.join(PYTHON_LIB_DIR, "auto_structure.py"),
    os.path.join(PYTHON_LIB_DIR, "auto_help.py"),
    os.path.join(PYTHON_LIB_DIR, "omega_reporter.py"),
    os.path.join(PYTHON_LIB_DIR, "omega_job_watcher.py")
]

def main():
    print("========================================")
    print("🚀 OMEGA MASTER DAEMON INITIALIZING...")
    print("========================================")
    
    processes = []
    
    for script_path in WATCHERS:
        if os.path.exists(script_path):
            print(f"✅ Booting: {os.path.basename(script_path)}")
            # Spawn each script in the background
            p = subprocess.Popen([sys.executable, script_path])
            processes.append(p)
        else:
            print(f"❌ Could not find: {script_path}")
            
    print("\n[DAEMON] All Watchers Active. Press Ctrl+C to terminate the entire suite.")
    
    try:
        # Keep the main thread alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n🛑 SHUTTING DOWN OMEGA MASTER DAEMON...")
        for p in processes:
            p.terminate()
            p.wait()
        print("🛑 All sub-processes safely terminated.")

if __name__ == "__main__":
    main()
