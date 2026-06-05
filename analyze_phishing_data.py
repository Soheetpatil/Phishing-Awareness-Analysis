#!/usr/bin/env python3
"""
Phishing Data Analyzer
A simple script to analyze the sample phishing dataset.
"""

import json

def load_dataset(file_path):
    """Load the phishing dataset from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

def analyze_dataset(data):
    """Analyze the phishing dataset."""
    if not data:
        print("No data to analyze.")
        return

    total_samples = len(data)
    attack_types = {}
    all_red_flags = []

    print("=" * 60)
    print("           PHISHING DATASET ANALYSIS")
    print("=" * 60)
    print(f"\nTotal samples: {total_samples}")

    for sample in data:
        # Count attack types
        attack_type = sample['type']
        attack_types[attack_type] = attack_types.get(attack_type, 0) + 1
        
        # Collect all red flags
        all_red_flags.extend(sample['red_flags'])

    print("\nAttack Type Distribution:")
    for attack_type, count in attack_types.items():
        print(f"  {attack_type}: {count} sample(s)")

    print("\nCommon Red Flags:")
    red_flag_counts = {}
    for flag in all_red_flags:
        red_flag_counts[flag] = red_flag_counts.get(flag, 0) + 1
    
    for flag, count in sorted(red_flag_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {flag}: {count} time(s)")

    print("\n" + "=" * 60)
    print("\nDetailed Sample Analysis:")
    print("-" * 60)
    for sample in data:
        print(f"\nSample {sample['id']}:")
        print(f"  Type: {sample['type']}")
        print(f"  Subject: {sample['subject']}")
        print(f"  Red Flags:")
        for flag in sample['red_flags']:
            print(f"    - {flag}")

    print("\n" + "=" * 60)

def main():
    dataset_file = 'sample_phishing_dataset.json'
    data = load_dataset(dataset_file)
    analyze_dataset(data)

if __name__ == "__main__":
    main()

