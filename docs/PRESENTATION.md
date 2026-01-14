# Presentation Slide Outline

## Metadata
- **Title**: Claude Code: From Coding to Workflow Design
- **Duration**: 45-60 minutes
- **Audience**: Internal computational team (familiar with Cursor, coding agents)
- **Core Question**: What's different about Claude Code vs. Cursor with any model?

---

## Act 1: The Shift We're Living Through

---

### Slide 1: Title Slide
**Title**: Claude Code: From Coding to Workflow Design

**Content**:
- Presenter name
- Date: January 2026
- Internal Computational Team

**Notes**: Welcome, context for why this presentation matters to our team.

---

### Slide 2: We're stuck in an old mental model of development

**Title**: We're stuck in an old mental model of development

**Content**:
| Old Model | New Model |
|-----------|-----------|
| Developer writes code line by line | Developer describes outcomes |
| IDE assists with autocomplete | Agent plans and executes |
| Human is the executor | Human supervises and validates |

**Notes**: The shift isn't about better autocomplete—it's about changing who does the work.

**Source**: [topics/06-workflow-paradigm.md](topics/06-workflow-paradigm.md)

---

### Slide 3: Engineers are designing systems, not writing code

**Title**: Engineers are no longer writing software—they're designing higher-order systems

**Content**:
- One person built a Polymarket analysis tool in 2 hours without writing code
- The technique mattered more than which AI was used
- Architecture and process design become primary skills

> "The outcome is defined by the process, not the model." — Mike.tech

**Figure**: [figures/blog-mike-tech-death-of-software.png](../figures/blog-mike-tech-death-of-software.png)

**Notes**: This isn't hypothetical—it's happening now. The skill shift is real. Show the blog post header.

**Source**: [topics/06-workflow-paradigm.md](topics/06-workflow-paradigm.md)

---

### Slide 4: Think in abstractions, not code

**Title**: Communicate intent structurally—let the agent find the implementation

**Content**:
```xml
<task>What you want Claude to do</task>
<context>Background information it needs</context>
<constraints>Any limits or rules</constraints>
<output_format>How you want the answer</output_format>
```

| Code-Level Thinking | Abstract Thinking |
|--------------------|--------------------|
| "Write a function that..." | "I need to transform X into Y" |
| Focus on implementation | Focus on intent |
| One solution path | Multiple approaches possible |

> "It's like I was driving a race car in first gear the whole time."

**Figure**: [figures/reddit-xml-structured-prompting.png](../figures/reddit-xml-structured-prompting.png)

**Notes**: The more abstractly you communicate, the more leverage you give the agent.

**Source**: [topics/06-workflow-paradigm.md](topics/06-workflow-paradigm.md)

---

### Slide 5: Workflows compound—every update makes the system smarter

**Title**: Every update to CLAUDE.md, skills, and artifacts compounds your efficiency gains

**Content**:
```
Session 1: Write CLAUDE.md with basic project context
    ↓
Session 5: Add common commands, conventions, warnings
    ↓
Session 20: Refined skills, custom hooks, team patterns
    ↓
Session 100: Agent works like a trained team member
```

**The Improvement Loop**:
- Update CLAUDE.md → agent behaves better → update again
- Create skills → reuse across projects → refine based on failures
- Artifacts persist → knowledge compounds → efficiency accelerates

**Notes**: This is the architecture for rapid efficiency gains. The future is here—adoption is the challenge.

**Figure**: [figures/workflow-improvement-loop.png](../figures/workflow-improvement-loop.png)

**Source**: [topics/06-workflow-paradigm.md](topics/06-workflow-paradigm.md)

---

### Slide 6: Claude Code is a general agent, not a coding tool

**Title**: Claude Code is a general agent for computer automation, not just a coding tool

**Content**:
- February 2025: Launch as CLI research preview
- October 2025: Web launch on claude.ai
- November 2025: $1B revenue run-rate
- January 2026: Multi-agent infrastructure (v2.1.0)

**Notes**: The trajectory tells the story—this is being adopted rapidly.

**Source**: [topics/01-what-is-claude-code.md](topics/01-what-is-claude-code.md)

---

### Slide 7: Claude Code automates anything you can type into a computer

**Title**: Claude Code can automate anything you can achieve by typing commands into a computer

**Content**:
- File system access (read, write, edit)
- Command execution (shell access)
- Context awareness (understands project structure)
- Autonomous operation (minimal supervision)

> "2025 has become the year of agents... agents are 'tools in a loop'" — Simon Willison

**Notes**: This is the general agent concept—not limited to coding.

**Source**: [topics/01-what-is-claude-code.md](topics/01-what-is-claude-code.md)

---

## Act 1.5: The Key Insight — LLM + Filesystem

---

### Slide 8: The critical distinction is filesystem access

**Title**: Claude Code is an LLM that got permission to access a file system

**Content**:
| Web Chatbot | Claude Code |
|-------------|-------------|
| Stateless conversations | Persistent filesystem access |
| Copy-paste code snippets | Direct file read/write |
| Describe your environment | Agent explores your environment |
| Human executes commands | Agent executes commands |
| No memory between sessions | Project context via CLAUDE.md |

> "An LLM that got permission to access a file system" — Simon Willison

**Notes**: This is THE insight. Filesystem access transforms chatbot → agent.

**Source**: [topics/01-what-is-claude-code.md](topics/01-what-is-claude-code.md)

---

### Slide 9: The power comes from simplicity

**Title**: Claude Code's power comes from its simplicity: minimal protocol, maximum capability

**Content**:
- No heavyweight protocols needed
- Skills are just markdown files the agent reads
- Four tools (read, write, edit, bash) outperform complex ecosystems
- "Outsources the hard parts to the LLM harness and the computer environment"

**Notes**: Counter-intuitive: less infrastructure = better performance.

**Source**: [topics/02-context-engineering.md](topics/02-context-engineering.md)

---

## Act 2: The Fundamental Constraint

---

### Slide 10: The transformer architecture imposes a hard constraint

**Title**: The O(N²) memory complexity of transformers creates a hard context limit

**Content**:
- Attention mechanism scales quadratically with sequence length
- Context window is a hard limit on what the model can "see"
- Everything the model knows about your task must fit in this window
- Wasted tokens = reduced capability

**Notes**: This constraint isn't going away soon—we must engineer around it.

**Source**: [topics/02-context-engineering.md](topics/02-context-engineering.md)

---

### Slide 11: Context engineering is the fundamental skill

**Title**: Context engineering—managing what enters the context window—is the fundamental skill

**Content**:
Key strategies:
1. **Minimal system prompts**: <1,000 tokens vs competitors' 10,000+
2. **File-based planning**: External markdown preserves info across sessions
3. **Progressive disclosure**: Load tool docs only when needed
4. **Pre-session artifacts**: Research sessions → implementation sessions

**Notes**: This discipline shapes every design decision.

**Source**: [topics/02-context-engineering.md](topics/02-context-engineering.md)

---

### Slide 12: You can monitor your context usage in real-time

**Title**: The /status command lets you monitor context usage in real-time

**Content**:
- Current session: percentage of context window used
- Session reset: when the 5-hour window resets
- Weekly usage across Opus and Sonnet models

**Figure**: [figures/status-tab-usage.png](../figures/status-tab-usage.png)

**Notes**: Demo the /status command. Emphasize how context fills up.

**Source**: [topics/10-setup-and-configuration.md](topics/10-setup-and-configuration.md)

---

## Act 3: Solutions Derived from the Constraint

---

### Slide 13: Subagents solve the context limitation through fresh windows

**Title**: Subagents spawn fresh context windows to handle parallel tasks

**Content**:
- Each subagent gets its own fresh context window
- Example: 36 files ÷ 3 subagents = 12 files each
- Prevents main agent from sequential overload
- Enables parallel processing

**Notes**: Direct solution to context limits—divide and conquer.

**Source**: [topics/04-subagents.md](topics/04-subagents.md)

---

### Slide 14: Agentic patterns provide a taxonomy of solutions

**Title**: A taxonomy of agentic patterns has emerged from practical experience

**Content**:
| Category | Example Patterns |
|----------|-----------------|
| Context & Memory | Context-minimization, dynamic injection |
| Feedback Loops | Self-critique, reflection, spec-as-test |
| Orchestration | Plan-then-execute, phase separation |
| Tool Use | CLI-first, code-over-API |

**Notes**: These patterns are learnable and repeatable.

**Source**: [topics/04-subagents.md](topics/04-subagents.md)

---

### Slide 15: Skills are token-efficient instructions in markdown

**Title**: Skills are elegantly simple: markdown files with instructions that Claude loads on demand

**Content**:
- Just markdown files with YAML metadata
- Brief summaries scanned before full load
- Shareable across models and tools
- No heavyweight protocols

**Notes**: The simplicity is the feature, not a limitation.

**Source**: [topics/05-skills.md](topics/05-skills.md)

---

### Slide 16: 140+ scientific skills are available for research

**Title**: 140+ scientific skills cover databases, packages, and integrations

**Content**:
- 28+ Scientific databases (OpenAlex, PubMed, ChEMBL, UniProt)
- 55+ Python packages (RDKit, Scanpy, PyTorch)
- 15+ Scientific integrations (Benchling, DNAnexus)

Categories: Bioinformatics, Cheminformatics, Clinical Research, ML/AI

**Notes**: Directly relevant to our team's work.

**Source**: [topics/05-skills.md](topics/05-skills.md)

---

### Slide 17: The MCP debate reveals a context trade-off

**Title**: MCP servers can waste 7-9% of context window with unused tool descriptions

**Content**:
**Anti-MCP argument**:
- Tools you never use still consume tokens
- Alternative: CLI tools with README loaded on-demand

**Pro-MCP argument**:
- Convenience of always-available tools
- No manual loading required

**Trade-off**: Convenience vs. context efficiency

**Notes**: There's a real debate here; neither side is wrong.

**Source**: [topics/02-context-engineering.md](topics/02-context-engineering.md)

---

### Slide 18: Git worktree enables parallel Claude Code sessions

**Title**: Once workflows are automated, git worktree enables running multiple sessions in parallel

**Content**:
```bash
# Create parallel worktrees for independent tasks
git worktree add ../feature-auth feature/auth
git worktree add ../feature-api feature/api
git worktree add ../refactor-tests refactor/tests

# Run Claude Code in each (separate terminals)
cd ../feature-auth && claude
cd ../feature-api && claude
cd ../feature-tests && claude
```

| Single Session | Parallel Sessions |
|----------------|-------------------|
| Sequential task completion | Simultaneous progress |
| One context window | Multiple fresh contexts |
| Blocking on long tasks | Non-blocking workflow |

**Figure**: [figures/tweet-boris-cherny-parallel-claudes.png](../figures/tweet-boris-cherny-parallel-claudes.png)

**Notes**: This is unconventional but powerful—treat Claude Code sessions like parallel workers. Even Boris Cherny (Claude Code creator) runs 5 Claudes in parallel!

**Source**: [topics/12-parallel-sessions.md](topics/12-parallel-sessions.md)

---

### Slide 19: Parallelization is the next efficiency multiplier

**Title**: Workflow → Context → Parallelization: three pillars of agent-era efficiency

**Content**:
**Progression**:
1. **Workflow Design**: Define what agents should do
2. **Context Engineering**: Optimize what agents can see
3. **Parallelization**: Scale by running multiple agents

**Practical patterns**:
- Feature branches in separate worktrees
- Research session + implementation session simultaneously
- Run tests in one session while developing in another

**Notes**: Once you trust the workflow, multiplying it becomes the obvious next step.

**Source**: [topics/12-parallel-sessions.md](topics/12-parallel-sessions.md)

---

## Act 4: Practical Setup and Considerations

---

### Slide 20: Installation is a single npm command

**Title**: Getting started requires one npm install and authentication

**Content**:
```bash
npm install -g @anthropic-ai/claude-code
claude --version
cd your-project
claude
```

First run: authenticate, create ~/.claude/, optionally run /init

**Notes**: Demo-able in real-time if needed.

**Source**: [topics/10-setup-and-configuration.md](topics/10-setup-and-configuration.md)

---

### Slide 21: Subscription plans scale from $20 to $200/month

**Title**: Subscription plans range from Pro ($20) to Max 20x ($200) based on usage needs

**Content**:
| Plan | Price | Best For |
|------|-------|----------|
| Pro | $20/month | Light usage, small repos |
| Max 5x | $100/month | Moderate usage, larger repos |
| Max 20x | $200/month | Heavy usage, complex projects |

Usage shared across Claude web, desktop, and Code.

**Notes**: Most of us would start at Pro, scale to Max as needed.

**Source**: [topics/10-setup-and-configuration.md](topics/10-setup-and-configuration.md)

---

### Slide 22: The statusline shows real-time session data

**Title**: A customizable statusline displays model, cost, and tokens in real-time

**Content**:
Available data fields:
- `model.display_name`: Current model
- `tokens.input` / `tokens.output`: Token counts
- `cost.current` / `cost.total`: Cost tracking
- `git.branch`: Current branch

Setup: `/statusline show the model name and context usage percentage`

**Notes**: Claude Code generates the script automatically.

**Source**: [topics/10-setup-and-configuration.md](topics/10-setup-and-configuration.md)

---

### Slide 23: The /status command provides a session dashboard

**Title**: The /status command shows session info, config, and usage in tabs

**Content**:
Three tabs:
- **Status**: Version, session ID, model, MCP servers, memory
- **Config**: Preferences, theme, checkpoints
- **Usage**: Context percentage, weekly limits

**Figure**: [figures/status-tab-status.png](../figures/status-tab-status.png)

**Notes**: Demo switching between tabs with Tab key.

**Source**: [topics/10-setup-and-configuration.md](topics/10-setup-and-configuration.md)

---

### Slide 24: CLAUDE.md provides project-specific context

**Title**: CLAUDE.md files give Claude persistent project-specific context at every session

**Content**:
```markdown
# Project Name
## Tech Stack
- Python 3.11, FastAPI, PostgreSQL
## Commands
- pytest tests/
- uvicorn main:app --reload
## Conventions
- Type hints required
- Google-style docstrings
```

Hierarchy: ~/.claude/ → parent → project → subdirectory

**Notes**: The /init command generates a starter file.

**Source**: [topics/10-setup-and-configuration.md](topics/10-setup-and-configuration.md)

---

### Slide 25: Four permission modes balance control and convenience

**Title**: Four permission modes let you choose the right balance of control and convenience

**Content**:
| Mode | Behavior |
|------|----------|
| **default** | Prompts for first use of each tool |
| **acceptEdits** | Auto-accepts file edits for session |
| **plan** | Read-only analysis, no modifications |
| **bypassPermissions** | Skips all prompts (safe environment only) |

Switch with `Shift+Tab`

**Notes**: Recommend starting with default, not YOLO mode.

**Source**: [topics/03-permissions-and-safety.md](topics/03-permissions-and-safety.md)

---

### Slide 26: Granular rules provide fine-grained control

**Title**: Granular allow/deny/ask rules in settings.json provide fine-grained control

**Content**:
```json
{
  "permissions": {
    "allow": ["Bash(npm run test:*)", "Bash(git:*)"],
    "deny": ["Read(./.env)", "Read(**/*.key)"],
    "ask": ["Bash(git push:*)", "Bash(rm:*)"]
  }
}
```

Evaluation order: deny → allow → ask

**Notes**: This is the middle ground between constant prompts and YOLO.

**Source**: [topics/03-permissions-and-safety.md](topics/03-permissions-and-safety.md)

---

### Slide 27: Hooks enable custom permission logic

**Title**: Hooks let you run custom scripts before and after tool execution

**Content**:
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{"type": "command", "command": "/path/to/validator.sh"}]
    }]
  }
}
```

Events: PreToolUse, PostToolUse, PermissionRequest

**Notes**: Can block, modify, or auto-approve based on custom logic.

**Source**: [topics/03-permissions-and-safety.md](topics/03-permissions-and-safety.md)

---

### Slide 28: Three elements create the security risk surface

**Title**: The "Lethal Trifecta" identifies three elements that create data theft risk

**Content**:
1. **Access to private data** (env vars, credentials)
2. **Exposure to untrusted content** (web pages, user input)
3. **External communication ability** (network access)

> "Anyone who can get text into your LLM has full control over what tools it runs next"

**Notes**: AI cannot reliably detect prompt injection—architecture must prevent it.

**Source**: [topics/03-permissions-and-safety.md](topics/03-permissions-and-safety.md)

---

### Slide 29: Cursor and Claude Code represent different paradigms

**Title**: Cursor is an AI assistant; Claude Code is an autonomous agent

**Content**:
| Aspect | Cursor IDE | Claude Code |
|--------|------------|-------------|
| Paradigm | Enhanced IDE | Autonomous Agent |
| Interface | GUI (VS Code fork) | CLI / Terminal |
| Model | User-selectable | Claude (optimized) |
| Execution | User-initiated | Autonomous |
| Context | IDE-provided | Full filesystem + shell |

**Notes**: This answers the team's core question.

**Source**: [topics/07-cursor-vs-claude-code.md](topics/07-cursor-vs-claude-code.md)

---

### Slide 30: The choice reflects your mental model of development

**Title**: If you think in files and edits, use Cursor; if you think in tasks and outcomes, use Claude Code

**Content**:
**Cursor excels at**:
- Quick inline edits
- Code explanation while reading
- GUI preference
- Multiple AI providers

**Claude Code excels at**:
- Multi-file refactoring
- Autonomous task completion
- Pipeline automation
- Tasks requiring shell access

**Notes**: Many developers use both for different contexts.

**Source**: [topics/07-cursor-vs-claude-code.md](topics/07-cursor-vs-claude-code.md)

---

### Slide 31: The alternatives landscape includes several strong options

**Title**: Alternatives like OpenCode, Aider, and Gemini CLI offer different trade-offs

**Content**:
| Tool | Strength | Best For |
|------|----------|----------|
| OpenCode | 75+ providers, free | Budget, model flexibility |
| Aider | Code graph, git integration | Monorepos, explicit control |
| Gemini CLI | 1M context, free tier | Google Cloud, docs tasks |
| Codex CLI | GitHub Actions | CI/CD integration |

**Notes**: No tool is strictly better—match to your needs.

**Source**: [topics/08-alternatives-comparison.md](topics/08-alternatives-comparison.md)

---

### Slide 32: Benchmark scores show performance differences

**Title**: Claude Code with Opus 4.5 leads SWE-bench at 80.9%

**Content**:
| Tool/Model | SWE-bench Score |
|------------|-----------------|
| Claude Code + Opus 4.5 | 80.9% |
| Aider | 67% |
| Cline | 63% |
| Gemini 2.5 Pro | 63.8% |

*Benchmarks vary by methodology*

**Notes**: Performance isn't everything, but it matters for complex tasks.

**Source**: [topics/08-alternatives-comparison.md](topics/08-alternatives-comparison.md)

---

## Act 5: Demonstration

---

### Slide 33: This presentation was built using the workflow we've described

**Title**: This presentation demonstrates the workflow: CLAUDE.md → research → topics → PPTX

**Content**:
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

**Notes**: Show git commit history as proof.

**Source**: [topics/09-practical-examples.md](topics/09-practical-examples.md)

---

### Slide 34: Git commit history shows the iterative process

**Title**: Each meaningful change was committed, documenting the human-agent collaboration

**Content**:
[Show actual git log output]

Key commits:
1. Initial scaffolding
2. Phase 1: Research compilation
3. Additional research: permissions, alternatives
4. Narrative structure
5. Slide outline generation

**Notes**: Run `git log --oneline` live.

**Source**: [topics/09-practical-examples.md](topics/09-practical-examples.md)

---

### Slide 35: Live demonstration placeholder

**Title**: [Live Demo] Claude Code workflow on a practical task

**Content**:
Demo options:
1. Show /status, /statusline commands
2. Install a skill via /plugin
3. Run /init on a sample project
4. Simple code modification task

**Notes**: Keep scope small—one clear task with visible completion.

**Source**: [topics/09-practical-examples.md](topics/09-practical-examples.md)

---

## Act 6: Future Directions

---

### Slide 36: The future is iterative loops that run until completion

**Title**: Ralph-Wiggum: iterative loops that treat failure as data, not exit condition

**Content**:
> "A simple while loop that repeatedly feeds an AI agent a prompt until completion"

**Key concepts**:
- Deterministic stopping criteria (not "try once and fail")
- Failure-as-data philosophy: setbacks guide refinement
- Prompt-centric design: "LLMs are mirrors of operator skill"

**Emerging patterns**:
- Overnight automation for well-defined greenfield projects
- Parallel Ralph loops across git worktrees
- Structured multi-agent frameworks (BMAD-METHOD: 29.7k stars, 21 agents)

**Figure**: [figures/ralph-wiggum-awesomeclaude.png](../figures/ralph-wiggum-awesomeclaude.png)

**Notes**: Show the awesomeclaude.ai/ralph-wiggum page. Mention BMAD-METHOD as an example of structured frameworks emerging.

**Source**: [topics/13-future-directions.md](topics/13-future-directions.md)

---

### Slide 37: This is about adopting a new way of thinking

**Title**: The future is here—adoption to a new way of thinking is the primary challenge

**Content**:
**What's changing**:
| Old Thinking | New Thinking |
|--------------|--------------|
| Write code myself | Design workflows that write code |
| One-shot prompts | Iterative loops until done |
| Static instructions | Continuously improved artifacts |
| Single session | Parallel agents on worktrees |

**The call to action**:
- Start with CLAUDE.md on one project
- Refine it over 5-10 sessions
- Share learnings with the team
- Build team-wide skills and patterns

**Notes**: The adoption challenge is mindset, not technology. The tools exist.

**Source**: [topics/13-future-directions.md](topics/13-future-directions.md)

---

## Closing

---

### Slide 38: Key takeaways

**Title**: Key takeaways: compound efficiency through workflow, context, and parallelization

**Content**:
1. Claude Code = LLM + filesystem access = general agent
2. Workflows compound—every CLAUDE.md update makes the system smarter
3. Context engineering is the fundamental skill
4. Parallelization via git worktree multiplies efficiency
5. The future is iterative loops that run until completion
6. Adoption is the challenge—the technology is here

**Notes**: The message: compound efficiency through continuous improvement. The future is here.

---

### Slide 39: Resources and next steps

**Title**: Resources for getting started with Claude Code

**Content**:
**Official**:
- [code.claude.com/docs](https://code.claude.com/docs)
- [DeepLearning.ai Course](https://www.deeplearning.ai/short-courses/claude-code-a-highly-agentic-coding-assistant/)

**Skills**:
- [github.com/anthropics/skills](https://github.com/anthropics/skills)
- [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills)

**This presentation**: [Repository URL]

**Notes**: Encourage exploration; offer to help with setup.

---

### Slide 40: Questions and discussion

**Title**: Questions?

**Content**:
Discussion topics:
- How might this change our team's workflows?
- What tasks would benefit most from agent automation?
- Security considerations for our environment
- Skill development for our specific use cases

**Notes**: Open floor for Q&A.

---

## Appendix (Backup Slides)

---

### Slide A1: Built-in tools are minimal by design

**Title**: Claude Code uses only four core tools: Read, Write, Edit, Bash

**Content**:
| Tool | Purpose |
|------|---------|
| Read | File contents, images, PDFs |
| Write | Create new files |
| Edit | String replacement in files |
| Bash | Shell command execution |

> "Four tools outperform complex tool ecosystems" — Mario Zechner

**Source**: [topics/11-appendix-tools-and-mcp.md](topics/11-appendix-tools-and-mcp.md)

---

### Slide A2: MCP server setup adds external capabilities

**Title**: MCP servers extend Claude Code with external tool capabilities

**Content**:
Installation:
```bash
/plugin install @anthropic-ai/mcp-server-github
/plugin install @anthropic-ai/mcp-server-context7
```

Available servers: GitHub, databases, APIs

**Trade-off**: Convenience vs. context window overhead

**Source**: [topics/11-appendix-tools-and-mcp.md](topics/11-appendix-tools-and-mcp.md)

---

### Slide A3: Gemini CLI offers the largest context window

**Title**: Gemini CLI provides 1M token context and a generous free tier

**Content**:
- 1 million token context window
- 60 requests/minute, 1000/day (free)
- Deep Google Cloud integration
- Lower SWE-bench scores than Claude

**Best for**: Google Cloud users, documentation, exploration

**Source**: [topics/11-appendix-tools-and-mcp.md](topics/11-appendix-tools-and-mcp.md)

---

## Figure Index

| Slide | Figure | Path | Status |
|-------|--------|------|--------|
| 3 | Death of Software Blog | [figures/blog-mike-tech-death-of-software.png](../figures/blog-mike-tech-death-of-software.png) | EXISTS |
| 4 | XML Structured Prompting | [figures/reddit-xml-structured-prompting.png](../figures/reddit-xml-structured-prompting.png) | EXISTS |
| 5 | Workflow Improvement Loop | [figures/workflow-improvement-loop.png](../figures/workflow-improvement-loop.png) | TO CREATE |
| 12 | Usage Tab | [figures/status-tab-usage.png](../figures/status-tab-usage.png) | EXISTS |
| 18 | Boris Cherny Parallel Claudes | [figures/tweet-boris-cherny-parallel-claudes.png](../figures/tweet-boris-cherny-parallel-claudes.png) | EXISTS |
| 23 | Status Tab | [figures/status-tab-status.png](../figures/status-tab-status.png) | EXISTS |
| 36 | Ralph-Wiggum | [figures/ralph-wiggum-awesomeclaude.png](../figures/ralph-wiggum-awesomeclaude.png) | EXISTS |

### Additional Screenshots Available

| Figure | Description | Suggested Use |
|--------|-------------|---------------|
| status-tab-config.png | Config tab | Appendix |
| status-tab-usage-full.png | Full usage view | Alternative |
| claude-code-preferences-ui.png | Preferences interface | Demo |

---

## Slide Count Summary

| Section | Slides |
|---------|--------|
| Act 1: The Shift (inc. abstract thinking, compounding) | 7 |
| Act 1.5: LLM + Filesystem | 2 |
| Act 2: Constraint | 3 |
| Act 3: Solutions + Parallelization | 7 |
| Act 4: Practical | 13 |
| Act 5: Demo | 3 |
| Act 6: Future Directions | 2 |
| Closing | 3 |
| Appendix | 3 |
| **Total** | **43** |

---

## Notes for PPTX Generation

- Use the document-skills:pptx skill for generation
- Reference figures by relative path for proper linking
- Tables should be rendered as actual PowerPoint tables
- Code blocks should use monospace formatting
- Quotes should be styled distinctively
