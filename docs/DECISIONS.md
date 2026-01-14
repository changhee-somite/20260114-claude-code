# Decisions Log

This document captures key decisions made during presentation preparation to ensure continuity across sessions.

---

## Session 1: 2026-01-14 (Initial Research & Structure)

### Audience & Context
- **Audience**: Internal computational team, well-versed in coding agents and Cursor IDE
- **Duration**: 30-60 minutes
- **Primary question to address**: "What's the difference between Cursor with any model vs. Claude Code?"

### Presentation Preferences (User Input)
- **Tone**: Balanced mix — technical depth where needed, accessible elsewhere
- **Demo ratio**: Flexible — prepare both slide-heavy and demo-heavy options
- **Key emphasis areas**:
  1. Context engineering theory (why context window matters)
  2. Workflow paradigm shift (from coding to orchestration)

### Narrative Decisions

#### Core Thesis
> We're shifting from "coding" to "workflow design," driven by the fundamental context window constraint.

#### Key Insight Added (Act 1.5)
Decided to add "LLM + Filesystem = Agent" as bridge concept between Acts 1 and 2:
- This distinguishes Claude Code from web chatbots
- Quote: "An LLM that got permission to access a file system" — Simon Willison
- Important because audience may think of Claude Code as "just another chatbot"

#### 5-Act Structure
1. **Act 1**: The Shift (old model → new model → what is Claude Code)
2. **Act 1.5**: LLM + Filesystem (key differentiator from chatbots)
3. **Act 2**: The Fundamental Constraint (O(N²), context window)
4. **Act 3**: Solutions Derived from Constraint (subagents, skills, MCP debate)
5. **Act 4**: Practical Setup (config, permissions, Cursor comparison, alternatives)
6. **Act 5**: Demonstrations (this presentation workflow, fastq_analysis example)

### Content Decisions

#### Topics Covered (10 documents)
1. What is Claude Code — general agent concept, timeline
2. Context Engineering — O(N²), strategies, minimal toolset
3. Permissions & Safety — 4 modes, granular config, hooks, YOLO mode
4. Subagents — fresh contexts, coordination patterns
5. Skills — markdown simplicity, 140+ scientific skills
6. Workflow Paradigm — process > model
7. Cursor vs Claude Code — assistant vs agent paradigm
8. Alternatives — OpenCode, Aider, Gemini CLI with pros/cons
9. Practical Examples — this presentation + fastq_analysis (placeholder)
10. Setup & Configuration — pricing, /status, /statusline, /plugin, CLAUDE.md

#### Permissions Section Enhancement
Decided to go beyond just "YOLO mode" to include:
- Four permission modes (default, acceptEdits, plan, bypass)
- Granular allow/deny/ask rules in settings.json
- Hooks for custom permission logic
- Enterprise managed-settings.json

#### Alternatives Section
Added comprehensive comparison because:
- Team may want flexibility
- Important to show Claude Code isn't the only option
- OpenCode for cost control, Aider for explicit control, Gemini for free tier

### Figure Decisions

#### Screenshots Added
- `/status` command tabs (Status, Config, Usage)
- Named descriptively: `status-tab-*.png`
- Usage tab emphasized for context engineering narrative

#### Figure Placement
- Usage screenshots → Context Engineering slides AND Setup slides
- Config screenshots → Setup & Configuration slides

### Practical Example Decisions

#### This Presentation as Meta-Example
- Show git commit history as proof of workflow
- Demonstrate: CLAUDE.md → research → topics → PRESENTATION.md → PPTX

#### fastq_analysis Example (Placeholder)
- Location: `~/fastq_analysis/utilities`
- **Future task**: Access ~/.claude/ conversation logs to extract real example
- Purpose: Show diversity of tasks beyond presentation-building

### Technical Decisions

#### Git Workflow
- Commit after each meaningful change
- Clear, descriptive commit messages
- Co-authored with Claude for transparency

#### Context Management
- At 59% context, decided to document everything before Phase 2
- Fresh session recommended for PRESENTATION.md generation
- All context preserved in committed documentation

---

## Quotes Selected for Use

> "An LLM that got permission to access a file system" — Simon Willison

> "Engineers are no longer writing software—they're designing higher-order systems" — Mike.tech

> "The outcome is defined by the process, not the model" — Mike.tech

> "Four tools (read, write, edit, bash) outperform complex tool ecosystems" — Mario Zechner

> "If you think in files and edits: Cursor. If you think in tasks and outcomes: Claude Code"

---

## Open Items for Future Sessions

- [ ] Fill in fastq_analysis practical example (access conversation logs)
- [ ] Create PRESENTATION.md slide-by-slide outline
- [ ] Generate additional figures if needed
- [ ] Create PPTX using Skills

---

## How to Continue

For Phase 2, start a new session and say:
> "Continue with Phase 2: Create PRESENTATION.md following docs/NARRATIVE.md. See docs/DECISIONS.md for preferences and context."

Key files to reference:
- `docs/NARRATIVE.md` — presentation flow
- `docs/DECISIONS.md` — this file (preferences, decisions)
- `docs/OVERVIEW.md` — topic index
