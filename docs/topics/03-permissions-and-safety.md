# Permissions and Safety

## Summary
Claude Code operates with significant system access. Understanding the permission model and safety considerations is crucial for effective and secure usage. Importantly, there's a middle ground between constant prompts and "YOLO mode."

## Permission Modes

Claude Code offers four permission modes, switchable via `Shift+Tab`:

| Mode | Behavior |
|------|----------|
| **default** | Prompts for approval on first use of each tool |
| **acceptEdits** | Automatically accepts file edits for the session |
| **plan** | Read-only analysis; cannot modify files or execute commands |
| **bypassPermissions** | Skips all permission prompts (requires safe environment) |

### Plan Mode
- Claude analyzes but cannot modify
- Uses a "Plan subagent" to gather context
- Presents plan for approval before execution
- Good for reviewing what changes will be made

## Granular Permission Configuration

### Settings File Hierarchy (Priority Order)
```
1. Enterprise managed (highest) → managed-settings.json
2. Command line arguments     → session-specific
3. Local project settings     → .claude/settings.local.json (git-ignored)
4. Shared project settings    → .claude/settings.json (version-controlled)
5. User settings (lowest)     → ~/.claude/settings.json
```

### Allow/Deny/Ask Rules

Configure in `settings.json`:

```json
{
  "permissions": {
    "allow": [
      "Bash(npm run lint)",
      "Bash(npm run test:*)",
      "Bash(git:*)",
      "Read(~/.zshrc)",
      "Edit"
    ],
    "deny": [
      "Bash(curl:*)",
      "Read(./.env)",
      "Read(./secrets/**)",
      "Read(**/*.key)"
    ],
    "ask": [
      "Bash(git push:*)",
      "Bash(rm:*)"
    ]
  }
}
```

### Rule Evaluation Order
1. **deny** rules checked first (block regardless of other rules)
2. **allow** rules checked next (permit if matched)
3. **ask** rules force confirmation even if allowed

### Pattern Syntax

**Bash commands:**
- `Bash(npm run lint)` - exact command
- `Bash(npm run test:*)` - wildcard suffix
- `Bash(git:*)` - any git command

**File paths (gitignore-style):**
- `Read(**/.env)` - .env files in any directory
- `Read(**/*.key)` - files with .key extension
- `Read(**/node_modules/**)` - any node_modules directory

**WebFetch:**
- `WebFetch(domain:docs.anthropic.com)` - specific domain

### Interactive Permission Commands

During a session:
```
/permissions add Edit
/permissions add Bash(git commit:*)
/permissions remove Bash(rm:*)
/permissions list
```

## Hooks for Custom Permission Logic

Hooks allow custom code to run at key events:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/validator.sh"
          }
        ]
      }
    ]
  }
}
```

### Hook Events
- **PreToolUse**: Block or modify tool calls before execution
- **PostToolUse**: Run formatters, linters after file changes
- **PermissionRequest**: Auto-approve specific patterns

### Security Note
Direct edits to hook configuration require review in `/hooks` menu - prevents malicious code from silently adding hooks.

## YOLO Mode (`--dangerously-skip-permissions`)

### When It's Appropriate
- Isolated environments (Docker containers)
- Non-sensitive codebases
- Well-scoped, defined tasks
- When you can review all changes afterward

### When to Avoid
- Production environments
- Codebases with credentials
- Tasks involving untrusted input

### Best Practice
Even with YOLO mode, configure an `AllowedTools` whitelist:
```json
{
  "allowedTools": ["Read", "Write", "Edit", "Bash(npm:*)", "Bash(git:*)"]
}
```

## Security Considerations

### The Lethal Trifecta
Three elements that create data theft risk:
1. **Access to private data** (env vars, files, credentials)
2. **Exposure to untrusted content** (web pages, user input)
3. **External communication ability** (network access)

### Prompt Injection
> "Anyone who can get text into your LLM has full control over what tools it runs next"

AI cannot reliably detect prompt injection attacks.

## Sandboxing Solutions

| Approach | Description |
|----------|-------------|
| macOS `sandbox-exec` | Anthropic's built-in with HTTP proxy controls |
| Docker containers | Isolated filesystem and network |
| Cloud sandboxes | Claude Code for Web, Codex Cloud |
| VM-per-session | Maximum isolation |

## Enterprise Settings

`managed-settings.json` files cannot be overridden by user or project settings - ideal for enforcing organization-wide security policies.

Location:
- macOS: `/Library/Application Support/ClaudeCode/managed-settings.json`
- Linux/WSL: `/etc/claude-code/managed-settings.json`

## Key References

- [Claude Code Permissions Guide](https://www.eesel.ai/blog/claude-code-permissions)
- [Claude Code Settings Docs](https://code.claude.com/docs/en/settings)
- [Hooks Guide](https://code.claude.com/docs/en/hooks-guide)
- [Simon Willison: Living Dangerously](https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/)
- [Permission Management Guide](https://claudefa.st/blog/guide/development/permission-management)
