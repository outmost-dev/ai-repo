# CLAUDE.md - Project Overview

## Project Information

**Project Name:** cum-sa-faci-agenti (How to Use Agents)  
**Type:** Documentation/Educational Resource  
**Language:** Markdown (Romanian)  
**Purpose:** Comprehensive tutorial and interactive learning path for using AI agents in Claude Code  
**Repository Size:** 24KB (single file)  
**Location:** /home/valim/ai-repo/cum-sa-faci-agenti

## Project Structure

This is a documentation-only repository with a single file:

```
cum-sa-faci-agenti/
└── how-touse-agents.md     # Main tutorial document (540 lines, ~19KB)
```

**Note:** This repository contains no source code, configuration files, or build scripts. It is purely educational documentation.

## Architecture & Organization

### Content Structure

The `how-touse-agents.md` file is organized into the following major sections:

1. **Introduction (Lines 1-6)**
   - Definition of agents (subagents) in Claude Code
   - Overview of agent capabilities

2. **Usage Instructions (Lines 8-31)**
   - Automatic delegation
   - Explicit invocation with examples

3. **Agent Types (Lines 33-66)**
   - Built-in agents documentation
   - Custom agent creation (project-level and user-level)

4. **Agent Management (Lines 69-92)**
   - `/agents` command usage
   - Manual agent configuration with YAML frontmatter

5. **Practical Examples (Lines 94-153)**
   - Step-by-step workflows for common scenarios
   - Code exploration, review, debugging, and refactoring

6. **Best Practices (Lines 154-189)**
   - Agent design guidelines
   - Efficient usage patterns
   - Version control recommendations

7. **Common Workflows (Lines 191-225)**
   - Feature development workflow
   - Debugging workflow
   - Data analysis workflow

8. **Custom Agent Template (Lines 227-255)**
   - Complete example with YAML configuration
   - System prompt structure

9. **FAQ Section (Lines 257-273)**
   - Common questions and answers

10. **Interactive Learning Path (Lines 275-517)**
    - 15 structured exercises across 3 levels
    - Progress tracking system
    - Final project

11. **Conclusion & Resources (Lines 519-539)**
    - Summary of benefits
    - Official documentation links

## Key Concepts & Patterns

### 1. Agent Types Documented

**Built-in Agents:**
- **Plan** - Code research without modifications
- **Explore** - Rapid codebase navigation and search
- **Code-reviewer** - Code quality and security analysis
- **Debugger** - Root cause analysis for errors
- **Data-scientist** - SQL queries and data visualization

**Custom Agents:**
- Project-level: `.claude/agents/` (Git-synchronized)
- User-level: `~/.claude/agents/` (available across all projects)

### 2. Agent Configuration Pattern

Agents are defined using Markdown files with YAML frontmatter:

```yaml
---
name: agent-name
description: When and how to use this agent
tools: Read, Edit, Bash  # Optional - limit tools
model: sonnet            # Optional - specify model
---

System prompt defining the role, approach, and specific instructions.
```

### 3. Invocation Patterns

**Automatic Delegation:**
- Claude decides automatically based on task description
- Agents with "use PROACTIVELY" in description are auto-invoked

**Explicit Invocation:**
- "Use the code-reviewer agent to check my changes"
- "Ask the debugger agent to investigate this error"
- "Use the Explore agent to find all configuration files"

### 4. Workflow Patterns

**Single Agent:** Simple tasks with one specialized agent

**Sequential Workflow:** Multiple agents in a pipeline
- Explore → Plan → Implement → Code-review

**Parallel Workflow:** Multiple independent agent tasks

## Development Workflow

### No Build System

This is a documentation-only project with no build, test, or lint commands.

### Content Management

- **Editing:** Direct Markdown file editing
- **Version Control:** Designed to be committed to Git (though directory itself is not a repo)
- **Sharing:** Can be shared as part of project documentation or user guides

### Usage Context

This tutorial is intended to be:
1. Read by developers learning Claude Code
2. Used as a reference during development
3. Followed interactively through the learning path exercises
4. Shared within development teams

## Related Projects

Located in parent directory `/home/valim/ai-repo/`:
- **cum-sa-folosesti-claude-cli** - Sibling project about Claude CLI usage

## Interactive Learning Path

The tutorial includes a comprehensive 15-exercise learning path:

### Level 1: Beginner (5 exercises)
- Exercise 1.1: First agent interaction
- Exercise 1.2: Explicit invocation with Explore agent
- Exercise 1.3: Understanding agent output
- Exercise 1.4: Simple code review
- Exercise 1.5: Automatic delegation

### Level 2: Intermediate (5 exercises)
- Exercise 2.1: Creating first custom agent
- Exercise 2.2: Testing custom agent
- Exercise 2.3: Two-agent workflow
- Exercise 2.4: Debugging with specialized agent
- Exercise 2.5: Plan mode for refactoring

### Level 3: Advanced (4 exercises)
- Exercise 3.1: Advanced custom agent with multiple tools
- Exercise 3.2: Complex 3+ agent cascading workflow
- Exercise 3.3: Optimization and tool permissions
- Exercise 3.4: Error handling and recovery

### Final Project
- Build a complete system with 3-4 custom agents working together

## Documentation Standards

### Language & Style
- **Primary Language:** Romanian
- **Tone:** Educational, step-by-step, beginner-friendly
- **Format:** Markdown with clear sections and examples

### Conventions Used
- ✅ for DO recommendations
- ❌ for DON'T warnings
- Emojis for section markers (🌱, 🚀, 💎, 🏆, 🎯)
- Code blocks for examples
- Checkboxes [ ] for progress tracking

### Example Patterns
Each practical example follows this structure:
1. **Scenario:** Describe the situation
2. **Steps:** Command or request to make
3. **Agent behavior:** What the agent will do
4. **Expected outcome:** Results you'll see

## Important Notes

1. **No Executable Code:** This repository contains only documentation, no runnable code
2. **Educational Focus:** Designed as a learning resource, not a software project
3. **Romanian Language:** All content is in Romanian for Romanian-speaking developers
4. **Claude Code Specific:** Content is specifically about Claude Code features, not generic AI agents
5. **Interactive Design:** Includes progress tracking and hands-on exercises
6. **Version Agnostic:** No specific Claude Code version mentioned

## Resources Referenced

- Official Documentation: https://code.claude.com/docs/en/sub-agents.md
- Agent directories: `.claude/agents/` in projects
- Commands: `/agents` and `/help`

## Quick Reference

### Key Commands Mentioned
- `/agents` - View, create, edit, and delete agents
- `/help` - General help

### Key Directories
- `.claude/agents/` - Project-level custom agents
- `~/.claude/agents/` - User-level custom agents

### Agent Tool Options
- Read - Read files
- Grep - Search content
- Write - Create/modify files
- Edit - Edit existing files
- Bash - Execute commands
- Glob - Find files by pattern

## Target Audience

- Developers learning Claude Code
- Teams wanting to implement custom agents
- Users wanting to optimize their Claude Code workflow
- Romanian-speaking developers (primary audience)

## Maintenance Notes

- Content is self-contained in single file
- No dependencies or external requirements
- Can be updated by editing the Markdown file directly
- Progress tracking checkboxes can be modified for each learner
- Should be kept in sync with Claude Code feature updates

---

**Last Analyzed:** 2025-11-07  
**Analysis Tool:** Claude Code - Explore capability  
**File Count:** 1  
**Total Lines:** 540  
**Total Size:** ~19KB
