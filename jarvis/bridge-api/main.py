from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import subprocess
import os
from pathlib import Path
from typing import List

app = FastAPI(title="Omega Jarvis Bridge API")

# --- CONFIG ---
DEV_ROOT = Path(__file__).parent.parent.parent
OMEGA_CONFIG_PATH = DEV_ROOT / "jarvis" / "CONFIG.md"

# Allow Next.js frontend to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Tighten this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CommandRequest(BaseModel):
    command: str
    args: List[str] = []

@app.get("/health")
async def health_check():
    return {"status": "online", "engine": "Omega Claw"}

@app.post("/execute")
async def execute_command(req: CommandRequest):
    """Executes an Omega system command."""
    # Security: validate command
    allowed_scripts = ["omega-backup.py", "omega-publish.py"]
    if req.command not in allowed_scripts:
        raise HTTPException(status_code=403, detail="Unauthorized command.")
    
    cmd = ["python3", req.command] + req.args
    try:
        result = subprocess.run(cmd, cwd=str(DEV_ROOT), capture_output=True, text=True)
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/tasks")
async def get_tasks():
    task_file = Path("/Users/eds/.gemini/antigravity/brain/be8c1bd9-adb6-424d-a58b-f7f1254dad83/task.md")
    if not task_file.exists():
        return {"tasks": []}
    return {"content": task_file.read_text()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
