import argparse
import json
import re
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

VERIFY_CONFIG = CONFIG["verification"]

REQUIRED_KEYS = VERIFY_CONFIG["required_root_keys"]

SEMVER_PATTERN = VERIFY_CONFIG["semantic_version_regex"]

CHECKS = VERIFY_CONFIG["checks"]


# ---------------------------------------------------------
# Verification
# ---------------------------------------------------------

def verify_json(input_file):

    input_path = Path(input_file)

    if not input_path.exists():
        print(f"[ERROR] File not found: {input_path}")
        sys.exit(1)

    with input_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    errors = []

    # -----------------------------------------------------
    # Required Root Keys
    # -----------------------------------------------------

    if CHECKS["duplicate_components"] or CHECKS["deployment_stages"]:

        for key in REQUIRED_KEYS:

            if key not in data:
                errors.append(f"Missing root key: {key}")

    # -----------------------------------------------------
    # Duplicate Component IDs
    # -----------------------------------------------------

    if CHECKS["duplicate_components"]:

        component_ids = set()

        for component in data.get("components", []):

            component_id = component.get("component_id")

            if component_id in component_ids:
                errors.append(
                    f"Duplicate component ID: {component_id}"
                )

            component_ids.add(component_id)

    # -----------------------------------------------------
    # Semantic Version Validation
    # -----------------------------------------------------

    if CHECKS["semantic_versions"]:

        for component in data.get("components", []):

            version = component.get("version")

            if version:

                if not re.match(SEMVER_PATTERN, version):

                    errors.append(
                        f"Invalid version '{version}' "
                        f"in component '{component.get('component_id')}'"
                    )

    # -----------------------------------------------------
    # Deployment Stages
    # -----------------------------------------------------

    if CHECKS["deployment_stages"]:

        stages = data.get(
            "deployment",
            {}
        ).get(
            "stages",
            []
        )

        if len(stages) == 0:
            errors.append(
                "Deployment stages are empty"
            )

    # -----------------------------------------------------
    # Report
    # -----------------------------------------------------

    print("\n===================================")
    print(" JSON VERIFICATION REPORT")
    print("===================================")

    if errors:

        for error in errors:
            print(f"✗ {error}")

        print("\nStatus : FAILED\n")

        sys.exit(1)

    print("✓ Required keys exist")

    if CHECKS["duplicate_components"]:
        print("✓ Component IDs unique")

    if CHECKS["semantic_versions"]:
        print("✓ Versions valid")

    if CHECKS["deployment_stages"]:
        print("✓ Deployment stages present")

    print("\nStatus : PASSED\n")


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Verify transformed JSON."
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Input JSON file"
    )

    args = parser.parse_args()

    verify_json(args.input)