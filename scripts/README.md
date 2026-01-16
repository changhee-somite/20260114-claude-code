# Scripts

## Working Scripts

### add_images_only.py ✅

**Status**: Working, validated

Minimal script that adds images to presentations without modifying text content.

**Usage:**
```bash
python add_images_only.py \
    input.pptx \
    output.pptx \
    --mapping image-mapping.json
```

**Features:**
- Resizes text placeholders to make room for images
- Inserts images at specified positions
- Preserves all text content unchanged
- Includes validation to catch common issues
- Handles the python-pptx position offset bug correctly

---

## Deprecated Scripts

### generate_presentation.py ❌

**Status**: Deprecated - do not use

This script attempted to parse PRESENTATION.md and regenerate all text content. It caused issues:
- Destroyed existing text formatting
- Created vertical text artifacts
- Didn't preserve original paragraph styles

**Use instead**: The two-stage workflow:
1. `replace.py` (from PPTX skill) for text
2. `add_images_only.py` for images

---

## Workflow

```
┌─────────────────────────────────────────┐
│  Stage 1: Text (PPTX Skill)              │
│                                          │
│  template → rearrange.py → working.pptx  │
│  working.pptx + replacement.json         │
│      → replace.py → text-done.pptx       │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  Stage 2: Images (add_images_only.py)    │
│                                          │
│  text-done.pptx + image-mapping.json     │
│      → add_images_only.py → final.pptx   │
└─────────────────────────────────────────┘
```

---

## Image Mapping Format

```json
{
  "slides": [
    {
      "slide_number": 5,
      "images": [
        {"path": "../figures/Slide005-image.png"}
      ]
    }
  ]
}
```

Paths are relative to the mapping file location.
