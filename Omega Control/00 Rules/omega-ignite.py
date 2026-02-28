import subprocess
import time
import sys
import os

def ignite():
    print("🔥 OMEGA JARVIS IGNITION SEQUENCE STARTING...")
    
    # 1. Start Python Bridge API
    print("⚡ Starting Bridge API (FastAPI)...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    workspace_root = os.path.abspath(os.path.join(script_dir, "../../"))
    jarvis_root = os.path.join(workspace_root, "Projects/Dev Version (Edit)/Omega Claw v1 DEV/jarvis")
    
    bridge_proc = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "main:app", "--port", "8000", "--reload"],
        cwd=os.path.join(jarvis_root, "bridge-api")
    )
    
    # 2. Start Next.js Frontend
    print("💎 Starting Next.js Dashboard...")
    frontend_proc = subprocess.Popen(
        ["npm", "run", "dev"],
        cwd=os.path.join(jarvis_root, "dashboard-next")
    )
    
    # 3. Start Omega Backup Watcher (5-min pulse)
    print("🛡️  Starting Omega Backup Watcher...")
    backup_proc = subprocess.Popen(
        [sys.executable, "omega-backup.py", "watch"]
    )
    
    print("\n✅ ECOSYSTEM IGNITED.")
    print("🔗 API: http://localhost:8000")
    print("🔗 DASHBOARD: http://localhost:3000")
    print("\nPress Ctrl+C to shutdown both services.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 SHUTTING DOWN...")
        bridge_proc.terminate()
        frontend_proc.terminate()
        backup_proc.terminate()
        print("✅ ECOSYSTEM COLD.")

if __name__ == "__main__":
    ignite()
