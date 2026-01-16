# Claude Code: From Coding to Workflow Design

A tutorial presentation and reference repository demonstrating Claude Code workflows for computational teams.

## Overview

This repository contains materials for a 45-60 minute presentation introducing Claude Code to teams familiar with coding agents and IDEs like Cursor. The key question addressed: **What's different about Claude Code vs. using Cursor with any model?**

**Presentation Date**: January 14, 2026
**Audience**: Internal computational team

## Repository Structure

```
.
├── docs/
│   ├── PRESENTATION.md      # Complete slide outline (49 slides)
│   ├── NARRATIVE.md         # Presentation flow and structure
│   ├── OVERVIEW.md          # High-level topic overview
│   └── topics/              # Deep-dive topic documentation
│       ├── 01-what-is-claude-code.md
│       ├── 02-context-engineering.md
│       ├── 03-permissions-and-safety.md
│       ├── 04-subagents.md
│       ├── 05-skills.md
│       ├── 06-workflow-paradigm.md
│       ├── 07-cursor-vs-claude-code.md
│       ├── 08-alternatives-comparison.md
│       └── ...
├── figures/                 # Screenshots and diagrams for slides
├── scratch/                 # Raw notes and initial research
├── scripts/                 # PPTX generation and validation tools
│   ├── add_images_only.py   # Image insertion with position offset fix
│   ├── pptx_inspector.py    # Validate PPTX for layout issues
│   └── README.md            # Script documentation
├── workspace/               # Working files and image mappings
├── CLAUDE.md                # Project instructions for Claude Code
└── *.pptx                   # Generated presentation files
```

## Key Topics Covered

1. **The Paradigm Shift** — From writing code to designing workflows
2. **Context Engineering** — The O(N²) constraint and how to work around it
3. **Getting Started** — Installation, configuration, CLAUDE.md, permissions
4. **Cursor vs Alternatives** — Comparing tools for different workflows
5. **Demo & Future** — Live demonstration and emerging patterns

## This Repository as a Workflow Demo

This presentation was itself built using Claude Code, demonstrating the workflow:

```
CLAUDE.md (instructions)
    ↓
scratch/SCRATCH.md (raw notes)
    ↓
docs/topics/*.md (organized knowledge)
    ↓
docs/NARRATIVE.md (flow structure)
    ↓
docs/PRESENTATION.md (slide outline)
    ↓
*.pptx (Skills-generated output)
```

The git commit history documents each step of the human-agent collaboration.

## PPTX Generation with Images

This project includes a two-stage workflow for generating PowerPoint presentations with integrated images, along with validation tools to catch layout issues.

- **Workflow**: [docs/PPTX-IMAGE-SKILL-SPEC.md](docs/PPTX-IMAGE-SKILL-SPEC.md)
- **Validation**: [docs/PPTX-INSPECTOR-SKILL.md](docs/PPTX-INSPECTOR-SKILL.md)
- **Research & Lessons Learned**: [docs/IMAGE-INSERTION-RESEARCH.md](docs/IMAGE-INSERTION-RESEARCH.md)

## Quick Start

To explore this repository with Claude Code:

```bash
# Clone the repository
git clone git@github.com:changhee-somite/20260114-claude-code.git
cd 20260114-claude-code

# Start Claude Code (reads CLAUDE.md automatically)
claude
```

## Key Files

| File | Description |
|------|-------------|
| [docs/PRESENTATION.md](docs/PRESENTATION.md) | Complete slide-by-slide outline |
| [docs/topics/07-cursor-vs-claude-code.md](docs/topics/07-cursor-vs-claude-code.md) | Cursor vs Claude Code comparison |
| [docs/topics/02-context-engineering.md](docs/topics/02-context-engineering.md) | Context window management strategies |
| [docs/PPTX-IMAGE-SKILL-SPEC.md](docs/PPTX-IMAGE-SKILL-SPEC.md) | PPTX with images workflow specification |
| [docs/PPTX-INSPECTOR-SKILL.md](docs/PPTX-INSPECTOR-SKILL.md) | PPTX validation techniques and patterns |
| [scripts/add_images_only.py](scripts/add_images_only.py) | Image insertion script with bug fix |
| [CLAUDE.md](CLAUDE.md) | Project instructions demonstrating the pattern |

## Resources

**Official Documentation**
- [Claude Code Docs](https://code.claude.com/docs)
- [DeepLearning.ai Course](https://www.deeplearning.ai/short-courses/claude-code-a-highly-agentic-coding-assistant/)

**Skills**
- [Anthropic Skills](https://github.com/anthropics/skills)
- [Scientific Skills](https://github.com/K-Dense-AI/claude-scientific-skills)

## License

This repository is for educational and internal use.
