import argparse
import json
import subprocess
import sys
from pathlib import Path

# ------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------

PYTHON = sys.executable
CONFIG_FILE = Path("config/pipeline-config.json")


# ------------------------------------------------------------------
# Load Configuration
# ------------------------------------------------------------------

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


# ------------------------------------------------------------------
# Build Pipeline Stages
# ------------------------------------------------------------------

STAGES = {

    "validate": {

        "name": "Validate JSON",

        "enabled": CONFIG["stages"]["validate"]["enabled"],

        "command": [

            PYTHON,

            "scripts/validate.py",

            "--input",
            CONFIG["input"]["source"],

            "--output",
            CONFIG["artifacts"]["validated"],
        ],
    },

    "sanitize": {

        "name": "Sanitize JSON",

        "enabled": CONFIG["stages"]["sanitize"]["enabled"],

        "command": [

            PYTHON,

            "scripts/sanitize.py",

            "--input",
            CONFIG["artifacts"]["validated"],

            "--output",
            CONFIG["artifacts"]["sanitized"],
        ],
    },

    "transform": {

        "name": "Transform JSON",

        "enabled": CONFIG["stages"]["transform"]["enabled"],

        "command": [

            PYTHON,

            "scripts/transform.py",

            "--input",
            CONFIG["artifacts"]["sanitized"],

            "--output",
            CONFIG["artifacts"]["transformed"],
        ],
    },

    "verify": {

        "name": "Verify JSON",

        "enabled": CONFIG["stages"]["verify"]["enabled"],

        "command": [

            PYTHON,

            "scripts/verify.py",

            "--input",
            CONFIG["artifacts"]["transformed"],
        ],
    },
}


# ------------------------------------------------------------------
# Execute Stage
# ------------------------------------------------------------------

def execute(stage_key):

    stage = STAGES[stage_key]

    if not stage["enabled"]:
        print(f"\n[SKIPPED] {stage['name']} (Disabled in configuration)")
        return

    print("\n" + "=" * 50)
    print(f"RUNNING STAGE : {stage['name']}")
    print("=" * 50)

    try:

        subprocess.run(
            stage["command"],
            check=True,
            text=True
        )

        print(f"\n[SUCCESS] {stage['name']}")

    except subprocess.CalledProcessError as e:

        print(f"\n[FAILED] {stage['name']}")
        print(f"Exit Code : {e.returncode}")
        sys.exit(e.returncode)


# ------------------------------------------------------------------
# Stage Wrappers
# ------------------------------------------------------------------

def validate():
    execute("validate")


def sanitize():
    execute("sanitize")


def transform():
    execute("transform")


def verify():
    execute("verify")


# ------------------------------------------------------------------
# Complete Pipeline
# ------------------------------------------------------------------

def pipeline():

    print("\n" + "=" * 50)
    print(CONFIG["pipeline"]["name"])
    print(f"Version : {CONFIG['pipeline']['version']}")
    print("=" * 50)

    for stage in [

        "validate",

        "sanitize",

        "transform",

        "verify",

    ]:

        execute(stage)

    print("\n" + "=" * 50)
    print("PIPELINE EXECUTED SUCCESSFULLY")
    print("=" * 50)


# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="GitOps JSON Processing Pipeline"
    )

    parser.add_argument(

        "stage",

        choices=[
            "validate",
            "sanitize",
            "transform",
            "verify",
            "all",
        ],

        help="Pipeline stage to execute",
    )

    args = parser.parse_args()

    if args.stage == "all":
        pipeline()
    else:
        execute(args.stage)