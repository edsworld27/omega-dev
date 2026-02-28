import os
import time
import datetime
import json

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
USER_SPACE = os.path.join(ROOT_DIR, "USER SPACE")
HIVE_DIR = os.path.join(USER_SPACE, "dev-work", "hive")
INBOX_DIR = os.path.join(HIVE_DIR, "telegram_inbox")
ALERT_FILE = os.path.join(USER_SPACE, "dev-work", "PICKUP_ALERT.md")
PROCESSED_LOG = os.path.join(INBOX_DIR, ".processed.json")

os.makedirs(INBOX_DIR, exist_ok=True)

def load_processed():
    if os.path.exists(PROCESSED_LOG):
        try:
            with open(PROCESSED_LOG, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def save_processed(processed):
    with open(PROCESSED_LOG, 'w') as f:
        json.dump(processed, f)

def scan_inbox():
    """Scan for new FOUNDER_JOB files that haven't been picked up yet."""
    processed = load_processed()
    
    if not os.path.exists(INBOX_DIR):
        return []
    
    new_jobs = []
    for filename in sorted(os.listdir(INBOX_DIR)):
        if filename.startswith("FOUNDER_JOB") and filename.endswith(".md"):
            if filename not in processed:
                new_jobs.append(filename)
    
    return new_jobs

def write_alert(new_jobs):
    """Write a PICKUP_ALERT.md so Claude Code sees new jobs on session start."""
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    content = f"""# 🚨 PICKUP ALERT — New Founder Jobs Detected

**Generated:** {now}
**Source:** Omega Job Watcher Daemon

---

## Pending Jobs

The following FOUNDER_JOBs were dropped from Telegram and are waiting for you to orchestrate:

"""
    for job in new_jobs:
        filepath = os.path.join(INBOX_DIR, job)
        with open(filepath, 'r') as f:
            preview = f.read(200)
        content += f"### {job}\n```\n{preview}\n```\n\n"
    
    content += """---

## Your Action

1. Read each FOUNDER_JOB file in `USER SPACE/dev-work/hive/telegram_inbox/`
2. Apply the **Rule of 3** to calculate the required Hive scale
3. Scaffold the Manager and Worker sandboxes
4. Begin orchestration

*This alert will be cleared once all jobs are picked up.*
"""
    
    with open(ALERT_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

def clear_alert():
    """Remove the alert if no pending jobs exist."""
    if os.path.exists(ALERT_FILE):
        os.remove(ALERT_FILE)

def run_watcher():
    print("👁️ Starting Omega Job Watcher Daemon...")
    while True:
        try:
            new_jobs = scan_inbox()
            if new_jobs:
                print(f"🚨 Detected {len(new_jobs)} new FOUNDER_JOB(s): {new_jobs}")
                write_alert(new_jobs)
                
                # Mark them as processed so we don't alert again
                processed = load_processed()
                processed.extend(new_jobs)
                save_processed(processed)
            else:
                # No new jobs — clear any stale alert
                clear_alert()
            
            time.sleep(5)  # Check every 5 seconds
        except Exception as e:
            print(f"Job Watcher error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    run_watcher()
