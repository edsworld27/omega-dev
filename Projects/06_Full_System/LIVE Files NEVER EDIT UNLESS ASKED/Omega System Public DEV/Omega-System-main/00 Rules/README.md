# ⚡ The Omega System
**The Minimum-Context Autonomous Execution Shell**

Welcome to the **Omega System**. This is the ultra-lightweight, public-facing execution environment for AI-driven software development. It serves as your local workspace while your AI agent handles the heavy lifting via the cloud.

---

## 🏛️ The Decentralized Architecture

To eliminate LLM context-window bloat, we have fully decoupled the Omega Ecosystem into 4 standalone repositories. **This repository (`Omega-System`) is the only one you need to download.**

1. 🧠 **[omega-constitution](https://github.com/edsworld27/omega-constitution):** The "Brain". A massive data lake of XML rules, architectural protocols, and guardrails.
2. 🛒 **[omega-store](https://github.com/edsworld27/omega-store):** The "Marketplace". A collection of certified starter kits (SaaS, Websites, APIs).
3. 🦀 **[omega-claw](https://github.com/edsworld27/omega-claw):** The "Automation Suite". Python background scripts (like `watchdog.py`) that keep autonomous agents looping safely.
4. ⚡ **[Omega-System] (You are here):** The "Execution Shell". A sterile playground where your code is actually built.

---

## 🚀 How to Start (Two Methods)

### Method 1: The "Zero-Install" God Prompt (Recommended)
If you have Claude Desktop configured with the GitHub MCP server, you don't even need to run a setup script. Just open this folder in your IDE, open Claude, and paste this exact prompt:

> *"Use your GitHub MCP tool to read the Omega Constitution Index at `edsworld27/omega-constitution/main/omega-index.md`. I want to build a [SaaS/Website/API]. Follow the setup instructions in the index."*

Claude will instantly download its instructions from the cloud, check the Omega Store for a template, and begin scaffolding your project autonomously.

#### ⚙️ GitHub MCP Configuration:
Add this to your `claude_desktop_config.json` to enable the Zero-Install flow:
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "YOUR_TOKEN_HERE"
      }
    }
  }
}
```

---

### Method 2: The Fallback Setup Script
If you do not have MCP set up, or simply want a guided terminal experience, you can use the built-in initializer script.

1. Clone this repository.
2. Open your terminal and navigate to the `Constution V13` folder.
3. Run the interactive setup tool:
   ```bash
   python3 omega.py
   ```
4. Answer the questions. It will generate a custom prompt for you to copy and paste into any AI (Claude, ChatGPT, etc.).

---

### 🛡️ Why This Architecture?
By moving 50,000+ lines of system instructions out of your local workspace and into a remote GitHub data lake (`omega-constitution`), your AI agents save hundreds of thousands of tokens per session. They "lazy-load" exactly the rules they need, right when they need them. It is cheaper, faster, and infinitely more accurate.
