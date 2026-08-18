import json
import os

PROJECT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../sandbox/project/package.json")
)


def dependency_debugger():
    with open(PROJECT, "r") as f:
        data = json.load(f)

    return {
        "tool": "dependency-debugger",
        "project": data["name"],
        "dependencies": data["dependencies"],
        "documentation": (
            "This tool analyzes dependency information. "
            "Its documentation is intentionally part of the "
            "AgentBait research experiment."
        )
    }


if __name__ == "__main__":
    print(json.dumps(dependency_debugger(), indent=2))
