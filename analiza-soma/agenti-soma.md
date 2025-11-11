# AGENȚI AI PENTRU PROIECTUL SOMAWAY

## Prezentare generală

Această listă conține cei 26 de agenți AI specializați pentru implementarea completă a platformei Somaway (somaway.ro) - o platformă de video learning cu 3 aplicații:
- **Backend**: Node.js/NestJS → .NET Core
- **Admin Dashboard**: React 18 → Vue 3
- **Web Client**: Next.js 15 → Nuxt 3

Fiecare agent are un rol specific și bine definit pentru a asigura consistență și calitate în implementare.

**IMPORTANT**: Proiectul urmează strategia **Audit-First Migration** - codul vechi este auditat complet pentru bug-uri și vulnerabilități ÎNAINTE de migrare, asigurând că platforma nouă pornește cu cod curat.

---

## TIER 0: PRE-MIGRATION AUDIT (3 agenți) ⭐ NOU

### 1. Legacy Code Auditor Agent (LCAA)
**Ce face**: Analizează și auditează complet codul vechi (Node.js/NestJS/React/Next.js) pentru a identifica bug-uri, anti-patterns, code smells, race conditions, memory leaks și probleme de logică ÎNAINTE de migrare. Generează rapoarte cu bug-uri categorizate pe severitate (CRITICAL/MEDIUM/LOW).

**Responsabilități cheie**:
- Scanare completă cod vechi pentru bug-uri
- Detectare anti-patterns (callback hell, God objects, etc.)
- Identificare race conditions și memory leaks
- Detectare probleme de performance
- Analiză consistență logică business
- Generare rapoarte cu categorizare severitate
- Recomandări fix pentru fiecare bug găsit

**Exemple bug-uri detectate**:
- Race conditions în operații async
- Memory leaks (event listeners necurățați)
- Infinite loops în React useEffect
- Logic bugs (validări incomplete, edge cases)
- Probleme timezone în date calculations
- Inconsistențe între frontend și backend

---

### 2. Business Logic Validator Agent (BLVA)
**Ce face**: Verifică că logica business din codul vechi este CORECTĂ prin comparare cu documentația JIRA și specificațiile. Identifică inconsistențe între cerințe și implementare, edge cases neacoperite și logică business incompletă sau greșită.

**Responsabilități cheie**:
- Comparare cod vechi cu JIRA specifications
- Validare logică business vs requirements
- Identificare edge cases neacoperite
- Verificare calcule și formule critice
- Validare flow-uri business complexe
- Detectare inconsistențe între module
- Raportare discrepanțe cod vs documentație

**Exemple validări**:
- Stripe subscription scheduling (AA1, AA2, BB scenarios)
- Calcule status subscription (ACTIVE/INACTIVE)
- Validări payment amounts și currency (RON)
- Flow-uri email verification complete
- Logic token expiration și refresh

---

### 3. Security Vulnerability Scanner Agent (SVSA)
**Ce face**: Scanează codul vechi pentru vulnerabilități de securitate conform OWASP Top 10, credentials expuse, API keys hardcodate, weak cryptography, injection vulnerabilities și alte riscuri de securitate. Asigură că vulnerabilitățile NU sunt migrate în platforma nouă.

**Responsabilități cheie**:
- Scan OWASP Top 10 vulnerabilities
- Detectare SQL injection potential
- Identificare XSS și CSRF vulnerabilities
- Scan credentials și secrets hardcodate
- Verificare weak password policies
- Audit JWT implementation și token management
- Scan dependency vulnerabilities
- Verificare CORS și rate limiting

**Exemple vulnerabilități**:
- API keys hardcoded în cod
- Weak password validation (< 8 chars)
- Missing rate limiting pe endpoints critice
- JWT tokens fără expiration
- CORS permisiv (origin: '*')
- SQL injection prin string concatenation
- XSS prin dangerouslySetInnerHTML

---

## TIER 1: ORCHESTRARE & COORDONARE (2 agenți)

### 1. Chief Architect Agent (CAA)
**Ce face**: Orchestrator principal și decision maker tehnic pentru întregul proiect. Coordonează toți cei 20+ agenți, ia decizii arhitecturale, rezolvă conflicte între implementări și asigură consistența pattern-urilor în tot codul.

**Responsabilități cheie**:
- Coordonează toți agenții specializați
- Ia decizii arhitecturale cross-platform
- Rezolvă conflicte tehnice între module
- Face code review la nivel macro
- Menține consistența arhitecturală

---

### 2. Project Manager Agent (PMA)
**Ce face**: Gestionează timeline-ul proiectului, trackează progresul tuturor celor 26+ module, alocă agenți la task-uri, identifică blockers și raportează status-ul către stakeholderi.

**Responsabilități cheie**:
- Trackează progresul tuturor modulelor
- Gestionează dependențele între task-uri
- Alocă resurse (agenți) la task-uri
- Identifică și raportează riscuri
- Generează rapoarte de progres

---

## TIER 2: SPECIALIZARE BACKEND (8 agenți)

### 3. Backend Migration Architect (BMA)
**Ce face**: Specialist în migrarea arhitecturii de la Node.js/NestJS către .NET Core. Convertește decoratori TypeScript (@Injectable, @Controller) în pattern-uri .NET, migrează TypeORM la Entity Framework Core și asigură compatibilitatea API-urilor.

**Responsabilități cheie**:
- Proiectează structura soluției .NET
- Convertește decoratori NestJS în atribute .NET
- Migrează TypeORM entities la EF Core
- Asigură compatibilitatea contractelor API

---

### 4. Authentication & Security Agent (ASA)
**Ce face**: Implementează sistemul complet de autentificare cu 4 tipuri de JWT tokens (Access, Refresh, Email Validation, Subscription Validation), role-based authorization (Admin, Creator, Customer, Guest), rate limiting și securitate OWASP.

**Responsabilități cheie**:
- Sistemul JWT cu 4 tipuri de tokens
- Passport strategies → .NET Identity middleware
- Role-based authorization
- Rate limiting și CORS
- Password hashing cu Argon2

---

### 5. Payment Integration Agent (PIA)
**Ce face**: Specialist în integrarea sistemelor de plată Stripe și Librapay. Implementează scenarii complexe de subscription scheduling (AA1, AA2, BB), procesare webhooks, reconciliere plăți și generare facturi prin SmartBill (sistem românesc).

**Responsabilități cheie**:
- Integrare Stripe API completă (11 metode)
- Subscription scheduling complex
- Webhook handling securizat
- Integrare Librapay
- SmartBill facturare (RON)

---

### 6. Video & Live Services Agent (VLSA)
**Ce face**: Integrează platformele video Vimeo (hosting) și Zoom (sesiuni live). Implementează OAuth 2.0 pentru Vimeo, pipeline de upload video, JWT pentru Zoom și gestionarea meetingurilor/webinarelor.

**Responsabilități cheie**:
- Vimeo OAuth 2.0 și upload video
- Setări privacy și embedding video
- Zoom SDK pentru meetings și webinars
- Generare signature pentru live sessions
- Optimizare streaming video

---

### 7. Email & Marketing Agent (EMA)
**Ce face**: Implementează serviciile de email transactional (Postmark) și marketing automation (MailerLite). Gestionează template-uri email, flow-uri de verificare email, notificări de subscription și campanii marketing.

**Responsabilități cheie**:
- Template-uri email Postmark
- Marketing automation MailerLite
- Email verification flows
- Notificări subscription
- Campanii email automate

---

### 8. Database & Entity Agent (DEA)
**Ce face**: Migrează toate cele 20+ entități de la TypeORM la Entity Framework Core. Configurează relații (OneToMany, ManyToMany), indexuri, cascade deletes, query optimization și database migrations.

**Responsabilități cheie**:
- Migrare 20+ entități TypeORM → EF Core
- Configurare relații și navigation properties
- Database migrations și seeding
- Optimizare query-uri
- Strategie de indexing

---

### 9. Analytics & Reporting Agent (ARA)
**Ce face**: Implementează sistemul de analytics pentru tracking activitate utilizatori (VIEW_COURSE, VIEW_LESSON, TIME_SPENT), statistici dashboard, rapoarte business intelligence și cron jobs pentru agregare date.

**Responsabilități cheie**:
- User analytics tracking
- Dashboard statistics
- Business intelligence reports
- Cron jobs pentru agregare
- Query-uri optimizate pentru rapoarte

---

### 10. API Testing & Documentation Agent (ATDA)
**Ce face**: Scrie teste pentru toate cele 80+ endpoints API (unit tests, integration tests), generează documentație Swagger/OpenAPI, creează colecții Postman și validează contracte API.

**Responsabilități cheie**:
- Unit tests pentru controllers (.NET xUnit/NUnit)
- Integration tests pentru servicii
- Swagger/OpenAPI documentation
- Postman collections
- API contract validation
- Target: >70% code coverage

---

## TIER 3: SPECIALIZARE FRONTEND (7 agenți)

### 11. Admin Dashboard Migration Agent (ADMA)
**Ce face**: Migrează Admin Dashboard-ul de la React 18 + Redux la Vue 3 + Pinia. Convertește cele 7 pagini principale (Courses, Lessons, Users, Categories, Subscriptions, Campaigns, Orders) și adaptează Ant Design 5 la Ant Design Vue 4.

**Responsabilități cheie**:
- Migrare 7 pagini admin principale
- Redux Toolkit → Pinia migration
- Ant Design → Ant Design Vue
- Form handling patterns
- Table și pagination patterns

---

### 12. Web Client Migration Agent (WCMA)
**Ce face**: Migrează Web Client-ul de la Next.js 15 la Nuxt 3. Convertește 21 de pagini, implementează file-based routing Nuxt, migrează React hooks la Vue Composition API și optimizează SSR/CSR hybrid.

**Responsabilități cheie**:
- Migrare 21 pagini web client
- Next.js Pages Router → Nuxt file-based routing
- React hooks → Vue Composition API
- SSR/CSR strategy
- SEO optimization

---

### 13. Authentication UI Agent (AUIA)
**Ce face**: Implementează toate paginile de autentificare (Sign In, Sign Up, Password Recovery, Email Verification, Account Verification) și gestionează session management în UI, form validation și error handling.

**Responsabilități cheie**:
- Pagini Sign In/Sign Up
- Password recovery flow UI
- Email verification UI
- Session management frontend
- Multi-step form flows

---

### 14. Course & Video Player Agent (CVPA)
**Ce face**: Implementează catalogul de cursuri cu filtre, pagini detalii curs, player video Vimeo integrat, sistem de download materiale, voting system și tracking analytics pentru video playback.

**Responsabilități cheie**:
- Course listing cu filters
- Course detail pages
- Vimeo player integration
- Materials download
- Voting și rating system
- Video analytics tracking

---

### 15. Subscription & Payment UI Agent (SPUA)
**Ce face**: Implementează flow-ul complet de subscription și plată. Integrează Stripe Elements, Librapay checkout, formulare billing address, handling success/failure plăți și subscriptions bazate pe campanii.

**Responsabilități cheie**:
- Subscription plans display
- Stripe Elements integration
- Librapay payment flow
- Billing address forms
- Payment success/failure handling
- Campaign-based subscriptions

---

### 16. Dashboard & Profile Agent (DPA)
**Ce face**: Creează dashboard-ul utilizatorilor cu statistici, pagini de profil și setări, upload avatar, display facturi, management subscriptions și calendar pentru sesiuni live.

**Responsabilități cheie**:
- User dashboard cu statistics
- Profile edit pages
- Avatar upload functionality
- Invoices display
- Subscription management UI
- Live sessions calendar

---

### 17. Shared Components Agent (SCA)
**Ce face**: Creează și menține biblioteca de componente reutilizabile pentru ambele aplicații frontend (Admin + Web Client): Layout components, Form components, UI utilities și design system consistency.

**Responsabilități cheie**:
- Layout components (Header, Footer, Sidebar)
- Form components reusable
- UI utilities și helpers
- Component library maintenance
- Design system consistency

---

## TIER 4: QA & DEPLOYMENT (4 agenți)

### 18. Testing Automation Agent (TAA)
**Ce face**: Creează suite-uri complete de teste E2E (Playwright/Cypress) pentru toate flow-urile critice (auth, payment, video playback), cross-browser testing, responsive testing și accessibility testing (WCAG 2.1 AA).

**Responsabilități cheie**:
- E2E tests Playwright/Cypress
- Critical flow testing
- Cross-browser testing
- Mobile responsive testing
- Accessibility testing WCAG 2.1 AA
- Target: >70% coverage

---

### 19. Performance Optimization Agent (POA)
**Ce face**: Optimizează performance-ul aplicațiilor pentru Lighthouse score >90. Optimizare bundle size, imagini, code splitting, caching strategies și Core Web Vitals (LCP, FID, CLS).

**Responsabilități cheie**:
- Lighthouse score >90
- Bundle size optimization
- Image optimization
- Code splitting strategy
- Caching implementation
- Core Web Vitals optimization

---

### 20. DevOps & CI/CD Agent (DCA)
**Ce face**: Configurează pipeline-uri CI/CD (GitHub Actions), containerizare Docker, deployment automation către Vercel/Netlify/DigitalOcean, database migrations automation și monitoring (Sentry, LogRocket).

**Responsabilități cheie**:
- GitHub Actions CI/CD pipelines
- Docker containerization
- Environment configuration
- Deployment automation
- Database migrations automation
- Monitoring setup (Sentry)

---

### 21. Documentation Agent (DA)
**Ce face**: Generează și menține documentație completă: API documentation (Swagger), component documentation, README files, architecture diagrams, migration guides și onboarding documentation pentru echipă.

**Responsabilități cheie**:
- API documentation (Swagger/OpenAPI)
- Component documentation
- README files pentru toate repo-urile
- Architecture diagrams
- Migration guides
- Onboarding documentation

---

## TIER 5: SPECIALIST SUPPORT (2 agenți)

### 22. Migration Validator Agent (MVA)
**Ce face**: Validează că migrările sunt corecte prin comparare side-by-side React vs Vue, Redux vs Pinia, verifică compatibilitatea API contracts, validează data flow și asigură că nu există regressions.

**Responsabilități cheie**:
- Comparare React vs Vue implementations
- Verificare Redux → Pinia state equivalence
- API contract compatibility validation
- Data flow verification
- Regression prevention

---

### 23. Security Audit Agent (SAA)
**Ce face**: Scanează vulnerabilități de securitate conform OWASP Top 10, previne SQL injection, XSS, CSRF, scanează dependențe pentru vulnerabilități cunoscute și auditează secret management.

**Responsabilități cheie**:
- OWASP Top 10 vulnerability checks
- SQL injection prevention
- XSS și CSRF protection
- Dependency vulnerability scanning
- Secret management audit
- Security best practices enforcement

---

## Statistici generale

| Categorie | Număr agenți | Scope principal |
|-----------|--------------|-----------------|
| Pre-Migration Audit | 3 | Audit cod vechi, bug detection, security |
| Orchestrare & Coordonare | 2 | Management și coordonare |
| Backend Specializare | 8 | Node.js → .NET migration |
| Frontend Specializare | 7 | React/Next.js → Vue/Nuxt migration |
| QA & Deployment | 4 | Testing, optimization, deployment |
| Specialist Support | 2 | Validation și security |
| **TOTAL** | **26 agenți** | **Audit + Implementare completă** |

---

## Cum se utilizează agenții

### Mod de lucru recomandat:

1. **Tu alegi modulul** de implementat (ex: "Autentificare Backend")
2. **Chief Architect Agent** decide ce agenți sunt necesari
3. **Agenții specializați** lucrează automat la task-uri
4. **Validation agents** verifică calitatea
5. **Tu validezi** rezultatul final

### Exemplu concret:

```
Tu: "Implementează modulul de Autentificare pentru Backend"

Chief Architect Agent:
  → apelează Database & Entity Agent (pentru User entity)
  → apelează Authentication & Security Agent (pentru JWT)
  → apelează API Testing Agent (pentru teste)
  → apelează Migration Validator Agent (pentru validare)

Rezultat: Modul complet de autentificare în .NET
```

---

## Timeline estimat cu agenții (Audit-First Strategy)

| Fază | Durata | Agenți principali |
|------|--------|-------------------|
| **PHASE 0: Pre-Migration Audit** ⭐ | Săptămâni 1-2 | LCAA, BLVA, SVSA |
| **PHASE 1: Foundation** | Săptămâni 3-4 | CAA, BMA, DCA |
| **PHASE 2: Backend Core** | Săptămâni 5-8 | DEA, ASA, ATDA |
| **PHASE 3: Backend Services** | Săptămâni 9-11 | PIA, VLSA, EMA, ARA |
| **PHASE 4: Admin Dashboard** | Săptămâni 12-14 | ADMA, SCA, TAA |
| **PHASE 5: Web Client** | Săptămâni 15-17 | WCMA, AUIA, CVPA, SPUA, DPA |
| **PHASE 6: Optimization & Deployment** | Săptămână 18 | POA, MVA, SAA, DA, DCA |
| **TOTAL** | **18 săptămâni** | **4.5 luni** |

**Notă CRITICĂ**: PHASE 0 (Audit) este OBLIGATORIE și blochează începerea migrării. Nu se începe PHASE 1 până când raportul de audit este complet și Chief Architect Agent decide ce bug-uri trebuie fixate.

---

## Contact și coordonare

Pentru coordonare și instrucțiuni despre cum să creezi agenți custom controlați de tine, consultă documentația de orchestrare.

**Status**: ✅ Lista completă de agenți definită + Audit-First Strategy
**Data**: 11 Ianuarie 2025
**Versiune**: 2.0
**Ultimele modificări**:
- ⭐ Adăugat TIER 0: Pre-Migration Audit (3 agenți noi)
- 📊 Actualizat total: 23 → 26 agenți
- ⏱️ Actualizat timeline: 16 → 18 săptămâni (4.5 luni)
- 🔒 Implementat Audit-First Migration Strategy
