---
name: pptx-tables
description: "Insert tables into PowerPoint presentations. Use when adding comparison tables, data grids, or structured information to slides."
---

# PPTX Table Insertion Skill

Add tables to PowerPoint presentations with customizable styling and positioning.

## When to Use This Skill

- User wants to add tables/data grids to specific slides
- User has a presentation that needs comparison tables
- User mentions "add table to slide X" or "create a comparison table"
- User provides data in tabular format (markdown tables, CSV-like data)

## Script Location

```
scripts/add_tables.py          # Standalone table insertion
scripts/table_renderer.py      # Core rendering module
```

## Usage

### Standalone Script

```bash
python scripts/add_tables.py \
    input.pptx \
    output.pptx \
    --mapping table-mapping.json \
    --text-width 6.5 \
    --table-left 7.0 \
    --table-top 1.5
```

### Arguments

| Argument | Default | Description |
|----------|---------|-------------|
| `input_pptx` | required | Input PowerPoint file |
| `output_pptx` | required | Output PowerPoint file |
| `--mapping` | required | Table mapping JSON file |
| `--text-width` | 6.5 | Width for text placeholder on table slides (inches) |
| `--table-left` | 7.0 | Left position for tables (inches) |
| `--table-top` | 1.5 | Top position for tables (inches) |
| `--table-width` | 5.5 | Table width (inches) |

## Table Mapping Format

Create a JSON file specifying which slides get tables:

```json
{
  "slides": [
    {
      "slide_number": 8,
      "description": "Feature comparison table",
      "tables": [
        {
          "headers": ["Feature", "Cursor", "Claude Code"],
          "rows": [
            ["Context Window", "Limited", "200k tokens"],
            ["Agentic Mode", "Partial", "Full support"],
            ["MCP Integration", "No", "Native"]
          ],
          "position": {
            "left": 7.0,
            "top": 1.5,
            "width": 5.5
          },
          "style": {
            "header_fill": "#4472C4",
            "header_text": "#FFFFFF",
            "use_alt_rows": true
          }
        }
      ]
    }
  ]
}
```

### Using Markdown Tables

You can also provide markdown format:

```json
{
  "slides": [
    {
      "slide_number": 10,
      "tables": [
        {
          "markdown": "| Feature | Status |\n|---------|--------|\n| Images | Done |\n| Tables | New |"
        }
      ]
    }
  ]
}
```

## Integration with generate_presentation.py

Tables are automatically detected and rendered when using the unified generator.

### PRESENTATION.md Format

Add tables to slides using the `**Table**:` directive:

```markdown
### Slide 8: Claude Code offers significant advantages over Cursor

**Title**: Claude Code offers significant advantages over Cursor

**Content**:
- Direct integration with Claude's latest models
- Full agentic capabilities

**Table**:
```table
| Feature | Cursor | Claude Code |
|---------|--------|-------------|
| Context | Limited | 200k tokens |
| Agentic | Partial | Full |
```
```

Or using YAML-like format:

```markdown
**Table**:
```table
headers:
  - Feature
  - Cursor
  - Claude Code
rows:
  - [Context, Limited, 200k tokens]
  - [Agentic Mode, Partial, Full support]
style:
  header_fill: "#4472C4"
```
```

## Style Options

| Option | Default | Description |
|--------|---------|-------------|
| `header_fill` | #4472C4 | Header background color (hex) |
| `header_text` | #FFFFFF | Header text color |
| `row_fill` | #FFFFFF | Row background color |
| `alt_row_fill` | #F2F2F2 | Alternating row color |
| `text_color` | #000000 | Body text color |
| `font_size` | 10 | Font size in points |
| `header_font_size` | 11 | Header font size |
| `header_bold` | true | Bold header text |
| `use_alt_rows` | true | Alternate row colors |

## Validation

Tables are validated by `pptx_inspector.py` at multiple levels:

### Level 1 - Object Validation
- Empty tables (no rows/columns)
- Empty header cells
- Mismatched column counts
- Narrow column widths (< 0.3")
- Empty data rows

### Level 4 - Overlap Detection
- Table overlapping with text content
- Multiple tables overlapping

### Run Validation

```bash
python scripts/pptx_inspector.py output.pptx --level 4
```

## Critical Implementation Detail

The scripts correctly handle the **python-pptx position offset bug**:

```python
# All four properties must be set for complete XML
left = Inches(config.left)
top = Inches(config.top)
width = Inches(config.width)
height = Inches(height)

table_shape = slide.shapes.add_table(
    num_rows, num_cols,
    left, top, width, height
)
```

## Workflow Integration

### Three-Stage Workflow

```
Stage 1: Text Replacement (PPTX skill)
    template.pptx → replace.py → text-done.pptx

Stage 2: Image/Diagram/Table Insertion
    text-done.pptx + mappings → add_*.py → enriched.pptx

Stage 3: Validation
    enriched.pptx → pptx_inspector.py → final.pptx
```

### Or Unified Generation

```
PRESENTATION.md + template.pptx → generate_presentation.py → final.pptx
```

## Example

```bash
# Add tables to slides 8 and 15
python scripts/add_tables.py \
    workspace/text-replaced.pptx \
    output/with-tables.pptx \
    --mapping workspace/table-mapping.json

# Validate the output
python scripts/pptx_inspector.py output/with-tables.pptx --level 4
```

## See Also

- `skills/pptx-images` - Image insertion
- `skills/pptx-inspector` - Presentation validation
- `scripts/diagram_renderer.py` - Vector diagram generation
