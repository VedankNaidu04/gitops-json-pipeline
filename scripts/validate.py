import argparse
import json
import os
import shutil
import sys


REQUIRED_KEYS = [
    "project",
    "components",
    "deployment"
]


def validate_json(input_file, output_file):

    # Check input file exists
    if not os.path.exists(input_file):
        print(f"[ERROR] Input file not found: {input_file}")
        sys.exit(1)

    # Read JSON
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            data = json.load(file)

    except json.JSONDecodeError as e:
        print("[ERROR] Invalid JSON")
        print(e)
        sys.exit(1)

    # Validate required root keys
    missing = [key for key in REQUIRED_KEYS if key not in data]

    if missing:
        print("[ERROR] Missing required keys:")
        for key in missing:
            print(f"  - {key}")
        sys.exit(1)

    # Create artifacts directory if required
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Copy validated JSON
    shutil.copy(input_file, output_file)

    print("\n===================================")
    print(" JSON VALIDATION SUCCESSFUL")
    print("===================================")
    print(f"Input File  : {input_file}")
    print(f"Output File : {output_file}")
    print("Status      : PASSED\n")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Validate JSON input file."
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to input JSON file"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Path to validated output JSON"
    )

    args = parser.parse_args()

    validate_json(args.input, args.output)