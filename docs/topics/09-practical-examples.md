# Practical Examples

## Summary
Theory without practice is incomplete. This section documents concrete examples of Claude Code workflows, serving both as demonstration material and as templates for the audience.

---

## Example 1: This Presentation (Meta-Workflow)

### What We Built
A complete presentation about Claude Code, built using Claude Code itself.

### Workflow Demonstrated
```
CLAUDE.md (instructions)
    ↓
scratch/SCRATCH.md (raw notes, URLs)
    ↓
Research (WebFetch, WebSearch)
    ↓
docs/topics/*.md (organized knowledge)
    ↓
docs/NARRATIVE.md (flow structure)
    ↓
docs/PRESENTATION.md (slide outline)
    ↓
*.pptx (final output via Skills)
```

### Git Commit History as Proof
Each step is tracked:
1. `Initial commit: Project scaffolding`
2. `Phase 1 complete: Research compilation and topic organization`
3. `Additional research: granular permissions, alternatives, narrative`
4. [Subsequent commits as work progresses]

### Key Points Demonstrated
- Human provides direction (CLAUDE.md)
- Agent executes research (web searches, documentation)
- Artifacts are persistent (markdown files, not in-context)
- Iterative refinement through commits
- Final output generated from structured documentation

---

## Example 2: Internal Coding - FASTQ Analysis Utilities

> **[PLACEHOLDER]**: This section to be filled with specific example from `~/fastq_analysis/utilities`

### Context
Location: `~/fastq_analysis/utilities`

### Task Description
[To be filled: What problem was solved? What was the starting state?]

### Workflow Steps
1. [To be filled: Initial prompt/task given to Claude Code]
2. [To be filled: How Claude Code explored the codebase]
3. [To be filled: Planning phase - what was proposed]
4. [To be filled: Implementation - what was created/modified]
5. [To be filled: Validation - how was it tested]

### Code Changes
[To be filled: Key files modified, nature of changes]

### Lessons Learned
[To be filled: What worked well? What required human intervention?]

---

## Example 3: Bioinformatics Skills Application

### Potential Demonstration
Using scientific skills from [claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills):

#### Single-Cell Analysis Workflow
```
User: "Analyze the expression patterns in my 10X dataset"

Claude Code:
1. Loads Scanpy skill
2. Reads data with sc.read_10x_mtx()
3. Performs QC, normalization, clustering
4. Identifies cell types
5. Generates visualization
```

#### Drug Discovery Workflow
```
User: "Find compounds similar to aspirin that might inhibit COX-2"

Claude Code:
1. Loads ChEMBL + RDKit skills
2. Queries ChEMBL for aspirin structure
3. Searches for similar compounds
4. Filters by COX-2 activity data
5. Ranks candidates
```

---

## Demonstration Tips

### For Live Demos
1. **Pre-warm the context**: Have CLAUDE.md ready with clear instructions
2. **Use Plan Mode first**: Show the planning before execution
3. **Keep scope small**: One clear task, visible completion
4. **Have fallback**: Pre-recorded demo if live fails

### What to Show
- [ ] The prompt given to Claude Code
- [ ] How it explores the codebase
- [ ] The plan it generates
- [ ] Execution with real-time output
- [ ] Final result + git diff

### What to Avoid
- Complex multi-hour tasks (won't complete in demo)
- Sensitive data (credentials, patient info)
- Network-dependent tasks (might fail)

---

## Template for Adding Examples

When adding new examples, include:

```markdown
## Example N: [Name]

### Context
- Location: [path]
- Purpose: [what this code/project does]

### Task Given
> [Exact prompt given to Claude Code]

### Workflow
1. Research phase: [what Claude Code read/searched]
2. Planning phase: [what plan was generated]
3. Execution: [what was created/modified]
4. Validation: [how it was verified]

### Result
- Files changed: [list]
- Outcome: [what was achieved]

### Lessons
- What worked: [observations]
- What needed adjustment: [interventions required]
```

---

## Repository Link

All examples and materials available at:
[Repository URL to be added after GitHub setup]
