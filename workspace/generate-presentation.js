const pptxgen = require('pptxgenjs');
const html2pptx = require('/Users/somite-changheelee/.claude/plugins/cache/anthropic-agent-skills/document-skills/69c0b1a06741/skills/pptx/scripts/html2pptx.js');
const fs = require('fs');
const path = require('path');

// Design palette - Professional slate blue theme
const COLORS = {
    primary: '#3B5265',      // Slate blue
    secondary: '#64A5B9',    // Light teal
    accent: '#40A9A3',       // Teal accent
    dark: '#2D3E4E',         // Dark slate
    light: '#F5F7FA',        // Light background
    white: '#FFFFFF',
    text: '#2D3E4E',
    lightText: '#6B7B8A',
    codeBg: '#F0F4F8',
    quoteBg: '#EEF4F7'
};

const WORKSPACE = '/Users/somite-changheelee/Desktop/04_Presentations/20260114 ClaudeCode/workspace';
const FIGURES = '/Users/somite-changheelee/Desktop/04_Presentations/20260114 ClaudeCode/figures';

// Ensure workspace exists
if (!fs.existsSync(WORKSPACE)) fs.mkdirSync(WORKSPACE, { recursive: true });

// Slide definitions from PRESENTATION.md
const slides = [
    // Slide 1: Title
    {
        type: 'title',
        title: 'Claude Code: From Coding to Workflow Design',
        subtitle: 'Internal Computational Team\nJanuary 2026'
    },
    // Slide 2
    {
        type: 'comparison',
        title: "We're stuck in an old mental model of development",
        table: {
            headers: ['Old Model', 'New Model'],
            rows: [
                ['Developer writes code line by line', 'Developer describes outcomes'],
                ['IDE assists with autocomplete', 'Agent plans and executes'],
                ['Human is the executor', 'Human supervises and validates']
            ]
        },
        note: "The shift isn't about better autocomplete—it's about changing who does the work."
    },
    // Slide 3
    {
        type: 'content_image',
        title: "Engineers are no longer writing software—they're designing higher-order systems",
        bullets: [
            'One person built a Polymarket analysis tool in 2 hours without writing code',
            'The technique mattered more than which AI was used',
            'Architecture and process design become primary skills'
        ],
        quote: '"The outcome is defined by the process, not the model." — Mike.tech',
        image: 'blog-mike-tech-death-of-software.png'
    },
    // Slide 4
    {
        type: 'content_code',
        title: "Communicate intent structurally—let the agent find the implementation",
        code: `<task>What you want Claude to do</task>
<context>Background information it needs</context>
<constraints>Any limits or rules</constraints>
<output_format>How you want the answer</output_format>`,
        table: {
            headers: ['Code-Level Thinking', 'Abstract Thinking'],
            rows: [
                ['"Write a function that..."', '"I need to transform X into Y"'],
                ['Focus on implementation', 'Focus on intent'],
                ['One solution path', 'Multiple approaches possible']
            ]
        },
        quote: '"It\'s like I was driving a race car in first gear the whole time."',
        image: 'reddit-xml-structured-prompting.png'
    },
    // Slide 5
    {
        type: 'content_image',
        title: 'Every update to CLAUDE.md, skills, and artifacts compounds your efficiency gains',
        code: `Session 1: Write CLAUDE.md with basic project context
    ↓
Session 5: Add common commands, conventions, warnings
    ↓
Session 20: Refined skills, custom hooks, team patterns
    ↓
Session 100: Agent works like a trained team member`,
        bullets: [
            'Update CLAUDE.md → agent behaves better → update again',
            'Create skills → reuse across projects → refine based on failures',
            'Artifacts persist → knowledge compounds → efficiency accelerates'
        ],
        image: 'workflow-improvement-loop.png'
    },
    // Slide 6
    {
        type: 'timeline',
        title: 'Claude Code is a general agent for computer automation, not just a coding tool',
        events: [
            { date: 'February 2025', text: 'Launch as CLI research preview' },
            { date: 'October 2025', text: 'Web launch on claude.ai' },
            { date: 'November 2025', text: '$1B revenue run-rate' },
            { date: 'January 2026', text: 'Multi-agent infrastructure (v2.1.0)' }
        ]
    },
    // Slide 7
    {
        type: 'content',
        title: 'Claude Code can automate anything you can achieve by typing commands into a computer',
        bullets: [
            'File system access (read, write, edit)',
            'Command execution (shell access)',
            'Context awareness (understands project structure)',
            'Autonomous operation (minimal supervision)'
        ],
        quote: '"2025 has become the year of agents... agents are \'tools in a loop\'" — Simon Willison'
    },
    // Slide 8: Key insight
    {
        type: 'comparison',
        title: 'Claude Code is an LLM that got permission to access a file system',
        table: {
            headers: ['Web Chatbot', 'Claude Code'],
            rows: [
                ['Stateless conversations', 'Persistent filesystem access'],
                ['Copy-paste code snippets', 'Direct file read/write'],
                ['Describe your environment', 'Agent explores your environment'],
                ['Human executes commands', 'Agent executes commands'],
                ['No memory between sessions', 'Project context via CLAUDE.md']
            ]
        },
        quote: '"An LLM that got permission to access a file system" — Simon Willison'
    },
    // Slide 9
    {
        type: 'content',
        title: "Claude Code's power comes from its simplicity: minimal protocol, maximum capability",
        bullets: [
            'No heavyweight protocols needed',
            'Skills are just markdown files the agent reads',
            'Four tools (read, write, edit, bash) outperform complex ecosystems',
            '"Outsources the hard parts to the LLM harness and the computer environment"'
        ]
    },
    // Slide 10
    {
        type: 'content',
        title: 'The O(N²) memory complexity of transformers creates a hard context limit',
        bullets: [
            'Attention mechanism scales quadratically with sequence length',
            'Context window is a hard limit on what the model can "see"',
            'Everything the model knows about your task must fit in this window',
            'Wasted tokens = reduced capability'
        ]
    },
    // Slide 11
    {
        type: 'content',
        title: 'Context engineering—managing what enters the context window—is the fundamental skill',
        bullets: [
            'Minimal system prompts: <1,000 tokens vs competitors\' 10,000+',
            'File-based planning: External markdown preserves info across sessions',
            'Progressive disclosure: Load tool docs only when needed',
            'Pre-session artifacts: Research sessions → implementation sessions'
        ]
    },
    // Slide 12
    {
        type: 'content_image',
        title: 'The /status command lets you monitor context usage in real-time',
        bullets: [
            'Current session: percentage of context window used',
            'Session reset: when the 5-hour window resets',
            'Weekly usage across Opus and Sonnet models'
        ],
        image: 'status-tab-usage.png'
    },
    // Slide 13
    {
        type: 'content',
        title: 'Subagents spawn fresh context windows to handle parallel tasks',
        bullets: [
            'Each subagent gets its own fresh context window',
            'Example: 36 files ÷ 3 subagents = 12 files each',
            'Prevents main agent from sequential overload',
            'Enables parallel processing'
        ]
    },
    // Slide 14
    {
        type: 'table_slide',
        title: 'A taxonomy of agentic patterns has emerged from practical experience',
        table: {
            headers: ['Category', 'Example Patterns'],
            rows: [
                ['Context & Memory', 'Context-minimization, dynamic injection'],
                ['Feedback Loops', 'Self-critique, reflection, spec-as-test'],
                ['Orchestration', 'Plan-then-execute, phase separation'],
                ['Tool Use', 'CLI-first, code-over-API']
            ]
        }
    },
    // Slide 15
    {
        type: 'content',
        title: 'Skills are elegantly simple: markdown files with instructions that Claude loads on demand',
        bullets: [
            'Just markdown files with YAML metadata',
            'Brief summaries scanned before full load',
            'Shareable across models and tools',
            'No heavyweight protocols'
        ]
    },
    // Slide 16
    {
        type: 'content',
        title: '140+ scientific skills cover databases, packages, and integrations',
        bullets: [
            '28+ Scientific databases (OpenAlex, PubMed, ChEMBL, UniProt)',
            '55+ Python packages (RDKit, Scanpy, PyTorch)',
            '15+ Scientific integrations (Benchling, DNAnexus)'
        ],
        note: 'Categories: Bioinformatics, Cheminformatics, Clinical Research, ML/AI'
    },
    // Slide 17
    {
        type: 'content',
        title: 'MCP servers can waste 7-9% of context window with unused tool descriptions',
        bullets: [
            'Anti-MCP: Tools you never use still consume tokens',
            'Alternative: CLI tools with README loaded on-demand',
            'Pro-MCP: Convenience of always-available tools',
            'Trade-off: Convenience vs. context efficiency'
        ]
    },
    // Slide 18
    {
        type: 'content_code_image',
        title: 'Once workflows are automated, git worktree enables running multiple sessions in parallel',
        code: `# Create parallel worktrees for independent tasks
git worktree add ../feature-auth feature/auth
git worktree add ../feature-api feature/api

# Run Claude Code in each (separate terminals)
cd ../feature-auth && claude
cd ../feature-api && claude`,
        image: 'tweet-boris-cherny-parallel-claudes.png'
    },
    // Slide 19
    {
        type: 'content',
        title: 'Workflow → Context → Parallelization: three pillars of agent-era efficiency',
        bullets: [
            '1. Workflow Design: Define what agents should do',
            '2. Context Engineering: Optimize what agents can see',
            '3. Parallelization: Scale by running multiple agents'
        ],
        note: 'Once you trust the workflow, multiplying it becomes the obvious next step.'
    },
    // Slide 20
    {
        type: 'content_code',
        title: 'Getting started requires one npm install and authentication',
        code: `npm install -g @anthropic-ai/claude-code
claude --version
cd your-project
claude`,
        note: 'First run: authenticate, create ~/.claude/, optionally run /init'
    },
    // Slide 21
    {
        type: 'table_slide',
        title: 'Subscription plans range from Pro ($20) to Max 20x ($200) based on usage needs',
        table: {
            headers: ['Plan', 'Price', 'Best For'],
            rows: [
                ['Pro', '$20/month', 'Light usage, small repos'],
                ['Max 5x', '$100/month', 'Moderate usage, larger repos'],
                ['Max 20x', '$200/month', 'Heavy usage, complex projects']
            ]
        },
        note: 'Usage shared across Claude web, desktop, and Code.'
    },
    // Slide 22
    {
        type: 'content_code',
        title: 'A customizable statusline displays model, cost, and tokens in real-time',
        code: `model.display_name  # Current model
tokens.input / tokens.output  # Token counts
cost.current / cost.total  # Cost tracking
git.branch  # Current branch`,
        note: 'Setup: /statusline show the model name and context usage percentage'
    },
    // Slide 23
    {
        type: 'content_image',
        title: 'The /status command shows session info, config, and usage in tabs',
        bullets: [
            'Status: Version, session ID, model, MCP servers, memory',
            'Config: Preferences, theme, checkpoints',
            'Usage: Context percentage, weekly limits'
        ],
        image: 'status-tab-status.png'
    },
    // Slide 24
    {
        type: 'content_code',
        title: 'CLAUDE.md files give Claude persistent project-specific context at every session',
        code: `# Project Name
## Tech Stack
- Python 3.11, FastAPI, PostgreSQL
## Commands
- pytest tests/
- uvicorn main:app --reload
## Conventions
- Type hints required
- Google-style docstrings`,
        note: 'Hierarchy: ~/.claude/ → parent → project → subdirectory'
    },
    // Slide 25
    {
        type: 'table_slide',
        title: 'Four permission modes let you choose the right balance of control and convenience',
        table: {
            headers: ['Mode', 'Behavior'],
            rows: [
                ['default', 'Prompts for first use of each tool'],
                ['acceptEdits', 'Auto-accepts file edits for session'],
                ['plan', 'Read-only analysis, no modifications'],
                ['bypassPermissions', 'Skips all prompts (safe environment only)']
            ]
        },
        note: 'Switch with Shift+Tab'
    },
    // Slide 26
    {
        type: 'content_code',
        title: 'Granular allow/deny/ask rules in settings.json provide fine-grained control',
        code: `{
  "permissions": {
    "allow": ["Bash(npm run test:*)", "Bash(git:*)"],
    "deny": ["Read(./.env)", "Read(**/*.key)"],
    "ask": ["Bash(git push:*)", "Bash(rm:*)"]
  }
}`,
        note: 'Evaluation order: deny → allow → ask'
    },
    // Slide 27
    {
        type: 'content_code',
        title: 'Hooks let you run custom scripts before and after tool execution',
        code: `{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{"type": "command",
                 "command": "/path/to/validator.sh"}]
    }]
  }
}`,
        note: 'Events: PreToolUse, PostToolUse, PermissionRequest'
    },
    // Slide 28
    {
        type: 'content',
        title: 'The "Lethal Trifecta" identifies three elements that create data theft risk',
        bullets: [
            '1. Access to private data (env vars, credentials)',
            '2. Exposure to untrusted content (web pages, user input)',
            '3. External communication ability (network access)'
        ],
        quote: '"Anyone who can get text into your LLM has full control over what tools it runs next"'
    },
    // Slide 29
    {
        type: 'comparison',
        title: 'Cursor is an AI assistant; Claude Code is an autonomous agent',
        table: {
            headers: ['Aspect', 'Cursor IDE', 'Claude Code'],
            rows: [
                ['Paradigm', 'Enhanced IDE', 'Autonomous Agent'],
                ['Interface', 'GUI (VS Code fork)', 'CLI / Terminal'],
                ['Model', 'User-selectable', 'Claude (optimized)'],
                ['Execution', 'User-initiated', 'Autonomous'],
                ['Context', 'IDE-provided', 'Full filesystem + shell']
            ]
        }
    },
    // Slide 30
    {
        type: 'two_column',
        title: 'If you think in files and edits, use Cursor; if you think in tasks and outcomes, use Claude Code',
        leftTitle: 'Cursor excels at',
        leftBullets: ['Quick inline edits', 'Code explanation while reading', 'GUI preference', 'Multiple AI providers'],
        rightTitle: 'Claude Code excels at',
        rightBullets: ['Multi-file refactoring', 'Autonomous task completion', 'Pipeline automation', 'Tasks requiring shell access']
    },
    // Slide 31
    {
        type: 'table_slide',
        title: 'Alternatives like OpenCode, Aider, and Gemini CLI offer different trade-offs',
        table: {
            headers: ['Tool', 'Strength', 'Best For'],
            rows: [
                ['OpenCode', '75+ providers, free', 'Budget, model flexibility'],
                ['Aider', 'Code graph, git integration', 'Monorepos, explicit control'],
                ['Gemini CLI', '1M context, free tier', 'Google Cloud, docs tasks'],
                ['Codex CLI', 'GitHub Actions', 'CI/CD integration']
            ]
        }
    },
    // Slide 32
    {
        type: 'table_slide',
        title: 'Claude Code with Opus 4.5 leads SWE-bench at 80.9%',
        table: {
            headers: ['Tool/Model', 'SWE-bench Score'],
            rows: [
                ['Claude Code + Opus 4.5', '80.9%'],
                ['Aider', '67%'],
                ['Cline', '63%'],
                ['Gemini 2.5 Pro', '63.8%']
            ]
        },
        note: 'Benchmarks vary by methodology'
    },
    // Slide 33
    {
        type: 'content_code',
        title: 'This presentation demonstrates the workflow: CLAUDE.md → research → topics → PPTX',
        code: `CLAUDE.md (instructions)
    ↓
scratch/SCRATCH.md (raw notes)
    ↓
docs/topics/*.md (organized knowledge)
    ↓
docs/NARRATIVE.md (flow structure)
    ↓
docs/PRESENTATION.md (slide outline)
    ↓
*.pptx (Skills-generated output)`
    },
    // Slide 34
    {
        type: 'content',
        title: 'Each meaningful change was committed, documenting the human-agent collaboration',
        bullets: [
            '1. Initial scaffolding',
            '2. Phase 1: Research compilation',
            '3. Additional research: permissions, alternatives',
            '4. Narrative structure',
            '5. Slide outline generation'
        ],
        note: 'Run `git log --oneline` live.'
    },
    // Slide 35
    {
        type: 'content',
        title: '[Live Demo] Claude Code workflow on a practical task',
        bullets: [
            '1. Show /status, /statusline commands',
            '2. Install a skill via /plugin',
            '3. Run /init on a sample project',
            '4. Simple code modification task'
        ],
        note: 'Keep scope small—one clear task with visible completion.'
    },
    // Slide 36
    {
        type: 'content_image',
        title: 'Ralph-Wiggum: iterative loops that treat failure as data, not exit condition',
        bullets: [
            'Deterministic stopping criteria (not "try once and fail")',
            'Failure-as-data philosophy: setbacks guide refinement',
            'Prompt-centric design: "LLMs are mirrors of operator skill"'
        ],
        quote: '"A simple while loop that repeatedly feeds an AI agent a prompt until completion"',
        image: 'ralph-wiggum-awesomeclaude.png'
    },
    // Slide 37
    {
        type: 'comparison',
        title: 'The future is here—adoption to a new way of thinking is the primary challenge',
        table: {
            headers: ['Old Thinking', 'New Thinking'],
            rows: [
                ['Write code myself', 'Design workflows that write code'],
                ['One-shot prompts', 'Iterative loops until done'],
                ['Static instructions', 'Continuously improved artifacts'],
                ['Single session', 'Parallel agents on worktrees']
            ]
        },
        note: 'The adoption challenge is mindset, not technology.'
    },
    // Slide 38
    {
        type: 'content',
        title: 'Key takeaways: compound efficiency through workflow, context, and parallelization',
        bullets: [
            '1. Claude Code = LLM + filesystem access = general agent',
            '2. Workflows compound—every CLAUDE.md update makes the system smarter',
            '3. Context engineering is the fundamental skill',
            '4. Parallelization via git worktree multiplies efficiency',
            '5. The future is iterative loops that run until completion',
            '6. Adoption is the challenge—the technology is here'
        ]
    },
    // Slide 39
    {
        type: 'resources',
        title: 'Resources for getting started with Claude Code',
        sections: [
            { title: 'Official', items: ['code.claude.com/docs', 'DeepLearning.ai Course'] },
            { title: 'Skills', items: ['github.com/anthropics/skills', 'K-Dense-AI/claude-scientific-skills'] }
        ]
    },
    // Slide 40
    {
        type: 'content',
        title: 'Questions?',
        bullets: [
            'How might this change our team\'s workflows?',
            'What tasks would benefit most from agent automation?',
            'Security considerations for our environment',
            'Skill development for our specific use cases'
        ]
    },
    // Appendix A1
    {
        type: 'table_slide',
        title: 'Claude Code uses only four core tools: Read, Write, Edit, Bash',
        table: {
            headers: ['Tool', 'Purpose'],
            rows: [
                ['Read', 'File contents, images, PDFs'],
                ['Write', 'Create new files'],
                ['Edit', 'String replacement in files'],
                ['Bash', 'Shell command execution']
            ]
        },
        quote: '"Four tools outperform complex tool ecosystems" — Mario Zechner'
    },
    // Appendix A2
    {
        type: 'content_code',
        title: 'MCP servers extend Claude Code with external tool capabilities',
        code: `/plugin install @anthropic-ai/mcp-server-github
/plugin install @anthropic-ai/mcp-server-context7`,
        note: 'Trade-off: Convenience vs. context window overhead'
    },
    // Appendix A3
    {
        type: 'content',
        title: 'Gemini CLI provides 1M token context and a generous free tier',
        bullets: [
            '1 million token context window',
            '60 requests/minute, 1000/day (free)',
            'Deep Google Cloud integration',
            'Lower SWE-bench scores than Claude'
        ],
        note: 'Best for: Google Cloud users, documentation, exploration'
    }
];

// HTML generation functions
function escapeHtml(text) {
    return text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function generateTitleSlideHtml(slide, index) {
    return `<!DOCTYPE html>
<html>
<head>
<style>
html { background: #ffffff; }
body {
    width: 720pt; height: 405pt; margin: 0; padding: 0;
    background: ${COLORS.primary}; font-family: Arial, sans-serif;
    display: flex; flex-direction: column; justify-content: center; align-items: center;
}
h1 { color: ${COLORS.white}; font-size: 36pt; margin: 0 40pt; text-align: center; line-height: 1.3; }
p { color: ${COLORS.secondary}; font-size: 18pt; margin-top: 30pt; text-align: center; }
</style>
</head>
<body>
<h1>${escapeHtml(slide.title)}</h1>
<p>${escapeHtml(slide.subtitle.replace(/\n/g, '<br>'))}</p>
</body>
</html>`;
}

function generateContentSlideHtml(slide, index) {
    let bulletsHtml = '';
    if (slide.bullets) {
        bulletsHtml = '<ul>' + slide.bullets.map(b => `<li>${escapeHtml(b)}</li>`).join('') + '</ul>';
    }
    let noteHtml = slide.note ? `<p class="note">${escapeHtml(slide.note)}</p>` : '';
    let quoteHtml = slide.quote ? `<div class="quote"><p>${escapeHtml(slide.quote)}</p></div>` : '';

    return `<!DOCTYPE html>
<html>
<head>
<style>
html { background: #ffffff; }
body {
    width: 720pt; height: 405pt; margin: 0; padding: 0;
    background: ${COLORS.white}; font-family: Arial, sans-serif;
    display: flex; flex-direction: column;
}
.header { background: ${COLORS.primary}; padding: 15pt 25pt; }
h1 { color: ${COLORS.white}; font-size: 18pt; margin: 0; line-height: 1.3; }
.content { padding: 20pt 30pt; flex: 1; }
ul { color: ${COLORS.text}; font-size: 16pt; margin: 0; padding-left: 25pt; }
li { margin-bottom: 12pt; line-height: 1.4; }
.note { color: ${COLORS.lightText}; font-size: 12pt; font-style: italic; margin-top: 15pt; }
.quote { background: ${COLORS.quoteBg}; padding: 12pt 20pt; margin-top: 15pt; border-left: 4pt solid ${COLORS.accent}; }
.quote p { color: ${COLORS.text}; font-size: 14pt; font-style: italic; margin: 0; }
</style>
</head>
<body>
<div class="header"><h1>${escapeHtml(slide.title)}</h1></div>
<div class="content">
${bulletsHtml}
${quoteHtml}
${noteHtml}
</div>
</body>
</html>`;
}

function generateContentCodeSlideHtml(slide, index) {
    let noteHtml = slide.note ? `<p class="note">${escapeHtml(slide.note)}</p>` : '';
    let quoteHtml = slide.quote ? `<div class="quote"><p>${escapeHtml(slide.quote)}</p></div>` : '';

    return `<!DOCTYPE html>
<html>
<head>
<style>
html { background: #ffffff; }
body {
    width: 720pt; height: 405pt; margin: 0; padding: 0;
    background: ${COLORS.white}; font-family: Arial, sans-serif;
    display: flex; flex-direction: column;
}
.header { background: ${COLORS.primary}; padding: 15pt 25pt; }
h1 { color: ${COLORS.white}; font-size: 18pt; margin: 0; line-height: 1.3; }
.content { padding: 20pt 30pt; flex: 1; display: flex; flex-direction: column; }
.code { background: ${COLORS.codeBg}; padding: 15pt; border-radius: 6pt; flex: 1; }
.code p { font-family: Courier New, monospace; font-size: 11pt; color: ${COLORS.text}; margin: 0; white-space: pre-wrap; line-height: 1.5; }
.note { color: ${COLORS.lightText}; font-size: 12pt; font-style: italic; margin-top: 12pt; }
.quote { background: ${COLORS.quoteBg}; padding: 10pt 15pt; margin-top: 12pt; border-left: 4pt solid ${COLORS.accent}; }
.quote p { color: ${COLORS.text}; font-size: 12pt; font-style: italic; margin: 0; }
</style>
</head>
<body>
<div class="header"><h1>${escapeHtml(slide.title)}</h1></div>
<div class="content">
<div class="code"><p>${escapeHtml(slide.code)}</p></div>
${quoteHtml}
${noteHtml}
</div>
</body>
</html>`;
}

function generateComparisonSlideHtml(slide, index) {
    let noteHtml = slide.note ? `<p class="note">${escapeHtml(slide.note)}</p>` : '';
    let quoteHtml = slide.quote ? `<div class="quote"><p>${escapeHtml(slide.quote)}</p></div>` : '';

    // Generate table placeholder
    return `<!DOCTYPE html>
<html>
<head>
<style>
html { background: #ffffff; }
body {
    width: 720pt; height: 405pt; margin: 0; padding: 0;
    background: ${COLORS.white}; font-family: Arial, sans-serif;
    display: flex; flex-direction: column;
}
.header { background: ${COLORS.primary}; padding: 15pt 25pt; }
h1 { color: ${COLORS.white}; font-size: 18pt; margin: 0; line-height: 1.3; }
.content { padding: 20pt 30pt; flex: 1; display: flex; flex-direction: column; }
.table-area { background: ${COLORS.light}; flex: 1; border-radius: 6pt; }
.note { color: ${COLORS.lightText}; font-size: 12pt; font-style: italic; margin-top: 12pt; }
.quote { background: ${COLORS.quoteBg}; padding: 10pt 15pt; margin-top: 12pt; border-left: 4pt solid ${COLORS.accent}; }
.quote p { color: ${COLORS.text}; font-size: 12pt; font-style: italic; margin: 0; }
</style>
</head>
<body>
<div class="header"><h1>${escapeHtml(slide.title)}</h1></div>
<div class="content">
<div id="table" class="placeholder table-area"></div>
${quoteHtml}
${noteHtml}
</div>
</body>
</html>`;
}

function generateTableSlideHtml(slide, index) {
    let noteHtml = slide.note ? `<p class="note">${escapeHtml(slide.note)}</p>` : '';
    let quoteHtml = slide.quote ? `<div class="quote"><p>${escapeHtml(slide.quote)}</p></div>` : '';

    return `<!DOCTYPE html>
<html>
<head>
<style>
html { background: #ffffff; }
body {
    width: 720pt; height: 405pt; margin: 0; padding: 0;
    background: ${COLORS.white}; font-family: Arial, sans-serif;
    display: flex; flex-direction: column;
}
.header { background: ${COLORS.primary}; padding: 15pt 25pt; }
h1 { color: ${COLORS.white}; font-size: 18pt; margin: 0; line-height: 1.3; }
.content { padding: 20pt 30pt; flex: 1; display: flex; flex-direction: column; }
.table-area { background: ${COLORS.light}; flex: 1; border-radius: 6pt; }
.note { color: ${COLORS.lightText}; font-size: 12pt; font-style: italic; margin-top: 12pt; }
.quote { background: ${COLORS.quoteBg}; padding: 10pt 15pt; margin-top: 12pt; border-left: 4pt solid ${COLORS.accent}; }
.quote p { color: ${COLORS.text}; font-size: 12pt; font-style: italic; margin: 0; }
</style>
</head>
<body>
<div class="header"><h1>${escapeHtml(slide.title)}</h1></div>
<div class="content">
<div id="table" class="placeholder table-area"></div>
${quoteHtml}
${noteHtml}
</div>
</body>
</html>`;
}

function generateContentImageSlideHtml(slide, index) {
    let bulletsHtml = '';
    if (slide.bullets) {
        bulletsHtml = '<ul>' + slide.bullets.map(b => `<li>${escapeHtml(b)}</li>`).join('') + '</ul>';
    }
    let codeHtml = '';
    if (slide.code) {
        codeHtml = `<div class="code"><p>${escapeHtml(slide.code)}</p></div>`;
    }
    let quoteHtml = slide.quote ? `<div class="quote"><p>${escapeHtml(slide.quote)}</p></div>` : '';

    return `<!DOCTYPE html>
<html>
<head>
<style>
html { background: #ffffff; }
body {
    width: 720pt; height: 405pt; margin: 0; padding: 0;
    background: ${COLORS.white}; font-family: Arial, sans-serif;
    display: flex; flex-direction: column;
}
.header { background: ${COLORS.primary}; padding: 15pt 25pt; }
h1 { color: ${COLORS.white}; font-size: 18pt; margin: 0; line-height: 1.3; }
.content { padding: 15pt 25pt; flex: 1; display: flex; gap: 20pt; }
.left { flex: 1; display: flex; flex-direction: column; }
.right { width: 280pt; display: flex; align-items: center; justify-content: center; }
.image-placeholder { background: ${COLORS.light}; width: 100%; height: 100%; border-radius: 6pt; }
ul { color: ${COLORS.text}; font-size: 14pt; margin: 0; padding-left: 20pt; }
li { margin-bottom: 8pt; line-height: 1.3; }
.code { background: ${COLORS.codeBg}; padding: 10pt; border-radius: 6pt; margin-bottom: 10pt; }
.code p { font-family: Courier New, monospace; font-size: 9pt; color: ${COLORS.text}; margin: 0; white-space: pre-wrap; line-height: 1.4; }
.quote { background: ${COLORS.quoteBg}; padding: 8pt 12pt; margin-top: auto; border-left: 3pt solid ${COLORS.accent}; }
.quote p { color: ${COLORS.text}; font-size: 11pt; font-style: italic; margin: 0; }
</style>
</head>
<body>
<div class="header"><h1>${escapeHtml(slide.title)}</h1></div>
<div class="content">
<div class="left">
${codeHtml}
${bulletsHtml}
${quoteHtml}
</div>
<div class="right">
<div id="image" class="placeholder image-placeholder"></div>
</div>
</div>
</body>
</html>`;
}

function generateContentCodeImageSlideHtml(slide, index) {
    return `<!DOCTYPE html>
<html>
<head>
<style>
html { background: #ffffff; }
body {
    width: 720pt; height: 405pt; margin: 0; padding: 0;
    background: ${COLORS.white}; font-family: Arial, sans-serif;
    display: flex; flex-direction: column;
}
.header { background: ${COLORS.primary}; padding: 15pt 25pt; }
h1 { color: ${COLORS.white}; font-size: 18pt; margin: 0; line-height: 1.3; }
.content { padding: 15pt 25pt; flex: 1; display: flex; gap: 20pt; }
.left { flex: 1; display: flex; flex-direction: column; }
.right { width: 280pt; display: flex; align-items: center; justify-content: center; }
.image-placeholder { background: ${COLORS.light}; width: 100%; height: 100%; border-radius: 6pt; }
.code { background: ${COLORS.codeBg}; padding: 12pt; border-radius: 6pt; flex: 1; }
.code p { font-family: Courier New, monospace; font-size: 10pt; color: ${COLORS.text}; margin: 0; white-space: pre-wrap; line-height: 1.4; }
</style>
</head>
<body>
<div class="header"><h1>${escapeHtml(slide.title)}</h1></div>
<div class="content">
<div class="left">
<div class="code"><p>${escapeHtml(slide.code)}</p></div>
</div>
<div class="right">
<div id="image" class="placeholder image-placeholder"></div>
</div>
</div>
</body>
</html>`;
}

function generateTimelineSlideHtml(slide, index) {
    let eventsHtml = slide.events.map((e, i) => `
        <div class="event">
            <div class="date"><p>${escapeHtml(e.date)}</p></div>
            <div class="dot"></div>
            <div class="text"><p>${escapeHtml(e.text)}</p></div>
        </div>
    `).join('');

    return `<!DOCTYPE html>
<html>
<head>
<style>
html { background: #ffffff; }
body {
    width: 720pt; height: 405pt; margin: 0; padding: 0;
    background: ${COLORS.white}; font-family: Arial, sans-serif;
    display: flex; flex-direction: column;
}
.header { background: ${COLORS.primary}; padding: 15pt 25pt; }
h1 { color: ${COLORS.white}; font-size: 18pt; margin: 0; line-height: 1.3; }
.content { padding: 30pt 40pt; flex: 1; display: flex; flex-direction: column; justify-content: space-around; }
.event { display: flex; align-items: center; gap: 15pt; }
.date { width: 120pt; text-align: right; }
.date p { color: ${COLORS.primary}; font-size: 14pt; font-weight: bold; margin: 0; }
.dot { width: 12pt; height: 12pt; background: ${COLORS.accent}; border-radius: 50%; flex-shrink: 0; }
.text p { color: ${COLORS.text}; font-size: 14pt; margin: 0; }
</style>
</head>
<body>
<div class="header"><h1>${escapeHtml(slide.title)}</h1></div>
<div class="content">
${eventsHtml}
</div>
</body>
</html>`;
}

function generateTwoColumnSlideHtml(slide, index) {
    let leftBullets = '<ul>' + slide.leftBullets.map(b => `<li>${escapeHtml(b)}</li>`).join('') + '</ul>';
    let rightBullets = '<ul>' + slide.rightBullets.map(b => `<li>${escapeHtml(b)}</li>`).join('') + '</ul>';

    return `<!DOCTYPE html>
<html>
<head>
<style>
html { background: #ffffff; }
body {
    width: 720pt; height: 405pt; margin: 0; padding: 0;
    background: ${COLORS.white}; font-family: Arial, sans-serif;
    display: flex; flex-direction: column;
}
.header { background: ${COLORS.primary}; padding: 15pt 25pt; }
h1 { color: ${COLORS.white}; font-size: 18pt; margin: 0; line-height: 1.3; }
.content { padding: 20pt 30pt; flex: 1; display: flex; gap: 30pt; }
.column { flex: 1; }
h2 { color: ${COLORS.primary}; font-size: 16pt; margin: 0 0 15pt 0; }
ul { color: ${COLORS.text}; font-size: 14pt; margin: 0; padding-left: 20pt; }
li { margin-bottom: 10pt; line-height: 1.3; }
</style>
</head>
<body>
<div class="header"><h1>${escapeHtml(slide.title)}</h1></div>
<div class="content">
<div class="column">
<h2>${escapeHtml(slide.leftTitle)}</h2>
${leftBullets}
</div>
<div class="column">
<h2>${escapeHtml(slide.rightTitle)}</h2>
${rightBullets}
</div>
</div>
</body>
</html>`;
}

function generateResourcesSlideHtml(slide, index) {
    let sectionsHtml = slide.sections.map(s => `
        <div class="section">
            <h2>${escapeHtml(s.title)}</h2>
            <ul>${s.items.map(i => `<li>${escapeHtml(i)}</li>`).join('')}</ul>
        </div>
    `).join('');

    return `<!DOCTYPE html>
<html>
<head>
<style>
html { background: #ffffff; }
body {
    width: 720pt; height: 405pt; margin: 0; padding: 0;
    background: ${COLORS.white}; font-family: Arial, sans-serif;
    display: flex; flex-direction: column;
}
.header { background: ${COLORS.primary}; padding: 15pt 25pt; }
h1 { color: ${COLORS.white}; font-size: 18pt; margin: 0; line-height: 1.3; }
.content { padding: 25pt 40pt; flex: 1; display: flex; gap: 40pt; }
.section { flex: 1; }
h2 { color: ${COLORS.primary}; font-size: 18pt; margin: 0 0 15pt 0; }
ul { color: ${COLORS.text}; font-size: 14pt; margin: 0; padding-left: 20pt; }
li { margin-bottom: 12pt; line-height: 1.3; }
</style>
</head>
<body>
<div class="header"><h1>${escapeHtml(slide.title)}</h1></div>
<div class="content">
${sectionsHtml}
</div>
</body>
</html>`;
}

function generateSlideHtml(slide, index) {
    switch(slide.type) {
        case 'title': return generateTitleSlideHtml(slide, index);
        case 'content': return generateContentSlideHtml(slide, index);
        case 'content_code': return generateContentCodeSlideHtml(slide, index);
        case 'comparison': return generateComparisonSlideHtml(slide, index);
        case 'table_slide': return generateTableSlideHtml(slide, index);
        case 'content_image': return generateContentImageSlideHtml(slide, index);
        case 'content_code_image': return generateContentCodeImageSlideHtml(slide, index);
        case 'timeline': return generateTimelineSlideHtml(slide, index);
        case 'two_column': return generateTwoColumnSlideHtml(slide, index);
        case 'resources': return generateResourcesSlideHtml(slide, index);
        default: return generateContentSlideHtml(slide, index);
    }
}

async function main() {
    const pptx = new pptxgen();
    pptx.layout = 'LAYOUT_16x9';
    pptx.author = 'Generated with Claude Code';
    pptx.title = 'Claude Code: From Coding to Workflow Design';

    console.log(`Generating ${slides.length} slides...`);

    for (let i = 0; i < slides.length; i++) {
        const slide = slides[i];
        const htmlPath = path.join(WORKSPACE, `slide${i + 1}.html`);

        // Generate HTML
        const html = generateSlideHtml(slide, i);
        fs.writeFileSync(htmlPath, html);

        console.log(`Processing slide ${i + 1}: ${slide.title.substring(0, 50)}...`);

        try {
            const { slide: pptxSlide, placeholders } = await html2pptx(htmlPath, pptx);

            // Add tables where needed
            if ((slide.type === 'comparison' || slide.type === 'table_slide') && slide.table) {
                const tableData = [
                    slide.table.headers.map(h => ({
                        text: h,
                        options: { fill: { color: '3B5265' }, color: 'FFFFFF', bold: true, align: 'center' }
                    })),
                    ...slide.table.rows.map(row =>
                        row.map(cell => ({ text: cell, options: { align: 'left' } }))
                    )
                ];

                if (placeholders.length > 0) {
                    const p = placeholders[0];
                    pptxSlide.addTable(tableData, {
                        x: p.x,
                        y: p.y,
                        w: p.w,
                        h: p.h,
                        border: { pt: 1, color: 'CCCCCC' },
                        fontSize: 12,
                        valign: 'middle'
                    });
                }
            }

            // Add images where needed
            if (slide.image && placeholders.length > 0) {
                const imgPlaceholder = placeholders.find(p => p.id === 'image') || placeholders[0];
                const imgPath = path.join(FIGURES, slide.image);

                if (fs.existsSync(imgPath)) {
                    pptxSlide.addImage({
                        path: imgPath,
                        x: imgPlaceholder.x,
                        y: imgPlaceholder.y,
                        w: imgPlaceholder.w,
                        h: imgPlaceholder.h,
                        sizing: { type: 'contain', w: imgPlaceholder.w, h: imgPlaceholder.h }
                    });
                }
            }
        } catch (err) {
            console.error(`Error on slide ${i + 1}: ${err.message}`);
        }
    }

    const outputPath = '/Users/somite-changheelee/Desktop/04_Presentations/20260114 ClaudeCode/Claude-Code-Presentation.pptx';
    await pptx.writeFile({ fileName: outputPath });
    console.log(`\nPresentation saved to: ${outputPath}`);
}

main().catch(console.error);
