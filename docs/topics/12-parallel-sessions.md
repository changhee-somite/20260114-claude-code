# Parallel Sessions with Git Worktree

## Summary

Once workflows are semi-automated with Claude Code, the next efficiency multiplier is parallelization. Git worktree enables running multiple independent Claude Code sessions simultaneously on the same codebase—an unconventional but powerful mode of operation.

## The Three Pillars of Agent-Era Efficiency

```
Workflow Design → Context Engineering → Parallelization
      ↓                   ↓                    ↓
  Define what         Optimize what       Scale by running
  agents do           agents see          multiple agents
```

Each pillar builds on the previous. Parallelization only becomes practical once you trust your workflow and understand context management.

## What is Git Worktree?

Git worktree allows multiple working directories linked to the same repository, each on a different branch. Unlike cloning, worktrees share the same `.git` directory.

### Basic Commands

```bash
# Create a new worktree for a feature branch
git worktree add ../feature-auth feature/auth

# Create worktree with new branch
git worktree add -b feature/api ../feature-api

# List all worktrees
git worktree list

# Remove a worktree when done
git worktree remove ../feature-auth
```

## Parallel Claude Code Sessions

### Setup Pattern

```bash
# Main project directory
cd ~/projects/myapp

# Create parallel worktrees
git worktree add ../myapp-auth feature/auth
git worktree add ../myapp-api feature/api
git worktree add ../myapp-tests refactor/tests

# In separate terminals, start Claude Code in each
cd ../myapp-auth && claude
cd ../myapp-api && claude
cd ../myapp-tests && claude
```

### Why This Works

| Single Session | Parallel Sessions |
|----------------|-------------------|
| Sequential task completion | Simultaneous progress on independent tasks |
| One context window | Multiple fresh context windows |
| Blocking on long operations | Non-blocking workflow |
| Context accumulates over time | Each session starts fresh |

## Practical Patterns

### 1. Feature Branch Parallelization

Work on multiple features simultaneously:
- Session 1: Implementing authentication
- Session 2: Building API endpoints
- Session 3: Writing integration tests

### 2. Research + Implementation Split

Run a research session while implementing:
- Session 1: Exploring codebase, reading documentation
- Session 2: Making actual code changes based on findings

### 3. Testing in Parallel

Run tests while continuing development:
- Session 1: Active development
- Session 2: Running and fixing failing tests
- Session 3: Code review and refactoring

### 4. Multi-Module Refactoring

Large refactoring across independent modules:
- Session 1: Refactoring Module A
- Session 2: Refactoring Module B
- Merge when both complete

## Best Practices

### Do

- **Keep branches independent**: Avoid merge conflicts by working on orthogonal tasks
- **Use descriptive worktree names**: Match the task or branch name
- **Clean up when done**: Remove worktrees to avoid confusion
- **Document your setup**: Note which worktree is doing what

### Avoid

- **Conflicting file edits**: Two sessions editing the same files will conflict
- **Shared state assumptions**: Each session is isolated
- **Too many sessions**: Cognitive overhead; 2-4 is practical
- **Long-lived worktrees**: Treat as temporary workspaces

## When to Parallelize

### Good Candidates

- Independent feature development
- Test writing while features are in progress
- Documentation alongside implementation
- Exploration/research sessions
- CI/CD-like local validation

### Poor Candidates

- Tightly coupled changes
- Same file/module modifications
- Sequential dependencies (A must complete before B)
- Debugging a single issue

## Merging Parallel Work

After completing parallel sessions:

```bash
# In main worktree
cd ~/projects/myapp

# Merge completed feature branches
git merge feature/auth
git merge feature/api
git merge refactor/tests

# Clean up worktrees
git worktree remove ../myapp-auth
git worktree remove ../myapp-api
git worktree remove ../myapp-tests
```

## Resource Considerations

### System Resources

Each Claude Code session uses:
- API quota (shared across sessions)
- Local memory and CPU for the terminal
- Network bandwidth

### API Usage

- Multiple sessions consume quota faster
- Monitor with `/status` in each session
- Consider subscription tier for heavy parallel use

## The Mindset Shift

Traditional development: one developer, one workspace, sequential tasks.

Agent-era development: one developer supervising multiple agents, parallel progress.

This is "unconventional" because:
1. We're used to single-focus work
2. Context switching is usually costly (but agents maintain their own context)
3. Coordination seems complex (but git handles merging)

Once you trust the workflow, multiplying it becomes the obvious next step.

## Key References

- [Git Worktree Documentation](https://git-scm.com/docs/git-worktree)
- [Using Git Worktrees for Parallel Development](https://opensource.com/article/21/4/git-worktree)
