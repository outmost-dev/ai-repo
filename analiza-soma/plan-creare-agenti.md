# PLAN CREARE AGENȚI AI - PROIECT SOMAWAY

## Prezentare Generală

Acest document trackează procesul de creare a tuturor cei 27 de agenți AI necesari pentru migrarea platformei Somaway.

**Status general**: 3/27 agenți creați (11.1%)
- ✅ WAVE 0: Meta Quality - 1/1 complete (Gandalf 99/100)
- ✅ WAVE 0.5: Requirements - 1/1 complete (SCA 96/100)
- ⏳ WAVE 1: Audit & Orchestrare - 1/5 complete (LCAA 96/100 ✅, next: BLVA)

**Data start**: 11 Ianuarie 2025
**Ultima actualizare**: 12 Noiembrie 2025
**Timp investit până acum**: ~10 hours (Gandalf 2h + SCA 6h + LCAA 2h)

---

## Strategie de Creare

### Ordinea de Prioritate

Creăm agenții în **4 WAVE-uri**, prioritizând cei mai critici:

**WAVE 0 - META QUALITY (1 agent)** ⭐ CREAT PRIMUL!
- Gandalf 🧙‍♂️ - wizardul care evaluează TOȚI ceilalți agenți
- MUST be created FIRST - evaluează fiecare agent înainte să fie marcat DONE
- Standard: 95%+ pentru producție ("You shall not pass!")
- Motto: *"You shall not pass... unless you score 95%+"*

**WAVE 1 - AUDIT & ORCHESTRARE (5 agenți)** - Săptămâna 1
- Trebuie creați PRIMII pentru că blochează tot
- Fără aceștia, nu putem începe niciun fel de implementare
- Fiecare evaluat de Gandalf înainte de DONE

**WAVE 2 - BACKEND CORE (8 agenți)** - Săptămâna 2
- Backend-ul este fundația pentru frontend
- Fără API-uri, frontend-ul nu poate fi testat
- Fiecare evaluat de Gandalf înainte de DONE

**WAVE 3 - FRONTEND & QA (13 agenți)** - Săptămâna 3
- Depind de backend-ul finalizat
- QA poate rula în paralel cu development
- Fiecare evaluat de Gandalf înainte de DONE

---

## WAVE 0: META QUALITY (1 agent) ⭐ PRIORITATE ABSOLUTĂ

### 🔴 Agent 0: Gandalf - The Quality Wizard 🧙‍♂️

**Status**: ✅ DONE
**Prioritate**: META-CRITICAL (Primul creat!)
**Locație**: `.claude/agents/meta-quality/gandalf.md`
**Durată**: 60 minute (creare completă)
**Data finalizare**: 11 Ianuarie 2025

**Ce face**:
- Wizardul care păzește podul calității
- Evaluează FIECARE agent creat înainte să treacă
- Scorează pe 5 dimensiuni (Clarity, Completeness, Correctness, Actionability, Robustness)
- Standard: 95%+ pentru producție
- Battle cry: *"You shall not pass... unless you score 95%+"*
- Final guardian la podul către producție

**Framework de evaluare**:
- [ ] Clarity & Specificity (20%) - Zero ambiguități
- [ ] Completeness (25%) - Toate edge cases
- [ ] Correctness (25%) - Tehnic corect
- [ ] Actionability (15%) - Executabil autonom
- [ ] Robustness (15%) - Error handling complet

**Output**:
- Raport detaliat cu score per dimensiune
- Status: ✅ PRODUCTION READY (95+) | 🟡 CONDITIONAL (90-94) | 🔴 REJECT (<90)
- Liste puncte tari/slabe
- Blocker-e critice
- Recomandări îmbunătățire
- Verdic final: APPROVE / FIX / REJECT

**Dependențe**: Niciunul (primul agent creat!)

**Testare**: Va fi testat pe el însuși (meta-evaluation) și pe primul agent din WAVE 1

**Reguli CRITICE**:
- ❌ NICIUN agent nu poate fi marcat DONE fără evaluare Gandalf
- ❌ Score <95 = "You shall NOT pass!"
- ❌ Nu se trece la următorul agent până când cel curent are 95+
- ✅ Gandalf trebuie invocat după crearea FIECĂRUI agent
- 🧙‍♂️ Gandalf păzește podul cu toiagul său de putere

---

## Template Standard pentru Fiecare Agent

Pentru fiecare agent creăm:

```
📁 .claude/agents/{category}/{agent-name}.md

Structură fișier:
1. Header (Nume, Role, Activation)
2. STRICT RULES (MUST DO / MUST NOT DO)
3. Input Requirements
4. Output Format (cu exemple concrete)
5. Validation Checklist
6. Success Criteria
7. Examples (2-3 concrete)
8. Error Handling
```

---

## WAVE 0.5: REQUIREMENTS CLARITY (1 agent) ⭐ CRITICAL FOUNDATION

### 🔴 Agent 0.5: Story Clarity Agent (SCA)

**Status**: ✅ DONE (v2.2 - PRODUCTION READY)
**Prioritate**: CRITICAL (feeds all other agents)
**Locație**: `.claude/agents/requirements/story-clarity-agent.md`
**Durată totală**: 6 hours (creare + 2 iterations de repair)
**Data finalizare**: 12 Noiembrie 2025

**Final Score**: 🎯 **96/100** (APPROVED FOR PRODUCTION) ✅

**Evaluation History**:
- v1.0: 87/100 (REJECTED - 5 blockers: tool failure, scoring, multi-stakeholder, session persistence, quota)
- v2.0: +560 lines added (comprehensive fixes for all 5 blockers)
- v2.0 First Eval: 97/100 (APPROVED - but too lenient given agent criticality)
- v2.0 Ultra-Critical Re-Eval: 87/100 (NEEDS WORK - 8 new blockers found under maximum scrutiny)
- v2.1: 92/100 (CONDITIONAL APPROVAL - 8 blockers fixed, 5 new issues found)
- **v2.2**: **96/100** ✅ (PRODUCTION APPROVED - all 5 issues fixed)

**Quality Progression**: 87 → 87 → 92 → **96** (+9 points in 2 iterations)

**v2.2 Fixes (5 issues, +478 lines)**:
- ✅ **Issue 3 (MEDIUM)**: Added "Circuit Breaker Deployment Options" (+209 lines)
  - 3 deployment models: per-instance (simple), per-user (balanced), global (production)
  - Pros/cons, implementation examples, Redis code, monitoring requirements
- ✅ **Issue 4 (MEDIUM)**: Added "Alert Response Playbook" (+149 lines)
  - 10 detailed alerts with automated responses, manual actions, recovery times
  - Automation examples, Grafana queries, incident report template, severity definitions
- ✅ **Issue 5 (LOW)**: Fixed example notation consistency (× 20% → × 20 / 10)
- ✅ **Issue 1 (LOW)**: Added "Edge Case Selection Algorithm" (+96 lines)
  - Decision tree with 10 IF-THEN rules (DATE/TIME → timezone, EXTERNAL API → retry, etc.)
  - Example application: Zoom meeting story → 5 mandatory + 5 domain-specific = 10 edge cases
- ✅ **Circuit Breaker Scope**: Explicitly defined for all 3 deployment models

**Final Stats**:
- **Total lines**: 2,726 (started at 1,687 in v1.0)
- **Comprehensive coverage**: 10-dimension clarity scoring, 6 tool failure scenarios, circuit breaker, resource limits, multi-stakeholder conflicts, regression detection, alert playbook
- **Production readiness**: 100% (zero blockers, all ZERO-TOLERANCE rules passed)

**Ce face**:
- Clarifies EVERY user story to 100% clarity before implementation
- 10-dimension scoring: Actor, Action, Input, Output, Error Handling, Business Rules, Edge Cases, Acceptance, Dependencies, Technical
- Risk-weighted scoring (Error Handling 20%, Business Rules 15%, etc.)
- Multi-stakeholder conflict resolution protocol
- Session persistence with auto-save and resume
- Tool failure resilience (6 scenarios: timeout, disconnect, error, fallback, unavailable, partial)
- Circuit breaker pattern (3 deployment models: per-instance, per-user, global)
- Resource limits with alert playbook (10 alerts with automated responses)
- Iterative Q&A until score = 100/100 (max 5 iterations, then escalate to CAA)

**Why CRITICAL**:
- Feeds requirements to ALL 26 implementation agents
- Any ambiguity cascades catastrophically through 4.5-month migration
- Standard bar: 95%+ for production (achieved 96%)
- One unclear requirement → multiple agents implement differently → rework

**Gandalf's Verdict**:
> *"You shall pass... and you did."*
>
> Story Clarity Agent v2.2 is **production-ready** as the requirements gatekeeper for the €500K+ Somaway migration. All 27 downstream agents can now depend on it.

**Dependențe**: Gandalf (for evaluation), Chief Architect Agent (for escalations)
**Evaluation Report**: `.claude/evaluations/story-clarity-agent-evaluation-v2.2-20251112-154004.md`

---

## WAVE 1: AUDIT & ORCHESTRARE (5 agenți) ⭐ PRIORITATE CRITICĂ

### 🔴 Agent 1: Legacy Code Auditor Agent (LCAA)

**Status**: ✅ DONE (v2.0 - PRODUCTION READY)
**Prioritate**: CRITICAL
**Locație**: `.claude/agents/audit/legacy-code-auditor.md`
**Durată totală**: ~2 hours (creare + 1 iteration de repair)
**Data finalizare**: 11 Ianuarie 2025

**Final Score**: 🎯 **96/100** (APPROVED FOR PRODUCTION) ✅

**Evaluation History**:
- v1.0: Score unknown (REJECTED - 5 blockers: timeout, verification, scope, TypeScript, madge)
- v2.0: 96/100 ✅ (PRODUCTION APPROVED - all 5 blockers fixed)

**Score Breakdown (v2.0)**:
- Clarity & Specificity: 97/100 (20%)
- Completeness: 96/100 (25%)
- Correctness: 95/100 (25%)
- Actionability: 96/100 (15%)
- Robustness: 95/100 (15%)

**v2.0 Fixes**:
- ✅ Added 120-minute timeout protection
- ✅ Added autonomous verification algorithm (3-step confidence scoring)
- ✅ Added file inclusion rules (72+ patterns, INCLUDE/EXCLUDE logic)
- ✅ Added TypeScript pre-check (compilation + dependency graph)
- ✅ Added madge tool integration (circular dependencies detection)

**Ce face**:
- Scanează cod vechi (Node.js/NestJS/React/Next.js) pentru bug-uri
- Detectează 6 categorii: anti-patterns, race conditions, memory leaks, logic errors, error handling gaps, type safety issues
- Generează raport Markdown cu categorizare CRITICAL/MEDIUM/LOW
- Pre-audit validation: TypeScript compilation + dependency graph
- Autonomous verification cu confidence scoring
- Integrare cu BLVA, SVSA, CAA

**Coverage**:
- 72+ file patterns (include/exclude)
- 6 error scenarios handled
- 4 edge cases covered (large codebases, third-party libs, generated code, test files)
- 14-section Markdown report
- Validation checklist cu 8 criterii

**Gandalf's Verdict**:
> *"Exceptionally well-crafted agent that demonstrates production-grade quality across all evaluation dimensions. Fully autonomous, technically sound, and ready for production use."*

**Dependențe**: Niciunul (primul agent din TIER 0!)
**Evaluation Report**: `.claude/evaluations/lcaa-v2-evaluation-20251111-234915.md`

---

### 🔴 Agent 2: Business Logic Validator Agent (BLVA)

**Status**: ⏳ TO DO
**Prioritate**: CRITICAL
**Locație**: `.claude/agents/audit/business-logic-validator.md`
**Durată estimată**: 40 minute

**Ce face**:
- Compară cod vechi cu documentația JIRA
- Validează că implementarea respectă specificațiile
- Identifică edge cases neacoperite

**Instrucțiuni cheie de definit**:
- [ ] Cum citește și parsează fișierele JIRA
- [ ] Algoritm de comparare cod vs specs
- [ ] Liste de edge cases comune (null, empty, timezone, etc.)
- [ ] Format raport discrepanțe
- [ ] Validări pentru calcule business critice (Stripe, subscriptions)
- [ ] Exemple de inconsistențe găsite

**Dependențe**: LCAA (folosește partea de scanare)
**Testare**: Pe modul Auth cu specs JIRA cunoscute

---

### 🔴 Agent 3: Security Vulnerability Scanner Agent (SVSA)

**Status**: ⏳ TO DO
**Prioritate**: CRITICAL
**Locație**: `.claude/agents/audit/security-vulnerability-scanner.md`
**Durată estimată**: 50 minute

**Ce face**:
- Scanează OWASP Top 10 vulnerabilities
- Detectează credentials hardcodate, API keys
- Identifică SQL injection, XSS, CSRF potential

**Instrucțiuni cheie de definit**:
- [ ] Checklist OWASP Top 10 complet
- [ ] Patterns pentru hardcoded secrets (regex)
- [ ] Validări JWT și token management
- [ ] Detectare SQL injection patterns
- [ ] Verificare CORS și rate limiting
- [ ] Format raport vulnerabilități cu severity scoring (CVSS)

**Dependențe**: LCAA (bază de scanare)
**Testare**: Pe cod cu vulnerabilități cunoscute

---

### 🟡 Agent 4: Chief Architect Agent (CAA)

**Status**: ⏳ TO DO
**Prioritate**: HIGH
**Locație**: `.claude/agents/orchestration/chief-architect.md`
**Durată estimată**: 60 minute

**Ce face**:
- Orchestrează toți ceilalți agenți
- Ia decizii arhitecturale
- Rezolvă conflicte între implementări

**Instrucțiuni cheie de definit**:
- [ ] Framework de luare decizii (când alege .NET patterns)
- [ ] Proces de rezolvare conflicte între agenți
- [ ] Criterii pentru aprobare/rejecție soluții
- [ ] Template review arhitectural
- [ ] Protocol comunicare cu ceilalți agenți
- [ ] Raportare către Project Manager Agent

**Dependențe**: Niciuna (orchestrator de top-level)
**Testare**: Simulare conflict între 2 agenți mock

---

### 🟡 Agent 5: Project Manager Agent (PMA)

**Status**: ⏳ TO DO
**Prioritate**: HIGH
**Locație**: `.claude/agents/orchestration/project-manager.md`
**Durată estimată**: 45 minute

**Ce face**:
- Trackează progres module (26+)
- Gestionează dependențe între tasks
- Raportează status și blockers

**Instrucțiuni cheie de definit**:
- [ ] Format tracking progress (Kanban/Gantt style)
- [ ] Algoritm detectare dependențe
- [ ] Template rapoarte status (daily/weekly)
- [ ] Criterii identificare blockers
- [ ] Metrici de urmărit (velocity, completion rate)
- [ ] Escalation protocol către stakeholderi

**Dependențe**: CAA (pentru decizii strategice)
**Testare**: Tracking pe 5 module fictive

---

## WAVE 2: BACKEND CORE (8 agenți)

### 🟢 Agent 6: Backend Migration Architect (BMA)

**Status**: ⏳ TO DO
**Prioritate**: HIGH
**Locație**: `.claude/agents/backend/backend-migration-architect.md`
**Durată estimată**: 50 minute

**Ce face**:
- Convertește NestJS → .NET Core architecture
- Mapează decoratori TypeScript la atribute .NET
- Asigură compatibilitate API contracts

**Instrucțiuni cheie de definit**:
- [ ] Mapping table: NestJS decorators → .NET attributes
- [ ] Pattern-uri pentru middleware NestJS → .NET middleware
- [ ] Structură folder .NET solution (Controllers, Services, etc.)
- [ ] Naming conventions .NET vs TypeScript
- [ ] API versioning strategy
- [ ] Dependency injection NestJS → .NET DI

**Dependențe**: LCAA (audit backend existent)
**Testare**: Conversie modul Auth complet

---

### 🟢 Agent 7: Authentication & Security Agent (ASA)

**Status**: ⏳ TO DO
**Prioritate**: CRITICAL
**Locație**: `.claude/agents/backend/authentication-security.md`
**Durată estimată**: 55 minute

**Ce face**:
- Implementează 4 tipuri JWT tokens
- Role-based authorization
- Password hashing Argon2

**Instrucțiuni cheie de definit**:
- [ ] Schema JWT pentru cele 4 token types
- [ ] Implementare Argon2 în .NET (Konscious.Security.Cryptography)
- [ ] Middleware order (authn → authz → rate limiting)
- [ ] Token refresh flow complet
- [ ] Rate limiting configuration (20,000 req/60s)
- [ ] CORS policy strict (nu origin: '*')

**Dependențe**: BMA (structură backend)
**Testare**: Auth flow complet (signin → refresh → validate)

---

### 🟢 Agent 8: Payment Integration Agent (PIA)

**Status**: ⏳ TO DO
**Prioritate**: HIGH
**Locație**: `.claude/agents/backend/payment-integration.md`
**Durată estimată**: 60 minute

**Ce face**:
- Integrează Stripe API (11 metode)
- Subscription scheduling (AA1, AA2, BB)
- Webhook handling securizat

**Instrucțiuni cheie de definit**:
- [ ] Stripe API wrapper în .NET (Stripe.net SDK)
- [ ] Implementare webhook signature validation
- [ ] Scenarii subscription scheduling detailate
- [ ] SmartBill integration pentru facturi RON
- [ ] Error handling Stripe errors (card declined, etc.)
- [ ] Idempotency keys pentru retry safety

**Dependențe**: ASA (auth pentru API calls), DEA (entities)
**Testare**: Flow complet Stripe test mode

---

### 🟢 Agent 9: Video & Live Services Agent (VLSA)

**Status**: ⏳ TO DO
**Prioritate**: MEDIUM
**Locație**: `.claude/agents/backend/video-live-services.md`
**Durată estimată**: 50 minute

**Ce face**:
- Vimeo OAuth 2.0 integration
- Zoom SDK pentru meetings/webinars
- Video upload pipeline

**Instrucțiuni cheie de definit**:
- [ ] Vimeo OAuth flow în .NET
- [ ] Video upload chunking strategy (large files)
- [ ] Zoom JWT generation pentru SDK
- [ ] Webhook handling pentru Vimeo/Zoom events
- [ ] Video encoding status polling
- [ ] Error handling (quota exceeded, upload failed)

**Dependențe**: ASA (auth), DEA (Course/Lesson entities)
**Testare**: Upload video test + create Zoom meeting

---

### 🟢 Agent 10: Email & Marketing Agent (EMA)

**Status**: ⏳ TO DO
**Prioritate**: MEDIUM
**Locație**: `.claude/agents/backend/email-marketing.md`
**Durată estimată**: 40 minute

**Ce face**:
- Postmark transactional emails
- MailerLite marketing automation
- Email template management

**Instrucțiuni cheie de definit**:
- [ ] Postmark API integration (.NET client)
- [ ] Email templates în HTML (Razor views)
- [ ] MailerLite API pentru campaigns
- [ ] Queue system pentru email batches
- [ ] Tracking email delivery/opens (Postmark webhooks)
- [ ] Unsubscribe link management

**Dependențe**: ASA (auth), DEA (User entity)
**Testare**: Send test email prin Postmark

---

### 🟢 Agent 11: Database & Entity Agent (DEA)

**Status**: ⏳ TO DO
**Prioritate**: CRITICAL
**Locație**: `.claude/agents/backend/database-entity.md`
**Durată estimată**: 60 minute

**Ce face**:
- Migrează 20+ entities TypeORM → EF Core
- Configurează relationships și indexuri
- Database migrations

**Instrucțiuni cheie de definit**:
- [ ] Mapping TypeORM decorators → EF Core annotations
- [ ] Relationship patterns (OneToMany, ManyToMany)
- [ ] Index strategy pentru performance
- [ ] Migration naming conventions
- [ ] Seeding data strategy
- [ ] Query optimization patterns (Include, ThenInclude)

**Dependențe**: BMA (structură .NET)
**Testare**: Creare entities + migration pentru User, Course

---

### 🟢 Agent 12: Analytics & Reporting Agent (ARA)

**Status**: ⏳ TO DO
**Prioritate**: MEDIUM
**Locație**: `.claude/agents/backend/analytics-reporting.md`
**Durată estimată**: 45 minute

**Ce face**:
- Analytics tracking (VIEW_COURSE, VIEW_LESSON, TIME_SPENT)
- Dashboard statistics
- Cron jobs pentru agregare

**Instrucțiuni cheie de definit**:
- [ ] Schema analytics events
- [ ] Aggregation queries pentru dashboard
- [ ] Hangfire/Quartz.NET pentru cron jobs
- [ ] Performance optimization (materialized views)
- [ ] Data retention policy
- [ ] Export rapoarte (CSV, Excel)

**Dependențe**: DEA (Analytics entities)
**Testare**: Track events + generat raport

---

### 🟢 Agent 13: API Testing & Documentation Agent (ATDA)

**Status**: ⏳ TO DO
**Prioritate**: HIGH
**Locație**: `.claude/agents/backend/api-testing-documentation.md`
**Durată estimată**: 50 minute

**Ce face**:
- xUnit/NUnit tests pentru controllers
- Integration tests
- Swagger/OpenAPI documentation

**Instrucțiuni cheie de definit**:
- [ ] Test structure (unit vs integration vs E2E)
- [ ] Mock setup pentru dependencies
- [ ] Test data builders pattern
- [ ] Swagger annotations pentru endpoints
- [ ] Postman collection generation
- [ ] Code coverage target (>70%)

**Dependențe**: Toți agenții backend (testează tot)
**Testare**: Test suite pentru Auth module

---

## WAVE 3: FRONTEND & QA (13 agenți)

### 🔵 Agent 14: Admin Dashboard Migration Agent (ADMA)

**Status**: ⏳ TO DO
**Prioritate**: HIGH
**Locație**: `.claude/agents/frontend/admin-dashboard-migration.md`
**Durată estimată**: 55 minute

**Ce face**:
- React 18 → Vue 3 pentru 7 pagini admin
- Redux → Pinia migration
- Ant Design → Ant Design Vue

**Instrucțiuni cheie de definit**:
- [ ] Mapping React hooks → Vue Composition API
- [ ] Redux patterns → Pinia patterns
- [ ] Component lifecycle React → Vue
- [ ] Form handling Ant Design → Ant Design Vue
- [ ] Table pagination patterns
- [ ] State persistence localStorage → Pinia persist

**Dependențe**: Agenții backend (API contracts)
**Testare**: Migrare pagina Users completă

---

### 🔵 Agent 15: Web Client Migration Agent (WCMA)

**Status**: ⏳ TO DO
**Prioritate**: HIGH
**Locație**: `.claude/agents/frontend/web-client-migration.md`
**Durată estimată**: 60 minute

**Ce face**:
- Next.js 15 → Nuxt 3 pentru 21 pagini
- Pages Router → file-based routing
- SSR/CSR strategy

**Instrucțiuni cheie de definit**:
- [ ] Next.js patterns → Nuxt 3 patterns
- [ ] getServerSideProps → Nuxt server API
- [ ] Image optimization Next → Nuxt
- [ ] SEO meta tags management
- [ ] Dynamic routing patterns
- [ ] API routes migration

**Dependențe**: Agenții backend (API contracts)
**Testare**: Migrare pagina Courses

---

### 🔵 Agent 16: Authentication UI Agent (AUIA)

**Status**: ⏳ TO DO
**Prioritate**: HIGH
**Locație**: `.claude/agents/frontend/authentication-ui.md`
**Durată estimată**: 45 minute

**Ce face**:
- Pagini Sign In/Sign Up/Password Recovery
- Form validation
- Session management frontend

**Instrucțiuni cheie de definit**:
- [ ] Form validation patterns (Vuelidate/VeeValidate)
- [ ] Token storage (cookies vs localStorage)
- [ ] Auto-redirect logic authenticated users
- [ ] Multi-step forms (registration flow)
- [ ] Error messages user-friendly
- [ ] Remember me functionality

**Dependențe**: ASA (backend auth), WCMA/ADMA (structure)
**Testare**: Complete auth flow user journey

---

### 🔵 Agent 17: Course & Video Player Agent (CVPA)

**Status**: ⏳ TO DO
**Prioritate**: MEDIUM
**Locație**: `.claude/agents/frontend/course-video-player.md`
**Durată estimată**: 50 minute

**Ce face**:
- Course catalog cu filters
- Vimeo player integration
- Video analytics tracking

**Instrucțiuni cheie de definit**:
- [ ] Vimeo player component Vue 3
- [ ] Video playback analytics tracking
- [ ] Course filters (category, price, rating)
- [ ] Materials download UI
- [ ] Voting/rating system UI
- [ ] Progress tracking visual

**Dependențe**: VLSA (backend video), WCMA (structure)
**Testare**: Player video + tracking events

---

### 🔵 Agent 18: Subscription & Payment UI Agent (SPUA)

**Status**: ⏳ TO DO
**Prioritate**: HIGH
**Locație**: `.claude/agents/frontend/subscription-payment-ui.md`
**Durată estimată**: 55 minute

**Ce face**:
- Stripe Elements integration
- Payment flow UI
- Billing address forms

**Instrucțiuni cheie de definit**:
- [ ] Stripe Elements Vue 3 integration
- [ ] Payment form validation
- [ ] 3D Secure handling
- [ ] Success/failure pages
- [ ] Campaign-based pricing display
- [ ] Romanian billing address validation

**Dependențe**: PIA (backend payments), WCMA (structure)
**Testare**: Complete payment flow (test cards)

---

### 🔵 Agent 19: Dashboard & Profile Agent (DPA)

**Status**: ⏳ TO DO
**Prioritate**: MEDIUM
**Locație**: `.claude/agents/frontend/dashboard-profile.md`
**Durată estimată**: 45 minute

**Ce face**:
- User dashboard cu statistics
- Profile edit pages
- Avatar upload

**Instrucțiuni cheie de definit**:
- [ ] Avatar upload component (crop/resize)
- [ ] Statistics cards layout
- [ ] Profile form validation
- [ ] Subscription display active/inactive
- [ ] Live sessions calendar integration
- [ ] Invoice download links

**Dependențe**: ARA (analytics), WCMA (structure)
**Testare**: Dashboard load + profile edit

---

### 🔵 Agent 20: Shared Components Agent (SCA)

**Status**: ⏳ TO DO
**Prioritate**: HIGH
**Locație**: `.claude/agents/frontend/shared-components.md`
**Durată estimată**: 50 minute

**Ce face**:
- Layout components (Header, Footer, Sidebar)
- Form components reusable
- Design system consistency

**Instrucțiuni cheie de definit**:
- [ ] Component library structure
- [ ] Props interface standards
- [ ] Event emitting patterns
- [ ] Slot usage guidelines
- [ ] Styling approach (scoped vs global)
- [ ] Storybook setup (optional)

**Dependențe**: WCMA, ADMA (need structure first)
**Testare**: Use component în 3 pages diferite

---

### 🟣 Agent 21: Testing Automation Agent (TAA)

**Status**: ⏳ TO DO
**Prioritate**: HIGH
**Locație**: `.claude/agents/qa/testing-automation.md`
**Durată estimată**: 60 minute

**Ce face**:
- Playwright/Cypress E2E tests
- Cross-browser testing
- Accessibility testing WCAG 2.1

**Instrucțiuni cheie de definit**:
- [ ] Test structure (Page Object Model)
- [ ] Critical flows priority (auth, payment, video)
- [ ] Cross-browser matrix (Chrome, Firefox, Safari)
- [ ] Mobile responsive tests
- [ ] Accessibility checks (axe-core)
- [ ] CI/CD integration

**Dependențe**: Toți agenții (testează totul)
**Testare**: E2E test pentru auth flow

---

### 🟣 Agent 22: Performance Optimization Agent (POA)

**Status**: ⏳ TO DO
**Prioritate**: MEDIUM
**Locație**: `.claude/agents/qa/performance-optimization.md`
**Durată estimată**: 50 minute

**Ce face**:
- Lighthouse score >90
- Bundle size optimization
- Core Web Vitals

**Instrucțiuni cheie de definit**:
- [ ] Lighthouse audit checklist
- [ ] Bundle analyzer setup
- [ ] Code splitting strategy
- [ ] Image optimization (WebP, lazy load)
- [ ] Caching headers configuration
- [ ] Performance budget enforcement

**Dependențe**: Frontend agenți (optimizează after build)
**Testare**: Lighthouse audit pe 5 pages

---

### 🟣 Agent 23: DevOps & CI/CD Agent (DCA)

**Status**: ⏳ TO DO
**Prioritate**: HIGH
**Locație**: `.claude/agents/devops/cicd-deployment.md`
**Durată estimată**: 60 minute

**Ce face**:
- GitHub Actions pipelines
- Docker containerization
- Deployment automation

**Instrucțiuni cheie de definit**:
- [ ] GitHub Actions workflow structure
- [ ] Dockerfile pentru backend .NET
- [ ] Dockerfile pentru frontend Nuxt
- [ ] Environment variables management
- [ ] Database migrations în CD pipeline
- [ ] Rollback strategy

**Dependențe**: Toți agenții (deployează totul)
**Testare**: Deploy pe staging environment

---

### 🟣 Agent 24: Documentation Agent (DA)

**Status**: ⏳ TO DO
**Prioritate**: MEDIUM
**Locație**: `.claude/agents/documentation/documentation-generator.md`
**Durată estimată**: 40 minute

**Ce face**:
- API documentation Swagger
- Component documentation
- README files

**Instrucțiuni cheie de definit**:
- [ ] Swagger annotations standards
- [ ] Component documentation template
- [ ] README structure (per-repo)
- [ ] Architecture diagrams (C4 model)
- [ ] Onboarding guide structure
- [ ] Changelog maintenance

**Dependențe**: Toți agenții (documentează totul)
**Testare**: Generate docs pentru Auth module

---

### 🟣 Agent 25: Migration Validator Agent (MVA)

**Status**: ⏳ TO DO
**Prioritate**: HIGH
**Locație**: `.claude/agents/validation/migration-validator.md`
**Durată estimată**: 50 minute

**Ce face**:
- Compară React vs Vue implementations
- Validează API contracts
- Regression testing

**Instrucțiuni cheie de definit**:
- [ ] Side-by-side comparison strategy
- [ ] API contract validation rules
- [ ] Behavior equivalence checks
- [ ] Data flow verification
- [ ] Performance comparison benchmarks
- [ ] Regression test suite

**Dependențe**: Frontend + Backend agenți
**Testare**: Validate Auth migration

---

### 🟣 Agent 26: Security Audit Agent (SAA)

**Status**: ⏳ TO DO
**Prioritate**: HIGH
**Locație**: `.claude/agents/security/security-audit.md`
**Durată estimată**: 55 minute

**Ce face**:
- OWASP Top 10 post-migration
- Dependency scanning
- Penetration testing

**Instrucțiuni cheie de definit**:
- [ ] OWASP checklist pentru .NET + Vue
- [ ] Dependency scanner setup (Snyk, OWASP Dependency-Check)
- [ ] Security headers validation
- [ ] Penetration testing scenarios
- [ ] Secret scanning în git history
- [ ] Security report template

**Dependențe**: Toți agenții (auditează totul)
**Testare**: Security audit pe Auth + Payment modules

---

## Tracking & Metrics

### Progress Overview

| Wave | Total | Creați | %   | Status |
|------|-------|--------|-----|--------|
| WAVE 0 (Meta Quality) | 1 | 1 | 100% | ✅ |
| WAVE 1 (Audit & Orchestrare) | 5 | 0 | 0%  | ⏳ |
| WAVE 2 (Backend Core) | 8 | 0 | 0%  | ⏳ |
| WAVE 3 (Frontend & QA) | 13 | 0 | 0%  | ⏳ |
| **TOTAL** | **27** | **1** | **3.7%** | ⏳ |

### Time Estimates

| Wave | Timp estimat | Timp real | Status |
|------|--------------|-----------|--------|
| WAVE 0 | ~1 oră | 1 oră | ✅ |
| WAVE 1 | ~4 ore | - | ⏳ |
| WAVE 2 | ~7 ore | - | ⏳ |
| WAVE 3 | ~11 ore | - | ⏳ |
| **TOTAL** | **~23 ore** | **1 oră** | ⏳ |

---

## Process de Creare pentru Fiecare Agent

### Pas 1: Discuție & Design (15-20 min)
- Analizăm ce face agentul
- Definim instrucțiuni MUST DO / MUST NOT DO
- Stabilim format input/output
- Alegem exemple concrete

### Pas 2: Creare Fișier Agent (20-30 min)
- Scriem fișierul `.md` complet
- Includem toate secțiunile
- Adăugăm exemple și validări

### Pas 3: Review & Validare (10-15 min)
- Verificăm completitudine
- Testăm pe un caz simplu
- Ajustăm dacă e nevoie

### Pas 4: Update Tracking (2 min)
- Marcăm agent ca finalizat în acest fișier
- Actualizăm progress percentage
- Comitem în git

**Timp total per agent**: ~45-60 minute

---

## Regulă de Update

**DUPĂ FIECARE AGENT CREAT**:
1. Schimbă status din `⏳ TO DO` în `✅ DONE`
2. Adaugă data finalizării
3. Adaugă link către fișierul agentului
4. Actualizează Progress Overview
5. Comit în git cu mesaj descriptiv

---

## Notes & Observații

- Unii agenți sunt mai complecși (60 min) vs altii mai simpli (40 min)
- WAVE 1 este CRITICĂ - fără ea nu putem testa ceilalți
- Backend (WAVE 2) trebuie terminat înainte de Frontend (WAVE 3)
- Testarea fiecărui agent este OBLIGATORIE

---

**Ultimă actualizare**: 11 Ianuarie 2025
**Versiune document**: 1.0
**Status**: Plan inițial - ready to start!
