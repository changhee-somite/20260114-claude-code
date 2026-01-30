---
name: conversation-search
description: "Search past Claude Code conversations by keyword, project, or date. Use when the user asks about previous sessions, wants to find past discussions, or needs to recall what was done in earlier conversations."
---

# Claude Code Conversation Search

Search and analyze past Claude Code conversation sessions.

## When to Use This Skill

- User asks "What did we discuss about X?"
- User wants to find a previous session
- User asks "When did we work on Y?"
- User needs to recall past decisions or context
- User wants to resume a previous conversation

## Conversation Storage Structure

Claude Code stores conversations locally:

```
~/.claude/
├── projects/                              # All project conversations
│   └── -Users-name-path-to-project/       # Path-encoded project folder
│       ├── sessions-index.json            # Session metadata index
│       ├── <session-id>.jsonl             # Individual session files
│       └── <session-id>/                  # Session artifacts (if any)
├── history.jsonl                          # Global history index
└── settings.json                          # User settings
```

## Session Index Structure

The `sessions-index.json` contains metadata for all sessions in a project:

```json
{
  "version": 1,
  "entries": [
    {
      "sessionId": "uuid-here",
      "fullPath": "/path/to/session.jsonl",
      "firstPrompt": "User's first message...",
      "customTitle": "Optional custom title",
      "messageCount": 25,
      "created": "2026-01-14T14:23:46.203Z",
      "modified": "2026-01-14T15:40:24.589Z",
      "gitBranch": "main",
      "projectPath": "/path/to/project"
    }
  ]
}
```

## JSONL Message Structure

Each line in a `.jsonl` file is a JSON object with:

```json
{
  "type": "user" | "assistant",
  "message": {
    "role": "user" | "assistant",
    "content": [
      {"type": "text", "text": "Message content"},
      {"type": "tool_use", "name": "ToolName", "input": {...}},
      {"type": "tool_result", "content": "Result..."}
    ]
  },
  "timestamp": "2026-01-14T14:27:00.684Z",
  "sessionId": "uuid"
}
```

## Search Methods

### Method 1: Quick Session Overview (Recommended First Step)

```bash
# List all sessions for current project
cat ~/.claude/projects/-Users-*-$(basename $(pwd))*/sessions-index.json 2>/dev/null | python3 -c "
import json, sys
data = json.load(sys.stdin)
for e in data.get('entries', []):
    print(f\"{e.get('modified', '')[:10]} | {e.get('customTitle') or e.get('firstPrompt', '')[:50]}... | {e.get('sessionId')}\")
"
```

### Method 2: Search by Keyword in Session Content

```python
#!/usr/bin/env python3
import json
import os
import re
from pathlib import Path

def search_sessions(keyword, project_path=None):
    """Search all sessions for a keyword."""
    base = Path.home() / '.claude' / 'projects'

    # Filter by project if specified
    if project_path:
        encoded = project_path.replace('/', '-')
        dirs = [d for d in base.iterdir() if encoded in d.name]
    else:
        dirs = list(base.iterdir())

    results = []
    pattern = re.compile(keyword, re.IGNORECASE)

    for proj_dir in dirs:
        if not proj_dir.is_dir():
            continue

        for jsonl_file in proj_dir.glob('*.jsonl'):
            with open(jsonl_file, 'r') as f:
                for line_num, line in enumerate(f, 1):
                    try:
                        data = json.loads(line)
                        content = json.dumps(data)
                        if pattern.search(content):
                            # Extract readable text
                            msg = data.get('message', {})
                            text_parts = []
                            for c in msg.get('content', []):
                                if isinstance(c, dict) and c.get('type') == 'text':
                                    text_parts.append(c.get('text', '')[:200])

                            if text_parts or pattern.search(content):
                                results.append({
                                    'session': jsonl_file.stem,
                                    'project': proj_dir.name,
                                    'line': line_num,
                                    'preview': ' '.join(text_parts)[:300] if text_parts else '[Tool/System message]'
                                })
                    except json.JSONDecodeError:
                        continue

    return results

# Usage:
# results = search_sessions("image insertion")
# for r in results[:10]:
#     print(f"{r['session']}: {r['preview'][:100]}...")
```

### Method 3: Search with Bash (Quick)

```bash
# Search all sessions for a keyword
grep -r -l "keyword" ~/.claude/projects/*/\*.jsonl 2>/dev/null

# Search with context
grep -r -i "keyword" ~/.claude/projects/*/\*.jsonl 2>/dev/null | head -20

# Find sessions mentioning a specific tool
grep -r "\"name\":\"Edit\"" ~/.claude/projects/*/\*.jsonl 2>/dev/null | cut -d: -f1 | sort -u
```

### Method 4: Get Session Details

```python
def get_session_summary(session_id, project_encoded):
    """Get a summary of a specific session."""
    base = Path.home() / '.claude' / 'projects'

    # Find the session file
    for proj_dir in base.iterdir():
        if project_encoded and project_encoded not in proj_dir.name:
            continue

        session_file = proj_dir / f'{session_id}.jsonl'
        if session_file.exists():
            messages = []
            with open(session_file, 'r') as f:
                for line in f:
                    try:
                        data = json.loads(line)
                        if data.get('type') == 'user':
                            msg = data.get('message', {})
                            for c in msg.get('content', []):
                                if isinstance(c, dict) and c.get('type') == 'text':
                                    messages.append(('USER', c.get('text', '')[:500]))
                    except:
                        continue

            return messages

    return None
```

## Resume a Session

Once you find a session ID, resume it with:

```bash
claude --resume <session-id>
```

## Common Search Patterns

| Goal | Search Term |
|------|-------------|
| Find file edits | `"name":"Edit"` |
| Find bash commands | `"name":"Bash"` |
| Find user questions | `"type":"text"` with `"role":"user"` |
| Find specific file | `"file_path":"path/to/file"` |
| Find errors | `"is_error":true` |
| Find commits | `git commit` |

## Tips

1. **Start with sessions-index.json** - It has titles and first prompts
2. **Use timestamps** - Sessions are named by UUID but index has dates
3. **Filter by project** - Project paths are URL-encoded in folder names
4. **Check customTitle** - Users can rename sessions for easier finding
5. **Tool results have context** - Look at `toolUseResult` for file contents, command outputs
