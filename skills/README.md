# Custom Claude Code Skills

This directory contains custom skills developed during this presentation project.

## Available Skills

| Skill | Description | Script |
|-------|-------------|--------|
| `pptx-images` | Insert images into presentations | `scripts/add_images_only.py` |
| `pptx-inspector` | Validate presentations for issues | `scripts/pptx_inspector.py` |
| `conversation-search` | Search past Claude Code conversations | `skills/conversation-search/search.py` |

---

## pptx-images

Insert images into PowerPoint presentations while preserving text content.

**When to use:**
- Adding figures, screenshots, or diagrams to slides
- After text replacement is complete (two-stage workflow)

**Usage:**
```bash
python scripts/add_images_only.py \
    input.pptx output.pptx \
    --mapping image-mapping.json
```

**Features:**
- Resizes text placeholders to make room for images
- Inserts images at specified positions
- Preserves all text content unchanged
- Includes validation for common issues
- Correctly handles the python-pptx position offset bug

See `skills/pptx-images/SKILL.md` for full documentation.

---

## pptx-inspector

Validate PowerPoint presentations for layout issues and broken XML.

**When to use:**
- Before visual review of generated presentations
- When troubleshooting visual glitches
- In CI/CD pipelines for automated validation

**Usage:**
```bash
python scripts/pptx_inspector.py presentation.pptx --level 2
```

**Validation levels:**
1. Quick object inspection (dimensions, positions)
2. XML structure inspection (catches position offset bug)
3. Content validation (placeholder text, overflow)
4. Layout overlap detection

See `skills/pptx-inspector/SKILL.md` for full documentation.

---

## conversation-search

Search past Claude Code conversation history by keyword, project, or date.

**When to use:**
- Finding previous sessions about a topic
- Recalling past decisions or context
- Resuming a previous conversation

**Usage:**
```bash
# List all sessions
python skills/conversation-search/search.py --list

# Search for keyword
python skills/conversation-search/search.py "image insertion"

# View session content
python skills/conversation-search/search.py --session <session-id>
```

See `skills/conversation-search/SKILL.md` for full documentation.

---

## Two-Stage PPTX Workflow

These skills support a two-stage workflow for creating presentations:

```
┌─────────────────────────────────────────────────────────┐
│  Stage 1: Text Replacement (standard PPTX skill)        │
│                                                         │
│  template.pptx → rearrange.py → working.pptx            │
│  working.pptx + replacement.json → replace.py → text.pptx│
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│  Stage 2: Image Insertion (pptx-images skill)           │
│                                                         │
│  text.pptx + image-mapping.json → add_images_only.py    │
│      → final.pptx                                       │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│  Validation (pptx-inspector skill)                      │
│                                                         │
│  final.pptx → pptx_inspector.py → issues report         │
└─────────────────────────────────────────────────────────┘
```

---

## Installation

These skills are project-local. To install globally:

```bash
# Copy all skills to Claude Code skills directory
cp -r skills/* ~/.claude/skills/
```

---

## Contributing

To add a new skill:

1. Create a directory under `skills/`
2. Add a `SKILL.md` with frontmatter (name, description) and documentation
3. Add any supporting scripts
4. Update this README
