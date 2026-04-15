#!/usr/bin/env python3
"""
Normalize 19 Invoice Detail JSON files by:
1. Removing "ModelVersionRemoved": ""
2. Replacing "Condition": [] with "Condition": {}
"""

import json
import os
from pathlib import Path

def normalize_json(data):
    """
    Recursively normalize JSON data:
    - Remove ModelVersionRemoved fields
    - Replace Condition arrays with empty objects
    """
    if isinstance(data, dict):
        # Remove ModelVersionRemoved
        if "ModelVersionRemoved" in data:
            del data["ModelVersionRemoved"]
        
        # Replace Condition array with object
        if "Condition" in data and data["Condition"] == []:
            data["Condition"] = {}
        
        # Recurse into nested dicts
        for key in list(data.keys()):
            data[key] = normalize_json(data[key])
    
    elif isinstance(data, list):
        # Recurse into lists
        data = [normalize_json(item) for item in data]
    
    return data


def process_files():
    """Process all 19 target Invoice Detail column files"""
    
    base_path = Path("/Users/mfuller/git/github/FOCUS_Spec/specification/requirements_model/releases/1.4/model_rules/datasets/invoice_detail/columns")
    
    target_files = [
        "billedcost.json",
        "billingaccountid.json",
        "billingcurrency.json",
        "billingperiodend.json",
        "billingperiodstart.json",
        "invoiceissuedate.json",
        "invoicedetailcreated.json",
        "invoicedetaillastupdated.json",
        "paymentduedate.json",
        "invoiceid.json",
        "paymentcurrency.json",
        "paymentcurrencyinvoicedetailid.json",
        "paymentcurrencybilledcost.json",
        "invoiceissuestatus.json",
        "invoicedetaildescription.json",
        "invoicedetailgrain.json",
        "chargecategory.json",
        "purchaseordernumber.json",
        "referenceinvoiceid.json",
    ]
    
    processed = 0
    errors = 0
    
    for filename in target_files:
        filepath = base_path / filename
        
        if not filepath.exists():
            print(f"❌ File not found: {filename}")
            errors += 1
            continue
        
        try:
            # Read JSON
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            # Normalize
            normalized_data = normalize_json(data)
            
            # Write back with nice formatting (2-space indent)
            with open(filepath, 'w') as f:
                json.dump(normalized_data, f, indent=2)
            
            print(f"✓ {filename}")
            processed += 1
            
        except json.JSONDecodeError as e:
            print(f"❌ {filename}: JSON decode error: {e}")
            errors += 1
        except Exception as e:
            print(f"❌ {filename}: {type(e).__name__}: {e}")
            errors += 1
    
    print(f"\nSummary: {processed} files processed, {errors} errors")
    return errors == 0


if __name__ == "__main__":
    success = process_files()
    exit(0 if success else 1)
