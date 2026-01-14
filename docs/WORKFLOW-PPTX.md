# PPTX Generation Workflow

This document describes the workflow for generating PowerPoint presentations from markdown documentation.

## Overview Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         PPTX GENERATION WORKFLOW                            │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   CLAUDE.md    │     │  scratch/       │     │  docs/topics/   │
│  (instructions) │     │  SCRATCH.md     │     │  *.md           │
└────────┬────────┘     └────────┬────────┘     └────────┬────────┘
         │                       │                       │
         │     Research &        │      Organize &       │
         │     Compile           │      Structure        │
         └───────────┬───────────┴───────────┬───────────┘
                     │                       │
                     ▼                       ▼
           ┌─────────────────┐     ┌─────────────────┐
           │ docs/NARRATIVE  │     │ docs/OVERVIEW   │
           │     .md         │────▶│     .md         │
           │ (story flow)    │     │ (index/status)  │
           └────────┬────────┘     └─────────────────┘
                    │
                    ▼
         ┌─────────────────────┐
         │ docs/PRESENTATION   │
         │        .md          │◀─── Single source of truth
         │ (slide-by-slide)    │     for all slide content
         └──────────┬──────────┘
                    │
    ┌───────────────┼───────────────┐
    │               │               │
    ▼               ▼               ▼
┌────────┐   ┌────────────┐   ┌────────────┐
│figures/│   │ Template   │   │ workspace/ │
│SlideXXX│   │ PPTX       │   │ scripts    │
│-*.png  │   │            │   │            │
└───┬────┘   └─────┬──────┘   └─────┬──────┘
    │              │                │
    │              ▼                │
    │    ┌─────────────────┐        │
    │    │  working.pptx   │        │
    │    │ (N slides from  │◀───────┘
    │    │   template)     │    rearrange slides
    │    └────────┬────────┘
    │             │
    │             ▼
    │    ┌─────────────────┐
    │    │  replacement-   │
    │    │  text.json      │◀─── generate-replacement.py
    │    │ (title + body   │     parses PRESENTATION.md
    │    │  per slide)     │
    │    └────────┬────────┘
    │             │
    │             ▼
    │    ┌─────────────────┐
    │    │   replace.py    │
    │    │ (apply text to  │
    │    │  PPTX shapes)   │
    │    └────────┬────────┘
    │             │
    └──────┬──────┘
           │
           ▼
┌─────────────────────┐
│ Claude-Code-        │
│ Presentation.pptx   │◀─── FINAL OUTPUT
│ (figures inserted   │     (manual figure insertion)
│  manually)          │
└─────────────────────┘
```

## Step-by-Step Process

### Phase 1: Content Development

1. **CLAUDE.md** defines project goals and constraints
2. **scratch/SCRATCH.md** captures raw research notes
3. **docs/topics/*.md** organizes content by topic (10+ files)
4. **docs/NARRATIVE.md** establishes presentation flow (5-act structure)
5. **docs/PRESENTATION.md** defines slide-by-slide content

### Phase 2: Figure Preparation

1. Screenshots captured and saved to `figures/`
2. Files renamed with `SlideXXX-` prefix for sorting
3. Diagrams generated (e.g., workflow-improvement-loop.png)

### Phase 3: Template Preparation

```bash
# Template file provides consistent styling
2026-01-14_ClaudeCode.pptx (original template)
    │
    ▼
workspace/working.pptx (expanded to N slides)
```

### Phase 4: Text Generation

```bash
# Generate replacement JSON from PRESENTATION.md
python workspace/generate-replacement-fullsentences.py
    │
    ▼
workspace/replacement-text-fullsentences.json
```

**JSON Structure:**
```json
{
  "slides": [
    {
      "slide_index": 0,
      "replacements": [
        {"shape_name": "Title", "new_text": "Slide title here"},
        {"shape_name": "Content", "new_text": "• Bullet 1\n• Bullet 2"}
      ]
    }
  ]
}
```

### Phase 5: PPTX Generation

```bash
# Apply text replacements to working.pptx
python workspace/replace.py
    │
    ▼
Claude-Code-Presentation.pptx
```

### Phase 6: Manual Finishing

1. Open generated PPTX in PowerPoint
2. Insert figures from `figures/SlideXXX-*.png` at appropriate slides
3. Adjust layouts as needed
4. Add speaker notes

## File Inventory

| File | Purpose |
|------|---------|
| `2026-01-14_ClaudeCode.pptx` | Template with styling |
| `workspace/working.pptx` | Intermediate (N blank slides) |
| `workspace/generate-replacement-fullsentences.py` | Content generator |
| `workspace/replacement-text-fullsentences.json` | Structured content |
| `Claude-Code-Presentation.pptx` | Final output |
| `figures/SlideXXX-*.png` | Images for manual insertion |

## Key Design Decisions

1. **Template-based**: Preserves custom styling from user's template
2. **JSON intermediate**: Enables programmatic text replacement
3. **Manual figure insertion**: Allows precise positioning
4. **Slide-prefixed figures**: Easy to match figures to slides
5. **Full-sentence titles**: Each title conveys complete idea

## Regeneration Command

To regenerate the PPTX after updating PRESENTATION.md:

```bash
cd workspace/
python generate-replacement-fullsentences.py  # Update JSON
python replace.py                              # Apply to PPTX
```

Or use Claude Code with the pptx skill for automated generation.
