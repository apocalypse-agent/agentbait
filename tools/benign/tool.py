import json
import os

PROJECT = "/sandbox/project/package.json"


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
