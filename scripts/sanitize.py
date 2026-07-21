import argparse
import json
import subprocess
import sys
import tempfile
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
        with open(CONFIG_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError as e:
        print("[ERROR] Invalid configuration file.")
        print(e)
        sys.exit(1)


CONFIG = load_config()

FILTERS = CONFIG["stages"]["sanitize"]["filters"]


# ---------------------------------------------------------
# Execute jq Filter
# ---------------------------------------------------------

def apply_filter(filter_file, input_file, output_file):

    command = [
        "jq",
        "-f",
        filter_file,
        input_file,
    ]

    try:

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
        )

        Path(output_file).write_text(
            result.stdout,
            encoding="utf-8"
        )

    except subprocess.CalledProcessError as e:

        print(f"\n[ERROR] Failed while running filter:")
        print(filter_file)
        print(e.stderr)

        sys.exit(1)


# ---------------------------------------------------------
# Sanitize Pipeline
# ---------------------------------------------------------

def sanitize_json(input_file, output_file):

    Path(output_file).parent.mkdir(
        parents=True,
        exist_ok=True
    )

    current_file = input_file

    temporary_files = []

    for jq_filter in FILTERS:

        temp = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".json"
        )

        temp.close()

        temporary_files.append(temp.name)

        apply_filter(
            jq_filter,
            current_file,
            temp.name,
        )

        current_file = temp.name

    Path(output_file).write_text(
        Path(current_file).read_text(encoding="utf-8"),
        encoding="utf-8"
    )

    # Cleanup temporary files
    for temp_file in temporary_files:

        try:
            Path(temp_file).unlink(missing_ok=True)

        except Exception:
            pass

    print("\n===================================")
    print(" JSON SANITIZATION SUCCESSFUL")
    print("===================================")
    print(f"Input File  : {input_file}")
    print(f"Output File : {output_file}")

    print("\nApplied Filters:")

    for jq_filter in FILTERS:
        print(f"  ✓ {Path(jq_filter).name}")

    print("\nStatus      : PASSED\n")


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Sanitize JSON using configurable jq filters."
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Input JSON"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Output JSON"
    )

    args = parser.parse_args()

    sanitize_json(
        args.input,
        args.output,
    )