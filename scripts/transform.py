import argparse
import json
import os
import sys


def transform_json(input_file, output_file):

    if not os.path.exists(input_file):
        print(f"[ERROR] File not found: {input_file}")
        sys.exit(1)

    with open(input_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Sort components
    if "components" in data:
        data["components"] = sorted(
            data["components"],
            key=lambda x: x.get("component_id", "")
        )

    # Sort servers
    if "servers" in data:
        data["servers"] = sorted(
            data["servers"],
            key=lambda x: x.get("hostname", "")
        )

    # Generate summary
    data["summary"] = {
        "component_count": len(data.get("components", [])),
        "server_count": len(data.get("servers", [])),
        "environment": data.get("project", {}).get("environment", "unknown")
    }

    # Pipeline information
    data["pipeline"] = {
        "processed_by": "GitOps JSON Pipeline",
        "stage": "transform",
        "status": "SUCCESS"
    }

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4
        )

    print("\n===================================")
    print(" JSON TRANSFORMATION SUCCESSFUL")
    print("===================================")
    print(f"Input File  : {input_file}")
    print(f"Output File : {output_file}")
    print("Status      : PASSED\n")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    transform_json(
        args.input,
        args.output
    )