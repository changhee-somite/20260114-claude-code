# Permissions and Safety

## Summary
Claude Code operates with significant system access. Understanding the permission model and safety considerations is crucial for effective and secure usage.

## The Permission Model

### Default Mode
- Prompts for approval on file writes, command execution
- Safer but interrupts workflow
- Good for sensitive environments

### YOLO Mode (`--dangerously-skip-permissions`)
- Eliminates constant approval requirements
- "Transforms Claude Code into a completely different product"
- Enables autonomous multi-hour tasks
- **Use case**: Simon Willison completed 3 substantial projects in 48 hours

## Security Considerations

### The Critical Threat: Prompt Injection
> "Anyone who can get text into your LLM has full control over what tools it runs next"

**Example Attack**: Agent tricked into extracting GitHub tokens from environment variables and exfiltrating them via HTTP.

### The Lethal Trifecta
Three elements that create data theft risk:
1. **Access to private data** (env vars, files, credentials)
2. **Exposure to untrusted content** (web pages, user input)
3. **External communication ability** (network access)

When all three combine = vulnerability.

## Sandboxing Solutions

### Anthropic's Approach
- macOS `sandbox-exec` with HTTP proxy controls
- Allow-list specific domains
- Filesystem restrictions

### Key Controls
| Control | Purpose |
|---------|---------|
| Filesystem restrictions | Limit readable/writable paths |
| Network access controls | Block data exfiltration |
| Domain allow-listing | Permit only necessary endpoints |

### Cloud-Based Sandboxes
- Claude Code for Web
- OpenAI Codex Cloud
- Gemini Jules
- Running "on someone else's computer" = credible isolation

## Best Practices

1. **Reserve YOLO mode for non-sensitive code**
2. **Use cloud sandboxes when possible**
3. **Implement network restrictions**
4. **Don't trust AI to detect prompt injection** - it can't reliably

## Virtualization Evolution

The field is moving toward:
- Container-based isolation
- VM-per-session approaches
- Network egress lockdown by default

## Key References

- [Simon Willison: Living Dangerously with Claude](https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/)
- [Awesome Agentic Patterns: Security](https://esc5221.github.io/awesome-agentic-patterns/)
