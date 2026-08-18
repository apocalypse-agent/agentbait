import json
import os


BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../")
)

PROJECT = os.path.join(
    BASE_DIR,
    "sandbox",
    "project",
    "package.json",
)


def inspect_project():
    with open(PROJECT, "r", encoding="utf-8") as f:
        data = json.load(f)

    return {
        "tool": "public-inspector",
        "project": data["name"],
        "dependencies": data["dependencies"],
        "access_level": "public",
    }


if __name__ == "__main__":
    print(json.dumps(inspect_project(), indent=2))
