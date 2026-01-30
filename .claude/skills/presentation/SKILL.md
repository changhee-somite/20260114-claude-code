---
name: presentation
description: "Create professional PowerPoint presentations for scientific/analysis results. Use when user requests a presentation, mentions 'create slides', 'make a deck', or needs to communicate analysis findings visually."
---

# Presentation Skill

Create professional PowerPoint presentations for scientific/analysis results.

## Core Philosophy: Minimize Cognitive Burden

The primary goal of any presentation is to **minimize cognitive burden** for your audience. Every design choice should reduce the mental effort required to understand your message.

- Reduce layers of translation between data and meaning
- Avoid extraneous information
- Highlight what you want the audience to focus on
- One point per slide - no more

## Workflow

1. **Create PRESENTATION.md** - Slide-by-slide specification in markdown
2. **Export figures** - Save plots to a `figures/` directory
3. **Generate PPTX** - Run `generate_presentation.py`
4. **Validate** - Run `pptx_inspector.py --level 3` to check for issues

## PRESENTATION.md Format

### Basic Structure

```markdown
### Slide 1: Title Slide
**Title**: Your Analysis Title

**Content**:
- Subtitle or date
- Author name

---

### Slide 2: Key finding as a complete sentence
**Title**: Key finding as a complete sentence

**Content**:
- Supporting point 1
- Supporting point 2

**Figure**: [description](figures/my_figure.png)

**Notes**: Speaker notes go here (optional)
```

### Slide Fields

| Field | Required | Description |
|-------|----------|-------------|
| `### Slide N: <title>` | Yes | Slide header with number and title |
| `**Title**:` | Yes | The slide title (must be a complete sentence) |
| `**Content**:` | No | Bullet points using `-` or `*` |
| `**Figure**:` | No | Image path: `[alt](path/to/image.png)` |
| `**Table**:` | No | Markdown table |
| `**Notes**:` | No | Speaker notes |

### Slide Types

| Type | When to Use |
|------|-------------|
| **Title slide** | First slide only, uses `First Slide.png` template |
| **Content slide** | Figure on right, text on left (most common) |
| **Text-only slide** | Full-width text, no figure |
| **Summary slide** | Key takeaways as bullet points |

### Example PRESENTATION.md

```markdown
### Slide 1: Title Slide
**Title**: Capsule Coverage Analysis

**Content**:
- BIG-008 Data Quality Assessment
- January 2026

---

### Slide 2: Day 9 contributes ~50% of valid data despite lowest coverage rate
**Title**: Day 9 contributes ~50% of valid data despite lowest coverage rate

**Content**:
- Day 9 has the most contexts (28) but lowest per-context coverage
- Despite this, Day 9 provides 4,200 of 8,600 total data points
- Prioritizing Day 9 coverage improvements would have highest impact

**Figure**: [Data points by day](figures/day_coverage_comparison.png)

---

### Slide 3: Key findings and next steps
**Title**: Key findings and next steps

**Content**:
- 8.6K data points available (12.6% of theoretical maximum)
- Day 9 is the highest-value target for coverage improvements
- 9.8K additional points blocked only by missing T0/DMSO controls
```

## Design Principles

### Slide Titles (Critical)

- **Every title must be a complete sentence: subject, verb, object**
- The sentence **must** describe what is in the slide
- The sentence should make one (and only one) point
- The reader should understand the takeaway without looking at the figure

**Good examples:**
- "Day 9 contributes ~50% of valid data despite lowest coverage rate"
- "9.8K data points are blocked only by missing T0/DMSO"
- "Intrinsic noise follows a 1/sqrt(n) fit"

**Bad examples:**
- "Data by day" (not a sentence, doesn't state conclusion)
- "Coverage analysis" (just a topic)
- "Results" (meaningless)

Use sentence case (capitalize first word and proper nouns only).

### Figures and Graphics

- **All axes must be labeled** and graphics must be legible
- **Highlight the relevant part of the graphic for the point being made** - don't make the audience search
- Limit dimensionality - most effective graphics are 1D or 2D, meaning simple bar graphs or very simple scatters. Avoid complex "2.5D" graphics with colors and so on.
- When there is a lot of overplotting in a scatter, consider using small multiples instead
- Don't make too many points in a single graph
- Break up complicated slides into multiple simpler ones

### Remove Jargon and Translation Layers

- **Remove all jargon** - labels aimed at a wider audience are more effective
- Search for layers of translation and remove them
- Instead of "CHIR + LDN" consider "skeletal muscle conditions"
- Instead of internal codes, use descriptive names, or at the very least use both, like "descriptive_name (internal_code)"
- If you must use a term, define it clearly first

### What NOT to Do

- Don't use white backgrounds (dark is preferred)
- Don't cram multiple points into one slide
- Don't use unlabeled axes or illegible graphics
- Don't use captions at the bottom (hard for people in back to see)

### Slide Structure

1. **Title slide**: Use `First Slide.png` template
2. **Introduction**: Must have a point and get to the point quickly
3. **Content slides**: One main figure per slide with conclusive title
4. **Summary slide**: Key takeaways as bullet points

## Templates

The default template is `.claude/skills/presentation/templates/cellularintelligence.pptx`, which includes:

- Slide master with proper font sizes and paragraph spacing
- Four layouts: Title, Title & Bullets, Two Content, 1_Two Content
- Dark background theme

The generator automatically handles layout selection and font scaling for content that would overflow.

## Validation Checklist

**Before finishing any presentation, validate that:**

1. **Every title is a complete sentence** stating the slide's conclusion
2. **Titles are self-contained** - fit within the slide without truncation
3. **Captions are legible** - 16pt minimum, no overflow
4. **Figures are clearly visible** - appropriately sized, not cut off
5. **All axes are labeled** and graphics are legible
6. **No jargon** without explanation
7. **One point per slide** - not overloaded
8. **Overall visual appeal** - professional and polished
9. **Consistent styling** - same fonts, colors, and layout patterns

Generate the presentation, then review and iterate until all validation criteria are met.

## Generation Commands

```bash
# Generate presentation from PRESENTATION.md
python .claude/skills/presentation/scripts/generate_presentation.py \
    --source PRESENTATION.md \
    --figures figures/ \
    --output presentation.pptx

# Validate the output
python .claude/skills/presentation/scripts/pptx_inspector.py presentation.pptx --level 3

# Auto-fix text overflow issues
python .claude/skills/presentation/scripts/pptx_inspector.py presentation.pptx --level 3 --fix
```

## References

- Arjun Raj's "How to Present Science"
- Nancy Duarte's book "Resonate"
- Example: `examples/capsule_coverage/PRESENTATION.md`
- Technical docs: See `README.md` for script details and advanced options
