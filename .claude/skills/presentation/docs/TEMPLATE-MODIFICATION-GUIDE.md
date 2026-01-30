# Template Modification Guide

**Purpose**: Add split layouts with picture placeholders to your PowerPoint template.

---

## Current Template Analysis

Your template `2026-01-14_ClaudeCode.pptx` has these layouts:

| Index | Layout Name | Placeholders | Picture Support |
|-------|-------------|--------------|-----------------|
| 0 | Title | TITLE, BODY | No |
| 1 | Title & Bullets | TITLE, BODY | No |
| 2 | 1_Title & Bullets | TITLE, BODY | No |
| 3 | 1_Title and Content | TITLE, OBJECT | No |

**Problem**: No layouts have picture placeholders, so all body placeholders span full width.

---

## Required New Layouts

### Layout A: Text + Image (50/50 Split)

```
┌────────────────────────────────────────────────────────────┐
│  TITLE PLACEHOLDER (full width)                             │
├────────────────────────────────┬───────────────────────────┤
│                                │                           │
│  TEXT/BODY PLACEHOLDER         │  PICTURE PLACEHOLDER      │
│  (50% width, ~6")              │  (50% width, ~6")         │
│                                │                           │
│  • Bullet 1                    │  ┌───────────────────┐    │
│  • Bullet 2                    │  │                   │    │
│  • Bullet 3                    │  │     [IMAGE]       │    │
│                                │  │                   │    │
│                                │  └───────────────────┘    │
│                                │                           │
└────────────────────────────────┴───────────────────────────┘
```

**Specifications**:
- Title: Left=0.42", Top=0.42", Width=11.49", Height=0.66"
- Body: Left=0.42", Top=1.5", Width=6.0", Height=5.0"
- Picture: Left=6.67", Top=1.5", Width=5.5", Height=5.0"

### Layout B: Text + Image (60/40 Split)

For slides with more text content:

```
┌────────────────────────────────────────────────────────────┐
│  TITLE PLACEHOLDER (full width)                             │
├─────────────────────────────────────┬──────────────────────┤
│                                     │                      │
│  TEXT/BODY PLACEHOLDER              │  PICTURE             │
│  (60% width, ~7.2")                 │  PLACEHOLDER         │
│                                     │  (40% width, ~4.8")  │
│  • Bullet point 1                   │                      │
│  • Bullet point 2                   │  ┌──────────────┐    │
│  • Bullet point 3                   │  │              │    │
│  • Bullet point 4                   │  │   [IMAGE]    │    │
│                                     │  │              │    │
│                                     │  └──────────────┘    │
│                                     │                      │
└─────────────────────────────────────┴──────────────────────┘
```

**Specifications**:
- Title: Left=0.42", Top=0.42", Width=11.49", Height=0.66"
- Body: Left=0.42", Top=1.5", Width=7.0", Height=5.0"
- Picture: Left=7.67", Top=1.5", Width=4.5", Height=5.0"

---

## Step-by-Step Instructions

### Step 1: Open Slide Master

1. Open `2026-01-14_ClaudeCode.pptx` in PowerPoint
2. Go to **View** → **Slide Master**

### Step 2: Create New Layout (50/50 Split)

1. In the left panel, right-click below existing layouts
2. Select **Insert Layout**
3. A new blank layout appears

### Step 3: Add Title Placeholder

1. Go to **Slide Master** tab → **Insert Placeholder** → **Text**
2. Draw at top: Left=0.42", Top=0.42", Width=11.49", Height=0.66"
3. Or copy the title placeholder from an existing layout

### Step 4: Add Body Placeholder (Left Side)

1. **Insert Placeholder** → **Text**
2. Draw on left side: Left=0.42", Top=1.5", Width=6.0", Height=5.0"
3. This will hold bullet points

### Step 5: Add Picture Placeholder (Right Side)

1. **Insert Placeholder** → **Picture** (NOT Content, specifically Picture!)
2. Draw on right side: Left=6.67", Top=1.5", Width=5.5", Height=5.0"
3. The placeholder will show a picture icon

### Step 6: Rename the Layout

1. Right-click the new layout in the left panel
2. Select **Rename Layout**
3. Name it: `Text Left / Image Right`

### Step 7: Create Second Layout (60/40 Split)

Repeat steps 2-6 with these dimensions:
- Body: Left=0.42", Width=7.0"
- Picture: Left=7.67", Width=4.5"
- Name: `Text Left / Image Right (Wide)`

### Step 8: Close and Save

1. Click **Close Master View**
2. Save the template

---

## Verification

After modification, run this to verify layouts:

```bash
python3 -c "
from pptx import Presentation
from pptx.enum.shapes import PP_PLACEHOLDER

prs = Presentation('2026-01-14_ClaudeCode.pptx')
print('Layouts with Picture Placeholders:')
print('-' * 40)
for i, layout in enumerate(prs.slide_layouts):
    has_picture = False
    for ph in layout.placeholders:
        if ph.placeholder_format.type == PP_PLACEHOLDER.PICTURE:
            has_picture = True
            print(f'Layout {i}: {layout.name}')
            print(f'  Picture placeholder idx={ph.placeholder_format.idx}')
            break
if not has_picture:
    print('No picture placeholders found!')
"
```

---

## Alternative: Python Script to Modify Template

If you prefer, I can create a Python script that programmatically adds these layouts. However, creating slide layouts via python-pptx has limitations - it's often easier to do manually in PowerPoint.

---

## Layout Index Reference

After modification, your template should have:

| Index | Layout Name | Use Case |
|-------|-------------|----------|
| 0 | Title | First slide |
| 1 | Title & Bullets | Text-only slides |
| 2 | 1_Title & Bullets | Alternative text-only |
| 3 | 1_Title and Content | Content slides |
| **4** | **Text Left / Image Right** | **Slides with figures (50/50)** |
| **5** | **Text Left / Image Right (Wide)** | **Slides with figures (60/40)** |

---

## Quick Reference: Placeholder Types

When working with python-pptx:

```python
from pptx.enum.shapes import PP_PLACEHOLDER

PP_PLACEHOLDER.TITLE         # 1 - Title text
PP_PLACEHOLDER.BODY          # 2 - Body/bullet text
PP_PLACEHOLDER.PICTURE       # 18 - Picture placeholder
PP_PLACEHOLDER.OBJECT        # 7 - Content (can hold anything)
PP_PLACEHOLDER.SLIDE_NUMBER  # 12 - Slide number
```

---

## Troubleshooting

### "Picture placeholder not working"

- Ensure you selected **Insert Placeholder → Picture**, not Content
- Verify with the verification script above

### "Text overlapping image"

- Check body placeholder width doesn't extend past picture placeholder
- Leave ~0.25" gap between body and picture placeholders

### "Image not filling placeholder"

- Picture placeholders auto-crop to fit
- Use images with similar aspect ratio to placeholder

---

## Next Steps

After modifying the template:

1. Run verification script to confirm layouts
2. Note the layout indices for `Text Left / Image Right`
3. Update `layout-map.json` with correct indices
4. Run the unified generation script
