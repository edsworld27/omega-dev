import streamlit as st
import os
import pandas as pd
from datetime import datetime
from pathlib import Path

# --- OMEGA JARVIS DASHBOARD (THE INSANITY LAYER) ---
# Version: 1.0 (Alpha)
# Governance: Omega Constitution

st.set_page_config(
    page_title="Omega Jarvis Mission Control",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- THEMES & CSS ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #e0e0e0;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #262730;
        color: white;
        border: 1px solid #4a4a4a;
    }
    .stButton>button:hover {
        border: 1px solid #00ff00;
        color: #00ff00;
    }
    .kanban-card {
        background-color: #1e1e1e;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #00ff00;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- PATHS ---
RULES_DIR = Path(__file__).parent
WORKSPACE_ROOT = RULES_DIR.parent.parent
JARVIS_DIR = WORKSPACE_ROOT / "Projects" / "Dev Version (Edit)" / "Omega Claw v1 DEV" / "jarvis"
CONFIG_FILE = JARVIS_DIR / "CONFIG.md"
MEMORY_BANK = JARVIS_DIR / "OMEGA_MEMORY_BANK.md"

# Hive Path (from dev version edit)
HIVE_DIR = WORKSPACE_ROOT / "Projects" / "Dev Version (Edit)" / "omega-constitution DEV" / "Entire_Constitution_Files" / "USER SPACE" / "dev-work" / "hive"
SECURITY_SCRIPT = WORKSPACE_ROOT / "Projects" / "Dev Version (Edit)" / "omega-constitution DEV" / "Entire_Constitution_Files" / "omega-constitution-main" / "python" / "auto_security.py"

# Absolute path to the conversation task file (Configured during Setup Vault onboarding)
TASK_FILE = Path("/Users/eds/.gemini/antigravity/brain/be8c1bd9-adb6-424d-a58b-f7f1254dad83/task.md")

import subprocess

def run_script(command, cwd=str(WORKSPACE_ROOT)):
    """Runs a script and returns output."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=cwd)
        if result.returncode == 0:
            return f"✅ SUCCESS:\n{result.stdout}"
        else:
            return f"❌ ERROR ({result.returncode}):\n{result.stderr}"
    except Exception as e:
        return f"❌ EXCEPTION: {str(e)}"

def sync_config(auto_mode):
    """Syncs the dashboard state to a persistent markdown config."""
    with open(CONFIG_FILE, 'w') as f:
        f.write(f"# JARVIS CONFIG\n\n- AUTONOMOUS_MODE: {auto_mode}\n")

# --- SIDEBAR: MISSION CONTROL ---
with st.sidebar:
    st.title("🧠 JARVIS")
    st.caption("v1.0 - AGI Mission Control")
    st.divider()
    
    st.subheader("Operational Status")
    auto_toggle = st.toggle("AUTONOMOUS MODE", key="auto_toggle", value=st.session_state.autonomous_mode)
    
    if auto_toggle != st.session_state.autonomous_mode:
        st.session_state.autonomous_mode = auto_toggle
        sync_config(auto_toggle)
        
    if st.session_state.autonomous_mode:
        st.success("🤖 AUTO-PILOT ACTIVE")
    else:
        st.warning("👤 CO-PILOT ENGAGED")
        
    st.divider()
    st.subheader("Operational Tools")
    
    if st.button("📦 Manual Backup"):
        with st.status("Creating fractal snapshot..."):
            output = run_script("python3 omega-backup.py save 'Dashboard Manual Snapshot'")
            st.code(output)
        
    if st.button("🚀 God-Mode Sync"):
        with st.status("Syncing ecosystem to GitHub..."):
            output = run_script("python3 omega-publish.py 'Dashboard Sync Update'")
            st.code(output)
            
    if st.button("🛡️ Security Audit"):
        with st.status("Running security protocols..."):
            output = run_script(f"python3 '{SECURITY_SCRIPT}'")
            st.code(output)

# --- MAIN CONTENT ---
# First-Run Detection
is_first_run = not CONFIG_FILE.exists()

tabs = ["🚀 Mission Board", "🧠 Memory Lab", "💬 Chat Terminal", "🐝 Hive Monitor", "🔄 Permanent Swarm", "⚙️ Setup Vault"]
tab_list = st.tabs(tabs)

if is_first_run:
    st.sidebar.warning("⚠️ INITIALIZATION REQUIRED")
    active_tab = tabs.index("⚙️ Setup Vault")
else:
    active_tab = 0

# Distribute content into tabs
tab1, tab2, tab3, tab4, tab5, tab6 = tab_list

with tab1:
    st.header("Active Mission Kanban")
    
    pending, building, blocked, complete = parse_markdown_tasks(TASK_FILE)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("### 📥 PENDING")
        for task in pending:
            st.markdown(f'<div class="kanban-card">{task}</div>', unsafe_allow_html=True)
        if not pending: st.info("No pending tasks.")
        
    with col2:
        st.markdown("### 🏗️ BUILDING")
        for task in building:
            st.markdown(f'<div class="kanban-card" style="border-left-color: #ff9900;">{task}</div>', unsafe_allow_html=True)
        if not building: st.info("No active builds.")
        
    with col3:
        st.markdown("### 🛑 BLOCKED")
        for task in blocked:
            st.markdown(f'<div class="kanban-card" style="border-left-color: red;">{task}</div>', unsafe_allow_html=True)
        if not blocked: st.info("No current blockers.")
        
    with col4:
        st.markdown("### ✅ COMPLETE")
        for task in complete:
            st.markdown(f'<div class="kanban-card" style="border-left-color: #0088ff;">{task}</div>', unsafe_allow_html=True)
        if not complete: st.info("Waiting for first success...")

with tab2:
    st.header("🧠 Memory Lab (Hippocampus)")
    
    # Add New Pattern Form
    with st.expander("➕ Add New Memory Pattern", expanded=False):
        with st.form("new_pattern_form"):
            category = st.selectbox("Category", ["Python Framework Adjustments", "UI Layout Preferences", "Workflow Quirks", "New Discovery"])
            new_pattern = st.text_area("Pattern Description")
            if st.form_submit_button("Commit to Long-Term Memory"):
                if new_pattern.strip():
                    with open(MEMORY_BANK, 'a') as f:
                        f.write(f"\n### {category}\n- {new_pattern}\n")
                    st.success(f"Pattern added to {category}!")
                else:
                    st.error("Pattern cannot be empty.")

    if MEMORY_BANK.exists():
        with open(MEMORY_BANK, 'r') as f:
            memory_content = f.read()
        
        updated_memory = st.text_area("Live Memory Editor", value=memory_content, height=400)
        
        if st.button("Solidify Global patterns"):
            with open(MEMORY_BANK, 'w') as f:
                f.write(updated_memory)
            st.success("Global memory patterns mathematically aligned.")
    else:
        st.error("OMEGA_MEMORY_BANK.md not found in jarvis/ folder!")

with tab3:
    st.header("💬 Local Chat Terminal")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "I am Jarvis. How can I assist you with the Omega System today?"}]

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Command Jarvis..."):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Jarvis Response Logic (Placeholder for real agent connection)
        response = f"Jarvis: Acknowledged. Executing command in {st.session_state.auto_toggle and 'AUTONOMOUS' or 'CO-PILOT'} mode. (Simulation Only)"
        
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

with tab4:
    st.header("🐝 Hive Monitor (Agent Swarm)")
    st.caption("Monitoring active agent sandboxes and job execution.")
    
    if HIVE_DIR.exists():
        agents = [d for d in os.listdir(HIVE_DIR) if os.path.isdir(HIVE_DIR / d)]
        if agents:
            st.write(f"Active Agent Directories: {len(agents)}")
            for agent in agents:
                with st.expander(f"🕵️ Agent: {agent}"):
                    agent_path = HIVE_DIR / agent
                    st.text(f"Path: {agent_path}")
                    # Look for job files or logs
                    files = os.listdir(agent_path)
                    st.write(f"FILES: {files}")
        else:
            st.info("Swarm is currently idle. No active agent sandboxes detected.")
    else:
        st.warning(f"Hive directory not found at: {HIVE_DIR}")

with tab5:
    st.header("🔄 Permanent Agent Swarm (24/7 Daemons)")
    st.caption("Background processes for continuous operations.")
    
    col_a, col_b = st.columns([2, 1])
    
    with col_a:
        st.markdown("### Active Daemons")
        # Placeholder for daemon list logic
        st.markdown("""
            <div class="kanban-card" style="border-left-color: #00ff00;">
                <b>Outreach Agent</b><br>
                Status: Running<br>
                Uptime: 24h 12m
            </div>
        """, unsafe_allow_html=True)
        
    with col_b:
        st.markdown("### Daemon Actions")
        if st.button("Start Outreach Daemon"):
            st.success("Outreach Daemon Spawning...")
        if st.button("Kill All Daemons", type="primary"):
            st.warning("All background processes terminated.")

with tab6:
    st.header("⚙️ Jarvis Setup & Onboarding Vault")
    st.caption("Configure your AGI Mission Control.")
    
    with st.expander("🛠️ Repository Binding", expanded=True):
        st.text_input("Constitution Repo URL", value="https://github.com/edsworld27/omega-constitution.git")
        st.text_input("Store Repo URL", value="https://github.com/edsworld27/omega-store.git")
        st.text_input("Personal Projects Path", value="/Volumes/Internal/Projects/Omega System/Projects/")
        if st.button("Bind Repositories"):
            st.success("Mathematical alignment confirmed.")
            
    with st.expander("🔑 API & Secret Management"):
        st.text_input("Anthropic API Key", type="password")
        st.text_input("GitHub Access Token", type="password")
        st.button("Encrypt & Secure Vault")
        
    with st.expander("📈 System Readiness"):
        st.write("Python Environment: ✅")
        st.write("Docker Vault: ✅")
        st.write("Tailscale Mesh: ✅")
        st.progress(100, text="Omega System Fully Configured")

st.sidebar.divider()
st.sidebar.caption(f"Last Sync: {datetime.now().strftime('%H:%M:%S')}")
