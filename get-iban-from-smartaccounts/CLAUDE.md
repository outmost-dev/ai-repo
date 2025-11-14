# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains Python scripts for extracting payment data from the **Smart Accounts Platform API** (a PSD2-compliant Romanian banking aggregation service) and matching extracted IBANs with their corresponding CUI (Romanian tax identification numbers) from internal partner databases.

The workflow consists of three main phases:
1. **Extract payments** from Smart Accounts API (last 30 days)
2. **Match beneficiary names** to partner records using fuzzy matching
3. **Generate enriched CSV** with IBAN, beneficiary name, CUI, and partner name

## Key Scripts

### 1. `extract_payments.py` - Main Data Extraction
Primary script that:
- Authenticates with Smart Accounts API using client credentials flow
- Fetches all bank accounts accessible to the API user
- Retrieves paginated transaction data (50 transactions per page, max 150 pages per account)
- Filters transactions to only outgoing payments (negative amounts)
- Extracts unique creditor IBANs with beneficiary names
- Attempts basic CUI extraction from transaction details fields
- Outputs: `plati_iban_cui.csv`

**Configuration variables (hardcoded in script):**
- `CLIENT_ID` and `CLIENT_SECRET`: API credentials for Smart Accounts Platform
- `MAX_PAGES_PER_ACCOUNT`: Rate limiting protection (default: 150 pages)
- `BASE_URL`: `https://appsmartaccounts.eu/sacc-web-gateway`

**Run:** `python3 extract_payments.py`

### 2. `match_cui_from_parteneri.py` - CUI Matching Engine
Matches payment beneficiaries to partner database using fuzzy string matching:
- Reads `Parteneri.xlsx` (converted to CSV) containing partner names and CUIs
- Normalizes company names (removes legal suffixes, punctuation, converts to uppercase)
- Uses `SequenceMatcher` for fuzzy matching with 0.75 threshold
- Substring matching receives 0.9 score (high confidence)
- **Preserves exact CUI format** from source file (including "RO" prefix, spaces, etc.)
- Outputs: `plati_iban_cui_final.csv` with 4 columns:
  - IBAN (from transactions)
  - Nume Beneficiar (from Smart Accounts)
  - CUI (from Parteneri file, exact format)
  - Nume Partener (from Parteneri file)

**Run:** `python3 match_cui_from_parteneri.py`

**Important:** This script expects:
- `plati_iban_cui_updated.csv` as input (previous extraction output)
- `parteneri.csv` (converted from `Parteneri.xlsx`)

### 3. `read_excel_simple.py` - Excel Converter
Utility that converts `.xlsx` files to CSV using only Python stdlib (no pandas/openpyxl):
- Reads XLSX as ZIP archive
- Parses XML sheets using `xml.etree.ElementTree`
- Handles shared strings
- Used to convert `Parteneri.xlsx` and `Raport neplatite.xlsx`

**Run:** `python3 read_excel_simple.py <input.xlsx> <output.csv>`

### 4. `match_cui_from_report.py` - Alternative Matching (Legacy)
Earlier version that matches against `Raport neplatite.xlsx` instead of `Parteneri.xlsx`. Similar logic but with different source data structure.

## Data Pipeline Flow

```
1. Smart Accounts API
   ↓ (extract_payments.py)
2. plati_iban_cui.csv
   ↓ (read_excel_simple.py: Parteneri.xlsx → parteneri.csv)
3. parteneri.csv
   ↓ (match_cui_from_parteneri.py)
4. plati_iban_cui_final.csv (FINAL OUTPUT)
```

## Smart Accounts Platform API

API documentation available in `documentatie.yaml` (OpenAPI 3.0.1 spec).

**Authentication Flow:**
1. POST `/ryke-authenticate-api/rest/api/authenticate/sacc-web/tokens`
   - Payload: `grant_type: client_credentials`, `client_id`, `client_secret`
   - Returns: `accessToken` (short-lived) and `refreshToken`

2. GET `/ryke-accounts/rest/api/ais/sacc-web/export/aisp-accounts`
   - Header: `Authorization: Bearer <accessToken>`
   - Returns: Array of bank accounts with IBAN, balance, bank name

3. GET `/ryke-accounts/rest/api/ais/sacc-web/export/aisp-transactions`
   - Query params: `startDate`, `endDate` (required, YYYY-MM-DD format)
   - Optional: `accountId`, `pageNumber`, `pageSize` (default: 50)
   - Returns: Paginated transactions with `totalPages`, `totalElements`

**Rate Limiting:**
- API has implicit rate limits
- Script includes 0.3s delay between requests
- Page limit per account prevents excessive API calls

**Supported Romanian Banks:**
Banca Transilvania, BCR, ING Bank, BRD, Raiffeisen Bank, CEC Bank, First Bank, UniCredit Bank, Revolut, Garanti BBVA, Libra Bank

## CUI Matching Algorithm

The fuzzy matching algorithm in `match_cui_from_parteneri.py`:

1. **Normalization** (`normalize_name` function):
   - Convert to uppercase
   - Remove legal entity suffixes: SRL, S.R.L., SA, S.A., PFA, II, SCS, SNC, ASOCIATIA, SRL-D
   - Strip special characters (keep alphanumeric + spaces)
   - Collapse multiple spaces

2. **Matching Strategy** (`find_best_match` function):
   - **Exact match**: Normalized names identical → score 1.0
   - **Substring match**: One name contains the other → score 0.9
   - **Fuzzy match**: `SequenceMatcher.ratio()` → score 0.0-1.0
   - **Threshold**: Minimum 0.75 score required for match

3. **CUI Format Preservation**:
   - CUI stored exactly as in `Parteneri.xlsx` (no transformation)
   - May include "RO" prefix, spaces (e.g., "RO 31014235", "RO5110535", "1883902")

## Expected Input Files

- **Parteneri.xlsx**: Excel file with columns:
  - Column 1: `Partener` (CUI with various formats)
  - Column 2: `Nume Partener` (company name)

- **Raport neplatite.xlsx** (optional, legacy):
  - Financial report with supplier data
  - Multiple columns including CUI and company names

## Common Commands

```bash
# Full extraction and matching workflow
python3 extract_payments.py
python3 read_excel_simple.py "Parteneri.xlsx" parteneri.csv
python3 match_cui_from_parteneri.py

# Convert Excel to CSV
python3 read_excel_simple.py "<filename>.xlsx" "<output>.csv"

# Check matching results
head -50 plati_iban_cui_final.csv
```

## Output Files

- `plati_iban_cui.csv`: Initial extraction (IBAN, Nume Beneficiar, CUI)
  - CUI column mostly empty (basic extraction from transaction details)

- `plati_iban_cui_final.csv`: **Final enriched output** (IBAN, Nume Beneficiar, CUI, Nume Partener)
  - ~95% CUI match rate achieved
  - 4th column allows verification of matching accuracy

- `parteneri.csv`: Converted partner database
- `raport_neplatite.csv`: Converted financial report (19MB, 195K+ rows)

## Architecture Notes

### Why No External Dependencies?
The Excel reading utility (`read_excel_simple.py`) uses only Python stdlib to avoid dependency issues in the deployment environment (no pip available, hence no pandas/openpyxl).

### API Pagination Strategy
Smart Accounts API returns up to 50 transactions per page. The script processes all pages sequentially with delay to avoid rate limiting. The `MAX_PAGES_PER_ACCOUNT` limit prevents infinite loops and excessive API calls for accounts with very large transaction history.

### Fuzzy Matching Rationale
Payment beneficiary names from banks often differ from official company records:
- Different legal suffixes (SRL vs S.R.L.)
- Truncated names
- Encoding issues
- Informal names vs. registered names

The fuzzy matching algorithm handles these variations while maintaining high accuracy.

## Credentials Management

**Current state:** API credentials are **hardcoded** in `extract_payments.py`.

For production use, credentials should be:
- Moved to environment variables or config file
- Added to `.gitignore`
- Rotated periodically via Smart Accounts Platform UI

## Typical Match Rate

Based on typical runs:
- Total payments extracted: ~4,800 (30-day window)
- Unique beneficiary IBANs: ~480
- Matched with CUI: ~455 (94.8%)
- Unmatched: ~25 (5.2%) - typically associations, individuals, or non-partners
