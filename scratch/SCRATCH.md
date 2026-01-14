# Rough organization I have in mind

## Big view

1. What is Claude Code

* When was it launched
* When I personally started evaluating: 2025-07-01.


* I believe it is a  general agent for computer automation. See this blog post: https://simonwillison.net/2025/Oct/16/claude-skills/#claude-as-a-general-agent
  - Just an LLM that got permission to access a file system
* I think context engineering -- essentially that we would live by the constraint of context window is paramount
  - Because of the O(N^2) architecture of transformer architecture
  - Then it becomes important to efficiently put relevant context to LLM to do the task - all the Skills, Subagents are derived from this fundamental (short-term) constraint.

* Emphasis that this is not really coding, but how you establish workflows
  - article of this: https://x.com/eyad_khrais/article/2010076957938188661
  - article also this: https://mike.tech/blog/death-of-software-development

# Somethings that I need clarification

* What is "Harness"
* How do you define "Context Window"
 

# Things to cover

* Boris Cherny, the developer of Claude Code how he uses it: https://x.com/bcherny/status/2007179832300581177?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E2007179832300581177%7Ctwgr%5Ef73f8b5afa6782e27efb402024db75e79dd6b858%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fbawi.org%2Fboard%2Fread.cgi%3Fbid%3D3524aid%3D1794279p%3D24

* Context engineering
  - https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
  - 

* Permissions, and --dangerously-skip-permissions option
  - The article in the following link was how I got the sense of it: https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/
  - But we need to check how it evolved, virtualization options etc.

* Subagent
  - reference: https://esc5221.github.io/awesome-agentic-patterns/

* Skills
  - https://simonwillison.net/2025/Oct/16/claude-skills/
  - reference: https://github.com/anthropics/skills?tab=readme-ov-file
  - reference (for bio): https://github.com/K-Dense-AI/claude-scientific-skills
  - I heard about the Skill learning with the following starting point: https://www.youtube.com/watch?v=3EHnp-SH4O8

* Tutorials
  - https://www.youtube.com/playlist?list=PL4cUxeGkcC9g4YJeBqChhFJwKQ9TRiivY
  - https://www.deeplearning.ai/short-courses/claude-code-a-highly-agentic-coding-assistant/

* Workflow
  - https://awesomeclaude.ai/ralph-wiggum
  - article post: https://mike.tech/blog/death-of-software-development


* Small things that gives further context
  - How to arrange the /statusline
 

* Alternatives to Claude Code
  - https://opencode.ai/
  - https://github.com/code-yeongyu/oh-my-opencode


