import json
import subprocess

TOOLS = {
    "project-inspector": [
        "python",
        "/tools/benign/tool.py"
    ],
    "dependency-debugger": [
        "python",
        "/tools/bait/tool.py"
    ]
}


def run_tool(name):
    result = subprocess.run(
        TOOLS[name],
        capture_output=True,
        text=True
    )

    return result.stdout


def main():
    print("Available tools:")
    for tool in TOOLS:
        print(f"  - {tool}")

    print("\nRunning dependency-debugger...\n")

    output = run_tool("dependency-debugger")

    print(output)


if __name__ == "__main__":
    main()
