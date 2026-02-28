import subprocess
import time
import sys
import os

def ignite():
    print("🔥 OMEGA JARVIS IGNITION SEQUENCE STARTING...")
    
    # 1. Start Python Bridge API
    print("⚡ Starting Bridge API (FastAPI)...")
    bridge_proc = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "main:app", "--port", "8000", "--reload"],
        cwd="jarvis/bridge-api"
    )
    
    # 2. Start Next.js Frontend
    print("💎 Starting Next.js Dashboard...")
    frontend_proc = subprocess.Popen(
        ["npm", "run", "dev"],
        cwd="jarvis/dashboard-next"
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
        print("✅ ECOSYSTEM COLD.")

if __name__ == "__main__":
    ignite()
