# Agent Teams: Architecture Patterns & Advanced Techniques

Advanced patterns and architectural approaches for building highly effective agent teams.

## Table of Contents

1. [Team Composition Patterns](#team-composition-patterns)
2. [Communication Patterns](#communication-patterns)
3. [Task Coordination Patterns](#task-coordination-patterns)
4. [Work Division Strategies](#work-division-strategies)
5. [Quality Gates & Verification](#quality-gates--verification)
6. [Advanced Use Cases](#advanced-use-cases)
7. [Performance Optimization](#performance-optimization)

---

## Team Composition Patterns

### Pattern 1: Specialist Teams

**Best For**: Tasks requiring deep expertise in specific areas

**Structure**:
```
Lead
├── Database Specialist
├── API Specialist
└── Frontend Specialist
```

**Characteristics**:
- Each teammate has focused expertise
- Minimal overlap in responsibilities
- Clear file/module ownership
- Low coordination overhead

**When to Use**:
- Implementing new features
- Building new modules
- Cross-layer refactoring

**Example**: Building an e-commerce checkout module
- **Payment Specialist**: Payment processing, transaction handling
- **Inventory Specialist**: Stock management, reservations
- **UI Specialist**: Checkout flow, user experience

### Pattern 2: Reviewer Teams

**Best For**: Reviews requiring different perspectives

**Structure**:
```
Lead (Synthesis)
├── Security Reviewer
├── Performance Reviewer
├── Quality Reviewer
└── Business Logic Reviewer
```

**Characteristics**:
- Each teammate applies different lens
- No file ownership conflicts
- Findings are synthesized by lead
- Parallel review reduces time

**When to Use**:
- Code reviews
- Design reviews
- Architecture reviews
- Security audits

**Example**: Multi-perspective code review
- Each reviewer gets same PR
- Each applies their specific criteria
- Lead consolidates findings

### Pattern 3: Hypothesis Teams

**Best For**: Debugging/investigation with uncertain root cause

**Structure**:
```
Lead (Debate Moderator)
├── Hypothesis 1 Investigator
├── Hypothesis 2 Investigator
├── Hypothesis 3 Investigator
├── Hypothesis 4 Investigator
└── Consensus Builder
```

**Characteristics**:
- Each teammate tests different theory
- Teammates challenge each other
- Debate format accelerates convergence
- Lead synthesizes consensus

**When to Use**:
- Root cause analysis
- Performance investigations
- Behavior anomalies
- System debugging

**Example**: Investigating intermittent API timeouts
- **Connection Pool Theory**: Check pool exhaustion
- **Database Theory**: Check slow queries
- **Network Theory**: Check latency and timeouts
- **Application Theory**: Check code hotspots
- **Infrastructure Theory**: Check resource availability

### Pattern 4: Hierarchical Teams (Advanced)

**Best For**: Large projects with multiple sub-teams

**Structure**:
```
Lead (Project Manager)
├── Backend Sub-Lead
│   ├── Database Specialist
│   └── API Specialist
├── Frontend Sub-Lead
│   ├── UI Component Specialist
│   └── State Management Specialist
└── DevOps Lead
    └── Infrastructure Specialist
```

**Characteristics**:
- Each sub-lead coordinates their area
- Reduces direct coordination burden
- Better for large, complex projects
- Requires more setup

**When to Use**:
- Large features with multiple components
- Organization with multiple teams
- Complex projects with many dependencies

**Coordination Model**:
- Lead manages sub-leads
- Sub-leads manage their specialists
- Specialists focus on implementation
- Sub-leads handle cross-team sync

### Pattern 5: Iterative Review Cycle

**Best For**: Incremental development with feedback loops

**Structure**:
```
Iteration 1:
- Architect designs solution
- Reviewers critique design
- Lead collects feedback

Iteration 2:
- Implementer builds from feedback
- Reviewers test implementation
- Tester validates quality

Iteration 3:
- Optimizer refines performance
- Final reviewers approve
- Lead synthesizes results
```

**Characteristics**:
- Multiple rounds of reviews
- Feedback drives iterations
- Quality increases each cycle
- Higher token cost but better results

**When to Use**:
- Critical components
- Novel solutions
- High-quality requirements
- Complex architectures

---

## Communication Patterns

### Pattern: Information Hub

**Purpose**: One teammate acts as central coordinator/synthesizer

```
Configuration:
- Information Hub: Receives all updates
- Specialist 1: Works, reports to hub
- Specialist 2: Works, reports to hub
- Specialist 3: Works, reports to hub

Hub responsibilities:
- Collect findings
- Identify conflicts
- Request clarifications
- Build consensus document
```

**When to Use**:
- Large teams (5+ members)
- Complex integration requirements
- Need for real-time synchronization

**Prompt Direction**:
```
Designate the Architect teammate as the information hub.
All other teammates should keep the hub informed of progress.
The hub should identify conflicts and sync findings.
```

### Pattern: Bidirectional Sync

**Purpose**: Teammates pair up for deep coordination

```
Configuration:
- Frontend + API teammates (sync points)
- Backend + Database teammates (sync points)
- Each pair meets at specific milestones
```

**When to Use**:
- Tasks with tight dependencies
- API contracts need alignment
- Performance depends on coordination

**Prompt Direction**:
```
After implementing the database schema, the Database teammate should 
sync with the API teammate on:
- Endpoint design
- Query optimization
- Error handling strategy

After the sync, API teammate implements endpoints.
```

### Pattern: Broadcast + Summarize

**Purpose**: Share information with all, then consolidate

```
Configuration:
- Specialist 1: Broadcasts findings
- Specialist 2: Broadcasts findings
- Specialist 3: Broadcasts findings
- Lead: Summarizes into coherent output
```

**When to Use**:
- Review teams (all need context of others' findings)
- Research teams (all need to know what others discovered)
- Investigation teams (consensus requires all data)

**Prompt Direction**:
```
After each teammate completes their analysis:
1. Broadcast your findings to all other teammates
2. Review what others found
3. Lead: Synthesize all findings into a final report

This ensures everyone knows the full picture before concluding.
```

### Pattern: Private Channels

**Purpose**: Subgroups communicate separately from main team

```
Configuration:
- Security group: Communicates privately
- Performance group: Communicates privately
- Lead: Integrates both perspectives
```

**When to Use**:
- Competing priorities
- Contradictory requirements
- Need to preserve objectivity

**Prompt Direction**:
```
Security-focused reviewers should discuss and align their findings.
Performance-focused reviewers should discuss their findings.
Lead: Integrate both perspectives without favoring one side.
```

---

## Task Coordination Patterns

### Pattern: Dependency Chain

**Structure**:
```
Task 1: Design (Phase 1)
  ↓ (depends on)
Task 2: Implementation (Phase 1)
  ↓ (depends on)
Task 3: Testing (Phase 1)
  ↓ (depends on)
Task 4: Deployment (Phase 1)
```

**Characteristics**:
- Clear sequential flow
- Each task unblocks the next
- Long dependency chain

**When to Use**:
- Waterfall-style sequential work
- Strong temporal dependencies

**Anti-Pattern Alert**: ⚠️ This defeats the purpose of agent teams. Use for truly sequential work only.

### Pattern: Diamond Dependency

**Structure**:
```
        Task 1: Requirements
       /                    \
      /                      \
  Task 2: Backend     Task 3: Frontend
      \                      /
       \                    /
    Task 4: Integration Tests
```

**Characteristics**:
- Parallel work in middle
- Converges at end
- Good parallelism

**When to Use**:
- Features with frontend + backend
- Work that can be done in parallel initially

**Implementation**:
```
Spawn 3 teammates:
- Requirements teammate: Document requirements
- Backend teammate: Implement backend (depends on requirements)
- Frontend teammate: Implement frontend (depends on requirements)
- Once both done, Integration tester verifies they work together
```

### Pattern: Matrix Organization

**Structure**:
```
         Task 1  Task 2  Task 3  Task 4
Teammate 1   X       X       
Teammate 2           X       X
Teammate 3       X       X       X
Teammate 4               X       X
```

**Characteristics**:
- Each teammate touches multiple tasks
- Each task involves multiple teammates
- High coordination complexity
- Only for experienced teams

**When to Use**:
- Large, complex projects
- Shared concerns across tasks
- Deep expertise sharing needed

**Warning**: This pattern has high coordination overhead. Use only when necessary.

### Pattern: Kanban-Style (Open Tasks)

**Structure**:
```
Pending Tasks:
- Task 1 (unassigned)
- Task 2 (unassigned)
- Task 3 (unassigned)
- Task 4 (unassigned)
- ...

Teammates self-claim and work through tasks in order
```

**Characteristics**:
- Flexible task assignment
- Teammates pull work as needed
- Natural load balancing
- Best for similar-sized tasks

**When to Use**:
- Tasks are independent
- Tasks are similar complexity
- Parallel implementation

**Implementation**:
```
Create 8-10 tasks of similar size and complexity.
Tell teammates: "Work through the task list in order.
Claim the next available task when you finish."

Lead monitors progress and reassigns if someone gets stuck.
```

### Pattern: Work Streaming

**Structure**:
```
Input Queue → Teammate 1 → Teammate 2 → Teammate 3 → Output Queue
```

**Characteristics**:
- Assembly line style
- Each teammate specializes in one transformation
- Continuous flow of work
- Bottleneck at slowest stage

**When to Use**:
- Repetitive transformation work
- Clear handoff points
- High-volume processing

**Example**: Code refactoring pipeline
- **Teammate 1**: Identify code sections needing refactoring
- **Teammate 2**: Apply refactoring transformations
- **Teammate 3**: Write tests for refactored code
- **Lead**: Verify and approve

---

## Work Division Strategies

### Strategy 1: By Module/Component

**Division**:
```
Frontend Module → Frontend Teammate
Backend Module → Backend Teammate
Database Layer → Database Teammate
DevOps → DevOps Teammate
```

**Pros**:
- Clear ownership
- Minimal conflicts
- Specialization advantage

**Cons**:
- Integration challenges
- Potential bottlenecks
- Requires good API contracts

### Strategy 2: By Concern/Aspect

**Division**:
```
Functionality → Functionality Teammates
Security → Security Specialists
Performance → Performance Specialists
Testing → QA Specialists
```

**Pros**:
- Deep expertise per concern
- Parallel review/audit
- Different perspectives

**Cons**:
- High coordination needs
- Potential duplication
- Less suitable for implementation

### Strategy 3: By User Story/Feature

**Division**:
```
Story 1: User signup → Team A (full stack)
Story 2: User login → Team B (full stack)
Story 3: Password reset → Team C (full stack)
```

**Pros**:
- Clear deliverables
- Full ownership
- Easier prioritization

**Cons**:
- Less specialization
- Potential code duplication
- Integration challenges

### Strategy 4: By Risk/Complexity

**Division**:
```
High-Risk Core Logic → Expert Teammate
Standard Implementation → Mid-level Teammate
Infrastructure/Setup → Operational Teammate
Testing/QA → Quality Specialist
```

**Pros**:
- Experts handle complex parts
- Risk mitigation
- Clear expertise matching

**Cons**:
- Potential bottleneck at experts
- Difficult to balance load

### Strategy 5: By Skill Level

**Division**:
```
Architectural decisions → Architects
Core implementation → Senior engineers
Testing & validation → Mid-level engineers
Documentation → Anyone who finishes early
```

**Pros**:
- Optimal skill utilization
- Mentoring opportunities
- Efficient work distribution

**Cons**:
- Requires skill assessment
- May underutilize some teammates

---

## Quality Gates & Verification

### Pattern: Checkpoint Approval

**Implementation**:
```
Checkpoint 1: Design approval
- Teammates present design
- Lead reviews and approves
- Proceed to implementation

Checkpoint 2: Implementation review
- Teammates demo features
- Code review by lead
- Approve or request changes

Checkpoint 3: Testing validation
- QA verifies all tests pass
- Performance targets met
- Approve or request fixes
```

**Trigger Points**:
```
Tell teammates: "After completing your design document, 
wait for checkpoint approval before implementing."
```

### Pattern: Hook-Based Quality Gates

**Using TeammateIdle Hook**:
```json
{
  "hooks": {
    "TeammateIdle": [{
      "matcher": "",
      "hooks": [{
        "type": "prompt",
        "prompt": "Has the teammate completed their assigned task correctly? 
                   Review their work and either approve them to go idle 
                   or send feedback to continue working."
      }]
    }]
  }
}
```

**Using TaskCompleted Hook**:
```json
{
  "hooks": {
    "TaskCompleted": [{
      "matcher": "",
      "hooks": [{
        "type": "command",
        "command": "echo 'Verify task completion: Did it meet the definition of done?'"
      }]
    }]
  }
}
```

### Pattern: Peer Review Before Completion

**Implementation**:
```
Setup:
- Teammate A completes their work
- Teammate B reviews the work
- Only after approval does Teammate A mark task complete

Prompt:
"When you finish implementing {COMPONENT}, 
have the {PEER_REVIEWER} teammate review your work.
Only mark the task complete after their approval."
```

### Pattern: Lead Spot Checks

**Implementation**:
```
"Check in on the team's progress.
Review 1-2 tasks that are marked complete.
If they don't meet standards, ask the teammate to revise.
Only approve high-quality work."
```

---

## Advanced Use Cases

### Use Case 1: Refactoring with Validation

**Team Structure**:
- Refactoring specialist (does the work)
- Validation specialist (ensures correctness)
- Testing specialist (writes/updates tests)

**Coordination**:
```
1. Refactorer: Refactor code section
2. Validator: Verify behavior unchanged
3. Tester: Run tests, update if needed
4. Cycle repeats for next section
```

### Use Case 2: Competing Solutions

**Team Structure**:
- Solution A implementer
- Solution B implementer
- Evaluator (tests both)

**Process**:
```
1. Both implement their solution independently
2. Evaluator tests both on same criteria
3. Compare performance, complexity, maintainability
4. Lead decides which to use
```

### Use Case 3: Security-First Development

**Team Structure**:
- Security reviewer (early feedback)
- Developer (implements with feedback)
- Final validator (confirms fixes)

**Process**:
```
1. Security reviewer analyzes requirements
2. Developer implements while considering feedback
3. Validator ensures no security issues remain
4. Multiple passes until approved
```

### Use Case 4: Documentation-Driven Development

**Team Structure**:
- Documentation specialist (writes docs first)
- Developer (implements to match docs)
- Reviewer (verifies implementation matches)

**Process**:
```
1. Docs specialist writes API/behavior documentation
2. Developer implements based on docs
3. Reviewer verifies implementation matches docs
4. Update docs based on implementation reality
```

---

## Performance Optimization

### Optimization 1: Reduce Idle Time

**Problem**: Teammates waiting for each other

**Solution**:
```
Create independent tasks that don't block each other.
Have teammates work in parallel on unrelated concerns.
Use async communication instead of synchronous discussions.
```

**Example**:
```
❌ Bad: Task A blocks Task B which blocks Task C
✅ Good: Tasks A, B, C are independent, work in parallel
```

### Optimization 2: Right-Size Team

**Guidelines**:
- 1-2 teammates: Overhead, use single session
- 3-5 teammates: Optimal for most tasks
- 6+ teammates: Coordinate well, but higher token cost
- 10+: Diminishing returns, consider sub-teams

**Token Cost per Teammate**: ~1x full Claude session

### Optimization 3: Batch Communications

**Problem**: Too many messages = high latency

**Solution**:
```
Instead of: Continuous updates
Use: Batched reports at checkpoints

Tell teammates: "Work independently. 
Update the status doc at these checkpoints:
- After 25% complete
- After 50% complete
- When finished"
```

### Optimization 4: Minimize Context Switching

**Problem**: Teammates switching between too many tasks

**Solution**:
```
Each teammate gets 2-3 focused tasks maximum.
After completing, pick next available task.
Avoid frequent context switches.
```

### Optimization 5: Async Task Dependencies

**Problem**: Teammate blocked waiting for another

**Solution**:
```
Instead of: Task B depends on Task A output
Use: Task B can start with assumptions about Task A output

Task A outputs specs → Task B starts implementing to specs
When Task A completes → Task B adjusts if specs changed
```

### Optimization 6: Parallel Review Phases

**Problem**: Sequential review burns time

**Solution**:
```
✅ Parallel: All reviewers review simultaneously
❌ Sequential: Reviewer 1 → Reviewer 2 → Reviewer 3

Time savings: O(N) → O(1) for review time
```

---

## Anti-Patterns to Avoid

### Anti-Pattern 1: Over-Coordination

**Problem**: Teammates constantly checking with each other

**Warning Signs**:
- Frequent messages between teammates
- Waiting for responses
- Decision paralysis

**Fix**: 
- Give clear autonomy
- Define boundaries upfront
- Trust teammates to coordinate

### Anti-Pattern 2: Unbalanced Work Distribution

**Problem**: Some teammates finish early, others overloaded

**Warning Signs**:
- Uneven completion times
- Some teammates idle while others work

**Fix**:
- Break work into equal-sized chunks
- Use self-claiming for dynamic allocation
- Monitor and rebalance

### Anti-Pattern 3: Unclear Ownership

**Problem**: Two teammates editing same file

**Warning Signs**:
- Conflicting edits
- Overwrites and rework
- Frustration

**Fix**:
- Clear file ownership before starting
- Each teammate owns specific modules/files
- Coordinate API contracts, not implementations

### Anti-Pattern 4: Task Silos

**Problem**: Teammates isolated, not sharing information

**Warning Signs**:
- No communication between teammates
- Duplicate work
- Missing integration points

**Fix**:
- Require communication at checkpoints
- Use shared documents
- Create explicit sync points

### Anti-Pattern 5: Insufficient Specs

**Problem**: Teammates implement different things

**Warning Signs**:
- Incompatible implementations
- Re-implementation needed
- Wasted effort

**Fix**:
- Write clear requirements first
- Specify interfaces/contracts
- Have specialists agree on architecture

---

## Debugging Common Issues

### Issue: Teammates Getting Stuck

**Diagnosis**:
```
Ask lead to check on all teammates and report status
```

**Resolution Options**:
1. Give teammate additional context/guidance
2. Spawn replacement teammate to continue work
3. Reassign task to different teammate

### Issue: Tasks Not Progressing

**Diagnosis**:
```
Verify task dependencies are correctly resolved
```

**Resolution Options**:
1. Manually mark blocking task as complete
2. Create workaround task
3. Have lead reassign work

### Issue: Inconsistent Quality

**Diagnosis**:
```
Check individual teammate outputs
```

**Resolution Options**:
1. Request teammate to revise
2. Use peer review gates
3. Adjust team composition

---

**Last Updated**: 2026-04-08  
**Version**: 1.0
