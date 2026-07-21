import argparse
import json
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

TRANSFORM = CONFIG["stages"]["transform"]


# ---------------------------------------------------------
# Transformation
# ---------------------------------------------------------

def transform_json(input_file, output_file):

    input_path = Path(input_file)
    output_path = Path(output_file)

    if not input_path.exists():
        print(f"[ERROR] File not found: {input_path}")
        sys.exit(1)

    with input_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    # -----------------------------------------------------
    # Sort Components
    # -----------------------------------------------------

    if TRANSFORM["sort"]["components"]:

        if "components" in data:

            data["components"] = sorted(
                data["components"],
                key=lambda component: component.get(
                    "component_id",
                    ""
                )
            )

    # -----------------------------------------------------
    # Sort Servers
    # -----------------------------------------------------

    if TRANSFORM["sort"]["servers"]:

        if "servers" in data:

            data["servers"] = sorted(
                data["servers"],
                key=lambda server: server.get(
                    "hostname",
                    ""
                )
            )

    # -----------------------------------------------------
    # Summary
    # -----------------------------------------------------

    if TRANSFORM["summary"]["enabled"]:

        data["summary"] = {

            "component_count": len(
                data.get("components", [])
            ),

            "server_count": len(
                data.get("servers", [])
            ),

            "environment": data.get(
                "project",
                {}
            ).get(
                "environment",
                "unknown"
            )
        }

    # -----------------------------------------------------
    # Pipeline Metadata
    # -----------------------------------------------------

    if TRANSFORM["pipeline_metadata"]["enabled"]:

        data["pipeline"] = {

            "processed_by": CONFIG["pipeline"]["name"],

            "version": CONFIG["pipeline"]["version"],

            "stage": "transform",

            "status": "SUCCESS"
        }

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with output_path.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )

    print("\n===================================")
    print(" JSON TRANSFORMATION SUCCESSFUL")
    print("===================================")
    print(f"Input File  : {input_path}")
    print(f"Output File : {output_path}")
    print("Status      : PASSED\n")


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Transform JSON."
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

    transform_json(
        args.input,
        args.output
    )
    