import argparse
import subprocess
import sys


PYTHON = sys.executable


def execute(command, stage_name):
    """
    Execute a pipeline stage and terminate on failure.
    """

    print("\n" + "=" * 50)
    print(f"RUNNING STAGE : {stage_name}")
    print("=" * 50)

    try:
        result = subprocess.run(
            command,
            check=True,
            text=True
        )

        print(f"\n[SUCCESS] {stage_name}")

    except subprocess.CalledProcessError as e:

        print(f"\n[FAILED] {stage_name}")
        print(f"Exit Code : {e.returncode}")
        sys.exit(e.returncode)


def validate():
    execute(
        [
            PYTHON,
            "scripts/validate.py",
            "--input",
            "input/sample.json",
            "--output",
            "artifacts/validated.json",
        ],
        "Validate JSON",
    )


def sanitize():
    execute(
        [
            PYTHON,
            "scripts/sanitize.py",
            "--input",
            "artifacts/validated.json",
            "--output",
            "artifacts/result.template.json",
        ],
        "Sanitize JSON",
    )


def transform():
    execute(
        [
            PYTHON,
            "scripts/transform.py",
            "--input",
            "artifacts/result.template.json",
            "--output",
            "artifacts/transformed.json",
        ],
        "Transform JSON",
    )


def verify():
    execute(
        [
            PYTHON,
            "scripts/verify.py",
            "--input",
            "artifacts/transformed.json",
        ],
        "Verify JSON",
    )


def pipeline():
    """
    Execute the complete GitOps JSON Pipeline.
    """

    validate()
    sanitize()
    transform()
    verify()

    print("\n" + "=" * 50)
    print("PIPELINE EXECUTED SUCCESSFULLY")
    print("=" * 50)


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

    stage_functions = {
        "validate": validate,
        "sanitize": sanitize,
        "transform": transform,
        "verify": verify,
        "all": pipeline,
    }

    stage_functions[args.stage]()