#!/usr/bin/env python3
"""Generate replacement JSON for 49-slide presentation with sections."""

import json

# Slide content based on updated PRESENTATION.md with 5 sections
# FULL SENTENCE TITLES - each is a complete declarative sentence
slides = [
    # Slide 0: Title
    {
        "title": "Claude Code: From Coding to Workflow Design",
        "body": "ChangHee Lee\nComputational Team Lunch & Learn 2026-01-14"
    },
    # Slide 1: Agenda
    {
        "title": "Here is our journey today.",
        "bullets": [
            ("The Paradigm Shift — From coding to orchestration", 0),
            ("Context Engineering — The fundamental constraint", 0),
            ("Getting Started — Installation and configuration", 0),
            ("Cursor vs Alternatives — Comparing tools", 0),
            ("Demo & Future — Live demo and what's next", 0),
        ]
    },
    # Slide 2: Section 1 Divider
    {
        "title": "Section 1: The Paradigm Shift",
        "bullets": [
            ("From writing code to designing workflows", 0),
        ]
    },
    # Slide 3: Old mental model
    {
        "title": "We are stuck in an old mental model.",
        "bullets": [
            ("Old: Developer writes code line by line", 0),
            ("New: Developer describes outcomes", 1),
            ("Old: IDE assists with autocomplete", 0),
            ("New: Agent plans and executes", 1),
            ("Old: Human is the executor", 0),
            ("New: Human supervises and validates", 1),
        ]
    },
    # Slide 4: Engineers designing systems
    {
        "title": "Engineers now design systems.",
        "bullets": [
            ("One person built a Polymarket tool in 2 hours without writing code", 0),
            ("The technique mattered more than which AI was used", 0),
            ("Architecture and process design become primary skills", 0),
            ('"The outcome is defined by the process, not the model." — Mike.tech', 0),
        ]
    },
    # Slide 5: Abstract thinking
    {
        "title": "You communicate intent to agents.",
        "bullets": [
            ("Use XML tags: <task>, <context>, <constraints>, <output_format>", 0),
            ("Code-Level: \"Write a function that...\" → Implementation focus", 0),
            ("Abstract: \"I need to transform X into Y\" → Intent focus", 0),
            ('"It\'s like I was driving a race car in first gear."', 0),
        ]
    },
    # Slide 6: Compounding workflows
    {
        "title": "CLAUDE.md updates compound over time.",
        "bullets": [
            ("Session 1: Write CLAUDE.md with basic project context", 0),
            ("Session 5: Add common commands, conventions, warnings", 1),
            ("Session 20: Refined skills, custom hooks, team patterns", 1),
            ("Session 100: Agent works like a trained team member", 1),
        ]
    },
    # Slide 7: Claude Code is general agent
    {
        "title": "Claude Code is a general agent.",
        "bullets": [
            ("February 2025: Launch as CLI research preview", 0),
            ("October 2025: Web launch on claude.ai", 0),
            ("November 2025: $1B revenue run-rate", 0),
            ("January 2026: Multi-agent infrastructure (v2.1.0)", 0),
        ]
    },
    # Slide 8: Automates anything
    {
        "title": "It automates anything you can type.",
        "bullets": [
            ("File system access (read, write, edit)", 0),
            ("Command execution (shell access)", 0),
            ("Context awareness (understands project structure)", 0),
            ("Autonomous operation (minimal supervision)", 0),
            ('"Agents are tools in a loop" — Simon Willison', 0),
        ]
    },
    # Slide 9: LLM + Filesystem
    {
        "title": "It is an LLM with filesystem access.",
        "bullets": [
            ("Web Chatbot: Stateless conversations, copy-paste snippets", 0),
            ("Claude Code: Persistent filesystem access, direct file read/write", 0),
            ("Web Chatbot: Describe your environment, human executes commands", 0),
            ("Claude Code: Agent explores and executes autonomously", 0),
        ]
    },
    # Slide 10: Power from simplicity
    {
        "title": "Its power comes from simplicity.",
        "bullets": [
            ("No heavyweight protocols needed", 0),
            ("Skills are just markdown files the agent reads", 0),
            ("Four tools (read, write, edit, bash) outperform complex ecosystems", 0),
            ("Outsources hard parts to the LLM harness and computer environment", 0),
        ]
    },
    # Slide 11: Section 2 Divider
    {
        "title": "Section 2: Context Engineering",
        "bullets": [
            ("The fundamental constraint and how to work around it", 0),
        ]
    },
    # Slide 12: O(N²) constraint
    {
        "title": "O(N²) complexity creates hard limits.",
        "bullets": [
            ("Attention mechanism scales quadratically with sequence length", 0),
            ("Context window is a hard limit on what the model can \"see\"", 0),
            ("Everything the model knows about your task must fit in this window", 0),
            ("Wasted tokens = reduced capability", 0),
        ]
    },
    # Slide 13: Context engineering
    {
        "title": "Context engineering is the key skill.",
        "bullets": [
            ("Minimal system prompts: <1,000 tokens vs competitors' 10,000+", 0),
            ("File-based planning: External markdown preserves info across sessions", 0),
            ("Progressive disclosure: Load tool docs only when needed", 0),
            ("Pre-session artifacts: Research sessions → implementation sessions", 0),
        ]
    },
    # Slide 14: Monitor context
    {
        "title": "/status monitors context in real-time.",
        "bullets": [
            ("Current session: percentage of context window used", 0),
            ("Session reset: when the 5-hour window resets", 0),
            ("Weekly usage across Opus and Sonnet models", 0),
            ("[Figure: status-tab-usage.png]", 0),
        ]
    },
    # Slide 15: Subagents
    {
        "title": "Subagents spawn fresh context windows.",
        "bullets": [
            ("Each subagent gets its own fresh context window", 0),
            ("Example: 36 files ÷ 3 subagents = 12 files each", 0),
            ("Prevents main agent from sequential overload", 0),
            ("Enables parallel processing", 0),
        ]
    },
    # Slide 16: Agentic patterns
    {
        "title": "Agentic patterns have emerged.",
        "bullets": [
            ("Context & Memory: Context-minimization, dynamic injection", 0),
            ("Feedback Loops: Self-critique, reflection, spec-as-test", 0),
            ("Orchestration: Plan-then-execute, phase separation", 0),
            ("Tool Use: CLI-first, code-over-API", 0),
        ]
    },
    # Slide 17: Skills
    {
        "title": "Skills are markdown with instructions.",
        "bullets": [
            ("Just markdown files with YAML metadata", 0),
            ("Brief summaries scanned before full load", 0),
            ("Shareable across models and tools", 0),
            ("No heavyweight protocols", 0),
        ]
    },
    # Slide 18: Scientific skills
    {
        "title": "140+ scientific skills are available.",
        "bullets": [
            ("28+ Scientific databases (OpenAlex, PubMed, ChEMBL, UniProt)", 0),
            ("55+ Python packages (RDKit, Scanpy, PyTorch)", 0),
            ("15+ Scientific integrations (Benchling, DNAnexus)", 0),
            ("Categories: Bioinformatics, Cheminformatics, Clinical Research, ML/AI", 0),
        ]
    },
    # Slide 19: MCP debate
    {
        "title": "MCP can waste 7-9% of context.",
        "bullets": [
            ("Anti-MCP: Tools you never use still consume tokens", 0),
            ("Alternative: CLI tools with README loaded on-demand", 1),
            ("Pro-MCP: Convenience of always-available tools", 0),
            ("Trade-off: Convenience vs. context efficiency", 0),
        ]
    },
    # Slide 20: Git worktree
    {
        "title": "Git worktree enables parallel sessions.",
        "bullets": [
            ("git worktree add ../feature-auth feature/auth", 0),
            ("Run Claude Code in each worktree (separate terminals)", 0),
            ("Single Session: Sequential task completion, one context", 0),
            ("Parallel Sessions: Simultaneous progress, multiple fresh contexts", 0),
        ]
    },
    # Slide 21: Parallelization
    {
        "title": "Parallelization multiplies efficiency.",
        "bullets": [
            ("1. Workflow Design: Define what agents should do", 0),
            ("2. Context Engineering: Optimize what agents can see", 0),
            ("3. Parallelization: Scale by running multiple agents", 0),
            ("Boris Cherny (Claude Code creator) runs 5 Claudes in parallel!", 0),
        ]
    },
    # Slide 22: Section 3 Divider
    {
        "title": "Section 3: Getting Started",
        "bullets": [
            ("Installation, configuration, and safety", 0),
        ]
    },
    # Slide 23: Installation
    {
        "title": "One npm install gets you started.",
        "bullets": [
            ("npm install -g @anthropic-ai/claude-code", 0),
            ("claude --version", 0),
            ("cd your-project && claude", 0),
            ("First run: authenticate, create ~/.claude/, optionally run /init", 0),
        ]
    },
    # Slide 24: Pricing
    {
        "title": "Plans range from $20 to $200/month.",
        "bullets": [
            ("Pro ($20/month): Light usage, small repos", 0),
            ("Max 5x ($100/month): Moderate usage, larger repos", 0),
            ("Max 20x ($200/month): Heavy usage, complex projects", 0),
            ("Usage shared across Claude web, desktop, and Code", 0),
        ]
    },
    # Slide 25: Statusline
    {
        "title": "The statusline shows real-time data.",
        "bullets": [
            ("model.display_name: Current model", 0),
            ("tokens.input / tokens.output: Token counts", 0),
            ("cost.current / cost.total: Cost tracking", 0),
            ("Setup: /statusline show the model name and context usage percentage", 0),
        ]
    },
    # Slide 26: /status command
    {
        "title": "/status shows session info and usage.",
        "bullets": [
            ("Status tab: Version, session ID, model, MCP servers, memory", 0),
            ("Config tab: Preferences, theme, checkpoints", 0),
            ("Usage tab: Context percentage, weekly limits", 0),
            ("[Figure: status-tab-status.png]", 0),
        ]
    },
    # Slide 27: CLAUDE.md
    {
        "title": "CLAUDE.md provides persistent context.",
        "bullets": [
            ("# Project Name → ## Tech Stack → ## Commands → ## Conventions", 0),
            ("Hierarchy: ~/.claude/ → parent → project → subdirectory", 0),
            ("The /init command generates a starter file", 0),
            ("Updates compound over sessions", 0),
        ]
    },
    # Slide 28: Permission modes
    {
        "title": "Four permission modes are available.",
        "bullets": [
            ("default: Prompts for first use of each tool", 0),
            ("acceptEdits: Auto-accepts file edits for session", 0),
            ("plan: Read-only analysis, no modifications", 0),
            ("bypassPermissions: Skips all prompts (safe environment only)", 0),
        ]
    },
    # Slide 29: Granular rules
    {
        "title": "Granular rules provide fine control.",
        "bullets": [
            ('allow: ["Bash(npm run test:*)", "Bash(git:*)"]', 0),
            ('deny: ["Read(./.env)", "Read(**/*.key)"]', 0),
            ('ask: ["Bash(git push:*)", "Bash(rm:*)"]', 0),
            ("Evaluation order: deny → allow → ask", 0),
        ]
    },
    # Slide 30: Hooks
    {
        "title": "Hooks run scripts on tool events.",
        "bullets": [
            ("PreToolUse: Run validation before tool executes", 0),
            ("PostToolUse: Process results after tool completes", 0),
            ("PermissionRequest: Custom permission logic", 0),
            ("Can block, modify, or auto-approve based on custom logic", 0),
        ]
    },
    # Slide 31: Security
    {
        "title": "Three elements create security risk.",
        "bullets": [
            ("1. Access to private data (env vars, credentials)", 0),
            ("2. Exposure to untrusted content (web pages, user input)", 0),
            ("3. External communication ability (network access)", 0),
            ("AI cannot reliably detect prompt injection—architecture must prevent it", 0),
        ]
    },
    # Slide 32: Section 4 Divider
    {
        "title": "Section 4: Cursor vs Alternatives",
        "bullets": [
            ("Comparing tools for different workflows", 0),
        ]
    },
    # Slide 33: Cursor vs Claude Code
    {
        "title": "Cursor is an assistant; Claude Code is an agent.",
        "bullets": [
            ("Cursor: Enhanced IDE, GUI (VS Code fork), User-selectable model", 0),
            ("Claude Code: Autonomous Agent, CLI/Terminal, Claude (optimized)", 0),
            ("Cursor: User-initiated execution, IDE-provided context", 0),
            ("Claude Code: Autonomous execution, Full filesystem + shell", 0),
        ]
    },
    # Slide 34: When to use each
    {
        "title": "Choose based on how you think.",
        "bullets": [
            ("Cursor excels at: Quick inline edits, code explanation, GUI preference", 0),
            ("Claude Code excels at: Multi-file refactoring, autonomous tasks", 0),
            ("Claude Code excels at: Pipeline automation, shell access tasks", 0),
            ("Many developers use both for different contexts", 0),
        ]
    },
    # Slide 35: Alternatives
    {
        "title": "Alternatives offer different trade-offs.",
        "bullets": [
            ("OpenCode: 75+ providers, free — Best for budget, model flexibility", 0),
            ("Aider: Code graph, git integration — Best for monorepos, explicit control", 0),
            ("Gemini CLI: 1M context, free tier — Best for Google Cloud, docs tasks", 0),
            ("Codex CLI: GitHub Actions — Best for CI/CD integration", 0),
        ]
    },
    # Slide 36: Benchmarks
    {
        "title": "Claude Code leads SWE-bench at 80.9%.",
        "bullets": [
            ("Claude Code + Opus 4.5: 80.9%", 0),
            ("Aider: 67%", 0),
            ("Cline: 63%", 0),
            ("Gemini 2.5 Pro: 63.8%", 0),
        ]
    },
    # Slide 37: Section 5 Divider
    {
        "title": "Section 5: Demo & Future",
        "bullets": [
            ("Live demonstration and what's coming next", 0),
        ]
    },
    # Slide 38: This presentation workflow
    {
        "title": "This presentation demonstrates the workflow.",
        "bullets": [
            ("CLAUDE.md (instructions) → scratch/SCRATCH.md (raw notes)", 0),
            ("→ docs/topics/*.md (organized knowledge)", 0),
            ("→ docs/NARRATIVE.md → docs/PRESENTATION.md", 0),
            ("→ *.pptx (Skills-generated output)", 0),
        ]
    },
    # Slide 39: Git commit history
    {
        "title": "Commits document the collaboration.",
        "bullets": [
            ("Initial scaffolding", 0),
            ("Phase 1: Research compilation", 0),
            ("Additional research: permissions, alternatives", 0),
            ("Narrative structure → Slide outline → PPTX generation", 0),
        ]
    },
    # Slide 40: Live demo
    {
        "title": "Let us see Claude Code in action.",
        "bullets": [
            ("Show /status, /statusline commands", 0),
            ("Install a skill via /plugin", 0),
            ("Run /init on a sample project", 0),
            ("Simple code modification task", 0),
        ]
    },
    # Slide 41: Ralph-Wiggum future
    {
        "title": "Ralph-Wiggum treats failure as data.",
        "bullets": [
            ("A simple while loop that feeds an AI agent a prompt until completion", 0),
            ("Deterministic stopping criteria (not \"try once and fail\")", 0),
            ("Failure-as-data philosophy: setbacks guide refinement", 0),
            ("Emerging: Overnight automation, parallel loops, BMAD-METHOD", 0),
        ]
    },
    # Slide 42: Adoption challenge
    {
        "title": "The future is here—adoption is key.",
        "bullets": [
            ("Old: Write code myself → New: Design workflows that write code", 0),
            ("Old: One-shot prompts → New: Iterative loops until done", 0),
            ("Old: Static instructions → New: Continuously improved artifacts", 0),
            ("Start with CLAUDE.md on one project, refine over 5-10 sessions", 0),
        ]
    },
    # Slide 43: Key takeaways
    {
        "title": "Here are the key takeaways.",
        "bullets": [
            ("Claude Code = LLM + filesystem access = general agent", 0),
            ("Workflows compound—every CLAUDE.md update makes the system smarter", 0),
            ("Context engineering is the fundamental skill", 0),
            ("Parallelization via git worktree multiplies efficiency", 0),
        ]
    },
    # Slide 44: Resources
    {
        "title": "Here are resources to get started.",
        "bullets": [
            ("Official: code.claude.com/docs", 0),
            ("Course: DeepLearning.ai Claude Code course", 0),
            ("Skills: github.com/anthropics/skills", 0),
            ("Scientific: K-Dense-AI/claude-scientific-skills", 0),
        ]
    },
    # Slide 45: Questions
    {
        "title": "Questions?",
        "bullets": [
            ("How might this change our team's workflows?", 0),
            ("What tasks would benefit most from agent automation?", 0),
            ("Security considerations for our environment", 0),
            ("Skill development for our specific use cases", 0),
        ]
    },
    # Slide 46: Appendix A1 - Built-in tools
    {
        "title": "Claude Code uses only four core tools.",
        "bullets": [
            ("Read: File contents, images, PDFs", 0),
            ("Write: Create new files", 0),
            ("Edit: String replacement in files", 0),
            ("Bash: Shell command execution", 0),
        ]
    },
    # Slide 47: Appendix A2 - MCP setup
    {
        "title": "MCP servers extend capabilities.",
        "bullets": [
            ("/plugin install @anthropic-ai/mcp-server-github", 0),
            ("/plugin install @anthropic-ai/mcp-server-context7", 0),
            ("Available servers: GitHub, databases, APIs", 0),
            ("Trade-off: Convenience vs. context window overhead", 0),
        ]
    },
    # Slide 48: Appendix A3 - Gemini CLI
    {
        "title": "Gemini CLI offers 1M token context.",
        "bullets": [
            ("1 million token context window", 0),
            ("60 requests/minute, 1000/day (free)", 0),
            ("Deep Google Cloud integration", 0),
            ("Lower SWE-bench scores than Claude", 0),
        ]
    },
]

def generate_replacement_json():
    """Generate the replacement JSON for all 49 slides."""
    result = {}

    for i, slide in enumerate(slides):
        slide_key = f"slide-{i}"
        result[slide_key] = {}

        # Shape-0 is always the title
        title_paragraphs = [{"text": slide["title"], "bold": True}]
        result[slide_key]["shape-0"] = {"paragraphs": title_paragraphs}

        # Shape-1 is the body content
        if "body" in slide:
            # Title slide has simple body text
            body_paragraphs = [{"text": slide["body"]}]
        elif "bullets" in slide:
            # Content slides have bullet points
            body_paragraphs = []
            for text, level in slide["bullets"]:
                para = {
                    "text": text,
                    "bullet": True,
                    "level": level,
                }
                body_paragraphs.append(para)
        else:
            body_paragraphs = []

        result[slide_key]["shape-1"] = {"paragraphs": body_paragraphs}

    return result

if __name__ == "__main__":
    replacement_data = generate_replacement_json()

    output_file = "replacement-text-49.json"
    with open(output_file, "w") as f:
        json.dump(replacement_data, f, indent=2)

    print(f"Generated replacement JSON for {len(slides)} slides")
    print(f"Output saved to: {output_file}")
