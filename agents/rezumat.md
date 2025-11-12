# Documentație Agenți Claude Code

Acest document conține o analiză detaliată a tuturor agenților din repository-ul [wshobson/agents](https://github.com/wshobson/agents).

**Total agenți identificați:** 145

---

## Agenți Analizați (1-10)

| Nr. | Nume Agent | Plugin | Descriere | Utilizare Principală | Model |
|-----|------------|--------|-----------|---------------------|-------|
| 1 | **ui-visual-validator** | accessibility-compliance | Expert în validare vizuală UI specializat în testare UI, conformitate design system și verificare accessibility. Analizează screenshot-uri, teste de regresie vizuală și validare componente. Folosește instrumente moderne (Chromatic, Percy, Applitools, Playwright). | Validare modificări UI, verificare implementare design system, testare WCAG 2.1/2.2, validare consistență cross-browser și responsive design. Util pentru QA vizual și accessibility compliance. | sonnet |
| 2 | **context-manager** | agent-orchestration | Specialist în inginerie context AI, managementul context dinamic, vector databases, knowledge graphs și sisteme de memorie inteligente. Orchestrează contextul pentru workflow-uri multi-agent și aplicații AI enterprise. | Management context pentru sisteme AI complexe, implementare RAG (Retrieval-Augmented Generation), integrare Pinecone/Weaviate/Qdrant, knowledge graphs, memorie long-term pentru conversații AI și orchestrare workflow multi-agent. | haiku |
| 3 | **backend-architect** | api-scaffolding | Arhitect backend expert în design API scalabile, arhitectură microservices și sisteme distribuite. Stăpânește REST/GraphQL/gRPC, arhitecturi event-driven, service mesh și framework-uri backend moderne. | Proiectare servicii backend noi, definire boundaries servicii, arhitecturi microservices, comunicare inter-servicii, implementare pattern-uri de reziliență (circuit breaker, retry), design observabilitate și strategii de caching. | sonnet |
| 4 | **django-pro** | api-scaffolding | Expert Django 5.x specializat în async views, Django REST Framework (DRF), Celery și Django Channels. Construiește aplicații web scalabile cu arhitectură robustă, testare și deployment. | Dezvoltare aplicații Django moderne, optimizare ORM (select_related, prefetch_related), implementare API-uri cu DRF, procesare background tasks cu Celery, WebSockets cu Django Channels, migrații database complexe. | sonnet |
| 5 | **fastapi-pro** | api-scaffolding | Expert FastAPI specializat în API-uri async high-performance cu SQLAlchemy 2.0 și Pydantic V2. Stăpânește microservices, WebSockets și pattern-uri async Python moderne. | Dezvoltare microservices async, API-uri RESTful performante, implementare autentificare JWT, integrare SQLAlchemy async, WebSockets real-time, optimizare performanță și documentare automată OpenAPI. | sonnet |
| 6 | **graphql-architect** | api-scaffolding | Arhitect GraphQL expert în federation, optimizare performanță și securitate enterprise. Construiește scheme scalabile, implementează caching avansat și proiectează sisteme real-time. | Design arhitectură GraphQL federată, optimizare query-uri cu DataLoader, implementare subscriptions real-time, Apollo Federation v2, caching multi-nivel, field-level authorization și migrare de la REST la GraphQL. | sonnet |
| 7 | **api-documenter** | api-testing-observability | Specialist documentație API cu OpenAPI 3.1, instrumente AI-powered și practici moderne de developer experience. Creează documentație interactivă, generează SDK-uri și construiește portale developer. | Scriere specificații OpenAPI 3.1, creare portale developer interactive, generare SDK-uri multi-limbaj, documentare autentificare și securitate, Swagger UI/Redoc customization, testare automată a exemplelor de cod. | haiku |
| 8 | **frontend-developer** | application-performance | Developer frontend expert în React 19, Next.js 15 și arhitectură frontend modernă. Stăpânește React Server Components, rendering concurrent și optimizare performanță avansată. | Dezvoltare componente React moderne, implementare Server Components și Server Actions, optimizare Core Web Vitals, Next.js App Router, state management (Zustand, React Query), Tailwind CSS, testare cu React Testing Library. | sonnet |
| 9 | **observability-engineer** | application-performance | Inginer observabilitate specializat în monitoring production-ready, logging și tracing pentru aplicații enterprise. Implementează strategii comprehensive de observabilitate, management SLI/SLO și workflow-uri incident response. | Implementare Prometheus+Grafana, distributed tracing cu Jaeger/OpenTelemetry, management log-uri cu ELK Stack, alerting inteligent cu PagerDuty, definire SLI/SLO și error budgets, chaos engineering, dashboards custom pentru stakeholders. | sonnet |
| 10 | **performance-engineer** | application-performance | Inginer performanță expert în observabilitate modernă, optimizare aplicații și performanță sistem scalabil. Stăpânește OpenTelemetry, distributed tracing, load testing, caching multi-tier și Core Web Vitals. | Optimizare performanță end-to-end, implementare OpenTelemetry și APM, load testing cu k6/JMeter, strategii caching multi-tier (Redis, CDN), profiling aplicații, optimizare Core Web Vitals, capacity planning și scalability testing. | sonnet |

---

## Agenți Analizați (11-20)

| Nr. | Nume Agent | Plugin | Descriere | Utilizare Principală | Model |
|-----|------------|--------|-----------|---------------------|-------|
| 11 | **arm-cortex-expert** | arm-cortex-microcontrollers | Expert firmware și driver-uri pentru microcontrolere ARM Cortex-M (Teensy, STM32, nRF52, SAMD). Specializat în dezvoltare firmware fiabilă și optimizată cu expertiză în memory barriers, DMA/cache coherency, interrupt-driven I/O și peripheral drivers. | Dezvoltare driver-uri pentru I²C/SPI/UART/ADC/PWM/USB, implementare ISR și ring buffers, integrare FreeRTOS/Zephyr, optimizare DMA și cache pentru Cortex-M7, debugging hardfault și memory safety patterns pentru embedded systems. | sonnet |
| 12 | **backend-security-coder** | backend-api-security | Expert în practici de coding securizat backend specializat în validare input, autentificare și securitate API. Focus pe implementare hands-on (nu audit), prevenire vulnerabilități și defensive programming. | Implementare JWT cu refresh token rotation, protecție CSRF, validare input cu allowlist, queries parametrizate pentru SQL injection prevention, configurare security headers (CSP, HSTS), rate limiting și DDoS protection, SSRF prevention. | sonnet |
| 13 | **tdd-orchestrator** | backend-development | Master TDD orchestrator specializat în disciplina red-green-refactor, coordonare workflow multi-agent și practici comprehensive de test-driven development. Enforces TDD best practices cu AI-assisted testing și framework-uri moderne. | Orchestrare ciclu TDD complet, coordonare agenți specialized testing (unit, integration, E2E), property-based testing, mutation testing, TDD pentru legacy code, metrics TDD și quality gates, training și governance TDD cross-team. | sonnet |
| 14 | **blockchain-developer** | blockchain-web3 | Developer blockchain specializat în aplicații Web3 production-ready, smart contracts și sisteme descentralizate. Implementează protocoale DeFi, platforme NFT, DAO-uri și integrări blockchain enterprise. | Dezvoltare smart contracts Solidity/Rust, protocoale DeFi (AMM, lending, yield farming), platforme NFT (ERC-721/1155), integrare wallet Web3, Apollo Federation, cross-chain bridges, audit securitate smart contracts, gas optimization. | sonnet |
| 15 | **business-analyst** | business-analytics | Expert business analyst specializat în luarea deciziilor data-driven prin analytics avansat, instrumente BI moderne și business intelligence strategic. Combină proficiență tehnică cu acumen business pentru insights actionabile. | Creare dashboards interactive (Tableau, Power BI, Looker), modelare predictivă cu ML, framework-uri KPI și OKR, analiză CLV și CAC, segmentare clienți, cohort analysis, data storytelling, A/B testing design și market sizing analysis (TAM/SAM/SOM). | haiku |
| 16 | **cloud-architect** | cicd-automation | Arhitect cloud expert în design infrastructură multi-cloud AWS/Azure/GCP, IaC avansat (Terraform/OpenTofu/CDK), optimizare costuri FinOps și pattern-uri arhitecturale moderne. Stăpânește serverless, microservices, securitate, compliance și disaster recovery. | Design arhitecturi resiliente multi-region, implementare Terraform/CDK, optimizare costuri FinOps (right-sizing, reserved instances), arhitecturi serverless și event-driven, zero-trust security, compliance SOC2/HIPAA/PCI-DSS, multi-cloud strategies și DR/BC planning. | sonnet |
| 17 | **deployment-engineer** | cicd-automation | Inginer deployment expert în pipeline-uri CI/CD moderne, workflow-uri GitOps și automatizare deployment avansată. Stăpânește GitHub Actions, ArgoCD/Flux, progressive delivery, container security și platform engineering. | Design pipeline-uri CI/CD cu GitHub Actions/GitLab CI, implementare GitOps cu ArgoCD/Flux, progressive delivery (canary, blue-green), zero-downtime deployments, container security și image scanning, SLSA framework, multi-environment management și developer platform engineering. | haiku |

**Notă:** Agenții **backend-architect** și **graphql-architect** apar în multiple plugin-uri (backend-api-security, backend-development) cu aceeași funcționalitate ca agenții #3 și #6, dar în contexte diferite (securitate, dezvoltare generală).

---

## Agenți Analizați (21-30)

| Nr. | Nume Agent | Plugin | Descriere | Utilizare Principală | Model |
|-----|------------|--------|-----------|---------------------|-------|
| 21 | **devops-troubleshooter** | cicd-automation | Expert DevOps troubleshooter specializat în răspuns rapid incident, debugging avansat și observabilitate modernă. Stăpânește analiza log-uri, distributed tracing, debugging Kubernetes, optimizare performanță și root cause analysis pentru outage-uri production. | Debugging production outages, analiza log-uri cu ELK/Loki, distributed tracing cu Jaeger/OpenTelemetry, troubleshooting Kubernetes (pods, networking, storage), analiza performanță, debugging CI/CD pipeline, incident response și preventive monitoring. | haiku |
| 22 | **kubernetes-architect** | cicd-automation | Expert arhitect Kubernetes specializat în infrastructură cloud-native, GitOps workflows avansate (ArgoCD/Flux) și orchestrare containere enterprise. Stăpânește EKS/AKS/GKE, service mesh (Istio/Linkerd), progressive delivery, multi-tenancy și platform engineering. | Design platforme Kubernetes cloud-native, implementare GitOps cu ArgoCD/Flux, progressive delivery cu Argo Rollouts/Flagger, configurare service mesh, Pod Security Standards, multi-cluster management, cost optimization cu KubeCost, disaster recovery cu Velero. | sonnet |
| 23 | **terraform-specialist** | cicd-automation | Expert Terraform/OpenTofu specializat în automatizare IaC avansată, state management și pattern-uri infrastructură enterprise. Mânuiește design module complexe, deployment-uri multi-cloud, workflow-uri GitOps, policy as code și integrare CI/CD. | Design module Terraform avansate, state management securizat (encryption, locking), deployment-uri multi-cloud, integrare GitOps, policy as code cu OPA/Sentinel, security scanning (tfsec, Checkov), automated testing cu Terratest, migration strategies. | sonnet |
| 24 | **hybrid-cloud-architect** | cloud-infrastructure | Expert arhitect hybrid cloud specializat în soluții complexe multi-cloud across AWS/Azure/GCP și cloud-uri private (OpenStack/VMware). Stăpânește conectivitate hybrid, optimizare workload placement, edge computing și automatizare cross-cloud. | Design arhitecturi hybrid cloud complexe, OpenStack implementation, conectivitate hybrid (Direct Connect, ExpressRoute), workload placement optimization, compliance multi-cloud, data replication cross-cloud, cost optimization hybrid, disaster recovery multi-site. | sonnet |
| 25 | **network-engineer** | cloud-infrastructure | Expert inginer rețea specializat în networking cloud modern, arhitecturi securitate și optimizare performanță. Stăpânește conectivitate multi-cloud, service mesh, zero-trust networking, SSL/TLS, global load balancing și troubleshooting avansat. | Design networking cloud-native (VPC, subnets, routing), global load balancing, DNS și service discovery, SSL/TLS management și PKI, zero-trust architecture, service mesh networking, CDN optimization, network troubleshooting cu tcpdump/Wireshark, VPN și SD-WAN. | haiku |
| 26 | **code-reviewer** | code-documentation | Expert elite code review specializat în analiză cod AI-powered, vulnerabilități securitate, optimizare performanță și production reliability. Stăpânește instrumente static analysis, security scanning și configuration review cu best practices 2024/2025. | Code review comprehensive cu AI tools (CodeQL, Semgrep, SonarQube), security vulnerability detection (OWASP Top 10), performance analysis (N+1 queries, memory leaks), configuration review (K8s, IaC), test coverage analysis, clean code patterns, mentoring feedback. | sonnet |

**Notă:** Agenții **cloud-architect**, **deployment-engineer**, **kubernetes-architect** și **terraform-specialist** apar din nou în plugin-ul `cloud-infrastructure` cu aceeași funcționalitate ca agenții #16, #17, #22, #23.

---

## Observații Generale

### Categorii de Agenți Identificate:
1. **API Development** - Backend architects, Django, FastAPI, GraphQL specialists
2. **Frontend Development** - React, Next.js, UI/UX specialists
3. **Quality Assurance** - Visual validators, testers, TDD orchestrators, security auditors
4. **DevOps & Infrastructure** - Cloud architects, deployment engineers, Kubernetes specialists
5. **Observability & Performance** - Monitoring, logging, performance optimization
6. **AI & ML** - Context management, AI engineers, ML ops
7. **Documentation** - API documenters, technical writers
8. **Security** - Security auditors, security coders, compliance specialists
9. **Blockchain & Web3** - Smart contracts, DeFi protocols, NFT platforms
10. **Embedded Systems** - ARM Cortex-M firmware, microcontroller drivers
11. **Business & Analytics** - Business analysts, BI specialists, data-driven insights

### Modele Utilizate:
- **sonnet** - Cel mai frecvent folosit pentru task-uri complexe și specializate (16/20 agenți)
- **haiku** - Folosit pentru task-uri mai rapide și optimizate (4/20 agenți: context-manager, api-documenter, business-analyst, deployment-engineer)
- **opus** - Nu a fost întâlnit încă în primii 20 de agenți

### Pattern-uri Observate:
- Unii agenți (backend-architect, graphql-architect) apar în multiple plugin-uri pentru contexte diferite
- Majoritatea agenților folosesc modelul **sonnet** pentru task-uri specializate
- Modelul **haiku** este folosit pentru orchestrare, documentație și deployment (task-uri mai rapide)

---

*Documentația va fi actualizată pe măsură ce mai mulți agenți sunt analizați.*

*Ultima actualizare: Primii 30 de agenți analizați (26 unici) din 145 (20.7%)*
*Progres: ████░░░░░░░░░░░░░░░░ 20.7%*

**Notă despre duplicate:** Din 30 de agenți analizați, 26 sunt unici. Unii agenți apar în multiple plugin-uri cu aceeași funcționalitate dar în contexte diferite.
