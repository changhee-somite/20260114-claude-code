# Diagram Generation Workflow

This document describes the workflow for generating vector graphics diagrams in PowerPoint presentations from natural language descriptions.

## Overview

Rather than requiring authors to write structured diagram specifications, this workflow uses a two-stage approach:

1. **Human writes natural language** in PRESENTATION.md
2. **LLM preflight stage** interprets and converts to structured format
3. **Deterministic rendering** generates vector shapes in PPTX

```
PRESENTATION.md                    (human writes natural language)
    │
    ▼
[preflight_diagrams.py]            (LLM interprets intent)
    │
    ▼
PRESENTATION-processed.md          (structured diagram specs)
    │
    ▼
[generate_presentation.py]         (deterministic rendering)
    │
    ▼
final.pptx                         (vector graphics)
```

## Why Two Stages?

| Concern | Solution |
|---------|----------|
| Humans don't write structured YAML | Natural language in source file |
| LLM interpretation is non-deterministic | Preflight produces reviewable intermediate |
| Diagram spec changes need tracking | Processed file can be committed |
| Debugging layout issues | Structured format is inspectable |

---

## Convention: Natural Language Diagrams

### In PRESENTATION.md

Use `**Diagram Description**:` to describe a diagram in natural language:

```markdown
### Slide 7: Workflows compound—every update makes the system smarter

**Title**: Every update to CLAUDE.md, skills, and artifacts compounds your efficiency gains

**Content**:
- Session 1: Write CLAUDE.md with basic project context
- Session 5: Add common commands, conventions, warnings
- Session 20: Refined skills, custom hooks, team patterns
- Session 100: Agent works like a trained team member

**Diagram Description**:
A circular improvement loop with four stages: (1) Update CLAUDE.md,
(2) Agent behavior improves, (3) Refine skills based on experience,
(4) Knowledge compounds—then back to step 1. Use rounded boxes with
light blue fill and arrows connecting each stage in a cycle.

**Notes**: This is the architecture for rapid efficiency gains.
```

### Guidelines for Descriptions

- **State the diagram type**: "A circular loop", "A flowchart", "A comparison diagram"
- **List the elements**: Number them or describe relationships
- **Describe connections**: "leads to", "flows into", "loops back to"
- **Optional styling hints**: Colors, shapes, layout direction

---

## Structured Diagram Format

### After Preflight Processing

The LLM converts natural language to a structured specification:

```markdown
**Diagram**:
```diagram
type: cycle
title: Improvement Loop
position: right
width: 5.0

nodes:
  - id: update
    text: Update CLAUDE.md
  - id: better
    text: Agent behavior improves
  - id: refine
    text: Refine skills
  - id: compound
    text: Knowledge compounds

edges:
  - from: update
    to: better
  - from: better
    to: refine
  - from: refine
    to: compound
  - from: compound
    to: update

style:
  shape: rounded_rectangle
  fill: "#E8F4F8"
  line: "#2D5F73"
  text_color: "#1A3A47"
```
```

### Diagram Types

| Type | Description | Layout |
|------|-------------|--------|
| `cycle` | Circular flow returning to start | Shapes arranged in circle/rectangle loop |
| `flow` | Linear progression | Left→right or top→down |
| `flow_vertical` | Vertical progression | Top→down |
| `comparison` | Side-by-side elements | Two columns |
| `hierarchy` | Tree structure | Parent above children |

### Node Properties

| Property | Required | Description |
|----------|----------|-------------|
| `id` | Yes | Unique identifier for connections |
| `text` | Yes | Display text inside shape |
| `shape` | No | Override default shape (rectangle, diamond, etc.) |

### Edge Properties

| Property | Required | Description |
|----------|----------|-------------|
| `from` | Yes | Source node id |
| `to` | Yes | Target node id |
| `label` | No | Text label on the connector |

### Style Properties

| Property | Default | Description |
|----------|---------|-------------|
| `shape` | `rounded_rectangle` | Shape type for nodes |
| `fill` | `#E8F4F8` | Background color (hex) |
| `line` | `#2D5F73` | Border/connector color (hex) |
| `text_color` | `#1A3A47` | Text color (hex) |

### Position Properties

| Property | Default | Description |
|----------|---------|-------------|
| `position` | `right` | Where on slide: `right`, `left`, `center`, `full` |
| `width` | `5.0` | Width in inches |
| `top` | `1.5` | Top position in inches |

---

## Usage

### Step 1: Run Preflight

```bash
python scripts/preflight_diagrams.py \
    --input docs/PRESENTATION.md \
    --output docs/PRESENTATION-processed.md
```

This script:
1. Reads PRESENTATION.md
2. Finds all `**Diagram Description**:` blocks
3. Uses Claude to convert each to structured `**Diagram**:` format
4. Writes PRESENTATION-processed.md with conversions

### Step 2: Generate PPTX

```bash
python scripts/generate_presentation.py \
    --template template.pptx \
    --source docs/PRESENTATION-processed.md \
    --figures figures/ \
    --output output/final.pptx
```

The generator now:
1. Parses `**Diagram**:` blocks
2. Creates vector shapes using python-pptx
3. Positions diagrams according to specs

---

## Supported Shapes (python-pptx)

The following MSO_SHAPE types are available:

### Basic Shapes
- `RECTANGLE`, `ROUNDED_RECTANGLE`
- `OVAL`, `DIAMOND`
- `PARALLELOGRAM`, `TRAPEZOID`

### Arrows
- `RIGHT_ARROW`, `LEFT_ARROW`, `UP_ARROW`, `DOWN_ARROW`
- `CHEVRON`, `PENTAGON`

### Flowchart
- `FLOWCHART_PROCESS` (rectangle)
- `FLOWCHART_DECISION` (diamond)
- `FLOWCHART_TERMINATOR` (rounded ends)
- `FLOWCHART_DATA` (parallelogram)

### Connectors
- `STRAIGHT` - Direct line
- `ELBOW` - Right-angle bends
- `CURVED` - Smooth curves

---

## Example: Slide 7 Improvement Loop

### Input (PRESENTATION.md)

```markdown
**Diagram Description**:
A circular improvement loop with four stages: (1) Update CLAUDE.md,
(2) Agent behavior improves, (3) Refine skills based on experience,
(4) Knowledge compounds—then back to step 1. Use rounded boxes with
light blue fill and arrows connecting each stage in a cycle.
```

### Output (PRESENTATION-processed.md)

```markdown
**Diagram**:
```diagram
type: cycle
position: right
width: 5.0

nodes:
  - id: update
    text: Update CLAUDE.md
  - id: better
    text: Agent improves
  - id: refine
    text: Refine skills
  - id: compound
    text: Knowledge compounds

edges:
  - from: update
    to: better
  - from: better
    to: refine
  - from: refine
    to: compound
  - from: compound
    to: update

style:
  shape: rounded_rectangle
  fill: "#E8F4F8"
  line: "#2D5F73"
```
```

### Rendered Result

Four rounded rectangles arranged in a square pattern with arrows connecting them in sequence, creating a visual cycle.

---

## Future Enhancements

1. **Option B Integration**: Direct diagram generation during Claude Code sessions without intermediate file
2. **More diagram types**: Swimlanes, Gantt-style, network diagrams
3. **Smart layout**: Auto-positioning based on content length
4. **Theme integration**: Pull colors from PPTX template theme
5. **Interactive preview**: Generate PNG preview before PPTX

---

## Related Documentation

- [WORKFLOW-PPTX.md](WORKFLOW-PPTX.md) - Overall PPTX generation workflow
- [IMAGE-WORKFLOW.md](IMAGE-WORKFLOW.md) - Image insertion workflow
- [TEMPLATE-MODIFICATION-GUIDE.md](TEMPLATE-MODIFICATION-GUIDE.md) - Template customization
