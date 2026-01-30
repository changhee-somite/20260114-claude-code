# Claude Code: From Coding to Workflow Design

A tutorial presentation and reference repository demonstrating Claude Code workflows for computational teams.

## Overview

This repository contains materials for a 45-60 minute presentation introducing Claude Code to teams familiar with coding agents and IDEs like Cursor. The key question addressed: **What's different about Claude Code vs. using Cursor with any model?**

**Presentation Date**: January 14, 2026
**Audience**: Internal computational team

## Repository Structure

```
.
├── .claude/
│   └── skills/              # Portable Claude Code skills
│       ├── presentation/    # PPTX generator from markdown
│       │   ├── SKILL.md
│       │   ├── scripts/     # generate_presentation.py, pptx_inspector.py
│       │   └── templates/   # PPTX template
│       └── conversation-search/  # Search past Claude Code sessions
│           ├── SKILL.md
│           └── search.py
├── docs/
│   ├── PRESENTATION.md      # Complete slide outline (49 slides)
│   ├── NARRATIVE.md         # Presentation flow and structure
│   ├── topics/              # Deep-dive topic documentation
│   │   ├── 01-what-is-claude-code.md
│   │   ├── 02-context-engineering.md
│   │   └── ...
│   └── archive/             # Legacy skill documentation
├── figures/                 # Screenshots and diagrams for slides
├── output/                  # Generated PPTX files
├── scratch/                 # Raw notes and initial research
└── CLAUDE.md                # Project instructions for Claude Code
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

## PPTX Generation

This project includes a unified workflow for generating PowerPoint presentations from markdown, with support for images, tables, and diagrams.

- **Skill Documentation**: [.claude/skills/presentation/SKILL.md](.claude/skills/presentation/SKILL.md)
- **Technical Reference**: [.claude/skills/presentation/README.md](.claude/skills/presentation/README.md)
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
| [.claude/skills/presentation/SKILL.md](.claude/skills/presentation/SKILL.md) | PPTX generation skill documentation |
| [.claude/skills/conversation-search/SKILL.md](.claude/skills/conversation-search/SKILL.md) | Conversation search skill |
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
