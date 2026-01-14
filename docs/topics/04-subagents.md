# Subagents and Agentic Patterns

## Summary
Subagents are specialized AI agents spawned by a main agent to handle discrete portions of larger tasks. They're a direct solution to context window limitations.

## What Are Subagents?

### Definition
Specialized agents spawned to handle discrete task portions, each receiving its own **fresh context window**.

### Example
Dividing 36 files among 3 subagents with 12 files each - prevents main agent from being overwhelmed by sequential processing.

### Why They Exist
- Context window is finite
- Parallel processing is faster
- Specialized agents can be optimized for specific tasks

## Agentic Patterns Taxonomy

### Context & Memory Patterns
| Pattern | Description |
|---------|-------------|
| Context-Minimization | Keep context lean and relevant |
| Dynamic Context Injection | Load context on-demand |
| Filesystem-Based Agent State | External state storage |

### Feedback Loop Patterns
| Pattern | Description |
|---------|-------------|
| Self-Critique | Agent evaluates own output |
| Reflection Loops | Iterative improvement cycles |
| Spec-as-Test | Use specifications as validation |

### Orchestration Patterns
| Pattern | Description |
|---------|-------------|
| Plan-then-Execute | Separate planning from execution |
| Discrete Phase Separation | Specialized phases with handoffs |
| Tree-of-Thought | Branching reasoning paths |

### Tool Use Patterns
| Pattern | Description |
|---------|-------------|
| CLI-First Skill Design | Prefer command-line tools |
| Code-Over-API | Generate code rather than API calls |

### Security Patterns
| Pattern | Description |
|---------|-------------|
| Deterministic Scanning | Predictable security checks |
| PII Tokenization | Protect sensitive data |
| Egress Lockdown | Restrict outbound network |

## Coordination Mechanisms

### 1. Hierarchical Spawning
- Main agent decomposes tasks
- Spawns subagents
- Merges results

### 2. Message Passing
- Structured outputs between agents
- Queue-based communication

### 3. Shared State Externalization
- Files accessible across agent sessions
- Progress tracking in filesystem

### 4. Discrete Handoffs
- Pass distilled findings, not full context
- Reduces information loss

## Best Practices

1. **Isolation**: Run separate VMs/containers per agent
2. **Structured Communication**: Type-safe, parseable handoffs
3. **Progressive Autonomy**: Unlock capabilities gradually
4. **Human-in-the-Loop**: Approval for high-risk operations
5. **Chain-of-Thought Monitoring**: Catch errant reasoning early
6. **Clear Boundaries**: Explicit tool/capability restrictions

## Key References

- [Awesome Agentic Patterns](https://esc5221.github.io/awesome-agentic-patterns/)
- [Simon Willison: Claude Skills](https://simonwillison.net/2025/Oct/16/claude-skills/)
