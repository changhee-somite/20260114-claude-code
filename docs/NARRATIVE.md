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

10. **Parallel Sessions with Git Worktree** (5 min)
    - Once workflows are semi-automated, parallelization becomes possible
    - Git worktree enables multiple working directories from same repo
    - Run independent Claude Code sessions simultaneously
    - Three pillars: Workflow → Context → Parallelization
    - Topic: [12-parallel-sessions.md](topics/12-parallel-sessions.md)

---

### Act 4: Practical Setup and Considerations

**Grounding:** How do we actually set up and use this effectively?

11. **Setup & Configuration** (5 min)
    - `/statusline` for real-time feedback (tokens, cost, model)
    - `/plugin` for skills marketplace
    - CLAUDE.md for project context
    - AGENTS.md as cross-platform standard
    - Topic: [10-setup-and-configuration.md](topics/10-setup-and-configuration.md)

12. **Permissions & Safety** (5 min)
    - Four permission modes (default, acceptEdits, plan, bypass)
    - Granular configuration via settings.json
    - Hooks for custom logic
    - The "Lethal Trifecta" security model
    - Topic: [03-permissions-and-safety.md](topics/03-permissions-and-safety.md)

13. **Cursor vs Claude Code** (5 min)
    - Assistant (Cursor) vs Agent (Claude Code)
    - "If you think in files and edits: Cursor"
    - "If you think in tasks and outcomes: Claude Code"
    - Topic: [07-cursor-vs-claude-code.md](topics/07-cursor-vs-claude-code.md)

14. **Alternatives Landscape** (3 min)
    - OpenCode: model flexibility, open source
    - Aider: terminal-first, explicit control
    - Gemini CLI: free tier, large context
    - Topic: [08-alternatives-comparison.md](topics/08-alternatives-comparison.md)

---

### Act 5: Demonstration

**Live Proof:** This presentation was built using the workflow.

15. **This Presentation as Workflow Demo** (5 min)
    - Show git commit history
    - CLAUDE.md → SCRATCH.md → topics → PRESENTATION.md → PPTX
    - Human provides direction; agent executes and synthesizes

16. **Internal Coding Example** (5-10 min)
    - Practical work with ~/fastq_analysis/utilities
    - [Placeholder: specific example to be filled]
    - Topic: [09-practical-examples.md](topics/09-practical-examples.md)

---

### Act 6: Future Directions

**Vision:** The future is here—adoption is the challenge.

17. **Ralph-Wiggum: Iterative Loops** (3 min)
    - "A simple while loop that repeatedly feeds an AI agent a prompt until completion"
    - Failure-as-data philosophy
    - Overnight automation for greenfield projects
    - Topic: [13-future-directions.md](topics/13-future-directions.md)

18. **Adoption as the Primary Challenge** (2 min)
    - Old thinking → new thinking transition
    - Start with CLAUDE.md, refine over sessions
    - Share learnings, build team patterns
    - The technology is here; mindset is the barrier

---

### Closing

19. **Key Takeaways** (2 min)
    - Claude Code = LLM + filesystem access = general agent
    - Workflows compound—every update makes the system smarter
    - Context engineering is the fundamental skill
    - Parallelization via git worktree multiplies efficiency
    - The future is iterative loops that run until completion
    - Adoption is the challenge—the technology is here

20. **Resources & Next Steps** (1 min)
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

### Theme 4: Compound Efficiency
Workflows improve continuously; every CLAUDE.md update makes the system smarter.

### Theme 5: Three Pillars of Efficiency
Workflow → Context → Parallelization. Each builds on the previous.

### Theme 6: Adoption > Technology
The future is here—adoption to a new way of thinking is the primary challenge.

### Theme 7: Practical Grounding
Abstract concepts anchored in real examples (this presentation, fastq_analysis).

---

## Slide Count Estimate

| Act | Topic Count | Est. Slides |
|-----|-------------|-------------|
| Act 1: The Shift (inc. compounding) | 4 | 6 |
| Act 1.5: LLM + Filesystem | 1 | 2 |
| Act 2: Constraint | 2 | 3 |
| Act 3: Solutions + Parallelization | 4 | 7 |
| Act 4: Practical | 4 | 13 |
| Act 5: Demo | 2 | 3 |
| Act 6: Future Directions | 2 | 2 |
| Closing | 2 | 3 |
| Appendix | 3 | 3 |
| **Total** | **24** | **42** |

---

## Time Allocation (45-60 min target)

| Section | Time |
|---------|------|
| Acts 1-1.5 (The shift, compounding, key insight) | 15 min |
| Act 2 (Constraint) | 8 min |
| Act 3 (Solutions + Parallelization) | 15 min |
| Act 4 (Practical setup) | 15 min |
| Act 5 (Demo) | 10-15 min |
| Act 6 (Future) + Closing + Q&A | 10 min |

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
