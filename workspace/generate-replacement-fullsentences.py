#!/usr/bin/env python3
"""Generate replacement JSON with full-sentence titles (concise but complete)."""

import json

# Slide content with CONCISE FULL SENTENCE titles
# Each title is a complete sentence that captures the key insight
slides = [
    # Slide 0: Title
    {
        "title": "Claude Code: From Coding to Workflow Design",
        "body": "Internal Computational Team\nJanuary 2026"
    },
    # Slide 1
    {
        "title": "We're stuck in an old mental model of development.",
        "bullets": [
            ("Old: Developer writes code line by line", 0),
            ("New: Developer describes outcomes", 0),
            ("Old: IDE assists with autocomplete", 0),
            ("New: Agent plans and executes", 0),
            ("Old: Human is the executor", 0),
            ("New: Human supervises and validates", 0),
        ]
    },
    # Slide 2
    {
        "title": "Engineers now design systems, not write software.",
        "bullets": [
            ("One person built a Polymarket tool in 2 hours without writing code", 0),
            ("The technique mattered more than which AI was used", 0),
            ("Architecture and process design become primary skills", 0),
            ('"The outcome is defined by the process, not the model." — Mike.tech', 0),
        ]
    },
    # Slide 3
    {
        "title": "Communicate intent structurally—let agents find the implementation.",
        "bullets": [
            ("Use XML tags: <task>, <context>, <constraints>, <output_format>", 0),
            ("Code-Level: \"Write a function that...\" → Focus on implementation", 0),
            ("Abstract: \"I need to transform X into Y\" → Focus on intent", 0),
            ('"It\'s like I was driving a race car in first gear the whole time."', 0),
        ]
    },
    # Slide 4
    {
        "title": "Every CLAUDE.md update compounds your efficiency gains.",
        "bullets": [
            ("Session 1: Write CLAUDE.md with basic project context", 0),
            ("Session 5: Add common commands, conventions, warnings", 1),
            ("Session 20: Refined skills, custom hooks, team patterns", 1),
            ("Session 100: Agent works like a trained team member", 1),
        ]
    },
    # Slide 5
    {
        "title": "Claude Code is a general agent, not just a coding tool.",
        "bullets": [
            ("February 2025: Launch as CLI research preview", 0),
            ("October 2025: Web launch on claude.ai", 0),
            ("November 2025: $1B revenue run-rate", 0),
            ("January 2026: Multi-agent infrastructure (v2.1.0)", 0),
        ]
    },
    # Slide 6
    {
        "title": "Claude Code automates anything you can type into a computer.",
        "bullets": [
            ("File system access (read, write, edit)", 0),
            ("Command execution (shell access)", 0),
            ("Context awareness (understands project structure)", 0),
            ("Autonomous operation (minimal supervision)", 0),
            ('"Agents are tools in a loop" — Simon Willison', 0),
        ]
    },
    # Slide 7
    {
        "title": "Claude Code is an LLM with permission to access a file system.",
        "bullets": [
            ("Web Chatbot: Stateless conversations, copy-paste snippets", 0),
            ("Claude Code: Persistent filesystem access, direct file read/write", 0),
            ("Web Chatbot: Describe your environment, human executes commands", 0),
            ("Claude Code: Agent explores and executes autonomously", 0),
        ]
    },
    # Slide 8
    {
        "title": "Claude Code's power comes from its simplicity.",
        "bullets": [
            ("No heavyweight protocols needed", 0),
            ("Skills are just markdown files the agent reads", 0),
            ("Four tools (read, write, edit, bash) outperform complex ecosystems", 0),
            ("Outsources hard parts to the LLM harness and computer environment", 0),
        ]
    },
    # Slide 9
    {
        "title": "Transformers have a hard context limit due to O(N²) complexity.",
        "bullets": [
            ("Attention mechanism scales quadratically with sequence length", 0),
            ("Context window is a hard limit on what the model can \"see\"", 0),
            ("Everything the model knows about your task must fit in this window", 0),
            ("Wasted tokens = reduced capability", 0),
        ]
    },
    # Slide 10
    {
        "title": "Context engineering is the fundamental skill for agent work.",
        "bullets": [
            ("Minimal system prompts: <1,000 tokens vs competitors' 10,000+", 0),
            ("File-based planning: External markdown preserves info across sessions", 0),
            ("Progressive disclosure: Load tool docs only when needed", 0),
            ("Pre-session artifacts: Research sessions → implementation sessions", 0),
        ]
    },
    # Slide 11
    {
        "title": "The /status command lets you monitor context usage in real-time.",
        "bullets": [
            ("Current session: percentage of context window used", 0),
            ("Session reset: when the 5-hour window resets", 0),
            ("Weekly usage across Opus and Sonnet models", 0),
            ("Demo the /status command", 0),
        ]
    },
    # Slide 12
    {
        "title": "Subagents spawn fresh context windows for parallel tasks.",
        "bullets": [
            ("Each subagent gets its own fresh context window", 0),
            ("Example: 36 files ÷ 3 subagents = 12 files each", 0),
            ("Prevents main agent from sequential overload", 0),
            ("Enables parallel processing", 0),
        ]
    },
    # Slide 13
    {
        "title": "A taxonomy of agentic patterns has emerged from practice.",
        "bullets": [
            ("Context & Memory: Context-minimization, dynamic injection", 0),
            ("Feedback Loops: Self-critique, reflection, spec-as-test", 0),
            ("Orchestration: Plan-then-execute, phase separation", 0),
            ("Tool Use: CLI-first, code-over-API", 0),
        ]
    },
    # Slide 14
    {
        "title": "Skills are markdown files that Claude loads on demand.",
        "bullets": [
            ("Just markdown files with YAML metadata", 0),
            ("Brief summaries scanned before full load", 0),
            ("Shareable across models and tools", 0),
            ("No heavyweight protocols", 0),
        ]
    },
    # Slide 15
    {
        "title": "140+ scientific skills cover databases, packages, and integrations.",
        "bullets": [
            ("28+ Scientific databases (OpenAlex, PubMed, ChEMBL, UniProt)", 0),
            ("55+ Python packages (RDKit, Scanpy, PyTorch)", 0),
            ("15+ Scientific integrations (Benchling, DNAnexus)", 0),
            ("Categories: Bioinformatics, Cheminformatics, Clinical Research, ML/AI", 0),
        ]
    },
    # Slide 16
    {
        "title": "MCP servers can waste 7-9% of context window on unused tools.",
        "bullets": [
            ("Anti-MCP: Tools you never use still consume tokens", 0),
            ("Alternative: CLI tools with README loaded on-demand", 0),
            ("Pro-MCP: Convenience of always-available tools", 0),
            ("Trade-off: Convenience vs. context efficiency", 0),
        ]
    },
    # Slide 17
    {
        "title": "Git worktree enables running multiple Claude sessions in parallel.",
        "bullets": [
            ("git worktree add ../feature-auth feature/auth", 0),
            ("git worktree add ../feature-api feature/api", 0),
            ("Run Claude Code in each (separate terminals)", 0),
            ("Boris Cherny (Claude Code creator) runs 5 Claudes in parallel!", 0),
        ]
    },
    # Slide 18
    {
        "title": "Workflow, context, and parallelization are the efficiency pillars.",
        "bullets": [
            ("1. Workflow Design: Define what agents should do", 0),
            ("2. Context Engineering: Optimize what agents can see", 0),
            ("3. Parallelization: Scale by running multiple agents", 0),
            ("Once you trust the workflow, multiplying it becomes obvious", 0),
        ]
    },
    # Slide 19
    {
        "title": "Getting started requires one npm install and authentication.",
        "bullets": [
            ("npm install -g @anthropic-ai/claude-code", 0),
            ("claude --version", 0),
            ("cd your-project && claude", 0),
            ("First run: authenticate, create ~/.claude/, optionally run /init", 0),
        ]
    },
    # Slide 20
    {
        "title": "Subscription plans range from $20 to $200/month.",
        "bullets": [
            ("Pro: $20/month — Light usage, small repos", 0),
            ("Max 5x: $100/month — Moderate usage, larger repos", 0),
            ("Max 20x: $200/month — Heavy usage, complex projects", 0),
            ("Usage shared across Claude web, desktop, and Code", 0),
        ]
    },
    # Slide 21
    {
        "title": "A customizable statusline displays model, cost, and tokens.",
        "bullets": [
            ("model.display_name: Current model", 0),
            ("tokens.input / tokens.output: Token counts", 0),
            ("cost.current / cost.total: Cost tracking", 0),
            ("Setup: /statusline show the model name and context usage percentage", 0),
        ]
    },
    # Slide 22
    {
        "title": "The /status command shows session info, config, and usage.",
        "bullets": [
            ("Status: Version, session ID, model, MCP servers, memory", 0),
            ("Config: Preferences, theme, checkpoints", 0),
            ("Usage: Context percentage, weekly limits", 0),
            ("Demo switching between tabs with Tab key", 0),
        ]
    },
    # Slide 23
    {
        "title": "CLAUDE.md gives Claude persistent project-specific context.",
        "bullets": [
            ("# Project Name, ## Tech Stack, ## Commands, ## Conventions", 0),
            ("Example: Python 3.11, FastAPI, PostgreSQL", 1),
            ("Example: pytest tests/, uvicorn main:app --reload", 1),
            ("Hierarchy: ~/.claude/ → parent → project → subdirectory", 0),
        ]
    },
    # Slide 24
    {
        "title": "Four permission modes balance control and convenience.",
        "bullets": [
            ("default: Prompts for first use of each tool", 0),
            ("acceptEdits: Auto-accepts file edits for session", 0),
            ("plan: Read-only analysis, no modifications", 0),
            ("bypassPermissions: Skips all prompts (safe environment only)", 0),
            ("Switch with Shift+Tab", 0),
        ]
    },
    # Slide 25
    {
        "title": "Granular allow/deny/ask rules provide fine-grained control.",
        "bullets": [
            ('allow: ["Bash(npm run test:*)", "Bash(git:*)"]', 0),
            ('deny: ["Read(./.env)", "Read(**/*.key)"]', 0),
            ('ask: ["Bash(git push:*)", "Bash(rm:*)"]', 0),
            ("Evaluation order: deny → allow → ask", 0),
        ]
    },
    # Slide 26
    {
        "title": "Hooks let you run custom scripts before and after tool execution.",
        "bullets": [
            ("PreToolUse: Run validator before Bash commands", 0),
            ("PostToolUse: Run scripts after tool execution", 0),
            ("PermissionRequest: Custom permission logic", 0),
            ("Can block, modify, or auto-approve based on custom logic", 0),
        ]
    },
    # Slide 27
    {
        "title": 'The "Lethal Trifecta" identifies three data theft risk elements.',
        "bullets": [
            ("1. Access to private data (env vars, credentials)", 0),
            ("2. Exposure to untrusted content (web pages, user input)", 0),
            ("3. External communication ability (network access)", 0),
            ('"Text into your LLM = full control over what tools it runs"', 0),
        ]
    },
    # Slide 28
    {
        "title": "Cursor is an AI assistant; Claude Code is an autonomous agent.",
        "bullets": [
            ("Paradigm: Cursor = Enhanced IDE, Claude Code = Autonomous Agent", 0),
            ("Interface: Cursor = GUI (VS Code fork), Claude Code = CLI", 0),
            ("Model: Cursor = User-selectable, Claude Code = Claude (optimized)", 0),
            ("Execution: Cursor = User-initiated, Claude Code = Autonomous", 0),
            ("Context: Cursor = IDE-provided, Claude Code = Full filesystem + shell", 0),
        ]
    },
    # Slide 29
    {
        "title": "Think in files → use Cursor. Think in tasks → use Claude Code.",
        "bullets": [
            ("Cursor excels at: Quick inline edits, code explanation, GUI preference", 0),
            ("Claude Code excels at: Multi-file refactoring, autonomous completion", 0),
            ("Claude Code: Pipeline automation, tasks requiring shell access", 0),
            ("Many developers use both for different contexts", 0),
        ]
    },
    # Slide 30
    {
        "title": "OpenCode, Aider, and Gemini CLI offer different trade-offs.",
        "bullets": [
            ("OpenCode: 75+ providers, free — Budget, model flexibility", 0),
            ("Aider: Code graph, git integration — Monorepos, explicit control", 0),
            ("Gemini CLI: 1M context, free tier — Google Cloud, docs tasks", 0),
            ("Codex CLI: GitHub Actions — CI/CD integration", 0),
        ]
    },
    # Slide 31
    {
        "title": "Claude Code with Opus 4.5 leads SWE-bench at 80.9%.",
        "bullets": [
            ("Claude Code + Opus 4.5: 80.9%", 0),
            ("Aider: 67%", 0),
            ("Cline: 63%", 0),
            ("Gemini 2.5 Pro: 63.8%", 0),
            ("Benchmarks vary by methodology", 0),
        ]
    },
    # Slide 32
    {
        "title": "This presentation demonstrates the workflow we've described.",
        "bullets": [
            ("CLAUDE.md (instructions) → scratch/SCRATCH.md (raw notes)", 0),
            ("docs/topics/*.md (organized knowledge)", 1),
            ("docs/NARRATIVE.md (flow structure)", 1),
            ("docs/PRESENTATION.md (slide outline)", 1),
            ("*.pptx (Skills-generated output)", 1),
        ]
    },
    # Slide 33
    {
        "title": "Each commit documents the human-agent collaboration.",
        "bullets": [
            ("1. Initial scaffolding", 0),
            ("2. Phase 1: Research compilation", 0),
            ("3. Additional research: permissions, alternatives", 0),
            ("4. Narrative structure", 0),
            ("5. Slide outline generation", 0),
        ]
    },
    # Slide 34
    {
        "title": "[Live Demo] Claude Code workflow on a practical task.",
        "bullets": [
            ("1. Show /status, /statusline commands", 0),
            ("2. Install a skill via /plugin", 0),
            ("3. Run /init on a sample project", 0),
            ("4. Simple code modification task", 0),
        ]
    },
    # Slide 35
    {
        "title": "Ralph-Wiggum: iterative loops that treat failure as data.",
        "bullets": [
            ('"A while loop that feeds an AI agent a prompt until completion"', 0),
            ("Deterministic stopping criteria (not \"try once and fail\")", 0),
            ("Failure-as-data philosophy: setbacks guide refinement", 0),
            ("Prompt-centric design: \"LLMs are mirrors of operator skill\"", 0),
        ]
    },
    # Slide 36
    {
        "title": "The future is here—adoption is the primary challenge.",
        "bullets": [
            ("Old: Write code myself → New: Design workflows that write code", 0),
            ("Old: One-shot prompts → New: Iterative loops until done", 0),
            ("Old: Static instructions → New: Continuously improved artifacts", 0),
            ("Old: Single session → New: Parallel agents on worktrees", 0),
        ]
    },
    # Slide 37
    {
        "title": "Compound efficiency through workflow, context, and parallelization.",
        "bullets": [
            ("1. Claude Code = LLM + filesystem access = general agent", 0),
            ("2. Workflows compound—every CLAUDE.md update improves the system", 0),
            ("3. Context engineering is the fundamental skill", 0),
            ("4. Parallelization via git worktree multiplies efficiency", 0),
            ("5. The future is iterative loops that run until completion", 0),
        ]
    },
    # Slide 38
    {
        "title": "Resources for getting started with Claude Code.",
        "bullets": [
            ("Official: code.claude.com/docs", 0),
            ("DeepLearning.ai Course", 1),
            ("Skills: github.com/anthropics/skills", 0),
            ("K-Dense-AI/claude-scientific-skills", 1),
        ]
    },
    # Slide 39
    {
        "title": "Questions?",
        "bullets": [
            ("How might this change our team's workflows?", 0),
            ("What tasks would benefit most from agent automation?", 0),
            ("Security considerations for our environment", 0),
            ("Skill development for our specific use cases", 0),
        ]
    },
    # Appendix A1
    {
        "title": "Claude Code uses only four core tools: Read, Write, Edit, Bash.",
        "bullets": [
            ("Read: File contents, images, PDFs", 0),
            ("Write: Create new files", 0),
            ("Edit: String replacement in files", 0),
            ("Bash: Shell command execution", 0),
            ('"Four tools outperform complex tool ecosystems" — Mario Zechner', 0),
        ]
    },
    # Appendix A2
    {
        "title": "MCP servers extend Claude Code with external tool capabilities.",
        "bullets": [
            ("/plugin install @anthropic-ai/mcp-server-github", 0),
            ("/plugin install @anthropic-ai/mcp-server-context7", 0),
            ("Available servers: GitHub, databases, APIs", 0),
            ("Trade-off: Convenience vs. context window overhead", 0),
        ]
    },
    # Appendix A3
    {
        "title": "Gemini CLI provides 1M token context and a generous free tier.",
        "bullets": [
            ("1 million token context window", 0),
            ("60 requests/minute, 1000/day (free)", 0),
            ("Deep Google Cloud integration", 0),
            ("Lower SWE-bench scores than Claude", 0),
            ("Best for: Google Cloud users, documentation, exploration", 0),
        ]
    },
]

def generate_replacement():
    replacement = {}

    for i, slide in enumerate(slides):
        slide_key = f"slide-{i}"
        replacement[slide_key] = {}

        # Title shape - use slightly smaller font for longer titles
        title_len = len(slide["title"])
        if title_len > 60:
            title_font_size = 22.0
        elif title_len > 45:
            title_font_size = 24.0
        else:
            title_font_size = 28.0

        replacement[slide_key]["shape-0"] = {
            "paragraphs": [{"text": slide["title"], "bold": True, "font_size": title_font_size}]
        }

        # Body shape
        if "body" in slide:
            # Title slide with plain body
            replacement[slide_key]["shape-1"] = {
                "paragraphs": [{"text": slide["body"], "alignment": "CENTER"}]
            }
        elif "bullets" in slide:
            # Content slide with bullets
            paragraphs = []
            for item in slide["bullets"]:
                if isinstance(item, tuple):
                    text, level = item
                else:
                    text, level = item, 0
                paragraphs.append({
                    "text": text,
                    "bullet": True,
                    "level": level
                })
            replacement[slide_key]["shape-1"] = {"paragraphs": paragraphs}

    return replacement

if __name__ == "__main__":
    replacement = generate_replacement()
    with open("workspace/replacement-text-fullsentences.json", "w") as f:
        json.dump(replacement, f, indent=2)
    print(f"Generated replacement JSON with {len(replacement)} slides")

    # Print titles for review
    print("\nTitles for review:")
    for i, slide in enumerate(slides):
        marker = "✓" if len(slide["title"]) <= 60 else "⚠"
        print(f"  {i+1:2}. {marker} ({len(slide['title']):2} chars) {slide['title']}")
