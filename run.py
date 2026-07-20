import argparse
import subprocess
import sys


def execute(command, stage_name):
    """Execute a pipeline stage."""

    print("\n" + "=" * 50)
    print(f"RUNNING STAGE : {stage_name}")
    print("=" * 50)

    result = subprocess.run(command)

    if result.returncode != 0:
        print(f"\n[FAILED] {stage_name}")
        sys.exit(result.returncode)

    print(f"\n[SUCCESS] {stage_name}")


def validate():
    execute(
        [
            "python",
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
            "python",
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
            "python",
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
            "python",
            "scripts/verify.py",
            "--input",
            "artifacts/transformed.json",
        ],
        "Verify JSON",
    )


def pipeline():
    validate()
    sanitize()
    transform()
    verify()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="GitOps JSON Pipeline")

    parser.add_argument(
        "stage",
        choices=[
            "validate",
            "sanitize",
            "transform",
            "verify",
            "all",
        ],
    )

    args = parser.parse_args()

    if args.stage == "validate":
        validate()

    elif args.stage == "sanitize":
        sanitize()

    elif args.stage == "transform":
        transform()

    elif args.stage == "verify":
        verify()

    elif args.stage == "all":
        pipeline()