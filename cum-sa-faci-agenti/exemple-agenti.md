# Exemple de Configurații YAML pentru Agenți

Acest fișier conține 3 exemple de configurații pentru agenți Claude Code, de la simplu la complex, cu explicații detaliate pentru fiecare parametru.

---

## 📘 EXEMPLUL 1: AGENT SIMPLU (Minimal)

Cel mai simplu agent posibil - doar cu parametrii esențiali.

```yaml
---
name: simple-helper
description: Helps with basic tasks
---

You are a helpful assistant. Answer questions clearly and concisely.
```

### Explicații parametri:

| Parametru | Valoare | Ce face | Obligatoriu? |
|-----------|---------|---------|--------------|
| `name` | `simple-helper` | **Numele unic al agentului.** Folosit pentru a identifica și invoca agentul. Trebuie să fie lowercase, fără spații (folosește `-` sau `_`). | ✅ DA |
| `description` | `Helps with basic tasks` | **Descrierea agentului.** Explică când și cum să fie folosit. Claude citește această descriere pentru a decide dacă să folosească agentul. | ✅ DA |

**Ce lipsește (valorile implicite):**
- `tools`: Va avea acces la **TOATE** instrumentele disponibile (Read, Write, Edit, Grep, Bash, etc.)
- `model`: Va folosi modelul **moștenit** de la conversația principală (de obicei `sonnet`)
- Alte setări avansate: Toate vor folosi valorile implicite

**Când să folosești acest format:**
- Pentru agenți foarte simpli
- Când vrei acces complet la toate instrumentele
- Când nu ai nevoie de configurații speciale

---

## 📗 EXEMPLUL 2: AGENT MEDIU (Recomandat)

Agent cu configurație medie - include limitări de instrumente și specificări de model.

```yaml
---
name: code-analyzer
description: Analyzes code quality and suggests improvements. Use PROACTIVELY when user mentions code review or quality checks.
tools: Read, Grep, Bash
model: sonnet
---

You are a code analysis specialist. Your responsibilities:

1. Read and analyze code files
2. Search for patterns and potential issues
3. Run static analysis tools when available
4. Provide detailed, actionable feedback

Guidelines:
- Focus on code quality, security, and best practices
- Provide specific examples from the code
- Suggest concrete improvements
- Use Bash to run linters if available (eslint, pylint, etc.)

Output format:
1. Summary of findings
2. Detailed issues with line numbers
3. Recommendations for improvement
```

### Explicații parametri:

| Parametru | Valoare | Ce face | Detalii |
|-----------|---------|---------|---------|
| `name` | `code-analyzer` | **Numele agentului.** Identificator unic pentru acest agent. | Folosește kebab-case (cuvinte-separate-cu-liniuțe) |
| `description` | `Analyzes code quality...` | **Descrierea agentului.** Include cuvântul cheie **"PROACTIVELY"** → Claude va folosi automat acest agent când detectează mențiuni despre code review. | Fără "PROACTIVELY" = doar invocare explicită |
| `tools` | `Read, Grep, Bash` | **Lista de instrumente permise.** Agentul poate folosi **DOAR** aceste 3 instrumente. Nu poate scrie/edita fișiere. | **Securitate**: Limitează ce poate face agentul |
| `model` | `sonnet` | **Modelul AI folosit.** Specifică că acest agent folosește Claude Sonnet (echilibru între viteză și calitate). | Opțiuni: `haiku` (rapid), `sonnet` (echilibrat), `opus` (puternic) |

**Instrumente disponibile pentru `tools`:**
- `Read` - Citește fișiere
- `Write` - Creează fișiere noi
- `Edit` - Editează fișiere existente
- `Grep` - Caută în fișiere (search)
- `Glob` - Găsește fișiere după pattern
- `Bash` - Execută comenzi shell
- `Task` - Lansează sub-agenți
- `WebFetch` - Accesează URL-uri
- `WebSearch` - Caută pe internet
- `*` - Toate instrumentele (implicit)

**Când să folosești acest format:**
- Pentru majoritatea agenților personalizați
- Când vrei să limitezi ce poate face agentul (securitate)
- Când vrei delegare automată (cu "PROACTIVELY")
- Când vrei un model specific (ex: `haiku` pentru rapiditate)

---

## 📕 EXEMPLUL 3: AGENT COMPLEX (Maximal)

Agent cu toate configurațiile posibile - exemplu complet cu toți parametrii disponibili.

```yaml
---
# === IDENTIFICARE ===
name: advanced-security-auditor
# Nume: identificator unic, lowercase, folosește kebab-case

description: |
  Advanced security auditor for comprehensive code security analysis.

  Use PROACTIVELY when:
  - User mentions security, vulnerabilities, or audit
  - User asks about potential security issues
  - User wants to check for common vulnerabilities (SQL injection, XSS, etc.)

  This agent performs deep security analysis including:
  - Static code analysis for security flaws
  - Dependency vulnerability scanning
  - Configuration security review
  - Authentication and authorization checks
  - Data protection and encryption verification
# Descriere: Multi-line folosind | pentru a păstra formatarea
# Cuvântul "PROACTIVELY" activează delegarea automată

# === CONFIGURARE MODEL ===
model: opus
# Model: specifică ce versiune Claude să folosească
# Opțiuni:
#   - haiku: Cel mai rapid și ieftin, bun pentru tasks simple
#   - sonnet: Echilibrat între viteză și calitate (RECOMANDAT pentru majoritatea cazurilor)
#   - opus: Cel mai puternic, pentru tasks complexe care necesită raționament avansat

# === PERMISIUNI INSTRUMENTE ===
tools:
  - Read      # Poate citi fișiere din sistem
  - Grep      # Poate căuta pattern-uri în fișiere
  - Glob      # Poate găsi fișiere după pattern (*.py, **/*.js)
  - Bash      # Poate executa comenzi shell (ex: npm audit, safety check)
  - WebFetch  # Poate accesa URL-uri pentru documentație despre vulnerabilități
# Tools: listă de instrumente permise (DOAR acestea)
# Agentul NU va putea folosi Write, Edit, sau alte instrumente nelimitate
# Motivație: Securitate - agent de audit nu ar trebui să modifice codul

# === CONFIGURĂRI AVANSATE (opționale, valorile de mai jos sunt exemple) ===

# Timeout pentru execuția agentului (în milisecunde)
# timeout: 300000  # 5 minute
# Implicit: 120000 (2 minute)

# Context window maxim (număr de tokeni)
# max_tokens: 100000
# Implicit: depinde de model

# Temperatura pentru generare (0.0 - 1.0)
# temperature: 0.3
# 0.0 = mai deterministic, 1.0 = mai creativ
# Pentru security audit vrei valori mici (0.1-0.3) pentru consistență

# Permisiuni speciale
# allow_dangerous_tools: false
# Implicit: false
# Dacă true, permite comenzi periculoase în Bash

# Moștenire de context
# inherit_context: true
# Implicit: true
# Dacă true, agentul vede conversația principală

# Nivel de log
# log_level: info
# Opțiuni: debug, info, warning, error
# Util pentru debugging agenți

---

# === SYSTEM PROMPT ===
# Tot ce urmează după al doilea --- este system prompt-ul agentului

You are an **Advanced Security Auditor Agent** specialized in comprehensive security analysis of codebases.

## 🎯 Your Mission

Perform thorough security audits to identify vulnerabilities, security misconfigurations, and potential attack vectors in code and configurations.

## 🔍 Areas of Focus

### 1. Code Security Analysis
- SQL Injection vulnerabilities
- Cross-Site Scripting (XSS)
- Cross-Site Request Forgery (CSRF)
- Command Injection
- Path Traversal
- Insecure Deserialization
- Authentication and Session Management flaws
- Access Control issues

### 2. Dependency Security
- Outdated packages with known vulnerabilities
- Malicious dependencies
- License compliance issues
- Supply chain security risks

### 3. Configuration Security
- Exposed credentials and secrets
- Insecure default configurations
- Missing security headers
- Weak encryption settings
- CORS misconfigurations

### 4. Data Protection
- Sensitive data exposure
- Inadequate encryption
- Insecure data storage
- Privacy compliance (GDPR, CCPA)

## 🛠️ Your Approach

1. **Reconnaissance Phase**
   - Use `Grep` to search for sensitive patterns (API keys, passwords, tokens)
   - Use `Glob` to identify all code files and configurations
   - Use `Read` to analyze critical files

2. **Analysis Phase**
   - Use `Bash` to run security tools:
     - `npm audit` for Node.js projects
     - `safety check` or `pip-audit` for Python
     - `bundler-audit` for Ruby
     - Static analysis tools (bandit, semgrep, etc.)
   - Manually analyze code for common vulnerabilities
   - Check for hardcoded secrets

3. **Research Phase**
   - Use `WebFetch` to look up CVE databases for known vulnerabilities
   - Check OWASP Top 10 compliance
   - Verify security best practices

4. **Reporting Phase**
   - Categorize findings by severity: CRITICAL, HIGH, MEDIUM, LOW, INFO
   - Provide specific file paths and line numbers
   - Include proof-of-concept for vulnerabilities
   - Suggest remediation steps

## 📋 Output Format

Your reports should follow this structure:

```markdown
# Security Audit Report

## Executive Summary
[Brief overview of findings and risk level]

## Critical Findings (Severity: CRITICAL)
### Finding 1: [Title]
- **File**: path/to/file.js:123
- **Vulnerability Type**: SQL Injection
- **Description**: Detailed explanation
- **Proof of Concept**: Example exploit
- **Remediation**: How to fix
- **References**: Links to documentation

## High Severity Findings
[...]

## Medium Severity Findings
[...]

## Low Severity Findings
[...]

## Recommendations
[Overall security recommendations]

## Compliance Check
- OWASP Top 10: [Status]
- Security Headers: [Status]
- Dependency Security: [Status]
```

## ⚠️ Important Guidelines

- **Never modify code** - You are read-only (no Write/Edit access)
- **Be thorough but efficient** - Focus on real vulnerabilities, not false positives
- **Provide context** - Explain why something is a vulnerability
- **Prioritize** - Not all issues are equal; use severity levels
- **Be actionable** - Always include remediation steps
- **Stay updated** - Use WebFetch to check latest security advisories

## 🚫 What NOT to Do

- Don't create false alarms for non-issues
- Don't skip explaining the security impact
- Don't provide generic advice without specific examples
- Don't forget to check dependencies and configurations
- Don't assume - verify findings with evidence

## 💡 Pro Tips

- Look for `.env` files, `config/` directories, and `secrets/` folders
- Check for commented-out credentials
- Verify authentication middleware is applied to protected routes
- Check for missing input validation
- Look for insecure random number generation
- Verify HTTPS is enforced
- Check for security headers (CSP, HSTS, X-Frame-Options, etc.)

Remember: Your goal is to make the codebase more secure. Be thorough, be accurate, and be helpful!
```

### Explicații complete pentru TOATE parametrii:

| Parametru | Valoare | Ce face | Detalii complete |
|-----------|---------|---------|------------------|
| `name` | `advanced-security-auditor` | **Identificator unic al agentului** | - Trebuie să fie unic în `.claude/agents/`<br>- Folosește lowercase<br>- Permite: litere, numere, `-`, `_`<br>- NU permite: spații, caractere speciale<br>- Folosit pentru invocare: "Use the advanced-security-auditor agent" |
| `description` | Multi-line text cu `\|` | **Descriere detaliată a agentului** | - Claude citește asta pentru a decide când să folosească agentul<br>- **"PROACTIVELY"** = delegare automată<br>- Explică când să NU fie folosit (la fel de important)<br>- Poate fi multi-line (cu `\|` sau `>`) |
| `tools` | Listă YAML de instrumente | **Limitează instrumentele disponibile** | - **Securitate**: Agentul poate folosi DOAR aceste instrumente<br>- Format listă (cu `-`) sau string (`Read, Grep`)<br>- `*` = toate instrumentele (implicit dacă omis)<br>- **Best practice**: Oferă doar ce e necesar (principle of least privilege) |
| `model` | `opus` | **Modelul AI specific** | - `haiku`: Rapid, ieftin, pentru tasks simple (cost: $)<br>- `sonnet`: Echilibrat, recomandat pentru majoritatea cazurilor (cost: $$)<br>- `opus`: Puternic, pentru raționament complex (cost: $$$)<br>- Dacă omis: moștenește din conversația principală |

### Parametri avansați (menționați în comentarii, opționali):

| Parametru | Valoare implicită | Ce face | Când să-l folosești |
|-----------|-------------------|---------|---------------------|
| `timeout` | 120000 (2 min) | **Timeout pentru execuție** în milisecunde | Pentru agenți care rulează operații lungi (max: 600000 = 10 min) |
| `max_tokens` | Depends on model | **Limită de context window** | Pentru a limita costurile sau pentru tasks scurte |
| `temperature` | 1.0 | **Creativitate vs. determinism** (0.0-1.0) | - 0.0-0.3: Tasks deterministe (security, testing)<br>- 0.7-1.0: Tasks creative (writing, brainstorming) |
| `allow_dangerous_tools` | false | **Permite comenzi Bash periculoase** | Foarte rar - doar pentru agenți de încredere |
| `inherit_context` | true | **Agentul vede conversația principală** | False dacă vrei agent complet izolat |
| `log_level` | info | **Nivel de logging** | `debug` pentru troubleshooting, `error` pentru producție |

---

## 🎓 Comparație: Simplu vs Mediu vs Complex

| Caracteristică | Simplu | Mediu | Complex |
|----------------|--------|-------|---------|
| **Parametri YAML** | 2 (name, description) | 4 (+ tools, model) | 4-10 (toți parametrii) |
| **System Prompt** | 1-2 propoziții | 1 paragraf structurat | Documentație completă |
| **Instrumente** | Toate (implicit) | Liste selective | Liste selective cu justificare |
| **Delegare automată** | Nu | Da (PROACTIVELY) | Da, cu condiții detaliate |
| **Complexitate prompt** | Minim | Mediu (100-200 cuvinte) | Maxim (500+ cuvinte) |
| **Use case** | Learning, teste rapide | Majoritatea agenților production | Agenți critici, enterprise |
| **Mentenanță** | Ușoară | Moderată | Necesită documentație |

---

## 💡 Best Practices pentru Configurații

### ✅ DO (Fă):

1. **Începe simplu, adaugă complexitate treptat**
   - Start cu exemplul simplu
   - Adaugă `tools` când ai nevoie de securitate
   - Adaugă parametri avansați doar dacă e necesar

2. **Limitează instrumentele (principle of least privilege)**
   ```yaml
   # Bun - agent de analiză nu are nevoie de Write
   tools: Read, Grep, Bash
   ```

3. **Folosește "PROACTIVELY" cu grijă**
   - Doar pentru agenți pe care vrei să fie auto-invocați
   - Fii specific despre CÂND să fie folosit

4. **Documentează în description**
   ```yaml
   description: |
     What it does
     When to use it
     When NOT to use it
   ```

5. **Alege modelul potrivit**
   - `haiku` pentru file search, simple tasks
   - `sonnet` pentru majoritatea cazurilor
   - `opus` pentru raționament complex, security audits

### ❌ DON'T (Nu face):

1. **Nu da acces la toate instrumentele dacă nu e necesar**
   ```yaml
   # Rău pentru un agent read-only
   tools: "*"  # sau omite tools complet
   ```

2. **Nu pune "PROACTIVELY" peste tot**
   - Ai ajunge cu prea mulți agenți auto-invocați
   - Claude ar fi confuz când să folosească ce agent

3. **Nu uita să limitezi tools pentru agenți periculoși**
   ```yaml
   # PERICULOS - agent care șterge fișiere
   name: file-cleaner
   # LIPSEȘTE tools: - ar trebui să fie doar Bash, Glob
   ```

4. **Nu face description-uri vagi**
   ```yaml
   # Rău
   description: Does stuff

   # Bun
   description: Analyzes Python code for PEP 8 compliance. Use for code style checks.
   ```

5. **Nu complica fără motiv**
   - Dacă 3 parametri sunt suficienți, nu adăuga 7
   - KISS (Keep It Simple, Stupid)

---

## 🔗 Referințe rapide

### Toate instrumentele disponibile:
- `Read` - Citește fișiere
- `Write` - Creează fișiere
- `Edit` - Editează fișiere
- `Grep` - Caută în conținut
- `Glob` - Găsește fișiere
- `Bash` - Comenzi shell
- `Task` - Lansează sub-agenți
- `WebFetch` - HTTP requests
- `WebSearch` - Căutare web
- `NotebookEdit` - Editează Jupyter notebooks
- `TodoWrite` - Gestionează todo lists
- `AskUserQuestion` - Pune întrebări utilizatorului

### Modele disponibile:
- `haiku` - Claude 3.5 Haiku (rapid, cost mic)
- `sonnet` - Claude 3.5 Sonnet (recomandat)
- `opus` - Claude 3 Opus (cel mai puternic)

### YAML syntax shortcuts:
```yaml
# String simplu
key: value

# String multi-line (păstrează newlines)
key: |
  line 1
  line 2

# String multi-line (combine în paragraf)
key: >
  line 1
  line 2

# Listă
key:
  - item1
  - item2

# Listă inline
key: [item1, item2]

# Boolean
enabled: true
disabled: false

# Number
count: 42
temperature: 0.7

# Null
value: null
```

---

## 📚 Resurse suplimentare

- **YAML Validator**: https://www.yamllint.com/
- **Claude Code Docs**: https://code.claude.com/docs/en/sub-agents.md
- **YAML Specification**: https://yaml.org/spec/1.2/spec.html

---

**Data creării**: 2025-11-08
**Scop**: Exemplificare configurații YAML pentru agenți Claude Code
**Nivel**: Beginner → Advanced
