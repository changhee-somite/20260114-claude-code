# PPTX Inspector Skill: Validating PowerPoint Presentations

**Version**: 1.0
**Date**: 2026-01-16
**Purpose**: Detect layout breakage and common issues in PowerPoint files before visual review

---

## Why This Skill Exists

During the development of the image insertion workflow, a critical lesson was learned:

> **Python object properties can show correct values even when the underlying XML is broken.**

The python-pptx library reported `shape.left = 0.42"` and `shape.top = 1.65"` correctly, but the actual XML was missing the position offset element, causing PowerPoint to render the shape in the wrong location.

**Only by examining the raw XML could the bug be detected.**

This skill documents validation techniques that catch issues before they reach visual review.

---

## Validation Levels

### Level 1: Python Object Inspection (Quick, but Limited)

```python
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

def inspect_level1(pptx_path):
    """Quick inspection using python-pptx object model."""
    issues = []
    prs = Presentation(pptx_path)

    for i, slide in enumerate(prs.slides):
        slide_num = i + 1

        for shape in slide.shapes:
            # Check 1: Zero dimensions
            if shape.width == 0:
                issues.append(f"Slide {slide_num}: {shape.name} has width=0")
            if shape.height == 0:
                issues.append(f"Slide {slide_num}: {shape.name} has height=0")

            # Check 2: Negative positions
            if shape.left < 0:
                issues.append(f"Slide {slide_num}: {shape.name} has negative left")
            if shape.top < 0:
                issues.append(f"Slide {slide_num}: {shape.name} has negative top")

            # Check 3: Shape outside slide bounds
            slide_width = prs.slide_width
            slide_height = prs.slide_height
            if shape.left + shape.width > slide_width * 1.1:  # 10% tolerance
                issues.append(f"Slide {slide_num}: {shape.name} extends beyond slide width")
            if shape.top + shape.height > slide_height * 1.1:
                issues.append(f"Slide {slide_num}: {shape.name} extends beyond slide height")

    return issues
```

**Limitations**: Cannot detect XML structure issues like missing `<a:off>` elements.

---

### Level 2: XML Structure Inspection (Thorough)

This is the critical validation level that catches the position offset bug.

```python
import zipfile
import re
from pathlib import Path

def inspect_level2_xml(pptx_path):
    """Deep inspection of XML structure."""
    issues = []

    with zipfile.ZipFile(pptx_path, 'r') as z:
        # Find all slide XML files
        slide_files = [f for f in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml', f)]

        for slide_file in sorted(slide_files):
            slide_num = int(re.search(r'slide(\d+)', slide_file).group(1))

            with z.open(slide_file) as f:
                content = f.read().decode('utf-8')

                # Check 1: xfrm with ext but without off (THE CRITICAL BUG)
                xfrm_blocks = re.findall(r'<a:xfrm>.*?</a:xfrm>', content, re.DOTALL)
                for block in xfrm_blocks:
                    has_off = '<a:off' in block
                    has_ext = '<a:ext' in block

                    if has_ext and not has_off:
                        issues.append({
                            'slide': slide_num,
                            'type': 'MISSING_POSITION_OFFSET',
                            'severity': 'CRITICAL',
                            'description': 'xfrm has size but no position - will cause rendering issues',
                            'xml_snippet': block[:200]
                        })

                # Check 2: Empty spPr that should have transforms
                # (This is actually OK for placeholders that inherit from layout)

                # Check 3: Malformed XML references
                if 'r:embed=""' in content:
                    issues.append({
                        'slide': slide_num,
                        'type': 'EMPTY_EMBED_REFERENCE',
                        'severity': 'ERROR',
                        'description': 'Empty embed reference - image may not display'
                    })

                # Check 4: Missing relationship references
                embed_ids = re.findall(r'r:embed="(rId\d+)"', content)

        # Check relationships file
        for slide_file in slide_files:
            slide_num = int(re.search(r'slide(\d+)', slide_file).group(1))
            rels_file = slide_file.replace('slides/', 'slides/_rels/') + '.rels'

            try:
                with z.open(rels_file) as f:
                    rels_content = f.read().decode('utf-8')

                    # Check for broken image references
                    if 'Target="../media/' in rels_content:
                        media_refs = re.findall(r'Target="\.\./media/([^"]+)"', rels_content)
                        media_files = [f for f in z.namelist() if f.startswith('ppt/media/')]

                        for ref in media_refs:
                            expected = f'ppt/media/{ref}'
                            if expected not in media_files:
                                issues.append({
                                    'slide': slide_num,
                                    'type': 'MISSING_MEDIA_FILE',
                                    'severity': 'ERROR',
                                    'description': f'Referenced media file not found: {ref}'
                                })
            except KeyError:
                pass  # No rels file is OK for some slides

    return issues
```

---

### Level 3: Content Validation

```python
def inspect_level3_content(pptx_path):
    """Validate content integrity."""
    issues = []
    prs = Presentation(pptx_path)

    for i, slide in enumerate(prs.slides):
        slide_num = i + 1

        for shape in slide.shapes:
            if not hasattr(shape, 'text_frame'):
                continue

            if not shape.has_text_frame:
                continue

            text = shape.text_frame.text

            # Check 1: Placeholder text not replaced
            placeholder_patterns = [
                r'\[.*?\]',  # [Figure: something]
                r'Lorem ipsum',
                r'Click to add',
                r'Title Text',
                r'Body Level',
            ]

            for pattern in placeholder_patterns:
                if re.search(pattern, text, re.IGNORECASE):
                    issues.append({
                        'slide': slide_num,
                        'shape': shape.name,
                        'type': 'UNREPLACED_PLACEHOLDER',
                        'severity': 'WARNING',
                        'description': f'May contain placeholder text: "{text[:50]}..."'
                    })
                    break

            # Check 2: Extremely long text that might overflow
            if len(text) > 1000:
                issues.append({
                    'slide': slide_num,
                    'shape': shape.name,
                    'type': 'VERY_LONG_TEXT',
                    'severity': 'WARNING',
                    'description': f'Text length ({len(text)} chars) may overflow placeholder'
                })

            # Check 3: Text with only whitespace
            if text and not text.strip():
                issues.append({
                    'slide': slide_num,
                    'shape': shape.name,
                    'type': 'WHITESPACE_ONLY',
                    'severity': 'INFO',
                    'description': 'Shape contains only whitespace'
                })

    return issues
```

---

### Level 4: Layout Overlap Detection

```python
def inspect_level4_overlaps(pptx_path, tolerance=0.1):
    """Detect overlapping shapes that might cause visual issues."""
    issues = []
    prs = Presentation(pptx_path)

    def shapes_overlap(s1, s2):
        """Check if two shapes overlap."""
        # Convert to inches for readability
        l1, t1 = s1.left / 914400, s1.top / 914400
        r1, b1 = (s1.left + s1.width) / 914400, (s1.top + s1.height) / 914400

        l2, t2 = s2.left / 914400, s2.top / 914400
        r2, b2 = (s2.left + s2.width) / 914400, (s2.top + s2.height) / 914400

        # Add tolerance
        h_overlap = not (r1 <= l2 + tolerance or l1 >= r2 - tolerance)
        v_overlap = not (b1 <= t2 + tolerance or t1 >= b2 - tolerance)

        return h_overlap and v_overlap

    for i, slide in enumerate(prs.slides):
        slide_num = i + 1
        shapes = list(slide.shapes)

        for j, s1 in enumerate(shapes):
            for s2 in shapes[j+1:]:
                # Skip slide number placeholders
                if 'Slide Number' in s1.name or 'Slide Number' in s2.name:
                    continue

                if shapes_overlap(s1, s2):
                    # Determine if this is expected (e.g., title over background)
                    # or problematic (e.g., text over text)

                    s1_has_text = hasattr(s1, 'text_frame') and s1.has_text_frame and s1.text_frame.text.strip()
                    s2_has_text = hasattr(s2, 'text_frame') and s2.has_text_frame and s2.text_frame.text.strip()

                    if s1_has_text and s2_has_text:
                        issues.append({
                            'slide': slide_num,
                            'type': 'TEXT_OVERLAP',
                            'severity': 'WARNING',
                            'description': f'"{s1.name}" overlaps with "{s2.name}" - both have text',
                            'shapes': [s1.name, s2.name]
                        })

    return issues
```

---

## Complete Inspector Script

```python
#!/usr/bin/env python3
"""
PPTX Inspector - Validate PowerPoint presentations for common issues.

Usage:
    python pptx_inspector.py presentation.pptx [--level N] [--json]
"""

import argparse
import json
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='Inspect PPTX for issues')
    parser.add_argument('pptx_file', help='PowerPoint file to inspect')
    parser.add_argument('--level', type=int, default=2, choices=[1,2,3,4],
                       help='Inspection depth (1=quick, 2=xml, 3=content, 4=overlaps)')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--fail-on', choices=['critical', 'error', 'warning', 'info'],
                       default='error', help='Exit with error code if issues at this level or above')

    args = parser.parse_args()

    all_issues = []

    # Run inspections up to requested level
    if args.level >= 1:
        all_issues.extend(inspect_level1(args.pptx_file))
    if args.level >= 2:
        all_issues.extend(inspect_level2_xml(args.pptx_file))
    if args.level >= 3:
        all_issues.extend(inspect_level3_content(args.pptx_file))
    if args.level >= 4:
        all_issues.extend(inspect_level4_overlaps(args.pptx_file))

    # Output
    if args.json:
        print(json.dumps(all_issues, indent=2))
    else:
        if not all_issues:
            print("✅ No issues found")
        else:
            severity_order = {'CRITICAL': 0, 'ERROR': 1, 'WARNING': 2, 'INFO': 3}
            sorted_issues = sorted(all_issues,
                                  key=lambda x: (x.get('severity', 'INFO'), x.get('slide', 0)))

            print(f"Found {len(all_issues)} issue(s):\n")
            for issue in sorted_issues:
                sev = issue.get('severity', 'INFO')
                icon = {'CRITICAL': '🔴', 'ERROR': '❌', 'WARNING': '⚠️', 'INFO': 'ℹ️'}.get(sev, '?')
                print(f"{icon} [{sev}] Slide {issue.get('slide', '?')}: {issue.get('description', issue)}")

    # Exit code
    fail_levels = {
        'critical': ['CRITICAL'],
        'error': ['CRITICAL', 'ERROR'],
        'warning': ['CRITICAL', 'ERROR', 'WARNING'],
        'info': ['CRITICAL', 'ERROR', 'WARNING', 'INFO']
    }

    should_fail = any(
        issue.get('severity') in fail_levels[args.fail_on]
        for issue in all_issues
        if isinstance(issue, dict)
    )

    sys.exit(1 if should_fail else 0)


if __name__ == '__main__':
    main()
```

---

## Key Validation Patterns Discovered

### 1. The Position Offset Bug (CRITICAL)

**What to look for:**
```xml
<!-- BROKEN -->
<a:xfrm>
  <a:ext cx="5943600" cy="4648200"/>
</a:xfrm>

<!-- CORRECT -->
<a:xfrm>
  <a:off x="387391" y="1510234"/>
  <a:ext cx="5943600" cy="4648200"/>
</a:xfrm>
```

**Detection:**
```python
xfrm_blocks = re.findall(r'<a:xfrm>.*?</a:xfrm>', xml_content, re.DOTALL)
for block in xfrm_blocks:
    if '<a:ext' in block and '<a:off' not in block:
        # CRITICAL: Missing position offset!
```

**Root cause:** python-pptx creates incomplete XML when only `shape.width` or `shape.height` is set without also setting `shape.left` and `shape.top`.

---

### 2. Zero Height After Width Change

**What to look for:** `shape.height == 0` after modification

**Detection:**
```python
if shape.height == 0 and 'Placeholder' in shape.name:
    # ERROR: Height was reset to zero
```

**Root cause:** Setting `shape.width` in python-pptx resets `shape.height` to 0 as a side effect.

---

### 3. Placeholder Inheritance Broken

**What to look for:** Placeholders that should inherit from layout but have explicit transforms

**When it's OK:** If the explicit transform is complete (has both off and ext)
**When it's broken:** If the explicit transform is partial

---

## Validation Workflow Recommendation

```
1. Generate presentation
        ↓
2. Run inspector at level 2 (XML validation)
        ↓
   ┌────┴────┐
   │ Issues? │
   └────┬────┘
        │
   Yes  │  No
   ↓    │   ↓
Fix and │  Continue
retry   │
        ↓
3. Visual spot-check (human review)
        ↓
4. Done
```

---

## Integration with add_images_only.py

The `add_images_only.py` script already includes validation. The validation function can be extracted and enhanced:

```python
# In add_images_only.py
def validate_presentation(pptx_path, image_slides):
    """Validates the generated presentation."""
    # ... implementation included in script
```

This validation runs automatically after image insertion and fails the script if critical issues are found.

---

## Future Enhancements

1. **Visual diff tool**: Compare before/after presentations visually
2. **Thumbnail generation**: Create slide thumbnails for quick visual review
3. **CI/CD integration**: Exit codes for automated pipelines
4. **Fix suggestions**: Not just detect issues but suggest fixes
5. **Batch validation**: Check multiple files at once

---

## References

- [OOXML Specification - DrawingML](http://officeopenxml.com/drwOverview.php)
- [python-pptx Documentation](https://python-pptx.readthedocs.io/)
- [PresentationML Structure](https://docs.microsoft.com/en-us/office/open-xml/structure-of-a-presentationml-document)
