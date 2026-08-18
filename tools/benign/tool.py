import json
import os

PROJECT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../sandbox/project/package.json")
)


def inspect_project():
    with open(PROJECT, "r") as f:
        data = json.load(f)

    return {
        "name": data["name"],
        "version": data["version"],
        "dependencies": data["dependencies"]
    }


if __name__ == "__main__":
    print(json.dumps(inspect_project(), indent=2))
