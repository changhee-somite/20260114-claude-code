# PPTX with Images: Skill Specification

**Version**: 2.0
**Date**: 2026-01-16
**Status**: Working - Validated

---

## Overview

This skill generates PowerPoint presentations from markdown source files with properly integrated images. It uses a **two-stage workflow** that preserves template formatting while allowing text replacement and image insertion.

---

## Critical Lesson Learned

### The Position Offset Bug

When modifying placeholder dimensions in python-pptx, a **critical bug** occurs:

```python
# ❌ WRONG - Creates broken XML
shape.width = Inches(6.5)  # This creates <a:xfrm> with only <a:ext>, no <a:off>

# ✅ CORRECT - Creates complete XML
original_left = shape.left
original_top = shape.top
original_height = shape.height
shape.left = original_left      # Must set position
shape.top = original_top        # Must set position
shape.width = Inches(6.5)       # Then set size
shape.height = original_height  # Then set size
```

**Why this matters**: PowerPoint placeholders inherit position from slide layouts. When you set only width, python-pptx creates:

```xml
<!-- ❌ BROKEN - Missing position -->
<a:xfrm>
  <a:ext cx="5943600" cy="4648200"/>
</a:xfrm>

<!-- ✅ CORRECT - Has both position and size -->
<a:xfrm>
  <a:off x="387391" y="1510234"/>
  <a:ext cx="5943600" cy="4648200"/>
</a:xfrm>
```

Without `<a:off>`, PowerPoint doesn't know where to position the shape, causing visual glitches like text appearing in wrong locations.

---

## Workflow Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│  STAGE 1: TEXT REPLACEMENT (existing PPTX skill)                        │
│                                                                          │
│  template.pptx ──→ rearrange.py ──→ working.pptx                        │
│                          ↓                                               │
│  replacement-text.json + working.pptx ──→ replace.py ──→ text-done.pptx │
│                                                                          │
│  ✓ Text content is correct                                              │
│  ✓ All formatting preserved                                              │
│  ✓ Placeholders at original positions/sizes                              │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  STAGE 2: IMAGE INSERTION (add_images_only.py)                          │
│                                                                          │
│  text-done.pptx + image-mapping.json ──→ add_images_only.py ──→ final   │
│                                                                          │
│  For each slide with images:                                             │
│    1. Resize text placeholder width (preserving position + height)       │
│    2. Insert image at specified position                                 │
│    3. Validate XML structure                                             │
│                                                                          │
│  ✓ Text unchanged                                                        │
│  ✓ Images properly positioned                                            │
│  ✓ No visual glitches                                                    │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## File Locations

```
project/
├── docs/
│   ├── PRESENTATION.md              # Slide content source
│   └── PPTX-IMAGE-SKILL-SPEC.md     # This specification
├── figures/
│   ├── Slide005-*.png               # Images named by slide number
│   ├── Slide006-*.png
│   └── ...
├── scripts/
│   └── add_images_only.py           # Image insertion script
├── workspace/
│   ├── working-49.pptx              # Rearranged template
│   ├── output-text-replaced.pptx    # After text replacement
│   ├── image-mapping-v2.json        # Image placement config
│   └── replacement-text-49.json     # Text replacement data
└── 2026-01-14_ClaudeCode.pptx       # Original template
```

---

## Scripts

### add_images_only.py

Minimal script that ONLY resizes placeholders and inserts images. Does NOT modify text.

**Usage:**
```bash
python scripts/add_images_only.py \
    workspace/output-text-replaced.pptx \
    final-presentation.pptx \
    --mapping workspace/image-mapping-v2.json \
    --text-width 6.5 \
    --image-left 7.0 \
    --image-top 1.5
```

**Arguments:**

| Argument | Default | Description |
|----------|---------|-------------|
| `input_pptx` | required | Input file (with text already set) |
| `output_pptx` | required | Output file |
| `--mapping` | required | Image mapping JSON file |
| `--text-width` | 6.5 | Width for text placeholder on image slides |
| `--image-left` | 7.0 | Left position for images |
| `--image-top` | 1.5 | Top position for images |
| `--image-max-width` | 5.5 | Maximum image width |
| `--image-max-height` | 5.5 | Maximum image height |

**Key function - resize with position preservation:**
```python
def resize_placeholder_width(shape, new_width_inches):
    """
    Resize placeholder width while preserving height AND position.

    CRITICAL: Must set all four properties to generate complete XML.
    """
    original_left = shape.left
    original_top = shape.top
    original_height = shape.height

    shape.left = original_left      # Preserve position
    shape.top = original_top        # Preserve position
    shape.width = Inches(new_width_inches)
    shape.height = original_height  # Preserve height

    return shape
```

---

## Image Mapping Format

**image-mapping-v2.json:**
```json
{
  "_comment": "Image mapping - slide numbers are 1-indexed",
  "slides": [
    {
      "slide_number": 5,
      "description": "Blog screenshot on right",
      "images": [
        {
          "path": "../figures/Slide005-blog-mike-tech-death-of-software.png"
        }
      ]
    },
    {
      "slide_number": 15,
      "description": "Status tab screenshot",
      "images": [
        {
          "path": "../figures/Slide015-status-tab-usage.png"
        }
      ]
    }
  ]
}
```

---

## Validation

The script includes built-in validation that checks:

1. **Placeholder dimensions** - Height > 0.5", Width > 2.0"
2. **Image presence** - Each mapped slide has an image
3. **XML structure** - All `<a:xfrm>` elements have both `<a:off>` and `<a:ext>`

**Validation output:**
```
VALIDATION
==================================================
✅ All validation checks passed!
```

Or if issues found:
```
VALIDATION
==================================================
❌ Found 2 issue(s):
  - Slide 5: xfrm missing position offset (will cause display issues)
  - Slide 15: Text placeholder height too small (0.00")
```

---

## Complete Workflow Example

```bash
# Step 1: Rearrange template slides (if needed)
python skills/pptx/scripts/rearrange.py \
    2026-01-14_ClaudeCode.pptx \
    workspace/working-49.pptx \
    0,1,1,1,1,1,...  # Slide indices to use

# Step 2: Extract text inventory
python skills/pptx/scripts/inventory.py \
    workspace/working-49.pptx \
    workspace/text-inventory-49.json

# Step 3: Generate replacement text (manual or scripted)
# Create workspace/replacement-text-49.json

# Step 4: Apply text replacement
python skills/pptx/scripts/replace.py \
    workspace/working-49.pptx \
    workspace/replacement-text-49.json \
    workspace/output-text-replaced.pptx

# Step 5: Add images
python scripts/add_images_only.py \
    workspace/output-text-replaced.pptx \
    final-presentation.pptx \
    --mapping workspace/image-mapping-v2.json

# Output: final-presentation.pptx with correct text AND images
```

---

## Troubleshooting

### Issue: Text appears in wrong position / overlaps with title

**Cause**: `<a:xfrm>` in XML has size but no position offset.

**Solution**: Use `add_images_only.py` which sets all four properties (left, top, width, height) together.

### Issue: Text placeholder height is 0

**Cause**: Setting width resets height in python-pptx.

**Solution**: Save and restore height after setting width.

### Issue: Vertical text (one character per line)

**Cause**: Text content was incorrectly modified by a script that rewrites text.

**Solution**: Use the two-stage workflow - `replace.py` for text, `add_images_only.py` for images only.

### Issue: "[Figure: ...]" appears as literal text

**Cause**: Figure references from PRESENTATION.md were included in replacement text.

**Solution**: Filter out figure references when generating replacement-text.json, or don't parse PRESENTATION.md directly - use the already-generated replacement text.

---

## Layout Dimensions Reference

For a 13.33" × 7.50" slide (standard widescreen):

| Element | Left | Top | Width | Height |
|---------|------|-----|-------|--------|
| Title | 0.42" | 0.42" | 11.49" | 0.66" |
| Body (full) | 0.42" | 1.65" | 11.49" | 5.08" |
| Body (with image) | 0.42" | 1.65" | **6.50"** | 5.08" |
| Image | **7.00"** | **1.50"** | 5.50" | varies |
| Gap between text/image | 0.08" | - | - | - |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-16 | Initial specification |
| 2.0 | 2026-01-16 | Fixed position offset bug, added validation, confirmed working |
