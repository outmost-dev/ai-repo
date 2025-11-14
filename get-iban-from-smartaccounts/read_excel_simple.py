#!/usr/bin/env python3
"""
Simple XLSX reader without external dependencies
"""
import zipfile
import xml.etree.ElementTree as ET
import csv
import sys

def read_xlsx_to_csv(xlsx_path, csv_path):
    """Read XLSX and convert to CSV using only built-in libraries"""

    # Open the XLSX file (it's a ZIP archive)
    with zipfile.ZipFile(xlsx_path, 'r') as zip_ref:
        # Read shared strings (if any)
        shared_strings = []
        try:
            with zip_ref.open('xl/sharedStrings.xml') as xml_file:
                tree = ET.parse(xml_file)
                root = tree.getroot()
                ns = {'': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
                for si in root.findall('.//t', ns):
                    shared_strings.append(si.text or '')
        except KeyError:
            pass  # No shared strings

        # Read the first worksheet
        with zip_ref.open('xl/worksheets/sheet1.xml') as xml_file:
            tree = ET.parse(xml_file)
            root = tree.getroot()

            ns = {'': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

            rows_data = []

            for row in root.findall('.//row', ns):
                row_data = []
                for cell in row.findall('.//c', ns):
                    cell_type = cell.get('t')
                    value_elem = cell.find('.//v', ns)

                    if value_elem is not None:
                        value = value_elem.text

                        # If it's a shared string, look it up
                        if cell_type == 's':
                            try:
                                value = shared_strings[int(value)]
                            except (ValueError, IndexError):
                                pass

                        row_data.append(value)
                    else:
                        row_data.append('')

                if row_data:  # Skip empty rows
                    rows_data.append(row_data)

            # Write to CSV
            with open(csv_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(rows_data)

            print(f"✅ Converted {len(rows_data)} rows to CSV")
            return rows_data

if __name__ == '__main__':
    xlsx_file = sys.argv[1] if len(sys.argv) > 1 else 'Raport neplatite.xlsx'
    csv_file = sys.argv[2] if len(sys.argv) > 2 else 'raport_neplatite.csv'

    read_xlsx_to_csv(xlsx_file, csv_file)
