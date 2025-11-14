# Propunere Tehnică - Funcționalitate QR Code pentru Validare ITDR

**De la:** Vali Manu & Andrei Popescu - Arhitecți Platformă
**Către:** Andreea (PMT)
**Data:** 13 Noiembrie 2025
**Subiect:** Soluție tehnică pentru implementarea funcționalității QR Code

---

## 1. Context

În urma întâlnirii din 6 noiembrie 2025, am analizat cerințele pentru noua funcționalitate de validare prin QR code în magazine. Scopul este de a simplifica experiența de participare la campanii prin eliminarea intervenției manuale a operatorului în faza de înregistrare și de a muta o parte din proces direct către consumatori.

## 2. Soluția Propusă

### 2.1 Flow Consumator (Mobile-First)

**Pas 1: Scanare QR Code**
- Consumatorul scanează QR code-ul din materialele promoționale din magazin
- QR code-ul este universal (același pentru toate magazinele din rețea)
- Redirectionează către interfața web mobile-responsive

**Pas 2: Verificare Vârstă & Acord Marketing**
- Colectare dată naștere (verificare 18+ și campanii de la mulți ani)
- Checkbox acord procesare date pentru marketing
- Validare automată - reject pentru sub 18 ani

**Pas 3: Selecție Campanie**
- Afișare listă campanii active (similar cu aplicația mobilă existentă)
- Layout tip card pentru fiecare campanie disponibilă
- Gestionare campanii de către echipa tehnică (nu de către client)

**Pas 4: Selecție Pachete**
- Selectare tip sortiment cumpărat (Amber, Gold, Classic, Gold Slim, etc.)
- Selectare număr de pachete conform campaniei (ex: 5 pachete pentru campania 5+1)

**Pas 5: Generare & Confirmare**
- Generare cod unic de validare
- Afișare mesaj confirmare pe ecran
- **Trimitere automată SMS** cu codul unic către numărul de telefon înregistrat
- Mesaj generic: "Felicitări! Ai câștigat un pachet de țigări. Cod validare: XXXXX"

### 2.2 Flow Operator (Simplificat la maxim)

**Ecran Unic de Validare:**
1. Operator introduce codul primit de la client (de pe SMS sau ecran)
2. Sistem validează codul:
   - **Valid** → trece la pasul 3
   - **Invalid/Expirat/Folosit** → afișare mesaj eroare
3. Selectare tip pachet cadou oferit (Amber, Gold, Classic, etc.)
4. Finalizare → actualizare automată stocuri și raportare

**Eliminări față de flow-ul actual:**
- ❌ Nu mai introduce numărul de pachete cumpărate (deja în sistem)
- ❌ Nu mai introduce numărul de telefon (deja în sistem)
- ✅ Simplificare la 3 click-uri: cod → tip pachet → finalizare

### 2.3 Reguli de Business

- **Limitare participare:** 1 premiu / 24 ore per număr de telefon
- **Validare cod:** Cod unic, folosit o singură dată, expiră după validare
- **Tracking complet:**
  - Magazin în care s-a făcut validarea
  - Data și ora validării
  - Tip pachete cumpărate
  - Tip pachet cadou oferit
  - Status: generat / revendicat / expirat
- **Fără geolocație** (complexitate nejustificată, probleme GPS în magazine)

### 2.4 Integrări

- **SMS Gateway:** Trimitere coduri validare pe număr lung (evitare blocări numere scurte)
- **Sistem campanii existent:** Reutilizare module de gestionare campanii
- **Raportare:** Extindere rapoarte existente cu date din flow-ul QR

## 3. Estimare Efort

| Modul | Descriere | Efort (MD) |
|-------|-----------|------------|
| **Analiză & Design** | Arhitectură, wireframes, specificații tehnice | 1 MD |
| **Frontend Consumator** | Interfață mobile-responsive (5 ecrane) | 3.5 MD |
| **Backend Core** | API-uri generare cod, validare, integrare SMS | 5 MD |
| **Frontend Operator** | Simplificare ecran validare + selecție premiu | 1.5 MD |
| **Testing & QA** | Testing funcțional, integrare, securitate | 2 MD |
| **Deployment** | Deploy producție + documentație | 1 MD |
| **TOTAL** | | **14 MD** |

**Nota:** Estimarea include și buffer pentru ajustări în urma testărilor.

## 4. Tehnologii Utilizate

- **Backend:** .NET (în linie cu arhitectura existentă validare-itdr)
- **Frontend:** HTML5, CSS3, JavaScript (mobile-first, responsive design)
- **SMS:** Integrare gateway existent
- **Database:** Extindere schema existentă cu tabele: `QRCodes`, `QRValidations`

## 5. Termene de Livrare

### Timeline Propus

| Milestone | Dată țintă | Status |
|-----------|------------|--------|
| Aprobare soluție tehnică | 15 noiembrie 2025 | Pending |
| Design & Wireframes | 18 noiembrie 2025 | - |
| Development Sprint 1 | 25 noiembrie 2025 | - |
| Development Sprint 2 | 29 noiembrie 2025 | - |
| Testing & QA | 30 noiembrie 2025 | - |
| **Go Live** | **1 decembrie 2025** | - |

**Condiții:**
- Deadline 1 decembrie este realizabil cu resurse dedicate 100%
- Requiere aprobare promptă a soluției (max. 15 noiembrie)
- Orice modificări majore la specificații după 20 noiembrie pot impacta termenul

## 6. Avantaje Soluție

✅ **Simplificare drastică** pentru operator (3 click-uri vs. 7-8 click-uri)
✅ **Reducere erori** - eliminare introducere manuală date
✅ **Experiență modernă** - consumatorul își gestionează singur participarea
✅ **Tracking complet** - raportare detaliată per magazin/campanie/sortiment
✅ **Scalabilitate** - un singur QR code pentru toată rețeaua
✅ **Colectare date** - bază pentru campanii de marketing viitoare
✅ **Antifraudă** - cod unic, limitare 24h, validare instantanee

## 7. Livrabile

1. **Documentație tehnică** - arhitectură, API specs, flow diagrams
2. **Interfață consumator** - aplicație web mobile-responsive
3. **Interfață operator** - modul simplificat validare în platformă existentă
4. **Rapoarte** - extindere dashboard cu metrici QR code
5. **Manual utilizare** - ghid pentru operatori
6. **Campanie test** - configurare campanie pilot pentru validare

## 8. Costuri Mentenanță & Suport

*(Ofertă separată conform discuție - va include toate produsele platformei Validare ITDR)*

## 9. Next Steps

1. **Aprobare soluție:** Confirmare formală până pe 15 noiembrie
2. **Clarificări:** Întâlnire follow-up pentru detalii fine (dacă necesar)
3. **Start development:** Kick-off 18 noiembrie
4. **Producție materiale QR:** După finalizare development, va primi QR code final pentru print

## 10. Contact

Pentru orice clarificări suplimentare:

**Vali Manu** - Arhitect Platformă
valim@somaway.ro

**Andrei Popescu** - Arhitect Platformă
andrei.popescu@somaway.ro

---

*Documentul este confidențial și destinat exclusiv echipei Somaway & PMT.*
