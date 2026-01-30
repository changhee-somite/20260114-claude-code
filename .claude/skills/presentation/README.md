# Presentation Skill - Developer Documentation

Technical reference for the presentation generation scripts. For usage guidance, see `SKILL.md`.

## Scripts Overview

| Script | Purpose |
|--------|---------|
| `generate_presentation.py` | Convert PRESENTATION.md → PPTX |
| `pptx_inspector.py` | Validate and fix presentations |
| `add_images_only.py` | Insert images into existing PPTX |
| `table_renderer.py` | Render markdown tables (used internally) |
| `diagram_renderer.py` | Render vector diagrams (used internally) |

## generate_presentation.py

Converts a PRESENTATION.md file into a PowerPoint presentation.

### Usage

```bash
python scripts/generate_presentation.py \
    --source PRESENTATION.md \
    --figures figures/ \
    --output presentation.pptx \
    [--template template.pptx]
```

### Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `--source` | Yes | Path to PRESENTATION.md |
| `--figures` | No | Directory containing figure images (default: figures/ relative to source) |
| `--output` | Yes | Output PPTX file path |
| `--template` | No | Base PPTX template (default: `templates/cellularintelligence.pptx`) |

### Slide Layout Logic

The generator uses the slide master layouts from the PPTX template:

- **Layout 0 (Title)**: Title slides with subtitle
- **Layout 1 (Title & Bullets)**: Text-only content slides
- **Layout 2 (Two Content)**: Side-by-side layout (text left, image/diagram right)
- **Layout 3 (1_Two Content)**: Stacked layout (image top, text bottom)

### Proactive Overflow Detection

The generator automatically detects content that would overflow placeholders and scales fonts to fit:

- Uses template font sizes (24pt level 0, 18pt level 1, etc.)
- Accounts for paragraph spacing from slide master (12pt)
- Scales fonts proportionally when overflow detected (minimum 10pt)
- Prints a **Content Compression Summary** showing which slides were scaled

```
============================================================
CONTENT COMPRESSION SUMMARY
============================================================
  Slide 2: What is a training data point?...
    Font scaled to 83% (24pt -> 19pt)
```

## pptx_inspector.py

Validates PowerPoint files and optionally fixes common issues.

### Usage

```bash
# Basic validation
python scripts/pptx_inspector.py presentation.pptx

# Detailed content check
python scripts/pptx_inspector.py presentation.pptx --level 3

# Auto-fix text overflow
python scripts/pptx_inspector.py presentation.pptx --level 3 --fix

# Save fixed version to new file
python scripts/pptx_inspector.py presentation.pptx --fix --fix-output fixed.pptx
```

### Inspection Levels

| Level | Checks |
|-------|--------|
| 1 | Quick: dimensions, positions |
| 2 | XML: position offset bugs (default) |
| 3 | Content: text overflow, placeholder issues |
| 4 | Full: all above + overlap detection |

### Options

```bash
# Fix options
--fix                    # Auto-fix TEXT_OVERFLOW issues
--fix-output FILE        # Save fixed version to separate file
--min-font-size N        # Minimum font size when fixing (default: 10)

# Output options
--json                   # Output as JSON
--quiet                  # Only output if issues found
--fail-on LEVEL          # Exit with error if issues at level (critical/error/warning/info)
```

### Issue Types Detected

| Issue | Level | Auto-fixable |
|-------|-------|--------------|
| `TEXT_OVERFLOW` | error | Yes (shrinks font) |
| `POSITION_OFFSET` | warning | No |
| `EMPTY_PLACEHOLDER` | info | No |
| `SHAPE_OVERLAP` | warning | No |

## add_images_only.py

Inserts images into an existing PowerPoint file without modifying other content.

### Usage

```bash
python scripts/add_images_only.py \
    --input base.pptx \
    --images figures/ \
    --output with_images.pptx
```

## Implementation Details

### Template Backgrounds

Templates are PNG images inserted as the first shape on each slide, then moved to the back of the z-order:

```python
def add_background(slide, template_path):
    bg = slide.shapes.add_picture(
        template_path,
        Inches(0), Inches(0),
        width=Inches(13.333),
        height=Inches(7.5)
    )
    spTree = slide.shapes._spTree
    sp = bg._element
    spTree.remove(sp)
    spTree.insert(2, sp)
```

### Figure Frames

White rounded rectangles are added behind figures to ensure visibility on dark backgrounds:

```python
def add_figure_frame(slide, left, top, width, height):
    padding = 0.15
    frame = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(left - padding),
        Inches(top - padding),
        Inches(width + 2 * padding),
        Inches(height + 2 * padding)
    )
    frame.fill.solid()
    frame.fill.fore_color.rgb = RGBColor(255, 255, 255)
    frame.line.fill.background()
    frame.adjustments[0] = 0.05
```

### Color Constants

```python
TITLE_COLOR = RGBColor(255, 255, 255)  # White
TEXT_COLOR = RGBColor(230, 230, 230)   # Light gray (#E6E6E6)
```

### Dimensions

- Slide size: 13.333" x 7.5" (16:9 widescreen)
- Title area: 0.5" margins, 28pt font
- Content area: Two-column (text 6.5", figure 5.5")
- Figure max height: 5.5"

## Dependencies

```bash
pip install python-pptx Pillow
```

## Templates

The default template is `templates/cellularintelligence.pptx`:

| File | Usage |
|------|-------|
| `templates/cellularintelligence.pptx` | Default PPTX template with slide master layouts |

### Template Slide Master Requirements

The template slide master defines font sizes and paragraph spacing that the generator uses for overflow detection:

**Font sizes** (bodyStyle lvl1pPr through lvl5pPr):
- Level 0: 24pt, Level 1: 18pt, Level 2: 15pt, Level 3: 12pt, Level 4: 10pt

**Paragraph spacing** (spcBef - space before each paragraph):
- Recommended: 12pt (1200 in hundredths of a point)
- Too large spacing (e.g., 29.5pt) causes overflow with dense content

**Line spacing** (lnSpc):
- Template uses 100% (single spacing)

### Modifying Template Spacing

To adjust paragraph spacing in PowerPoint:
1. View → Slide Master
2. Select the master slide (top one)
3. Select a text placeholder
4. Right-click → Paragraph → Spacing Before
5. Set to ~12pt for all bullet levels

### Legacy Templates

| File | Usage |
|------|-------|
| `First Slide.png` | Legacy title slide background |
| `template.png` | Legacy content slide background |

## Example

See `examples/capsule_coverage/` for a complete working example:

```
examples/capsule_coverage/
├── PRESENTATION.md      # 8-slide specification
├── figures/             # Source images
│   ├── context_by_day.png
│   ├── context_coverage.png
│   └── ...
└── expected/
    └── 1008.pptx       # Reference output
```
