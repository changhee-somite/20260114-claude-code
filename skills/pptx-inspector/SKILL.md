---
name: pptx-inspector
description: "Validate PowerPoint presentations for layout issues, broken XML, and common problems. Use before visual review to catch issues that aren't visible in python-pptx object inspection."
---

# PPTX Inspector Skill

Validate PowerPoint presentations for common issues before visual review.

## When to Use This Skill

- User asks to "validate" or "check" a presentation
- After generating or modifying a PPTX file
- User reports visual glitches (text in wrong position, missing images)
- Before final review of a presentation
- User mentions "inspect presentation" or "find issues"

## Why This Skill Exists

**Critical discovery**: Python-pptx object properties can show correct values even when the underlying XML is broken.

For example, `shape.left = 0.42"` might be reported correctly, but the actual XML is missing the position offset element, causing PowerPoint to render incorrectly.

**Only by examining the raw XML can certain bugs be detected.**

## Script Location

```
scripts/pptx_inspector.py
```

## Usage

```bash
python scripts/pptx_inspector.py presentation.pptx [--level N] [--json] [--fail-on LEVEL]
```

## Arguments

| Argument | Default | Description |
|----------|---------|-------------|
| `pptx_file` | required | PowerPoint file to inspect |
| `--level` | 2 | Inspection depth (1-4) |
| `--json` | false | Output results as JSON |
| `--fail-on` | error | Exit with error if issues at this level or above |

## Validation Levels

### Level 1: Quick Object Inspection
- Zero dimensions (width=0, height=0)
- Negative positions
- Shapes outside slide bounds

**Limitation**: Cannot detect XML structure issues.

### Level 2: XML Structure Inspection (Recommended)
- **Missing position offset** (`<a:xfrm>` with `<a:ext>` but no `<a:off>`)
- Empty embed references
- Missing media files
- Broken relationship references

This level catches the critical position offset bug.

### Level 3: Content Validation
- Unreplaced placeholder text (`[Figure: ...]`, `Lorem ipsum`, `Click to add`)
- Extremely long text that may overflow
- Whitespace-only text boxes

### Level 4: Layout Overlap Detection
- Text overlapping with other text
- Shapes extending beyond slide boundaries

## Example Output

```
Found 2 issue(s):

🔴 [CRITICAL] Slide 5: xfrm has size but no position - will cause rendering issues
⚠️ [WARNING] Slide 12: May contain placeholder text: "[Figure: workflow diagram]..."
```

Or if clean:
```
✅ No issues found
```

## The Position Offset Bug

**What to look for in XML:**

```xml
<!-- BROKEN - Missing position -->
<a:xfrm>
  <a:ext cx="5943600" cy="4648200"/>
</a:xfrm>

<!-- CORRECT - Has both position and size -->
<a:xfrm>
  <a:off x="387391" y="1510234"/>
  <a:ext cx="5943600" cy="4648200"/>
</a:xfrm>
```

**Detection pattern:**
```python
if '<a:ext' in xfrm_block and '<a:off' not in xfrm_block:
    # CRITICAL: Missing position offset!
```

## Recommended Workflow

```
1. Generate/modify presentation
        ↓
2. Run inspector at level 2
        ↓
   Issues found? → Fix and retry
        ↓
   No issues → Continue
        ↓
3. Visual spot-check (human review)
        ↓
4. Done
```

## CI/CD Integration

Use exit codes for automated pipelines:

```bash
# Fail on any error or critical issue
python scripts/pptx_inspector.py output.pptx --fail-on error
echo $?  # 0 = pass, 1 = fail

# Fail only on critical issues
python scripts/pptx_inspector.py output.pptx --fail-on critical
```

## JSON Output

For programmatic processing:

```bash
python scripts/pptx_inspector.py presentation.pptx --json
```

```json
[
  {
    "slide": 5,
    "type": "MISSING_POSITION_OFFSET",
    "severity": "CRITICAL",
    "description": "xfrm has size but no position - will cause rendering issues",
    "xml_snippet": "<a:xfrm><a:ext cx=\"5943600\"..."
  }
]
```

## See Also

- `docs/PPTX-INSPECTOR-SKILL.md` - Full specification with code examples
- `skills/pptx-images` - Image insertion skill (includes validation)
- `docs/IMAGE-INSERTION-RESEARCH.md` - Research on the position offset bug
