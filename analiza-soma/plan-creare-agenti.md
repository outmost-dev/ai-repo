# PLAN CREARE AGENȚI AI - PROIECT SOMAWAY (OPTIMIZAT)

## Prezentare Generală

Acest document trackează procesul de creare a tuturor cei **15 agenți AI** necesari pentru migrarea platformei Somaway (arhitectură optimizată de la 27→15 agenți, **-44% complexitate**).

**Status general**: 8/15 agenți approved (53.3%) + 1 awaiting re-evaluation
- ✅ WAVE 0: Meta Quality - 1/1 complete (Gandalf 99/100)
- ✅ WAVE 0.5: Requirements - 1/1 complete (SCA 96/100)
- ✅ TIER 0: Audit - 3/3 complete (LCAA 96/100, BLVA 96/100, SVSA 95/100)
- ✅ TIER 1: Orchestration - 1/1 complete (CAA 95.2/100)
- ⏳ TIER 2: Backend - 3/5 created (BMA 97/100 ✅, PIA 96/100 ✅, ASA v2.0 🟡 PENDING RE-EVAL, 2 TO DO)
- ⏳ TIER 3: Frontend - 0/2 (TO DO)
- ⏳ TIER 4: QA & DevOps - 0/2 (TO DO)

**Data start**: 11 Ianuarie 2025
**Ultima actualizare**: 13 Noiembrie 2025 (ASA v2.0 fixes completed)
**Timp investit până acum**: ~19.2 hours (includes ASA v2.0 fixes: +2.5h)
**Timp estimat rămas**: ~8.0 hours (vs 17h în arhitectura veche)

---

## 🎯 DE CE 15 AGENȚI (NU 27)?

### Analiza Critică a Arhitecturii Vechi:
După crearea primilor 9 agenți, am descoperit că:
- **PMA redundant**: CAA poate prelua orchestrare + timeline tracking
- **Frontend fragmentat**: 7 agenți pentru pattern-uri identice (React→Vue)
- **Backend over-specialized**: VLSA, EMA, ARA pot fi consolidați (integrări externe)
- **QA duplicat**: SAA redundant cu SVSA, TAA/MVA/POA pot fi un singur agent

### Beneficii Arhitectură Optimizată:
- ✅ **-44% complexitate** (15 vs 27 agenți)
- ✅ **-40% timp implementare** (~20h vs ~32h)
- ✅ **Consistență crescută** (2 frontend agents vs 7)
- ✅ **Mai puține handoff-uri** între agenți
- ✅ **Orchestrare simplificată** (CAA gestionează 15 vs 27)

---

## Strategie de Creare

### Ordinea de Prioritate

Creăm agenții în **4 TIERS**, prioritizând cei mai critici:

**WAVE 0 - META QUALITY (1 agent)** ⭐ CREAT PRIMUL!
- Gandalf 🧙‍♂️ - evaluează TOȚI ceilalți agenți
- Standard: 95%+ pentru producție

**WAVE 0.5 - REQUIREMENTS CLARITY (1 agent)** ⭐ CRITICAL FOUNDATION
- SCA - clarificare cerințe 100% înainte de implementare

**TIER 0 - AUDIT (3 agenți)** - MANDATORY FIRST
- Audit-First Strategy: scană bug-uri ÎN codul vechi
- GATE: Nu migrăm până când auditul nu e complet

**TIER 1 - ORCHESTRATION (1 agent)** - Coordonează totul
- CAA - Chief Architect (preluează și responsabilități PM)

**TIER 2 - BACKEND (5 agenți)** - Fundație
- Backend-ul trebuie gata pentru frontend

**TIER 3 - FRONTEND (2 agenți)** - Consolidați
- Admin Dashboard + Web Client (pattern-uri omogene)

**TIER 4 - QA & DEVOPS (2 agenți)** - Validare finală
- Testing + deployment automation

---

## WAVE 0: META QUALITY (1 agent) ⭐

### 🔴 Agent 0: Gandalf - The Quality Wizard 🧙‍♂️

**Status**: ✅ DONE (v5.0)
**Score**: 🎯 **99/100** (HIGHEST SCORE - META)
**Locație**: `.claude/agents/meta-quality/gandalf.md`
**Durată**: 2 hours (creare + self-evaluation)
**Data finalizare**: 11 Ianuarie 2025

**Ce face**:
- Evaluează FIECARE agent pe 5 dimensiuni (Clarity, Completeness, Correctness, Actionability, Robustness)
- Battle cry: *"You shall not pass... unless you score 95%+"*
- Threshold: 95%+ pentru producție (el însuși la 99%)
- Final guardian pentru calitate

**Framework**:
- Clarity & Specificity (20%)
- Completeness (25%)
- Correctness (25%)
- Actionability (15%)
- Robustness (15%)

**Output**: Raport detaliat cu score, blockers, recommendations

**Evaluation Report**: `.claude/evaluations/gandalf-evaluation-v5-20250111-170000.md`

---

## WAVE 0.5: REQUIREMENTS CLARITY (1 agent) ⭐

### 🔴 Agent 0.5: Story Clarity Agent (SCA)

**Status**: ✅ DONE (v2.2 - PRODUCTION READY)
**Score**: 🎯 **96/100** (APPROVED)
**Locație**: `.claude/agents/requirements/story-clarity-agent.md`
**Durată totală**: 6 hours (4 iterations)
**Data finalizare**: 12 Noiembrie 2025

**Evolution**: 87 → 87 → 92 → **96** (+9 points)

**Ce face**:
- Clarificare 100% a fiecărei user story înainte de implementare
- 10-dimension scoring (Actor, Action, Input, Output, Error Handling, Business Rules, Edge Cases, etc.)
- Iterative Q&A până la 100/100 clarity (max 5 iterations)
- Multi-stakeholder conflict resolution
- Circuit breaker pattern (3 deployment models)

**Why CRITICAL**: Orice ambiguitate → 27 agenți implementează diferit → catastrofă

**Gandalf's Verdict**: *"You shall pass... and you did."*

**Evaluation Report**: `.claude/evaluations/story-clarity-agent-evaluation-v2.2-20251112-154004.md`

---

## TIER 0: PRE-MIGRATION AUDIT (3 agenți) ⭐ AUDIT-FIRST STRATEGY

### 🔴 Agent 1: Legacy Code Auditor Agent (LCAA)

**Status**: ✅ DONE (v2.0 - PRODUCTION READY)
**Score**: 🎯 **96/100** (APPROVED)
**Locație**: `.claude/agents/audit/legacy-code-auditor.md`
**Durată totală**: ~2 hours
**Data finalizare**: 11 Ianuarie 2025

**Ce face**:
- Scanează cod vechi (Node.js/NestJS/React/Next.js) pentru bug-uri
- 6 categorii: anti-patterns, race conditions, memory leaks, logic errors, error handling gaps, type safety
- Pre-audit validation: TypeScript compilation + dependency graph
- Autonomous verification cu confidence scoring
- 72+ file patterns coverage

**Raport**: 14 secțiuni Markdown cu CRITICAL/MEDIUM/LOW bugs

**Gandalf's Verdict**: *"Exceptionally well-crafted, production-grade quality."*

**Evaluation Report**: `.claude/evaluations/lcaa-v2-evaluation-20251111-234915.md`

---

### 🔴 Agent 2: Business Logic Validator Agent (BLVA)

**Status**: ✅ DONE (v1.0 - PRODUCTION READY)
**Score**: 🎯 **96/100** (APPROVED) - **Correctness: 25/25 (100%)** ⭐
**Locație**: `.claude/agents/audit/business-logic-validator.md`
**Durată totală**: ~2 hours
**Data finalizare**: 12 Noiembrie 2025

**Ce face**:
- Compară cod vechi cu documentația JIRA (37 fișiere)
- 7-dimensional validation: business logic, edge cases, data flow, integrations, errors, state, calculations
- **400-line example report template** (GOLD STANDARD)
- Somaway-specific: Stripe subscriptions, JWT tokens, analytics

**Complementary**: LCAA → technical bugs, BLVA → business logic bugs

**Gandalf's Verdict**: *"EXCEPTIONAL quality. 400-line example is a masterclass. Together with LCAA, unstoppable duo."*

**Evaluation Report**: `.claude/evaluations/blva-evaluation-20251112-204513.md`

---

### 🔴 Agent 3: Security Vulnerability Scanner Agent (SVSA)

**Status**: ✅ DONE (v1.0 - PRODUCTION READY)
**Score**: 🎯 **95/100** (APPROVED - at threshold)
**Locație**: `.claude/agents/audit/security-vulnerability-scanner.md`
**Durată totală**: ~50 minutes
**Data finalizare**: 12 Noiembrie 2025

**Ce face**:
- OWASP Top 10 (2021) - toate cele 10 categorii cu detection patterns + exploits + remediation
- Hardcoded secrets (regex + entropy analysis + git history)
- JWT security (4 token types: Access, Refresh, Email Validation, Subscription Validation)
- SQL/NoSQL/Command injection, XSS, CSRF detection
- CORS configuration + rate limiting validation
- Webhook signature validation (Stripe, Vimeo, Zoom)
- CVSS v3.1 scoring + business impact (€)

**7-phase autonomous execution**: Pre-scan → OWASP → Secrets → JWT → CORS → Verification → Report (118 min)

**Audit Trinity Complete**: LCAA (technical) + BLVA (business) + SVSA (security)

**Gandalf's Verdict**: *"Top 1% of security scanners. You form the Audit Trinity."*

**Evaluation Report**: `.claude/evaluations/svsa-evaluation-20251112-221606.md`

---

## TIER 1: ORCHESTRATION (1 agent) - PMA ELIMINAT ✂️

### 🟢 Agent 4: Chief Architect Agent (CAA)

**Status**: ✅ DONE (v1.0 - PRODUCTION READY)
**Score**: 🎯 **95.2/100** (APPROVED)
**Locație**: `.claude/agents/orchestration/chief-architect.md`
**Durată totală**: ~25 minutes
**Data finalizare**: 12 Noiembrie 2025

**Ce face**:
- Master orchestrator pentru toți cei 14 agenți
- Ia decizii arhitecturale finale (FINAL SAY)
- Rezolvă conflicte evidence-based
- **PRELUEAZĂ RESPONSABILITĂȚI PM**: timeline tracking, blocker escalation, resource allocation
- Weighted scoring: Business Value 30%, Cost 20%, Timeline 20%, Risk 15%, Maintainability 10%, Scalability 5%
- Escalation chain: CAA → CTO → CFO → CEO

**Features**:
- 1,219 lines orchestration logic
- 4-phase decision framework
- Technology stack expertise (NestJS→.NET, React→Vue mapping tables)
- **Correctness: 24.5/25 (98%)** ⭐
- Budget €500K + timeline 18 săptămâni management

**DE CE PMA ELIMINAT**:
- ❌ PMA avea 97/100 dar multe responsabilități se suprapuneau cu CAA
- ✅ CAA poate gestiona timeline, dependencies, blockers pentru proiect 18 săptămâni
- ✅ Simplificare: 1 orchestrator vs 2
- ✅ Decizii coerente (CAA ia decizii + trackează execuția)

**Gandalf's Verdict**: *"I'd trust you with €500K+ decisions. One of the highest-quality orchestrator agents."*

**Evaluation Report**: `.claude/evaluations/caa-evaluation-20251112-230000.md`

---

## TIER 2: BACKEND (5 agenți) - Consolidat de la 8

### 🟢 Agent 5: Backend Migration Architect (BMA)

**Status**: ✅ DONE (v1.0 - PRODUCTION READY)
**Score**: 🎯 **97/100** (APPROVED) - **🏆 HIGHEST IMPLEMENTATION AGENT SCORE**
**Locație**: `.claude/agents/backend/backend-migration-architect.md`
**Durată totală**: ~25 minutes
**Data finalizare**: 12 Noiembrie 2025

**Ce face**:
- Convertește NestJS → .NET Core cu 10-phase autonomous workflow (80-130 min/module)
- **7 comprehensive mapping tables**: decorators, TypeORM, guards, interceptors, pipes, exceptions, DI
- **1,200+ line example migration report** (gold standard)
- Preserves API contracts exactly (zero breaking changes)
- Integrates cu Audit Trinity (LCAA, BLVA, SVSA) → fix bugs during migration

**Features**:
- 2,394 lines total
- Clarity: 98/100, Correctness: 98/100 ⭐
- Complete Auth Module example (110 min end-to-end)
- Folder structure .NET (Controllers, Services, Entities, DTOs, Middleware)
- Naming conventions (PascalCase → camelCase JSON)

**Gandalf's Verdict**: *"Matches or exceeds Google/Amazon standards. HIGHEST SCORE TO DATE."*

**Evaluation Report**: `.claude/evaluations/bma-evaluation-20251112-230000.md`

---

### 🟡 Agent 6: Authentication & Security Agent (ASA)

**Status**: 🟡 AWAITING RE-EVALUATION (v2.0 - all 7 blockers fixed)
**Score v1.0**: 🔴 **88/100** (REJECTED)
**Score v2.0**: ⏳ **Pending Gandalf evaluation** (expected 95-97/100)
**Locație**: `.claude/agents/backend/authentication-security.md`
**Durată totală**: ~3.8 hours (v1.0: 1.3h + v2.0 fixes: 2.5h)
**Data v2.0**: 13 Noiembrie 2025

**Ce face**:
- 9 auth endpoints (signin, admin-signin, signup, signout, recovery, verification, check-token, refresh)
- 4 JWT token types (Access 8h, Refresh 30d, Email Validation 90d, Subscription Validation 365d)
- Argon2id password hashing
- Redis token blacklist
- Rate limiting (200K req/60s signin, 2K req/60s admin)
- CORS strict configuration

**v1.0 → v2.0 Evolution**:
- **v1.0**: 2,847 lines, 88/100, 7 CRITICAL blockers 🔴
- **v2.0**: 3,595 lines (+748 lines), pending evaluation ⏳

**ALL 7 BLOCKERS FIXED in v2.0**:
1. ✅ **FIX #1 (SECURITY)**: Replaced `new Random()` with `RandomNumberGenerator.Create()` (cryptographically secure PRNG)
2. ✅ **FIX #2**: Added hybrid Redis failure strategy (3-phase circuit breaker: fail-safe → degraded → fail-open)
3. ✅ **FIX #3**: Added PHASE 1.5 external service verification checklist (Stripe, Postmark, MailerLite, Redis)
4. ✅ **FIX #4**: Replaced subjective language with specific uncovered paths (6 line numbers documented)
5. ✅ **FIX #5**: Documented explicit Stripe failure behavior (background job + manual verification)
6. ✅ **FIX #6**: Added comprehensive timeout specifications table (7 services with exact milliseconds)
7. ✅ **FIX #7**: Defined deterministic email retry schedule (5min, 15min, 45min intervals = 65min total)

**Key Improvements v2.0**:
- Security hardened: Crypto-safe PRNG for all random generation
- Deterministic behavior: Zero ambiguous instructions
- Timeout specifications: 7 external services (Redis 5s, Stripe 10s, Postmark 5s, MailerLite 8s, etc.)
- Hybrid Redis strategy: Graceful degradation (blacklist → memory fallback → warning log)
- Email retry: Exponential backoff with deterministic intervals

**Key Lesson**: Comprehensive ≠ Correct. **Security bugs = instant reject**, even with 2,847 lines of code.

**Gandalf's v1.0 Verdict**: *"Fix your 7 blockers, eliminate ALL ambiguities. YOU SHALL NOT PASS... yet."*

**Awaiting**: Gandalf re-evaluation for v2.0 (expected score: 95-97/100)

**Evaluation Reports**:
- v1.0: `.claude/evaluations/asa-evaluation-20251112-232306.md` (88/100 REJECTED)
- v2.0: Pending

---

### 🟢 Agent 7: Payment Integration Agent (PIA)

**Status**: ✅ DONE (v1.0 - PRODUCTION READY)
**Score**: 🎯 **96/100** (APPROVED)
**Locație**: `.claude/agents/backend/payment-integration.md`
**Durată totală**: ~60 minutes
**Data finalizare**: 12 Noiembrie 2025

**Ce face**:
- Stripe API integration (11 metode: PaymentIntent, Subscription, Customer, Webhook)
- Subscription scheduling (AA1 monthly €19, AA2 annual €199, BB lifetime €599)
- Webhook security cu signature validation (prevent replay attacks)
- SmartBill integration (facturi românești, 19% TVA, format SOMA-YYYY-#####)
- 15 tipuri erori Stripe cu retry strategies (exponential backoff)
- Circuit breaker pattern (open după 5 failures, auto-close după 10 min)
- Idempotency keys pentru toate mutations (prevent double-charging)

**Features**:
- 1,492 lines production-grade
- **Correctness: 24.5/25 (98%)** ⭐
- Zero-tolerance policy pentru payment bugs
- 3 complete C# examples (compile-ready)
- 11 webhook event types handled
- Romanian law compliance (SmartBill mandatory)
- PSD2 compliance (3D Secure pentru EU cards)

**Gandalf's Verdict**: *"I'd trust you with €500K+ annual subscription revenue. Exceeds industry standard."*

**Evaluation Report**: `.claude/evaluations/pia-evaluation-20251112-233000.md`

---

### 🟢 Agent 8: Database & Entity Agent (DEA)

**Status**: ⏳ TO DO
**Prioritate**: CRITICAL (blocker pentru toți backend agents)
**Locație**: `.claude/agents/backend/database-entity.md`
**Durată estimată**: 60 minutes

**Ce face**:
- Migrează 20+ entities TypeORM → EF Core
- Configurează relationships: OneToMany, ManyToMany, OneToOne
- Database migrations + seeding strategy
- Index strategy pentru performance
- Query optimization patterns (Include, ThenInclude)

**Entities key**:
- User, Subscription, Course, Lesson, Category
- Invoice, Order, Campaign, Analytics, AnalyticsTime
- Shortlist, Address, Payment, SubscriptionType
- ZoomMeeting, ZoomWebinar

**Instrucțiuni cheie de definit**:
- [ ] Mapping TypeORM decorators → EF Core FluentAPI
- [ ] Relationship patterns cu navigation properties
- [ ] Migration naming conventions
- [ ] Seeding data strategy (admin users, subscription types)
- [ ] Index strategy (composite indexes pentru queries frecvente)
- [ ] Query optimization (eager loading vs lazy loading)

**Dependențe**: BMA (structură .NET)
**Testare**: Creare User + Course entities + migration

---

### 🟢 Agent 9: External Integrations Agent (EIA) ⭐ NOU - CONSOLIDAT

**Status**: ⏳ TO DO
**Prioritate**: MEDIUM
**Locație**: `.claude/agents/backend/external-integrations.md`
**Durată estimată**: 90 minutes (consolidează 3 agenți)

**CONSOLIDEAZĂ**:
- ❌ Video & Live Services Agent (VLSA) - 50 min
- ❌ Email & Marketing Agent (EMA) - 40 min
- ❌ Analytics & Reporting Agent (ARA) - 45 min
- ✅ **Total consolidat**: 135 min → 90 min (**-33% timp**)

**Ce face**:

**1. Video & Live Services** (Vimeo + Zoom):
- Vimeo OAuth 2.0 + video upload pipeline (chunking pentru large files)
- Vimeo privacy settings + embedding configuration
- Zoom SDK pentru meetings/webinars (JWT generation)
- Zoom signature generation pentru live sessions
- Webhook handling (Vimeo/Zoom events)

**2. Email & Marketing** (Postmark + MailerLite):
- Postmark transactional emails (.NET client)
- Email templates HTML (Razor views)
- MailerLite API pentru campaigns + automation
- Queue system pentru email batches (Hangfire/RabbitMQ)
- Tracking delivery/opens (Postmark webhooks)
- Unsubscribe link management (GDPR compliance)

**3. Analytics & Reporting** (FirstPromoter + Custom):
- FirstPromoter affiliate tracking integration
- Custom analytics events (VIEW_COURSE, VIEW_LESSON, TIME_SPENT)
- Dashboard statistics aggregation
- Cron jobs pentru agregare (Hangfire/Quartz.NET)
- Query optimization (materialized views)
- Export rapoarte (CSV, Excel)

**4. Facebook Pixel**:
- Lead tracking integration
- Event tracking pentru conversions

**Instrucțiuni cheie de definit**:
- [ ] Vimeo OAuth flow în .NET (3-legged OAuth)
- [ ] Video upload chunking strategy (10MB chunks, resume capability)
- [ ] Zoom JWT generation + SDK initialization
- [ ] Postmark API integration cu retry logic
- [ ] MailerLite API pentru subscriber management
- [ ] Analytics event schema (JSON structure)
- [ ] Hangfire setup pentru cron jobs + email batches
- [ ] Materialized views pentru dashboard performance
- [ ] Error handling pentru toate external APIs (circuit breaker, fallback)

**Raționament consolidare**:
- Toate sunt **external API integrations** cu pattern-uri similare
- Același error handling (circuit breaker, retry logic, timeout)
- Evităm handoff între 3 agenți separați
- Consistență în logging și monitoring

**Dependențe**: ASA (auth), DEA (entities)
**Testare**: Upload video Vimeo + send email Postmark + track analytics event

---

## TIER 3: FRONTEND (2 agenți) - Consolidat de la 7 ✂️

### 🔵 Agent 10: Admin Dashboard Agent (ADA) ⭐ NOU - CONSOLIDAT

**Status**: ⏳ TO DO
**Prioritate**: HIGH
**Locație**: `.claude/agents/frontend/admin-dashboard.md`
**Durată estimată**: 90 minutes (consolidează ADMA + components)

**CONSOLIDEAZĂ**:
- ❌ Admin Dashboard Migration Agent (ADMA) - 55 min
- ❌ Shared Components Agent (partea admin) - 25 min
- ✅ **Total consolidat**: 80 min → 90 min (**creștere 10 min pentru integrare**)

**Ce face**:
- Migrează **7 pagini admin**: Users, Courses, Lessons, Categories, Subscriptions, Analytics, Settings
- **React 18 → Vue 3 Composition API** (conversion patterns)
- **Redux Toolkit → Pinia** (state management migration)
- **Ant Design 5.20.1 → Ant Design Vue 4.x** (component mapping)
- **React Router 6 → Vue Router 4** (navigation patterns)
- Shared components library (Header, Sidebar, Table, Form, Modal, etc.)
- Form handling patterns (validation, submission, error display)
- Table pagination + filtering + sorting
- State persistence (localStorage → Pinia persist plugin)

**Instrucțiuni cheie de definit**:
- [ ] Mapping table React hooks → Vue Composition API (useState → ref, useEffect → onMounted)
- [ ] Redux patterns → Pinia patterns (actions, getters, mutations → actions + computed)
- [ ] Ant Design components → Ant Design Vue (API differences)
- [ ] Form handling (Formik/React Hook Form → Vuelidate/VeeValidate)
- [ ] Table patterns (pagination, filters, sorting cu server-side)
- [ ] Component library structure (composables, utils)
- [ ] Props interface standards (TypeScript)
- [ ] Event emitting patterns (emit vs callbacks)
- [ ] Slot usage guidelines (named slots, scoped slots)

**Raționament consolidare**:
- Admin dashboard = **pattern-uri omogene** (CRUD operations)
- Toate paginile folosesc aceleași componente (Table, Form, Modal)
- Evităm fragmentare (7 agenți cu micro-diferențe)
- Consistență styling și UX

**Dependențe**: Backend APIs (BMA endpoints)
**Testare**: Migrare completă pagina Users (list + create + edit + delete)

---

### 🔵 Agent 11: Web Client Agent (WCA) ⭐ NOU - CONSOLIDAT

**Status**: ⏳ TO DO
**Prioritate**: HIGH
**Locație**: `.claude/agents/frontend/web-client.md`
**Durată estimată**: 120 minutes (consolidează 6 agenți UI)

**CONSOLIDEAZĂ**:
- ❌ Web Client Migration Agent (WCMA) - 60 min
- ❌ Authentication UI Agent (AUIA) - 45 min
- ❌ Course & Video Player Agent (CVPA) - 50 min
- ❌ Subscription & Payment UI Agent (SPUA) - 55 min
- ❌ Dashboard & Profile Agent (DPA) - 45 min
- ❌ Shared Components Agent (partea web client) - 25 min
- ✅ **Total consolidat**: 280 min → 120 min (**-57% timp!**)

**Ce face**:

**1. Core Migration** (Next.js 15 → Nuxt 3):
- **21 pagini**: Home, Courses, Course Detail, Lesson Player, Auth (Sign In, Sign Up, Recovery), Subscription Plans, Checkout, Payment Success/Failure, Dashboard, Profile, Settings, About, Contact, Terms, Privacy, etc.
- **Next.js Pages Router → Nuxt 3 file-based routing**
- **getServerSideProps → Nuxt server API** (useFetch, useAsyncData)
- **next/image → Nuxt Image** (optimization)
- **next/router → useRouter** (navigation)
- SEO meta tags management (useHead, useSeoMeta)
- Dynamic routing patterns ([id].vue)

**2. Authentication UI**:
- Sign In / Sign Up forms cu validation (Vuelidate/VeeValidate)
- Password recovery flow (multi-step)
- Email verification UI
- Token storage (cookies vs localStorage - secure strategy)
- Auto-redirect logic (authenticated users)
- Remember me functionality

**3. Course & Video Player**:
- Course catalog cu filters (category, price, rating, search)
- Vimeo player component Vue 3 (embed API)
- Video analytics tracking (play, pause, progress, completion)
- Materials download UI
- Voting/rating system
- Progress tracking visual (progress bar, completion %)
- Course outline sidebar (lessons list)

**4. Subscription & Payment UI**:
- Stripe Elements Vue 3 integration (@stripe/stripe-js)
- Payment form validation
- 3D Secure handling (redirect flow)
- Billing address form (Romanian validation: județ, localitate)
- Campaign-based pricing display (AA1, AA2, BB)
- Success/failure pages (order confirmation)
- Invoice download links

**5. Dashboard & Profile**:
- User dashboard cu statistics (courses enrolled, hours watched, certificates)
- Statistics cards layout (Ant Design Vue Cards)
- Profile edit form (avatar upload, personal info)
- Avatar upload component (crop/resize - vue-advanced-cropper)
- Subscription display (active/inactive status, expiration date)
- Live sessions calendar integration (Zoom meetings list)
- Invoice history table

**6. Shared Components Library**:
- Layout components (Header, Footer, Navbar, Breadcrumbs)
- Form components (Input, Select, Checkbox, Radio, DatePicker)
- UI components (Button, Card, Modal, Drawer, Notification)
- Video player wrapper (Vimeo embed cu controls)
- Composables (useAuth, useCourse, usePayment, useAnalytics)

**Instrucțiuni cheie de definit**:
- [ ] Next.js patterns → Nuxt 3 patterns (comprehensive mapping table)
- [ ] getServerSideProps → useFetch/useAsyncData (data fetching strategies)
- [ ] next/image → Nuxt Image (optimization config)
- [ ] SEO meta tags (useHead vs useSeoMeta - când folosim fiecare)
- [ ] Stripe Elements integration (setup intent, payment intent flow)
- [ ] Form validation patterns (Vuelidate vs VeeValidate - recomandare)
- [ ] Vimeo player API (events: play, pause, progress, ended)
- [ ] Avatar upload + crop (vue-advanced-cropper setup)
- [ ] Component library structure (auto-import config)
- [ ] Composables patterns (reusable logic)
- [ ] Error handling UI (toast notifications, error pages)
- [ ] Loading states (skeletons, spinners)

**Raționament consolidare**:
- Web client = **21 pagini cu pattern-uri IDENTICE** (React→Vue conversion)
- Toate folosesc aceleași pattern-uri (forms, API calls, state management)
- **-57% timp** prin eliminare handoff între 6 agenți
- Consistență UX și code style

**Dependențe**: Backend APIs (toate endpoints), External Integrations (Vimeo, Stripe)
**Testare**:
- Complete user journey: Sign Up → Browse Courses → Subscribe → Watch Video → Complete Course
- Payment flow end-to-end cu Stripe test cards
- Responsive testing (mobile, tablet, desktop)

---

## TIER 4: QA & DEVOPS (2 agenți) - Consolidat de la 6 ✂️

### 🟣 Agent 12: QA & Testing Agent (QTA) ⭐ NOU - CONSOLIDAT

**Status**: ⏳ TO DO
**Prioritate**: HIGH
**Locație**: `.claude/agents/qa/qa-testing.md`
**Durată estimată**: 90 minutes (consolidează 3 agenți)

**CONSOLIDEAZĂ**:
- ❌ Testing Automation Agent (TAA) - 60 min
- ❌ Migration Validator Agent (MVA) - 50 min
- ❌ Performance Optimization Agent (POA) - 50 min
- ❌ Security Audit Agent (SAA) - **ELIMINAT** (redundant cu SVSA din TIER 0!)
- ✅ **Total consolidat**: 160 min → 90 min (**-44% timp**)

**Ce face**:

**1. E2E Testing** (Playwright/Cypress):
- Test structure (Page Object Model pattern)
- Critical flows priority:
  - Auth flow (sign up, sign in, password recovery)
  - Payment flow (subscribe, payment success, invoice generation)
  - Video flow (browse courses, watch lesson, track progress)
  - Admin flow (CRUD operations pe Users, Courses)
- Cross-browser testing matrix (Chrome, Firefox, Safari, Edge)
- Mobile responsive tests (iPhone, iPad, Android)
- Accessibility testing (WCAG 2.1 Level AA - axe-core integration)
- Visual regression testing (Percy/Chromatic - optional)

**2. Migration Validation**:
- Side-by-side comparison React vs Vue implementations
- API contract validation (request/response format identic)
- Behavior equivalence checks (business logic identică)
- Data flow verification (state management consistency)
- Performance comparison benchmarks (load time, bundle size)
- Regression test suite (ensure old features work în new platform)

**3. Performance Optimization**:
- Lighthouse audit checklist (target: >90 score on all metrics)
- Bundle analyzer setup (Nuxt analyze, webpack-bundle-analyzer)
- Code splitting strategy (route-based, component-based)
- Image optimization (WebP, AVIF, lazy loading, responsive images)
- Caching headers configuration (static assets, API responses)
- Core Web Vitals tracking (LCP <2.5s, FID <100ms, CLS <0.1)
- Performance budget enforcement (bundle size limits)
- Database query optimization (N+1 queries, missing indexes)
- API response time benchmarks (P50, P95, P99 latency)

**Instrucțiuni cheie de definit**:
- [ ] Playwright test structure (fixtures, page objects, helpers)
- [ ] Critical test scenarios (20+ high-priority tests)
- [ ] Cross-browser configuration (browsers matrix, parallel execution)
- [ ] Accessibility testing setup (axe-core rules, reporting)
- [ ] Migration validation protocol (comparison checklist)
- [ ] Lighthouse CI setup (automated audits în pipeline)
- [ ] Bundle size limits (main bundle <500KB, route chunks <200KB)
- [ ] Image optimization strategy (formats, sizes, lazy loading)
- [ ] Caching strategy (CDN, browser cache, service worker)
- [ ] Performance monitoring (Sentry, New Relic, custom metrics)

**Raționament consolidare**:
- Toate 3 sunt **QA activities** cu pattern-uri similare
- TAA + MVA = același scope (validare implementare)
- POA = parte din QA (performance = quality metric)
- SAA **ELIMINAT** - SVSA din TIER 0 deja face security audit complet!

**Dependențe**: Toți agenții (testează totul)
**Testare**:
- E2E test pentru auth flow (sign up → verify email → sign in)
- Lighthouse audit pe 5 pagini reprezentative
- Cross-browser test pe Chrome + Firefox + Safari

---

### 🟣 Agent 13: DevOps & CI/CD Agent (DCA)

**Status**: ⏳ TO DO
**Prioritate**: HIGH
**Locație**: `.claude/agents/devops/cicd-deployment.md`
**Durată estimată**: 60 minutes

**Ce face**:
- GitHub Actions pipelines (CI/CD automation)
- Docker containerization (backend .NET + frontend Nuxt)
- Deployment automation (staging + production)
- Environment variables management (secrets, config)
- Database migrations în CD pipeline
- Rollback strategy (blue-green deployment)
- Monitoring + alerting setup (Sentry, Grafana, Prometheus)

**Instrucțiuni cheie de definit**:
- [ ] GitHub Actions workflow structure:
  - CI: lint, test, build on every PR
  - CD: deploy to staging on merge to develop, production on merge to main
- [ ] Dockerfile pentru backend .NET:
  - Multi-stage build (build → publish → runtime)
  - Optimizare layer caching
  - Health check endpoint
- [ ] Dockerfile pentru frontend Nuxt:
  - SSR vs static generation decision
  - Environment variables injection
  - Nginx configuration (optional)
- [ ] Environment variables management:
  - GitHub Secrets pentru sensitive data
  - .env.example template
  - Validation script (ensure all vars defined)
- [ ] Database migrations în pipeline:
  - Run EF Core migrations automatically
  - Backup before migration (safety)
  - Rollback procedure if migration fails
- [ ] Deployment strategy:
  - Blue-green deployment (zero downtime)
  - Smoke tests post-deployment
  - Auto-rollback on failure
- [ ] Monitoring setup:
  - Sentry pentru error tracking (.NET + Vue)
  - Grafana dashboards (API latency, error rate, user activity)
  - Alerting rules (Slack/email notifications)

**Dependențe**: Toți agenții (deployează totul)
**Testare**:
- Deploy pe staging environment (DigitalOcean/AWS/Azure)
- Trigger CI/CD pipeline + verify successful deployment
- Simulate failure + verify rollback

---

## 📊 Progress Overview

| Tier | Total | Created | Approved | Pending | Rejected | % Complete | Status |
|------|-------|---------|----------|---------|----------|------------|--------|
| WAVE 0 (Meta) | 1 | 1 | 1 | 0 | 0 | 100% | ✅ |
| WAVE 0.5 (Requirements) | 1 | 1 | 1 | 0 | 0 | 100% | ✅ |
| TIER 0 (Audit) | 3 | 3 | 3 | 0 | 0 | 100% | ✅ |
| TIER 1 (Orchestration) | 1 | 1 | 1 | 0 | 0 | 100% | ✅ |
| TIER 2 (Backend) | 5 | 3 | 2 | 1 | 0 | 60% | ⏳ |
| TIER 3 (Frontend) | 2 | 0 | 0 | 0 | 0 | 0% | ⏳ |
| TIER 4 (QA & DevOps) | 2 | 0 | 0 | 0 | 0 | 0% | ⏳ |
| **TOTAL** | **15** | **9** | **8** | **1** | **0** | **60%** | ⏳ |

**Note**: ASA v2.0 (3,595 lines, +748 from v1.0) awaiting Gandalf re-evaluation

---

## ⏱️ Time Tracking

| Tier | Estimated | Actual | Remaining | Status |
|------|-----------|--------|-----------|--------|
| WAVE 0 | 1h | 2h | 0h | ✅ |
| WAVE 0.5 | 1h | 6h | 0h | ✅ |
| TIER 0 | 4h | 5.2h | 0h | ✅ |
| TIER 1 | 0.5h | 0.4h | 0h | ✅ (CAA only, PMA eliminated) |
| TIER 2 | 5h | 4.4h | 2.6h | ⏳ (ASA v1.0+v2.0: 3.8h ✅, BMA 0.4h ✅, PIA 1h ✅, DEA 1h, EIA 1.5h) |
| TIER 3 | 3.5h | 0h | 3.5h | ⏳ (ADA 1.5h + WCA 2h) |
| TIER 4 | 2.5h | 0h | 2.5h | ⏳ (QTA 1.5h + DCA 1h) |
| **TOTAL** | **~18h** | **~18h** | **~8.6h** | ⏳ |

**Economie vs arhitectură veche**: ~32h → ~26.6h (**-17% timp**)

**TIER 2 Breakdown**:
- BMA: 0.4h ✅
- PIA: 1h ✅
- ASA: 3.8h (v1.0: 1.3h + v2.0 fixes: 2.5h) 🟡 pending re-eval
- DEA: 1h ⏳
- EIA: 1.5h ⏳

---

## 📈 Agent Creation History (Chronological)

| # | Agent | Version | Score | Status | Date | Time | Rank |
|---|-------|---------|-------|--------|------|------|------|
| 0 | Gandalf 🧙‍♂️ | v5.0 | 99/100 | ✅ | 2025-01-11 | 2h | 🥇 META |
| 0.5 | SCA | v2.2 | 96/100 | ✅ | 2025-11-12 | 6h | 🥉 Tied |
| 1 | LCAA | v2.0 | 96/100 | ✅ | 2025-01-11 | 2h | 🥉 Tied |
| 2 | BLVA | v1.0 | 96/100 | ✅ | 2025-11-12 | 2h | 🥉 Tied |
| 3 | SVSA | v1.0 | 95/100 | ✅ | 2025-11-12 | 0.8h | - |
| 4 | CAA | v1.0 | 95.2/100 | ✅ | 2025-11-12 | 0.4h | - |
| 5 | BMA | v1.0 | **97/100** | ✅ | 2025-11-12 | 0.4h | 🥈 **HIGHEST** |
| 6 | PIA | v1.0 | 96/100 | ✅ | 2025-11-12 | 1h | 🥉 Tied |
| 7 | ASA | v1.0 | 88/100 | 🔴 | 2025-11-12 | 1.3h | REJECTED |
| 8 | **ASA** | **v2.0** | **Pending** | **🟡** | **2025-11-13** | **2.5h** | **Awaiting Gandalf** |
| ~~PMA~~ | ~~v2.0~~ | ~~97/100~~ | ❌ | ~~2025-11-12~~ | ~~0.8h~~ | **ELIMINATED** |

**Metrics (excluding ASA v2.0 pending)**:
- **Total approved**: 8 agents
- **Total rejected then fixed**: 1 agent (ASA v1.0→v2.0: 88→pending, +748 lines)
- **Pass Rate**: 89% (8/9 excluding eliminated PMA)
- **Avg Score**: 96.3/100 (approved only)
- **Avg Time**: ~2.1h per agent (including ASA rework)
- **Quality Trend**: IMPROVING ↗️ (BMA at 97/100, ASA fixes all 7 blockers)

---

## 🎯 Quality Distribution

### Score Breakdown:
- **99-100**: 1 agent (Gandalf meta) 🥇
- **97-98**: 1 agent (BMA) 🥈
- **95-96**: 5 agents (SCA, LCAA, BLVA, CAA, PIA) 🥉
- **<95**: 1 agent (SVSA at 95 - at threshold)
- **Rejected**: 1 agent (ASA at 88)

### First-Try Success Rate: 56% (5/9)
- ✅ **Passed first try**: BLVA, SVSA, CAA, PIA, BMA
- ❌ **Needed iterations**: Gandalf, SCA, LCAA, ASA

**Key Success Factor**: Detailed mapping tables + comprehensive examples = first-try approval

---

## 🚀 Next Steps - Prioritized Roadmap

### Phase 1: Complete TIER 2 Backend (Critical) - 2.6h
1. **ASA v2.0** (0h) - ✅ All 7 blockers fixed, awaiting Gandalf re-evaluation
2. **DEA** (1h) - CRITICAL - 20+ entities TypeORM→EF Core
3. **EIA** (1.5h) - External Integrations (Vimeo, Zoom, Postmark, MailerLite, Analytics)

### Phase 2: TIER 3 Frontend - 3.5h
4. **ADA** (1.5h) - Admin Dashboard (7 pages + components)
5. **WCA** (2h) - Web Client (21 pages + all UI)

### Phase 3: TIER 4 QA & DevOps - 2.5h
6. **QTA** (1.5h) - E2E tests + migration validation + performance
7. **DCA** (1h) - CI/CD + Docker + deployment

**Total Remaining**: ~8.6h (Phase 1: 2.6h + Phase 2: 3.5h + Phase 3: 2.5h)

**Grand Total**: 18h (done) + 8.6h (remaining) = **~26.6 hours** (vs 32h arhitectură veche)

**ASA v2.0 Status**: 3,595 lines (+748 from v1.0), all 7 critical blockers resolved, pending Gandalf evaluation

---

## 📋 Agenți Eliminați din Arhitectura Veche (27→15)

### Eliminați complet (12 agenți):
1. ❌ **PMA** (97/100) → Responsibilities merged into CAA
2. ❌ **VLSA** → Merged into EIA (External Integrations Agent)
3. ❌ **EMA** → Merged into EIA
4. ❌ **ARA** → Merged into EIA
5. ❌ **ATDA** → Testing responsibilities merged into QTA
6. ❌ **ADMA** → Merged into ADA (Admin Dashboard Agent)
7. ❌ **WCMA** → Merged into WCA (Web Client Agent)
8. ❌ **AUIA** → Merged into WCA
9. ❌ **CVPA** → Merged into WCA
10. ❌ **SPUA** → Merged into WCA
11. ❌ **DPA** → Merged into WCA
12. ❌ **SCA** (Shared Components) → Merged into ADA + WCA
13. ❌ **TAA** → Merged into QTA
14. ❌ **MVA** → Merged into QTA
15. ❌ **POA** → Merged into QTA
16. ❌ **SAA** → REDUNDANT cu SVSA (already in TIER 0)
17. ❌ **DA** (Documentation Agent) → MANUAL (Swagger auto-generated)

### Agenți noi consolidați (3 agenți):
- ✅ **EIA** (External Integrations Agent) - consolidează VLSA + EMA + ARA
- ✅ **ADA** (Admin Dashboard Agent) - consolidează ADMA + Shared Components (admin)
- ✅ **WCA** (Web Client Agent) - consolidează WCMA + AUIA + CVPA + SPUA + DPA + Shared Components (web)
- ✅ **QTA** (QA & Testing Agent) - consolidează TAA + MVA + POA

---

## 💡 Lecții învățate din primii 9 agenți

### ✅ Ce funcționează:
1. **Mapping tables comprehensive** → First-try success (BMA 97/100 în 25 min)
2. **Example reports 400-1200 lines** → Gold standard specification (BLVA, BMA)
3. **Autonomous workflows multi-phase** → Fully executable (LCAA, BMA, SVSA)
4. **Integration cross-referencing** → Synergy findings (SVSA references LCAA+BLVA)

### ❌ Ce NU funcționează:
1. **Ambiguity în security code** → INSTANT REJECT (ASA: `new Random()` instead of crypto-safe)
2. **Comprehensive ≠ Correct** → 2,847 lines cu 7 blockers (ASA) vs 2,314 lines cu 0 blockers (SVSA)
3. **Too many specialized agents** → Handoff overhead (7 frontend agents eliminated)

### 🎯 Optimizations Applied:
1. **Consolidare agenți omogeni** → Frontend de la 7→2 agents (-71%)
2. **Eliminate PM redundancy** → CAA preia orchestration + timeline tracking
3. **Merge external integrations** → Backend de la 8→5 agents (-37%)
4. **Remove security duplication** → SAA eliminat (SVSA deja face audit)

---

## 📖 Template Standard pentru Fiecare Agent

Pentru fiecare agent creăm:

```
📁 .claude/agents/{category}/{agent-name}.md

Structură fișier:
1. Header (Nume, Role, Activation Criteria)
2. STRICT RULES (15 MUST DO / 10 MUST NOT DO)
3. Input Requirements (format, validări)
4. Output Format (structured, cu exemple concrete)
5. Workflow (autonomous execution phases cu timings)
6. Validation Checklist (success criteria)
7. Examples (2-3 complete end-to-end)
8. Error Handling (6+ scenarios cu recovery)
9. Edge Cases (4+ documented)
10. Integration Points (dependencies, handoffs)
```

**Critical**: Fiecare agent MUST be evaluated by Gandalf before marking DONE (threshold: 95%+)

---

## 🔄 Process de Creare

### Pas 1: Design & Planning (15-20 min)
- Analizăm responsabilități agent
- Definim MUST DO / MUST NOT DO rules (strict)
- Stabilim format input/output (structured)
- Alegem 2-3 exemple complete

### Pas 2: Implementation (30-60 min)
- Scriem fișierul `.md` complet
- Includem toate secțiunile (10 sections minimum)
- Adăugăm mapping tables (dacă aplicabil)
- Scriem exemple comprehensive (400-1200 lines)

### Pas 3: Gandalf Evaluation (20-30 min)
- Invocăm Gandalf cu "Gandalf, evaluate agent {agent-name}"
- Analizăm raportul detaliat
- Identificăm blockers (dacă score <95)

### Pas 4: Fixes & Re-evaluation (optional, 30-120 min)
- Dacă score <95: Fix ALL blockers
- Re-submit pentru evaluare
- Iterăm până la 95%+

### Pas 5: Finalization (5 min)
- Marcăm agent ca ✅ DONE în plan-creare-agenti.md
- Comitem în git cu evaluation report
- Update progress metrics

**Timp mediu per agent**: ~2h (design 20min + implementation 60min + evaluation 25min + fixes 15min optional)

---

## 🎯 Success Criteria

### La nivel de agent:
- ✅ Score Gandalf ≥ 95/100
- ✅ Zero CRITICAL blockers
- ✅ Autonomous execution (no manual intervention)
- ✅ Comprehensive examples (2-3 end-to-end)
- ✅ Error handling (6+ scenarios)
- ✅ Edge cases documented (4+)

### La nivel de proiect:
- ✅ Toate cele 15 agenți created & approved
- ✅ Average score ≥ 96/100
- ✅ First-try success rate ≥ 50%
- ✅ Total time ≤ 24 hours
- ✅ Integration verified (cross-agent handoffs)

---

## 🔐 Quality Assurance

### Gandalf Rules (ZERO TOLERANCE):
1. ❌ Production-breaking bugs → Score = 0
2. ❌ Undefined critical behavior → Score = 0
3. ❌ Non-deterministic instructions → -20 points
4. ❌ Missing verification → -15 points
5. ❌ Circular dependencies → Score = 0
6. ❌ Token limit violations → -10 points
7. ❌ Unverifiable claims → -5 points per claim

### Mandatory Edge Cases (ALL agents):
1. Empty/null/undefined input
2. Maximum size/length input (boundary)
3. Concurrent access (if applicable)
4. External dependency failure (API down)
5. Timeout scenarios (10x normal time)

---

## 📝 Regulă de Update

**DUPĂ FIECARE AGENT**:
1. Actualizează status: `⏳ TO DO` → `✅ DONE` sau `🔴 REJECTED`
2. Adaugă score + date finalizare
3. Link către evaluation report
4. Update Progress Overview table
5. Update Time Tracking
6. Commit în git: `git commit -m "Agent {name} v{version}: {status} ({score}/100)"`

---

## 🚨 Blockers & Risks

### Current Blockers:
1. **ASA v1.0 rejected** (88/100) - 7 CRITICAL blockers
   - Impact: Auth module delayed
   - Mitigation: Fix all 7 blockers în v2.0 (estimated 2.5h)
   - Priority: HIGH

### Risks Identified:
1. **Frontend consolidation** (7→2 agents)
   - Risk: Agenți prea mari (WCA = 21 pages)
   - Mitigation: Detailed section breakdown, comprehensive mapping tables
   - Probability: LOW (BMA success cu 2,394 lines demonstrează scalability)

2. **External Integrations consolidation** (3→1 agent)
   - Risk: Prea multe API-uri diferite (Vimeo, Zoom, Postmark, MailerLite)
   - Mitigation: Separate sections per integration, common error handling patterns
   - Probability: MEDIUM

---

**Document Version**: 2.1 (OPTIMIZED ARCHITECTURE - ASA v2.0 FIXED)
**Last Updated**: 2025-11-13 (ASA v2.0 all blockers resolved)
**Architecture**: 15 agents (optimized from 27, -44% complexity)
**Status**: 8/15 approved (53%), 1 pending re-eval (ASA v2.0), 6 TO DO
**Next Agent**: DEA (1h) or EIA (1.5h) while ASA v2.0 awaits Gandalf
**Estimated Completion**: 18h done + 8.6h remaining = **~26.6h total** (vs 32h old architecture)
