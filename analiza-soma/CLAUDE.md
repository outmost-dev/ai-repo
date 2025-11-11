# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a **documentation and planning repository** for the complete migration of the Somaway platform (somaway.ro) - a video learning platform. The repository contains comprehensive JIRA-style documentation for migrating three applications:

- **Backend**: Node.js/NestJS → .NET Core (80+ API endpoints, 20+ entities)
- **Admin Dashboard**: React 18 + Redux → Vue 3 + Pinia (7 main pages)
- **Web Client**: Next.js 15 + Redux → Nuxt 3 + Pinia (21 pages)

**Important**: This repository contains **only documentation**, not implementation code. The actual implementation will happen in separate repositories.

## Repository Structure

```
analiza-soma/
├── BackEnd/                    # Backend migration documentation (17 files)
│   ├── JIRA_AUTH_MODULE.txt
│   ├── JIRA_DATABASE_ENTITIES.txt
│   ├── JIRA_PAYMENTS_MODULE.txt
│   ├── JIRA_STRIPE_SERVICE.txt
│   ├── JIRA_VIMEO_SERVICE.txt
│   ├── JIRA_ZOOM_SERVICE.txt
│   └── ... (11 more files)
│
├── Admin/                      # Admin dashboard migration docs (10 files)
│   ├── ADMIN_JIRA_AUTHENTICATION_MODULE.txt
│   ├── ADMIN_JIRA_USERS_MODULE.txt
│   ├── ADMIN_JIRA_COURSES_MODULE.txt
│   ├── ADMIN_MIGRATION_PLAN.txt
│   └── ... (6 more files)
│
├── Web - Client/               # Web client migration docs (10 files)
│   ├── WEB_CLIENT_JIRA_AUTHENTICATION_MODULE.txt
│   ├── WEB_CLIENT_JIRA_COURSES_MODULE.txt
│   ├── WEB_CLIENT_JIRA_SUBSCRIPTIONS_MODULE.txt
│   ├── WEB_CLIENT_MIGRATION_PLAN.txt
│   └── ... (6 more files)
│
└── agenti-soma.md             # 23 specialized AI agents for implementation
```

## Documentation Format

All documentation files follow a consistent JIRA-style format:

### Backend Documentation Structure
Each `JIRA_*_MODULE.txt` file contains:
- **Module Overview**: Description, tech stack transition, dependencies
- **User Stories**: Business requirements broken into tasks
- **Tasks**: Detailed implementation specs with:
  - Business logic explanation
  - Current implementation (NestJS/TypeScript)
  - Target implementation (.NET Core/C#)
  - API contracts (request/response examples)
  - Database schemas
  - Authorization requirements
  - Dependencies and integration points
  - Recommendations

### Frontend Documentation Structure
Each `*_JIRA_*_MODULE.txt` file contains:
- **Module Overview**: Pages, components, state management
- **Tasks**: Component-by-component migration specs with:
  - Current implementation (React/Next.js)
  - Target implementation (Vue 3/Nuxt 3)
  - Redux → Pinia migration patterns
  - Ant Design → Ant Design Vue conversions
  - Form handling patterns
  - API integration patterns

### Migration Plans
Files named `*_MIGRATION_PLAN.txt` contain:
- Week-by-week implementation timeline
- Phase breakdown
- Dependencies between tasks
- Tech stack transition details
- Testing strategies

## Key Project Details

### Technology Stack Transitions

**Backend (Node.js/NestJS → .NET Core)**:
- TypeORM → Entity Framework Core
- Passport strategies → .NET Identity + JWT middleware
- Express middleware → .NET middleware pipeline
- NestJS decorators → .NET attributes
- Jest tests → xUnit/NUnit

**Admin Dashboard (React → Vue 3)**:
- React 18.2.0 → Vue 3.4+
- Redux Toolkit → Pinia
- Ant Design 5.20.1 → Ant Design Vue 4.x
- React Router 6 → Vue Router 4.x
- React hooks → Vue Composition API

**Web Client (Next.js → Nuxt 3)**:
- Next.js 15 Pages Router → Nuxt 3 file-based routing
- React 18 → Vue 3 Composition API
- Redux Toolkit → Pinia
- next/router → Vue Router (via Nuxt)
- getServerSideProps → Nuxt server API

### Critical Integrations

The platform integrates with multiple external services:

**Payment Processing**:
- Stripe (primary): PaymentIntents, Subscriptions, Webhooks
- Librapay (secondary): Alternative payment gateway
- SmartBill: Romanian invoicing system (currency: RON)

**Video & Live Sessions**:
- Vimeo: Video hosting with OAuth 2.0
- Zoom: Live meetings and webinars with JWT auth

**Email & Marketing**:
- Postmark: Transactional emails
- MailerLite: Marketing automation campaigns

**Analytics & Tracking**:
- FirstPromoter: Affiliate tracking
- Facebook Pixel: Lead tracking
- Custom analytics: VIEW_COURSE, VIEW_LESSON, TIME_SPENT

**Authentication**:
- 4 JWT token types: Access, Refresh, Email Validation, Subscription Validation
- Role-based access: ADMIN, CREATOR, CUSTOMER, GUEST
- Password hashing: Argon2

### Database Architecture

**20+ Entities** with complex relationships:
- User, Subscription, Course, Lesson, Category
- Invoice, Order, Campaign, Analytics, AnalyticsTime
- Shortlist, Address, Payment, SubscriptionType
- ZoomMeeting, ZoomWebinar

**Key Relationships**:
- User → Subscriptions (OneToMany)
- User → Address (OneToOne)
- Course → Lessons (OneToMany)
- Subscription → SubscriptionType (ManyToOne)
- User → Campaigns (ManyToMany through junction table)

## AI Agents for Implementation

The file `agenti-soma.md` defines **26 specialized AI agents** organized in 6 tiers following an **Audit-First Migration Strategy**:

### TIER 0: Pre-Migration Audit (3 agents) ⭐ CRITICAL
1. **Legacy Code Auditor Agent (LCAA)** - Scans legacy code for bugs, anti-patterns, race conditions, memory leaks
2. **Business Logic Validator Agent (BLVA)** - Validates business logic against JIRA specs, detects edge cases
3. **Security Vulnerability Scanner Agent (SVSA)** - OWASP Top 10 scanning, hardcoded credentials, injection vulnerabilities

**CRITICAL**: These agents MUST run BEFORE migration starts. No code is migrated until audit is complete and Chief Architect decides which bugs to fix.

### TIER 1: Orchestration (2 agents)
4. **Chief Architect Agent (CAA)** - Master orchestrator and technical decision maker
5. **Project Manager Agent (PMA)** - Timeline management and resource allocation

### TIER 2: Backend Specialization (8 agents)
6. Backend Migration Architect, 7. Authentication & Security Agent, 8. Payment Integration Agent, 9. Video & Live Services Agent, 10. Email & Marketing Agent, 11. Database & Entity Agent, 12. Analytics & Reporting Agent, 13. API Testing & Documentation Agent

### TIER 3: Frontend Specialization (7 agents)
14. Admin Dashboard Migration Agent, 15. Web Client Migration Agent, 16. Authentication UI Agent, 17. Course & Video Player Agent, 18. Subscription & Payment UI Agent, 19. Dashboard & Profile Agent, 20. Shared Components Agent

### TIER 4: QA & Deployment (4 agents)
21. Testing Automation Agent, 22. Performance Optimization Agent, 23. DevOps & CI/CD Agent, 24. Documentation Agent

### TIER 5: Specialist Support (2 agents)
25. Migration Validator Agent, 26. Security Audit Agent

**Usage Pattern**:
1. **ALWAYS start with TIER 0** - audit legacy code before migration
2. Reference appropriate agents from `agenti-soma.md` for each module
3. Follow Audit-First Strategy - never migrate bugs from old platform
4. Validate migrations with TIER 5 agents before deployment

## Working with This Repository

### Reading Documentation

To understand a specific module:

1. **Identify the module** in the appropriate folder (BackEnd, Admin, or Web - Client)
2. **Read the complete file** - each file is comprehensive and self-contained
3. **Note the dependencies** - most modules reference other modules
4. **Check migration plans** - for timeline and phase information

### Creating Implementation Plans

When asked to implement a feature:

1. **Read relevant documentation files** for complete context
2. **Reference agent definitions** from `agenti-soma.md`
3. **Identify dependencies** between modules
4. **Follow migration patterns** documented in each file
5. **Preserve API contracts** - backend and frontend must match
6. **Consider external integrations** (Stripe, Vimeo, etc.)

### Key Considerations

**Always maintain**:
- API contract compatibility (80+ endpoints must match exactly)
- Database schema consistency (20+ entities with relationships)
- Authentication flow (4 token types, role-based access)
- External service integrations (Stripe, Vimeo, Zoom, etc.)
- Business logic equivalence (React → Vue must behave identically)

**Never**:
- Change API contracts without updating both backend and frontend docs
- Skip security considerations (OWASP Top 10, JWT validation, etc.)
- Ignore external service requirements (Stripe webhooks, Vimeo OAuth, etc.)
- Break existing functionality during migration

## Project Timeline (Audit-First Strategy)

**Estimated Duration**: 18 weeks (4.5 months)

**Phase Breakdown**:
- **Weeks 1-2: PHASE 0 - Pre-Migration Audit** ⭐ CRITICAL
  - Legacy code audit (LCAA)
  - Business logic validation (BLVA)
  - Security vulnerability scanning (SVSA)
  - Audit report generation and bug triage
  - **GATE**: No migration starts until audit complete

- Weeks 3-4: PHASE 1 - Foundation (project structure, CI/CD)
- Weeks 5-8: PHASE 2 - Backend Core (entities, auth, basic APIs)
- Weeks 9-11: PHASE 3 - Backend Services (payments, video, email, analytics)
- Weeks 12-14: PHASE 4 - Admin Dashboard (7 pages migration)
- Weeks 15-17: PHASE 5 - Web Client (21 pages migration)
- Week 18: PHASE 6 - Optimization & deployment

**IMPORTANT**: The 2-week audit phase (PHASE 0) is MANDATORY and BLOCKS all migration work. This ensures the new platform starts with clean, bug-free code.

## Common Workflows

### Pre-Migration Audit (MANDATORY FIRST STEP)

```
1. Select module for audit (start with critical: Auth, Payments)
2. Run Legacy Code Auditor Agent:
   - Scan for bugs, anti-patterns, memory leaks
   - Categorize: CRITICAL/MEDIUM/LOW
3. Run Business Logic Validator Agent:
   - Compare code with JIRA documentation
   - Identify edge cases and inconsistencies
4. Run Security Vulnerability Scanner Agent:
   - OWASP Top 10 scan
   - Check for hardcoded secrets, weak validation
5. Generate comprehensive audit report
6. Chief Architect Agent decides:
   - Which bugs to fix before migration
   - Which bugs to fix during migration
   - Which are not bugs (features)
7. GATE: Only proceed to migration after audit approval
```

### Analyzing a Module (After Audit)

```
1. Review audit report for the module
2. Read the module's JIRA documentation file
3. Identify all dependencies and integrations
4. Review current implementation (NestJS/React/Next.js)
5. Note bugs/issues from audit report
6. Study target implementation (.NET/Vue/Nuxt)
7. Plan how to migrate WITHOUT bugs
8. Note API contracts and data flows
9. Check security and authorization requirements
```

### Creating an Implementation Agent

When creating custom agents (in `.claude/agents/`):

```
1. Review agenti-soma.md for agent responsibilities
2. Read relevant documentation files for context
3. Define strict rules (what agent MUST and MUST NOT do)
4. Specify input/output formats
5. Add validation checklists
6. Include success criteria
```

### Validating Migrations

For any migration (Backend/Admin/Web Client):

```
1. Compare implementation with documentation
2. Verify API contracts match exactly
3. Check database relationships are preserved
4. Validate authentication/authorization flows
5. Test external service integrations
6. Ensure UI/UX equivalence (for frontend)
```

## Important Notes

- **File sizes**: Some documentation files are large (>100KB) due to comprehensive task breakdowns
- **Naming**: Note "Web - Client" folder has space in name (use quotes in paths)
- **Language**: Documentation is in Romanian (business context) and English (technical specs)
- **Completeness**: All 37 files have been analyzed - documentation is 100% complete
- **No code**: This repo contains ZERO implementation code - only planning and specifications

## Related Resources

- **Parent directory**: `/home/valim/ai-repo/` contains other learning materials
- **Agent marketplace**: Available at `wshobson/agents` (see `/home/valim/ai-repo/agents/`)
- **Custom agents**: Can be created in `.claude/agents/` directory

---

## Project Status

**Last Updated**: January 11, 2025

**Documentation Status**: ✅ Complete (37/37 files analyzed)

**Agent Architecture**: ✅ Complete (26 agents defined)
- TIER 0: Pre-Migration Audit (3 agents) ⭐
- TIER 1: Orchestration (2 agents)
- TIER 2: Backend (8 agents)
- TIER 3: Frontend (7 agents)
- TIER 4: QA & Deployment (4 agents)
- TIER 5: Support (2 agents)

**Migration Strategy**: ✅ Audit-First (never migrate bugs)

**Timeline**: 18 weeks (4.5 months)
- Phase 0: Audit (2 weeks) - CRITICAL GATE
- Phases 1-6: Implementation (16 weeks)

**Implementation Status**: ⏳ Not started (planning phase)

**Next Step**: Begin PHASE 0 - Pre-Migration Audit with TIER 0 agents
