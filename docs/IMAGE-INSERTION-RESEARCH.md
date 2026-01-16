# Image Insertion Enhancement: Research and Implementation Plan

**Date**: 2026-01-16
**Author**: Claude Code (Opus 4.5)
**Session Context**: Investigating why PPTX skill cannot insert figures into presentations

---

## Executive Summary

The current PPTX skill uses a **text replacement workflow** when working with templates, which does not support image insertion. This document captures our research findings and outlines a plan to enhance the workflow with image insertion capabilities using python-pptx.

---

## Problem Statement

When generating presentations from `docs/PRESENTATION.md`, the PPTX skill successfully:
- Rearranges slides from the template
- Replaces text content in placeholders
- Preserves template styling

However, it **cannot insert figures** referenced in PRESENTATION.md, requiring manual image insertion as a post-processing step.

---

## Root Cause Analysis

### 1. Template-Based Workflow Limitation

The skill provides two workflows:

| Workflow | Tool | Image Support |
|----------|------|---------------|
| **html2pptx** (from scratch) | PptxGenJS + Playwright | ✅ `<img>` tags supported |
| **Template-based** | replace.py + inventory.py | ❌ Text replacement only |

The template-based workflow uses `replace.py` which:
1. Extracts text shapes via `inventory.py`
2. Clears all text content
3. Applies new text from `replacement-text.json`

**There is no mechanism to add images to the OOXML structure.**

### 2. Template Has No Picture Placeholders

Analysis of `2026-01-14_ClaudeCode.pptx` reveals:

```
Layout 0: Title
  - idx=0: Title Text (type: TITLE)
  - idx=1: Body Level One… (type: BODY)
  - idx=2: 01 (type: SLIDE_NUMBER)

Layout 1: Title & Bullets
  - idx=0: Title Text (type: TITLE)
  - idx=1: Body Level One… (type: BODY)
  - idx=2: 01 (type: SLIDE_NUMBER)

Layout 2: 1_Title & Bullets
  - idx=0: Title Text (type: TITLE)
  - idx=1: Body Level One… (type: BODY)
  - idx=2: 01 (type: SLIDE_NUMBER)

Layout 3: 1_Title and Content
  - idx=0: Title 1 (type: TITLE)
  - idx=1: Content Placeholder 2 (type: OBJECT)
  - idx=10: Date Placeholder 3 (type: DATE)
  - idx=11: Footer Placeholder 4 (type: FOOTER)
  - idx=12: Slide Number Placeholder 5 (type: SLIDE_NUMBER)
```

**No layouts have `PICTURE (18)` type placeholders.** Even if the skill supported image insertion, there would be no designated locations for images.

### 3. Evidence from Conversation History

From session `ca332c11-f8d2-44e9-ad78-6f1d116e32a0` (2026-01-14):

> "**Note**: The workflow-improvement-loop.png figure was created earlier, but since this template-based approach uses text replacement rather than image insertion, you may want to manually add the figures from the `figures/` directory to the relevant slides"

This confirms the limitation was known and documented as a manual workaround.

---

## Technology Research

### python-pptx Capabilities

The python-pptx library **fully supports** inserting images into picture placeholders:

```python
from pptx import Presentation

prs = Presentation('template.pptx')
slide = prs.slides[0]

# Access picture placeholder by idx
picture_placeholder = slide.placeholders[1]  # idx, not position

# Insert image - automatically crops to fit
placeholder_picture = picture_placeholder.insert_picture('image.png')

prs.save('output.pptx')
```

**Key points:**
- Placeholders accessed by `idx` value (stable across slide lifetime)
- `insert_picture()` method handles sizing and cropping
- Images cropped to maintain aspect ratio within placeholder bounds
- Reference becomes invalid after insertion (use return value)

**Source**: [python-pptx Documentation](https://python-pptx.readthedocs.io/en/latest/user/placeholders-using.html)

### PptxGenJS Limitations

PptxGenJS (used by html2pptx workflow) **cannot import existing templates**:

> "Features not on the development roadmap include: ... Importing Existing Presentations and/or Templates"

This means we cannot use PptxGenJS to enhance template-based workflows.

**Source**: [PptxGenJS Documentation](https://gitbrent.github.io/PptxGenJS/docs/masters/)

### Alternative Tools Evaluated

| Tool | Verdict | Reason |
|------|---------|--------|
| **Presenton** | Viable alternative | Open source, supports templates, AI image generation |
| **PPT MCP Server** | Not suitable | Windows-only, no image support |
| **claude-office-skills** | Same limitation | Based on same skill architecture |

---

## Solution Options Evaluated

### Option 1: Manual Insertion (Current Workaround)
- **Effort**: Low (per presentation)
- **Scalability**: Poor
- **Verdict**: Acceptable for one-off presentations, not sustainable

### Option 2: Use Presenton
- **Effort**: Medium (setup + learning curve)
- **Pros**: Full-featured, AI image generation, active community
- **Cons**: Different workflow, external dependency, may not preserve exact template styling
- **Verdict**: Good for general use, but loses template control

### Option 3: Custom Skill Enhancement (Selected)
- **Effort**: Medium (one-time development)
- **Pros**:
  - Preserves exact template styling
  - Uses own figures (screenshots, diagrams)
  - Stays within Claude Code ecosystem
  - Full control over code
  - Reusable for future presentations
  - Demonstrates skill extensibility
- **Cons**:
  - Initial development effort
  - Template must have picture placeholders
- **Verdict**: Best fit for this use case

---

## Implementation Plan

### Phase 1: Template Enhancement (Manual Step)

Add picture placeholder layouts to `2026-01-14_ClaudeCode.pptx`:

| Layout Name | Structure | Use Case |
|-------------|-----------|----------|
| `Text Left / Image Right` | 50/50 horizontal split | Screenshots with explanation |
| `Image Left / Text Right` | 50/50 horizontal split | Alternate visual flow |
| `Title + Full Image` | Title bar + large image | Hero images, diagrams |
| `Image with Caption` | Image + caption below | Figures with descriptions |

**Steps in PowerPoint:**
1. View > Slide Master
2. Right-click > Insert Layout
3. Insert Placeholder > Picture
4. Position and size the placeholder
5. Rename layout descriptively
6. Close Master View
7. Save template

### Phase 2: Helper Script - analyze_placeholders.py

Create a script to discover placeholder information:

```python
# scripts/analyze_placeholders.py
# Outputs all layouts and their placeholders with idx values
# Essential for creating accurate image mappings
```

### Phase 3: Main Script - insert_images.py

Create the image insertion script:

```python
# scripts/insert_images.py
# Reads image-mapping.json
# Inserts images into designated placeholders
# Validates paths and placeholder existence
```

**Input format (image-mapping.json):**
```json
{
  "slides": [
    {
      "slide_index": 4,
      "images": [
        {
          "placeholder_idx": 1,
          "image_path": "figures/Slide005-workflow-loop.png"
        }
      ]
    }
  ]
}
```

### Phase 4: Workflow Integration

Update the presentation generation workflow:

```
Current:
PRESENTATION.md → rearrange.py → replace.py → output.pptx

Enhanced:
PRESENTATION.md → rearrange.py → replace.py → working.pptx
                                                    │
figures/ + image-mapping.json ──────────────────────┼──→ insert_images.py → final.pptx
```

### Phase 5: Documentation

Create `docs/IMAGE-WORKFLOW.md` documenting:
- How to add picture placeholders to templates
- How to create image-mapping.json
- How to run the enhanced workflow
- Troubleshooting common issues

---

## File Structure

```
scripts/
├── analyze_placeholders.py   # Helper to discover placeholder indices
├── insert_images.py          # Main image insertion script
├── rearrange.py              # Existing (unchanged)
├── replace.py                # Existing (unchanged)
└── inventory.py              # Existing (unchanged)

workspace/
├── image-mapping.json        # Generated per presentation
└── ...

docs/
├── IMAGE-INSERTION-RESEARCH.md  # This document
├── IMAGE-WORKFLOW.md            # Usage documentation (to be created)
└── ...
```

---

## Success Criteria

1. ✅ Template has at least 3 picture placeholder layouts
2. ✅ `analyze_placeholders.py` correctly identifies all placeholders
3. ✅ `insert_images.py` successfully inserts images without corruption
4. ✅ Generated PPTX opens correctly in PowerPoint/Keynote
5. ✅ Workflow is documented and reproducible

---

## References

- [python-pptx: Working with Placeholders](https://python-pptx.readthedocs.io/en/latest/user/placeholders-using.html)
- [python-pptx: Picture Placeholder Analysis](https://python-pptx.readthedocs.io/en/latest/dev/analysis/placeholders/slide-placeholders/picture-placeholder.html)
- [Microsoft: Add Picture Placeholder](https://support.microsoft.com/en-us/office/add-edit-or-remove-a-placeholder-on-a-slide-layout-a8d93d28-66cb-43fd-9f9d-e12d0a7a1f06)
- [SlideModel: Insert Picture Placeholder](https://slidemodel.com/how-to-insert-a-picture-placeholder-in-powerpoint/)
- [PptxGenJS: Masters and Placeholders](https://gitbrent.github.io/PptxGenJS/docs/masters/)
- [Presenton: Open Source AI Presentation Generator](https://github.com/presenton/presenton)
- [Anthropic Skills Repository](https://github.com/anthropics/skills)

---

## Appendix: Conversation History References

The investigation was prompted by the user's observation that figures could not be inserted during previous PPTX generation sessions. Key conversation sessions analyzed:

- `ca332c11-f8d2-44e9-ad78-6f1d116e32a0` - Phase 3: First PPTX generation
- `969e18e8-56dd-47a9-86b0-e31fffe81ee6` - PPTX v2 refinement
- `fba3fae3-a6a8-4ba5-b08e-05f688ffab27` - Phase 2: Presentation narrative

All sessions confirmed the limitation was architectural (text replacement workflow) rather than a bug or configuration issue.
