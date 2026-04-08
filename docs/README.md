# Agent Teams Documentation

Comprehensive guide for building effective and efficient agent teams in Claude Code.

This documentation provides everything needed to understand, design, and implement agent teams for parallel development work.

## 📚 Documentation Structure

### 1. **[AGENT_TEAMS_REFERENCE.md](./AGENT_TEAMS_REFERENCE.md)** - Complete Reference Guide
The primary reference for all agent team features and concepts.

**Contents**:
- Quick start and setup
- When to use agent teams vs subagents
- Architecture overview
- Team configuration and display modes
- Controlling teams and assigning work
- Best practices and guidelines
- Common troubleshooting
- Known limitations

**Best For**: 
- First-time setup
- Understanding core concepts
- Looking up specific features
- Troubleshooting issues

**Read This First** ✅

---

### 2. **[AGENT_TEAMS_TEMPLATES.md](./AGENT_TEAMS_TEMPLATES.md)** - Ready-to-Use Prompts & Examples
Template prompts and real-world examples for common scenarios.

**Contents**:
- Code review templates
- Debugging templates
- Feature development templates
- Research & analysis templates
- Refactoring templates
- Custom team templates
- Practical examples

**Best For**:
- Getting started with specific task
- Copy-paste ready prompts
- Learning from examples
- Understanding team roles

**Use When**: You have a specific task in mind

---

### 3. **[AGENT_TEAMS_PATTERNS.md](./AGENT_TEAMS_PATTERNS.md)** - Advanced Architecture & Patterns
Patterns and architectural approaches for optimized team performance.

**Contents**:
- Team composition patterns
- Communication patterns
- Task coordination patterns
- Work division strategies
- Quality gates and verification
- Advanced use cases
- Performance optimization
- Anti-patterns to avoid

**Best For**:
- Designing complex teams
- Optimizing token usage
- Solving coordination problems
- Learning advanced techniques

**Use When**: Working on complex projects or optimizing existing teams

---

## 🚀 Quick Start

### 1. Enable Agent Teams
```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

### 2. Create Your First Team
```
Create an agent team to [describe your task].
Spawn [N] teammates with [roles].
```

### 3. Use Templates
Find a matching template in `AGENT_TEAMS_TEMPLATES.md` and customize it.

### 4. Monitor and Coordinate
- Use `Shift+Down` to cycle through teammates
- Message teammates directly
- Manage shared task list
- Synthesize results

---

## 🎯 Choose Your Path

### I'm New to Agent Teams
1. Read: [AGENT_TEAMS_REFERENCE.md](./AGENT_TEAMS_REFERENCE.md) - Quick Start section
2. Explore: Basic templates in [AGENT_TEAMS_TEMPLATES.md](./AGENT_TEAMS_TEMPLATES.md)
3. Try: Create your first simple team

### I Want to Use Them Now
1. Find your scenario in [AGENT_TEAMS_TEMPLATES.md](./AGENT_TEAMS_TEMPLATES.md)
2. Copy the template
3. Customize for your task
4. Run it

### I'm Building Complex Teams
1. Read: [AGENT_TEAMS_PATTERNS.md](./AGENT_TEAMS_PATTERNS.md)
2. Study: Team composition patterns
3. Plan: Your team architecture
4. Implement: Using templates as base

### I'm Troubleshooting an Issue
1. Check: [AGENT_TEAMS_REFERENCE.md](./AGENT_TEAMS_REFERENCE.md) - Troubleshooting section
2. Read: Relevant pattern in [AGENT_TEAMS_PATTERNS.md](./AGENT_TEAMS_PATTERNS.md)
3. Review: Anti-patterns section

---

## 📋 Common Scenarios

### Parallel Code Review
**Best Guide**: [AGENT_TEAMS_REFERENCE.md](./AGENT_TEAMS_REFERENCE.md#common-use-cases) + [Templates](./AGENT_TEAMS_TEMPLATES.md#code-review-templates)

**Quick Steps**:
1. Use Code Review template
2. Assign different reviewers different lenses
3. Have them review in parallel
4. Synthesize findings

---

### Debugging with Competing Hypotheses
**Best Guide**: [Templates - Debugging](./AGENT_TEAMS_TEMPLATES.md#debugging-templates) + [Patterns - Hypothesis Teams](./AGENT_TEAMS_PATTERNS.md#pattern-3-hypothesis-teams)

**Quick Steps**:
1. Define hypotheses
2. Spawn investigator per hypothesis
3. Let them debate and converge
4. Document root cause

---

### Building New Module
**Best Guide**: [Templates - Feature Development](./AGENT_TEAMS_TEMPLATES.md#feature-development-templates) + [Patterns - Specialist Teams](./AGENT_TEAMS_PATTERNS.md#pattern-1-specialist-teams)

**Quick Steps**:
1. Break work into layers/components
2. Assign specialist to each
3. Define task dependencies
4. Coordinate via shared task list

---

### Design Exploration
**Best Guide**: [Templates - Research & Analysis](./AGENT_TEAMS_TEMPLATES.md#research--analysis-templates)

**Quick Steps**:
1. Define different perspectives
2. Spawn teammate per perspective
3. Have them explore and debate
4. Converge on design decision

---

## 🔍 Feature Reference

### By Feature
- **Display Modes** → [Reference Guide](./AGENT_TEAMS_REFERENCE.md#display-modes)
- **Task Management** → [Reference Guide](./AGENT_TEAMS_REFERENCE.md#task-management) + [Patterns](./AGENT_TEAMS_PATTERNS.md#task-coordination-patterns)
- **Communication** → [Patterns](./AGENT_TEAMS_PATTERNS.md#communication-patterns)
- **Team Composition** → [Patterns](./AGENT_TEAMS_PATTERNS.md#team-composition-patterns)
- **Work Division** → [Patterns](./AGENT_TEAMS_PATTERNS.md#work-division-strategies)
- **Quality Gates** → [Patterns](./AGENT_TEAMS_PATTERNS.md#quality-gates--verification)

### By Problem
- **Too many permission prompts** → [Reference - Troubleshooting](./AGENT_TEAMS_REFERENCE.md#too-many-permission-prompts)
- **Teammates getting stuck** → [Patterns - Debugging](./AGENT_TEAMS_PATTERNS.md#debugging-common-issues)
- **File conflicts** → [Reference - Best Practices](./AGENT_TEAMS_REFERENCE.md#4-avoid-file-conflicts) + [Patterns - Work Division](./AGENT_TEAMS_PATTERNS.md#work-division-strategies)
- **High token costs** → [Reference - Token Costs](./AGENT_TEAMS_REFERENCE.md#token-cost-considerations) + [Patterns - Optimization](./AGENT_TEAMS_PATTERNS.md#performance-optimization)
- **Poor coordination** → [Patterns - Communication](./AGENT_TEAMS_PATTERNS.md#communication-patterns)

---

## 📊 Token Cost Planning

**Baseline**: Each active teammate ≈ 1 full Claude session worth of tokens

**Cost by Team Size**:
| Teammates | Approximate Cost | Good For |
|-----------|-----------------|----------|
| 1-2 | 2-3x single session | Not recommended (use single session) |
| 3-5 | 4-6x single session | Most projects (good ROI) |
| 6-8 | 7-9x single session | Large complex projects |
| 10+ | 11+x single session | Very large initiatives |

**Cost Optimization Tips**:
1. Right-size team (3-5 is sweet spot)
2. Make tasks independent (avoid idle waiting)
3. Use subagents for smaller delegated work
4. Monitor and redirect unproductive teammates

See [Reference - Token Costs](./AGENT_TEAMS_REFERENCE.md#token-cost-considerations) for details.

---

## ✅ Best Practices Summary

### Before Starting a Team
- [ ] Enable agent teams (set environment variable)
- [ ] Define clear task boundaries
- [ ] Plan team composition
- [ ] Identify file/module ownership
- [ ] Write clear requirements

### While Team is Running
- [ ] Monitor progress regularly
- [ ] Check teammate outputs
- [ ] Redirect when needed
- [ ] Maintain communication
- [ ] Enforce quality standards

### After Completion
- [ ] Review team's work
- [ ] Synthesize findings
- [ ] Clean up team properly
- [ ] Document lessons learned
- [ ] Iterate for next time

---

## 🚨 Critical Warnings

### ⚠️ Known Limitations
- **No in-process resumption**: Teams don't restore after `/resume`
- **One team per session**: Can't have multiple teams at once
- **Task status lag**: Sometimes tasks don't mark as complete
- **No nested teams**: Teammates can't spawn their own teams

See [Reference - Limitations](./AGENT_TEAMS_REFERENCE.md#limitations) for full list.

### ⚠️ Anti-Patterns
Avoid these common mistakes:
- Over-coordination (teammates constantly checking)
- Unbalanced work distribution
- Unclear file ownership
- Missing task specifications
- Letting teams run unattended

See [Patterns - Anti-Patterns](./AGENT_TEAMS_PATTERNS.md#anti-patterns-to-avoid) for details.

---

## 📈 Success Metrics

How to know if your team is working well:

✅ **Good Signs**:
- Teammates finish at roughly the same time
- Minimal messages between teammates
- High-quality output first try
- Clear task progression
- Team achieves goals faster than single developer

❌ **Red Flags**:
- Significant idle time
- Frequent conflict/coordination
- Low-quality output requiring rework
- Tasks getting stuck
- Hidden communication breakdowns

---

## 🔗 Related Resources

- **Official Documentation**: https://code.claude.com/docs/en/agent-teams
- **Subagents**: https://code.claude.com/docs/en/sub-agents
- **Permissions**: https://code.claude.com/docs/en/permissions
- **Git Worktrees**: https://code.claude.com/docs/en/common-workflows

---

## 📝 Document Versions

| Document | Version | Last Updated |
|----------|---------|--------------|
| Reference Guide | 1.0 | 2026-04-08 |
| Templates | 1.0 | 2026-04-08 |
| Patterns | 1.0 | 2026-04-08 |

---

## 💡 Tips for Success

1. **Start small**: Begin with 3-teammate teams
2. **Use templates**: Don't reinvent prompts
3. **Learn from patterns**: Study successful architectures
4. **Monitor carefully**: Watch team progress, redirect as needed
5. **Iterate**: Each team teaches you something for the next

---

## ❓ FAQ

**Q: Should I use agent teams for this task?**  
A: See [Reference - When to Use](./AGENT_TEAMS_REFERENCE.md#when-to-use-agent-teams)

**Q: How many teammates do I need?**  
A: See [Reference - Best Practices](./AGENT_TEAMS_REFERENCE.md#2-choose-appropriate-team-size)

**Q: How much will this cost?**  
A: See [Reference - Token Costs](./AGENT_TEAMS_REFERENCE.md#token-cost-considerations)

**Q: How do I handle conflicts between teammates?**  
A: See [Patterns - Communication](./AGENT_TEAMS_PATTERNS.md#communication-patterns)

**Q: Why are my teammates idle?**  
A: See [Patterns - Performance Optimization](./AGENT_TEAMS_PATTERNS.md#optimization-1-reduce-idle-time)

---

## 🎓 Learning Path

**Beginner** (30 mins):
1. Read: Reference Guide Quick Start
2. Watch: One template example
3. Try: Create first simple team

**Intermediate** (2 hours):
1. Read: Full Reference Guide
2. Study: 3-5 templates
3. Plan: Your first real team
4. Create: Team for actual task

**Advanced** (4+ hours):
1. Study: All patterns
2. Design: Complex team architecture
3. Optimize: Token usage and coordination
4. Mentor: Others in building teams

---

**Created**: 2026-04-08  
**Last Updated**: 2026-04-08  
**Maintained By**: Development Team

---

## 📞 Support

For issues or questions:
- Check [Reference - Troubleshooting](./AGENT_TEAMS_REFERENCE.md#troubleshooting)
- Review [Patterns - Debugging](./AGENT_TEAMS_PATTERNS.md#debugging-common-issues)
- Consult official docs: https://code.claude.com/docs/en/agent-teams
