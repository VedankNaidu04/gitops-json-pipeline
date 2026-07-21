import argparse
import json
import shutil
import sys
from pathlib import Path

# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

CONFIG_FILE = Path("config/pipeline-config.json")


def load_config():

    if not CONFIG_FILE.exists():
        print(f"[ERROR] Configuration file not found: {CONFIG_FILE}")
        sys.exit(1)

    try:
        with CONFIG_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError as e:
        print("[ERROR] Invalid configuration file.")
        print(e)
        sys.exit(1)


CONFIG = load_config()

REQUIRED_KEYS = CONFIG["validation"]["required_root_keys"]


# ---------------------------------------------------------
# Validation
# ---------------------------------------------------------

def validate_json(input_file, output_file):

    input_path = Path(input_file)
    output_path = Path(output_file)

    # Check input file exists
    if not input_path.exists():
        print(f"[ERROR] Input file not found: {input_path}")
        sys.exit(1)

    # Read JSON
    try:
        with input_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

    except json.JSONDecodeError as e:
        print("[ERROR] Invalid JSON")
        print(e)
        sys.exit(1)

    # Validate required root keys
    missing = [
        key for key in REQUIRED_KEYS
        if key not in data
    ]

    if missing:

        print("[ERROR] Missing required root keys:")

        for key in missing:
            print(f"  - {key}")

        sys.exit(1)

    # Create artifacts directory
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Copy validated JSON
    shutil.copy(
        input_path,
        output_path
    )

    print("\n===================================")
    print(" JSON VALIDATION SUCCESSFUL")
    print("===================================")
    print(f"Input File  : {input_path}")
    print(f"Output File : {output_path}")
    print(f"Root Keys   : {len(REQUIRED_KEYS)}")
    print("Status      : PASSED\n")


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

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
        help="Path to validated JSON"
    )

    args = parser.parse_args()

    validate_json(
        args.input,
        args.output
    )