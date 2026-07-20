import argparse
import subprocess
import tempfile
import shutil
import os
import sys


FILTERS = [
    "filters/sanitize/remove_nulls.jq",
    "filters/sanitize/remove_metadata.jq",
    "filters/sanitize/remove_duplicates.jq",
    "filters/sanitize/remove_generic_names.jq",
]


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

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(result.stdout)

    except subprocess.CalledProcessError as e:

        print(f"\n[ERROR] Failed while running {filter_file}")
        print(e.stderr)
        sys.exit(1)


def sanitize_json(input_file, output_file):

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    current_file = input_file

    for jq_filter in FILTERS:

        temp = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".json"
        )

        temp.close()

        apply_filter(
            jq_filter,
            current_file,
            temp.name,
        )

        current_file = temp.name

    shutil.copy(current_file, output_file)

    print("\n===================================")
    print(" JSON SANITIZATION SUCCESSFUL")
    print("===================================")
    print(f"Input File  : {input_file}")
    print(f"Output File : {output_file}")
    print("\nApplied Filters:")

    for f in FILTERS:
        print(f"  ✓ {os.path.basename(f)}")

    print("\nStatus      : PASSED\n")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    sanitize_json(
        args.input,
        args.output,
    )