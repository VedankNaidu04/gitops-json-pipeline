import argparse
import json
import os
import re
import sys


SEMVER_PATTERN = r"^\d+\.\d+\.\d+$"


def verify_json(input_file):

    if not os.path.exists(input_file):
        print(f"[ERROR] File not found: {input_file}")
        sys.exit(1)

    with open(input_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    errors = []

    # Required root keys
    for key in ["project", "components", "deployment"]:
        if key not in data:
            errors.append(f"Missing root key: {key}")

    # Duplicate component IDs
    component_ids = []

    for component in data.get("components", []):
        cid = component.get("component_id")

        if cid in component_ids:
            errors.append(f"Duplicate component ID: {cid}")

        component_ids.append(cid)

    # Version validation
    for component in data.get("components", []):

        version = component.get("version")

        if version:

            if not re.match(SEMVER_PATTERN, version):
                errors.append(
                    f"Invalid version '{version}' in {component.get('component_id')}"
                )

    # Deployment stages
    if "deployment" in data:

        stages = data["deployment"].get("stages", [])

        if len(stages) == 0:
            errors.append("Deployment stages are empty")

    print("\n===================================")
    print(" JSON VERIFICATION REPORT")
    print("===================================")

    if errors:

        for error in errors:
            print(f"✗ {error}")

        print("\nStatus : FAILED\n")
        sys.exit(1)

    print("✓ Required keys exist")
    print("✓ Component IDs unique")
    print("✓ Versions valid")
    print("✓ Deployment stages present")

    print("\nStatus : PASSED\n")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True)

    args = parser.parse_args()

    verify_json(args.input)