# Context Engineering

## Summary
Context engineering is the discipline of managing what information enters the LLM's context window. Due to the O(N²) memory complexity of transformer architecture, this is the fundamental constraint that shapes all agent design decisions.

## Why Context Matters

### The Transformer Constraint
- Attention mechanism scales O(N²) with sequence length
- Context window is a **hard limit** on what the model can "see"
- Everything the model knows about your task must fit in this window
- Wasted tokens = reduced capability

### The Problem with Current Tools
Many harnesses "inject stuff behind your back that isn't even surfaced in the UI" - preventing developers from understanding what influences model behavior.

## Practical Context Management Strategies

### 1. Minimal System Prompts
- Pi coding agent: <1,000 tokens for entire system prompt
- Competitors: 10,000+ tokens
- Lean prompts leave more room for actual work

### 2. Anti-MCP Stance (Controversial)
- Popular MCP servers waste 7-9% of context window
- Tools users never employ still consume tokens
- Alternative: CLI tools with README documentation loaded on-demand

### 3. File-Based Planning
- External markdown files preserve information across sessions
- Maintains observability (you can see the plan)
- Doesn't pollute working context

### 4. Pre-Session Artifact Creation
- Gather context in dedicated "research" sessions
- Reuse artifacts in fresh "implementation" sessions
- Keeps working context clean

### 5. Progressive Disclosure
- Load tool documentation only when needed
- Not everything upfront

## Design Implications

These constraints lead directly to architectural features:
- **Subagents**: Fresh context windows for parallel tasks
- **Skills**: Token-efficient summaries scanned before full load
- **File-based state**: External storage rather than in-context memory

## The Minimal Toolset Insight

Mario Zechner's finding: **Four tools (read, write, edit, bash) outperform complex tool ecosystems in benchmarks.**

Complexity doesn't equal capability.

## Key References

- [Mario Zechner: Pi Coding Agent](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/)
- [Simon Willison: Claude Skills](https://simonwillison.net/2025/Oct/16/claude-skills/)
