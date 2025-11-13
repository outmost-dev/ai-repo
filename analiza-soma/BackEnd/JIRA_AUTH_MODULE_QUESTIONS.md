# JIRA_AUTH_MODULE - Chestionar Clarificare (SCA)

**Document evaluat**: `BackEnd/JIRA_AUTH_MODULE.txt`
**Data evaluării**: 2025-01-13
**Scor actual**: 92/100 (CONDITIONAL APPROVAL)
**Scor așteptat după clarificare**: 97-100/100

---

## Instrucțiuni

1. **Citește fiecare întrebare** și contextul asociat
2. **Răspunde în secțiunea "RĂSPUNSUL TĂU"** sub fiecare întrebare
3. **Păstrează formatarea** (nu șterge întrebările sau structura)
4. **Salvează fișierul** când ai terminat
5. **Notifică Claude** în chat: "Am completat chestionarul pentru JIRA_AUTH_MODULE"

---

## SECȚIUNEA 1: Error Handling (4 întrebări)

### M1: Rate limiting pentru conturi inactive

**Context**:
În TASK 1.1.2, există logică de rate limiting pentru login-uri eșuate. Însă nu este clar dacă rate limiting-ul se aplică și la încercări de login cu conturi inactive (care returnează eroare specifică "Account is not active").

**Risc**:
Dacă rate limiting nu se aplică la conturi inactive, un atacator poate face enumerare de conturi (distinge între "parolă greșită" și "cont inactiv").

**Întrebare**:
Ar trebui ca rate limiting-ul să se aplice uniform pentru TOATE încercările de login eșuate (inclusiv conturi inactive)?

**Recomandare SCA**: DA - aplică rate limiting uniform pentru a preveni enumerarea de conturi.

**RĂSPUNSUL TĂU**:
```
[Scrie DA/NU sau o altă strategie]


```

---

### M2: Sanitizarea erorilor SMTP

**Context**:
În TASK 1.3.4, se trimite email de validare prin Postmark. Dacă Postmark returnează eroare SMTP (ex: adresă invalidă, server indisponibil), nu este clar dacă detaliile erorii trebuie sanitizate înainte de a fi afișate utilizatorului.

**Risc**:
Expunerea detaliilor SMTP poate dezvălui informații despre server, logica de validare, sau adrese de email.

**Întrebare**:
Ar trebui ca erorile SMTP să fie sanitizate pentru utilizatori (ex: "Email sending failed, please try again later") în timp ce detaliile complete sunt loggate server-side?

**Recomandare SCA**: DA - returnează mesaj generic către user, loghează detalii complete server-side.

**RĂSPUNSUL TĂU**:
```
[Scrie DA/NU sau o altă strategie]


```

---

### M3: Strategia de migrare pentru bug-uri cunoscute ⭐ CRITIC

**Context**:
În TASK 1.5.4 (Signout), documentația menționează EXPLICIT bug-uri în codul legacy:
- Comentariu "// Not working..."
- Nume greșit de cookie 'acess_token' (typo, ar trebui 'access_token')

**Risc**:
Dacă migrezi bug-urile în platforma nouă, înfrângi strategia "Audit-First" (nu migra bug-uri din platforma veche). Acest bug face ca signout să nu funcționeze corect.

**Întrebare**:
Ar trebui ca migrația .NET să CORECTEZE aceste bug-uri (typo, logică defectă) în loc să le reproducă exact?

**Recomandare SCA**: DA CRITIC - Corectează TOATE bug-urile în timpul migrației (typo, logică), NU reproduci bug-uri.

**RĂSPUNSUL TĂU**:
```
[Scrie DA/NU sau o altă strategie]


```

---

### M4: Strategia pentru eșecurile serviciilor externe

**Context**:
Modulul AUTH integrează 7 servicii externe:
1. Stripe (creare customer)
2. Postmark (trimitere email)
3. MailerLite (campanii marketing)
4. Redis (blacklist tokens)
5. Vimeo OAuth
6. Facebook Pixel
7. FirstPromoter

Nu există documentație despre ce se întâmplă când aceste servicii eșuează (timeout, eroare 500, rate limit, etc.).

**Risc**:
Failure în cascadă, experiență proastă pentru user, operații incomplete.

**Întrebare**:
Ce strategie de error handling vrei pentru serviciile externe? (ex: retry cu exponential backoff, circuit breaker, fallback behavior, timeout-uri)

**Recomandare SCA**:
- **Retry**: 3 reîncercări cu exponential backoff (1s, 2s, 4s)
- **Circuit breaker**: Dacă serviciu eșuează de 5 ori consecutiv, nu mai încerca timp de 60s
- **Fallback**: Pentru servicii non-critice (Facebook Pixel, FirstPromoter), continuă fără ele
- **Timeout-uri**: Stripe 10s, Postmark 5s, Redis 1s

**RĂSPUNSUL TĂU**:
```
[Descrie strategia ta sau confirmă recomandarea SCA]




```

---

## SECȚIUNEA 2: Business Rules (3 întrebări)

### M5: Securitatea cheilor de recuperare (recovery keys)

**Context**:
În TASK 1.4.1, se generează chei de recuperare care permit setarea unei parole noi FĂRĂ să cunoști parola veche. Documentația nu specifică:
- Sunt stocate în plain text sau hash-uite?
- Au expirare sau sunt valabile permanent?

**Risc**:
- Dacă baza de date este compromisă, atacatorul obține chei de recuperare în plain text (backdoor permanent)
- Dacă nu expiră, user-ul nu are urgență să folosească cheia (poate fi furat mai târziu)

**Întrebare**:
Ar trebui ca recovery keys să fie:
1. Hash-uite cu Argon2 (ca parolele)
2. Să expire după 1 oră
3. Să fie regenerate după utilizare (one-time use)

**Recomandare SCA**: DA la toate 3 - hash cu Argon2, expirare 1h, regenerare după folosire.

**RĂSPUNSUL TĂU**:
```
[Scrie DA/NU sau o altă strategie]




```

---

### M6: Strategia de normalizare pentru email

**Context**:
În TASK 1.1.1 și 1.2.2, se validează unicitatea email-ului. Însă nu este clar CÂND se face normalizarea (lowercase):
- La validare input (înainte de validare)?
- La stocare în DB (înainte de INSERT)?
- La comparație (în query-uri)?

**Risc**:
Conturi duplicate (test@example.com vs TEST@example.com), comportament inconsistent.

**Întrebare**:
Când ar trebui să se facă normalizarea email-ului?

**Recomandare SCA**: La TOATE TREI punctele:
1. **La validare**: Convertește la lowercase înainte de validare format
2. **La stocare**: Stochează ÎNTOTDEAUNA lowercase în DB
3. **La comparație**: Query-uri case-insensitive (dar redundant dacă stochezi lowercase)

**RĂSPUNSUL TĂU**:
```
[Confirmă recomandarea sau descrie altă strategie]



```

---

### M7: Crearea conturilor ADMIN și CREATOR

**Context**:
În TASK 1.1.4, signup-ul permite doar role CUSTOMER. Însă sistemul are 4 role-uri: ADMIN, CREATOR, CUSTOMER, GUEST. Nu există documentație despre cum se creează conturi ADMIN sau CREATOR.

**Risc**:
Nu poți crea conturi admin, proces de onboarding neclar.

**Întrebare**:
Cum se creează conturile ADMIN și CREATOR?

Opțiuni:
- A) Endpoint separat (accesibil doar de ADMIN existent)
- B) Script de bază de date (run manual de DevOps)
- C) Primul user este ADMIN, restul se promovează prin UI
- D) Altă metodă

**RĂSPUNSUL TĂU**:
```
[Scrie A/B/C/D sau descrie altă metodă]



```

---

## SECȚIUNEA 3: Edge Cases (5 întrebări)

### M8: Race condition la signup concurent

**Context**:
În TASK 1.1.1, se validează unicitatea email-ului prin query la DB. Dacă 2 utilizatori încearcă să se înregistreze SIMULTAN cu același email:
1. Ambii verifică → email liber
2. Ambii încearcă INSERT → unul reușește, unul primește eroare de constraint

**Risc**:
Eroare tehnică expusă către user, mesaj confuz, experiență proastă.

**Întrebare**:
Cum gestionezi race condition-ul?

Opțiuni:
- A) Constraint UNIQUE în DB + handle elegant eroarea ("Email already taken")
- B) Database-level locking (SELECT FOR UPDATE)
- C) Distributed lock în Redis
- D) Altă metodă

**Recomandare SCA**: A - Constraint UNIQUE + handling elegant (mai simplu, suficient).

**RĂSPUNSUL TĂU**:
```
[Scrie A/B/C/D sau descrie altă metodă]


```

---

### M9: Cleanup pentru Stripe customer orphan

**Context**:
În TASK 1.1.3, se creează customer în Stripe ÎNAINTE de a crea user-ul în DB. Dacă:
1. Stripe reușește → customer creat
2. DB eșuează → user NU e creat

Rezultat: Customer Stripe orfan (nu are user asociat).

**Risc**:
- Acumulare de Stripe customers orfani (cost, clutter)
- User nu poate face signup mai târziu (email duplicat în Stripe)

**Întrebare**:
Ce faci dacă Stripe reușește dar DB eșuează?

Opțiuni:
- A) Șterge customer din Stripe (rollback manual)
- B) Folosește Stripe idempotency keys + reîncearcă
- C) Lasă customer orfan (cleanup periodic cu script)
- D) Inversează ordinea: creează user în DB, apoi Stripe

**Recomandare SCA**: A sau B - Rollback imediat (A) sau idempotency (B).

**RĂSPUNSUL TĂU**:
```
[Scrie A/B/C/D sau descrie altă metodă]



```

---

### M10: Invalidarea token-urilor la schimbarea parolei

**Context**:
În TASK 1.6.1, utilizatorul poate schimba parola. Însă nu este menționat dacă token-urile existente (access + refresh) trebuie invalidate.

**Risc**:
Dacă un token este furat, atacatorul rămâne autentificat chiar DUPĂ ce victima și-a schimbat parola (user nu se poate proteja).

**Întrebare**:
Ar trebui ca schimbarea parolei să invalideze TOATE refresh token-urile existente (forțând re-login pe toate device-urile)?

**Recomandare SCA**: DA - Incrementează user.tokenVersion, invalidează toate refresh token-urile (re-login forțat).

**RĂSPUNSUL TĂU**:
```
[Scrie DA/NU sau o altă strategie]


```

---

### M11: Invalidarea token-urilor la signout

**Context**:
În TASK 1.5.4, signout șterge cookie-urile client-side. Însă token-urile (access + refresh) rămân valide server-side până expiră natural.

**Risc**:
Dacă un atacator fură token-ul ÎNAINTE de signout, token-ul rămâne valid după signout (logout incomplet).

**Întrebare**:
Ar trebui ca signout să invalideze token-urile server-side?

Opțiuni:
- A) DA - Adaugă refresh token în Redis blacklist (sau șterge din whitelist)
- B) NU - Access token-urile sunt short-lived (5-15 min), risc acceptabil
- C) Altă strategie

**Recomandare SCA**: A - Blacklist în Redis pentru logout complet și sigur.

**RĂSPUNSUL TĂU**:
```
[Scrie A/B/C sau o altă strategie]



```

---

### M12: Rate limiting pentru recovery key

**Context**:
În TASK 1.4.1, recovery key-ul permite setarea unei parole noi FĂRĂ parolă veche. Nu este menționat rate limiting pentru încercări de recovery key.

**Risc**:
Brute force attack pe recovery keys (dacă sunt predictibile sau scurte).

**Întrebare**:
Ar trebui să fie rate limiting pentru utilizarea recovery keys?

**Recomandare SCA**:
- DA - Maximum 5 încercări per oră per email
- Adaugă CAPTCHA după 3 încercări eșuate

**RĂSPUNSUL TĂU**:
```
[Scrie DA/NU sau o altă strategie]


```

---

## FINALIZARE

**Când ai terminat**:

1. ✅ Salvează acest fișier
2. ✅ Scrie în chat: "Am completat chestionarul pentru JIRA_AUTH_MODULE"
3. ✅ Claude va:
   - Citi răspunsurile tale
   - Actualiza `BackEnd/JIRA_AUTH_MODULE.txt` cu clarificările
   - Re-rula SCA pentru verificare (target: 95-100/100)
   - Commit la git dacă scorul ≥ 95

**Mulțumesc pentru clarificări! 🚀**

---

**Raport complet SCA**: Vezi `.claude/evaluations/sca-jira-auth-module-20250113.md`
