# Tutorial: Cum să folosești Agenți în Claude Code

## Ce sunt agenții (subagents)?

Agenții sunt asistenți AI specializați pe care Claude Code îi poate delega pentru sarcini specifice. Fiecare agent operează cu propriul său context window și poate fi configurat cu propriile prompt-uri de sistem și acces la instrumente.

## Cum să invoici agenții

### 1. Delegare automată

Claude Code va delega automat sarcini către agenți potriviți în funcție de:
- Descrierea sarcinii
- Configurația agenților
- Instrumentele disponibile

**Nu trebuie să faci nimic special** - Claude va decide singur când să folosească un agent dacă acesta are în descriere "use PROACTIVELY".

### 2. Invocare explicită

Poți cere explicit să se folosească un anumit agent:

**Exemple de comenzi:**
```
"Folosește agentul code-reviewer să verifice modificările mele recente"

"Cere agentului debugger să investigheze această eroare"

"Întreabă agentul data-scientist să analizeze aceste rezultate"

"Folosește agentul Explore să găsești toate fișierele de configurare"
```

## Tipuri de agenți disponibili

### Agenți built-in (predefiniti)

1. **Plan (Plan subagent)**
   - Folosit pentru cercetarea codului în modul plan
   - Analizează codul fără să facă modificări
   - Ideal pentru refactorizări complexe

2. **Explore**
   - Specializat în explorarea rapidă a bazei de cod
   - Găsește fișiere după pattern-uri (ex: "src/components/**/*.tsx")
   - Caută cuvinte cheie în cod
   - Răspunde la întrebări despre arhitectura codului

3. **Code-reviewer**
   - Evaluează calitatea codului
   - Verifică securitatea
   - Sugerează îmbunătățiri de mentenabilitate

4. **Debugger**
   - Efectuează analiză root cause pentru erori
   - Investighează probleme complexe

5. **Data-scientist**
   - Gestionează query-uri SQL
   - Analizează date
   - Creează vizualizări

### Agenți personalizați

Poți crea propriii agenți la două nivele:
- **La nivel de proiect**: `.claude/agents/` (se sincronizează cu Git)
- **La nivel de utilizator**: `~/.claude/agents/` (disponibili în toate proiectele)

## Gestionarea agenților

### Comanda /agents

Folosește `/agents` pentru:
- ✅ Vizualizarea tuturor agenților disponibili
- ✅ Crearea de agenți noi cu asistență pas cu pas
- ✅ Editarea agenților existenți
- ✅ Ștergerea agenților personalizați
- ✅ Configurarea permisiunilor pentru instrumente

### Gestionare manuală

Agenții sunt stocați ca fișiere Markdown cu YAML frontmatter:

```markdown
---
name: numele-agentului
description: Când și cum să folosești acest agent
tools: Read, Edit, Bash  # Opțional - limitează instrumentele
model: sonnet  # Opțional - specifică modelul
---

Prompt-ul de sistem care definește rolul, abordarea și instrucțiunile specifice.
```

## Exemple practice pas cu pas

### Exemplul 1: Explorarea bazei de cod

**Scenariu**: Vrei să înțelegi unde sunt gestionate erorile de autentificare

**Pași**:
```
Tu: "Unde sunt gestionate erorile de autentificare?"
```

Claude va folosi automat agentul **Explore** pentru a:
1. Căuta pattern-uri relevante
2. Explora fișierele de configurare
3. Identifica funcțiile de handling a erorilor

### Exemplul 2: Review de cod

**Scenariu**: Ai scris o funcție nouă și vrei feedback

**Pași**:
```
Tu: "Folosește code-reviewer să verifice funcția pe care tocmai am scris-o"
```

Agentul **Code-reviewer** va:
1. Analiza codul pentru vulnerabilități
2. Verifica best practices
3. Sugera îmbunătățiri

### Exemplul 3: Debug complex

**Scenariu**: Ai o eroare pe care nu o înțelegi

**Pași**:
```
Tu: "Cere agentului debugger să investigheze această eroare de null pointer"
```

Agentul **Debugger** va:
1. Analiza stack trace-ul
2. Examina codul relevant
3. Identifica cauza root
4. Propune soluții

### Exemplul 4: Planificarea unei refactorizări

**Scenariu**: Vrei să refactorizezi o parte mare din cod

**Pași**:
```
Tu: "Vreau să refactorizez sistemul de autentificare. Hai să planificăm mai întâi."
```

Claude va activa automat modul **Plan** și:
1. Va explora codul existent
2. Va identifica dependențele
3. Va crea un plan detaliat de refactorizare
4. Va cere aprobarea ta înainte de implementare

## Best Practices (Cele mai bune practici)

### 1. Design-ul agenților

✅ **DO:**
- Creează agenți cu responsabilități clare și unice
- Scrie prompt-uri de sistem detaliate
- Limitează accesul la instrumente doar la cele necesare
- Adaugă "use PROACTIVELY" în descriere pentru delegare automată

❌ **DON'T:**
- Nu încerca să faci un agent universal care face totul
- Nu da acces la toate instrumentele dacă nu sunt necesare
- Nu uita să documentezi când și cum ar trebui folosit agentul

### 2. Utilizare eficientă

**Pentru sarcini complexe:**
```
Tu: "Folosește mai mulți agenți pentru această sarcină:
1. Explore pentru a înțelege structura
2. Plan pentru a crea strategia
3. Code-reviewer pentru verificare finală"
```

**Pentru context lung:**
Poți relua un agent folosind `agentId` pentru a menține contextul:
```
Tu: "Reia agentul cu id-ul agent_123 pentru a continua analiza"
```

### 3. Version control

- Păstrează agenții la nivel de proiect în `.claude/agents/`
- Commitează-i în Git pentru a-i partaja cu echipa
- Documentează scopul fiecărui agent în README

## Fluxuri de lucru comune

### Workflow 1: Dezvoltare nouă funcționalitate

```
1. Tu: "Folosește Explore să găsești unde sunt implementate features similare"
2. Claude folosește Explore agent
3. Tu: "Hai să planificăm implementarea"
4. Claude activează Plan mode
5. Tu: "Aprobat, implementează"
6. Claude implementează
7. Tu: "Code-reviewer să verifice modificările"
8. Claude folosește Code-reviewer agent
```

### Workflow 2: Debugging și fixing

```
1. Tu: "Am o eroare aici: [stack trace]"
2. Claude folosește Debugger agent automat
3. Agentul identifică problema
4. Tu: "Fixează problema"
5. Claude fixează
6. Tu: "Rulează testele să verificăm"
7. Claude rulează testele
```

### Workflow 3: Analiză de date

```
1. Tu: "Folosește data-scientist să analizeze aceste date din baza de date"
2. Claude folosește Data-scientist agent
3. Agentul scrie și rulează query-uri SQL
4. Agentul generează rapoarte și vizualizări
```

## Structura unui agent personalizat - Exemplu complet

```markdown
---
name: api-documenter
description: Generates API documentation from code. Use PROACTIVELY when user asks to document API endpoints.
tools: Read, Grep, Write
model: sonnet
---

You are an API documentation specialist. Your role is to:

1. Analyze API endpoint implementations
2. Extract route definitions, parameters, and response types
3. Generate comprehensive API documentation in OpenAPI/Swagger format

Guidelines:
- Always include request/response examples
- Document all error cases
- Add authentication requirements
- Include rate limiting information if present

Output format: Create a well-structured markdown file with:
- Endpoint overview table
- Detailed documentation for each endpoint
- Example requests and responses
- Authentication section
- Error codes reference
```

## Întrebări frecvente (FAQ)

**Î: Cum știu care agent se folosește?**
R: Claude îți va spune când folosește un agent. Vei vedea mesaje ca "I'm going to use the Explore agent" sau "Using the Task tool to launch the code-reviewer agent".

**Î: Pot opri delegarea automată?**
R: Da, poți cere explicit să nu folosești agenți sau poți modifica configurația agenților pentru a elimina "use PROACTIVELY" din descriere.

**Î: Cât de mult context păstrează un agent?**
R: Fiecare agent are propriul context window. Pentru sarcini lungi, poți relua un agent folosind ID-ul său.

**Î: Pot crea agenți care să folosească instrumente personalizate?**
R: Da, poți specifica în parametrul `tools` orice instrumente disponibile în Claude Code.

**Î: Cum văd ce agenți am disponibili?**
R: Rulează comanda `/agents` pentru a vedea toți agenții disponibili și configurările lor.

---

# 🎓 LEARNING PATH INTERACTIV

Parcurge acest traseu de învățare pas cu pas pentru a stăpâni utilizarea agenților în Claude Code. Vom lucra împreună și voi actualiza progresul tău pe măsură ce avansezi!

## 📊 Progres General

- [ ] **Nivel 1: Începător** (0/5 exerciții completate)
- [ ] **Nivel 2: Intermediar** (0/5 exerciții completate)
- [ ] **Nivel 3: Avansat** (0/4 exerciții completate)
- [ ] **Proiect Final** (0/1 completat)

**Progres total: 0/15 exerciții (0%)**

---

## 🌱 NIVEL 1: ÎNCEPĂTOR

**Obiectiv:** Familiarizare cu agenții built-in și invocare de bază

### Exercițiul 1.1: Prima ta interacțiune cu un agent
- [ ] **Status:** Neînceput
- **Sarcină:** Rulează comanda `/agents` și explorează agenții disponibili
- **Ce vei învăța:** Să vezi ce agenți sunt disponibili în sistemul tău
- **Când ești gata:** Spune-mi "Am rulat /agents" și descrie-mi ce agenți ai văzut

**Instrucțiuni:**
Pur și simplu scrie `/agents` în conversație și observă lista de agenți disponibili.

---

### Exercițiul 1.2: Invocare explicită - Explore Agent
- [ ] **Status:** Neînceput
- **Sarcină:** Cere-mi să folosesc agentul Explore pentru a găsi toate fișierele `.md` din proiectul tău
- **Ce vei învăța:** Cum să ceri explicit un agent să facă o sarcină
- **Când ești gata:** Spune-mi "Folosește agentul Explore să găsești toate fișierele .md"

**Instrucțiuni:**
Formulează o cerere explicită către mine pentru a folosi agentul Explore. Observă cum răspund și cum folosesc agentul.

---

### Exercițiul 1.3: Înțelegerea output-ului unui agent
- [ ] **Status:** Neînceput
- **Sarcină:** După ce agentul Explore își termină căutarea, identifică câte fișiere `.md` au fost găsite
- **Ce vei învăța:** Să interpretezi rezultatele returnate de un agent
- **Când ești gata:** Spune-mi câte fișiere au fost găsite și listează-le

**Instrucțiuni:**
Citește cu atenție output-ul pe care ți l-am dat și extrage informația relevantă.

---

### Exercițiul 1.4: Code Review simplu
- [ ] **Status:** Neînceput
- **Sarcină:** Creează un fișier Python simplu cu o funcție care adună două numere, apoi cere-mi să folosesc code-reviewer pentru a o analiza
- **Ce vei învăța:** Cum funcționează agentul code-reviewer pe cod simplu
- **Când ești gata:** Spune-mi "Creează o funcție Python simplă și apoi folosește code-reviewer să o verifice"

**Instrucțiuni:**
Voi crea o funcție simplă și apoi voi folosi code-reviewer. Observă ce fel de feedback oferă agentul.

---

### Exercițiul 1.5: Delegare automată
- [ ] **Status:** Neînceput
- **Sarcină:** Pune-mi o întrebare generală despre structura proiectului (ex: "Care este structura generală a proiectului?")
- **Ce vei învăța:** Cum Claude decide automat ce agent să folosească
- **Când ești gata:** Pune-mi întrebarea și observă dacă folosesc un agent automat

**Instrucțiuni:**
Nu specifica ce agent să folosesc - lasă-mă să decid automat. Observă procesul de decizie.

---

## 🚀 NIVEL 2: INTERMEDIAR

**Obiectiv:** Lucrul cu agenți multipli și scenarii mai complexe

### Exercițiul 2.1: Crearea primului tău agent personalizat
- [ ] **Status:** Neînceput
- **Sarcină:** Creează un agent personalizat simplu care documentează funcții Python
- **Ce vei învăța:** Structura unui agent și cum să îl configurezi
- **Când ești gata:** Spune-mi "Vreau să creez un agent care documentează funcții Python"

**Instrucțiuni:**
Voi folosi `/agents` pentru a crea împreună un agent personalizat. Vei învăța despre frontmatter YAML și system prompts.

---

### Exercițiul 2.2: Testarea agentului personalizat
- [ ] **Status:** Neînceput
- **Sarcină:** Folosește agentul pe care l-ai creat pentru a documenta o funcție Python
- **Ce vei învăța:** Cum să testezi și validezi un agent personalizat
- **Când ești gata:** Cere-mi explicit să folosesc agentul tău personalizat pe o funcție

**Instrucțiuni:**
După ce am creat agentul, hai să îl testăm pe cod real pentru a vedea dacă funcționează conform așteptărilor.

---

### Exercițiul 2.3: Workflow cu 2 agenți
- [ ] **Status:** Neînceput
- **Sarcină:** Orchestrează un workflow care folosește 2 agenți: Explore pentru a găsi cod, apoi Code-reviewer pentru a-l analiza
- **Ce vei învăța:** Cum să combini mai mulți agenți într-un flux de lucru
- **Când ești gata:** Spune-mi "Folosește Explore să găsești funcțiile Python, apoi code-reviewer să le analizeze"

**Instrucțiuni:**
Vei învăța să coordonezi mai mulți agenți pentru o sarcină complexă. Observă cum output-ul unui agent devine input pentru altul.

---

### Exercițiul 2.4: Debugging cu agentul specializat
- [ ] **Status:** Neînceput
- **Sarcină:** Creează intenționat o funcție cu un bug (ex: division by zero), apoi cere-mi să folosesc debugger agent
- **Ce vei învăța:** Cum funcționează agentul debugger și ce informații oferă
- **Când ești gata:** Spune-mi "Creează o funcție cu un bug și folosește debugger să îl găsești"

**Instrucțiuni:**
Voi crea cod cu bug și voi folosi agentul debugger pentru a identifica problema. Observă procesul de analiză.

---

### Exercițiul 2.5: Plan Mode pentru refactorizare
- [ ] **Status:** Neînceput
- **Sarcină:** Cere-mi să planific refactorizarea unui fișier de cod (fără să implementez)
- **Ce vei învăța:** Cum funcționează Plan mode și cum ajută la planificare
- **Când ești gata:** Spune-mi "Hai să planificăm refactorizarea fișierului X (alege un fișier din proiect)"

**Instrucțiuni:**
Voi activa Plan mode pentru a crea un plan detaliat. Vei învăța diferența între planificare și execuție.

---

## 💎 NIVEL 3: AVANSAT

**Obiectiv:** Scenarii complexe, optimizări și best practices

### Exercițiul 3.1: Agent personalizat avansat cu multiple tools
- [ ] **Status:** Neînceput
- **Sarcină:** Creează un agent complex care poate să citească, să analizeze și să modifice cod (cu tools: Read, Grep, Edit, Bash)
- **Ce vei învăța:** Configurare avansată cu permisiuni pentru multiple instrumente
- **Când ești gata:** Spune-mi "Vreau să creez un agent avansat pentru refactorizare automată"

**Instrucțiuni:**
Vom crea împreună un agent sofisticat cu capabilități extinse și vom discuta despre securitate și permisiuni.

---

### Exercițiul 3.2: Workflow cu 3+ agenți în cascadă
- [ ] **Status:** Neînceput
- **Sarcină:** Orchestrează un workflow complex: Explore → Plan → Implementare → Code-reviewer
- **Ce vei învăța:** Management de workflow-uri complexe cu mai mulți agenți
- **Când ești gata:** Spune-mi "Vreau să implementăm o funcționalitate nouă folosind un workflow complet cu mai mulți agenți"

**Instrucțiuni:**
Vei coordona un proces complet de dezvoltare folosind mai mulți agenți specializați. Vei învăța despre orchestrare și handoff între agenți.

---

### Exercițiul 3.3: Optimizare și configurare tool permissions
- [ ] **Status:** Neînceput
- **Sarcină:** Ia un agent existent și optimizează-i configurația (limitează tools, optimizează prompt-ul, ajustează model-ul)
- **Ce vei învăța:** Best practices pentru performanță și securitate
- **Când ești gata:** Spune-mi "Vreau să optimizăm agentul X pentru performanță mai bună"

**Instrucțiuni:**
Vom analiza un agent și vom face optimizări: limitare de permisiuni, îmbunătățire de prompts, alegere de model potrivit.

---

### Exercițiul 3.4: Error handling și recovery
- [ ] **Status:** Neînceput
- **Sarcină:** Creează un scenariu unde un agent întâmpină o eroare și învață să gestionezi situația
- **Ce vei învăța:** Cum să gestionezi erorile și să recuperezi contextul
- **Când ești gata:** Spune-mi "Vreau să învăț cum să gestionez erorile când un agent eșuează"

**Instrucțiuni:**
Vom simula scenarii de eroare și vei învăța strategii de recovery și debugging pentru agenți.

---

## 🏆 PROIECT FINAL: Sistem complet de agenți

### Proiect: Creează un sistem de agenți pentru un mini-proiect
- [ ] **Status:** Neînceput
- **Descriere:** Creează un set de 3-4 agenți personalizați care lucrează împreună pentru un scop specific (ex: sistem de documentare automată, sistem de code review, sau sistem de testing)
- **Ce vei învăța:** Să aplici tot ce ai învățat într-un proiect real
- **Componentele necesare:**
  - [ ] Cel puțin 3 agenți personalizați cu roluri distincte
  - [ ] Un workflow documentat care coordonează agenții
  - [ ] Teste pentru fiecare agent
  - [ ] Documentație completă în README
- **Când ești gata:** Spune-mi "Sunt gata să încep proiectul final" și descrie-mi ce sistem vrei să construiești

**Instrucțiuni:**
Acesta este proiectul culminant. Vom lucra împreună pentru a construi un sistem complet funcțional de agenți. Vei aplica toate conceptele învățate.

---

## 📈 Cum să folosești acest Learning Path

### Reguli:

1. **Parcurge în ordine:** Fiecare nivel construiește pe cunoștințele anterioare
2. **Nu sări peste exerciții:** Fiecare exercițiu învață un concept important
3. **Cere ajutor când ai nevoie:** Spune-mi dacă ceva nu e clar
4. **Experimentează:** După fiecare exercițiu, încearcă variații proprii

### Cum actualizez progresul:

După fiecare exercițiu completat, spune-mi:
```
"Am completat exercițiul X.Y"
```

Voi actualiza automat:
- Checkbox-ul exercițiului ca `[x]`
- Status-ul ca "Completat ✅"
- Progresul nivelului
- Progresul total

### Comenzi utile în timpul învățării:

```
"Arată-mi progresul" - Vezi un rezumat al progresului tău
"Repetă exercițiul X.Y" - Repetă un exercițiu specific
"Vreau să trec la nivelul următor" - Sari la nivelul următor (doar dacă ai completat nivelul curent)
"Am nevoie de ajutor la exercițiul X.Y" - Primești ajutor specific
```

---

## 🎯 Începe acum!

**Ești gata să începi?**

Spune-mi simplu: **"Hai să începem cu Exercițiul 1.1"** și pornim împreună în această aventură! 🚀

După ce completezi fiecare exercițiu, voi actualiza acest document pentru a reflecta progresul tău. Vei vedea checkboxurile bifate și procentele crescând pe măsură ce avansezi.

**Nota:** Progresul tău este salvat în acest fișier, deci poți reveni oricând și continua de unde ai rămas!

---

## Concluzie

Agenții în Claude Code sunt instrumente puternice pentru:
- 🎯 Specializarea sarcinilor
- 📊 Gestionarea contextului
- ⚡ Creșterea eficienței
- 🔄 Automatizarea workflow-urilor

**Începe simplu:**
1. Folosește agenții built-in pentru a te familiariza
2. Învață să ceri explicit agenți specifici
3. Creează-ți propriii agenți pentru nevoile tale
4. Construiește workflow-uri complexe cu mai mulți agenți

**Resurse utile:**
- Documentație oficială: https://code.claude.com/docs/en/sub-agents.md
- Exemple de agenți: `.claude/agents/` în proiectele tale
- Comenzi: `/agents` și `/help`

Succes în utilizarea agenților! 🚀
