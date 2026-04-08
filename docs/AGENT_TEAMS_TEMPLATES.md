# Agent Teams: Templates & Examples

This file provides ready-to-use prompts and templates for common agent team scenarios.

## Table of Contents

1. [Code Review Templates](#code-review-templates)
2. [Debugging Templates](#debugging-templates)
3. [Feature Development Templates](#feature-development-templates)
4. [Research & Analysis Templates](#research--analysis-templates)
5. [Refactoring Templates](#refactoring-templates)
6. [Custom Team Templates](#custom-team-templates)

---

## Code Review Templates

### Multi-Perspective Code Review

**Use Case**: Review PR with different focus areas to catch more issues

**Prompt Template**:
```
Create an agent team to review PR #{PR_NUMBER}. 
Spawn three reviewers with these specific focuses:

1. Security Reviewer
   - Check for authentication/authorization flaws
   - Verify input validation and sanitization
   - Look for cryptographic issues
   - Check for secrets/credentials in code

2. Performance Reviewer
   - Analyze algorithm complexity
   - Check for N+1 queries or inefficient loops
   - Identify memory leaks or resource issues
   - Look for unnecessary re-renders (if frontend)

3. Quality & Testing Reviewer
   - Verify test coverage
   - Check error handling
   - Validate code quality and style
   - Ensure documentation is complete

Each reviewer should:
- Analyze the same PR from their perspective
- Document findings with severity levels
- Point to specific line numbers
- Suggest fixes when appropriate

After all three finish reviewing, I'll synthesize findings.
```

### Service-Specific Code Review

**Use Case**: Review changes spanning multiple services/layers

**Prompt Template**:
```
Create an agent team to review changes across our {TECHNOLOGY_STACK}:

1. Backend Service Reviewer (for src/backend/)
   - API design and REST principles
   - Database query efficiency
   - Error handling and logging
   - Security for backend endpoints

2. Frontend Service Reviewer (for src/frontend/)
   - React/Vue component patterns
   - State management correctness
   - Accessibility compliance
   - Performance and bundle size

3. DevOps Reviewer (for infrastructure/)
   - Infrastructure-as-code correctness
   - Deployment safety
   - Monitoring and observability
   - Security group and permissions

Each reviewer should examine their service area and report findings.
Coordinate any cross-service concerns (e.g., API contract changes).
```

---

## Debugging Templates

### Competing Hypotheses Investigation

**Use Case**: Root cause is unclear, need to explore multiple theories

**Prompt Template**:
```
We have a production issue: {PROBLEM_DESCRIPTION}

Create an agent team with 5 investigators, each testing a different hypothesis:

1. Database Hypothesis Investigator
   - Check query performance
   - Look for connection pool exhaustion
   - Review transaction isolation
   - Check for deadlocks

2. Network & Infrastructure Investigator
   - Check network latency
   - Review load balancer config
   - Look for timeouts
   - Check CDN/caching issues

3. Application Logic Investigator
   - Trace request flow through code
   - Check for race conditions
   - Look for memory issues
   - Review error handling

4. Third-Party Integration Investigator
   - Check dependency versions
   - Review API rate limits
   - Look for breaking changes
   - Check external service health

5. Observability & Monitoring Investigator
   - Check logs for errors
   - Review metrics and traces
   - Look for performance degradation patterns
   - Examine alerting rules

Each investigator should:
- Thoroughly test their hypothesis
- Message others to debate findings
- Update the shared findings document
- Converge on the actual root cause

Make this a scientific debate where you challenge each other's theories.
```

### Performance Degradation Investigation

**Use Case**: App is slower, unclear why

**Prompt Template**:
```
Users report the {SERVICE} is significantly slower.
Create an agent team to investigate performance degradation:

1. Database Performance Investigator
   - Analyze slow query logs
   - Check index usage
   - Review connection pool metrics
   - Profile recent schema changes

2. Application Profiler
   - CPU usage analysis
   - Memory usage patterns
   - Identify hot code paths
   - Check for memory leaks

3. Infrastructure & DevOps
   - Server resource utilization
   - Network bandwidth usage
   - Container/pod metrics
   - Disk I/O analysis

4. Frontend Performance (if applicable)
   - Page load time breakdown
   - JavaScript execution time
   - Rendering performance
   - Network waterfall analysis

5. Data-Driven Analyzer
   - Compare metrics across time periods
   - Identify when degradation started
   - Check for traffic spikes
   - Correlate with deployments

Have the team converge on: what changed, what's the impact, and what needs fixing.
```

---

## Feature Development Templates

### Building a New Module

**Use Case**: Implement a new feature/module in parallel

**Prompt Template**:
```
Build the {MODULE_NAME} module by having teammates work on different layers.
Create an agent team with these specialist teammates:

1. Data & Database Specialist
   - Design database schema in {SCHEMA_PATH}
   - Create migrations
   - Define data models
   - Optimize for queries
   - Task: Complete before API teammate starts

2. API & Business Logic Specialist
   - Design API endpoints in {API_PATH}
   - Implement business logic
   - Add input validation
   - Create error handling
   - Depends on: Database schema completion
   
3. Frontend Integration Specialist
   - Implement UI components
   - Connect to API endpoints
   - Handle error states
   - Add loading states
   - Depends on: API endpoints completion

4. Testing & Quality Specialist
   - Write unit tests for business logic
   - Write integration tests for API
   - Write E2E tests for frontend
   - Ensure {MIN_COVERAGE}% coverage
   - Can work in parallel but validates overall

Each teammate should:
- Own their specific files/directories
- Write well-documented code
- Include error handling
- Create tests as they go
- Coordinate API contracts

Expected output: A fully implemented, tested {MODULE_NAME} module.
```

### Feature Flag & Rollout

**Use Case**: Implement feature behind feature flag

**Prompt Template**:
```
Implement {FEATURE_NAME} using feature flags for safe rollout.
Create an agent team:

1. Feature Implementation Specialist
   - Implement feature in src/features/{FEATURE_NAME}/
   - Write feature code
   - Create integration tests
   - Ensure no breaking changes

2. Feature Flag Infrastructure Specialist
   - Set up feature flag in {FLAG_SYSTEM}
   - Create flag configuration
   - Set up flag defaults
   - Document flag for operations team

3. Documentation & Migration Specialist
   - Document feature in docs/
   - Create migration guide if needed
   - Write rollout runbook
   - Create rollback procedures

4. Monitoring & Observability Specialist
   - Add feature flag metrics
   - Set up dashboards
   - Create alerts for issues
   - Document troubleshooting steps

Coordinate on the rollout strategy: gradual rollout from {START_PERCENTAGE}% to 100%.
```

---

## Research & Analysis Templates

### Design Decision Analysis

**Use Case**: Explore design tradeoffs from multiple angles

**Prompt Template**:
```
We need to design {SYSTEM/COMPONENT}.

Create an agent team to explore this from different perspectives:

1. User Experience Designer
   - How will users interact with this?
   - What's the mental model?
   - Where might users get confused?
   - How can we make it intuitive?

2. Architect/Infrastructure Designer
   - What's the technical architecture?
   - What are the scalability implications?
   - What are the failure modes?
   - How do we handle edge cases?

3. Operations/Reliability Engineer
   - How will we monitor this in production?
   - What are the failure modes?
   - How do we debug issues?
   - What metrics matter?

4. Security Specialist
   - What are the security implications?
   - What vulnerabilities exist?
   - How do we protect user data?
   - What compliance requirements apply?

5. Devil's Advocate
   - Challenge the assumptions
   - Point out problems with the approach
   - Suggest alternatives
   - Question what might break

Have them debate the design, challenge each other, and converge on:
- What approach should we take?
- What are the tradeoffs?
- What risks should we mitigate?
- What's our implementation plan?
```

### Technology Evaluation

**Use Case**: Evaluate technologies/libraries for adoption

**Prompt Template**:
```
We're considering {TECHNOLOGIES} for {USE_CASE}.

Create an agent team to evaluate from multiple angles:

1. Technical Fit Evaluator
   - Does it solve our problem?
   - Performance characteristics
   - Feature completeness
   - API design quality

2. Ecosystem & Stability Evaluator
   - Community size and activity
   - Maintenance and updates
   - Long-term viability
   - Dependency health

3. Integration Specialist
   - How hard is it to integrate?
   - Breaking changes in updates?
   - Compatibility with our stack?
   - Migration effort if we switch?

4. Security & Compliance Reviewer
   - Security track record
   - Vulnerability disclosure process
   - Compliance requirements
   - License implications

5. Cost & Resource Analyzer
   - Direct costs
   - Learning curve and training time
   - Long-term maintenance burden
   - Support and commercial options

Have them debate the options and recommend {TECHNOLOGY} or alternative.
Include risk analysis and mitigation strategies.
```

---

## Refactoring Templates

### Large-Scale Refactoring

**Use Case**: Refactor code across multiple files/modules

**Prompt Template**:
```
Refactor {COMPONENT_NAME} to improve {GOAL: code quality, performance, maintainability}.

Create an agent team where each teammate owns a specific aspect:

1. Data Model Refactorer
   - Refactor {DATA_MODEL_PATH}
   - Improve structure and clarity
   - Update types/interfaces
   - Maintain backward compatibility

2. Core Logic Refactorer
   - Refactor business logic in {LOGIC_PATH}
   - Extract helper functions
   - Improve testability
   - Add documentation

3. API/Interface Refactorer
   - Update public APIs in {API_PATH}
   - Maintain backward compatibility
   - Improve usability
   - Update documentation

4. Test Refactorer
   - Update tests in {TEST_PATH}
   - Improve test structure
   - Increase coverage
   - Add integration tests

5. Integration Verifier
   - Run the full test suite
   - Verify no regressions
   - Check performance impact
   - Validate refactoring goals

Each teammate should:
- Refactor their section
- Add/update tests
- Maintain backward compatibility
- Document changes
- Ensure integration points work

Final verification: All tests pass, performance targets met, code quality improved.
```

### Deprecated Dependency Removal

**Use Case**: Remove/replace deprecated dependency across codebase

**Prompt Template**:
```
We need to remove {OLD_LIBRARY} and replace with {NEW_LIBRARY}.

Create an agent team:

1. Search & Analysis Specialist
   - Find all usages of {OLD_LIBRARY}
   - Categorize usage patterns
   - Identify replacement strategy for each
   - Document dependency graph

2. Backend Migration Specialist
   - Migrate backend usages in src/backend/
   - Update imports
   - Test backend functionality
   - Verify API contracts

3. Frontend Migration Specialist
   - Migrate frontend usages in src/frontend/
   - Update components
   - Test UI functionality
   - Verify component contracts

4. Testing & QA Specialist
   - Update/create tests for new library usage
   - Run full test suite
   - Check for regressions
   - Verify behavior parity

5. Dependency Cleaner
   - Remove {OLD_LIBRARY} from package.json
   - Update lock files
   - Verify no dead code
   - Update documentation

Each teammate:
- Owns their specific file sections
- Maintains test coverage
- Documents migration decisions
- Handles compatibility issues

Goal: Complete migration from {OLD_LIBRARY} to {NEW_LIBRARY}.
```

---

## Custom Team Templates

### Template: 3-Teammate Specialist Team

Use this template for most projects:

```
Create an agent team with 3 specialist teammates:

1. {SPECIALIST_1_NAME}
   Role: {RESPONSIBILITY}
   Focus: {SPECIFIC_AREAS}
   Files: {FILE_PATHS}
   Success criteria: {GOALS}

2. {SPECIALIST_2_NAME}
   Role: {RESPONSIBILITY}
   Focus: {SPECIFIC_AREAS}
   Files: {FILE_PATHS}
   Success criteria: {GOALS}

3. {SPECIALIST_3_NAME}
   Role: {RESPONSIBILITY}
   Focus: {SPECIFIC_AREAS}
   Files: {FILE_PATHS}
   Success criteria: {GOALS}

Task breakdown:
- Task 1: {TASK_NAME} (assign to {SPECIALIST})
- Task 2: {TASK_NAME} (assign to {SPECIALIST})
- Task 3: {TASK_NAME} (assign to {SPECIALIST})
- Task 4: {TASK_NAME} (open for self-claiming)

Coordination:
- Sync points: After tasks 1 and 2
- Dependencies: Task 3 depends on tasks 1-2
- Communication: Message about {COORDINATION_POINTS}
```

### Template: 5-Teammate Review Team

Use for comprehensive reviews:

```
Create an agent team for comprehensive {THING} review:

1. {FOCUS_1} Reviewer
   Criteria: {WHAT_TO_CHECK}
   Severity mapping: Critical, High, Medium, Low
   Report: Line numbers + description + suggested fix

2. {FOCUS_2} Reviewer
   Criteria: {WHAT_TO_CHECK}
   Severity mapping: Critical, High, Medium, Low
   Report: Line numbers + description + suggested fix

3. {FOCUS_3} Reviewer
   Criteria: {WHAT_TO_CHECK}
   Severity mapping: Critical, High, Medium, Low
   Report: Line numbers + description + suggested fix

4. {FOCUS_4} Reviewer
   Criteria: {WHAT_TO_CHECK}
   Severity mapping: Critical, High, Medium, Low
   Report: Line numbers + description + suggested fix

5. {FOCUS_5} Reviewer
   Criteria: {WHAT_TO_CHECK}
   Severity mapping: Critical, High, Medium, Low
   Report: Line numbers + description + suggested fix

Each reviewer:
- Works independently from their perspective
- Creates a summary document
- Highlights critical issues first

After all reviews complete:
- Consolidate findings
- Prioritize by severity
- Create action items
```

### Template: Competitive Analysis Team

Use for exploring tradeoffs:

```
Create an agent team for competitive analysis of {OPTIONS}:

Each teammate explores one option:

1. {OPTION_1} Advocate
   - Deep dive into {OPTION_1}
   - Explore strengths
   - Best use cases
   - Integration ease

2. {OPTION_2} Advocate
   - Deep dive into {OPTION_2}
   - Explore strengths
   - Best use cases
   - Integration ease

3. {OPTION_3} Advocate
   - Deep dive into {OPTION_3}
   - Explore strengths
   - Best use cases
   - Integration ease

4. Critical Analyst
   - Identify weaknesses in each option
   - Challenge claims
   - Highlight risks
   - Ask hard questions

Team consensus:
- Which option wins and why
- Key tradeoffs
- Risks to mitigate
- Recommended approach
```

---

## Tips for Using Templates

1. **Customize for your context**: Replace placeholders with your actual values
2. **Adjust team size**: Use 3 for simple tasks, 5 for complex ones
3. **Set clear success criteria**: Specify what "done" looks like
4. **Define coordination points**: How will teammates sync up?
5. **Specify file ownership**: Avoid conflicts with clear boundaries
6. **Include output format**: How should teammates document findings?

---

## Examples Using Templates

### Example 1: Reviewing a PR with Security Focus

```
Create an agent team to review PR #456 on the authentication module.

Spawn three reviewers:

1. Security Reviewer
   - Look for authentication bypasses
   - Check JWT token handling (signature, expiration, claims)
   - Verify password hashing (using bcrypt?)
   - Check CORS configuration
   - Review error messages (no info leaks?)
   - Look for timing attacks

2. Code Quality Reviewer
   - Check code structure and readability
   - Verify error handling
   - Check for code duplication
   - Ensure proper logging
   - Validate documentation

3. Testing Reviewer
   - Verify test coverage
   - Check edge case handling
   - Validate error cases
   - Check for race conditions

Each reviewer: analyze independently, document findings with line numbers.
Conclude with severity rating (Critical/High/Medium/Low).
```

### Example 2: Debugging a Memory Leak

```
We suspect a memory leak in the {SERVICE}. 
Create an agent team with competing hypotheses:

1. Event Listener Leak Investigator
   - Check if event listeners are being removed
   - Look for setTimeout/setInterval cleanup
   - Check for observable subscriptions
   - Review timer cleanup

2. Object Reference Leak Investigator
   - Look for circular references
   - Check for global variable accumulation
   - Review cache implementations
   - Look for detached DOM nodes

3. Async Operations Investigator
   - Check if promises complete
   - Look for unresolved async operations
   - Check for connection pool leaks
   - Review request cleanup

4. Metrics-Based Investigator
   - Analyze heap snapshots over time
   - Check object allocation patterns
   - Look for growth trends
   - Correlate with specific operations

They should collaborate and converge on the actual cause.
Create a fix once identified.
```

---

**Last Updated**: 2026-04-08  
**Version**: 1.0
