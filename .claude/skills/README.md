# Claude Code Skills

Portable skills for Claude Code workflows. Each skill is self-contained and can be copied to other projects.

## Available Skills

| Skill | Description |
|-------|-------------|
| [presentation](presentation/) | Generate PPTX from markdown specifications |
| [conversation-search](conversation-search/) | Search past Claude Code sessions |

## Installation

These skills are project-local by default. To make them available globally:

```bash
# Copy all skills to Claude Code's global skills directory
cp -r .claude/skills/* ~/.claude/skills/
```

Or copy individual skills:

```bash
cp -r .claude/skills/presentation ~/.claude/skills/
cp -r .claude/skills/conversation-search ~/.claude/skills/
```

## Skill Structure

Each skill follows this structure:

```
skill-name/
├── SKILL.md           # Skill definition with frontmatter (name, description)
├── README.md          # Technical documentation (optional)
├── scripts/           # Python/bash implementations
│   └── *.py
└── templates/         # Supporting files (optional)
```

### SKILL.md Format

```markdown
---
name: skill-name
description: "Brief description for Claude to understand when to use this skill."
---

# Skill Name

User-facing documentation with:
- When to use this skill
- How to use it
- Examples
```

## Creating New Skills

1. Create a directory under `.claude/skills/`
2. Add `SKILL.md` with frontmatter and documentation
3. Add implementation scripts
4. Test the skill in your project
5. Copy to other projects or global directory

## Portability

To use these skills in another repository:

1. Copy the entire `.claude/skills/` directory
2. Or copy individual skill directories
3. Update any hardcoded paths in scripts (most use relative paths)
4. Install dependencies: `pip install python-pptx` (for presentation skill)
