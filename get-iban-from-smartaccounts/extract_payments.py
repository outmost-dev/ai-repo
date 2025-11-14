#!/usr/bin/env python3
"""
Smart Accounts Platform - Extract IBAN and CUI from payments
Extracts all payments from the last month and generates a CSV with unique IBANs and CUIs
"""

import requests
import json
import csv
import re
import time
from datetime import datetime, timedelta
from typing import Dict, List, Set, Tuple, Optional

# Configuration
BASE_URL = "https://appsmartaccounts.eu/sacc-web-gateway"
CLIENT_ID = "xpressapi"
CLIENT_SECRET = "b9e4d24a-9b3e-4aa6-b593-c54f92993e3e"
OUTPUT_FILE = "plati_iban_cui.csv"
MAX_PAGES_PER_ACCOUNT = 150  # Limit pages to avoid rate limiting and speed up processing


def authenticate() -> str:
    """
    Authenticate and get access token
    Returns: access_token
    """
    url = f"{BASE_URL}/ryke-authenticate-api/rest/api/authenticate/sacc-web/tokens"

    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    print("🔐 Authenticating...")
    response = requests.post(url, json=payload)
    response.raise_for_status()

    data = response.json()
    access_token = data.get("result", {}).get("accessToken")

    if not access_token:
        raise Exception("Failed to get access token")

    print("✅ Authentication successful")
    return access_token


def get_accounts(access_token: str) -> List[Dict]:
    """
    Get all authorized accounts
    Returns: list of account objects
    """
    url = f"{BASE_URL}/ryke-accounts/rest/api/ais/sacc-web/export/aisp-accounts"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    print("📋 Fetching accounts...")
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()
    accounts = data.get("result", [])

    print(f"✅ Found {len(accounts)} accounts")
    return accounts


def get_transactions(access_token: str, account_id: str, start_date: str, end_date: str, page_number: int = 0) -> Dict:
    """
    Get transactions for a specific account
    Returns: response with transactions and pagination info
    """
    url = f"{BASE_URL}/ryke-accounts/rest/api/ais/sacc-web/export/aisp-transactions"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    params = {
        "startDate": start_date,
        "endDate": end_date,
        "accountId": account_id,
        "pageNumber": page_number,
        "pageSize": 50
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    return response.json()


def extract_cui(text: str) -> Optional[str]:
    """
    Extract CUI from text using regex patterns
    Searches for: CUI, CIF, or RO followed by numbers
    """
    if not text:
        return None

    # Patterns to match CUI/CIF
    patterns = [
        r'CUI[\s:]*([A-Z]{0,2}\d{6,10})',  # CUI: RO12345678 or CUI 12345678
        r'CIF[\s:]*([A-Z]{0,2}\d{6,10})',  # CIF: RO12345678 or CIF 12345678
        r'RO\d{6,10}',                      # RO12345678
        r'\b(\d{6,10})\b'                   # Plain number between 6-10 digits
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            cui = match.group(1) if match.lastindex else match.group(0)
            return cui.strip()

    return None


def fetch_all_payments(access_token: str) -> List[Dict]:
    """
    Fetch all payments from the last month across all accounts
    Returns: list of payment transactions
    """
    # Calculate date range (last month)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)

    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")

    print(f"📅 Fetching transactions from {start_date_str} to {end_date_str}")

    # Get all accounts
    accounts = get_accounts(access_token)

    all_payments = []

    for account in accounts:
        account_id = str(account.get("accountId"))
        iban = account.get("iban", "N/A")
        bank = account.get("bank", "N/A")

        print(f"💳 Processing account: {iban} ({bank})")

        # Fetch all pages for this account
        page_number = 0
        while True:
            try:
                response_data = get_transactions(access_token, account_id, start_date_str, end_date_str, page_number)
                transactions = response_data.get("result", [])
                total_pages = response_data.get("totalPages", 1)

                # Filter only payments (negative amounts = money out)
                payments = [t for t in transactions if t.get("amount", 0) < 0]
                all_payments.extend(payments)

                print(f"  📄 Page {page_number + 1}/{total_pages}: {len(payments)} payments found")

                # Check if we've reached the page limit
                if page_number + 1 >= MAX_PAGES_PER_ACCOUNT:
                    print(f"  ⚠️  Reached page limit ({MAX_PAGES_PER_ACCOUNT}), moving to next account")
                    break

                # Check if there are more pages
                if page_number + 1 >= total_pages:
                    break

                page_number += 1

                # Add delay to avoid rate limiting
                time.sleep(0.3)

            except Exception as e:
                print(f"  ⚠️  Error fetching page {page_number}: {e}")
                break

    print(f"✅ Total payments found: {len(all_payments)}")
    return all_payments


def process_payments(payments: List[Dict]) -> List[Tuple[str, str, str]]:
    """
    Process payments and extract unique IBAN + Name + CUI combinations
    Returns: list of tuples (iban, name, cui)
    """
    iban_data_map = {}  # {iban: (name, cui)}

    print("🔍 Processing payments...")

    for payment in payments:
        # Extract creditor IBAN
        creditor_account = payment.get("creditorAccount", {})
        iban = creditor_account.get("iban")

        if not iban:
            continue

        # Skip if we already have this IBAN
        if iban in iban_data_map:
            continue

        # Extract creditor name
        creditor_name = payment.get("creditorName", "").strip()

        # Try to extract CUI from various fields
        cui = None

        # Check remittanceInformationUnstructured
        remittance_info = payment.get("remittanceInformationUnstructured", "")
        cui = extract_cui(remittance_info)

        # If not found, check smartTransactionDetails
        if not cui:
            smart_details = payment.get("smartTransactionDetails", "")
            cui = extract_cui(smart_details)

        # If not found, check creditorName
        if not cui:
            cui = extract_cui(creditor_name)

        # Store the IBAN with name and CUI
        iban_data_map[iban] = (creditor_name or "", cui or "")
        print(f"  ✓ IBAN: {iban} | Name: {creditor_name or 'N/A'} | CUI: {cui or 'N/A'}")

    print(f"✅ Unique IBANs found: {len(iban_data_map)}")

    # Convert to list of tuples (iban, name, cui)
    return [(iban, name, cui) for iban, (name, cui) in iban_data_map.items()]


def generate_csv(data: List[Tuple[str, str, str]], output_file: str):
    """
    Generate CSV file with IBAN, Name, and CUI
    """
    print(f"📝 Generating CSV file: {output_file}")

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['IBAN', 'Nume Beneficiar', 'CUI'])  # Header
        writer.writerows(data)

    print(f"✅ CSV file generated successfully: {output_file}")
    print(f"📊 Total records: {len(data)}")


def main():
    """
    Main execution flow
    """
    print("=" * 60)
    print("Smart Accounts Platform - Payment IBAN & CUI Extractor")
    print("=" * 60)
    print()

    try:
        # Step 1: Authenticate
        access_token = authenticate()
        print()

        # Step 2: Fetch all payments from last month
        payments = fetch_all_payments(access_token)
        print()

        # Step 3: Process payments and extract IBAN + CUI
        iban_cui_data = process_payments(payments)
        print()

        # Step 4: Generate CSV
        generate_csv(iban_cui_data, OUTPUT_FILE)
        print()

        print("=" * 60)
        print("✅ Process completed successfully!")
        print("=" * 60)

    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
        print(f"Response: {e.response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
