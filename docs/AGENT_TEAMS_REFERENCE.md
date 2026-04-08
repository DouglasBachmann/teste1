# Agent Teams Reference Guide

**Version:** 1.0  
**Last Updated:** 2026-04-08  
**Status:** Experimental Feature

## Table of Contents

1. [Quick Start](#quick-start)
2. [When to Use Agent Teams](#when-to-use-agent-teams)
3. [Architecture Overview](#architecture-overview)
4. [Team Configuration](#team-configuration)
5. [Controlling Teams](#controlling-teams)
6. [Best Practices](#best-practices)
7. [Common Use Cases](#common-use-cases)
8. [Troubleshooting](#troubleshooting)
9. [Token Cost Considerations](#token-cost-considerations)
10. [Limitations](#limitations)

---

## Quick Start

### Enable Agent Teams

Add to your `.claude/settings.local.json`:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

Or set the environment variable:
```bash
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

**Requirements:**
- Claude Code v2.1.32 or later (`claude --version`)

### Create Your First Team

Tell Claude Code to create a team with a clear task and desired structure:

```
Create an agent team to explore this CLI tool design from different angles: 
one teammate on UX, one on technical architecture, one playing devil's advocate.
```

Claude will:
1. Create the team
2. Spawn teammates with appropriate roles
3. Establish a shared task list
4. Coordinate work automatically

---

## When to Use Agent Teams

### ✅ Best Use Cases

Agent teams excel at **parallel exploration** where teammates need to work independently and share findings:

- **Research and Review**: Multiple teammates investigate different aspects simultaneously
- **New Modules or Features**: Each teammate owns a separate piece without dependency conflicts
- **Debugging with Competing Hypotheses**: Teammates test different theories in parallel
- **Cross-Layer Coordination**: Frontend, backend, and tests owned by different teammates
- **Code Review**: Multiple reviewers apply different lenses (security, performance, tests)

### ❌ When NOT to Use

Avoid agent teams for:

- **Sequential Tasks**: Dependencies require one task to finish before the next starts
- **Same-File Edits**: Multiple teammates editing the same file causes overwrites
- **Quick Focused Tasks**: Single session is more cost-efficient
- **High Coordination Needs**: Too many dependencies between teammates

### Agent Teams vs Subagents

| Aspect | Agent Teams | Subagents |
|--------|-----------|-----------|
| **Context** | Own context window; fully independent | Own context window; results return to caller |
| **Communication** | Teammates message each other directly | Report results back to main agent only |
| **Coordination** | Shared task list with self-coordination | Main agent manages all work |
| **Best For** | Complex work requiring collaboration | Focused tasks where only the result matters |
| **Token Cost** | Higher (each teammate is separate Claude) | Lower (results summarized back) |

---

## Architecture Overview

### Team Components

```
┌─────────────────────────────────────────────────────┐
│                    Team Lead                        │
│  (Main Claude Code session coordinating work)       │
└──────────────┬────────────────────────────────────┬─┘
               │                                    │
        ┌──────▼─────────┐              ┌──────────▼──────────┐
        │  Shared Task   │              │  Messaging System   │
        │     List       │              │    (Mailbox)        │
        └────────────────┘              └─────────────────────┘
               ▲                               ▲
        ┌──────┴───────┬──────────┬───────────┴──────┐
        │              │          │                  │
    ┌───▼───┐     ┌───▼───┐  ┌──▼────┐          ┌──▼────┐
    │Teammate│     │Teammate│  │Teammate│        │Teammate│
    │   #1   │     │   #2   │  │  #3   │  ...   │  #N    │
    └────────┘     └────────┘  └───────┘         └────────┘
```

### Key Components

| Component | Role | Storage |
|-----------|------|---------|
| **Team Lead** | Creates team, spawns teammates, coordinates work | Session context |
| **Teammates** | Separate Claude Code instances working on assigned tasks | Own context windows |
| **Task List** | Shared work items teammates claim and complete | `~/.claude/tasks/{team-name}/` |
| **Team Config** | Runtime state (session IDs, pane IDs, member info) | `~/.claude/teams/{team-name}/config.json` |
| **Mailbox** | Messages between agents (automatic delivery) | Ephemeral during session |

### Data Flow

1. **Task Creation**: Lead creates tasks and adds to shared task list
2. **Task Claiming**: Teammates automatically claim available, unblocked tasks
3. **Messaging**: Teammates send/receive messages directly (lead doesn't relay)
4. **Status Updates**: Task completion triggers dependency resolution
5. **Idle Notification**: Teammates auto-notify lead when finished

---

## Team Configuration

### Display Modes

**In-Process (Default)**
- All teammates run in main terminal
- Use `Shift+Down` to cycle between teammates
- Type to send messages
- Works in any terminal

**Split Panes**
- Each teammate gets its own pane (requires tmux or iTerm2)
- See everyone's output simultaneously
- Click into any pane to interact directly
- Better for visual coordination

### Selecting Display Mode

**Global configuration** (`~/.claude.json`):
```json
{
  "teammateMode": "in-process"  // or "tmux" or "auto"
}
```

**Per-session flag**:
```bash
claude --teammate-mode in-process
```

### Split Pane Requirements

**tmux**:
```bash
# Install via package manager
brew install tmux  # macOS
apt install tmux   # Ubuntu/Debian
```

**iTerm2**:
1. Install `it2` CLI: https://github.com/mkusaka/it2
2. Enable Python API: iTerm2 → Settings → General → Magic → Enable Python API

---

## Controlling Teams

### Task Management

#### Creating Tasks
Lead creates tasks automatically during team setup or on-demand:

```
Create 5 tasks for implementing the authentication module:
- Database schema
- API endpoints
- Token validation
- Error handling
- Tests
```

#### Task Structure
- **Name**: Clear, descriptive title
- **Description**: Context and requirements
- **Dependencies**: Tasks that must complete first
- **Status**: pending → in_progress → completed

#### Dependency System
```
Task: Write API endpoints
├─ Depends on: Database schema (must complete first)
│
Task: Write tests
└─ Depends on: API endpoints (must complete first)
```

Blocked tasks (with unmet dependencies) automatically unblock when dependencies complete.

### Assigning Work

**Lead Assigns Explicitly**:
```
Assign the "database schema" task to the backend teammate
```

**Self-Claiming** (Automatic):
After finishing a task, teammate automatically picks up the next unassigned, unblocked task.

### Directing Teammates

#### Direct Messaging
```
# In-process mode
Shift+Down          # Cycle to teammate
type message        # Send message
Enter              # View their session
Escape             # Return to lead
```

```
# Split panes
Click teammate pane → type message
```

#### Changing Instructions
```
Tell the security teammate to focus on JWT token handling specifically
```

#### Redirecting Approach
```
The database implementation is taking too long. 
Ask the database teammate to pause and sync with the lead first.
```

### Plan Approval Workflow

For complex/risky tasks, require teammates to plan before implementing:

```
Spawn an architect teammate to refactor authentication.
Require plan approval before they make any changes.
```

**Workflow**:
1. Teammate works in read-only plan mode
2. Finishes planning
3. Sends plan approval request to lead
4. Lead reviews and approves or rejects
5. If rejected: teammate revises and resubmits
6. If approved: teammate exits plan mode and implements

**Lead Decision Criteria**:
```
Only approve plans that include:
- At least 80% test coverage
- Security review of token handling
- No breaking changes to the API
```

### Shutdown and Cleanup

#### Shutting Down Individual Teammate
```
Ask the research teammate to shut down
```

Teammate can approve (graceful exit) or reject with explanation.

#### Team Cleanup
```
Clean up the team
```

**Important**: Always use the lead to clean up. Teammates running cleanup may leave resources in inconsistent state.

---

## Best Practices

### 1. Give Teammates Enough Context

Teammates don't inherit the lead's conversation history. Include task-specific details:

```
Spawn a security reviewer teammate with the prompt: 
"Review the authentication module at src/auth/ for security vulnerabilities. 
Focus on token handling (JWT in httpOnly cookies), session management, and 
input validation. Report any issues with severity ratings."
```

Include in spawn prompt:
- Specific file/directory paths
- Architecture context
- Constraints or requirements
- Desired output format

### 2. Choose Appropriate Team Size

| Team Size | Best For | Notes |
|-----------|----------|-------|
| **3-5** | Most workflows | Balances parallel work with coordination |
| **1-2** | Small tasks | Consider using single session instead |
| **6+** | Very large projects | Token costs scale linearly; monitor overhead |

**Guideline**: Aim for 5-6 tasks per teammate to keep everyone productive without context switching.

### 3. Size Tasks Appropriately

**Too Small** → Coordination overhead exceeds benefit  
**Too Large** → Teammates work too long without check-ins  
**Just Right** → Self-contained units with clear deliverables

Examples of well-sized tasks:
- Implement one function
- Write a test file
- Review one aspect of code
- Investigate one hypothesis

### 4. Avoid File Conflicts

❌ **Bad**: Two teammates editing `src/auth.js`  
✅ **Good**: Teammate A owns `src/auth/tokens.js`, Teammate B owns `src/auth/sessions.js`

Break work so each teammate owns distinct files.

### 5. Start with Research/Review

If new to agent teams, start with low-coordination tasks:
- ✅ Parallel code review (different lenses)
- ✅ Research (different sources/approaches)
- ✅ Bug investigation (different hypotheses)
- ❌ Parallel implementation (potential conflicts)

### 6. Monitor and Steer

Don't let teams run unattended too long:

```
# Check progress regularly
Check in on team progress and let me know what each teammate is working on

# Redirect when needed
The API design approach isn't working. 
Ask the API teammate to pivot and try a simpler approach.
```

### 7. Use CLAUDE.md for Team Context

All teammates read `CLAUDE.md` from working directory automatically:

```markdown
# Project Guidelines for Agent Teams

## Team Roles
- **Backend**: src/backend/
- **Frontend**: src/frontend/
- **DevOps**: infrastructure/

## Code Standards
- Use TypeScript strict mode
- Minimum 80% test coverage
- Security review for auth changes

## File Ownership
- Backend team: src/backend/**
- Frontend team: src/frontend/**
```

### 8. Handle Dependencies Carefully

**Explicitly define task dependencies**:

```
Create tasks in this order:
1. Database schema (no dependencies)
2. API endpoints (depends on: Database schema)
3. Frontend integration (depends on: API endpoints)
4. Tests (depends on: API endpoints)
```

Lead manages dependency resolution automatically.

### 9. Prevent Idle Waiting

```
Wait for your teammates to complete their tasks before proceeding
```

Leads sometimes start implementing instead of delegating. Remind them to wait for teammates.

### 10. Enforce Quality with Hooks

Use hooks to gate work at team boundaries:

```json
{
  "hooks": {
    "TaskCompleted": [{
      "matcher": "",
      "hooks": [{
        "type": "prompt",
        "prompt": "Verify this task was completed correctly and meets quality standards"
      }]
    }]
  }
}
```

Available hooks:
- `TeammateIdle`: Before teammate goes idle
- `TaskCreated`: When task is created
- `TaskCompleted`: When task marked complete

---

## Common Use Cases

### 1. Parallel Code Review

**Prompt**:
```
Create an agent team to review PR #142. Spawn three reviewers:
- One focused on security implications
- One checking performance impact
- One validating test coverage

Have each apply their lens and report findings.
```

**Key Points**:
- Each reviewer uses distinct criteria (no overlap)
- Lead synthesizes findings after all finish
- Task: Review specific file sections (not same file)

### 2. Competing Hypotheses Debugging

**Prompt**:
```
Users report the app exits after one message instead of staying connected.
Spawn 5 teammates to investigate different hypotheses. Have them:
1. Each test a different theory (connection pool, memory leak, socket handling, etc.)
2. Message each other to try to disprove each other's theories
3. Update the findings doc with consensus

Make it a scientific debate where they challenge each other.
```

**Key Points**:
- Multiple independent investigators find better root cause
- Debate structure prevents anchoring bias
- Document findings as they converge

### 3. New Module Implementation

**Prompt**:
```
Create an agent team to build the search module. Spawn 3 teammates:
- Database teammate: index schema, query optimization
- API teammate: endpoint design, validation
- Tests teammate: coverage, edge cases

Each task should be completed by the assigned teammate.
```

**Key Points**:
- Clear separation: each owns different files
- Tasks depend on database → API → tests order
- Minimal cross-file editing

### 4. Feature Design Exploration

**Prompt**:
```
Design a CLI tool to track TODO comments in codebases.
Create an agent team from three angles:
- UX/CLI design perspective
- Technical architecture perspective
- Devil's advocate (questioning assumptions)

Have them explore, share ideas, and challenge each other.
```

**Key Points**:
- Perfect for early design phase
- Non-code work (no file conflicts)
- Diverse perspectives improve design

### 5. Cross-Layer Refactoring

**Prompt**:
```
Refactor authentication to use a new token strategy.
Spawn 3 teammates:
- Auth service teammate: core logic
- Frontend teammate: login/logout flows
- Backend middleware teammate: request validation

Coordinate changes across layers.
```

**Key Points**:
- Each owns different layer
- API contract is the coordination point
- Tests should catch integration issues

---

## Troubleshooting

### Teammates Not Appearing

**In in-process mode**:
```
# Teammates may already be running but not visible
Shift+Down  # Cycle through active teammates
```

**In split-pane mode**:
```bash
# Verify tmux is installed
which tmux

# List active sessions
tmux ls
```

**Task too simple**:
Claude may not spawn teammates if the task doesn't warrant parallel work. Request explicitly:
```
Create a team with 3 teammates to work on this refactoring
```

### Too Many Permission Prompts

Teammate permissions bubble up to lead. Pre-approve common operations:

```json
{
  "permissions": {
    "allow": [
      "Bash(npm:*)",
      "Bash(git:*)",
      "Edit(src/**)",
      "Write(tests/**)"
    ]
  }
}
```

### Teammates Stopping on Errors

Teammates may stop after encountering errors. Check their status:

```
Shift+Down  # Cycle to teammate
# Review output and provide additional instructions
```

Or spawn replacement:
```
Spawn a replacement database teammate to continue the work
```

### Lead Shutting Down Too Early

```
Keep working on this. Wait for your teammates to complete their tasks.
```

### Task Status Appears Stuck

Sometimes teammates fail to mark tasks as completed:

```
Tell the teammate to mark the current task as complete
```

Or check task status manually and update it.

### Orphaned tmux Sessions

```bash
# List sessions
tmux ls

# Kill session
tmux kill-session -t <session-name>
```

### Session Resumption Issues

⚠️ **Known Limitation**: `/resume` and `/rewind` don't restore in-process teammates.

After resuming, spawn new teammates:
```
Spawn 3 new teammates to continue the refactoring work
```

---

## Token Cost Considerations

### Cost Structure

- **Each teammate = separate Claude instance** with its own context window
- **Token usage scales linearly** with number of active teammates
- **Lead + 3 teammates** ≈ 4x token cost of single session

### When Extra Tokens Pay Off

✅ **Good ROI**:
- Research/review (findings are valuable)
- Debugging competing hypotheses (root cause saves significant time)
- New feature development (parallel work saves calendar time)
- Code review (multiple perspectives catch more issues)

❌ **Poor ROI**:
- Routine single-task work
- Sequential dependencies
- Quick fixes

### Cost Optimization

1. **Right-size team**: 3-5 teammates for most tasks (not 10)
2. **Split work thoughtfully**: 5-6 tasks per teammate keeps efficiency high
3. **Monitor progress**: redirect teammates who aren't contributing
4. **Use subagents** for smaller delegated work (lower token cost)
5. **Set appropriate team size** based on complexity

---

## Limitations

⚠️ **Agent teams are experimental**. Current limitations:

### Session Management
- ❌ No session resumption for in-process teammates (`/resume`, `/rewind` don't restore teammates)
- ✅ Split-pane teammates may restore (depends on tmux)
- **Workaround**: Spawn new teammates after resuming

### Task Coordination
- ❌ Task status can lag (teammates don't always mark tasks complete)
- **Workaround**: Check task status manually and update if needed
- ✅ Dependencies are managed automatically

### Shutdown Behavior
- ❌ Shutdown can be slow (teammates finish current request first)
- ✅ Graceful shutdown is supported

### Team Constraints
- ❌ One team per session (can't have multiple teams in one lead)
- ❌ No nested teams (teammates can't spawn their own teams)
- ❌ Lead is fixed (can't promote teammate or transfer leadership)
- **Workaround**: Clean up team and start new one if needed

### Permissions
- ❌ Teammates start with lead's permission mode
- ✅ Can change individual teammate modes after spawning
- ❌ Can't set per-teammate modes at spawn time

### Display Modes
- ✅ In-process mode works in any terminal
- ❌ Split panes require tmux or iTerm2
- ❌ Not supported in VS Code integrated terminal, Windows Terminal, Ghostty

### CLAUDE.md
- ✅ Works normally - teammates read from their working directory
- ✅ Use to provide team-wide guidance

---

## Reference: Key Commands

### Team Creation
```
Create an agent team to [task description]
Spawn [N] teammates [with roles/attributes]
```

### Task Management
```
Create [N] tasks for [work]
Assign [task] to [teammate]
Mark [task] as complete
Update task dependencies
```

### Teammate Interaction
```
Tell [teammate] to [instruction]
Ask [teammate] to [request]
Sync with [teammate] about [topic]
```

### Team Control
```
Wait for teammates to finish
Have teammates message each other about [topic]
Ask [teammate] to shut down
Clean up the team
```

---

## Further Reading

- **Official Docs**: https://code.claude.com/docs/en/agent-teams
- **Subagents**: https://code.claude.com/docs/en/sub-agents
- **Permissions**: https://code.claude.com/docs/en/permissions
- **Git Worktrees**: https://code.claude.com/docs/en/common-workflows#run-parallel-claude-code-sessions

---

**Last Updated**: 2026-04-08  
**Version**: 1.0  
**Maintained By**: Development Team
