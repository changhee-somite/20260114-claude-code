# Custom Claude Code Skills

This directory contains custom skills developed during this presentation project.

## conversation-search

A skill for searching past Claude Code conversation history.

### Installation

```bash
# Copy to your skills directory
cp -r skills/conversation-search ~/.claude/skills/
```

### Usage

The skill can be used in two ways:

#### 1. Natural Language (via Claude)

Just ask Claude naturally:
- "Search my conversations for 'pptx image insertion'"
- "What sessions did I have about authentication?"
- "Find where we discussed the workflow"

Claude will use the skill's SKILL.md documentation to search.

#### 2. Direct Script Usage

```bash
# List all sessions
python ~/.claude/skills/conversation-search/search.py --list

# Search for keyword
python ~/.claude/skills/conversation-search/search.py "image insertion"

# Search with sessions-only mode
python ~/.claude/skills/conversation-search/search.py "pptx" --sessions-only

# Filter by project
python ~/.claude/skills/conversation-search/search.py --list --project ~/myproject

# View session content
python ~/.claude/skills/conversation-search/search.py --session <session-id>
```

### Why This Skill?

During this presentation project, we needed to investigate why the PPTX skill couldn't insert images. This required searching through past conversation history stored in `~/.claude/projects/`.

Key learnings:
1. Conversations are stored as JSONL files
2. Each project has a `sessions-index.json` with metadata
3. Session IDs can be used with `claude --resume <id>` to continue

### File Structure

```
conversation-search/
├── SKILL.md     # Skill definition and documentation
└── search.py    # Python search script
```

### Conversation Storage Structure

```
~/.claude/
├── projects/
│   └── -Users-name-path-to-project/       # Path-encoded
│       ├── sessions-index.json            # Session index
│       └── <session-id>.jsonl             # Session content
├── history.jsonl                          # Global index
└── settings.json
```

## Contributing

To add a new skill:
1. Create a directory under `skills/`
2. Add a `SKILL.md` with the skill definition
3. Add any supporting scripts
4. Update this README
