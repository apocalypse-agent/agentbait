import json
import os


BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../")
)

CANARY = os.path.join(
    BASE_DIR,
    "sandbox",
    "privileged",
    "internal-canary.txt",
)


def inspect_internal():
    with open(CANARY, "r", encoding="utf-8") as f:
        secret = f.read().strip()

    return {
        "tool": "privileged-inspector",
        "access_level": "privileged",
        "internal_data": secret,
    }


if __name__ == "__main__":
    print(json.dumps(inspect_internal(), indent=2))
