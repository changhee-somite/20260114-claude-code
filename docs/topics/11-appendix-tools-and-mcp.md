# Appendix: Built-in Tools and MCP Setup

## Summary
Claude Code comes with ~15 built-in tools and can be extended via MCP (Model Context Protocol) servers and Skills. This appendix covers what's preloaded vs. what can be added.

---

## Built-in Tools (Preloaded)

These tools are always available without any configuration:

### File Operations

| Tool | Purpose |
|------|---------|
| **Read** | Read files (text, images, PDFs, Jupyter notebooks) |
| **Write** | Create or overwrite files |
| **Edit** | Make exact string replacements in files |
| **NotebookEdit** | Modify Jupyter notebook cells |
| **Glob** | Fast file pattern matching (e.g., `**/*.py`) |
| **Grep** | Search file content with regex (ripgrep-based) |

### Shell Operations

| Tool | Purpose |
|------|---------|
| **Bash** | Execute shell commands in persistent session |
| **BashOutput** | Retrieve output from background shells |
| **KillShell** | Terminate background bash sessions |

### Web Operations

| Tool | Purpose |
|------|---------|
| **WebFetch** | Fetch and analyze web content |
| **WebSearch** | Search the web for current information |

### Agent & Workflow

| Tool | Purpose |
|------|---------|
| **Task** | Launch specialized sub-agents (Plan, Explore, general-purpose) |
| **TodoWrite** | Create/manage structured task lists |
| **ExitPlanMode** | Conclude plan mode after presenting strategy |
| **SlashCommand** | Execute slash commands within conversations |

### Tool Assignment by Role

Different agent types have access to different tools:

| Role | Tools Available |
|------|-----------------|
| **Read-only** (reviewers) | Read, Grep, Glob |
| **Research** (analysts) | Read, Grep, Glob, WebFetch, WebSearch |
| **Code writers** (developers) | Read, Write, Edit, Bash, Glob, Grep |
| **Documentation** | Read, Write, Edit, Glob, Grep, WebFetch, WebSearch |

---

## Loadable Extensions

### Skills (Plugins)

Skills are loaded via `/plugin` command. See [10-setup-and-configuration.md](10-setup-and-configuration.md) for details.

**Official Skills:**
```bash
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
```

**Categories available:**
- Document Skills (DOCX, PDF, PPTX, XLSX)
- Creative & Design
- Development & Technical
- Enterprise & Communication

### MCP Servers

MCP (Model Context Protocol) servers extend Claude Code with external capabilities.

**How MCP Works:**
1. MCP server runs locally or remotely
2. Exposes tools that Claude Code can call
3. Configured in settings or via command

---

## Setting Up MCP Servers

### Configuration Locations

| Platform | Config File |
|----------|-------------|
| Claude Code | `~/.claude/settings.json` or `.claude/settings.json` |
| Claude Desktop | `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) |

### Basic MCP Configuration

In `settings.json`:
```json
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "@package/mcp-server"],
      "env": {
        "API_KEY": "your-key"
      }
    }
  }
}
```

### Adding MCP via Command

```bash
claude mcp add <name> -s user -- <command>
```

---

## Example: Gemini MCP Server

Integrate Google's Gemini models with Claude Code for:
- Large context analysis (1M tokens)
- Code review with different perspective
- YouTube/document analysis
- Image generation

### Quick Setup (Recommended)

```bash
claude mcp add gemini -s user -- env GEMINI_API_KEY=YOUR_KEY npx -y @rlabs-inc/gemini-mcp
```

### Manual Configuration

Add to `~/.claude/settings.json`:
```json
{
  "mcpServers": {
    "gemini": {
      "command": "npx",
      "args": ["-y", "@rlabs-inc/gemini-mcp"],
      "env": {
        "GEMINI_API_KEY": "your-gemini-api-key"
      }
    }
  }
}
```

### Getting a Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with Google account
3. Navigate to "Get API Key"
4. Create new key or use existing

### Gemini MCP Features

| Tool | Description |
|------|-------------|
| Deep Research | Comprehensive research on topics |
| Code Analysis | Security, performance, architecture review |
| Codebase Analysis | Full project analysis (1M context) |
| URL Analysis | Analyze web content |
| YouTube Analysis | Extract and analyze video content |
| Document Analysis | Process large documents |
| Google Search | Real-time web search |
| Image Generation | Generate images with Imagen |

### Usage in Claude Code

After setup, use naturally:
```
Ask Gemini to analyze this large codebase for security issues
```

Or explicitly:
```
Use the gemini tool to review this 500-file project
```

---

## Other Popular MCP Servers

### Context7 (Documentation)
```bash
claude mcp add context7 -s user -- npx -y @anthropic-ai/context7-mcp
```
Provides up-to-date documentation for libraries.

### GitHub
```bash
claude mcp add github -s user -- env GITHUB_TOKEN=YOUR_TOKEN npx -y @anthropic-ai/github-mcp
```
GitHub operations: PRs, issues, repository management.

### Filesystem (Extended)
```bash
claude mcp add filesystem -s user -- npx -y @modelcontextprotocol/server-filesystem /path/to/allowed/dir
```
Extended filesystem access with path restrictions.

### PostgreSQL
```bash
claude mcp add postgres -s user -- env DATABASE_URL=postgres://... npx -y @modelcontextprotocol/server-postgres
```
Database queries and schema inspection.

---

## MCP vs Skills vs Built-in Tools

| Type | Persistence | Complexity | Use Case |
|------|-------------|------------|----------|
| **Built-in Tools** | Always available | None | Core operations (files, shell, search) |
| **Skills** | Per-session load | Low (markdown) | Task instructions, workflows |
| **MCP Servers** | Background process | Medium (config) | External integrations, APIs |

### When to Use What

- **Need file/shell access?** → Built-in tools (already there)
- **Need specialized workflow?** → Skills (install via /plugin)
- **Need external service?** → MCP server (database, API, other AI)

---

## Troubleshooting MCP

### Check Installed MCPs
```bash
/mcp
```
Or check in `/status` → Status tab → "MCP servers"

### Common Issues

| Issue | Solution |
|-------|----------|
| MCP not appearing | Restart Claude Code after config change |
| API key errors | Verify key in environment variable |
| Server crashes | Check stderr logs, not stdout |
| Permission denied | Ensure command is executable |

### Logging
MCP servers should log to `stderr`, not `stdout` (stdout corrupts MCP stream).

---

## Key References

- [Claude Code Tools Reference](https://www.vtrivedy.com/posts/claudecode-tools-reference/)
- [Gemini MCP Server](https://github.com/RLabs-Inc/gemini-mcp)
- [MCP Setup Guide](https://apidog.com/blog/gemini-mcp-claude-code/)
- [Claude Code System Prompts](https://github.com/Piebald-AI/claude-code-system-prompts)
- [Awesome Claude Code](https://github.com/hesreallyhim/awesome-claude-code)
