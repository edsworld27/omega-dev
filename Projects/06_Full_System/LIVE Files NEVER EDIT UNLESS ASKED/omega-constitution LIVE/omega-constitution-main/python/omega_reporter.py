import os
import time
import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
USER_SPACE = os.path.join(ROOT_DIR, "USER SPACE")
PROJECT_DIR = os.path.join(USER_SPACE, "project")
LOGGING_DIR = os.path.join(USER_SPACE, "logging")
REPORT_FILE = os.path.join(LOGGING_DIR, "compliance_report.md")

# Ensure logging dir exists
os.makedirs(LOGGING_DIR, exist_ok=True)

def check_structure():
    violations = []
    
    if not os.path.exists(PROJECT_DIR):
        return ["CRITICAL: USER SPACE/project/ directory is missing."]
        
    src_path = os.path.join(PROJECT_DIR, "src")
    if not os.path.exists(src_path):
        violations.append("WARNING: No `src/` directory found in `project/`. Code should be compartmentalized.")
        
    # Check for flat structure (too many files in root of project)
    root_files = [f for f in os.listdir(PROJECT_DIR) if os.path.isfile(os.path.join(PROJECT_DIR, f)) and not f.startswith('.')]
    if len(root_files) > 10:
        violations.append(f"WARNING: Too many files ({len(root_files)}) in the root of `project/`. Consider moving them to `src/` or specific subdirectories.")
        
    return violations

def generate_report():
    violations = check_structure()
    
    header = f"# Omega Compliance Report\n**Last Checked:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    if not violations:
        content = header + "✅ **STATUS: ALL CLEAR**\nNo structural or compliance violations detected.\n"
    else:
        content = header + "❌ **STATUS: VIOLATIONS DETECTED**\n\nThe following issues need architectural review:\n\n"
        for v in violations:
            content += f"- {v}\n"
            
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

def run_reporter():
    print("📝 Starting Omega Reporter Daemon...")
    while True:
        try:
            generate_report()
            time.sleep(10) # Run every 10 seconds
        except Exception as e:
            print(f"Reporter error: {e}")
            time.sleep(10)

if __name__ == "__main__":
    run_reporter()
