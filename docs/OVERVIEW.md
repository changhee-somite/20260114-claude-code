# Claude Code Presentation - Documentation Overview

## Purpose
Internal presentation (30-60 min) for a computational team already familiar with coding agents and Cursor IDE. Goal: introduce Claude Code and demonstrate effective workflows.

## Key Documents

| Document | Purpose |
|----------|---------|
| **[NARRATIVE.md](NARRATIVE.md)** | Presentation flow and storyline (5-act structure) |
| **[PRESENTATION.md](PRESENTATION.md)** | Slide-by-slide outline (37 slides) |
| **[DECISIONS.md](DECISIONS.md)** | Session decisions, preferences, continuation instructions |

**Core Thesis:** We're shifting from "coding" to "workflow design," driven by the fundamental context window constraint.

**Key Insight:** Claude Code is "an LLM that got permission to access a file system" — this transforms it from chatbot to general agent.

**Presentation Preferences:**
- Tone: Balanced mix (technical + accessible)
- Demo: Flexible (prepare both options)
- Emphasis: Context engineering theory, Workflow paradigm shift

## Topic Documentation

| # | Topic | File | Key Points |
|---|-------|------|------------|
| 1 | What is Claude Code? | [topics/01-what-is-claude-code.md](topics/01-what-is-claude-code.md) | General agent concept, timeline |
| 2 | Context Engineering | [topics/02-context-engineering.md](topics/02-context-engineering.md) | O(N²) constraint, strategies |
| 3 | Permissions & Safety | [topics/03-permissions-and-safety.md](topics/03-permissions-and-safety.md) | Modes, granular config, hooks |
| 4 | Subagents & Patterns | [topics/04-subagents.md](topics/04-subagents.md) | Fresh contexts, coordination |
| 5 | Skills System | [topics/05-skills.md](topics/05-skills.md) | Markdown simplicity, scientific skills |
| 6 | Workflow Paradigm | [topics/06-workflow-paradigm.md](topics/06-workflow-paradigm.md) | Process > model, system design |
| 7 | Cursor vs Claude Code | [topics/07-cursor-vs-claude-code.md](topics/07-cursor-vs-claude-code.md) | Assistant vs Agent paradigm |
| 8 | Alternatives | [topics/08-alternatives-comparison.md](topics/08-alternatives-comparison.md) | OpenCode, Aider, Gemini CLI |
| 9 | Practical Examples | [topics/09-practical-examples.md](topics/09-practical-examples.md) | This presentation, fastq_analysis |
| 10 | Setup & Configuration | [topics/10-setup-and-configuration.md](topics/10-setup-and-configuration.md) | /statusline, /plugin, CLAUDE.md |
| 11 | **Appendix: Tools & MCP** | [topics/11-appendix-tools-and-mcp.md](topics/11-appendix-tools-and-mcp.md) | Built-in tools, MCP setup, Gemini |

## Key Sources

### Primary References
- [Simon Willison: Claude Skills](https://simonwillison.net/2025/Oct/16/claude-skills/)
- [Simon Willison: Living Dangerously](https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/)
- [Mario Zechner: Pi Coding Agent](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/)
- [Mike.tech: Death of Software Development](https://mike.tech/blog/death-of-software-development)

### Skills & Patterns
- [Anthropic Skills Repository](https://github.com/anthropics/skills)
- [Scientific Skills](https://github.com/K-Dense-AI/claude-scientific-skills)
- [Awesome Agentic Patterns](https://esc5221.github.io/awesome-agentic-patterns/)

### Permissions & Configuration
- [Claude Code Settings Docs](https://code.claude.com/docs/en/settings)
- [Hooks Guide](https://code.claude.com/docs/en/hooks-guide)
- [Claude Code Permissions Guide](https://www.eesel.ai/blog/claude-code-permissions)
- [Status Line Configuration](https://code.claude.com/docs/en/statusline)
- [Discover Plugins](https://code.claude.com/docs/en/discover-plugins)

### Alternatives
- [OpenCode vs Claude Code](https://www.builder.io/blog/opencode-vs-claude-code)
- [Agentic CLI Tools Compared](https://research.aimultiple.com/agentic-cli/)
- [Top 5 Agentic CLI Tools](https://www.kdnuggets.com/top-5-agentic-coding-cli-tools)

### Tutorials
- [DeepLearning.ai: Claude Code Course](https://www.deeplearning.ai/short-courses/claude-code-a-highly-agentic-coding-assistant/)
- [Net Ninja YouTube Playlist](https://www.youtube.com/playlist?list=PL4cUxeGkcC9g4YJeBqChhFJwKQ9TRiivY)
- [Using CLAUDE.md Files](https://claude.com/blog/using-claude-md-files)

## Project Status

- [x] Phase 1: Research and compilation
- [x] Phase 1.5: Additional research (permissions, alternatives, narrative)
- [x] Phase 1.6: Setup/configuration guide, narrative refinement
- [x] Phase 2: PRESENTATION.md slide outline (37 slides)
- [ ] Phase 3: Figure preparation
- [ ] Phase 4: PPTX generation

## Next Steps

1. **Fill in practical example**: Add details for `~/fastq_analysis/utilities` example
2. **Prepare figures**: Generate or collect additional visuals for key concepts
3. **Generate PPTX**: Use document-skills:pptx to create final presentation
