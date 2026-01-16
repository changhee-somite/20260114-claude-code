---
name: pptx-images
description: "Insert images into PowerPoint presentations while preserving text content. Use when adding figures, screenshots, or diagrams to slides after text replacement is complete."
---

# PPTX Image Insertion Skill

Add images to PowerPoint presentations without modifying existing text content.

## When to Use This Skill

- User wants to add images/figures to specific slides
- User has a presentation with text already set and needs images added
- User mentions "add image to slide X" or "insert figure"
- After using the standard PPTX skill for text replacement

## Script Location

```
scripts/add_images_only.py
```

## Usage

```bash
python scripts/add_images_only.py \
    input.pptx \
    output.pptx \
    --mapping image-mapping.json \
    --text-width 6.5 \
    --image-left 7.0 \
    --image-top 1.5
```

## Arguments

| Argument | Default | Description |
|----------|---------|-------------|
| `input_pptx` | required | Input file (with text already set) |
| `output_pptx` | required | Output file |
| `--mapping` | required | Image mapping JSON file |
| `--text-width` | 6.5 | Width for text placeholder on image slides (inches) |
| `--image-left` | 7.0 | Left position for images (inches) |
| `--image-top` | 1.5 | Top position for images (inches) |
| `--image-max-width` | 5.5 | Maximum image width (inches) |
| `--image-max-height` | 5.5 | Maximum image height (inches) |

## Image Mapping Format

Create a JSON file specifying which slides get images:

```json
{
  "slides": [
    {
      "slide_number": 5,
      "description": "Blog screenshot on right",
      "images": [
        {"path": "../figures/Slide005-image.png"}
      ]
    },
    {
      "slide_number": 15,
      "images": [
        {"path": "../figures/Slide015-screenshot.png"}
      ]
    }
  ]
}
```

- `slide_number` is 1-indexed
- `path` is relative to the mapping file location
- Multiple images per slide are supported

## Two-Stage Workflow

This skill is part of a two-stage workflow:

```
Stage 1: Text Replacement (PPTX skill)
    template.pptx → rearrange.py → working.pptx
    working.pptx + replacement.json → replace.py → text-done.pptx

Stage 2: Image Insertion (this skill)
    text-done.pptx + image-mapping.json → add_images_only.py → final.pptx
```

## Critical Implementation Detail

The script correctly handles the **python-pptx position offset bug**:

```python
# Must set all four properties to generate complete XML
original_left = shape.left
original_top = shape.top
original_height = shape.height
shape.left = original_left      # Preserve position
shape.top = original_top        # Preserve position
shape.width = Inches(new_width)
shape.height = original_height  # Preserve height
```

Setting only `shape.width` creates broken XML missing the `<a:off>` element.

## Validation

The script includes built-in validation that checks:
1. Placeholder dimensions (height > 0.5", width > 2.0")
2. Image presence on mapped slides
3. XML structure (all `<a:xfrm>` elements have both `<a:off>` and `<a:ext>`)

## Example

```bash
# Add images to slides 5, 10, 15
python scripts/add_images_only.py \
    workspace/output-text-replaced.pptx \
    output/final-presentation.pptx \
    --mapping workspace/image-mapping.json
```

## See Also

- `docs/PPTX-IMAGE-SKILL-SPEC.md` - Full specification
- `docs/IMAGE-WORKFLOW.md` - Workflow documentation
- `skills/pptx-inspector` - Validate presentations for issues
