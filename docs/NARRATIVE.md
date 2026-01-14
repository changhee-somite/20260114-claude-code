# Presentation Narrative Structure

## Core Thesis

We are at an inflection point where the old mental model of "coding" is being replaced by a new paradigm of "workflow design." This shift is driven by a fundamental constraint—the context window—which shapes all the tools and techniques we use with AI agents.

---

## Narrative Arc

### Act 1: The Shift We're Living Through

**Opening Hook:** We're stuck in old ways of thinking about coding.

1. **The Old Model** (2 min)
   - Developer writes code line by line
   - IDE assists with autocomplete, syntax
   - Human is the executor, tools are passive

2. **The New Model** (3 min)
   - Developer describes outcomes
   - Agent plans and executes
   - Human supervises and validates
   - Reference: "Engineers are no longer writing software—they're designing higher-order systems"

3. **What is Claude Code?** (5 min)
   - Not a coding tool—a general agent for computer automation
   - "An LLM that got permission to access a file system"
   - Timeline: Feb 2025 launch → $1B revenue in 6 months
   - Topic: [01-what-is-claude-code.md](topics/01-what-is-claude-code.md)

---

### Act 2: The Fundamental Constraint

**Key Insight:** The context window limitation isn't going away soon, so we must engineer around it.

4. **The Transformer Constraint** (5 min)
   - O(N²) memory complexity
   - Context window is a hard limit
   - Everything the model knows must fit in this window
   - Topic: [02-context-engineering.md](topics/02-context-engineering.md)

5. **Why This Matters** (3 min)
   - Wasted tokens = reduced capability
   - Hidden context injection by tools
   - The minimal toolset insight: "Four tools outperform complex ecosystems"

---

### Act 3: Solutions Derived from the Constraint

**Framework:** All these features exist because of context limitations.

6. **Subagents** (5 min)
   - Fresh context windows for parallel tasks
   - Decompose large tasks
   - Coordinate through structured handoffs
   - Topic: [04-subagents.md](topics/04-subagents.md)

7. **Skills** (5 min)
   - Token-efficient instructions
   - Markdown simplicity
   - 140+ scientific skills available
   - Topic: [05-skills.md](topics/05-skills.md)

8. **The MCP Debate** (3 min)
   - MCP servers can waste 7-9% of context window
   - Counter-argument: on-demand CLI tools
   - Trade-off: convenience vs context efficiency

---

### Act 4: Practical Considerations

**Grounding:** How do we actually use this safely and effectively?

9. **Permissions & Safety** (5 min)
   - Four permission modes (default, acceptEdits, plan, bypass)
   - Granular configuration via settings.json
   - Hooks for custom logic
   - The "Lethal Trifecta" security model
   - Topic: [03-permissions-and-safety.md](topics/03-permissions-and-safety.md)

10. **Cursor vs Claude Code** (5 min)
    - Assistant (Cursor) vs Agent (Claude Code)
    - "If you think in files and edits: Cursor"
    - "If you think in tasks and outcomes: Claude Code"
    - Topic: [07-cursor-vs-claude-code.md](topics/07-cursor-vs-claude-code.md)

11. **Alternatives Landscape** (3 min)
    - OpenCode: model flexibility, open source
    - Aider: terminal-first, explicit control
    - Gemini CLI: free tier, large context
    - Topic: [08-alternatives-comparison.md](topics/08-alternatives-comparison.md)

---

### Act 5: Demonstration

**Live Proof:** This presentation was built using the workflow.

12. **This Presentation as Workflow Demo** (5 min)
    - Show git commit history
    - CLAUDE.md → SCRATCH.md → topics → PRESENTATION.md → PPTX
    - Human provides direction; agent executes and synthesizes

13. **Internal Coding Example** (5-10 min)
    - Practical work with ~/fastq_analysis/utilities
    - [Placeholder: specific example to be filled]
    - Topic: [09-practical-examples.md](topics/09-practical-examples.md)

---

### Closing

14. **Key Takeaways** (2 min)
    - Context engineering is the fundamental skill
    - Workflow design > coding syntax
    - Match tool to mental model (assistant vs agent)
    - Start with granular permissions, not YOLO

15. **Resources & Next Steps** (1 min)
    - Link to this repository
    - Tutorial resources
    - Open questions for discussion

---

## Narrative Themes

### Theme 1: Constraint → Design
Every feature (subagents, skills, modes) derives from the context window constraint.

### Theme 2: Process > Model
"The outcome is defined by the process, not the model."

### Theme 3: Old Thinking → New Thinking
We're changing behaviors, not just tools.

### Theme 4: Practical Grounding
Abstract concepts anchored in real examples (this presentation, fastq_analysis).

---

## Slide Count Estimate

| Act | Topic Count | Est. Slides |
|-----|-------------|-------------|
| Act 1: The Shift | 3 | 6-8 |
| Act 2: Constraint | 2 | 4-5 |
| Act 3: Solutions | 3 | 8-10 |
| Act 4: Practical | 3 | 6-8 |
| Act 5: Demo | 2 | 4-6 |
| Closing | 2 | 2-3 |
| **Total** | **15** | **30-40** |

---

## Time Allocation (45-60 min target)

| Section | Time |
|---------|------|
| Acts 1-2 (Context setting) | 15 min |
| Act 3 (Technical depth) | 13 min |
| Act 4 (Practical) | 13 min |
| Act 5 (Demo) | 10-15 min |
| Closing + Q&A | 5-10 min |
