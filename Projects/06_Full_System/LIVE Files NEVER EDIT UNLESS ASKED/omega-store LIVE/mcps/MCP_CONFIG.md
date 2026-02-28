# MCP CONFIGURATION
**Version:** 4.0

**Purpose:** Configure Model Context Protocol (MCP) servers for your project. MCPs extend the agent's capabilities by connecting to external tools and services.

**If blank:** The agent operates without MCP connections. Add servers as needed.

---

## Active MCP Servers

| Server | Purpose | Auth | Status |
| :--- | :--- | :--- | :--- |
| (e.g., filesystem) | (Local file access) | (None) | (🟢 Active / 🔴 Inactive) |
| (e.g., github) | (Repo management) | (Token in .env) | (🟢 / 🔴) |
| (e.g., postgres) | (Database access) | (Connection string in .env) | (🟢 / 🔴) |

## Server Definitions

*Copy this block for each MCP server.*

### [Server Name]
- **Package:** (e.g., `@modelcontextprotocol/server-filesystem`)
- **Purpose:** (What this server provides)
- **Configuration:**
```json
{
  "command": "",
  "args": [],
  "env": {}
}
```
- **Credentials:** (Where stored — must be in .env, never hardcoded)
- **Permissions:** (What the server can access)
- **Constraints:** (What the server must NOT access)

---

## Example Configurations

### Filesystem (Local File Access)
- **Package:** `@modelcontextprotocol/server-filesystem`
- **Purpose:** Read/write access to the project directory
- **Configuration:**
```json
{
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/project"]
}
```
- **Credentials:** None required
- **Permissions:** Read/write within project directory only
- **Constraints:** Must NOT access parent directories, `.env`, or `node_modules/`

### GitHub (Repository Management)
- **Package:** `@modelcontextprotocol/server-github`
- **Purpose:** Create issues, manage PRs, read repo contents
- **Configuration:**
```json
{
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-github"],
  "env": {
    "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
  }
}
```
- **Credentials:** `GITHUB_TOKEN` in `.env` (scope: `repo`, `issues`)
- **Permissions:** Read/write on configured repositories only
- **Constraints:** Must NOT delete repositories or modify organisation settings

### PostgreSQL (Database Access)
- **Package:** `@modelcontextprotocol/server-postgres`
- **Purpose:** Query database, inspect schema, run migrations
- **Configuration:**
```json
{
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-postgres", "${DATABASE_URL}"]
}
```
- **Credentials:** `DATABASE_URL` in `.env`
- **Permissions:** Read on production, read/write on development
- **Constraints:** Must NOT run `DROP`, `TRUNCATE`, or `ALTER` on production without CP-5 approval

### Brave Search (Web Search)
- **Package:** `@modelcontextprotocol/server-brave-search`
- **Purpose:** Search the web for documentation, debugging, and research
- **Configuration:**
```json
{
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-brave-search"],
  "env": {
    "BRAVE_API_KEY": "${BRAVE_API_KEY}"
  }
}
```
- **Credentials:** `BRAVE_API_KEY` in `.env`
- **Permissions:** Read-only web search
- **Constraints:** Results are Tier 4 sources (see `SOURCES.md`) — must be validated against Tier 1

---

## Security Rules
(From SECURITY.xml — applies to all MCP servers)

1. All MCP credentials stored in `.env` only — never in config files committed to Git
2. Each server gets minimum required permissions
3. Server connections are logged
4. Untrusted server output is treated as untrusted input (validate before use)
5. MCP servers must be listed in `deps.md` with version pins

## Adding A New Server
1. Define it in this file
2. Add it to `deps.md` with version pin
3. Add credentials to `.env` (never `.env.example` with real values)
4. Present to Pilot at CP-5 (Dependency Request) for approval
