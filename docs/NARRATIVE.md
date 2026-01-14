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
   - Timeline: Feb 2025 launch → $1B revenue in 6 months
   - Topic: [01-what-is-claude-code.md](topics/01-what-is-claude-code.md)

---

### Act 1.5: The Key Insight — LLM + Filesystem

**Bridge Concept:** What makes Claude Code fundamentally different from web chatbots?

4. **"An LLM That Got Permission to Access a File System"** (5 min)

   This is the critical distinction:

   | Web Chatbot | Claude Code |
   |-------------|-------------|
   | Stateless conversations | Persistent filesystem access |
   | Copy-paste code snippets | Direct file read/write |
   | Describe your environment | Agent explores your environment |
   | Human executes commands | Agent executes commands |
   | No memory between sessions | Project context via CLAUDE.md |

   **Why this matters:**
   - The moment you give an LLM filesystem access, it becomes a *general agent*
   - It can automate "anything you can achieve by typing commands into a computer"
   - This is NOT just a better chatbot—it's a different category of tool

   **The simplicity principle:**
   - No heavyweight protocols needed
   - Skills are just markdown files the agent reads
   - "Outsources the hard parts to the LLM harness and the associated computer environment"

---

### Act 2: The Fundamental Constraint

**Key Insight:** The context window limitation isn't going away soon, so we must engineer around it.

5. **The Transformer Constraint** (5 min)
   - O(N²) memory complexity
   - Context window is a hard limit
   - Everything the model knows must fit in this window
   - Topic: [02-context-engineering.md](topics/02-context-engineering.md)

6. **Why This Matters** (3 min)
   - Wasted tokens = reduced capability
   - Hidden context injection by tools
   - The minimal toolset insight: "Four tools outperform complex ecosystems"

---

### Act 3: Solutions Derived from the Constraint

**Framework:** All these features exist because of context limitations.

7. **Subagents** (5 min)
   - Fresh context windows for parallel tasks
   - Decompose large tasks
   - Coordinate through structured handoffs
   - Topic: [04-subagents.md](topics/04-subagents.md)

8. **Skills** (5 min)
   - Token-efficient instructions
   - Markdown simplicity
   - 140+ scientific skills available
   - Topic: [05-skills.md](topics/05-skills.md)

9. **The MCP Debate** (3 min)
   - MCP servers can waste 7-9% of context window
   - Counter-argument: on-demand CLI tools
   - Trade-off: convenience vs context efficiency

---

### Act 4: Practical Setup and Considerations

**Grounding:** How do we actually set up and use this effectively?

10. **Setup & Configuration** (5 min)
    - `/statusline` for real-time feedback (tokens, cost, model)
    - `/plugin` for skills marketplace
    - CLAUDE.md for project context
    - AGENTS.md as cross-platform standard
    - Topic: [10-setup-and-configuration.md](topics/10-setup-and-configuration.md)

11. **Permissions & Safety** (5 min)
    - Four permission modes (default, acceptEdits, plan, bypass)
    - Granular configuration via settings.json
    - Hooks for custom logic
    - The "Lethal Trifecta" security model
    - Topic: [03-permissions-and-safety.md](topics/03-permissions-and-safety.md)

12. **Cursor vs Claude Code** (5 min)
    - Assistant (Cursor) vs Agent (Claude Code)
    - "If you think in files and edits: Cursor"
    - "If you think in tasks and outcomes: Claude Code"
    - Topic: [07-cursor-vs-claude-code.md](topics/07-cursor-vs-claude-code.md)

13. **Alternatives Landscape** (3 min)
    - OpenCode: model flexibility, open source
    - Aider: terminal-first, explicit control
    - Gemini CLI: free tier, large context
    - Topic: [08-alternatives-comparison.md](topics/08-alternatives-comparison.md)

---

### Act 5: Demonstration

**Live Proof:** This presentation was built using the workflow.

14. **This Presentation as Workflow Demo** (5 min)
    - Show git commit history
    - CLAUDE.md → SCRATCH.md → topics → PRESENTATION.md → PPTX
    - Human provides direction; agent executes and synthesizes

15. **Internal Coding Example** (5-10 min)
    - Practical work with ~/fastq_analysis/utilities
    - [Placeholder: specific example to be filled]
    - Topic: [09-practical-examples.md](topics/09-practical-examples.md)

---

### Closing

16. **Key Takeaways** (2 min)
    - Claude Code = LLM + filesystem access = general agent
    - Context engineering is the fundamental skill
    - Workflow design > coding syntax
    - Match tool to mental model (assistant vs agent)
    - Start with granular permissions, not YOLO

17. **Resources & Next Steps** (1 min)
    - Link to this repository
    - Tutorial resources
    - Open questions for discussion

---

## Narrative Themes

### Theme 1: LLM + Filesystem = Agent
The moment an LLM gets filesystem access, it transforms from chatbot to agent.

### Theme 2: Constraint → Design
Every feature (subagents, skills, modes) derives from the context window constraint.

### Theme 3: Process > Model
"The outcome is defined by the process, not the model."

### Theme 4: Old Thinking → New Thinking
We're changing behaviors, not just tools.

### Theme 5: Practical Grounding
Abstract concepts anchored in real examples (this presentation, fastq_analysis).

---

## Slide Count Estimate

| Act | Topic Count | Est. Slides |
|-----|-------------|-------------|
| Act 1: The Shift | 3 | 6-8 |
| Act 1.5: LLM + Filesystem | 1 | 3-4 |
| Act 2: Constraint | 2 | 4-5 |
| Act 3: Solutions | 3 | 8-10 |
| Act 4: Practical | 4 | 8-10 |
| Act 5: Demo | 2 | 4-6 |
| Closing | 2 | 2-3 |
| **Total** | **17** | **35-46** |

---

## Time Allocation (45-60 min target)

| Section | Time |
|---------|------|
| Acts 1-1.5 (The shift, key insight) | 15 min |
| Act 2 (Constraint) | 8 min |
| Act 3 (Technical solutions) | 13 min |
| Act 4 (Practical setup) | 18 min |
| Act 5 (Demo) | 10-15 min |
| Closing + Q&A | 5-10 min |

---

## Key Quotes to Use

> "An LLM that got permission to access a file system"
> — Simon Willison

> "Engineers are no longer writing software—they're designing higher-order systems"
> — Mike.tech

> "The outcome is defined by the process, not the model"
> — Mike.tech

> "Four tools (read, write, edit, bash) outperform complex tool ecosystems"
> — Mario Zechner

> "If you think in files and edits: Cursor. If you think in tasks and outcomes: Claude Code"
