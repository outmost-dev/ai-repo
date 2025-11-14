#!/usr/bin/env python3
"""
Match CUI from Raport neplatite to payments CSV
Uses fuzzy string matching to find CUI for each beneficiary
"""
import csv
import re
from difflib import SequenceMatcher

def normalize_name(name):
    """Normalize company name for matching"""
    if not name:
        return ""

    # Convert to uppercase
    name = name.upper()

    # Remove common suffixes
    suffixes = ['SRL', 'S.R.L.', 'SA', 'S.A.', 'PFA', 'II', 'SCS', 'SNC', 'ASOCIATIA']
    for suffix in suffixes:
        name = name.replace(suffix, '')

    # Remove special characters but keep spaces
    name = re.sub(r'[^A-Z0-9\s]', '', name)

    # Remove extra spaces
    name = ' '.join(name.split())

    return name.strip()

def similarity(a, b):
    """Calculate similarity between two strings (0-1)"""
    return SequenceMatcher(None, a, b).ratio()

def load_suppliers_from_report(report_csv):
    """Load suppliers and CUI from report"""
    suppliers = {}  # {normalized_name: (original_name, cui)}

    print("📋 Loading suppliers from report...")

    with open(report_csv, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)

        # Skip first 3 rows (headers)
        for _ in range(3):
            next(reader)

        for row in reader:
            if len(row) < 3:
                continue

            cui_raw = row[1].strip()  # Column "Furnizor"
            name = row[2].strip()     # Column "Nume Furnizor"

            if not cui_raw or not name:
                continue

            # Keep CUI exactly as it appears in the report (with RO prefix)
            cui = cui_raw

            normalized = normalize_name(name)

            if normalized and cui:
                # Store with normalized name as key
                if normalized not in suppliers:
                    suppliers[normalized] = (name, cui)

    print(f"✅ Loaded {len(suppliers)} unique suppliers")
    return suppliers

def find_best_match(beneficiary_name, suppliers, threshold=0.75):
    """
    Find best matching supplier for a beneficiary name
    Returns (original_name, cui, similarity_score) or (None, None, 0)
    """
    if not beneficiary_name or beneficiary_name == 'Nespecificat':
        return None, None, 0

    normalized_beneficiary = normalize_name(beneficiary_name)

    if not normalized_beneficiary:
        return None, None, 0

    best_match = None
    best_score = 0

    # First try exact match
    if normalized_beneficiary in suppliers:
        name, cui = suppliers[normalized_beneficiary]
        return name, cui, 1.0

    # Try fuzzy matching
    for supplier_normalized, (supplier_name, cui) in suppliers.items():
        # Check if one contains the other (substring match)
        if supplier_normalized in normalized_beneficiary or normalized_beneficiary in supplier_normalized:
            score = 0.9  # High score for substring match
        else:
            score = similarity(normalized_beneficiary, supplier_normalized)

        if score > best_score and score >= threshold:
            best_score = score
            best_match = (supplier_name, cui, score)

    if best_match:
        return best_match

    return None, None, 0

def match_cui_to_payments(payments_csv, report_csv, output_csv):
    """Match CUI from report to payments CSV"""

    # Load suppliers from report
    suppliers = load_suppliers_from_report(report_csv)

    print("\n🔍 Matching CUI to payments...")

    # Read payments CSV
    with open(payments_csv, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # IBAN, Nume Beneficiar, CUI

        payments = []
        for row in reader:
            if len(row) >= 3:
                payments.append(row)

    # Match and update
    matched_count = 0
    updated_rows = []

    for iban, beneficiary_name, existing_cui in payments:
        # Skip if CUI already exists
        if existing_cui and existing_cui.strip():
            updated_rows.append([iban, beneficiary_name, existing_cui])
            continue

        # Try to find match
        matched_name, cui, score = find_best_match(beneficiary_name, suppliers)

        if cui:
            matched_count += 1
            print(f"  ✓ Match: {beneficiary_name[:40]:40} -> CUI: {cui} (score: {score:.2f})")
            updated_rows.append([iban, beneficiary_name, cui])
        else:
            updated_rows.append([iban, beneficiary_name, ''])

    # Write updated CSV
    print(f"\n📝 Writing updated CSV...")
    with open(output_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['IBAN', 'Nume Beneficiar', 'CUI'])
        writer.writerows(updated_rows)

    print(f"✅ Matched {matched_count} new CUI entries")
    print(f"✅ Updated CSV saved to: {output_csv}")

    # Statistics
    total = len(updated_rows)
    with_cui = sum(1 for row in updated_rows if row[2].strip())
    print(f"\n📊 Statistics:")
    print(f"   Total IBANs: {total}")
    print(f"   With CUI: {with_cui} ({with_cui/total*100:.1f}%)")
    print(f"   Without CUI: {total - with_cui} ({(total-with_cui)/total*100:.1f}%)")

if __name__ == '__main__':
    payments_csv = 'plati_iban_cui.csv'
    report_csv = 'raport_neplatite.csv'
    output_csv = 'plati_iban_cui_updated.csv'

    match_cui_to_payments(payments_csv, report_csv, output_csv)
