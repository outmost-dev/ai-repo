#!/usr/bin/env python3
"""
Match CUI from Parteneri file to payments CSV
Uses fuzzy string matching and preserves CUI format exactly as in Parteneri file
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
    suffixes = ['SRL', 'S.R.L.', 'SA', 'S.A.', 'PFA', 'II', 'SCS', 'SNC', 'ASOCIATIA', 'SRL-D']
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

def load_parteneri(parteneri_csv):
    """Load parteneri and CUI from CSV"""
    parteneri = {}  # {normalized_name: (original_name, cui)}

    print("📋 Loading parteneri from file...")

    with open(parteneri_csv, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)

        # Skip header
        header = next(reader)
        print(f"   Header: {header}")

        for row in reader:
            if len(row) < 2:
                continue

            cui = row[0].strip()      # Column "Partener" - keep EXACTLY as is
            name = row[1].strip()     # Column "Nume Partener"

            if not cui or not name:
                continue

            normalized = normalize_name(name)

            if normalized and cui:
                # Store with normalized name as key
                # If duplicate, keep first occurrence
                if normalized not in parteneri:
                    parteneri[normalized] = (name, cui)

    print(f"✅ Loaded {len(parteneri)} unique parteneri")
    return parteneri

def find_best_match(beneficiary_name, parteneri, threshold=0.75):
    """
    Find best matching partener for a beneficiary name
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
    if normalized_beneficiary in parteneri:
        name, cui = parteneri[normalized_beneficiary]
        return name, cui, 1.0

    # Try fuzzy matching
    for partener_normalized, (partener_name, cui) in parteneri.items():
        # Check if one contains the other (substring match)
        if partener_normalized in normalized_beneficiary or normalized_beneficiary in partener_normalized:
            score = 0.9  # High score for substring match
        else:
            score = similarity(normalized_beneficiary, partener_normalized)

        if score > best_score and score >= threshold:
            best_score = score
            best_match = (partener_name, cui, score)

    if best_match:
        return best_match

    return None, None, 0

def match_cui_to_payments(payments_csv, parteneri_csv, output_csv):
    """Match CUI from parteneri to payments CSV"""

    # Load parteneri
    parteneri = load_parteneri(parteneri_csv)

    print("\n🔍 Matching CUI to payments...")

    # Read payments CSV
    with open(payments_csv, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # IBAN, Nume Beneficiar, CUI

        payments = []
        for row in reader:
            if len(row) >= 2:  # At least IBAN and Name
                # Ensure we have 3 columns (add empty CUI if missing)
                while len(row) < 3:
                    row.append('')
                payments.append(row[:3])  # Keep only first 3 columns

    # Match and update
    matched_count = 0
    updated_rows = []

    for iban, beneficiary_name, existing_cui in payments:
        # Try to find match (even if CUI already exists, to get partner name)
        matched_name, cui, score = find_best_match(beneficiary_name, parteneri)

        # Use existing CUI if present, otherwise use matched CUI
        final_cui = existing_cui.strip() if existing_cui and existing_cui.strip() else (cui if cui else '')
        final_partner_name = matched_name if matched_name else ''

        if final_cui:
            matched_count += 1
            if cui and not existing_cui.strip():  # New match found
                print(f"  ✓ Match: {beneficiary_name[:40]:40} -> CUI: {cui} | Partner: {matched_name[:30]}")
            updated_rows.append([iban, beneficiary_name, final_cui, final_partner_name])
        else:
            updated_rows.append([iban, beneficiary_name, '', ''])

    # Write updated CSV
    print(f"\n📝 Writing updated CSV...")
    with open(output_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['IBAN', 'Nume Beneficiar', 'CUI', 'Nume Partener'])
        writer.writerows(updated_rows)

    print(f"✅ Matched {matched_count} CUI entries")
    print(f"✅ Updated CSV saved to: {output_csv}")

    # Statistics
    total = len(updated_rows)
    with_cui = sum(1 for row in updated_rows if row[2].strip())
    print(f"\n📊 Statistics:")
    print(f"   Total IBANs: {total}")
    print(f"   With CUI: {with_cui} ({with_cui/total*100:.1f}%)")
    print(f"   Without CUI: {total - with_cui} ({(total-with_cui)/total*100:.1f}%)")

if __name__ == '__main__':
    payments_csv = 'plati_iban_cui_updated.csv'
    parteneri_csv = 'parteneri.csv'
    output_csv = 'plati_iban_cui_final.csv'

    match_cui_to_payments(payments_csv, parteneri_csv, output_csv)
